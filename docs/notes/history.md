# History 4HI1: build notes

## Confirmed spec facts (specification Issue 5, papers 2019–2025)

- **Qualification:** Pearson Edexcel International GCSE History, code 4HI1. Two papers, each 1 h 30 min, 60 marks and 50% of the qualification.
- **Paper 1 (4HI1/01) Depth Studies:** candidates answer two depth studies, 30 marks each, about 45 minutes each.
- **Paper 2 (4HI1/02):**
  - Section A (historical investigation, options A1–A5): one question, 30 marks.
  - Section B (breadth study in change, options B1–B8): one question, 30 marks.
- **AO split:** AO1 34%, AO2 36%, AO3 15%, AO4 15%.

## Option mapping (verified against the spec and papers)

| Option id | Title | Spec ref | Paper / section id |
|---|---|---|---|
| germany | Germany: development of dictatorship, 1918–45 | Depth study 3 | p1 / depth-germany |
| world-divided | A world divided: superpower relations, 1943–72 | Depth study 6 | p1 / depth-world-divided |
| russia | Russia and the Soviet Union, 1905–24 | A2 | p2 / A |
| america | America: from new nation to divided union, 1783–1877 | B1 | p2 / B |

- All four titles match the brief exactly.
- The key topic refs (3.1–3.5, 6.1–6.5, A2.1–A2.5 and B1.1–B1.5) follow the spec's numbering.
- The point letters (for example 3.1a) are ours. The spec lists content as bullets without letters.

## Differences from the brief and GOAL.md

- **Paper 1 has no "explain why" question with two stimulus points and no "account" question.** Those belong to the UK GCSE 9–1 format. In the international paper, the stimulus bullets sit on the 16-mark judgement in part (c). Paper 1 is therefore modelled as impression (6), explain two effects (8) and judgement (16).
- **Paper 2 Section A has no source-utility question.** Its (b) asks how far Source A supports Source B (8 marks, AO3). Examiners say reliability is not required.
- **EITHER/OR in part (c) is not modelled.** Each (c) record is a single 16-mark question, because two alternatives would make the marks add up to 32. A full paper therefore shows one (c) question, not a choice of two. **Decision for the lead:** should the assembler pair two judgement records as (i) and (ii)?
- **Section A (b) and (c) share their sources.** They are stored together as a 24-mark `investigation` record with parts (b) and (c), and the full-paper preset uses that record. Stand-alone `source-support` and `interpretation` records exist for topic tests.
- **Section A (a) is one 6-mark part.** It keeps the internal "EITHER topic OR topic" wording.

## Corpus gaps

- The text of the June 2024 Paper 2 examiner report is garbled, so it was not usable.
- Some November series have no examiner report.
- The question-paper files contain every option, so the topic-frequency counts in the style guide are approximate keyword counts.

## Content and provenance

- Every extract is an original text in the style of a modern history book. Labels name a generic book and year, and no real historian is named.
- Every source is an original text attributed to an invented, unnamed person of the period.
- Each record carries a `provenance` string.
- No corpus wording, figures or sources were reused. similarity_check.py flags nothing; worst overlap is 0.043.

## Final counts

- **809 questions in total:**
  - germany 201
  - world-divided 185
  - russia 242
  - america 181
- There are 65 subtopic × qtype cells, all at 12 or more.
- **12 templates:**
  - germany: impression, effects, judgement
  - world-divided: impression, effects, judgement
  - russia: describe, support, interpretation, investigation
  - america: difference, causes, judgement
- **Difficulty:** 1-3 = 124, 4-6 = 436, 7-9 = 249.

The generator is `scripts/gen/history.py`, with content in `history_germany.py`, `history_cold_war.py`, `history_russia.py` and `history_america.py`.
