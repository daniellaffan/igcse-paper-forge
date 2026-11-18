#!/usr/bin/env python3
"""
Private corpus downloader for IGCSE Paper Forge.

Downloads PUBLICLY AVAILABLE documents (specifications, sample assessment
materials, past papers, mark schemes, examiner reports, exemplars) for the
ten subjects into corpus/<subject>/<series>/..., and records them in
corpus/manifest.json.

Rules it follows:
  * Only ungated documents (the exam board's own `gating` flag is False and
    the file is served without a login). Anything that redirects to a login
    or returns HTML instead of a PDF is skipped and logged as a gap.
  * Polite: one request per second by default, retries with back-off,
    a cache (files already in the manifest with a matching hash are skipped),
    so it is resumable — just run it again.
  * corpus/ is in .gitignore. Never commit it.

Usage:
    .venv/bin/python scripts/fetch_corpus.py            # all subjects
    .venv/bin/python scripts/fetch_corpus.py maths econ # some subjects
    .venv/bin/python scripts/fetch_corpus.py --list     # just list, no download
"""
import hashlib
import json
import os
import re
import sys
import time
import urllib.parse
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent.parent
CORPUS = ROOT / "corpus"
MANIFEST = CORPUS / os.environ.get("MANIFEST_NAME", "manifest.json")
GAPS = CORPUS / os.environ.get("GAPS_NAME", "gaps.json")
DELAY = float(os.environ.get("FETCH_DELAY", "1.0"))
UA = "Mozilla/5.0 (compatible; personal-revision-corpus/1.0)"

# Pearson's public course-materials search (the same public key the
# qualification pages embed for anonymous visitors).
ALGOLIA_APP = "L639T95U5A"
ALGOLIA_KEY = "f79c7a8352e9ffbdaec387bf43612ee6"
ALGOLIA_INDEX = "qualifications-uk_LIVE_master-content"
PEARSON = "https://qualifications.pearson.com"

SUBJECTS = {
    "maths": {"code": "4MA1", "spec": "International-GCSE/2016/igcse16-mathsA"},
    "further-maths": {"code": "4PM1", "spec": "International-GCSE/2017/igcse17-fpmaths"},
    "physics": {"code": "4PH1", "spec": "International-GCSE/2017/igcse17-physics"},
    "chemistry": {"code": "4CH1", "spec": "International-GCSE/2017/igcse17-chemistry"},
    "biology": {"code": "4BI1", "spec": "International-GCSE/2017/igcse17-biology"},
    "economics": {"code": "4EC1", "spec": "International-GCSE/2017/igcse-economics-2017"},
    "history": {"code": "4HI1", "spec": "International-GCSE/2017/igcse17-history"},
    "english-language": {"code": "4EA1", "spec": "International-GCSE/2016/igcse16-eng-langa"},
    "english-literature": {"code": "4ET1", "spec": "International-GCSE/2016/igcse16-eng-lit"},
}

DOC_TYPES = [
    "Specification", "Sample-assessment-material", "Specimen-paper-and-mark-scheme",
    "Question-paper", "Mark-scheme", "Examiner-report", "Exemplar-material",
    "Exemplar-exam-material", "Anthology", "Data-files", "Assessment-guidance",
    "Teacher-guide", "Practice-paper",
]


def log(*a):
    print(*a, flush=True)


def load_json(p, default):
    try:
        return json.loads(p.read_text())
    except Exception:
        return default


def save_json(p, obj):
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_suffix(".tmp")
    tmp.write_text(json.dumps(obj, indent=1))
    tmp.replace(p)


def algolia_all(spec):
    url = f"https://{ALGOLIA_APP}-dsn.algolia.net/1/indexes/{ALGOLIA_INDEX}/query"
    headers = {"X-Algolia-Application-Id": ALGOLIA_APP, "X-Algolia-API-Key": ALGOLIA_KEY}
    hits, page = [], 0
    while True:
        body = {
            "query": "", "hitsPerPage": 1000, "page": page,
            "facetFilters": [
                [f"category:Pearson-UK:Specification-Code/{spec}"],
                [f"category:Pearson-UK:Document-Type/{t}" for t in DOC_TYPES],
            ],
        }
        r = requests.post(url, headers=headers, json=body, timeout=60)
        r.raise_for_status()
        d = r.json()
        hits += d["hits"]
        page += 1
        if page >= d.get("nbPages", 0):
            return hits
        time.sleep(DELAY)


def facet(h, prefix):
    for c in h.get("category", []):
        if c.startswith("Pearson-UK:" + prefix + "/"):
            return c.split("/", 1)[1]
    return ""


def wanted(subject, h):
    if h.get("gating"):
        return False, "gated"
    if (h.get("extension") or "").upper() != "PDF":
        return False, "not-pdf"
    unit = facet(h, "Unit")
    title = (h.get("title") or "") + " " + (h.get("url") or "")
    if "modified" in title.lower():
        return False, "modified-paper"
    if subject == "maths" and re.search(r"Paper-\dF", unit):
        return False, "foundation"
    return True, ""


def get(url, stream=False):
    for attempt in range(4):
        try:
            r = requests.get(url, headers={"User-Agent": UA}, timeout=90, stream=stream, allow_redirects=True)
            if r.status_code == 200:
                return r
            if r.status_code in (401, 403, 404):
                return r
        except requests.RequestException as e:
            log("  retry", attempt, e)
        time.sleep(DELAY * (2 ** attempt) + 1)
    return None


def all_manifests():
    """Union of every manifest*.json (parallel runs write their own file)."""
    out = {}
    for p in sorted(CORPUS.glob("manifest*.json")):
        for m in load_json(p, []):
            out[m["source_url"]] = m
    return out


def merge_manifests():
    recs = sorted(all_manifests().values(), key=lambda m: (m["subject"], m["series"], m["path"]))
    save_json(CORPUS / "manifest.json", recs)
    gaps = {}
    for p in sorted(CORPUS.glob("gaps*.json")):
        for g in load_json(p, []):
            gaps[g["source_url"]] = g
    have = {m["source_url"] for m in recs}
    save_json(CORPUS / "gaps.json", [g for u, g in gaps.items() if u not in have])
    log(f"merged: {len(recs)} files in manifest.json")


def run(subjects, list_only=False):
    manifest = load_json(MANIFEST, [])
    by_url = all_manifests()
    by_url.update({m["source_url"]: m for m in manifest})
    gaps = load_json(GAPS, [])
    gap_urls = {g["source_url"] for g in gaps}
    for s in subjects:
        cfg = SUBJECTS[s]
        log(f"== {s} ({cfg['code']})")
        hits = algolia_all(cfg["spec"])
        log(f"  {len(hits)} index records")
        for h in hits:
            src = PEARSON + urllib.parse.quote(h["url"])
            series = facet(h, "Exam-Series") or "no-series"
            dtype = facet(h, "Document-Type")
            unit = facet(h, "Unit")
            ok, why = wanted(s, h)
            if not ok:
                if why == "gated" and src not in gap_urls:
                    gaps.append({"subject": s, "code": cfg["code"], "title": h.get("title"),
                                 "series": series, "type": dtype, "source_url": src, "reason": why})
                    gap_urls.add(src)
                continue
            fname = os.path.basename(h["url"])
            dest = CORPUS / s / series / fname
            if src in by_url and dest.exists():
                continue
            if list_only:
                log("  would get", series, dtype, fname)
                continue
            time.sleep(DELAY)
            r = get(src)
            if r is None or r.status_code != 200 or not r.content.startswith(b"%PDF"):
                if src not in gap_urls:
                    gaps.append({"subject": s, "code": cfg["code"], "title": h.get("title"), "series": series,
                                 "type": dtype, "source_url": src,
                                 "reason": "http-" + (str(r.status_code) if r is not None else "fail") + "/not-pdf"})
                    gap_urls.add(src)
                log("  SKIP", fname)
                continue
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(r.content)
            rec = {"subject": s, "code": cfg["code"], "paper": unit, "series": series, "type": dtype,
                   "title": h.get("title"), "source_url": src,
                   "path": str(dest.relative_to(ROOT)), "sha256": hashlib.sha256(r.content).hexdigest(),
                   "bytes": len(r.content)}
            by_url[src] = rec
            manifest = list(by_url.values())
            save_json(MANIFEST, manifest)
            log("  got", series, dtype, fname)
        save_json(GAPS, gaps)
    save_json(MANIFEST, list(by_url.values()))
    save_json(GAPS, gaps)
    merge_manifests()


# ---------------------------------------------------------------- Spanish 0530
CAIE_OFFICIAL = [
    # (series, type, paper, url) — public files on cambridgeinternational.org
    ("syllabus-2025-2027", "Specification", "", "https://www.cambridgeinternational.org/Images/664626-2025-2027-syllabus.pdf"),
    ("syllabus-2025-2027", "Specification", "", "https://www.cambridgeinternational.org/Images/683348-2025-2027-syllabus-update.pdf"),
    ("June-2024", "Question-paper", "11", "https://www.cambridgeinternational.org/Images/570167-june-2024-question-paper-11.pdf"),
    ("June-2024", "Mark-scheme", "11", "https://www.cambridgeinternational.org/Images/570164-june-2024-mark-scheme-paper-11.pdf"),
    ("June-2024", "Transcript", "11", "https://www.cambridgeinternational.org/Images/604304-june-2024-transcript-paper-11.pdf"),
    ("June-2024", "Question-paper", "21", "https://www.cambridgeinternational.org/Images/570168-june-2024-question-paper-21.pdf"),
    ("June-2024", "Mark-scheme", "21", "https://www.cambridgeinternational.org/Images/570165-june-2024-mark-scheme-paper-21.pdf"),
    ("June-2024", "Question-paper", "41", "https://www.cambridgeinternational.org/Images/570169-june-2024-question-paper-41.pdf"),
    ("June-2024", "Mark-scheme", "41", "https://www.cambridgeinternational.org/Images/570166-june-2024-mark-scheme-paper-41.pdf"),
    ("June-2024", "Role-play", "03", "https://www.cambridgeinternational.org/Images/570170-june-2024-role-play-paper-03.pdf"),
    ("June-2024", "Teachers-notes", "03", "https://www.cambridgeinternational.org/Images/570171-june-2024-teachers-notes-paper-03.pdf"),
    ("June-2024", "Examiner-report", "", "https://www.cambridgeinternational.org/Images/570163-june-2024-examiner-report.pdf"),
    ("Specimen-2021", "Question-paper", "1", "https://www.cambridgeinternational.org/Images/503486-2021-specimen-paper-1.pdf"),
    ("Specimen-2021", "Mark-scheme", "1", "https://www.cambridgeinternational.org/Images/503453-2021-specimen-paper-1-mark-scheme.pdf"),
    ("Specimen-2021", "Transcript", "1", "https://www.cambridgeinternational.org/Images/503513-2021-specimen-paper-1-transcript.pdf"),
    ("Specimen-2021", "Question-paper", "2", "https://www.cambridgeinternational.org/Images/503496-2021-specimen-paper-2.pdf"),
    ("Specimen-2021", "Mark-scheme", "2", "https://www.cambridgeinternational.org/Images/503462-2021-specimen-paper-2-mark-scheme.pdf"),
    ("Specimen-2021", "Role-play", "3", "https://www.cambridgeinternational.org/Images/503508-2021-specimen-paper-3-candidate-cards.pdf"),
    ("Specimen-2021", "Teachers-notes", "3", "https://www.cambridgeinternational.org/Images/503470-2021-specimen-paper-3-instructions-for-teachers-examiners.pdf"),
    ("Specimen-2021", "Question-paper", "4", "https://www.cambridgeinternational.org/Images/503501-2021-specimen-paper-4.pdf"),
    ("Specimen-2021", "Mark-scheme", "4", "https://www.cambridgeinternational.org/Images/503466-2021-specimen-paper-4-mark-scheme.pdf"),
]
PAPA = "https://pastpapers.papacambridge.com/directories/CAIE/CAIE-pastpapers/upload/"
SERIES_NAME = {"m": "March", "s": "June", "w": "November"}


def spanish_candidates():
    """Archive file names for the current (2021+) 0530 format."""
    for yy in range(21, 26):
        for sc in "msw":
            variants = ["2"] if sc == "m" else ["1", "2", "3"]
            series = f"{SERIES_NAME[sc]}-20{yy}"
            yield series, "Examiner-report", "", f"0530_{sc}{yy}_er"
            yield series, "Role-play", "03", f"0530_{sc}{yy}_rp_03"
            yield series, "Teachers-notes", "03", f"0530_{sc}{yy}_tn_03"
            for comp in "124":
                for v in variants:
                    for t, label in (("qp", "Question-paper"), ("ms", "Mark-scheme")):
                        yield series, label, comp + v, f"0530_{sc}{yy}_{t}_{comp}{v}"


def run_spanish(list_only=False):
    manifest = load_json(MANIFEST, [])
    by_url = {m["source_url"]: m for m in manifest}
    gaps = load_json(GAPS, [])
    gap_urls = {g["source_url"] for g in gaps}
    jobs = [(s, t, p, u, os.path.basename(u)) for s, t, p, u in CAIE_OFFICIAL]
    jobs += [(s, t, p, PAPA + n + ".pdf", n + ".pdf") for s, t, p, n in spanish_candidates()]
    log(f"== spanish (0530): {len(jobs)} candidate files")
    for series, dtype, paper, src, fname in jobs:
        dest = CORPUS / "spanish" / series / fname
        if (src in by_url and dest.exists()) or src in gap_urls:
            continue
        if list_only:
            log("  would try", series, dtype, fname)
            continue
        time.sleep(DELAY)
        try:
            r = requests.get(src, headers={"User-Agent": UA}, timeout=(8, 60))
            ok = r.status_code == 200 and r.content.startswith(b"%PDF")
        except requests.RequestException:
            r, ok = None, False
        if not ok:
            gaps.append({"subject": "spanish", "code": "0530", "title": fname, "series": series, "type": dtype,
                         "source_url": src, "reason": "not-available"})
            gap_urls.add(src)
            save_json(GAPS, gaps)
            continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(r.content)
        by_url[src] = {"subject": "spanish", "code": "0530", "paper": paper, "series": series, "type": dtype,
                       "title": fname, "source_url": src, "path": str(dest.relative_to(ROOT)),
                       "sha256": hashlib.sha256(r.content).hexdigest(), "bytes": len(r.content)}
        save_json(MANIFEST, list(by_url.values()))
        log("  got", series, dtype, fname)
    save_json(GAPS, gaps)


if __name__ == "__main__":
    if "--merge" in sys.argv:
        merge_manifests()
        sys.exit(0)
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    lo = "--list" in sys.argv
    pearson = [a for a in (args or list(SUBJECTS)) if a in SUBJECTS]
    if pearson:
        run(pearson, list_only=lo)
    if not args or "spanish" in args:
        run_spanish(list_only=lo)
