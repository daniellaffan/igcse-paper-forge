# Notes: Further Pure Mathematics 4PM1

## Spec facts confirmed

- Pearson Edexcel International GCSE Further Pure Mathematics, code 4PM1. There are two papers, 4PM1/01 and 4PM1/02.
- Each paper is 2 hours and 100 marks, with a calculator allowed in both. Each is 50% of the qualification.
- The papers are untiered. Grades run from 9 to 4, and a grade 3 is allowed.
- The formulae sheet is spec Appendix 4, reproduced as `data/reference/further-maths-formulae.json`.
- Assessment objectives: AO1 30–40%, AO2 20–30%, AO3 35–50%.
- Content areas:
  - 1 logarithmic functions and indices (1A–1D)
  - 2 quadratic function (2A–2C)
  - 3 identities and inequalities (3A–3E)
  - 4 graphs (4A–4B)
  - 5 series (5A–5B)
  - 6 binomial series (6A(i)/(ii))
  - 7 scalar and vector quantities (7A–7F)
  - 8 rectangular Cartesian coordinates (8A–8E)
  - 9 calculus (9A–9G)
  - 10 trigonometry (10A–10H)

  Subtopic ids in `data/spec/further-maths.json` are `fm.<area>.<name>`. Point refs follow the spec letters.
- Papers have 10 to 12 questions, all compulsory, with no sections.
- **GOAL.md section 2:** it agrees ("Papers 1 and 2"). Nothing disagrees. Calculators are allowed in both papers.

## Corpus gaps

- **June 2019 Paper 1:** the question-paper text is effectively empty (about 100 bytes). The 01R re-sit paper and its mark scheme for that series are usable.
- **June 2021:** there are no examiner reports.
- **November 2021, 2023 and 2024:** these series are partial, with 6 files each instead of 12.
- **Diagrams:** the diagrams are images, so their content is lost in extraction. Topic counts for diagram-heavy questions are keyword estimates.

## Implementation notes

- **Runner:** `scripts/gen/further-maths.py`. The templates live in `further_maths_{util,spec,alg,series,geom,calc,trig}.py`. They use underscores because a hyphenated module name cannot be imported.
- **Spec and reference files:** the runner also writes the spec JSON and the formulae reference.
- **Mark tokens:** dependent method marks are written as `M1` with `dM1` in the notes, and follow-through as `A1` with `ft` in the notes. This is because the validator's mark parser does not accept `dM1` or `A1ft`.

## Final counts

- **Questions:** 1,771 from 82 template functions (176 variants), across 80 subtopic × qtype cells.
- **Cell sizes:** the smallest cell has 22 questions. There are no duplicates.
- **Checks:** every answer was computed with sympy and has `checked: true`. `validate_bank.py` prints OK, and `similarity_check.py` flags 0 questions (worst overlap 0.083).
- **By topic:**

  | Topic | Questions |
  |---|---|
  | Logs | 165 |
  | Quadratics | 154 |
  | Identities and inequalities | 198 |
  | Graphs | 88 |
  | Series | 176 |
  | Binomial | 110 |
  | Vectors | 88 |
  | Coordinates | 110 |
  | Calculus | 396 |
  | Trigonometry | 286 |

- **By qtype:**

  | qtype | Questions |
  |---|---|
  | short | 682 |
  | multi-part | 528 |
  | show-that | 286 |
  | applied | 154 |
  | graph | 121 |

- **By difficulty:**

  | Band | Questions |
  |---|---|
  | 1–3 | 103 |
  | 4–6 | 1,057 |
  | 7–9 | 611 |
