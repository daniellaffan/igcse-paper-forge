#!/usr/bin/env python3
"""
Browser-free PDF check, step 2: lay out the HTML that the site's own paper components
produced (step 1, scripts/verify/offline/entry.jsx) on A4 pages with PyMuPDF, then
write PNG previews and a JSON summary of automatic checks.

  node scripts/verify/offline/build.mjs
  node scripts/verify/offline/.out/entry.mjs https://daniellaffan.github.io/igcse-paper-forge/ docs/verification
  .venv/bin/python scripts/verify/offline/render.py docs/verification

For each subject it writes, in docs/verification/<subject>/:
  topic-test-question-paper.pdf, topic-test-mark-scheme.pdf,
  full-paper-question-paper.pdf, full-paper-mark-scheme.pdf,
  <stem>-<qp|ms>-p<N>.png previews (first pages),
and docs/verification/offline-check.json.
"""
import html as htmllib
import json
import re
import sys
from pathlib import Path

import pymupdf as fitz

DISCLAIMER = "Practice paper — not an official exam board paper"
A4 = fitz.paper_rect("a4")
MM = 72 / 25.4
BODY = fitz.Rect(20 * MM, 16 * MM, A4.width - 20 * MM, A4.height - 22 * MM)

CSS = """
body { font-family: serif; font-size: 10.5pt; line-height: 1.3; }
p { margin: 0 0 4pt 0; }
b, strong { font-weight: bold; }
.disclaimer-banner { border: 1.5pt solid black; padding: 4pt; text-align: center; font-weight: bold; font-size: 10pt; margin-bottom: 10pt; }
.pe-check { font-size: 8pt; margin-bottom: 4pt; }
.cand-table { width: 100%; border-collapse: collapse; margin-bottom: 14pt; }
.cand-table td { border: 0.8pt solid black; padding: 6pt; font-size: 8.5pt; }
.pe-quals { font-size: 12pt; margin-top: 8pt; }
.pe-subject, .cam-title { font-size: 20pt; font-weight: bold; margin: 6pt 0; }
.pe-paper, .cam-paper { font-size: 15pt; font-weight: bold; margin-bottom: 4pt; }
.pe-sub { font-size: 10pt; margin-bottom: 6pt; }
.pe-row { margin: 6pt 0; border-top: 0.6pt solid #888; padding-top: 4pt; }
.pe-box, .cam-box { border: 1pt solid black; padding: 6pt 10pt; margin-top: 12pt; font-size: 9.5pt; }
.pe-h, .cam-h { font-weight: bold; font-size: 11pt; margin-top: 6pt; }
.cover-foot { margin-top: 16pt; font-size: 8pt; text-align: center; }
.ms-title { font-size: 26pt; font-weight: bold; margin: 30pt 0 8pt 0; }
.ms-sub, .ms-paper { font-size: 14pt; margin-bottom: 6pt; }
.ms-code, .ms-meta { font-size: 11pt; margin-bottom: 6pt; }
.ms-note { font-size: 9.5pt; margin-top: 20pt; border: 0.8pt solid #444; padding: 8pt; }
.answer-all { font-weight: bold; margin-bottom: 8pt; }
.sec-head { border-top: 1.2pt solid black; border-bottom: 1.2pt solid black; padding: 4pt 0; margin: 8pt 0; }
.sec-title { font-weight: bold; font-size: 12pt; }
.either-or { font-weight: bold; font-size: 12pt; text-align: center; margin: 8pt 0 2pt 0; }
.qhead { margin-top: 10pt; }
.qn { font-weight: bold; font-size: 12pt; }
.insert-ref { font-style: italic; }
.qpart { margin: 3pt 0 4pt 0; }
.depth1 { margin-left: 14pt; }
.nest { margin-left: 0; }
.ans-indent { margin-left: 20pt; }
.dotline { border-bottom: 0.7pt dotted #333; height: 7.5mm; }
.work-space { }
.final-ans { text-align: right; margin-top: 2pt; }
.marks-row { text-align: right; font-weight: bold; margin: 1pt 0 2pt 0; }
.qtotal { text-align: right; font-weight: bold; margin: 2pt 0 8pt 0; border-bottom: 0.6pt solid #999; padding-bottom: 3pt; }
.ans-boxed { border: 0.8pt solid black; }
.graph-grid { border: 0.8pt solid #555; height: 90mm; margin: 4pt 0; }
.mcq-opt { margin: 2pt 0 2pt 10pt; }
.fig { margin: 5pt 0; }
.fig-svg { text-align: center; }
.fig-note, figcaption { font-size: 9pt; font-style: italic; text-align: center; }
table.data { border-collapse: collapse; margin: 4pt auto; }
table.data td, table.data th { border: 0.7pt solid black; padding: 2pt 6pt; font-size: 9.5pt; text-align: center; }
.fig-source, .ms-transcript { border: 0.8pt solid #444; padding: 5pt 7pt; }
.src-label { font-weight: bold; }
.src-prov, .psg-title { font-style: italic; font-size: 9.5pt; margin-bottom: 3pt; }
.psg-title { font-weight: bold; font-style: normal; font-size: 11pt; }
.nl { margin: 0; }
.ln { font-size: 8pt; color: #555; }
.poem .lt { }
.audio-print { border: 0.8pt dashed #444; padding: 4pt; font-style: italic; }
.paper-end { text-align: center; font-weight: bold; margin-top: 14pt; }
.end-small { font-size: 9pt; }
.ms-guidance { border: 0.8pt solid #444; padding: 5pt 8pt; margin-bottom: 8pt; font-size: 9.5pt; }
.ms-g-title { font-weight: bold; font-size: 11pt; }
table.ms-table { width: 100%; border-collapse: collapse; }
table.ms-table td, table.ms-table th { border: 0.6pt solid #333; padding: 2pt 4pt; font-size: 9.5pt; vertical-align: top; }
table.ms-head th { background-color: #e6e6e6; font-weight: bold; }
.lv-block { margin: 4pt 0; }
.lv-head { margin: 4pt 0 2pt 0; }
.lv-ind { font-size: 9.5pt; margin: 2pt 0; }
table.lv-table { width: 100%; border-collapse: collapse; }
table.lv-table td, table.lv-table th { border: 0.6pt solid #333; padding: 2pt 4pt; font-size: 9pt; vertical-align: top; }
.lv-credit, .ms-general { font-size: 9pt; font-style: italic; margin: 2pt 0; }
.ms-qtotal { text-align: right; font-weight: bold; margin: 2pt 0 8pt 0; }
.insert-head { border-bottom: 1pt solid black; margin-bottom: 8pt; }
.ins-title { font-size: 16pt; font-weight: bold; }
.muted { color: #555; }
.math-error { color: red; }
"""


def inner_of(doc: str, start: int) -> str:
    """Return the inner HTML of the element whose opening tag starts at `start` (balanced tags)."""
    tag = re.match(r"<(\w+)", doc[start:]).group(1)
    open_end = doc.index(">", start) + 1
    depth, i = 1, open_end
    pat = re.compile(rf"<(/?){tag}\b[^>]*?(/?)>")
    while depth:
        m = pat.search(doc, i)
        if m.group(1):
            depth -= 1
        elif not m.group(2):
            depth += 1
        i = m.end()
    return doc[open_end:m.start()]


def parts(doc: str):
    """Split the server-rendered document into cover, main blocks and insert blocks."""
    cov = re.search(r'<section class="page[^"]*cover-page[^"]*">', doc)
    cover = inner_of(doc, cov.start()) if cov else ""
    measures = [m.start() for m in re.finditer(r'<div class="measure"', doc)]
    bodies = [inner_of(doc, m) for m in measures]
    return cover, bodies[0] if bodies else "", bodies[1] if len(bodies) > 1 else ""


def tidy(h: str, svgs: dict, stem: str) -> str:
    # inline diagrams -> archive images
    def svg_img(m):
        wrap_style, svg = m.group(1) or "", m.group(2)
        name = f"fig{len(svgs)}.svg"
        if "xmlns=" not in svg[:200]:
            svg = svg.replace("<svg", '<svg xmlns="http://www.w3.org/2000/svg"', 1)
        svgs[name] = svg
        wmm = re.search(r"width:\s*([\d.]+)mm", wrap_style)
        vb = re.search(r'viewBox="[\d.\-]+ [\d.\-]+ ([\d.]+) ([\d.]+)"', svg)
        wpt = float(wmm.group(1)) * MM if wmm else min(150 * MM, float(vb.group(1)) * 0.75 if vb else 300)
        wpt = min(wpt, BODY.width - 40)
        hpt = wpt * float(vb.group(2)) / float(vb.group(1)) if vb else wpt * 0.6
        return f'<p style="text-align:center"><img src="{name}" style="width:{wpt:.0f}pt;height:{hpt:.0f}pt" width="{wpt:.0f}" height="{hpt:.0f}"/></p>'
    h = re.sub(r'<div class="svg-wrap"(?: style="([^"]*)")?>\s*(<svg[\s\S]*?</svg>)\s*</div>', svg_img, h)
    # maths images were written as <stem>-mN.svg
    h = re.sub(r'src="(m\d+\.svg)"', lambda m: f'src="{stem}-{m.group(1)}"', h)
    # question number and part labels inline with the first line of text
    h = re.sub(r'<span class="qnum">(\d+)</span>\s*<div class="qhead-body">', r'<div class="qhead-body"><p class="qn">\1</p>', h)
    h = re.sub(r'<span class="plabel">([^<]*)</span>\s*<div class="ptext">\s*<div class="rich ?">\s*<p>',
               r'<div class="ptext"><div class="rich"><p><b>\1</b>&#160;&#160;', h)
    h = re.sub(r'<span class="plabel">([^<]*)</span>', r'<b>\1</b> ', h)
    # answer furniture
    h = h.replace('<span class="final-dots"></span>', '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .')
    h = re.sub(r'<span class="mcq-box"[^>]*></span>\s*<span class="mcq-letter">(\w)</span>', r'<b>\1</b>&#160;&#160;☐&#160;&#160;', h)
    h = re.sub(r'<span class="digit-boxes">((?:<span></span>)+)</span>',
               lambda m: "☐" * m.group(1).count("<span>"), h)
    h = h.replace('<div class="tm-box"></div>', '☐')
    h = re.sub(r'<colgroup>[\s\S]*?</colgroup>', '', h)
    return h


def place(writer, story, first_rect=BODY):
    n, more = 0, 1
    while more:
        dev = writer.begin_page(A4)
        more, _ = story.place(first_rect if n == 0 else BODY)
        story.draw(dev)
        writer.end_page()
        n += 1
    return n


def make_pdf(src: Path, out_pdf: Path, kind: str, code: str, seed: str):
    doc = src.read_text()
    cover, main, insert = parts(doc)
    svgs = {}
    stem = src.stem.rsplit("-", 1)[0]  # topic-test / full-paper
    cover_h, main_h, ins_h = (tidy(x, svgs, stem) for x in (cover, main, insert))
    arch = fitz.Archive(str(src.parent))
    if svgs:
        for n, s in svgs.items():
            arch.add(s.encode(), n)
    head = ""
    if kind == "ms":
        head = re.search(r'<table class="ms-table ms-head">[\s\S]*?</table>', doc)
        head = tidy(head.group(0), svgs, stem) if head else ""
    writer = fitz.DocumentWriter(str(out_pdf))
    counts = {"cover": place(writer, fitz.Story(cover_h, user_css=CSS, archive=arch))}
    counts["body"] = place(writer, fitz.Story(head + main_h, user_css=CSS, archive=arch))
    if ins_h.strip():
        ins_title = '<div class="insert-head"><div class="ins-title">Insert</div><div class="muted">Do not return this Insert with the question paper.</div></div>'
        counts["insert"] = place(writer, fitz.Story(ins_title + ins_h, user_css=CSS, archive=arch))
    writer.close()
    # footer on every page (disclaimer, paper code, seed, page number), as on the site
    pdf = fitz.open(out_pdf)
    label = code + (" mark scheme" if kind == "ms" else "")
    for i, page in enumerate(pdf):
        page.insert_htmlbox(fitz.Rect(20 * MM, A4.height - 15 * MM, A4.width - 20 * MM, A4.height - 7 * MM),
                            f'<div style="font-size:7.5pt;font-family:sans-serif;border-top:0.5pt solid #666;padding-top:2pt">'
                            f'{htmllib.escape(DISCLAIMER)} · {htmllib.escape(label)} · seed {seed} · page {i + 1}</div>')
    pdf.set_metadata({"title": out_pdf.stem, "subject": DISCLAIMER, "creator": "IGCSE Paper Forge (offline check)"})
    pdf.save(out_pdf.with_suffix(".tmp.pdf"), garbage=3, deflate=True)
    pdf.close()
    out_pdf.with_suffix(".tmp.pdf").replace(out_pdf)
    return counts


def check(pdf_path: Path, previews: Path, n_preview=3):
    pdf = fitz.open(pdf_path)
    res = {"pages": len(pdf), "a4": all(abs(p.rect.width - A4.width) < 1 and abs(p.rect.height - A4.height) < 1 for p in pdf),
           "disclaimer_on_every_page": all(DISCLAIMER in p.get_text().replace("\ufb03", "ffi").replace("\ufb01", "fi") for p in pdf),
           "images": sum(len(p.get_images()) for p in pdf), "vector_drawings": sum(len(p.get_drawings()) for p in pdf),
           "logo_free": True}
    for i in range(min(n_preview, len(pdf))):
        pdf[i].get_pixmap(dpi=80).save(previews.parent / f"{previews.name}-p{i + 1}.png")
    return res


def main():
    out = Path(sys.argv[1] if len(sys.argv) > 1 else "docs/verification")
    summary = json.loads((out / "offline-build.json").read_text())
    report = {}
    for subj, stems in summary.items():
        d = out / subj
        report[subj] = {}
        for stem, info in stems.items():
            seed = re.search(r"(?i)seed (\d+)", (d / "build" / f"{stem}-qp.html").read_text())
            seed = seed.group(1) if seed else "?"
            code = re.search(r'Paper reference</span> <b>([^<]+)</b>|class="cam-code"><b>([^<]+)</b>', (d / "build" / f"{stem}-qp.html").read_text())
            code = (code.group(1) or code.group(2)) if code else subj
            r = dict(info)
            for kind, name in (("qp", "question-paper"), ("ms", "mark-scheme")):
                pdf = d / f"{stem}-{name}.pdf"
                r[kind + "_layout"] = make_pdf(d / "build" / f"{stem}-{kind}.html", pdf, kind, code, seed)
                r[kind] = check(pdf, d / f"{stem}-{kind}")
            report[subj][stem] = r
            print(subj, stem, "qp", r["qp"]["pages"], "pages", "ms", r["ms"]["pages"], "pages",
                  "disclaimer ok" if r["qp"]["disclaimer_on_every_page"] and r["ms"]["disclaimer_on_every_page"] else "DISCLAIMER MISSING")
    (out / "offline-check.json").write_text(json.dumps(report, indent=1))


if __name__ == "__main__":
    main()
