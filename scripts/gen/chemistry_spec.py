"""Builds data/spec/chemistry.json (4CH1, separate science) and the periodic-table
reference sheet data/reference/chemistry-periodic-table.json.

Point refs are the specification's own statement numbers (1.1 ... 4.50C). Statements
with a 'C' suffix are printed in bold in the specification and are assessed only on
Paper 2C, so they carry paper2_only. Summaries are our own plain-English wording.
"""
import json
from pathlib import Path

from chemistry_util import EL

ROOT = Path(__file__).resolve().parents[2]

QTYPES = [
    {"id": "mcq", "label": "Multiple choice", "marks": "1",
     "description": "Choose one of four options A–D and mark it with a cross."},
    {"id": "recall", "label": "Recall: state / give / name", "marks": "1-3",
     "description": "Short factual answers: name a substance, give a formula, state a condition or colour."},
    {"id": "describe", "label": "Describe", "marks": "2-4",
     "description": "Give an account of observations, a process or a test, without needing reasons."},
    {"id": "explain", "label": "Explain", "marks": "2-5",
     "description": "Give reasons using structure, bonding, particles or electrons; linked marking points."},
    {"id": "calculation", "label": "Calculation", "marks": "2-5",
     "description": "Moles, masses, concentrations, gas volumes, yields, energy changes, Rf values; working shown."},
    {"id": "equation", "label": "Equations", "marks": "1-3",
     "description": "Word equations, balanced symbol equations with state symbols, ionic and half-equations."},
    {"id": "practical", "label": "Practical skills", "marks": "2-6",
     "description": "Methods, apparatus, variables, safety, sources of error and improvements for set practicals."},
    {"id": "data", "label": "Data and graphs", "marks": "2-8",
     "description": "Read, plot and interpret tables and graphs; spot trends, anomalies and draw conclusions."},
    {"id": "extended", "label": "Extended response (6 marks)", "marks": "6",
     "description": "A longer description or explanation, e.g. a full method or a linked chain of reasoning."},
]

P12 = ["1C", "2C"]

# topic id, ref, title, [subtopics]
# subtopic: (id suffix, ref, title, summary, qtypes, [(point ref, summary)])
TOPICS = [
 ("principles", "1", "Principles of chemistry", [
  ("states", "1(a)", "States of matter and solutions",
   "Particle model of solids, liquids and gases, changes of state, diffusion, solutions and solubility.",
   ["mcq", "recall", "explain", "calculation", "practical", "data"],
   [("1.1", "Describe solids, liquids and gases by how their particles are arranged, move and how much energy they have."),
    ("1.2", "Name the changes of state, say how each is brought about and what happens to the particles."),
    ("1.3", "Use moving particles to explain diffusion of gases and the dilution of coloured solutions."),
    ("1.4", "Know the meanings of solvent, solute, solution and saturated solution."),
    ("1.5C", "Solubility is the mass of solute in grams that dissolves in 100 g of solvent."),
    ("1.6C", "Draw solubility curves and read information from them."),
    ("1.7C", "Practical: find how much of a solid dissolves in water at a chosen temperature.")]),
  ("mixtures", "1(b)", "Elements, compounds and mixtures",
   "Telling elements, compounds and mixtures apart, purity, separation techniques and chromatography.",
   ["mcq", "recall", "describe", "explain", "calculation", "practical", "data", "extended"],
   [("1.8", "Decide whether a substance is an element, a compound or a mixture."),
    ("1.9", "Pure substances melt and boil at one fixed temperature; mixtures change state over a range."),
    ("1.10", "Describe simple and fractional distillation, filtration, crystallisation and paper chromatography."),
    ("1.11", "Use a chromatogram to work out what a mixture contains."),
    ("1.12", "Calculate Rf values and use them to identify substances."),
    ("1.13", "Practical: separate inks or food colourings by paper chromatography.")]),
  ("atoms", "1(c)", "Atomic structure",
   "Protons, neutrons and electrons, atomic and mass numbers, isotopes and relative atomic mass.",
   ["mcq", "recall", "explain", "calculation"],
   [("1.14", "Know what atoms and molecules are."),
    ("1.15", "Know where protons, neutrons and electrons are found and their relative masses and charges."),
    ("1.16", "Define atomic number, mass number, isotopes and relative atomic mass."),
    ("1.17", "Work out a relative atomic mass from isotope masses and their abundances.")]),
  ("periodic", "1(d)", "The Periodic Table",
   "How the table is arranged, electron configurations, metals and non-metals, and group properties.",
   ["mcq", "recall", "explain"],
   [("1.18", "Elements are placed in order of atomic number, in groups (columns) and periods (rows)."),
    ("1.19", "Work out the electronic configuration of elements 1 to 20 from their place in the table."),
    ("1.20", "Use electrical conductivity and whether the oxide is acidic or basic to sort metals from non-metals."),
    ("1.21", "Tell whether an element is a metal or non-metal from where it sits in the table."),
    ("1.22", "Link the group and period of a main-group element to its electron arrangement."),
    ("1.23", "Elements in the same group react similarly because they have the same number of outer electrons."),
    ("1.24", "Noble gases are unreactive because their outer shells are full.")]),
  ("formulae", "1(e)", "Formulae, equations and calculations",
   "Writing equations, relative formula mass, moles, reacting masses, yields, empirical formulae, "
   "solution concentrations and gas volumes.",
   ["mcq", "equation", "calculation", "practical", "data"],
   [("1.25", "Write word equations and balanced symbol equations with state symbols, including for unfamiliar reactions."),
    ("1.26", "Calculate relative formula mass (Mr) from relative atomic masses."),
    ("1.27", "The mole is the unit for amount of substance."),
    ("1.28", "Convert between mass, moles and Mr or Ar."),
    ("1.29", "Calculate reacting masses from an equation or experimental results."),
    ("1.30", "Calculate the percentage yield of a reaction."),
    ("1.31", "Find formulae by experiment, e.g. metal oxides and the water in hydrated salts."),
    ("1.32", "Know the difference between an empirical formula and a molecular formula."),
    ("1.33", "Calculate empirical and molecular formulae from experimental data."),
    ("1.34C", "Calculations linking moles, solution volume and concentration in mol/dm³."),
    ("1.35C", "Calculations using the molar gas volume: 24 dm³ (24 000 cm³) per mole at rtp."),
    ("1.36", "Practical: find the formula of a metal oxide by burning a metal or reducing an oxide.")]),
  ("ionic", "1(f)", "Ionic bonding",
   "How ions form, ion charges and formulae, dot-and-cross diagrams and properties of ionic compounds.",
   ["mcq", "recall", "describe", "explain"],
   [("1.37", "Ions form when atoms lose or gain electrons."),
    ("1.38", "Know the charges of ions from Groups 1, 2, 3, 5, 6, 7 and of common transition metal and compound ions."),
    ("1.39", "Write formulae of compounds made from these ions."),
    ("1.40", "Draw dot-and-cross diagrams showing electron transfer to form ionic compounds."),
    ("1.41", "Ionic bonding is strong electrostatic attraction between oppositely charged ions."),
    ("1.42", "Giant ionic lattices have high melting and boiling points because many strong attractions must be overcome."),
    ("1.43", "Ionic compounds conduct when molten or dissolved but not when solid.")]),
  ("covalent", "1(g)", "Covalent bonding and structures",
   "Shared electron pairs, dot-and-cross diagrams, simple molecular and giant covalent structures.",
   ["mcq", "recall", "explain", "data", "extended"],
   [("1.44", "A covalent bond is a shared pair of electrons between two atoms."),
    ("1.45", "Covalent bonds are attractions between the shared electrons and the nuclei."),
    ("1.46", "Draw dot-and-cross diagrams for simple molecules such as H₂, Cl₂, HCl, H₂O, NH₃, CO₂, CH₄ and C₂H₄."),
    ("1.47", "Simple molecular substances have low melting and boiling points: weak forces between molecules."),
    ("1.48", "Boiling points of simple molecular substances generally rise as molecules get bigger."),
    ("1.49", "Giant covalent substances have high melting points: many strong covalent bonds to break."),
    ("1.50", "Relate the structures of diamond, graphite and C₆₀ to hardness and conductivity."),
    ("1.51", "Covalent substances usually do not conduct electricity.")]),
  ("metallic", "1(h)", "Metallic bonding",
   "The metal lattice of positive ions in a sea of electrons and how it explains metal properties.",
   ["mcq", "recall", "explain"],
   [("1.52C", "Draw a 2-D diagram of a metallic lattice."),
    ("1.53C", "Metallic bonding is attraction between positive ions and delocalised electrons."),
    ("1.54C", "Explain why metals conduct electricity and are malleable.")]),
  ("electrolysis", "1(i)", "Electrolysis",
   "Why ionic substances conduct when molten or dissolved, products at each electrode and half-equations.",
   ["mcq", "recall", "explain", "equation", "practical", "extended"],
   [("1.55C", "Covalent compounds do not conduct because they have no ions or free electrons."),
    ("1.56C", "Ionic compounds conduct only when molten or dissolved because the ions can then move."),
    ("1.57C", "Anions are negative ions; cations are positive ions."),
    ("1.58C", "Describe electrolysis of molten salts and of solutions with inert electrodes and predict the products."),
    ("1.59C", "Write half-equations at each electrode and say which is oxidation and which is reduction."),
    ("1.60C", "Practical: electrolyse aqueous solutions.")]),
 ]),
 ("inorganic", "2", "Inorganic chemistry", [
  ("group1", "2(a)", "Group 1: the alkali metals",
   "Reactions of lithium, sodium and potassium with water and air, the reactivity trend and predictions.",
   ["mcq", "recall", "describe", "explain", "equation", "data"],
   [("2.1", "Similar reactions with water show lithium, sodium and potassium belong to one family."),
    ("2.2", "Differences in their reactions with air and water show reactivity increases down the group."),
    ("2.3", "Predict properties of other alkali metals from the group trends."),
    ("2.4C", "Explain the reactivity trend using electron shells and attraction for the outer electron.")]),
  ("group7", "2(b)", "Group 7: the halogens",
   "Colours, states and trends of chlorine, bromine and iodine, displacement reactions and reactivity.",
   ["mcq", "recall", "explain", "equation", "practical", "data"],
   [("2.5", "Know the colours and states of chlorine, bromine and iodine and how their physical properties change down the group."),
    ("2.6", "Predict properties of other halogens from the trends."),
    ("2.7", "Use halogen/halide displacement reactions to show reactivity falls down the group."),
    ("2.8C", "Explain the reactivity trend using electron shells and attraction for an incoming electron.")]),
  ("air", "2(c)", "Gases in the atmosphere",
   "Composition of air, measuring the oxygen in air, burning elements in oxygen, carbon dioxide and climate.",
   ["mcq", "recall", "describe", "equation", "calculation", "practical"],
   [("2.9", "Know the rough percentages of nitrogen, oxygen, argon and carbon dioxide in dry air."),
    ("2.10", "Find the percentage of oxygen in air by reacting it with a metal or non-metal."),
    ("2.11", "Describe how magnesium, hydrogen and sulfur burn in oxygen."),
    ("2.12", "Metal carbonates such as copper(II) carbonate decompose on heating to give carbon dioxide."),
    ("2.13", "Carbon dioxide is a greenhouse gas; rising levels may contribute to climate change."),
    ("2.14", "Practical: find the approximate percentage by volume of oxygen in air.")]),
  ("reactivity", "2(d)", "Reactivity series, rusting and redox",
   "Ordering metals by their reactions and displacements, rusting and its prevention, oxidation and reduction.",
   ["mcq", "recall", "explain", "equation", "practical", "data", "extended"],
   [("2.15", "Put metals in a reactivity order from their reactions with water and dilute acids."),
    ("2.16", "Put metals in order using displacement from metal oxides and from salt solutions."),
    ("2.17", "Know the order: K, Na, Li, Ca, Mg, Al, Zn, Fe, Cu, Ag, Au."),
    ("2.18", "Iron rusts only when both water and oxygen are present."),
    ("2.19", "Prevent rusting by barriers, galvanising or sacrificial protection."),
    ("2.20", "Define oxidation, reduction, redox, oxidising agent and reducing agent by oxygen and by electrons."),
    ("2.21", "Practical: react metals such as magnesium, zinc and iron with dilute acids.")]),
  ("extraction", "2(e)", "Extraction and uses of metals",
   "Ores, choosing an extraction method from reactivity, uses of metals and why alloys are harder.",
   ["mcq", "recall", "explain", "data"],
   [("2.22C", "Most metals come from ores; very unreactive metals are found uncombined."),
    ("2.23C", "The extraction method depends on reactivity: carbon for iron, electrolysis for aluminium."),
    ("2.24C", "Comment on an unfamiliar extraction process from information given."),
    ("2.25C", "Explain uses of aluminium, copper, iron and steels from their properties."),
    ("2.26C", "An alloy is a mixture of a metal with other elements, usually metals or carbon."),
    ("2.27C", "Alloys are harder because different-sized atoms stop layers sliding.")]),
  ("acids", "2(f)", "Acids, alkalis and titrations",
   "Indicators, the pH scale, H⁺ and OH⁻ ions, neutralisation and carrying out a titration.",
   ["mcq", "recall", "describe", "calculation", "practical"],
   [("2.28", "Use litmus, phenolphthalein and methyl orange to tell acids from alkalis."),
    ("2.29", "Use pH 0–14 to class solutions from strongly acidic to strongly alkaline."),
    ("2.30", "Use universal indicator to estimate pH."),
    ("2.31", "Acids give H⁺ ions in water; alkalis give OH⁻ ions."),
    ("2.32", "Alkalis neutralise acids."),
    ("2.33C", "Describe how to carry out an acid–alkali titration.")]),
  ("salts", "2(g)", "Acids, bases and making salts",
   "Solubility rules, proton transfer, reactions of acids, and preparing soluble and insoluble salts.",
   ["mcq", "recall", "equation", "practical", "extended"],
   [("2.34", "Use the solubility rules for sodium, potassium, ammonium, nitrates, chlorides, sulfates, carbonates and hydroxides."),
    ("2.35", "Acid–base reactions involve transfer of protons."),
    ("2.36", "An acid donates protons; a base accepts them."),
    ("2.37", "Reactions of hydrochloric, sulfuric and nitric acids with metals, bases and carbonates to make salts."),
    ("2.38", "Metal oxides, hydroxides and ammonia are bases; alkalis are soluble bases."),
    ("2.39", "Make a pure, dry soluble salt from an acid and an insoluble reactant."),
    ("2.40C", "Make a pure, dry soluble salt from an acid and an alkali."),
    ("2.41C", "Make a pure, dry insoluble salt by mixing two soluble reactants."),
    ("2.42", "Practical: make pure, dry hydrated copper(II) sulfate crystals from copper(II) oxide."),
    ("2.43C", "Practical: make a pure, dry sample of lead(II) sulfate.")]),
  ("tests", "2(h)", "Chemical tests",
   "Tests for gases, flame tests, tests for cations and anions, and tests for water and its purity.",
   ["mcq", "recall", "describe", "data", "extended"],
   [("2.44", "Test for hydrogen, oxygen, carbon dioxide, ammonia and chlorine."),
    ("2.45", "Describe how to do a flame test."),
    ("2.46", "Flame colours: Li⁺ red, Na⁺ yellow, K⁺ lilac, Ca²⁺ orange-red, Cu²⁺ blue-green."),
    ("2.47", "Test for NH₄⁺, Cu²⁺, Fe²⁺ and Fe³⁺ with sodium hydroxide solution."),
    ("2.48", "Test for halide, sulfate and carbonate ions."),
    ("2.49", "Test for water with anhydrous copper(II) sulfate."),
    ("2.50", "Use melting or boiling point to show whether water is pure.")]),
 ]),
 ("physical", "3", "Physical chemistry", [
  ("energetics", "3(a)", "Energetics",
   "Exothermic and endothermic changes, calorimetry, Q = mcΔT, molar enthalpy changes, energy diagrams "
   "and bond energies.",
   ["mcq", "recall", "explain", "calculation", "practical", "data"],
   [("3.1", "Exothermic reactions give out heat; endothermic reactions take heat in."),
    ("3.2", "Describe simple calorimetry for combustion, displacement, dissolving and neutralisation."),
    ("3.3", "Calculate heat energy change with Q = mcΔT."),
    ("3.4", "Calculate a molar enthalpy change ΔH from Q and the moles reacting."),
    ("3.5C", "Draw and explain energy level diagrams for exothermic and endothermic reactions."),
    ("3.6C", "Breaking bonds takes in energy; making bonds gives energy out."),
    ("3.7C", "Calculate an enthalpy change from bond energies."),
    ("3.8", "Practical: measure temperature changes when salts dissolve, in neutralisation, displacement and combustion.")]),
  ("rates", "3(b)", "Rates of reaction",
   "Measuring rates, the effect of surface area, concentration, pressure, temperature and catalysts, and "
   "collision theory.",
   ["mcq", "recall", "explain", "calculation", "practical", "data", "extended"],
   [("3.9", "Describe experiments to see how surface area, concentration, temperature and catalysts change the rate."),
    ("3.10", "Describe how these factors and gas pressure affect the rate."),
    ("3.11", "Explain the effects using collision theory: frequency and energy of collisions."),
    ("3.12", "A catalyst speeds up a reaction but is chemically unchanged at the end."),
    ("3.13", "A catalyst provides another route with a lower activation energy."),
    ("3.14C", "Draw and explain reaction profiles showing ΔH and activation energy."),
    ("3.15", "Practical: marble chips and hydrochloric acid – effect of chip size and acid concentration."),
    ("3.16", "Practical: compare solids as catalysts for decomposing hydrogen peroxide.")]),
  ("equilibria", "3(c)", "Reversible reactions and equilibria",
   "Reversible reactions, dynamic equilibrium and the effect of temperature, pressure and catalysts.",
   ["mcq", "recall", "explain", "data"],
   [("3.17", "Some reactions are reversible, shown by ⇌."),
    ("3.18", "Examples: dehydrating hydrated copper(II) sulfate, heating ammonium chloride."),
    ("3.19C", "A reversible reaction in a closed system can reach dynamic equilibrium."),
    ("3.20C", "At equilibrium forward and back rates are equal and concentrations stay constant."),
    ("3.21C", "A catalyst does not change the equilibrium position; it speeds both directions equally."),
    ("3.22C", "Raising temperature favours the endothermic direction; raising pressure favours fewer gas moles.")]),
 ]),
 ("organic", "4", "Organic chemistry", [
  ("intro", "4(a)", "Introduction to organic chemistry",
   "Hydrocarbons, types of formula, homologous series, functional groups, isomers, naming and reaction types.",
   ["mcq", "recall", "explain"],
   [("4.1", "A hydrocarbon contains hydrogen and carbon only."),
    ("4.2", "Use empirical, molecular, general, structural and displayed formulae."),
    ("4.3", "Know what homologous series, functional group and isomers mean."),
    ("4.4", "Name compounds of up to six carbons using IUPAC rules."),
    ("4.5", "Draw possible structures (isomers) for a given molecular formula."),
    ("4.6", "Classify organic reactions as substitution, addition or combustion.")]),
  ("crude", "4(b)", "Crude oil, fuels and cracking",
   "Fractional distillation of crude oil, fractions and their uses, combustion and pollution, and cracking.",
   ["mcq", "recall", "describe", "explain", "equation", "extended"],
   [("4.7", "Crude oil is a mixture of hydrocarbons."),
    ("4.8", "Describe how fractional distillation separates crude oil into fractions."),
    ("4.9", "Name the main fractions and give a use of each."),
    ("4.10", "Know how colour, boiling point and viscosity change across the fractions."),
    ("4.11", "A fuel releases heat energy when it burns."),
    ("4.12", "Products of complete and incomplete combustion of hydrocarbons."),
    ("4.13", "Carbon monoxide is toxic because it reduces how much oxygen the blood can carry."),
    ("4.14", "High engine temperatures make nitrogen and oxygen react to form oxides of nitrogen."),
    ("4.15", "Sulfur impurities in fuels burn to form sulfur dioxide."),
    ("4.16", "Sulfur dioxide and nitrogen oxides cause acid rain."),
    ("4.17", "Cracking breaks long alkanes into shorter alkanes and alkenes (silica or alumina, 600–700 °C)."),
    ("4.18", "Cracking matches supply to demand for the more useful short-chain fractions.")]),
  ("alkanes", "4(c)", "Alkanes",
   "General formula, saturation, structures and names, and substitution with halogens in UV light.",
   ["mcq", "recall", "explain", "equation"],
   [("4.19", "The alkane general formula is CₙH₂ₙ₊₂."),
    ("4.20", "Alkanes are saturated: only single C–C bonds."),
    ("4.21", "Draw and name alkanes and their straight-chain isomers up to five carbons."),
    ("4.22", "Alkanes react with halogens in UV light, replacing one hydrogen atom.")]),
  ("alkenes", "4(d)", "Alkenes",
   "The C=C functional group, general formula, structures and names, and addition of bromine.",
   ["mcq", "recall", "describe", "equation"],
   [("4.23", "Alkenes contain a carbon–carbon double bond."),
    ("4.24", "The alkene general formula is CₙH₂ₙ."),
    ("4.25", "Alkenes are unsaturated because of the C=C bond."),
    ("4.26", "Draw and name alkenes and their straight-chain isomers up to four carbons."),
    ("4.27", "Alkenes add bromine to form dibromoalkanes."),
    ("4.28", "Use bromine water to tell an alkene from an alkane.")]),
  ("alcohols", "4(e)", "Alcohols",
   "The –OH group, the first four alcohols, oxidation of ethanol and the two ways of making ethanol.",
   ["mcq", "recall", "explain", "equation", "extended"],
   [("4.29C", "Alcohols contain the –OH functional group."),
    ("4.30C", "Draw and name methanol, ethanol, propan-1-ol and butan-1-ol."),
    ("4.31C", "Ethanol can be oxidised by burning, by microbes in air, or by acidified potassium dichromate(VI)."),
    ("4.32C", "Ethanol is made from ethene and steam (phosphoric acid, 300 °C, 60–70 atm) or by fermenting glucose with yeast."),
    ("4.33C", "Explain why fermentation needs no air and a temperature of about 30 °C.")]),
  ("acids", "4(f)", "Carboxylic acids",
   "The –COOH group, the first four acids, their reactions with metals and carbonates, and vinegar.",
   ["mcq", "recall", "equation"],
   [("4.34C", "Carboxylic acids contain the –COOH functional group."),
    ("4.35C", "Draw and name straight-chain carboxylic acids with up to four carbons."),
    ("4.36C", "Carboxylic acid solutions react with metals and carbonates."),
    ("4.37C", "Vinegar is a solution of ethanoic acid in water.")]),
  ("esters", "4(g)", "Esters",
   "The ester link, making ethyl ethanoate, naming and drawing esters, and their uses.",
   ["mcq", "recall", "equation", "practical"],
   [("4.38C", "Esters contain the –COO– functional group."),
    ("4.39C", "Ethanol and ethanoic acid with an acid catalyst give ethyl ethanoate."),
    ("4.40C", "Draw the structural and displayed formulae of ethyl ethanoate."),
    ("4.41C", "Work out an ester's structure from its alcohol and acid, and the reverse."),
    ("4.42C", "Esters are volatile, smell distinctive and are used in flavourings and perfumes."),
    ("4.43C", "Practical: prepare an ester such as ethyl ethanoate.")]),
  ("polymers", "4(h)", "Synthetic polymers",
   "Addition polymers, repeat units and monomers, disposal problems, and condensation polyesters.",
   ["mcq", "recall", "explain", "equation"],
   [("4.44", "Addition polymers are made by joining many small monomer molecules."),
    ("4.45", "Draw repeat units of poly(ethene), poly(propene), poly(chloroethene) and PTFE."),
    ("4.46", "Work out the monomer from a repeat unit and the reverse."),
    ("4.47", "Addition polymers are hard to dispose of: inert, non-biodegradable and toxic gases when burned."),
    ("4.48C", "Condensation polymerisation of a dicarboxylic acid and a diol gives a polyester and water."),
    ("4.49C", "Draw the repeat unit of a polyester from its monomers, e.g. ethanedioic acid and ethanediol."),
    ("4.50C", "Some polyesters (biopolyesters) are biodegradable.")]),
 ]),
]

INSTR = ["Use black ink or ball-point pen.",
         "Write your name, centre number and candidate number in the boxes at the top of the cover.",
         "Answer all questions.",
         "Write your answers in the spaces provided – there may be more room than you need.",
         "Show every step of any calculation and give the units."]
ADVICE = ["Read each question carefully before you begin your answer.",
          "Write neatly and in clear, good English.",
          "Try to answer every question.",
          "If you have time at the end, check your answers."]


def paper(pid, code, name, minutes, marks, note):
    return {"id": pid, "name": name, "paper_code": code, "minutes": minutes, "marks": marks, "calculator": True,
            "materials": "Calculator, ruler",
            "instructions": INSTR,
            "information": [f"The total mark for this paper is {marks}.",
                            "The marks for each question are shown in brackets – use them as a guide to how "
                            "long to spend on each question.",
                            "Some questions are answered by putting a cross in a box. To change your mind, put "
                            "a line through the box and then cross your new answer.",
                            note],
            "advice": ADVICE, "reference_sheet": "chemistry-periodic-table", "answer_style": "in-booklet",
            "sections": [{"id": pid + "-all", "title": "Answer ALL questions.", "marks": marks}]}


def build():
    is_c = lambda ref: ref.endswith("C")
    topics = []
    for tid, tref, ttitle, subs in TOPICS:
        st_out = []
        for sid, sref, stitle, summ, qts, pts in subs:
            points = []
            for ref, s in pts:
                p = {"ref": ref, "summary": s}
                if is_c(ref):
                    p["paper2_only"] = True
                points.append(p)
            papers = ["2C"] if all(is_c(r) for r, _ in pts) else P12
            st_out.append({"id": f"chemistry.{tid}.{sid}", "ref": sref, "title": stitle, "summary": summ,
                           "papers": papers, "qtypes": qts, "points": points})
        topics.append({"id": f"chemistry.{tid}", "ref": tref, "title": ttitle, "papers": P12, "subtopics": st_out})
    spec = {
        "subject": "chemistry", "code": "4CH1",
        "board": "Pearson Edexcel International GCSE (9–1)",
        "title": "Chemistry", "short": "Chemistry 4CH1",
        "official_url": "https://qualifications.pearson.com/en/qualifications/edexcel-international-gcses/"
                        "international-gcse-chemistry-2017.html",
        "spec_url": "https://qualifications.pearson.com/content/dam/pdf/International%20GCSE/Chemistry/2017/"
                    "specification-and-sample-assessments/international-gcse-chemistry-2017-specification.pdf",
        "papers": [
            paper("1C", "4CH1/1C", "Paper 1C", 120, 110,
                  "Paper 1 tests only the content that is not marked 'C' (Paper 2-only) in the specification."),
            paper("2C", "4CH1/2C", "Paper 2C", 75, 70,
                  "Paper 2 can test any content, including the statements marked 'C'."),
        ],
        "qtypes": QTYPES,
        "topics": topics,
    }
    out = ROOT / "data" / "spec" / "chemistry.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(spec, ensure_ascii=False, indent=1))
    build_reference()
    return spec


# --------------------------------------------------------------- periodic table
LAYOUT = [
    ["H", None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, "He"],
    ["Li", "Be"] + [None] * 10 + ["B", "C", "N", "O", "F", "Ne"],
    ["Na", "Mg"] + [None] * 10 + ["Al", "Si", "P", "S", "Cl", "Ar"],
    ["K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr"],
    ["Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe"],
    ["Cs", "Ba", "La", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn"],
    ["Fr", "Ra", "Ac", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", None, None, None, None, None, None, None],
]


def cell(sym):
    if sym is None:
        return ""
    z, a, nm = EL[sym]
    star = "*" if sym in ("La", "Ac") else ""
    return f"{a}\n**{sym}{star}**\n{nm}\n{z}"


def build_reference():
    headers = ["1", "2"] + [""] * 10 + ["3", "4", "5", "6", "7", "0"]
    rows = [[cell(s) for s in r] for r in LAYOUT]
    ref = {
        "id": "chemistry-periodic-table",
        "title": "The Periodic Table of the Elements",
        "blocks": [
            {"type": "table", "headers": ["Key"],
             "rows": [["relative atomic mass\n**atomic symbol**\nname\natomic (proton) number"]],
             "caption": "How to read each box"},
            {"type": "table", "headers": headers, "rows": rows,
             "caption": "Group numbers are shown at the top of each main-group column; the central block holds "
                        "the transition metals. Periods run across in rows 1 to 7."},
            {"type": "source", "label": "Notes",
             "text": "* Elements 58–71 and 90–103 are not shown.\n"
                     "Relative atomic masses of copper (63.5) and chlorine (35.5) are not rounded to whole numbers.\n"
                     "Values in square brackets are mass numbers of the most stable isotope."},
        ],
    }
    out = ROOT / "data" / "reference" / "chemistry-periodic-table.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(ref, ensure_ascii=False, indent=1))
