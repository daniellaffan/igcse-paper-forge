# Chemistry 4CH1: style guide

This guide comes from studying the private corpus for Chemistry 4CH1. The corpus covers question papers, mark schemes and examiner reports for 1C, 2C and the R variants, from June 2019 to June 2025 (48 question papers). Everything here is my own description. Nothing longer than a few words is quoted.

## Paper anatomy

| | Paper 1C | Paper 2C |
|---|---|---|
| Time | 2 hours | 1 hour 15 minutes |
| Marks | 110 (61.1%) | 70 (38.9%) |
| Content | All non-bold specification content | All content, including bold "C" statements |
| Questions | 10–12 (usually 10–11) | 6–8 (usually 7) |
| Question size | 4–17 marks; most are 7–15 | 4–16 marks; most are 7–14 |
| Calculator | Allowed | Allowed |

- **Marks per question.** These are counted from the "Total for Question" lines:
  - 1C June 2024: 7 9 10 12 9 13 13 15 11 11.
  - 1C November 2023: 7 10 12 11 17 12 11 9 12 9.
  - 2C June 2024: 7 5 11 10 10 14 13.
- **Order of questions.** Question 1 is a gentle 4–7 mark starter, often a matching or MCQ item on particles, separation or the periodic table. After that the topics are mixed. Each question has one theme (for example "a student investigates rusting") and works from recall up to application, calculation or evaluation.
- **Periodic table.** The back page of both papers carries a periodic table, which gives Ar values to the nearest whole number (Cl 35.5, Cu 63.5). It is reproduced in our own layout in `data/reference/chemistry-periodic-table.json`.
- **Cover rubric** (paraphrased):
  - Use black ink.
  - Answer all questions in the spaces provided.
  - Show working in calculations and give units.
  - The marks for each part are shown in brackets.
  - To change an MCQ answer, put a line through the crossed box.
  - Some answers need extended writing, and the quality of that writing is judged.
- **Furniture and conventions:**
  - Each question ends with a bold "(Total for Question N = M marks)" line, and the paper ends with "TOTAL FOR PAPER".
  - Answer lines take the form "quantity = .......... unit". The unit is printed unless the unit carries a mark.
  - Tables have ruled borders and carry the units in the column headers, e.g. "Temperature in °C".
  - Apparatus diagrams are simple line drawings with labels.

## Question types (tariffs and stems)

- **MCQ (1 mark):** four options A–D with boxes to cross. Usually about four per paper, embedded at the start of a multi-part question. The options are distractors built from common errors, such as the wrong charge or a formula with the wrong ratio.
- **Recall: give / name / state / identify (1–2 marks):**
  - names of reagents, products and processes
  - test results, uses and colours
  - formulae, including general formulae, molecular and empirical formulae, and naming from a displayed formula
- **Describe (2–4 marks):** how to carry out a test or a process, or what is seen. Marks go to the steps in a sensible order and to stated observations.
- **Explain (2–4 marks):** marks are awarded for linked cause and effect. Typical contexts:
  - bonding and structure, linked to melting point or conductivity
  - reactivity trends in Groups 1 and 7
  - rates, explained with collision theory
  - equilibrium shifts
  - why cracking is needed
- **Calculation (2–5 marks):** answers usually need to be given to 2 or 3 significant figures, and an ecf chain usually runs through the steps. Topics:
  - Ar from isotopic abundance, and Mr
  - percentage composition
  - empirical and molecular formula
  - reacting masses, percentage yield
  - moles of gas at rtp (24 dm³), and concentration and titration (2C)
  - Q = mcΔT and ΔH, bond energies (2C), mean rate, Rf
- **Equations (1–3 marks):** word equations, balanced symbol equations, state symbols (often a separate mark), ionic equations, and half-equations at electrodes (2C).
- **Practical (3–6 marks):** an unfamiliar experimental set-up. Candidates name the apparatus, the variable to control, an improvement, or the reason for a step. Common set-ups:
  - titration
  - calorimetry with a polystyrene cup or a spirit burner
  - gas syringe, or collecting gas over water
  - mass loss on a balance
  - chromatography
  - electrolysis
  - iron wool in a syringe for the percentage of oxygen
  - making salts
- **Data and graphs (3–8 marks):** plot points, draw a curve of best fit, read values off the graph, identify an anomaly, describe a trend, or predict a value for the next member of a group or series.
- **Extended response (5–6 marks):** this appears about once per paper. It is either a method question ("describe how to prepare a pure dry sample of …", "how to identify the ions in …") or a comparison and evaluation question. The mark scheme is point-marked: a list of 7–10 creditworthy points, with "any six from" and a maximum.

## Command words

The most frequent command words are state, give, name, describe, explain, calculate, suggest, deduce, identify, complete and draw. "Evaluate" and "compare" are rarer and appear mainly in 2C.

## How the mark scheme is written

- Every question has a table with these columns: question number, answer, notes, marks.
- **Marking points:**
  - Points are labelled M1, M2 and so on. Where order matters they are written in sequence.
  - "dep" marks a point that can only be awarded if an earlier point is gained.
  - "Any two from" lists are common.
- **Key words** in the notes column:
  - ALLOW gives acceptable alternatives.
  - REJECT marks a wrong idea that cancels a mark.
  - IGNORE marks text that is neither credited nor penalised, such as state symbols when they are not asked for.
- **Calculations:**
  - A correct final answer with no working usually earns full marks.
  - ecf (error carried forward) runs through each later step.
  - Significant-figure penalties are applied only where the question asks for a precision.
- **Equations:** M1 is for the correct formulae and M2 is for balancing. If the question asks for state symbols, they carry their own mark.
- **Extended answers:** these are point-marked, "any six from", and there are no levels grids. 4CH1 does not use levels-marked questions.
- **AOs:** the specification aims for AO1 38–42%, AO2 38–42% and AO3 19–21%. AO3 sits mainly in the practical and data questions.

## What examiner reports say

These are paraphrased themes from the reports for June 2019, January 2021, November 2021, June 2022, June 2023, June 2024 (2C) and June 2025:

- **Ar calculations:** weak answers divide by the sum of the mass numbers instead of 100. Others round the answer to a whole number when one decimal place was asked for.
- **Formulae:** candidates misread the number outside a bracket, as in Ca(OH)₂. They give the empirical formula when the molecular formula was asked for, and the reverse.
- **Displayed formulae:** marks are lost when not every bond is shown.
- **Names and formulae:** candidates give the name when the formula is asked for, for example "sulfuric acid" instead of H₂SO₄, and the reverse.
- **Homologous series:** "same chemical properties" is not accepted, because the properties are only similar.
- **Fractional distillation:** candidates say the crude oil is heated inside the column. They also give the wrong conditions for cracking.
- **Supply and demand:** answers that just mention "supply and demand" lose marks. The answer has to say which fractions are in surplus and which are in demand.
- **Observations:** observations in practical work are weak. Candidates name a gas instead of describing what is seen ("bubbles", "brown vapour").
- **Electrolysis:**
  - Candidates say that bromine loses electrons, when it is the bromide ions that do.
  - In explaining conductivity, they fail to state that the ions are free to move.
- **Sacrificial protection:** this is confused with barrier methods.
- **Strong answers:** these link each fact to a reason, use correct terms (ions, electrons, intermolecular forces) and quote data from the question.

## Topic frequency

The number of the 48 question papers that mention each area. The counts come from a keyword search, so they are approximate.

| Area | Papers |
|---|---|
| Moles and concentration | 27 |
| Empirical formula | 23 |
| Electronic configuration | 22 |
| Isotopes | 21 |
| Chromatography | 19 |
| Titration | 18 |
| Electrolysis | 18 |
| Rusting and corrosion | 16 |
| Halogens / Group 7 | 15 |
| Alkali metals / Group 1 | 10 |
| Dot-and-cross diagrams | 10 |
| Ion tests and precipitates | about 7–12 |
| Exothermic and endothermic reactions | 18 |
| Bond energies | 17 |
| Rates | 20 |
| Catalysts | 30 |
| Equilibrium | 15 |
| Crude oil | 23 |
| Cracking | 16 |
| Alkenes | 18 |
| Ethanol and alcohols | 30 |
| Carboxylic acids | 25 |
| Esters | 22 |
| Polymers | 19 |
| Condensation polymers | 6 |

Principles (Topic 1) and organic chemistry (Topic 4) each take roughly a third of the marks. Inorganic and physical chemistry share the rest.
