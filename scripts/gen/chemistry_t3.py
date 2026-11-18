"""Topic 3 templates: physical chemistry (3(a) to 3(c))."""
import math
from fractions import Fraction as Fr

from chemistry_util import tpl, mcq, P, F, row, Q, num, Mr, EQ, fig, table, graph
from chemistry_kb import facts, items, extended
import chemistry_svg as S

EN = "chemistry.physical.energetics"
RA = "chemistry.physical.rates"
EQM = "chemistry.physical.equilibria"


def D(**k):
    return k


# =================================================================== 3(a) energetics
facts(EN, "3.1", [
    D(mq="What happens to the temperature of the surroundings during an exothermic reaction?", c="it increases", w=["it decreases", "it stays the same", "it falls then rises"]),
    D(mq="Which process is endothermic?", c="dissolving ammonium nitrate in water", w=["burning methane", "neutralising an acid with an alkali", "magnesium reacting with acid"]),
    D(mq="What is the sign of ΔH for an exothermic reaction?", c="negative", w=["positive", "zero", "it depends on the temperature"]),
    D(mq="Which equation is used to calculate the heat energy change in a calorimetry experiment?", c="Q = mcΔT", w=["Q = m/ΔT", "Q = cΔT/m", "Q = mΔT/c"], ref="3.3"),
    D(mq="What is the specific heat capacity of water used in calorimetry calculations?", c="4.2 J/g/°C", w=["1.0 J/g/°C", "42 J/g/°C", "0.42 J/g/°C"], ref="3.3"),
    D(mq="Why is a polystyrene cup used in calorimetry?", c="it is a good thermal insulator", w=["it is a good conductor", "it reacts with the solution", "it is transparent"], ref="3.2"),
    D(mq="Is bond breaking exothermic or endothermic?", c="endothermic", w=["exothermic", "neither", "it depends on the bond"], ref="3.6C"),
    D(mq="In an energy level diagram for an exothermic reaction, the products are", c="lower in energy than the reactants", w=["higher in energy than the reactants",
      "at the same energy as the reactants", "above the activation energy"], ref="3.5C", d="4-6"),
    D(mq="Why is a reaction exothermic overall?", c="more energy is released making bonds than is taken in breaking bonds", w=["more energy is taken in breaking bonds than released making bonds",
      "no bonds are broken", "the products have more energy than the reactants"], ref="3.6C", d="7-9"),
    D(mq="The units of molar enthalpy change are", c="kJ/mol", w=["J/g", "kJ", "°C/mol"], ref="3.4"),
    D(mq="Which change shows that a reaction is endothermic?", c="the temperature of the solution falls", w=["the solution fizzes", "a precipitate forms", "the temperature rises"]),
    D(mq="Which reaction has a positive ΔH?", c="thermal decomposition of calcium carbonate", w=["combustion of ethanol", "neutralisation", "rusting of iron"], d="4-6"),
], intro="This question is about energy changes in reactions.")

facts(EN, "3.1", [
    D(q="State what is meant by an **exothermic** reaction.", a="a reaction that gives out heat energy (to the surroundings)", n="ALLOW temperature of surroundings rises"),
    D(q="State what is meant by an **endothermic** reaction.", a="a reaction that takes in heat energy (from the surroundings)"),
    D(q="Give the sign of ΔH for an endothermic reaction.", a="positive (+)"),
    D(q="Give one example of an endothermic process.", a="thermal decomposition / dissolving ammonium nitrate / photosynthesis / electrolysis"),
    D(q="State why bond making is exothermic.", a="energy is released when new bonds form", ref="3.6C"),
    D(q="Give the meaning of each symbol in Q = mcΔT.", m=3, pts=["Q heat energy change (J)", "m mass of the liquid / water heated (g)", "c specific heat capacity; ΔT temperature change"], ref="3.3", d="4-6"),
    D(q="State why a lid is placed on the polystyrene cup in a calorimetry experiment.", a="to reduce heat loss (by evaporation / convection)", ref="3.2"),
    D(q="State what is meant by **activation energy**.", a="the minimum energy needed for a reaction to occur / particles to react", ref="3.13"),
    D(q="Name the type of energy change when ice melts.", a="endothermic"),
    D(q="Give the value of ΔT when the temperature of a solution falls from 21.5 °C to 14.0 °C.", a="7.5 °C (a fall)", ref="3.3"),
], intro="This question is about exothermic and endothermic changes.")

items(EN, "explain", "3.6C", [
    D(s="Explain, in terms of bonds, why the combustion of methane is exothermic.", m=2,
      p=["energy taken in to break bonds (C–H and O=O) is less", "than energy released when bonds form (C=O and O–H)"]),
    D(s="Explain why the thermal decomposition of calcium carbonate is endothermic.", m=2, p=["more energy is needed to break bonds than is released making new bonds", "so heat is taken in overall"]),
    D(s="Explain why the temperature of the water rises when sodium hydroxide dissolves in it.", m=2, p=["the dissolving is exothermic", "heat energy is transferred to the water / surroundings"], ref="3.1"),
    D(s="Explain why the experimental value of the enthalpy of combustion of ethanol is usually less exothermic than the data book value.", m=3,
      p=["heat is lost to the surroundings / air", "incomplete combustion", "heat used to warm the can / thermometer / evaporation of fuel"], ref="3.2", d="7-9"),
    D(s="Explain why, on an energy level diagram, the products of an endothermic reaction are drawn above the reactants.", m=2,
      p=["products have more (chemical) energy than reactants", "energy was taken in from the surroundings"], ref="3.5C", d="4-6"),
    D(s="Explain why adding twice the volume of acid at the same concentration does not double the temperature rise in a neutralisation experiment if the alkali is limiting.", m=2,
      p=["the amount of reaction (moles of water formed) is set by the alkali", "the same heat is spread through a larger mass of solution, so the rise is smaller"], ref="3.3", d="7-9"),
    D(s="Explain why stirring is needed in a calorimetry experiment.", m=2, p=["to spread the heat evenly / mix the reactants", "so the thermometer reading is accurate (highest temperature recorded)"], ref="3.2"),
    D(s="Explain why the enthalpy change of a reaction is the same whether a catalyst is used or not.", m=2, p=["catalyst lowers the activation energy only", "the energies of reactants and products are unchanged"], ref="3.14C", d="7-9"),
    D(s="Explain what is meant by an energy change of −57 kJ/mol for a neutralisation reaction.", m=2, p=["57 kJ of heat energy is given out", "for each mole of water formed / per mole of acid reacting"], ref="3.4", d="4-6"),
    D(s="Explain why the temperature rise is smaller when the experiment is done in a glass beaker rather than a polystyrene cup.", m=2,
      p=["glass is a better conductor of heat than polystyrene", "more heat is lost to the surroundings"], ref="3.2", d="4-6"),
])

FUELS = [("methanol", "CH3OH", 32, -726), ("ethanol", "C2H5OH", 46, -1367), ("propan-1-ol", "C3H7OH", 60, -2021), ("butan-1-ol", "C4H9OH", 74, -2676),
         ("hexane", "C6H14", 86, -4163), ("heptane", "C7H16", 100, -4817)]
NEUT = [("hydrochloric acid", "sodium hydroxide"), ("nitric acid", "potassium hydroxide"), ("hydrochloric acid", "potassium hydroxide")]
DISS = [("ammonium nitrate", "NH4NO3", 25.7), ("potassium nitrate", "KNO3", 34.9), ("ammonium chloride", "NH4Cl", 14.8), ("sodium hydroxide", "NaOH", -44.5),
        ("potassium chloride", "KCl", 17.2), ("calcium chloride", "CaCl2", -82.8)]
DISP = [("zinc", "copper(II) sulfate", -217), ("magnesium", "copper(II) sulfate", -470), ("iron", "copper(II) sulfate", -152)]


@tpl(EN, "calculation", 40)
def energetics_calc(r, k):
    kind = k % 5
    if kind == 0:  # combustion
        nm, f, mr, dh = FUELS[(k // 5) % len(FUELS)]
        mw = r.choice([100, 150, 200, 250])
        dm = r.choice([0.46, 0.50, 0.62, 0.75, 0.88, 1.10, 0.35, 0.58])
        frac = r.choice([0.40, 0.45, 0.50, 0.55, 0.60])
        q = -dh * 1000 * dm / mr * frac
        dT = round(q / (mw * 4.2), 1)
        Q_ = mw * 4.2 * dT
        n = Fr(str(dm)) / mr
        dhx = -Q_ / 1000 / float(n)
        parts = [P("a", "Calculate the heat energy transferred to the water, in J.", 2, space="working", answer_prefix="heat energy = ", lines=3),
                 P("b", f"Calculate the molar enthalpy change of combustion of {nm} in kJ/mol. Give your answer to 3 significant figures.", 3, space="working",
                   answer_prefix="ΔH = ", lines=6)]
        rows = [row("a", f"M1 {mw} × 4.2 × {num(dT)}", 1, None, "AO2"), row("a", f"M2 {num(round(Q_, 1))} J", 1, None, "AO2"),
                row("b", f"M1 moles = {num(dm)} ÷ {mr} = {num(float(n), sf=3)}", 1, None, "AO2"),
                row("b", f"M2 {num(round(Q_, 1))} ÷ 1000 ÷ {num(float(n), sf=3)}", 1, "ALLOW ecf from (a)", "AO2"),
                row("b", f"M3 −{num(abs(dhx), sf=3)} kJ/mol", 1, "negative sign needed for M3", "AO2")]
        intro = (f"A student burns {nm} in a spirit burner to heat {mw} g of water in a copper can. The mass of {nm} burned is {num(dm)} g and "
                 f"the temperature of the water rises by {num(dT)} °C.\n\n[Mr of {nm} = {mr}; c = 4.2 J/g/°C]")
        return Q("Calculate", "7-9", parts, rows, ["3.3", "3.4"], intro=intro, figs=[fig(S.spirit_burner(nm), 110, caption="Apparatus")] if k % 2 else None,
                 ans=("Q=mcΔT, ΔH=-Q/n", {"Q_J": round(Q_, 1), "dH": -float(num(abs(dhx), sf=3))}), ao=["AO2"])
    if kind == 1:  # neutralisation
        a, b = NEUT[(k // 5) % 3]
        v = r.choice([25.0, 50.0, 40.0, 30.0])
        c = r.choice([Fr(1), Fr(2), Fr(1, 2), Fr(3, 2)])
        n = c * Fr(str(v)) / 1000
        m = 2 * v
        dT = round(57.1 * 1000 * float(n) / (m * 4.2), 1)
        Q_ = m * 4.2 * dT
        dhx = -Q_ / 1000 / float(n)
        stem = (f"{num(v)} cm³ of {num(float(c))} mol/dm³ {a} is added to {num(v)} cm³ of {num(float(c))} mol/dm³ {b} in a polystyrene cup. "
                f"The temperature rises by {num(dT)} °C.\n\nCalculate the molar enthalpy change for the reaction. Assume the solution has a mass of "
                f"{num(m)} g and a specific heat capacity of 4.2 J/g/°C. Give your answer to 3 significant figures.")
        rows = [row("", f"M1 Q = {num(m)} × 4.2 × {num(dT)} = {num(round(Q_, 1))} J", 1, None, "AO2"),
                row("", f"M2 moles = {num(float(c))} × {num(v)} ÷ 1000 = {num(float(n), sf=3)}", 1, None, "AO2"),
                row("", f"M3 {num(round(Q_, 1))} ÷ 1000 ÷ {num(float(n), sf=3)} = {num(abs(dhx), sf=3)}", 1, "ALLOW ecf", "AO2"),
                row("", f"M4 ΔH = −{num(abs(dhx), sf=3)} kJ/mol", 1, "sign and units", "AO2")]
        return Q("Calculate", "7-9", [P("", stem, 4, space="working", answer_prefix="ΔH = ", lines=8)], rows, ["3.3", "3.4", "1.34C"],
                 ans=("Q=mcΔT", {"dH": -float(num(abs(dhx), sf=3))}), ao=["AO2"])
    if kind == 2:  # dissolving
        nm, f, dh = DISS[(k // 5) % len(DISS)]
        mw = r.choice([50, 100, 25])
        ms = r.choice([2.0, 4.0, 5.0, 2.5, 8.0])
        n = Fr(str(ms)) / Mr(f)
        dT = round(abs(dh) * 1000 * float(n) / (mw * 4.2), 1)
        if dT < 0.5:
            return None
        Q_ = mw * 4.2 * dT
        rise = dh < 0
        dhx = Q_ / 1000 / float(n) * (-1 if rise else 1)
        stem = (f"{num(ms)} g of {nm} is dissolved in {mw} g of water. The temperature {'rises' if rise else 'falls'} by {num(dT)} °C.\n\n"
                f"Calculate the molar enthalpy change of solution of {nm}. [Mr of {F(f)} = {num(Mr(f))}; c = 4.2 J/g/°C] Give your answer to 2 significant figures.")
        rows = [row("", f"M1 Q = {mw} × 4.2 × {num(dT)} = {num(round(Q_, 1))} J", 1, "ALLOW mass of water + solid", "AO2"),
                row("", f"M2 moles = {num(ms)} ÷ {num(Mr(f))} = {num(float(n), sf=3)}", 1, None, "AO2"),
                row("", f"M3 {'−' if rise else '+'}{num(abs(dhx), sf=2)} kJ/mol", 1, "sign must match: " + ("exothermic" if rise else "endothermic"), "AO2")]
        return Q("Calculate", "7-9" if not rise else "4-6", [P("", stem, 3, space="working", answer_prefix="ΔH = ", lines=6)], rows, ["3.3", "3.4", "3.8"],
                 ans=("Q=mcΔT", {"dH": float(num(dhx, sf=2))}), ao=["AO2"])
    if kind == 3:  # simple Q
        m = r.choice([50, 100, 200, 75, 150, 250])
        dT = r.choice([4.5, 6.0, 8.2, 12.5, 15.0, 22.4, 3.6, 9.8])
        Q_ = m * 4.2 * dT
        unit = r.choice(["J", "kJ"])
        val = Q_ if unit == "J" else Q_ / 1000
        stem = f"A kettle element warms {m} g of water so that it gets {num(dT)} °C hotter. Work out how much energy the water gains. Give your answer in {unit}. [c = 4.2 J/g/°C]"
        rows = [row("", f"M1 {m} × 4.2 × {num(dT)}", 1, None, "AO2"), row("", f"M2 {num(val, sf=3)} {unit}", 1, "ALLOW " + num(Q_) + " J if kJ asked for M1 only", "AO2")]
        return Q("Calculate", "1-3", [P("", stem, 2, space="working", answer_prefix="heat energy = ", lines=3)], rows, ["3.3"],
                 ans=("mcΔT", {"Q": float(num(val, sf=3)), "unit": unit}), ao=["AO2"])
    # kind 4: bond energies (C)
    BE = {"C-H": 413, "O=O": 498, "C=O": 805, "O-H": 464, "H-H": 436, "Cl-Cl": 243, "H-Cl": 432, "N≡N": 945, "N-H": 391, "C-C": 347, "C=C": 612,
          "Br-Br": 193, "C-Br": 276, "C-Cl": 346, "I-I": 151, "H-I": 299, "H-Br": 366, "C-O": 358}
    rx = [("CH4 + 2O2 -> CO2 + 2H2O", {"C-H": 4, "O=O": 2}, {"C=O": 2, "O-H": 4}),
          ("H2 + Cl2 -> 2HCl", {"H-H": 1, "Cl-Cl": 1}, {"H-Cl": 2}),
          ("N2 + 3H2 -> 2NH3", {"N≡N": 1, "H-H": 3}, {"N-H": 6}),
          ("2H2 + O2 -> 2H2O", {"H-H": 2, "O=O": 1}, {"O-H": 4}),
          ("C2H4 + Br2 -> C2H4Br2", {"C=C": 1, "Br-Br": 1}, {"C-C": 1, "C-Br": 2}),
          ("C2H4 + H2 -> C2H6", {"C=C": 1, "H-H": 1}, {"C-C": 1, "C-H": 2}),
          ("H2 + I2 -> 2HI", {"H-H": 1, "I-I": 1}, {"H-I": 2}),
          ("H2 + Br2 -> 2HBr", {"H-H": 1, "Br-Br": 1}, {"H-Br": 2}),
          ("CH4 + Cl2 -> CH3Cl + HCl", {"C-H": 1, "Cl-Cl": 1}, {"C-Cl": 1, "H-Cl": 1}),
          ("C2H6 + 7/2O2 -> 2CO2 + 3H2O", {"C-C": 1, "C-H": 6, "O=O": Fr(7, 2)}, {"C=O": 4, "O-H": 6}),
          ("C2H4 + 3O2 -> 2CO2 + 2H2O", {"C=C": 1, "C-H": 4, "O=O": 3}, {"C=O": 4, "O-H": 4}),
          ("C2H4 + H2O -> C2H5OH", {"C=C": 1, "O-H": 2, "C-H": 4}, {"C-C": 1, "C-H": 5, "C-O": 1, "O-H": 1})]
    eq, brk, mk = rx[(k // 5) % len(rx)]
    bi = sum(BE[b] * n for b, n in brk.items())
    mo = sum(BE[b] * n for b, n in mk.items())
    dh = bi - mo
    used = sorted(set(brk) | set(mk))
    tb = table(["Bond"] + used, [["Bond energy in kJ/mol"] + [str(BE[b]) for b in used]])
    stem = f"Use the bond energies in the table to calculate the enthalpy change, ΔH, for the reaction\n\n{F(eq.replace('->', '→').replace('7/2O2', '3½O2'))}"
    rows = [row("", "M1 bonds broken: " + " + ".join(f"{num(n)}({b})" for b, n in brk.items()) + f" = {num(bi)} kJ", 1, None, "AO2"),
            row("", "M2 bonds made: " + " + ".join(f"{num(n)}({b})" for b, n in mk.items()) + f" = {num(mo)} kJ", 1, None, "AO2"),
            row("", f"M3 ΔH = {num(bi)} − {num(mo)}", 1, "ALLOW ecf", "AO2"),
            row("", f"M4 {'+' if dh > 0 else '−'}{num(abs(dh))} kJ/mol", 1, "sign needed", "AO2")]
    return Q("Calculate", "7-9", [P("", stem, 4, space="working", answer_prefix="ΔH = ", lines=8)], rows, ["3.7C"], figs=[tb],
             intro="All the substances are gases." if "C2H4Br2" not in eq else None, ans=("broken − made", {"dH": float(dh)}), ao=["AO2"])


items(EN, "practical", "3.8", [
    D(s="Describe how to measure the temperature change when {s} dissolves in water.", m=4,
      p=["measure a known volume / mass of water into a polystyrene cup", "record the starting temperature", "add a known mass of solid and stir", "record the lowest / highest temperature reached"],
      v=[{"s": "ammonium nitrate"}, {"s": "potassium chloride"}, {"s": "sodium hydroxide"}]),
    D(s="Describe how to carry out an experiment to find the enthalpy change of combustion of a liquid fuel.", m=5,
      p=["weigh the spirit burner with fuel", "measure a known mass/volume of water into a copper can and record its temperature", "light the burner and heat the water, stirring",
         "stop after a set temperature rise and record the final temperature", "reweigh the burner to find the mass of fuel burned"], ref="3.2"),
    D(s="Give two ways of reducing heat loss in a combustion experiment with a spirit burner.", m=2, p=["use a draught shield", "lid on the can", "keep the flame close to the can", "insulate the can"], any=True, ref="3.2"),
    D(s="Suggest why a copper can is used rather than a glass beaker in a fuel combustion experiment.", m=1, p=["copper is a good conductor so transfers heat to the water quickly"], ref="3.2", d="4-6"),
    D(s="Explain why the burner should be weighed with its cap on.", m=1, p=["to stop the fuel evaporating (which would give a mass loss not due to burning)"], ref="3.2", d="7-9"),
    D(s="Explain why the thermometer used in calorimetry should have a resolution of 0.1 °C rather than 1 °C.", m=2, p=["small temperature changes are measured", "so the percentage error is smaller"], d="7-9"),
    D(s="Describe how to measure the temperature change for the displacement reaction between zinc powder and copper(II) sulfate solution.", m=4,
      p=["25 cm³ of copper(II) sulfate solution in a polystyrene cup", "record the temperature", "add an excess of zinc powder and stir", "record the highest temperature"], ref="3.2", d="4-6"),
    D(s="Suggest why the mass of a solid used in a dissolving experiment should be the same each time when comparing different salts.", m=2,
      p=["the temperature change depends on the amount of solid", "so differences are due only to the type of salt (fair test)"], ref="3.8", d="4-6"),
    D(s="Suggest how a student could improve a neutralisation experiment that gave a smaller temperature rise than expected.", m=2,
      p=["use a lid / insulate the cup / put the cup in a beaker", "stir and take readings every few seconds to find the true maximum"], any=True, d="7-9"),
    D(s="Give two safety precautions when burning liquid fuels in spirit burners.", m=2, p=["keep other fuels away from flames / stoppered", "eye protection", "use a heatproof mat", "do not refill a lit burner"], any=True, d="1-3"),
    D(s="Explain why the temperature is recorded for a few minutes before mixing in a neutralisation experiment.", m=1, p=["to make sure the starting temperature is steady / accurate"], d="7-9"),
    D(s="State the independent variable and dependent variable when comparing the heat released by different fuels.", m=2, p=["independent: type of fuel", "dependent: temperature rise of the water (per gram of fuel)"], d="4-6"),
])


def _fit(ps):
    n = len(ps)
    mx = sum(x for x, _ in ps) / n
    my = sum(y for _, y in ps) / n
    sxx = sum((x - mx) ** 2 for x, _ in ps)
    m = sum((x - mx) * (y - my) for x, y in ps) / sxx
    return m, my - m * mx


def _cross(a, b):
    """x where the least-squares lines through point sets a and b intersect."""
    m1, c1 = _fit(a)
    m2, c2 = _fit(b)
    return (c2 - c1) / (m1 - m2)


@tpl(EN, "data", 16)
def energetics_temp_graph(r, k):
    kind = k % 2
    if kind == 0:
        # neutralisation: volume of acid vs max temperature
        T0 = r.choice([19.0, 20.0, 21.0, 22.0])
        veq = r.choice([15, 20, 25, 30])
        peak = r.choice([5.5, 6.5, 7.0, 8.0])
        vs = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
        pts_ = []
        for v in vs:
            if v <= veq:
                t = T0 + peak * v / veq * (25 + veq) / (25 + v)
            else:
                t = T0 + peak * (25 + veq) / (25 + v)
            pts_.append((v, round(t, 1)))
        tb = table(["Volume of acid added in cm³"] + [str(v) for v, _ in pts_], [["Temperature in °C"] + [f"{t:.1f}" for _, t in pts_]])
        top = max(t for _, t in pts_)
        vint = round(_cross([p for p in pts_ if p[0] < veq], [p for p in pts_ if p[0] > veq]), 1)
        lo, hi = math.floor(min(vint, veq) - 1), math.ceil(max(vint, veq) + 1.5)
        parts = [P("a", "Plot the results and draw two straight lines of best fit.", 3, space="graph"),
                 P("b", "Use your graph to find the volume of acid needed to neutralise the alkali.", 1, answer_prefix="volume = ", lines=1),
                 P("c", "Explain why the temperature falls after this volume has been added.", 2, lines=3)]
        rows = [row("a", "M1 axes and scale\nM2 points plotted\nM3 two straight lines that cross", 3, None, "AO3"),
                row("b", f"{num(vint)} cm³ (where the two lines cross)", 1, f"ALLOW {lo} to {hi}; ALLOW ecf from candidate's lines", "AO3"),
                row("c", "M1 all the alkali has reacted / no more heat released", 1, None, "AO3"),
                row("c", "M2 excess (cooler) acid added dilutes / cools the mixture", 1, None, "AO3")]
        return Q("Use", "7-9", parts, rows, ["3.2", "3.1"], figs=[tb],
                 intro="A student adds hydrochloric acid, 5 cm³ at a time, to 25 cm³ of sodium hydroxide solution in a polystyrene cup and records the temperature after each addition.",
                 ans=("least-squares line intersection", {"v_intersection": vint, "v_model": veq, "accept": [lo, hi], "T_max": top}), ao=["AO3"])
    # temperature-time graph with extrapolation
    T0 = r.choice([18.0, 19.5, 20.5, 21.0])
    tmix = 3
    rise = r.choice([6.0, 8.0, 10.0, 12.0, -5.0, -7.0])
    cool = 0.4 if rise > 0 else -0.3
    pts_ = [(t, T0) for t in range(0, tmix)]
    pts_ += [(t, round(T0 + rise - cool * (t - tmix), 1)) for t in range(tmix + 1, 11)]
    g = graph("time in minutes", "temperature in °C", [pts_], xmax=10, xstep=1, ymin=int(min(p[1] for p in pts_)) - 2,
              ymax=int(max(p[1] for p in pts_)) + 3, ystep=2, smooth=False)
    dT = abs(rise)
    parts = [P("a", "State whether the reaction is exothermic or endothermic. Give a reason.", 2, lines=2),
             P("b", f"The reactants were mixed at {tmix} minutes. Use the graph to find the temperature change at {tmix} minutes by extrapolating the line back.", 2, lines=3),
             P("c", "Suggest why extrapolation gives a more accurate value than using the highest (or lowest) temperature recorded.", 1, lines=2)]
    rows = [row("a", f"M1 {'exothermic' if rise > 0 else 'endothermic'}", 1, None, "AO3"),
            row("a", f"M2 temperature {'rises' if rise > 0 else 'falls'}", 1, None, "AO3"),
            row("b", f"M1 extrapolated temperature {num(T0 + rise)} °C", 1, None, "AO3"),
            row("b", f"M2 ΔT = {num(dT)} °C", 1, "ALLOW ±0.5", "AO3"),
            row("c", "corrects for heat lost/gained while the reaction was happening", 1, None, "AO3")]
    return Q("Use", "7-9", parts, rows, ["3.2", "3.1"], figs=[fig(g, 120, caption="Temperature against time")],
             intro="A student records the temperature of a solution every minute before and after adding a reactant.", ans=("extrapolate", {"dT": dT}), ao=["AO3"])


# =================================================================== 3(b) rates
facts(RA, "3.10", [
    D(mq="Which change increases the rate of reaction between marble chips and hydrochloric acid?", c="using smaller marble chips", w=["using larger marble chips",
      "using more dilute acid", "cooling the acid"]),
    D(mq="Why does increasing the temperature increase the rate of a reaction?", c="particles have more energy so more collisions have at least the activation energy",
      w=["the activation energy decreases", "the particles get bigger", "the concentration increases"], ref="3.11", d="4-6"),
    D(mq="What is a catalyst?", c="a substance that speeds up a reaction without being used up", w=["a substance that slows down a reaction", "a reactant that is used up",
      "a product of the reaction"], ref="3.12"),
    D(mq="How does a catalyst work?", c="it provides an alternative pathway with lower activation energy", w=["it increases the energy of the particles", "it increases the concentration",
      "it changes the products"], ref="3.13", d="4-6"),
    D(mq="Which catalyst speeds up the decomposition of hydrogen peroxide?", c="manganese(IV) oxide", w=["copper(II) sulfate", "sodium chloride", "calcium carbonate"], ref="3.16"),
    D(mq="Why does increasing the pressure increase the rate of a gas reaction?", c="particles are closer together so collide more often", w=["particles move faster",
      "activation energy falls", "particles get more energy"], ref="3.11", d="4-6"),
    D(mq="Which statement about concentration is correct?", c="a higher concentration gives more frequent collisions", w=["a higher concentration lowers the activation energy",
      "a higher concentration makes particles move faster", "concentration has no effect on rate"], ref="3.11"),
    D(mq="Which method could be used to follow the rate of reaction between calcium carbonate and acid?", c="measuring the loss of mass every 30 seconds", w=["measuring the pH once at the end",
      "measuring the colour of the calcium carbonate", "weighing the acid before the reaction"], ref="3.9"),
    D(mq="In a graph of gas volume against time, what does a steeper gradient show?", c="a faster rate", w=["a slower rate", "more product overall", "the reaction has stopped"], d="4-6"),
    D(mq="What does a reaction profile show?", c="how the energy changes as reactants become products", w=["how the rate changes with time", "how the temperature changes with pressure",
      "the mass of products formed"], ref="3.14C"),
    D(mq="Why is powdered magnesium faster than magnesium ribbon at reacting with acid?", c="powder has a larger surface area", w=["powder is more concentrated", "powder has more energy",
      "powder has a lower activation energy"]),
    D(mq="On a reaction profile, the activation energy is", c="the energy from the reactants up to the peak", w=["the energy from products up to the peak",
      "the difference between reactants and products", "the energy of the products"], ref="3.14C", d="7-9"),
], intro="This question is about rates of reaction.")

facts(RA, "3.10", [
    D(q="Give four factors that affect the rate of a reaction.", m=2, pts=["temperature", "concentration (of solution)", "surface area (of solid)", "catalyst", "pressure (of gas)"],
      n="two correct for 1 mark; four for 2 marks", any=True),
    D(q="State what is meant by a **catalyst**.", a="a substance that speeds up a reaction but is chemically unchanged at the end", ref="3.12"),
    D(q="State the effect of a catalyst on the activation energy of a reaction.", a="it lowers it (by providing another route)", ref="3.13"),
    D(q="State what is meant by **activation energy**.", a="the minimum energy that colliding particles need to react", ref="3.13"),
    D(q="Name two measurements that could be used to follow the rate of reaction of marble chips with hydrochloric acid.", m=2,
      pts=["volume of carbon dioxide (gas syringe)", "loss in mass", "time for reaction to finish"], any=True, ref="3.15"),
    D(q="State how the rate of a reaction changes as the reaction proceeds.", a="it decreases (as reactants are used up)", d="4-6"),
    D(q="Give the units of rate when gas volume is measured in cm³ and time in seconds.", a="cm³/s"),
    D(q="Give two things that must happen for particles to react.", m=2, pts=["they must collide", "with energy equal to or greater than the activation energy"], ref="3.11", d="4-6"),
    D(q="Name the gas produced when hydrogen peroxide decomposes.", a="oxygen", ref="3.16"),
    D(q="Give a reason why catalysts are used in industry.", a="speed up reactions / lower temperatures needed / save energy / costs", ref="3.12"),
], intro="This question is about the rates of chemical reactions.")

items(RA, "explain", "3.11", [
    D(s="Explain, in terms of particles, why increasing the concentration of acid increases the rate of reaction with magnesium.", m=2,
      p=["more acid particles in the same volume", "more frequent collisions (per second)"], n="REJECT more collisions without reference to time/frequency for M2"),
    D(s="Explain, in terms of particles, why increasing the temperature increases the rate of reaction.", m=3,
      p=["particles move faster / have more kinetic energy", "collide more often", "more collisions have energy ≥ activation energy / more successful collisions"]),
    D(s="Explain why powdered calcium carbonate reacts faster than lumps with hydrochloric acid.", m=2, p=["powder has a larger surface area", "more frequent collisions between acid particles and carbonate"]),
    D(s="Explain how a catalyst increases the rate of a reaction.", m=2, p=["provides an alternative route / pathway", "with a lower activation energy so more collisions are successful"], ref="3.13"),
    D(s="Explain why the rate of reaction decreases as the reaction goes on.", m=2, p=["reactant particles are used up / concentration falls", "fewer collisions per second"], d="4-6"),
    D(s="Explain why increasing the pressure increases the rate of a reaction between two gases.", m=2, p=["more particles in the same volume / closer together", "collide more often"], ref="3.10", d="4-6"),
    D(s="Explain why the same final volume of gas is obtained when the temperature is raised, if the same amounts of reactants are used.", m=2,
      p=["the amount of limiting reactant is the same", "so the same amount of product forms; only the rate changes"], d="7-9"),
    D(s="Explain why a catalyst can be recovered at the end of a reaction.", m=1, p=["it is not used up / is chemically unchanged"], ref="3.12"),
    D(s="Explain why a 10 °C rise in temperature can roughly double the rate of a reaction even though the particles only move a little faster.", m=2,
      p=["the proportion of particles with energy above the activation energy increases greatly", "so the number of successful collisions increases a lot"], d="7-9"),
    D(s="Explain why food stays fresh for longer in a refrigerator.", m=2, p=["lower temperature slows the reactions that cause decay", "particles have less energy so fewer successful collisions"], d="4-6"),
    D(s="Explain why only a small mass of catalyst is needed.", m=2, p=["the catalyst is not used up", "it can be used again and again"], ref="3.12", d="4-6"),
])

RXN = [("marble chips (calcium carbonate)", "hydrochloric acid", "carbon dioxide"), ("magnesium ribbon", "hydrochloric acid", "hydrogen"),
       ("zinc granules", "sulfuric acid", "hydrogen"), ("hydrogen peroxide solution", "manganese(IV) oxide", "oxygen")]


def _curve(vmax, kc, ts):
    import math
    return [(t, round(vmax * (1 - math.exp(-kc * t)), 1)) for t in ts]


@tpl(RA, "calculation", 20)
def rates_calc(r, k):
    kind = k % 3
    if kind == 0:
        v = r.choice([24, 36, 45, 48, 60, 72, 80, 96])
        t = r.choice([20, 30, 40, 60, 90, 120])
        rate = Fr(v, t)
        rx = RXN[(k // 3) % 4]
        stem = f"In a reaction between {rx[0]} and {rx[1]}, {v} cm³ of {rx[2]} is collected in the first {t} s.\n\nCalculate the mean rate of reaction in cm³/s."
        rows = [row("", f"M1 {v} ÷ {t}", 1, None, "AO2"), row("", f"M2 {num(float(rate), sf=3)} cm³/s", 1, "ALLOW 2 or 3 sf", "AO2")]
        return Q("Calculate", "1-3", [P("", stem, 2, space="working", answer_prefix="rate = ", lines=3)], rows, ["3.9"],
                 ans=("V/t", {"rate": float(num(float(rate), sf=3))}), ao=["AO2"])
    if kind == 1:
        m0 = round(r.uniform(150, 190), 2)
        loss = round(r.choice([0.88, 1.32, 1.76, 2.20, 0.66, 1.10]), 2)
        t = r.choice([60, 120, 180, 240, 300])
        rate = loss / t
        stem = (f"A flask containing marble chips and hydrochloric acid has a mass of {m0:.2f} g at the start. After {t} s the mass is "
                f"{m0 - loss:.2f} g.\n\nCalculate the mean rate of reaction in g/s. Give your answer in standard form to 2 significant figures.")
        e = num(rate, sf=2)
        rows = [row("", f"M1 loss = {loss:.2f} g", 1, None, "AO2"), row("", f"M2 {loss:.2f} ÷ {t}", 1, None, "AO2"),
                row("", f"M3 {'{:.1e}'.format(rate).replace('e-0', ' × 10^-').replace('e-', ' × 10^-')} g/s", 1, "ALLOW decimal " + e, "AO2")]
        rows[2]["answer"] = rows[2]["answer"].replace("10^-", "10⁻").replace("⁻3", "⁻³").replace("⁻2", "⁻²").replace("⁻4", "⁻⁴")
        return Q("Calculate", "4-6", [P("", stem, 3, space="working", answer_prefix="rate = ", lines=5)], rows, ["3.9", "3.15"],
                 ans=("loss/t", {"rate": float(e)}), ao=["AO2"])
    # kind 2: gradient (tangent) from graph data – initial rate from first interval and moles of gas
    v = r.choice([48, 60, 72, 96, 120])
    stem = (f"A reaction produces {v} cm³ of hydrogen in total at room temperature and pressure.\n\n"
            "Calculate the amount, in moles, of hydrogen produced. [1 mol of gas occupies 24 000 cm³ at rtp]")
    n = Fr(v, 24000)
    rows = [row("", f"M1 {v} ÷ 24 000", 1, None, "AO2"), row("", f"M2 {num(float(n), sf=3)} mol", 1, "ALLOW standard form", "AO2")]
    return Q("Calculate", "4-6", [P("", stem, 2, space="working", answer_prefix="amount = ", lines=3)], rows, ["1.35C", "3.9"],
             ans=("V/24000", {"mol": float(num(float(n), sf=3))}), ao=["AO2"])


@tpl(RA, "data", 18)
def rates_graph_data(r, k):
    rx = RXN[k % 4]
    vmax = r.choice([60, 72, 80, 90, 96])
    kc = r.choice([0.02, 0.025, 0.03, 0.035, 0.04])
    # make the 60 s reading fall exactly on a small-square line (grid 10 cm³, small square 2 cm³)
    v60t = 2 * round(vmax * (1 - math.exp(-kc * 60)) / 2)
    if v60t >= vmax:
        v60t -= 2
    kc = -math.log(1 - v60t / vmax) / 60
    ts = list(range(0, 241, 30))
    pts_ = _curve(vmax, kc, ts)
    fac = ["at a higher temperature", "with more concentrated acid", "with powdered solid", "with a catalyst"][(k // 4) % 4]
    if rx[0].startswith("hydrogen") and fac == "with powdered solid":
        fac = "with powdered catalyst"
    g = graph("time in s", f"volume of {rx[2]} in cm³", [pts_], xmax=240, xstep=30, ymax=100, ystep=10)
    v60 = v60t
    assert abs(dict(pts_)[60] - v60) < 0.05
    tend = next((t for t, v in pts_ if v >= vmax - 1), 240)
    parts = [P("a", f"Use the graph to find the volume of {rx[2]} collected after 60 s.", 1, answer_prefix="volume = ", lines=1),
             P("b", "Calculate the mean rate of reaction over the first 60 s.", 2, space="working", answer_prefix="rate = ", lines=3),
             P("c", "Explain why the graph levels off.", 2, lines=3),
             P("d", f"On the same axes, sketch the curve you would expect if the experiment were repeated {fac}, using the same amounts of reactants.", 2, space="none")]
    rows = [row("a", f"{num(v60)} cm³", 1, f"ALLOW {num(v60 - 1)} to {num(v60 + 1)} (±½ small square)", "AO3"),
            row("b", f"M1 {num(v60)} ÷ 60", 1, "ALLOW ecf from (a)", "AO2"), row("b", f"M2 {num(v60 / 60, sf=2)} cm³/s", 1, None, "AO2"),
            row("c", "M1 the reaction has stopped", 1, None, "AO3"), row("c", "M2 because one reactant (the limiting reactant) is used up", 1, None, "AO3"),
            row("d", "M1 steeper curve at the start\nM2 levels off at the same final volume", 2, None, "AO3")]
    return Q("Use", "4-6" if k % 2 else "7-9", parts, rows, ["3.9", "3.10"], figs=[fig(g, 120, caption=f"Volume of {rx[2]} against time")],
             intro=f"A student reacts {rx[0]} with {rx[1]} and measures the volume of {rx[2]} given off.",
             ans=("read graph", {"v60": v60, "rate": float(num(v60 / 60, sf=2))}), ao=["AO3", "AO2"])


items(RA, "practical", "3.15", [
    D(s="Describe how to investigate the effect of acid concentration on the rate of reaction between marble chips and hydrochloric acid.", m=5,
      p=["fixed mass of marble chips (same size) in a conical flask", "add a fixed volume of acid of one concentration and start the timer",
         "measure the volume of gas in a gas syringe (or mass loss) at regular intervals", "repeat with different concentrations of acid",
         "keep temperature and chip size constant; compare initial rates / plot graphs"], figs=[fig(S.gas_syringe(), 110, caption="One possible apparatus")]),
    D(s="Explain why a cotton wool plug is placed in the neck of the flask in a mass-loss experiment.", m=2, p=["lets the gas escape", "but stops acid spray escaping (so mass loss is only due to gas)"],
      figs=[fig(S.mass_loss(), 100, caption="Apparatus")]),
    D(s="Give two variables that must be controlled when investigating the effect of temperature on the rate of reaction between magnesium and acid.", m=2,
      p=["mass / length of magnesium", "volume of acid", "concentration of acid", "surface area of magnesium"], any=True),
    D(s="Describe how to find out whether copper(II) oxide is a catalyst for the decomposition of hydrogen peroxide.", m=4,
      p=["measure the rate of oxygen production with and without copper(II) oxide", "same volume and concentration of hydrogen peroxide", "faster rate with copper(II) oxide",
         "filter, dry and weigh the copper(II) oxide afterwards: same mass shows it is unchanged"], ref="3.16", d="7-9"),
    D(s="Suggest why a gas syringe is more accurate than collecting gas over water for carbon dioxide.", m=1, p=["carbon dioxide is slightly soluble in water"], d="7-9"),
    D(s="Describe how the 'disappearing cross' method could be used to follow the rate of a reaction that forms a precipitate.", m=3,
      p=["place the flask on a paper marked with a cross", "mix the reactants and start the timer", "stop timing when the cross can no longer be seen"], d="4-6"),
    D(s="Explain why the student should measure the volume of gas at regular time intervals rather than just at the end.", m=2,
      p=["to see how the rate changes / plot a graph", "the final volume alone does not show the rate"], d="4-6"),
    D(s="Suggest how to compare the effectiveness of three solid catalysts for decomposing hydrogen peroxide.", m=3,
      p=["same mass of each catalyst (same particle size)", "same volume and concentration of hydrogen peroxide", "measure the volume of oxygen in a set time / time for a set volume"], ref="3.16", d="7-9"),
    D(s="A student finds that the plunger of the gas syringe sticks during the experiment. Suggest how this would affect the results.", m=2,
      p=["the volume readings would be too low / jumpy", "so the rate calculated would be inaccurate"], d="7-9"),
    D(s="Give one reason why the marble chips should be the same size in an experiment testing the effect of acid concentration.", m=1, p=["surface area also affects the rate (keep it constant)"], d="1-3"),
    D(s="Suggest a safety precaution when using a water bath at 60 °C to investigate the effect of temperature on rate.", m=1, p=["handle with care / tongs to avoid scalds", "eye protection"], any=True, d="1-3"),
    D(s="Describe how you could use a balance to follow the rate of reaction between magnesium carbonate and hydrochloric acid.", m=3,
      p=["place the flask with acid and carbonate on a balance", "record the mass at regular intervals", "the loss in mass is due to carbon dioxide escaping"], d="4-6"),
])

FACT_EXT = [
    ("temperature", "magnesium ribbon and hydrochloric acid", "water baths at different temperatures"),
    ("concentration", "marble chips and hydrochloric acid", "different concentrations of acid"),
    ("surface area", "calcium carbonate and nitric acid", "chips of different sizes and powder"),
    ("a catalyst", "hydrogen peroxide decomposition", "different metal oxides"),
    ("concentration", "sodium thiosulfate and hydrochloric acid", "disappearing cross"),
    ("temperature", "sodium thiosulfate and hydrochloric acid", "disappearing cross at different temperatures"),
]


def _rate_ind(f, rx, how):
    expl = {"temperature": ["higher temperature: particles have more kinetic energy", "more frequent collisions and more collisions with energy ≥ activation energy"],
            "concentration": ["higher concentration: more acid particles in the same volume", "more frequent collisions"],
            "surface area": ["smaller pieces: larger surface area", "more frequent collisions at the surface"],
            "a catalyst": ["catalyst gives an alternative pathway with lower activation energy", "more collisions are successful; catalyst mass unchanged at end"]}[f]
    meas = "time for the cross to disappear" if "cross" in how else ("volume of gas in a gas syringe at regular intervals" if "peroxide" not in rx else "volume of oxygen in a gas syringe")
    return [f"method: react {rx} using {how}", f"measure the {meas}", "control variables: amounts / volumes / other conditions kept the same",
            "repeat and calculate mean values / plot graph", f"result: rate increases with {f}" if f != "a catalyst" else "result: the best catalyst gives the fastest rate"] + expl


extended(RA, "3.10", [
    D(s=f"Describe an experiment to investigate how {f} affects the rate of the reaction between {rx}. Explain the results in terms of particles.",
      ind=_rate_ind(f, rx, how), ref=["3.9", "3.11"] + (["3.16"] if f == "a catalyst" else ["3.15"] if "marble" in rx else []), ao="AO1 2, AO2 2, AO3 2",
      d="4-6" if i % 2 else "7-9") for i, (f, rx, how) in enumerate(FACT_EXT)
] + [
    D(s="Explain, using a reaction profile, how a catalyst increases the rate of an exothermic reaction. Include what is meant by activation energy.",
      ind=["activation energy is the minimum energy needed for a collision to lead to reaction", "profile: reactants above products (exothermic)", "peak above reactants: activation energy",
           "catalyst gives a lower peak (alternative pathway)", "ΔH unchanged", "more particles have energy ≥ lower activation energy", "so more collisions are successful per second"], ref=["3.13", "3.14C"], d="7-9"),
    D(s="A farmer wants to dissolve limestone chips in acid quickly. Explain three changes that would increase the rate and why each works.",
      ind=["crush into powder: larger surface area", "more collisions per second at the surface", "use more concentrated acid: more acid particles per volume", "more frequent collisions",
           "warm the acid: particles faster, more energy", "more collisions exceed activation energy"], ref=["3.10", "3.11"], d="4-6"),
    D(s="Explain why many industrial processes use catalysts, and why the catalyst is often in the form of a fine powder or mesh.",
      ind=["catalyst increases rate without being used up", "lower activation energy so less energy / lower temperature needed", "saves fuel costs and reduces emissions",
           "catalyst can be reused", "fine powder / mesh has large surface area", "more collisions at the catalyst surface"], ref=["3.12", "3.13"], d="4-6"),
    D(intro="Two students react 1.0 g of magnesium with excess 1 mol/dm³ hydrochloric acid. Student A uses ribbon and student B uses powder.",
      s="Describe how their results would differ, and explain this. Include how they could measure the rate and why the final volume of gas is the same.",
      ind=["measure volume of hydrogen with gas syringe at intervals", "B's reaction is faster: steeper initial gradient", "powder has larger surface area", "more frequent collisions with acid particles",
           "both finish with same volume", "magnesium is the limiting reactant and the same mass is used", "B's curve levels off sooner"], ref=["3.9", "3.11"], d="7-9"),
    D(s="Describe how the rate of reaction changes during the reaction between marble chips and excess hydrochloric acid, and explain these changes using collision theory.",
      ind=["fast at the start: steep gradient", "rate decreases over time: gradient less steep", "acid concentration falls / chips get smaller", "fewer collisions per second",
           "reaction stops when chips are used up", "graph levels off", "if acid is limiting, stops when acid used up"], ref=["3.10", "3.11"], d="4-6"),
    D(s="Explain why reactions between gases are faster at higher pressure and higher temperature, and why industrial plants do not always use the highest possible values.",
      ind=["higher pressure: particles closer, more frequent collisions", "higher temperature: more energy, more collisions above activation energy", "both increase rate",
           "high pressure is expensive and dangerous (strong equipment)", "high temperature uses more energy / fuel", "compromise conditions chosen; catalysts used instead"], ref=["3.10", "3.11"], d="7-9"),
], tag="rates")

# =================================================================== 3(c) equilibria
facts(EQM, "3.17", [
    D(mq="What does the symbol ⇌ show?", c="the reaction is reversible", w=["the reaction is fast", "the reaction is exothermic", "the reaction has stopped"]),
    D(mq="What colour change happens when water is added to anhydrous copper(II) sulfate?", c="white to blue", w=["blue to white", "white to pink", "green to blue"], ref="3.18"),
    D(mq="What happens when ammonium chloride is heated?", c="it decomposes into ammonia and hydrogen chloride", w=["it melts", "it forms ammonium oxide", "nothing happens"], ref="3.18"),
    D(mq="What is meant by dynamic equilibrium?", c="the forward and backward reactions happen at the same rate", w=["both reactions have stopped", "only the forward reaction happens",
      "the concentrations of reactants and products are equal"], ref="3.20C", d="4-6"),
    D(mq="Where must a reaction take place to reach equilibrium?", c="a closed system", w=["an open beaker", "a fume cupboard", "a vacuum"], ref="3.19C"),
    D(mq="What is the effect of a catalyst on the position of equilibrium?", c="no effect", w=["moves it to the right", "moves it to the left", "stops the reaction"], ref="3.21C"),
    D(mq="For N₂ + 3H₂ ⇌ 2NH₃, what is the effect of increasing pressure on the yield of ammonia?", c="it increases", w=["it decreases", "no change", "it falls to zero"], ref="3.22C", d="7-9"),
    D(mq="The forward reaction is exothermic. What happens to the equilibrium yield of product when temperature is increased?", c="it decreases", w=["it increases", "no change",
      "it doubles"], ref="3.22C", d="7-9"),
    D(mq="Why does a catalyst help an equilibrium reaction?", c="equilibrium is reached more quickly", w=["more product forms at equilibrium", "the forward reaction becomes exothermic",
      "the reaction becomes irreversible"], ref="3.21C", d="4-6"),
    D(mq="Which statement about the reaction to dehydrate hydrated copper(II) sulfate is correct?", c="it is endothermic", w=["it is exothermic", "it gives out heat", "it needs a catalyst"], ref="3.18", d="4-6"),
    D(mq="Increasing pressure moves the position of equilibrium towards the side with", c="fewer molecules of gas", w=["more molecules of gas", "more solid", "higher temperature"], ref="3.22C", d="7-9"),
    D(mq="When the concentration of a reactant is increased, the position of equilibrium", c="moves to the right (towards products)", w=["moves to the left", "does not change", "moves towards reactants"], ref="3.22C", d="4-6"),
], intro="This question is about reversible reactions and equilibrium.")

facts(EQM, "3.17", [
    D(q="State what is meant by a **reversible reaction**.", a="a reaction in which the products can react to re-form the reactants"),
    D(q="Name the substance formed when anhydrous copper(II) sulfate reacts with water.", a="hydrated copper(II) sulfate", ref="3.18"),
    D(q="Describe what you see at the cool top of a test tube when ammonium chloride is heated at the bottom.", a="white solid forms again (reforms ammonium chloride)", ref="3.18"),
    D(q="Give two features of a reaction at dynamic equilibrium.", m=2, pts=["forward and backward rates equal", "concentrations of reactants and products stay constant", "closed system"], any=True, ref="3.20C"),
    D(q="State why equilibrium can only be reached in a closed system.", a="no substances can escape / enter", ref="3.19C"),
    D(q="State the effect of a catalyst on the time taken to reach equilibrium.", a="it is shorter", ref="3.21C"),
    D(q="For a reaction whose forward reaction is endothermic, state the effect of increasing temperature on the yield.", a="yield increases / equilibrium moves right", ref="3.22C", d="4-6"),
    D(q="Give the sign of ΔH for the reverse of an exothermic reaction.", a="positive", d="4-6"),
    D(q="State what you would observe when water is added to anhydrous cobalt(II) chloride.", a="blue to pink", ref="3.18", d="4-6"),
    D(q="Give the effect on the equilibrium position of decreasing pressure for 2SO₂ + O₂ ⇌ 2SO₃.", a="moves left (towards more gas molecules)", ref="3.22C", d="7-9"),
], intro="This question is about equilibria.")

EQR = [("N2(g) + 3H2(g) <=> 2NH3(g)", -92, "ammonia"), ("2SO2(g) + O2(g) <=> 2SO3(g)", -197, "sulfur trioxide"),
       ("C2H4(g) + H2O(g) <=> C2H5OH(g)", -45, "ethanol"), ("N2O4(g) <=> 2NO2(g)", 58, "nitrogen dioxide"),
       ("H2(g) + I2(g) <=> 2HI(g)", -10, "hydrogen iodide"), ("CO(g) + 2H2(g) <=> CH3OH(g)", -91, "methanol"),
       ("CH4(g) + H2O(g) <=> CO(g) + 3H2(g)", 206, "hydrogen"), ("CO(g) + H2O(g) <=> CO2(g) + H2(g)", -41, "hydrogen")]


def _gas_mol(eq):
    import chemistry_util as U
    L_, R_ = U.eq_terms(eq)
    return sum(c for c, _, s in L_ if s == "g"), sum(c for c, _, s in R_ if s == "g")


def _eq_effects(eq, dh):
    l, r_ = _gas_mol(eq)
    pres = "increases" if r_ < l else ("decreases" if r_ > l else "no change")
    temp = "decreases" if dh < 0 else "increases"
    return pres, temp, l, r_


items(EQM, "explain", "3.22C", [
    D(s=f"The equation for a reaction is {EQ(eq)}  ΔH = {'+' if dh > 0 else '−'}{abs(dh)} kJ/mol\n\nExplain the effect of {ch} on the equilibrium yield of {pr}.", m=2,
      p=p) for eq, dh, pr in EQR for ch, p in [
        ("increasing the temperature", [f"yield {_eq_effects(eq, dh)[1]}", f"forward reaction is {'exothermic' if dh < 0 else 'endothermic'} so equilibrium shifts in the {'endothermic (backward)' if dh < 0 else 'endothermic (forward)'} direction"]),
        ("increasing the pressure", [f"yield {_eq_effects(eq, dh)[0]}",
                                     (f"equilibrium shifts towards the side with fewer gas molecules ({min(_eq_effects(eq, dh)[2:]):g} mol)" if _eq_effects(eq, dh)[0] != "no change"
                                      else "same number of gas molecules on each side so position unchanged")])]
] + [
    D(s="Explain why a catalyst does not change the yield of a reversible reaction.", m=2, p=["it speeds up the forward and backward reactions equally", "so equilibrium is reached faster but position unchanged"], ref="3.21C"),
    D(s="Explain why heating hydrated copper(II) sulfate and adding water to the anhydrous solid shows that the reaction is reversible.", m=2,
      p=["heating turns blue crystals white (water removed)", "adding water turns white powder blue again (and gets hot)"], ref="3.18"),
    D(s="Explain what is meant by the term dynamic in dynamic equilibrium.", m=2, p=["reactions are still happening / particles still reacting", "forward and backward rates are equal so no overall change"], ref="3.20C"),
], tag="equilibria")


@tpl(EQM, "data", 16)
def equilibria_yield_data(r, k):
    eq, dh, pr = EQR[[0, 1, 5, 2][k % 4]]
    pres, temp, l, rr = _eq_effects(eq, dh)
    Ts = [300, 350, 400, 450, 500]
    Ps = [50, 100, 200]
    import math
    base = r.uniform(0.9, 1.4)
    tbl = []
    for p in Ps:
        rowv = []
        for T in Ts:
            y = 100 / (1 + math.exp((T - 380) / 45) / (base * (p / 100) ** 0.8))
            rowv.append(round(y))
        tbl.append(rowv)
    tb = table(["Pressure in atm"] + [f"{T} °C" for T in Ts], [[str(p)] + [str(v) for v in rv] for p, rv in zip(Ps, tbl)],
               caption=f"Percentage yield of {pr} at equilibrium")
    Tq, Pq = r.choice(Ts), r.choice(Ps)
    parts = [P("a", f"Give the percentage yield of {pr} at {Tq} °C and {Pq} atm.", 1, lines=1),
             P("b", "Describe how the yield changes with temperature and with pressure.", 2, lines=3),
             P("c", "Use the data to deduce whether the forward reaction is exothermic or endothermic. Explain your answer.", 2, lines=3),
             P("d", "Suggest why the industrial process may use a moderate temperature rather than the temperature that gives the highest yield.", 2, lines=3)]
    rows = [row("a", f"{tbl[Ps.index(Pq)][Ts.index(Tq)]} %", 1, None, "AO3"),
            row("b", "M1 yield decreases as temperature increases", 1, None, "AO3"), row("b", "M2 yield increases as pressure increases", 1, None, "AO3"),
            row("c", "M1 exothermic", 1, None, "AO3"), row("c", "M2 increasing temperature lowers yield, so equilibrium moves in the endothermic (backward) direction", 1, None, "AO2"),
            row("d", "M1 at low temperature the rate is too slow", 1, None, "AO2"), row("d", "M2 a compromise gives an acceptable yield quickly", 1, None, "AO2")]
    return Q("Use", "7-9", parts, rows, ["3.22C", "3.20C"], figs=[tb], intro=f"The equation for a reversible reaction is\n\n{EQ(eq)}",
             ans=("read table", {"yield": tbl[Ps.index(Pq)][Ts.index(Tq)]}), ao=["AO3", "AO2"])
