#!/usr/bin/env python3
"""
Write docs/CORPUS_GAPS.md from corpus/manifest.json and corpus/gaps*.json.

  .venv/bin/python scripts/corpus_report.py

Only file names, series and public URLs go into the report, no exam content.
"""
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
C = ROOT / "corpus"
ORDER = ["maths", "further-maths", "physics", "chemistry", "biology", "economics", "history",
         "english-language", "english-literature", "spanish"]


def main():
    man = json.loads((C / "manifest.json").read_text())
    gaps = []
    seen = set()
    for f in sorted(C.glob("gaps*.json")):
        for g in json.loads(f.read_text()):
            k = g["source_url"]
            if k not in seen:
                seen.add(k)
                gaps.append(g)
    got = {e["source_url"] for e in man}
    gaps = [g for g in gaps if g["source_url"] not in got]
    skipped = defaultdict(list)  # gated ("secure") files the downloader skipped on purpose
    for log in sorted(ROOT.glob("corpus_fetch*.log")):
        for line in log.read_text().splitlines():
            m = re.match(r"\s+SKIP (\S+)", line)
            if m:
                skipped[m.group(1)[:4].lower()].append(m.group(1))

    have = defaultdict(Counter)
    series = defaultdict(set)
    for e in man:
        have[e["subject"]][e["type"]] += 1
        series[e["subject"]].add(e["series"])
    L = ["# Corpus gaps", "",
         "The private corpus (`corpus/`, never committed) holds the past papers, mark schemes, examiner reports",
         "and specifications that were **freely downloadable without logging in**. This page lists what is in it",
         "and what could not be downloaded. Regenerate with `.venv/bin/python scripts/corpus_report.py`.", "",
         f"Total files downloaded: **{len(man)}**.", "",
         "## What was downloaded", "",
         "| Subject | Files | Series covered | Breakdown |", "|---|---|---|---|"]
    for s in ORDER:
        if s not in have:
            L.append(f"| {s} | 0 | – | – |")
            continue
        ss = sorted(series[s], key=lambda x: (x[-4:], x))
        rng = f"{ss[0]} … {ss[-1]}" if ss else "–"
        brk = ", ".join(f"{k.replace('-', ' ')}: {v}" for k, v in have[s].most_common())
        L.append(f"| {s} | {sum(have[s].values())} | {len(ss)} ({rng}) | {brk} |")
    L += ["", "## What could not be downloaded", "",
          "### 1. Login-protected (\"secure\") Pearson files — not attempted",
          "Pearson keeps the most recent exam series (typically the last 1–2 series, e.g. November 2025 and",
          "June 2026) behind a login for teachers and exams officers. The goal forbids bypassing logins, so these",
          "were skipped. Examiner reports for recent series are also locked. They become public over time;",
          "re-running `scripts/fetch_corpus.py` later will pick them up.", ""]
    by_subj = defaultdict(list)
    for g in gaps:
        by_subj[g["subject"]].append(g)
    for s in ORDER:
        if s == "spanish":
            continue
        rows = by_subj.get(s, [])
        if not rows:
            continue
        L.append(f"**{s}** — {len(rows)} locked file(s):")
        for g in sorted(rows, key=lambda g: g["title"]):
            L.append(f"- {g['title']} ({g['type'].replace('-', ' ')})")
        L.append("")
    L += ["### 2. Cambridge 0530 Spanish",
          "Cambridge's own site only offers a sample of recent papers; the remaining 2021–2025 papers, mark schemes,",
          "role-play cards and teacher notes came from a public past-paper archive. These files were not found anywhere public:", ""]
    for g in sorted(by_subj.get("spanish", []), key=lambda g: g["title"]):
        L.append(f"- {g['title']} ({g['type'].replace('-', ' ')}, {g['series']})")
    L += ["", "Listening **audio recordings** are not published as files with the papers, so none were downloaded;",
          "the listening transcripts in the question papers / teacher notes were used for style instead.",
          "The 2025–2027 syllabus PDF could not be fetched by the script (the site blocks scripted downloads),",
          "so the syllabus content was taken from the official syllabus web page and earlier syllabus copies.", "",
          "### 3. Image-only PDFs",
          "A handful of PDFs contain scanned images rather than text. No OCR tool was available on this computer",
          "(installing Tesseract needs admin rights), so those were used only by eye, not by the similarity checker.", ""]
    if (ROOT / "corpus_text" / "needs_ocr.json").exists():
        for p in json.loads((ROOT / "corpus_text" / "needs_ocr.json").read_text()):
            L.append(f"- {Path(p).name if isinstance(p, str) else p}")
        L.append("")
    L += ["## Manual download (optional)",
          "If you (or a teacher) have a Pearson login, you can download the locked files yourself and drop them",
          "into `corpus/<subject>/<series>/`, then run `.venv/bin/python scripts/extract_text.py`. Nothing in",
          "`corpus/` is ever committed, so this stays private.", ""]
    (ROOT / "docs" / "CORPUS_GAPS.md").write_text("\n".join(L))
    print("wrote docs/CORPUS_GAPS.md", len(gaps), "gaps")


if __name__ == "__main__":
    main()
