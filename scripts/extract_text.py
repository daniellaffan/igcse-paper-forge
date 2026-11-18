#!/usr/bin/env python3
"""
Extract text from every PDF in corpus/ into corpus_text/ (both git-ignored).

  .venv/bin/python scripts/extract_text.py

Uses PyMuPDF's text layer. Pages with no text layer (scans) are OCR'd with
Tesseract if it is installed (PyMuPDF's OCR bridge); otherwise they are listed
in corpus_text/needs_ocr.json. Resumable: skips PDFs already extracted with
the same hash.
"""
import hashlib
import json
import shutil
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parent.parent
CORPUS = ROOT / "corpus"
OUT = ROOT / "corpus_text"
HAVE_TESS = shutil.which("tesseract") is not None


def main():
    OUT.mkdir(exist_ok=True)
    index_p = OUT / "index.json"
    index = json.loads(index_p.read_text()) if index_p.exists() else {}
    needs_ocr = []
    pdfs = sorted(CORPUS.rglob("*.pdf"))
    for i, pdf in enumerate(pdfs):
        rel = str(pdf.relative_to(CORPUS))
        h = hashlib.sha256(pdf.read_bytes()).hexdigest()
        dest = OUT / (rel[:-4] + ".txt")
        if index.get(rel, {}).get("sha256") == h and dest.exists():
            r = index[rel]
            if r.get("empty_pages") and r["empty_pages"] >= r.get("pages", 0) // 2:
                needs_ocr.append(rel)
            continue
        try:
            doc = pymupdf.open(pdf)
        except Exception as e:
            print("cannot open", rel, e)
            continue
        pages, empty = [], 0
        for page in doc:
            t = page.get_text("text")
            if len(t.strip()) < 20:
                if HAVE_TESS:
                    try:
                        tp = page.get_textpage_ocr(full=True)
                        t = page.get_text("text", textpage=tp)
                    except Exception:
                        pass
                if len(t.strip()) < 20:
                    empty += 1
            pages.append(t)
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text("\n\f\n".join(pages))
        if empty and empty >= len(pages) // 2:
            needs_ocr.append(rel)
        index[rel] = {"sha256": h, "pages": len(pages), "empty_pages": empty, "chars": sum(map(len, pages))}
        if i % 50 == 0:
            print(i, "/", len(pdfs), rel, flush=True)
            index_p.write_text(json.dumps(index, indent=1))
    index_p.write_text(json.dumps(index, indent=1))
    (OUT / "needs_ocr.json").write_text(json.dumps(needs_ocr, indent=1))
    print("done", len(index), "files;", len(needs_ocr), "mostly image-only")


if __name__ == "__main__":
    main()
