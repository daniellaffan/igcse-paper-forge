# GOAL: IGCSE Paper Forge — a practice paper generator website

You are building this for Dan, an IGCSE student (exams from May 2027) who can read code but does not write it. Work autonomously until every item in "Definition of done" is true. Do not stop to ask questions unless a step is impossible without him (for example a GitHub login); in that case give him the exact command to run and carry on with everything else.

## 1. What the finished thing is

A public GitHub repo and a live static website (GitHub Pages) where Dan can:

1. Pick a subject and see a **simplified specification checklist** (every topic and sub-topic, in plain language, mapped to the official spec reference numbers).
2. Tick the sub-topics he wants, choose **how long** the test is (by total marks or by minutes), choose **which question types** to include, and choose difficulty.
3. Get a **target-style test** that looks and reads like a real exam paper for that subject, plus a **separate mark scheme** in the exam board's style.
4. Download both as **two separate PDFs** (question paper, mark scheme).

There is no live AI on the site and no API key. Every question comes from a very large bank that you write during this build and commit as data.

## 2. Subjects and exact scope

Before writing anything, download the current specification for each subject and confirm the codes, paper structure, timings, marks and option names below. If anything here disagrees with the spec, the spec wins; record the difference in `docs/SCOPE_NOTES.md`.

| Subject | Board and code | Scope |
|---|---|---|
| Mathematics | Pearson Edexcel International GCSE 4MA1 | Higher tier, Papers 1H and 2H (assumed Higher; build Foundation only if trivial) |
| Further Pure Mathematics | Pearson Edexcel International GCSE 4PM1 | Papers 1 and 2 |
| Physics | Pearson Edexcel International GCSE 4PH1 | Separate science, Papers 1 and 2 (include Paper 2-only content, clearly tagged) |
| Chemistry | Pearson Edexcel International GCSE 4CH1 | Separate science, Papers 1 and 2 |
| Biology | Pearson Edexcel International GCSE 4BI1 | Separate science, Papers 1 and 2 |
| Economics | Pearson Edexcel International GCSE 4EC1 | Papers 1 and 2 |
| History | Pearson Edexcel International GCSE 4HI1 | Only Dan's four options, see below |
| English Language A | Pearson Edexcel International GCSE 4EA1 | Paper 1 only: non-fiction reading and transactional writing |
| English Literature | Pearson Edexcel International GCSE 4ET1 | Paper 1 only: unseen poetry, anthology poetry, modern prose = *Of Mice and Men* only |
| Spanish | **Cambridge** IGCSE 0530 (not Edexcel) | Listening, Reading, Speaking, Writing |

**History options.** Dan described them as: depth studies "Hitler's rise to power" and "global superpowers / Cold War"; and for Paper 2 "Civil War America" and "Communist Russia". The expected mapping is below, but verify each against the spec option list and note it in `SCOPE_NOTES.md`:
- Paper 1 depth: *Germany: development of dictatorship, 1918–45* and *A world divided: superpower relations, 1943–72*.
- Paper 2 Section A (source-based historical investigation): *Russia and the Soviet Union, 1905–24*.
- Paper 2 Section B (breadth study in change): *America: from new nation to divided union, 1783–1877*.
Paper 2 is one investigation plus one breadth study, so these two use different question formats. Build each in its own format.

**English.** Components 3 (coursework) for both English subjects are out of scope: do not generate coursework. For Language Paper 1, Section A uses an unseen non-fiction passage plus an anthology text, and Section B is transactional writing. For Literature Paper 1, Section C questions are on *Of Mice and Men* only.

## 3. Phase 1 — collect the source corpus (learning material, kept private)

Collect **everything publicly available** for each subject: specifications, sample assessment materials, every past question paper, every mark scheme, examiner reports, exemplar/graded student responses, data booklets, formula sheets, anthologies, and for Spanish the listening transcripts.

Rules:
- Official sources first: `qualifications.pearson.com` and `cambridgeinternational.org`. Fill gaps from free public past-paper archives.
- Never bypass a login, paywall or teacher-only lock. The most recent series are often locked; skip them and list them in `docs/CORPUS_GAPS.md`.
- Be polite: rate-limit, cache, retry, and make the downloader resumable (`scripts/fetch_corpus.*`).
- Save to `corpus/<subject>/<year-series>/...` with a `corpus/manifest.json` (subject, code, paper, series, type, source URL, file hash).
- **`corpus/` must be in `.gitignore` and must never be pushed.** These documents are copyright Pearson and Cambridge. The public repo and site contain only original material plus links to the official pages.
- If automated download is blocked, write `docs/MANUAL_DOWNLOAD.md` with direct links so Dan can drop files into `corpus/` himself, and continue with what you have.

Extract text from every PDF (OCR where needed) so it can be analysed.

## 4. Phase 2 — learn how each paper works

For every subject and paper, study the corpus and write `style-guides/<subject>.md` covering:
- Paper anatomy: sections, number of questions, mark totals, timing, rubric wording, what is printed on the cover and in the margins.
- Every **question type** with its mark tariff, command words, stem patterns, typical contexts, and how difficulty ramps through the paper.
- How the **mark scheme** is written: point-marked tables (answer / notes / marks), M/A/B marks in maths, ECF and "accept/reject/ignore" conventions, **levels-based grids** with level descriptors and indicative content, assessment objective splits.
- What examiner reports say separates strong from weak answers, and common errors.
- Topic frequency: how often each spec point appears and in what form.

Also produce the simplified spec as data: `data/spec/<subject>.json`, a tree of paper → topic → sub-topic → spec points, each with the official reference, a one-line plain-English summary, and the question types that can test it.

## 5. Phase 3 — write the question bank (this must be HUGE)

Write original questions that are indistinguishable in style, difficulty and mark allocation from real ones. Do not copy real questions; reuse their formats, not their wording, numbers or sources.

**Scale targets (minimums):**
- Every sub-topic has at least 12 questions for each question type that can test it.
- Maths, Further Pure, Physics, Chemistry, Biology, Economics: at least 1,500 questions each.
- Spanish: at least 1,200 across the four skills.
- History: at least 150 questions per option (600 total), covering every question format.
- English Language and English Literature: at least 400 each.
- Whole bank: at least 12,000 questions. Keep going past the minimums where a topic is broad.

**Every question record** (`data/bank/<subject>/<topic>.json`, validated by a JSON schema) has: id, subject, paper, spec references, sub-topic, question type, command word, marks, difficulty band (grades 1–3, 4–6, 7–9), estimated minutes, question body (with parts), any figure/table/source, the **full mark scheme** in the board's format, assessment objectives, and for levels-marked questions the full level grid plus indicative content and the line that other valid points are credited.

**Subject-specific requirements:**
- Maths / Further Pure: KaTeX for all notation; diagrams as accurate SVG ("diagram NOT accurately drawn" where the board does that); mark schemes with M1/A1/B1 and alternative methods. Solve every question with code (e.g. SymPy) and store the checked answer.
- Sciences: calculations, practical/required-experiment questions, data and graph questions, 6-mark extended responses; SVG diagrams, graphs and apparatus; correct units and significant figures; verify all numerical answers with code.
- Economics: multiple choice, define/state, calculate, diagram questions (supply and demand etc. as SVG), data-response with an original extract, and the 6-, 9- and 12-mark analyse/assess/evaluate questions with levels grids.
- History: each option's real formats (e.g. inference from an extract, explain two effects/causes, source utility and cross-referencing, interpretation questions, 16-mark judgement essays). Write original period-accurate extracts or use genuinely public-domain sources, each with provenance.
- English Language: write original non-fiction passages (articles, speeches, memoir, travel writing, letters) of the right length and difficulty for the unseen text. Refer to Pearson anthology texts by title only, never reproduce them. Section B: transactional tasks with form, audience and purpose.
- English Literature: unseen poetry using public-domain poems or original poems you write; anthology questions name the poems (print the text only if public domain); *Of Mice and Men* essay questions on character, theme, setting and context with indicative content. Do not print copyrighted extracts.
- Spanish (Cambridge 0530): reading and writing tasks in the real formats; listening tasks with original Spanish transcripts played through the browser's Spanish text-to-speech, with a show-transcript toggle; speaking role-play cards and topic conversation prompts with teacher script. All Spanish must be accurate and at IGCSE level.

**Quality control (required, not optional):**
- Generate in resumable batches; keep `data/bank/progress.json` so the work survives interruptions.
- A separate checking pass, done by a fresh agent that did not write the question, answers each question cold and compares with the mark scheme; fix or delete mismatches.
- Automatic checks: schema validity, marks add up, no near-duplicates, every spec reference exists, no text copied from the corpus (run a similarity check against extracted corpus text and rewrite anything too close).
- `docs/BANK_REPORT.md`: counts per subject, topic and type, and QC pass rates.

## 6. Phase 4 — the website

Static site, no backend. Suggested stack: Vite + React + TypeScript, KaTeX, data loaded lazily per subject. Change the stack only if you have a good reason and write it down.

Pages:
1. **Home**: subject grid.
2. **Subject page**: the simplified spec checklist as an expandable tree with tick boxes, select-all per topic, and a count of available questions per sub-topic.
3. **Test builder**: sub-topics (from the checklist), paper/component, length (marks or minutes), question types (multi-select, specific to the subject), difficulty mix, calculator/non-calculator where relevant, and a "full paper in real structure" preset for each paper. The builder assembles a balanced paper: ramped difficulty, mark total matching the target, no repeated questions, and already-seen questions avoided (remember seen ids in localStorage, wrapped in try/catch).
4. **Paper view**: laid out like the real paper: cover page with subject, paper title, time allowed, total marks, instructions and information boxes; numbered questions with part labels; marks in brackets at the right; ruled answer lines sized to the marks; "Total for Question" lines; correct fonts and spacing; formula sheet or data booklet page where the real paper has one.
5. **Mark scheme view**: separate document in the board's table and levels-grid style.
6. **PDF export**: one button each for the question paper and the mark scheme, producing two separate, properly paginated A4 PDFs.
7. A seed in the URL so the same paper can be reopened or shared.

Branding rule: copy the layout faithfully, but do **not** use Pearson, Edexcel or Cambridge logos or claim to be official. Every cover and footer says "Practice paper — not an official exam board paper". Each subject page links to the official past-papers page.

Design: clean, fast, works on phone and laptop, light and dark mode, keyboard accessible. No sign-in, no analytics.

## 7. Phase 5 — repo and hosting

- Create a public GitHub repo named `igcse-paper-forge` with the `gh` CLI, push, and deploy to GitHub Pages with a GitHub Actions workflow that builds and validates the bank on every push.
- If `gh` is not installed or logged in, tell Dan the exact commands, and finish everything else locally meanwhile.
- README in plain English: what it is, how to run it locally, how to add questions, how to rebuild the corpus privately.
- Before every push, confirm `corpus/` and any extracted corpus text are not staged.

## 8. Definition of done

- [ ] Specs confirmed and `SCOPE_NOTES.md`, `CORPUS_GAPS.md` written.
- [ ] Corpus manifest exists locally; nothing from `corpus/` is in the repo history.
- [ ] A style guide and a spec JSON exist for all 10 subjects.
- [ ] Bank meets every scale target in section 5, passes schema validation, the independent answer check and the similarity check; `BANK_REPORT.md` shows the numbers.
- [ ] For each of the 10 subjects you have generated one topic test and one full-structure paper on the live site, exported both PDFs, opened them, and compared them side by side with a real paper from the corpus for layout and style; screenshots saved in `docs/verification/`.
- [ ] Maths renders correctly, diagrams display, Spanish listening plays.
- [ ] Site is live on GitHub Pages; the URL is in the README and reported to Dan.
- [ ] Final message to Dan: the URL, question counts per subject, what could not be downloaded, and anything that needs his decision.
