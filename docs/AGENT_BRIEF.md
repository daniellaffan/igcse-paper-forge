# Brief for a subject builder

You are building one subject of **IGCSE Paper Forge**: a static website that turns a large, original, committed question bank into exam-style practice papers and mark schemes. Project root: the repository root. Read `GOAL.md` (sections 2–5) and `docs/DATA_FORMAT.md` first. The student is Dan (IGCSE exams May 2027).

## What you have

* `corpus_text/<subject>/<series>/*.txt` — extracted text of the official spec, sample assessment materials, past papers, mark schemes, examiner reports, exemplars (PRIVATE, git-ignored; `corpus/manifest.json` lists the source PDFs). Some downloads may still be arriving; re-list the folder before you finish. If the PDF is there but text is missing, run `.venv/bin/python scripts/extract_text.py`.
* `data/schema/question.schema.json`, `data/schema/spec.schema.json`.
* `scripts/gen/common.py` — `Bank` class, `row()`, `levels()`, `fmt_num()` helpers. Import with `sys.path.insert(0, 'scripts/gen')`.
* `scripts/validate_bank.py <subject>` and `scripts/similarity_check.py <subject>`.
* Python: `.venv/bin/python` (sympy, pymupdf, jsonschema, rapidfuzz installed). No network needed; do not download anything.

## What you must produce (all inside the project)

1. **`style-guides/<subject>.md`** — from studying the corpus (quote nothing longer than a few words; describe in your own words):
   paper anatomy (sections, number of questions, mark totals, timing, cover rubric, margin/footer furniture); every question type with mark tariff, command words, stem patterns, typical contexts, how difficulty ramps; how the mark scheme is written (point tables answer/notes/marks, M/A/B, ECF, accept/reject/ignore, levels grids with descriptors and indicative content, AO splits); what examiner reports say separates strong and weak answers and common errors; topic frequency (how often each spec area appears, in what form — count it from the papers).
2. **`data/spec/<subject>.json`** — valid against `spec.schema.json`. Tree: topics → subtopics → points with the **official spec reference numbers** and a **one-line plain-English summary in your own words** (never the spec's wording). Each subtopic lists the `qtypes` that genuinely can test it. `papers[]` must have the real paper code, minutes, marks, calculator flag, and cover-page `instructions`, `information` and `advice` lines in the board's style (paraphrased), plus `sections` (with `slots` for subjects whose papers have a fixed question order — History, English, Economics, Spanish; maths and science papers mix topics, so omit slots there). `official_url` = the board's official qualification/past-papers page. If the paper prints a formula sheet, periodic table or data page, write it as `data/reference/<id>.json` (`{"id","title","blocks":[figure objects]}`) in your own layout and set `reference_sheet` on the paper.
3. **`scripts/gen/<subject>.py`** (plus helper modules `scripts/gen/<subject>_*.py` if you like) — a deterministic generator (seeded RNG) that writes `data/bank/<subject>/<topic>.json` via `Bank.save()`. Hand-authored content (passages, extracts, knowledge bases, contexts) goes in `data/content/<subject>/*.json` or inside the generator — your choice, but it must all be original or genuinely public domain with provenance recorded.
4. **`docs/notes/<subject>.md`** — short: spec facts you confirmed (code, papers, timings, marks, option names), anything that disagrees with GOAL.md section 2, corpus gaps you noticed, and the final counts.

Do **not** edit shared files (`common.py`, the validators, schemas, `GOAL.md`, the site). If you need a schema change, say so in your notes file and work within the current schema.

## Scale and coverage (hard requirements — the validator enforces them)

* Every subtopic × each qtype listed for it: **at least 12 questions**. Only list qtypes that are realistic for that subtopic.
* Subject minimum totals: maths, further-maths, physics, chemistry, biology, economics ≥ 1,500 each; spanish ≥ 1,200 across the four skills; history ≥ 150 per option (4 options); english-language and english-literature ≥ 400 each. Go beyond where the topic is broad.
* Spread of difficulty bands `1-3`, `4-6`, `7-9` that matches real papers.

## Quality bar

* Indistinguishable in style, difficulty and mark allocation from real questions. Reuse formats, never wording, numbers, contexts or sources from the corpus. `similarity_check.py` must flag nothing.
* Variety: parameterised templates are fine (and necessary for scale), but each template must produce genuinely different questions (different numbers AND rotating contexts/wording), and you need many templates per subtopic. A paper built from the bank must not feel repetitive.
* **Every numerical / algebraic answer is computed in code** (sympy or exact arithmetic) and stored in `answer: {"method": "...", "values": {...}, "checked": true}`; the mark scheme is built from the same computed values. Check units and significant figures.
* Mark schemes in the board's format: maths M1/A1/B1 with method notes, `oe`, `cao`, `ft`, alternative methods; sciences point tables with accept/reject/ignore notes, `allow ecf`; levels-based grids (level, marks, descriptor) with indicative content and `credit_note` for extended answers.
* `marks` = sum of part marks; for each leaf part, mark-scheme row marks sum to the part's marks (an "any two from" list is ONE row with marks "2"); levels-marked parts are covered by a `levels` entry with the same `part` label.
* Answer space sized to the marks (`lines`, or `space: "working"` + `answer_prefix` for maths).
* Figures: SVG with a `viewBox`, black `stroke`/`fill` (`currentColor` is fine), no external references, no fonts other than generic `serif`/`sans-serif`, accurate where the board's are accurate; add `note: "Diagram NOT accurately drawn"` where the board does. Graph paper grids for plotting questions.
* Never reproduce copyrighted text (anthology texts, *Of Mice and Men*, modern poems, published articles). Public-domain texts (author died 70+ years ago, published before 1929 in the US) may be printed with `provenance`; otherwise write originals.
* Do not name the exam board in question text. Do not claim to be official.

## Definition of done for your subject

`.venv/bin/python scripts/validate_bank.py <subject>` prints OK, `.venv/bin/python scripts/similarity_check.py <subject>` flags nothing, the style guide and notes exist. Reply with: counts, number of templates, anything you could not do, and anything that needs the lead's decision. Keep the reply under 300 words.
