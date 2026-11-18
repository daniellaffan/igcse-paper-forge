# Notes: Mathematics 4MA1 (Higher)

## Spec facts confirmed

- The course is Pearson Edexcel International GCSE Mathematics A, code 4MA1. The bank is Higher tier only, covering Papers 1H and 2H.
- Each paper lasts 2 hours, is worth 100 marks and allows a calculator. Each paper is 50% of the qualification.
- The spec has 6 content areas:
  1. Number
  2. Equations, formulae and identities
  3. Sequences, functions and graphs
  4. Geometry and trigonometry
  5. Vectors and transformation geometry
  6. Statistics and probability
- Higher assumes the Foundation content. In `data/spec/maths.json`:
  - Point refs prefixed `F` (e.g. `F4.8A`) come from the Foundation list and are assumed knowledge.
  - Point refs prefixed `H` (e.g. `H4.8C`) come from the Higher list and are flagged `higher_only`.
  - Subtopic refs follow the spec numbering ("4.6", "6.3A").
- A formulae page is provided. It is reproduced as `data/reference/maths-formulae-higher.json`, with SVG figures and KaTeX captions.
- **GOAL.md section 2:** it agrees ("Higher tier, Papers 1H and 2H"). No Foundation bank was built.

## Corpus gaps

- 32 Higher question papers have usable text.
- Some series have no examiner report (June 2021 has none). Some series also lack one of the Higher papers' reports.
- Diagrams in the papers are images, so the text extraction loses them. Diagram-based topic counts are estimates from the surrounding text.

## Final counts

- **Questions:** 1,854 from 188 templates, across 100 subtopic × qtype cells. Every cell has at least 12 questions, there are no duplicates, and every answer is computed in code with `checked: true`.
- **By topic:**

  | Topic | Questions |
  |---|---|
  | Number | 309 |
  | Algebra | 324 |
  | Functions | 233 |
  | Geometry | 606 |
  | Vectors and transformations | 70 |
  | Statistics and probability | 312 |

- **By qtype:**

  | qtype | Questions |
  |---|---|
  | short | 594 |
  | problem | 555 |
  | algebra | 211 |
  | structured | 142 |
  | proof | 140 |
  | graph | 132 |
  | stats | 80 |

- **Difficulty:**

  | Band | Questions |
  |---|---|
  | 1-3 | 63 |
  | 4-6 | 744 |
  | 7-9 | 1,047 |

- **Checks:** `validate_bank.py maths` prints OK, and `similarity_check.py maths` flags 0 questions (worst overlap 0.150).
- **Regenerate:** run `.venv/bin/python scripts/gen/maths.py`. The output is deterministic.
