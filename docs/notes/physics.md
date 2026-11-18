# Physics 4PH1: build notes

## Spec facts confirmed from the corpus

- **Paper 1P (4PH1/1P):**
  - 2 hours, 110 marks (61.1%).
  - Assesses all non-bold content.
- **Paper 2P (4PH1/2P):**
  - 1 hour 15 minutes, 70 marks (38.9%).
  - Assesses all content, including the bold statements with a "P" suffix.
- Both papers are calculator papers and use g = 10 N/kg.
- **Equation sheets:**
  - 1P prints a FORMULAE page.
  - Since 2022 an Equation Booklet has also been enclosed, with an extra 2P-only section.
  - Both are captured in `data/reference/physics-equations.json`.
- **R papers:** 1PR and 2PR are parallel papers for other time zones. They have the same structure.
- **Paper 2-only tagging:** bold "P" statements are tagged `paper2_only: true` with paper `["2P"]`. This applies to any question citing a ref that ends in P. There are 674 such questions.

## Disagreements with GOAL.md section 2

- GOAL says "Papers 1 and 2"; the official codes are 1P and 2P. I used the codes 1P and 2P.
- **Six-mark questions (decided: point-marked):**
  - Real 4PH1 six-markers are point-marked: "any six from MP1…", sometimes with category maxima. They are not levels-marked.
  - The lead decided to follow the real papers: each extended part has one "any six from" row worth 6 marks with the note "max 6" (the validator needs row marks to sum to the part marks).
  - Units now go in `answer_suffix` (the field the lead added), not in `answer_prefix`.

## Corpus gaps

- June 2019 1P question text has no "Total for Question" markers, so it was left out of the frequency count.
- June 2021 has only two question papers and no examiner reports.
- November 2021, November 2023 and November 2024 have no R papers.
- The keyword topic count is approximate; Energy is under-counted.

## Units

- Units go in `answer_suffix`, for example prefix "speed = " and suffix "m/s". 490 parts use it.

## Final counts

- **Bank:** 2313 questions in 8 topic files.
- **Cells:** 30 subtopics, 165 subtopic × qtype cells, all with at least 12 questions. No thin cells and no duplicates.
- **By qtype:** mcq 420, recall 420, explain 378, describe 224, calc 290, extended 180, practical 160, diagram 127, data 114.
- **Generators:** 98 parametric templates, plus knowledge-base combination for all 30 subtopics.
- **Figures:** 209 SVG figures, all of which parse as valid XML.
- **Checks:**
  - `validate_bank.py physics` prints OK.
  - `similarity_check.py physics` flags 0; the worst overlap is 0.148.
