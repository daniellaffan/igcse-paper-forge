# Data format

Everything the website shows comes from two kinds of JSON file. Both are checked by `scripts/validate_bank.py` against the schemas in `data/schema/`.

## 1. Simplified specification — `data/spec/<subject>.json`

Schema: `data/schema/spec.schema.json`.

```
subject → papers[]        (id, name, paper_code, minutes, marks, calculator, cover text, sections + full-paper slots)
        → qtypes[]        (the question types this subject uses: id + label + typical marks)
        → options[]       (History options, English sections …)
        → topics[]        (id, official ref, title, papers)
            → subtopics[] (id, official ref, title, one-line plain-English summary, papers, qtypes that can test it)
                → points[] (official spec ref, plain-English one-line summary, paper2_only / higher_only flags)
```

Summaries are **our own words**, never the specification's wording. Ids are lower-case, dot/hyphen separated, and unique within the subject, e.g. `maths.algebra.quadratics`.

### Full-paper preset

Each `papers[].sections[].slots[]` entry describes one question position in the real paper, e.g.
`{"label": "Q1", "qtypes": ["describe-two"], "marks": 6, "option": "germany"}`.
The test builder fills each slot with a matching bank question. For maths and science papers (which mix topics freely) the slots are omitted and the builder ramps difficulty to hit the paper's mark total.

## 2. Question bank — `data/bank/<subject>/<topic>.json`

Schema: `data/schema/question.schema.json`. A file is a JSON array of question records.

Key fields: `id`, `subject`, `paper` (list of paper ids it can appear on), `spec_refs` (official refs, each must exist in the spec JSON), `topic`/`subtopic` (spec ids), `qtype` (one of the subject's qtype ids), `command_word`, `marks` (must equal the sum of part marks), `difficulty` (`1-3`, `4-6`, `7-9`), `minutes`, `calculator`, `intro`, `figures`, `parts`, `markscheme`, `ao`, `answer` (machine-checked values), `provenance` (for any extract/poem/source).

### Text markup (all text fields)

* `$...$` inline maths (KaTeX), `$$...$$` display maths. Use `\times`, `\div`, `\frac{a}{b}`, `\sqrt{}`, `^\circ`, `\text{ cm}`.
* `**bold**`, `*italic*`.
* A blank line (`\n\n`) starts a new paragraph; a single `\n` is a line break.
* `[[blank]]` draws an inline answer box, `[[dots]]` draws a dotted answer line (gap-fill).

### Figures

| type | fields | use |
|---|---|---|
| `svg` | `svg`, `width` (mm), `caption`, `note` | diagrams, graphs, apparatus. Use `note: "Diagram NOT accurately drawn"` where the board does. SVG uses `currentColor`/black strokes on transparent background. |
| `table` | `headers`, `rows`, `caption` | data tables |
| `source` | `label`, `text`, `provenance` | History sources and interpretations, Economics extracts |
| `passage` | `title`, `text`, `numbered`, `provenance` | English / Spanish reading texts (numbered = line numbers printed) |
| `poem` | `title`, `text`, `provenance` | poems (public domain or original only) |
| `audio` | `lang`, `transcript`, `voices` | Spanish listening: played with the browser's Spanish text-to-speech; transcript toggle |

### Parts

`parts[]` each have `label` (`a`, `b`, `(i)`…), `text`, `marks`, and the answer space: `lines` (number of ruled lines), `space` (`lines`, `working`, `box`, `mcq`, `graph`, `table`, `none`), `answer_prefix` (e.g. `x = `), `answer_suffix` (unit after the dots, e.g. `m/s`; with `space: lines` a prefix/suffix gives a single answer line like `speed = ........ m/s`), `choices` for multiple choice. Parts can nest one level (`parts` inside a part) for (i)/(ii).

### Mark scheme

* `rows[]`: `{part, answer, marks, notes, ao}` — point-marked tables. In maths `marks` uses `M1`, `A1`, `B1`, `M1 A1` etc.; `notes` holds accept/reject/ignore guidance, ECF and alternative methods.
* `levels[]`: for levels-marked parts: `{part, title, ao_split, grid:[{level, marks, descriptor}], indicative:[…], credit_note}`. `credit_note` is always the line that other valid points must be credited.
* `general`: optional general marking guidance for the question.
