# Biology 4BI1: notes

## Spec facts confirmed (specification and papers in the corpus)

- **Qualification.** Pearson Edexcel International GCSE Biology 4BI1. Separate science, Papers 1B and 2B.
- **Paper 1B.** 2 h, 110 marks, calculator allowed. It assesses all non-bold content.
- **Paper 2B.** 1 h 15 min, 70 marks. It assesses all content, including the bold "B" statements, which are Biology-only (not in Double Award).
- **R variants.** 1BR and 2BR are alternative time-zone versions with the same format.
- **AO weightings.** AO1 38–42%, AO2 38–42%, AO3 19–21%.
- **Spec tree.** 5 topics, 31 subtopics and 176 points in `data/spec/biology.json`. Each B point is flagged, and a subtopic is restricted to `["2B"]` only when every one of its points is a B point.

## Disagreements with GOAL.md and decisions for the lead

1. **Extended questions are point-marked (resolved).** There is no levels grid. Each one has a single 6-mark row ("any six from", each bullet (1), note "max 6"). This is one row, not six 1-mark rows, because the validator requires the part's marks to equal the sum of its rows, and the list holds more than six points.
2. **Paper 2 Q1 is built (resolved).** The `comprehension` qtype has 12 original articles of 406–492 words, each worth 17 marks, tagged papers ["2B"] with paper2_only set. All of them are hosted in the `variety.characteristics` cell, so the cell has at least 12 questions; their spec_refs span the whole specification. Slot 1 of the 2B section in data/spec/biology.json holds this question, so the full Paper 2 starts with it. Calculation parts use `answer_suffix` for units. Two-part duplicates are left as they are, as instructed.
3. **Composite questions reuse knowledge-base items.** Two-part describe and explain questions pair a recall or MCQ lead-in with a single-part item that also exists as its own question. They pass the near-duplicate check, but a paper builder may want to avoid putting both on one paper (they share a `template` prefix).

## Corpus gaps and caveats

- Examiner reports cover most sessions. Some sessions have only `pef` (examiner report) or `msc` files, and none has a separate grade-boundary document.
- Topic frequency in the style guide is a keyword proxy, not a hand classification.
- I could not render the SVG diagrams here: the sandbox blocks Quick Look, and the browser pane won't show local files. Diagrams, pedigrees and graphs are schematic and were checked from their geometry only. Someone should look at a few in the site.

## Final counts

- **Total: 3,217 questions**, in 200 subtopic × qtype cells (minimum 12 per cell; the 12 comprehension questions form one cell). There are 572 templates.

| Topic | Questions |
|---|---|
| Structures | 1,738 |
| Reproduction | 572 |
| Ecology | 382 |
| Resources | 376 |
| Variety | 149 |

| Qtype | Questions |
|---|---|
| mcq | 583 |
| recall | 521 |
| explain | 434 |
| data | 365 |
| describe | 364 |
| calculation | 238 |
| practical | 233 |
| extended | 208 |
| comprehension | 12 |
| diagram | 182 |
| genetics | 77 |

| Difficulty | Questions |
|---|---|
| 1-3 | 1,267 |
| 4-6 | 1,441 |
| 7-9 | 497 |

- 686 questions are Paper 2-only. 683 carry `answer` values that were computed and checked.
- `validate_bank.py biology` prints OK. `similarity_check.py biology` flags 0 (worst overlap 0.133).
- Generator: `.venv/bin/python scripts/gen/biology.py`. It is deterministic and made of these modules:
  - `biology_spec.py`, `biology_lib.py`, `biology_short.py`;
  - `biology_kb1`–`biology_kb5.py`;
  - `biology_calc.py`, `biology_prac.py`, `biology_data.py`, `biology_diag.py`, `biology_gen.py`, `biology_ext.py`.
