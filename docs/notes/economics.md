# Economics (4EC1): build notes

## Confirmed from the corpus

- The qualification is International GCSE Economics 4EC1, with two papers:
  - 4EC1/01: Microeconomics and Business Economics
  - 4EC1/02: Macroeconomics and the Global Economy
- Each paper is 1 h 30 min and 80 marks, with calculators allowed. Each has four compulsory 20-mark questions in a fixed order. The slots in `data/spec/economics.json` follow the real part order.
- Levels bands are 6 (AO2/AO3), 9 (AO2/AO3/AO4) and 12 (AO2/AO3/AO4, 4 marks each).
- This agrees with GOAL.md section 2 (4EC1, Papers 1 and 2).

## Spec references

- Refs have been checked against the official 4EC1 specification (Issue 3, now in the corpus).
- The numbering is:
  - topic areas 1.1 and 1.2 (Paper 1), 2.1 and 2.2 (Paper 2)
  - content sections x.x.x
  - lettered learning points, written as e.g. `1.1.3(a)`
- Several bank subtopics share one official section. For example, demand, supply and price are all in 1.1.3.
- A few bank subtopics are filed under a different topic from their official ref, because the subtopic ids had to stay stable:
  - `intervention` maps to 1.2.6(a–b)
  - `government` maps to 1.1.5(j–k) and 1.2.6(c)
- Point summaries are our own words.

## Caveats

- **AD/AS:** confirmed absent from the specification, so it is not included. GOAL.md mentions AD/AS diagrams.
- **Economic cycle:** uses the spec's stage names (boom, downturn, recession, recovery).
- **Content possibly beyond the spec:**
  - Maximum and minimum price items were removed: the spec names only the minimum wage. The generator filters them out and adds `intervention-pol-*` items on taxes, subsidies, fines, regulation and permits (`economics_kbint.py`). It uses a separate RNG, so no other ids changed.
  - Nationalisation and integration types are not named in the spec.
  - Aims of workers and of government in `assumptions` are also beyond it: the spec names only consumers and businesses.
- **Corpus:** 118 text files across 12 series (June 2019 to June 2025, including R papers), plus the spec.

## Generator

- **Entry point:** `scripts/gen/economics.py`, seeded and deterministic.
- **Helpers:**
  - `economics_spec.py`: spec and paper structure
  - `economics_util.py`: contexts and template filling
  - `economics_kb1-4.py`: original knowledge base for each spec topic
  - `economics_calc.py`: numeric generators using exact `Fraction` arithmetic
  - `economics_diag.py` and `economics_svg.py`: diagram items and SVG
- **Contexts:** fictional people and firms in real cities, and fictional countries for macroeconomic data.
- **`calculate` command word:** items are tagged `Calculate`. A few stems read "Work out", a wording used to avoid overlap with the corpus.

## Final counts

- **Total:** 4957 questions.
  - By topic: market-system 1621, business 1184, government 1484, global 668.
  - By qtype: explain 668, mcq 666, analyse 530, describe 516, state 474, assess 464, define 436, calculate 414, evaluate 352, diagram 241, data-response 196.
- **Checks:** every subtopic × qtype cell has at least 12 questions. `validate_bank.py economics` passes, and `similarity_check.py economics` flags 0 (worst overlap 0.133).
