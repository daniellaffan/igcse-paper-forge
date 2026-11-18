#!/usr/bin/env python3
"""
Check that no question text is copied from the private corpus.

  .venv/bin/python scripts/similarity_check.py [subject ...]

Method: every corpus text file for the subject is cut into overlapping
8-word shingles (hashed). Shingles that appear in 4+ different corpus
documents are treated as exam boilerplate ("Give your answer correct to 3
significant figures", "Total for Question 3 is 4 marks") and ignored — reusing
the board's *format* is allowed. Each question's text (stem, parts, sources,
passages, mark-scheme answers) is shingled the same way. A question is FLAGGED
if it shares a run of 5+ consecutive non-boilerplate shingles (about 12 words
copied in a row) or more than 15% of its shingles with one corpus document.

Writes data/bank/qc/similarity.json with ids and scores only (never corpus text).
Needs corpus_text/ (run extract_text.py first). Exits 1 if anything is flagged.
"""
import json
import re
import sys
import zlib
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEXT = ROOT / "corpus_text"
BANK = ROOT / "data" / "bank"
N = 8
RUN_FLAG = 5
RATIO_FLAG = 0.15
BOILER_DOCS = 4

WORD = re.compile(r"[a-záéíóúñü0-9]+")


def words(t):
    return WORD.findall(t.lower())


def shingles(ws):
    return [zlib.crc32(" ".join(ws[i:i + N]).encode()) for i in range(max(0, len(ws) - N + 1))]


def q_text(q):
    out = [q.get("intro", "")]

    def walk(ps):
        for p in ps:
            out.append(p.get("text", ""))
            out.extend(p.get("choices", []) or [])
            walk(p.get("parts", []) or [])
    walk(q["parts"])
    for f in (q.get("figures") or []):
        out += [f.get("text", ""), f.get("transcript", "")]
    ms = q["markscheme"]
    out += [r.get("answer", "") for r in ms.get("rows", [])]
    for lv in ms.get("levels", []) or []:
        out += lv.get("indicative", [])
    return " \n ".join(x for x in out if x)


def main():
    subjects = sys.argv[1:] or sorted(p.name for p in BANK.iterdir() if p.is_dir() and p.name != "qc")
    if not TEXT.exists():
        print("corpus_text/ missing: run scripts/extract_text.py first")
        sys.exit(2)
    report = {"method": __doc__.strip().splitlines()[2:12], "subjects": {}}
    any_flag = False
    for s in subjects:
        docs = sorted((TEXT / s).rglob("*.txt")) if (TEXT / s).exists() else []
        doc_of = defaultdict(set)
        for di, d in enumerate(docs):
            for h in set(shingles(words(d.read_text(errors="ignore")))):
                doc_of[h].add(di)
        boiler = {h for h, ds in doc_of.items() if len(ds) >= BOILER_DOCS}
        flagged, checked, worst = [], 0, 0.0
        for f in sorted((BANK / s).glob("*.json")):
            for q in json.loads(f.read_text()):
                checked += 1
                sh = shingles(words(q_text(q)))
                if not sh:
                    continue
                per_doc = defaultdict(int)
                run, best_run = 0, 0
                for h in sh:
                    if h in doc_of and h not in boiler:
                        run += 1
                        for di in doc_of[h]:
                            per_doc[di] += 1
                    else:
                        run = 0
                    best_run = max(best_run, run)
                ratio = max(per_doc.values()) / len(sh) if per_doc else 0.0
                worst = max(worst, ratio)
                if best_run >= RUN_FLAG or ratio > RATIO_FLAG:
                    flagged.append({"id": q["id"], "longest_run_shingles": best_run, "max_doc_overlap": round(ratio, 3)})
        report["subjects"][s] = {"corpus_docs": len(docs), "checked": checked, "flagged": len(flagged),
                                 "worst_overlap": round(worst, 3), "flagged_ids": flagged[:200]}
        any_flag |= bool(flagged)
        print(f"{s}: {checked} checked against {len(docs)} corpus docs, {len(flagged)} flagged, worst overlap {worst:.3f}")
    (BANK / "qc").mkdir(parents=True, exist_ok=True)
    out = BANK / "qc" / "similarity.json"
    old = json.loads(out.read_text()) if out.exists() else {"subjects": {}}
    old["subjects"].update(report["subjects"])
    old["method"] = report["method"]
    out.write_text(json.dumps(old, indent=1))
    sys.exit(1 if any_flag else 0)


if __name__ == "__main__":
    main()
