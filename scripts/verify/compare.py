#!/usr/bin/env python3
"""
Side-by-side comparison of generated PDFs with a real paper from the private corpus.

  .venv/bin/python scripts/verify/compare.py docs/verification

For each subject folder in docs/verification/ it renders pages 1-3 of the
generated full-paper question paper and mark scheme next to pages 1-3 of a real
question paper / mark scheme from corpus/<subject>/, and writes
docs/verification/compare/<subject>-qp.png and -ms.png.

The compare/ folder contains images of copyrighted exam papers, so it is
git-ignored and stays on this computer only.
It also writes docs/verification/pdf_check.json (page counts, page size, text found).
"""
import json
import sys
from pathlib import Path

import fitz  # PyMuPDF

ROOT = Path(__file__).resolve().parents[2]


def real_paper(subject: str, kind: str):
    pats = {"qp": ["*que*", "*_qp_*"], "ms": ["*msc*", "*rms*", "*_ms_*", "*-ms-*"]}[kind]
    files = []
    for p in pats:
        files += list((ROOT / "corpus" / subject).rglob(p + ".pdf"))
    files = [f for f in files if "insert" not in f.name.lower() and "ins" not in f.stem.lower().split("_")]
    return sorted(files, key=lambda f: f.stat().st_size, reverse=True)[0] if files else None


def render(pdf: Path, pages=3, zoom=0.9):
    doc = fitz.open(pdf)
    out = []
    for i in range(min(pages, len(doc))):
        out.append(doc[i].get_pixmap(matrix=fitz.Matrix(zoom, zoom)))
    return out


def strip(images, label_top, label_bottom, path: Path):
    tops, bots = images
    w = max(sum(p.width for p in tops), sum(p.width for p in bots)) + 40
    h = max((p.height for p in tops), default=0) + max((p.height for p in bots), default=0) + 120
    doc = fitz.open()
    page = doc.new_page(width=w, height=h)
    page.insert_text((10, 30), label_top, fontsize=18)
    x = 10
    for p in tops:
        page.insert_image(fitz.Rect(x, 40, x + p.width, 40 + p.height), pixmap=p)
        x += p.width + 10
    y = 40 + max((p.height for p in tops), default=0) + 40
    page.insert_text((10, y - 10), label_bottom, fontsize=18)
    x = 10
    for p in bots:
        page.insert_image(fitz.Rect(x, y, x + p.width, y + p.height), pixmap=p)
        x += p.width + 10
    page.get_pixmap(matrix=fitz.Matrix(0.6, 0.6)).save(path)


def check_pdf(pdf: Path):
    doc = fitz.open(pdf)
    r = doc[0].rect
    return {"file": pdf.name, "pages": len(doc), "a4": abs(r.width - 595.3) < 2 and abs(r.height - 841.9) < 2,
            "title": doc.metadata.get("title"), "subject": doc.metadata.get("subject")}


def main():
    out = Path(sys.argv[1] if len(sys.argv) > 1 else ROOT / "docs" / "verification")
    cmp = out / "compare"
    cmp.mkdir(parents=True, exist_ok=True)
    report = {}
    for d in sorted(p for p in out.iterdir() if p.is_dir() and p.name != "compare"):
        s = d.name
        report[s] = {"pdfs": [check_pdf(f) for f in sorted(d.glob("*.pdf"))]}
        for kind, ours in (("qp", d / "full-paper-question-paper.pdf"), ("ms", d / "full-paper-mark-scheme.pdf")):
            real = real_paper(s, kind)
            if not ours.exists() or not real:
                report[s][kind] = "missing " + ("generated" if not ours.exists() else "corpus") + " file"
                continue
            strip((render(ours), render(real)), f"GENERATED  {s} {ours.name}", f"REAL (private corpus)  {real.name}",
                  cmp / f"{s}-{kind}.png")
            report[s][kind] = {"compared_with": str(real.relative_to(ROOT))}
        print(s, json.dumps(report[s])[:300])
    (out / "pdf_check.json").write_text(json.dumps(report, indent=1))


if __name__ == "__main__":
    main()
