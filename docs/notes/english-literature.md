# Notes: English Literature 4ET1, Paper 1

## Spec facts confirmed (Issue 3 of the specification, SAMs and past papers)
- Code: 4ET1. Component 1 is **Poetry and Modern Prose**, paper code 4ET1/01 (the 01R variant is a timezone version). It lasts 2 hours, is worth 90 marks and carries 60% of the qualification. It runs in June and November (January in older series).
- Section A: Unseen poetry, 20 marks, AO2. Section B: Anthology poetry, a choice of 2 questions, 30 marks, AO2 15 + AO3 15. Section C: Modern prose, 2 questions per text, 40 marks, AO1 20 + AO4 20.
- The poems are the 16 in **Part 3** of the Pearson Edexcel International GCSE English Anthology. The spec lists them; our P3.01 to P3.16 follow the spec's order. *Of Mice and Men* is one of the modern prose set texts. Klara and the Sun and Western Lane were added as set texts for first assessment in 2026; they are out of scope here.
- The paper is closed-book for the novel, and a clean copy of the anthology poems is provided.

## Differences from GOAL.md and the request
- GOAL.md calls the anthology section "anthology poetry", which is correct. The spec places the poems in Part 3 of the anthology.
- The request mentions "bullet-point prompts" for Section C. Real Paper 1 Section C questions (2018 to 2025) have no bullets: only the Section A unseen question has the three bullet prompts. The bank follows the real paper, so it has bullets in Section A and none in Section C. If the lead wants scaffolding bullets in Section C, that is a one-line change in `gen_prose`.
- The spec has no numbered content points, so the references are our own scheme: 1A.n / 1B.n / 1C.n (section.subtopic), 1A.n.x / 1C.n.x for points, and P3.nn for poems.
- The site has no "choose one question" display. Sections B and C use two slots each (EITHER / OR), as in the real paper. The section instructions tell the candidate to answer one. The paper total stays at 90.

## Content and copyright
- Section A has 42 poems. **22 are originals** written for this bank (provenance says so). **20 are public domain**: Hardy, Edward Thomas, Yeats, Wordsworth, Dickinson, Owen, Teasdale, Stevenson, Rossetti, Tennyson, Dunbar, Hopkins, Blake, Shelley and McKay. Every one of these poets died before 1955 and every poem was published before 1929. Poems that appear in the corpus (for example *Leisure*) were avoided.
- The anthology poems are named by title and poet only and are never printed. The notes paraphrase the poems, with no lines quoted from the copyrighted modern poems.
- *Of Mice and Men* is never quoted. The epigraph-style "How far do you agree" prompts use invented critical statements.
- The levels grids are paraphrased from the board's structure: same bands and AO splits, but our own wording.

## Counts
- 459 questions: unseen 111 (6 subtopics, 12 to 27 each); anthology 224 (7 themes x 16 pair + 16 open); prose 124 (9 subtopics, 12 to 17 each).
- Difficulty: 1-3: 81, 4-6: 239, 7-9: 139.
- `validate_bank.py english-literature` gives OK. `similarity_check.py english-literature` gives 0 flagged (worst overlap 0.013).
- Templates: one per unseen poem (42), 14 anthology templates (pair or open x 7 themes), 9 prose templates.

## Corpus gaps
- Paper 1 question papers and mark schemes from June 2018 to June 2025 (including 01R), the SAMs and the examiners' reports were all available. The most recent series (November 2025 onwards) were not in the corpus. Nothing blocked this subject.
