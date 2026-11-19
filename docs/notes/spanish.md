# Notes: Spanish (Cambridge IGCSE 0530)

## Confirmed spec facts (syllabus 664626, 2025–2027, and the 2021–2025 papers)
- Four components with equal weight:
  - P1 Listening: about 50 min including 6 min transfer, 40 marks, 37 selected-response items.
  - P2 Reading: 1 h, 45 marks, six questions.
  - P3 Speaking: 10 min preparation, then a role play (10 marks) and two topic conversations (30 marks), 40 in total.
  - P4 Writing: 1 h, 45 marks. Q1 form 5; Q2 80–90 words 12; Q3 130–140 words 28 (task completion 10, range 10, accuracy 8).
- Topic areas: A Everyday activities, B Personal and social life, C The world around us, D The world of work, E The international world. There are 19 sub-topics (A1–A4, B1–B5, C1–C6, D1–D2, E1–E2), and the syllabus calls its sub-topic content examples only. `data/spec/spanish.json` follows this list.
- The paper formats are stable across every series from 2021 to 2025 and match the 2021 specimen.

## Against GOAL.md section 2
No disagreement. The board is Cambridge 0530, not Edexcel, and it covers the four skills. Only Paper 4 has a choice (Q3 a/b). There are no tiers.

## Corpus gaps
- No examiner reports for November 2024 or November 2025. March 2021 has no role-play cards and no report.
- There is no audio. Listening is built from the transcript files.
- Pictures in the papers are not in the text extraction, so picture options are known only from the mark-scheme letters.

## Design decisions (for the lead)
- **Pictures.** Picture items (l-short, r-pictures) print line drawings: Tabler outline icons (MIT licence), plus clock faces and a body figure drawn in code. `scripts/gen/spanish_pictures.py` maps 365 of the 473 captions. Colours, days, months, flags, countries and languages keep a boxed caption, because a black-and-white drawing could only show them by printing the English word. No question shows two captions with the same drawing. Listening options print side by side as A–D, reading pictures as an A–F grid, and the mark scheme gives the caption.
- **Speaking.** The two topic conversations are one 30-mark item, because the marks are awarded jointly. The role play is a separate 10-mark item. Both carry the teacher script.
- **Writing Q3.** Each Q3 is a single 28-mark task. The paper's a/b choice is not modelled as option_group.
- **Formats.** No gap-fill or true/false formats, because they are absent from the current papers.
- **Reading texts.** Long reading texts are `source` figures, which go to the Insert.
- **Light sub-topics.** B3 colours, C5 measurements and C6 materials only get picture, recognition and form tasks.
- **Vocabulary.** Spain and Latin American vocabulary are mixed, as in the papers.

## Final counts
- **Bank size.** 3,445 questions across 265 spec cells and 17 qtypes, with about 265 templates.
- **By area.** A 819, B 897, C 884, D 429, E 416.
- **By qtype.** l-short 247, l-announce 208, l-match 208, l-interview-3 208, l-interview-4 208, l-multi 208; r-pictures 247, r-signs 156, r-text-mcq 208, r-short 208, r-match-ads 117, r-long 208; s-roleplay 208, s-conversation 195; w-form 221, w-short 195, w-extended 195.
- **Checks.** `validate_bank.py spanish` prints OK, with 0 thin cells and 0 duplicates. `similarity_check.py spanish` flags 0 against 271 corpus documents, and the worst overlap is 0.022.
