# Chemistry 4CH1: build notes

## Spec facts confirmed from the corpus

- **Paper 1C (4CH1/1C):** 2 hours, 110 marks (61.1%). Assesses all non-bold content.
- **Paper 2C (4CH1/2C):** 1 hour 15 minutes, 70 marks (38.9%). Assesses all content, including the bold statements with a "C" suffix.
- **Both papers:** calculators are allowed and a periodic table is printed on the back page. That table is written as `data/reference/chemistry-periodic-table.json` and set as `reference_sheet` on both papers.
- **Assessment objectives:** AO1 38–42%, AO2 38–42%, AO3 19–21%.
- **Specification:** Issue 3, September 2024.
- **R papers:** 1CR and 2CR are parallel papers for other time zones, with the same structure.
- **Paper 2-only tagging:** bold "C" statements are tagged `paper2_only: true` with paper `["2C"]`, applied to any question citing a ref ending in C. There are 643 such questions.

## Disagreements with GOAL.md section 2

- GOAL says "Papers 1 and 2"; the official codes are 1C and 2C. I used 1C and 2C.
- **Six-mark questions:** GOAL section 3 anticipates levels grids, but 4CH1 six-markers are point-marked ("any six from"). The lead decided to follow the real papers. Each extended part now has one row worth 6 marks:
  - the row lists the points as M1…Mn
  - the note reads "max 6; credit any other valid chemistry"
  - the validator needs row marks to sum to the part marks, so the 6 marks sit on one row rather than on separate 1-mark rows
- **Units:** calculation units now go in `answer_suffix`, using the field the lead added.
  - The unit comes from the stem ("in cm³/s") or from the quantity (ΔH → kJ/mol, % and so on).
  - It is left blank where the unit carries a mark.

## Corpus gaps

- **June 2021:** only the 1C and 2C question papers and mark schemes exist. There are no R papers and no examiner reports.
- **November 2021, 2023 and 2024:** these series have no R papers.
- **June 2024 1C examiner report:** the extracted text is unreadable because of a font-encoding problem, so the June 2024 insights come from the 2C reports only.
- **Topic frequency:** this is a keyword count over 48 question papers, so it is approximate.

## Final counts

- **Questions:** 2,141 from 147 templates.
  - By topic file: principles 755, inorganic 651, organic 472, physical 263.
  - 138 subtopic × qtype cells, none with fewer than 12 questions, and no duplicates.
- **Difficulty:** 1–3: 528; 4–6: 1,031; 7–9: 582.
- **By qtype:**

  | Qtype | Count |
  |---|---|
  | mcq | 384 |
  | recall | 378 |
  | equation | 335 |
  | explain | 269 |
  | calculation | 220 |
  | data | 184 |
  | practical | 146 |
  | describe | 115 |
  | extended | 110 |

- **Checked answers:**
  - Numerical answers are computed in code.
  - Equations are atom- and charge-balance checked by `EQ()`.
  - Every numerical or equation answer is stored as `answer:{method, values, checked:true}`.
- **Checks:** `validate_bank.py chemistry` gives OK, and `similarity_check.py chemistry` flags 0 (worst overlap 0.148).

## Schema-change requests

None. (`answer_suffix` is already in place.)
