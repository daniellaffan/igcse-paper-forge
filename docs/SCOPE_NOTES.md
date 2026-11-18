# Scope notes

What each subject covers, where the bank deliberately differs from the real papers, and the decisions
Dan may want to revisit. Per-subject working notes (corpus findings, counts, template lists) are in
[`docs/notes/`](notes/). Every question is original; nothing is copied from Pearson or Cambridge papers.

## Across all subjects

- **Labelled as practice.** Every cover and page footer says "Practice paper — not an official exam
  board paper". No board logos, no candidate-number boxes that imitate the official layout exactly,
  and question references are our own.
- **Spec refs.** Where a specification numbers its content (sciences, maths, FPM, economics) the bank
  uses those numbers. Where it does not (English Language, English Literature, History option letters),
  we invented a stable reference scheme; it is documented in each `data/spec/<subject>.json`.
- **Modular 2023/24 specifications.** Pearson also runs modular versions (e.g. 4XEC1, first teaching
  2023). The bank targets the linear codes in the table in `README.md` only.
- **Six-mark science questions** (4PH1, 4CH1, 4BI1) are point-marked "any six from…", matching the real
  mark schemes, not levels-marked.
- **Units on answer lines** are printed after the dots (e.g. `....... m/s`), as on the real papers,
  except where the unit itself earns a mark.
- **Diagrams** are generated SVG: schematic, to scale where a reading is needed, and checked by the
  visual verification in `docs/verification/`.

## Mathematics A 4MA1
- Higher tier only (Papers 1H and 2H). Foundation content is assumed knowledge and tagged `F…`.
- The formulae sheet printed is our own wording of the standard Higher formulae (`data/reference/`).

## Further Pure Mathematics 4PM1
- Volumes of revolution are about the x-axis only (as on the spec).
- Mark schemes use M/A/B with `dM1` and `A1ft` where appropriate.

## Physics 4PH1
- Papers are named 1P and 2P; Paper-2-only (bold "P") content is tagged and only appears on 2P.
- An equations page is printed with each paper, in our own layout (`data/reference/physics-equations`).

## Chemistry 4CH1
- Papers 1C and 2C; bold "C" (Paper 2 only) content is tagged.
- Balanced-equation answers are checked in code; trivial balances (all coefficients 1) are excluded.

## Biology 4BI1
- Papers 1B and 2B; bold "B" content is tagged.
- Paper 2B opens with a comprehension question on a short original article (as on the real Paper 2); these
  are stored under the spec point the article is about (e.g. `variety.characteristics`).

## Economics 4EC1
- Papers 1 and 2. Spec point numbers checked against the official 4EC1 specification (Pearson, issue 2).
- **Maximum and minimum prices are not examined in general**: the spec names only the minimum wage, so
  price-control questions are limited to the minimum wage. Earlier max/min price templates were removed.
- Case-study settings use either real countries with realistic industries or clearly fictional ones; firm
  names match their sector.
- **AD/AS diagrams are excluded** (not in 4EC1).
- In the 4-mark calculation slot, the numbers are given in the question, not only in the extract.

## History 4HI1
- Options: Paper 1 Germany 1918–45 and A world divided 1943–72; Paper 2 Section A (historical
  investigation) Russia 1905–24 and Section B (breadth) America 1783–1877.
- **EITHER/OR choice for part (c)** is printed as on the real paper (two 16-mark alternatives;
  the paper total counts one).
- Sources are original, attributed to invented people of the period. Option letters/spec points are
  our own scheme.

## English Language A 4EA1
- Paper 1 only (non-fiction and transactional writing).
- **Anthology texts are not reprinted** (copyright). Questions on anthology texts name the title and
  author only; the student uses their own anthology. Unseen passages are original, 650–800 words.
- Section A is stored as one record per passage (the five linked questions travel together).

## English Literature 4ET1
- Paper 1 only: unseen poetry, anthology poetry (Part 3) and *Of Mice and Men* only.
- Anthology poems and the novel are **never quoted**; questions name the poem/novel only.
  Unseen poems are either original or genuinely public domain (poet died before 1955).
- **No bullet prompts in Section C**, because the real Paper 1 Section C has none (GOAL.md mentioned
  bullets; we followed the real papers). Section A has the three bullet prompts as on the real paper.

## Spanish 0530 (Cambridge)
- All four papers: Listening, Reading, Speaking, Writing.
- **Pictures** are replaced by short captions in boxes (we cannot use the board's pictures).
- **Listening audio** is read aloud by the browser's Spanish voice (Web Speech API), played twice;
  the transcript is in the mark scheme. No recorded audio exists.
- **Speaking:** role plays as on the real cards; the topic conversation is one 30-mark item.
- **Writing Q3** offers one task, not the a/b choice.

## Decisions Dan may want to make
1. Whether Spanish listening should get recorded audio (would need a TTS service or a speaker).
2. Whether to add a licensed extract booklet for English Language anthology texts.
3. Whether to add Maths Foundation tier.
4. Whether Writing Q3 in Spanish should offer the a/b choice.
5. Whether science full papers should group questions into the real ~10–12 long multi-part questions. Today a
   full Chemistry/Biology/Physics paper has the right marks, timing, topic spread and difficulty ramp, but is made of
   more, shorter numbered questions (e.g. Chemistry 1C: 46 questions for 110 marks; a real paper has about 11).
   Grouping by topic under "This question is about …" is possible in the test builder if wanted.
6. Verification was done without a browser at Dan's request (see `docs/verification/README.md`). Pressing ▶ on one
   Spanish listening question on the live site would confirm speech playback on his device.
