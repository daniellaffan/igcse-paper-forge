# Style guide: Further Pure Mathematics 4PM1 (Papers 1 and 2)

This guide is based on the question papers, mark schemes and examiner reports for 4PM1 in the private corpus (2019 to 2025). It describes them in my own words. Nothing is quoted beyond a few words.

## 1. Paper anatomy

- **Two papers, 01 and 02.** Both have the same format: 2 hours, 100 marks, calculator allowed. Each is worth 50% of the qualification. The papers are not tiered. Grades run from 9 to 4, and a grade 3 is allowed.
- **No sections and no choice.** The cover asks candidates to answer every question. The number of questions is printed on the cover and varies from ten to twelve between series, with eleven the most common. Question totals range from 3 to 18 marks. Most fall between 6 and 12.
- **Ordering.** The early questions are short single-topic items worth 3–7 marks: a surd or log manipulation, a sector, a binomial coefficient, a straight line. The second half of the paper is made of long structured questions worth 10–18 marks. Each one chains several skills, for example roots of a quadratic, then new roots, then a new equation; or a curve, then its tangent, then an area, then a volume.
- **Cover rubric.** The cover asks for black ink and says to answer in the spaces provided. It states that every stage of working must be shown and that answers without working may get no credit. Candidates are told where the formulae page is. The marks for each part appear in brackets. The usual advice follows: read carefully, watch the time, check answers.
- **Formulae page** (Appendix 4 of the spec, reproduced as `further-maths-formulae`). It gives:
  - the areas and volumes of standard solids
  - the sums of arithmetic and geometric series, and the sum to infinity
  - the binomial series for positive integer and rational $n$, with its validity condition
  - the quotient rule
  - the trigonometric addition formulae
  - the change-of-base rule for logarithms

  Candidates must remember the sine and cosine rules, sector formulae in radians, $\frac{\mathrm d}{\mathrm dx}$ of $\sin$, $\cos$ and $\mathrm e^{x}$, and the product and chain rules.
- **Furniture.**
  - Each question ends with a total line, and the paper ends with a paper total.
  - Long questions leave a whole page or more of working space.
  - Geometric diagrams carry the "not accurately drawn" note; this appears about 120 times across the papers. Grids for graph questions are printed at true scale without it.
  - Tables to complete, for graph plotting, are printed with blank cells.

## 2. Question types (qtypes) and tariffs

Command-word counts in the question papers: *Find* about 340, *Show that* about 100, *Hence* about 90, *Use* about 50, *Write down* and *Solve* about 18 each, *Calculate* 14, *Express* 9, *Sketch* 5.

| qtype | What it looks like | Tariff | Command words |
|---|---|---|---|
| `short` | One technique, one answer: evaluate a sum, find a coefficient, solve a log or trig equation, differentiate, find an equation of a tangent, use the sine or cosine rule | 3–6 | Find, Solve, Evaluate, Differentiate, Write down |
| `multi-part` | (a), (b), (c)... in one setting, each part feeding the next with "hence" links: roots → new equation; expansion → coefficient → estimate; curve → stationary points → range of $k$; vectors in a triangle → $\lambda$ and $\mu$ | 7–16 | Find, Hence, Use your answer to |
| `show-that` | The answer is printed and the candidate must reach it legitimately: identities, given equations, given derivatives, given expressions for a volume or area | 3–8 | Show that, Prove, Verify |
| `graph` | Draw or read graphs: complete a table and plot a curve, add a straight line to solve an equation, shade a region for inequalities, sketch with intercepts and asymptotes | 4–12 | Complete, Draw, Sketch, Use your graph, By drawing a suitable line |
| `applied` | Calculus or series in context: kinematics, rates of change, optimisation (box, can, pen), salary, depreciation, bouncing ball, 3D trigonometry | 5–12 | Find, Show that, Use calculus to |

**Stem patterns.** Most stems open with a definition such as "The curve $C$ has equation ...", "$f(x) = ...$ where $p$ and $q$ are constants" or "In triangle $OAB$ ...". A diagram usually follows. Each part is then a single-line instruction. Answer forms are often specified: "in the form $ax + by + c = 0$ where $a$, $b$ and $c$ are integers", "exact", "in terms of $\pi$", "as a simplified surd". Required accuracy is stated (3 s.f. or 1 d.p.), and angles are in degrees unless radians are stated. Contexts are few and plain: particles on a line, containers filling, cuboids and pyramids, fields, savings plans. In-paper names are rare.

**How difficulty ramps.**

- **1–3:** single routine steps, such as the midpoint and distance, a sector arc and area, or the derivative of a polynomial.
- **4–6:** two or three linked steps or a reverse step: find $n$ from $S_n$, find $k$ from a coefficient, find a tangent, a sine-rule angle with an ambiguity check.
- **7–9:** algebraic linking of two topics: symmetric functions of roots, rational-index expansion followed by an approximation, intersecting vector lines, total distance when velocity changes sign, optimisation with justification, quadratics in $\sin x$ with one root rejected.

## 3. How the mark scheme is written

- **Layout.** There is a table per question with columns *Part*, *Working/Answer*, *Mark* and *Notes*. Every scoring step has its own row. Totals are given per part and per question.
- **Mark types.**
  - **M** is a method mark, given for the right approach even with slips.
  - **A** is an accuracy mark and depends on the preceding M.
  - **B** is independent.
  - **dM** (dependent method) needs the previous M. In the bank it is written as `M1` with `dM1` in the notes, so the validator can parse it.
- **Abbreviations:** cao, cso (correct solution only, used for every show-that), ft, isw, oe, awrt, SC, eeoo, dep.
- **General principles** appear at the start of every scheme:
  - **Solving a quadratic.** M1 is earned by factorising so that the brackets give the correct $x^2$ and constant terms, or by a correct formula or completing the square. Calculator-only solutions of a wrong quadratic lose the M mark.
  - **Differentiation.** At least one power must drop by one.
  - **Integration.** At least one power must rise by one, and limits must be substituted and subtracted.
  - **Show that.** Every step must be seen, and the final line must match the printed result (cso).
- **Alternative methods.** These are set out in full as "ALT" blocks with their own rows, for example a scalar-product route versus a gradient route, or the cosine rule versus right-angled trigonometry.
- **AO split** (spec): AO1 30–40%, AO2 20–30%, AO3 35–50%. In the bank: `short` → AO1; `multi-part` and `graph` → AO1 and AO3; `show-that` → AO3 and AO1; `applied` → AO2 and AO3.

## 4. What examiner reports say

- **Show-that questions** score poorly when steps are skipped or the printed answer is "reached" by working backwards. Strong answers write every intermediate line and a conclusion.
- **"Hence" links.** Weak candidates restart from scratch instead of using an earlier part. Strong candidates spot that part (a) builds the tool for part (b).
- **Quadratic solving.** Solving a wrong quadratic on a calculator with no method shown loses the M mark. Reports keep saying to show the factorisation or the formula.
- **Constant of integration.** It is often missed when a curve is found from $\frac{\mathrm dy}{\mathrm dx}$ or a displacement is found from velocity.
- **Kinematics.** Candidates give displacement when distance is asked. Strong answers find where $v = 0$ and split the interval.
- **Binomial.** Common errors are sign errors with negative or fractional $n$, forgetting to take out the constant in $(a + bx)^n$, and missing the validity range.
- **Trigonometric equations.** Candidates lose solutions by not extending the interval for $kx + c$, and leave in roots outside $[-1, 1]$. Degrees and radians get mixed up in sector work.
- **Vectors.** Direction errors are frequent ($\overrightarrow{AB} = \mathbf b - \mathbf a$). Strong answers equate the coefficients of $\mathbf a$ and $\mathbf b$ explicitly.
- **Logs.** The laws are misapplied, for example $\log(a + b)$ split into $\log a + \log b$. Candidates also fail to check that roots are valid for the original log equation.

## 5. Topic frequency

These counts come from a keyword scan of 487 questions in the corpus. A question can count under more than one topic.

| Spec area | Approx. count | Typical form |
|---|---|---|
| Coordinate geometry (8) | 100 | Lines, perpendiculars, ratio division, triangle area; often in a long question |
| Triangles: sine and cosine rules, area (10D) | 99 | Short items and 3D or field contexts |
| Logs and indices (1) | 88 | Solve log equations, change of base, $\log y$ against $x$ graphs |
| Series: AP and GP (5) | 79 | Find $a$, $d$ or $r$; least $n$; sum to infinity; context |
| Differentiation (9A/9B) | 76 | Product, quotient and chain rules; show a given derivative |
| Trig identities (10E–10G) | 68 | Prove, then "hence solve" |
| Binomial (6) | 67 | Coefficients, unknown $k$, rational index, validity, estimate |
| Inequalities (3D/3E) | 67 | Linear and quadratic; regions on a grid |
| Integration, areas (9C) | 51 | Area between curve and line or axis |
| Roots of quadratics (2C) | 46 | $\alpha^2 + \beta^2$, new equations with given roots |
| Stationary points, max/min (9D/9E) | 36 | Nature tests, optimisation |
| Asymptotes and curve sketching (4A) | 34 | Rational functions |
| Tangents and normals (9F) | 31 | Equation, then a triangle or area |
| Radians, sectors (10A) | 30 | Arc, sector, segment, perimeter |
| Vectors (7) | 29 | Triangle and parallelogram geometry, $\lambda$ and $\mu$ |
| 3D trigonometry (10C) | 29 | Cuboids, pyramids, line–plane angles |
| Graphical solution (4B) | 27 | Draw a line to solve an equation |
| Completing the square (2A) | 23 | Minimum point, range |
| Volumes of revolution (9C) | 20 | About the $x$-axis, exact in $\pi$ |
| Kinematics (9C) | 19 | Velocity and acceleration, distance |
| Factor and remainder theorem (3A/3B) | 18 | Find constants, factorise a cubic |
| Trig equations (10H) | 11 | Often inside an identity question |
| Sigma notation (5A) | 9 | Evaluate or show a sum formula |

## 6. How the bank follows this

- Every question uses KaTeX in `$...$`.
- Geometry figures are SVG with the "Diagram NOT accurately drawn" note. Graph-paper grids carry no note.
- Mark schemes use M/A/B rows with dM, cso, oe, ft and awrt in the notes. Show-that rows are marked to the printed answer.
- All values are computed with sympy in the template and stored with `checked: true`.
