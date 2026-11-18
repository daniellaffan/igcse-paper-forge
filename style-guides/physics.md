# Physics 4PH1: style guide

This guide comes from studying the private corpus for Physics 4PH1. The corpus covers question papers, mark schemes and examiner reports (pef) for 1P, 2P and the R variants, from June 2019 to June 2025. Everything here is my own description. Nothing longer than a few words is quoted.

## Paper anatomy

| | Paper 1P | Paper 2P |
|---|---|---|
| Time | 2 hours | 1 hour 15 minutes |
| Marks | 110 (61.1%) | 70 (38.9%) |
| Content | All non-bold specification content | All content, including bold "P" statements |
| Questions | 11–12 | 7–9 |
| Question size | 4–15 marks; most are 6–13 | 3–15 marks; most are 6–13 |
| Calculator | Allowed | Allowed |

- **Marks per question.** Each row lists one paper's question totals in order, counted from the "Total for Question" lines:
  - 1P June 2024: 5 5 10 9 11 8 12 6 6 15 11 12.
  - 1P November 2023: 5 4 6 10 11 10 12 6 11 10 12 13.
  - 2P June 2024: 5 10 8 9 8 7 10 13.
  - 2P June 2022: 7 8 15 10 9 8 13.
  - The opening question is usually a gentle 4–7 mark MCQ/recall starter. There is no strict difficulty ramp after that; each multi-part question ramps internally from recall to application.
- **Cover rubric** (paraphrased):
  - Use black ink.
  - Fill in the candidate boxes.
  - Answer all questions in the spaces provided.
  - Show all the steps in calculations and give units.
  - The total mark is shown.
  - Marks for each part are given in brackets.
  - Some questions need extended writing, and the quality of that writing is judged.
  - Read each question carefully, keep an eye on time, and check answers.
- **Formulae page:** the inside cover of 1P carries a FORMULAE page listing the equations the specification does not require candidates to recall. Since 2022 an Equation Booklet has also been enclosed. It lists every equation with an extra 2P-only section. See `data/reference/physics-equations.json`.
- **Furniture and conventions:**
  - Each question ends with a bold "(Total for Question N = M marks)" line, and the paper ends with "TOTAL FOR PAPER = 110/70 MARKS".
  - Mark tariffs appear in brackets at the right margin.
  - Working lines end with an answer line of the form "quantity = ........ unit". The unit is usually printed, but some questions ask the candidate to supply it.
  - Diagrams carry "not drawn to scale" notes where relevant.
  - Graph grids are printed full width.
  - g is always 10 N/kg.

## Question types (tariffs and stems)

| Type | Tariff | Typical stem | Notes |
|---|---|---|---|
| MCQ | 1 | "Which of these…", followed by four options A–D with tick boxes | Usually 1–3 per paper, often as part (a) of a question. Mark schemes give the key and a one-line reason each distractor is wrong ("X is not the answer because…"). |
| State/Name/Give | 1–2 | "State the equation linking…", "Name the…", "Give two…" | Equation recall is a 1-mark item for any equation not on the formulae page. Symbols are accepted, but a unit-only equation is rejected. |
| Describe | 2–4 | "Describe how…", "Describe what happens…" | Marked as a point list ("any N from MP1…"). |
| Explain | 2–4 | "Explain why…" | Needs a linked cause and effect; a bare statement earns only the first point. |
| Calculation | 2–5 | "Calculate…", "Show that…", "Determine…" | Structure: equation (if not given), substitution, rearrangement, evaluation, sometimes a unit mark or a unit-conversion mark. "Show that" asks for an answer to more significant figures than the value given. |
| Practical / AO3 | 3–8 | "Describe a method…", "State the independent variable…", "Suggest an improvement…", "Give a reason…" | Practical-based items carry roughly 20% of the marks. The core practicals all appear across the series, including springs, refraction, SHC, density, I–V characteristics, sound speed and radiation absorption. |
| Graph / data | 4–8 | "Plot…", "Draw the line of best fit", "Use the graph to determine…" | Plotting is 4–5 marks: scale, axes with units, points within half a square, and a line or curve. Gradient questions expect a large triangle. |
| Diagrams | 2–4 | "Complete the ray diagram", "Draw the field pattern", "Draw a circuit diagram…", "Add arrows…" | Circuit symbols must be standard, and rays need arrows. |
| Extended response | 5–6 | "Describe how…", "Explain how…", "Discuss…" | One or two per paper. **The real 4PH1 scheme marks these as a point list with a category maximum** (for example "any six from MP1–MP10", sometimes "max 3 from each of A/B"), not as a levels grid. |

- **Command-word mix:** Calculate, Describe and Explain dominate. State and Give are common in practical parts. Suggest marks a novel context where any sensible physics is credited.
- **Contexts** are everyday or applied: vehicles and stopping, kettles and appliances, mains wiring, medical uses of radiation, satellites and planets, renewable energy, sound in buildings, optical fibres, weather balloons, divers and dams.

## How the mark scheme is written

- **Layout:** a table with question number, answer, notes and marks. Each creditworthy point ends in a semicolon.
- **Note keywords:**
  - "allow" accepts equivalent answers or alternative values.
  - "ignore" marks irrelevant extras.
  - "reject" or "do not accept" marks wrong physics that cancels a mark.
  - "condone" covers minor slips.
- **Calculations:** the rows are labelled "substitution;", "rearrangement;" and "evaluation;". An example line shows the working.
  - "-1 for POT error" applies to power-of-ten slips.
  - "allow ecf" lets a wrong earlier answer carry forward.
  - A correct bare answer usually earns full marks unless the question says "show that".
  - Answers rounded to 2 or 3 significant figures are both listed.
- **Point lists:** "any N from:" followed by MP1, MP2 and so on. Grouped maxima apply where several features are needed.
- **Graph rows:** a scale whose points cover over half the grid, labelled axes with units, plotting to within half a square, and a line of best fit (straight or curved as appropriate).
- **AO split:** AO1 is about 38–42%, AO2 about 38–42% and AO3 about 19–21%. Mark schemes do not label AOs per row; we add them to the bank as metadata.
- **Six-markers in this bank:** point-marked like the real papers, as one "any six from" row worth 6 marks with the note "max 6".

## What examiner reports say

- **Strong answers:**
  - Write the equation, substitute with units converted first, then rearrange.
  - Quote values from the data.
  - Make comparisons that are explicit ("increases from X to Y").
  - Use correct terms (thermal energy store, field lines, wavefront).
- **Common errors:**
  - Power-of-ten slips with kPa, kHz, ms, cm³ and grams.
  - Rearranging wrongly before substituting.
  - Missing or wrong units, such as N/m² confused with N/m, or kW h confused with J.
  - Using °C instead of kelvin in gas laws.
  - Forgetting to double the echo distance.
  - Not squaring v in KE.
  - Vague comparisons such as "it goes up".
  - Saying "energy is used up", or treating heat and temperature as the same thing.
  - Confusing irradiation with contamination.
  - Drawing ray arrows the wrong way.
  - Choosing scales that use less than half the grid.
  - Forcing the line of best fit through the origin.
  - In practical methods, omitting the control variables or what is measured with which instrument.
  - Extended answers that list facts without linking them to the question context.

## Topic frequency (counted from 27 non-R papers with "Total for Question" lines)

Each question was assigned to its dominant topic by keyword count. Shares are percentages of marks. The method is approximate, because many questions mix topics. Energy is under-counted since its questions often sit inside electricity or forces contexts.

| Topic | 1P questions / % marks | 2P questions / % marks |
|---|---|---|
| 1 Forces and motion | 24 / 17% | 19 / 17% |
| 2 Electricity | 29 / 20% | 15 / 14% |
| 3 Waves | 20 / 13% | 17 / 16% |
| 4 Energy | 6 / 5% | 8 / 7% |
| 5 Solids, liquids and gases | 18 / 13% | 16 / 15% |
| 6 Magnetism and electromagnetism | 15 / 8% | 12 / 11% |
| 7 Radioactivity and particles | 18 / 12% | 11 / 8% |
| 8 Astrophysics | 20 / 12% | 14 / 11% |

- **Form patterns:**
  - Electricity and forces carry most of the calculations and graph work.
  - Waves carries the ray diagrams and refraction practicals.
  - Radioactivity carries the nuclear equations and half-life graphs.
  - Astrophysics carries the orbital speed calculations, star life cycles and (on 2P) red-shift.
  - 2P draws heavily on bold content: SHC and change of state, transformers, moments, momentum, sound/oscilloscope, red-shift, static and energy resources.
