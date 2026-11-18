#!/usr/bin/env python3
"""
Pack data/spec + data/bank + data/reference into site/public/data/ for the website.

  python scripts/build_site_data.py

Output:
  site/public/data/index.json               subject list with counts
  site/public/data/<subject>/spec.json      spec + per-subtopic counts
  site/public/data/<subject>/bank.json      every question for the subject
  site/public/data/reference/<id>.json      formula sheets / data pages
Only original material is copied — nothing from corpus/.
"""
import json
import shutil
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "site" / "public" / "data"
ORDER = ["maths", "further-maths", "physics", "chemistry", "biology", "economics", "history",
         "english-language", "english-literature", "spanish"]


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    index = []
    for s in ORDER:
        sp = ROOT / "data" / "spec" / f"{s}.json"
        bd = ROOT / "data" / "bank" / s
        if not sp.exists():
            continue
        spec = json.loads(sp.read_text())
        qs = []
        for f in sorted(bd.glob("*.json")) if bd.exists() else []:
            qs += json.loads(f.read_text())
        for q in qs:  # trim generator-only fields the site does not need
            q.pop("answer", None) if not q.get("answer", {}).get("values") else None
        counts = defaultdict(lambda: {"total": 0, "byType": defaultdict(int)})
        for q in qs:
            c = counts[q["subtopic"]]
            c["total"] += 1
            c["byType"][q["qtype"]] += 1
        spec["counts"] = counts
        (OUT / s).mkdir()
        (OUT / s / "spec.json").write_text(json.dumps(spec, ensure_ascii=False, separators=(",", ":")))
        (OUT / s / "bank.json").write_text(json.dumps(qs, ensure_ascii=False, separators=(",", ":")))
        index.append({"subject": s, "title": spec.get("short") or spec["title"], "code": spec["code"],
                      "board": spec["board"], "questions": len(qs),
                      "papers": [{"id": p["id"], "name": p["name"]} for p in spec["papers"]]})
        print(f"{s}: {len(qs)} questions, {(OUT / s / 'bank.json').stat().st_size // 1024} KB")
    (OUT / "index.json").write_text(json.dumps(index, ensure_ascii=False, indent=1))
    ref = ROOT / "data" / "reference"
    (OUT / "reference").mkdir()
    for f in ref.glob("*.json") if ref.exists() else []:
        shutil.copy(f, OUT / "reference" / f.name)
    print(f"index: {len(index)} subjects, {sum(i['questions'] for i in index)} questions")


if __name__ == "__main__":
    main()
