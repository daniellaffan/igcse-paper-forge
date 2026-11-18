# Verification of the generated papers

For each of the 10 subjects, one **topic test** and one **full paper in the real structure** were generated from the **live site's data** (https://daniellaffan.github.io/igcse-paper-forge/), both PDFs (question paper and mark scheme) were produced, opened and checked, and the full paper was compared side by side with a real paper from the private corpus.

## How it was done (no browser)

At Dan's request no web browser (headless or otherwise) was used. Instead `scripts/verify/offline/`:

1. `build.mjs` bundles the site's **own** code — `assemble.ts` (the test builder) and `Documents.tsx` (the paper and mark-scheme components) — with esbuild; KaTeX output is swapped for MathJax SVG so formulas can be drawn without a browser.
2. `entry.mjs <site-url> docs/verification` downloads `index.json`, each subject's `spec.json`/`bank.json` and the reference sheets from the live site, assembles each paper exactly as the site does (same config and seed → same questions as the site link in `offline-build.json`), and renders both documents to HTML.
3. `render.py` lays the HTML out on A4 with PyMuPDF, page by page as the site's paginator does (blocks packed greedily, headings kept with what follows), adds the footer (disclaimer · paper code · seed · page), then checks every PDF: page size A4, disclaimer on every page, every "Total for Question" line present, no screen-only controls, no raw markup.
4. `scripts/verify/compare.py` puts the first pages next to a real corpus paper. Those images contain copyrighted pages, so they stay in the gitignored `docs/verification/compare/`.

Re-run:

```bash
node scripts/verify/offline/build.mjs
node scripts/verify/offline/.out/entry.mjs https://daniellaffan.github.io/igcse-paper-forge/ docs/verification
.venv/bin/python scripts/verify/offline/render.py docs/verification
.venv/bin/python scripts/verify/compare.py docs/verification
```

## Results

| Subject | Paper | Questions | Marks | QP pages | MS pages | Formulas | Diagrams | Audio | EITHER/OR | Reference sheet | A4 + disclaimer every page |
|---|---|---|---|---|---|---|---|---|---|---|---|
| maths | topic-test | 10 | 30/30 | 9 | 4 | 62 | 0 | 0 | 0 | maths-formulae-higher | yes |
| maths | full-paper | 30 | 100/100 | 25 | 10 | 160 | 7 | 0 | 0 | maths-formulae-higher | yes |
| further-maths | topic-test | 7 | 30/30 | 9 | 4 | 74 | 0 | 0 | 0 | further-maths-formulae | yes |
| further-maths | full-paper | 16 | 100/100 | 18 | 9 | 176 | 1 | 0 | 0 | further-maths-formulae | yes |
| physics | topic-test | 7 | 30/30 | 8 | 4 | 29 | 1 | 0 | 0 | physics-equations | yes |
| physics | full-paper | 30 | 110/110 | 22 | 10 | 29 | 1 | 0 | 0 | physics-equations | yes |
| chemistry | topic-test | 13 | 30/30 | 9 | 4 | 0 | 0 | 0 | 0 | chemistry-periodic-table | yes |
| chemistry | full-paper | 46 | 110/110 | 23 | 11 | 0 | 3 | 0 | 0 | chemistry-periodic-table | yes |
| biology | topic-test | 14 | 30/30 | 9 | 4 | 0 | 1 | 0 | 0 | – | yes |
| biology | full-paper | 37 | 110/110 | 24 | 9 | 0 | 8 | 0 | 0 | – | yes |
| economics | topic-test | 11 | 30/30 | 8 | 4 | 0 | 0 | 0 | 0 | – | yes |
| economics | full-paper | 22 | 80/80 | 14 | 10 | 0 | 2 | 0 | 0 | – | yes |
| history | topic-test | 3 | 28/30 | 8 | 4 | 0 | 0 | 0 | 0 | – | yes |
| history | full-paper | 8 | 60/60 | 17 | 8 | 0 | 0 | 0 | 4 | – | yes |
| english-language | topic-test | 6 | 29/30 | 14 | 5 | 0 | 0 | 0 | 0 | – | yes |
| english-language | full-paper | 2 | 90/90 | 11 | 7 | 0 | 0 | 0 | 0 | – | yes |
| english-literature | topic-test | 1 | 30/30 | 6 | 4 | 0 | 0 | 0 | 0 | – | yes |
| english-literature | full-paper | 5 | 90/90 | 18 | 11 | 0 | 0 | 0 | 4 | – | yes |
| spanish | topic-test | 4 | 27/30 | 7 | 6 | 0 | 0 | 5 | 0 | – | yes |
| spanish | full-paper | 6 | 40/40 | 11 | 7 | 0 | 0 | 7 | 0 | – | yes |

Each subject folder holds the four PDFs and PNG previews of their first pages (`<paper>-qp-pN.png`, `<paper>-ms-pN.png`).

## What the side-by-side comparison showed, and what was fixed

- **Diagram labels clipped** (axis titles, "24 cm" shown as "4 cm", Sankey "wasted"): 122 questions in 16 templates. Fixed for the whole bank in `scripts/gen/common.py` (`Bank.save` grows each diagram's drawing area to fit every label); `scripts/qc/svg_bounds.py` now finds 0.
- **Units before the answer dots** ("cm ........"): 570 answer lines in 41 maths templates moved to after the dots ("........ cm") as on real papers; `svg_bounds.py` checks this too (0 left).
- **"You must have: You must have:"** on maths/physics/biology/further-maths covers: fixed in `Cover.tsx`.
- **Raw `**` in text**: English Language insert references and English Literature indicative content (bold containing italics) printed the markup; fixed in `rich.tsx` and `QuestionBlocks.tsx`.
- **Periodic table wider than the page** (18 columns): many-column tables now use a compact fixed layout (`table.data.wide`).
- Formula sheet / periodic table / equation list page appears after the cover for maths, further maths, physics and chemistry, as on the real papers.

## Checked by eye on the previews

- Maths and Further Maths: formulas render (MathJax SVG from the same LaTeX the site gives KaTeX); diagrams and graphs display with all labels.
- Sciences and Economics: diagrams, tables, MCQ boxes, ruled answer lines sized to the marks, "(Total for Question N is M marks)".
- History: extracts boxed with provenance, EITHER/OR choices; English Language: insert with numbered lines, Section A/B; English Literature: sections, poems in the insert, EITHER/OR.
- Spanish: listening questions with the recording box; play buttons and transcripts are screen-only and correctly absent from the PDF.

## Limits of a browser-free check

- **Spanish listening** (`spanish/listening-check.json`, `scripts/verify/offline/listening.jsx`): the site's own
  `<Speaker>` component was mounted in jsdom (a DOM emulator in Node, not a browser) for **every one of the 1,495
  listening recordings (1,287 questions)** in the live bank. For each: the ▶ button is enabled, clicking it sends the whole
  transcript to the Web Speech API **twice** with a pause between (as in the real exam), every utterance is `es-ES` with a
  Spanish voice, the spoken text equals the transcript, the button becomes ■ Stop and resets when playback ends, and
  "Show transcript" shows it. **1,495 / 1,495 passed.** Then one transcript was spoken by macOS's own Spanish (Spain) voice,
  the same system voices Safari and Chrome use for speech synthesis on a Mac: `spanish/listening-sample.m4a`
  (35.6 s of audio). What a browser-free check cannot do is hear the browser play it; that last step needs a browser.
- The PDFs here are laid out by PyMuPDF from the site's own components, not by the site's jsPDF/html2canvas export (that export draws the page with the browser's layout engine, so it cannot run without a browser), so fonts and exact line breaks differ slightly from a PDF downloaded from the site; content, order, numbering and pagination rules are the same.
- Known difference from real papers: science full papers draw from a bank of mostly short questions, so e.g. Chemistry 1C has ~46 numbered questions where a real paper has ~11 longer multi-part ones (decision for Dan in the final notes).

## Left to Dan (his decision, 18 Nov 2026)

Because no browser may be used, two checks are Dan's to do by hand on the live site:

1. Open any Spanish paper with a listening question and press **▶ Play recording**: it should speak in Spanish, twice.
2. On any paper, click **Download question paper (PDF)** and **Download mark scheme (PDF)**: two separate A4 PDFs, each
   with "Practice paper — not an official exam board paper" in the footer of every page.
