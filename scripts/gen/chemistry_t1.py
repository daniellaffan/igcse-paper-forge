"""Topic 1 templates: principles of chemistry (1(a) to 1(i))."""
from fractions import Fraction as Fr

from chemistry_util import (tpl, mcq, pts, anyof, P, F, row, Q, num, Mr, AR, EL, config, GROUP, PERIOD, EQ,
                            fig, table, graph, lv6, LV_GENERAL)
from chemistry_kb import facts, items, extended
import chemistry_svg as S
import chemistry_util as U
import math

ST = "chemistry.principles.states"
MX = "chemistry.principles.mixtures"
AT = "chemistry.principles.atoms"
PT = "chemistry.principles.periodic"
FO = "chemistry.principles.formulae"
IO = "chemistry.principles.ionic"
CO = "chemistry.principles.covalent"
ME = "chemistry.principles.metallic"
EL_ = "chemistry.principles.electrolysis"


def D(**k):
    return k


# =================================================================== 1(a) states of matter
facts(ST, "1.1", [
    D(mq="Which change of state is called sublimation?", c="solid to gas",
      w=["gas to liquid", "liquid to gas", "solid to liquid"], ref="1.2"),
    D(mq="Which statement describes the particles in a liquid?",
      c="close together, randomly arranged and able to move past each other",
      w=["far apart, randomly arranged and moving quickly", "close together in a regular pattern, vibrating about fixed positions",
          "far apart in a regular pattern and vibrating"], d="1-3"),
    D(mq="In which state do the particles of a substance have the most energy?", c="gas",
      w=["liquid", "solid", "the particles have the same energy in every state"]),
    D(mq="What is the name of the change from gas to liquid?", c="condensing", w=["evaporating", "freezing", "melting"], ref="1.2"),
    D(mq="Which term describes the substance that dissolves in a solvent?", c="solute",
      w=["solution", "saturated solution", "filtrate"], ref="1.4"),
    D(mq="What is a saturated solution?", c="a solution in which no more solute will dissolve at that temperature",
      w=["a solution that contains only water", "a solution that contains more than one solute",
          "a solution that has been heated until it boils"], ref="1.4", d="4-6"),
    D(mq="Which of these gases diffuses fastest at the same temperature?", c="hydrogen, H2",
      w=["ammonia, NH3", "chlorine, Cl2", "carbon dioxide, CO2"], ref="1.3", d="4-6"),
    D(mq="Solubility is usually measured in which units?", c="g per 100 g of solvent",
      w=["g per dm³ of solution", "mol per 100 g of solvent", "cm³ per 100 g of solvent"], ref="1.5C", d="4-6"),
    D(mq="What happens to the particles in a liquid as the liquid is heated?", c="they gain kinetic energy and move faster",
      w=["they become larger", "they become heavier", "they stop moving and vibrate"]),
    D(mq="Which change of state takes in energy from the surroundings?", c="melting",
      w=["condensing", "freezing", "a gas changing into a solid"], ref="1.2", d="4-6"),
    D(mq="A purple crystal is placed at the bottom of a beaker of water. After a day the whole beaker is pale purple. "
         "Which process has taken place?", c="diffusion", w=["condensation", "evaporation", "melting"], ref="1.3"),
    D(mq="Which statement about the particles in a solid is correct?", c="they vibrate about fixed positions",
      w=["they move freely in all directions", "they are far apart", "they have no energy at all"]),
    D(mq="What is the name of the change from liquid to solid?", c="freezing",
      w=["condensing", "subliming", "boiling"], ref="1.2"),
    D(mq="Which mixture is a solution?", c="sugar dissolved in water",
      w=["sand stirred into water", "chalk powder shaken with water", "oil shaken with water"], ref="1.4"),
], intro="This question is about states of matter and solutions.")

facts(ST, "1.1", [
    D(q="Name the change of state when a liquid turns into a solid.", a="freezing", n="ALLOW solidifying", ref="1.2"),
    D(q="State what is meant by the term **solvent**.", a="the liquid in which a solute dissolves",
      n="ALLOW substance that dissolves a solute", ref="1.4"),
    D(q="State what is meant by the term **solute**.", a="the substance that dissolves (in a solvent)", ref="1.4"),
    D(q="State what is meant by the term **saturated solution**.",
      a="a solution in which no more solute will dissolve (at that temperature)",
      n="IGNORE references to heating; REJECT 'contains lots of solute' alone", ref="1.4", d="4-6"),
    D(q="Name the process by which particles spread from a region of high concentration to a region of low "
        "concentration.", a="diffusion", ref="1.3"),
    D(q="Give two differences between the particles in a solid and the particles in a gas.", m=2,
      pts=["solid particles close together/touching but gas particles far apart",
           "solid particles in a regular arrangement but gas particles random",
           "solid particles vibrate about fixed positions but gas particles move quickly/freely",
           "gas particles have more energy"], n="Comparison needed for each mark"),
    D(q="State what is meant by the term **solubility**.",
      a="the mass of solute that dissolves in 100 g of solvent (at a stated temperature)",
      n="ALLOW maximum mass that dissolves in 100 g of water to form a saturated solution", ref="1.5C", d="4-6"),
    D(q="Name the change of state when a solid turns directly into a gas.", a="sublimation", n="ALLOW subliming", ref="1.2"),
    D(q="State how the movement of particles in a liquid changes when the liquid is cooled.",
      a="the particles move more slowly / have less kinetic energy"),
    D(q="Give the units in which solubility is usually measured.", a="g per 100 g of water/solvent",
      n="ALLOW g/100 g", ref="1.5C"),
    D(q="State one way of making a gas condense.", a="cool it (below its boiling point)", n="ALLOW increase pressure / compress it", ref="1.2"),
    D(q="A sample of nitrogen is kept in a sealed flask. Describe how its particles are arranged and how they move.", m=2,
      pts=["(arrangement) far apart / random", "(movement) move quickly in all directions / randomly"]),
    D(q="State what happens to the arrangement of the particles when a solid melts.",
      a="the regular arrangement breaks down / particles become randomly arranged (but stay close)", ref="1.2", d="4-6"),
], intro="This question is about states of matter and solutions.")

items(ST, "explain", "1.1", [
    D(s="Explain, in terms of particles, why a gas can be compressed easily but a liquid cannot.", m=2,
      p=["gas particles are far apart / large spaces between them", "liquid particles are close together / touching so cannot be pushed closer"]),
    D(intro="A few drops of liquid bromine are placed at the bottom of a gas jar of air and a lid is put on. After an hour "
            "the brown colour has spread evenly through the jar.",
      s="Explain this observation.", m=3,
      p=["bromine evaporates / turns into a gas", "(bromine and air) particles move randomly",
         "bromine particles spread / diffuse from high to low concentration (until evenly mixed)"], ref="1.3"),
    D(intro="Cotton wool soaked in concentrated ammonia solution is placed at one end of a long glass tube and cotton wool "
            "soaked in concentrated hydrochloric acid at the other end. A white ring of ammonium chloride forms nearer the "
            "hydrochloric acid end.",
      s="Explain why the white ring forms nearer the hydrochloric acid end of the tube.", m=3,
      p=["ammonia particles/molecules have a lower mass (Mr) than hydrogen chloride", "so ammonia particles move/diffuse faster",
         "so ammonia travels further in the same time"], ref="1.3", d="7-9",
      n="ALLOW reverse arguments for hydrogen chloride"),
    D(s="Explain why gases diffuse faster at higher temperatures.", m=2,
      p=["particles have more (kinetic) energy", "so move faster"], ref="1.3"),
    D(s="Explain what happens to the particles when a block of ice is heated until it melts.", m=3,
      p=["particles gain (kinetic) energy", "vibrate more / faster",
         "(some) forces of attraction are overcome so particles can move past each other"], ref="1.2"),
    D(s="Explain why a liquid takes the shape of its container but a solid does not.", m=2,
      p=["liquid particles can move / slide past each other", "solid particles are held in fixed positions / can only vibrate"]),
    D(intro="A student dissolves one crystal of potassium manganate(VII) in 10 cm³ of water. She then dilutes the solution "
            "ten times over, five times in a row. The purple colour fades each time but can still be seen at the end.",
      s="Explain what this experiment suggests about the particles in the crystal.", m=2,
      p=["there are a very large number of particles (in the crystal)", "the particles are very small"], ref="1.3"),
    D(s="Water is heated in a kettle. Explain why the temperature of the boiling water stays at 100 °C even though it is "
        "still being heated.", m=2,
      p=["the energy is used to overcome forces of attraction between the particles",
         "rather than to increase the kinetic energy / speed of the particles"], ref="1.2", d="7-9"),
    D(s="A hot, saturated solution of potassium nitrate is left to cool. Explain why crystals form as it cools.", m=2,
      p=["solubility (of potassium nitrate) decreases as the temperature falls",
         "the solute that can no longer dissolve comes out as crystals"], ref="1.6C", d="4-6"),
    D(s="Explain why two gases mix much faster than two liquids.", m=2,
      p=["gas particles move faster", "there is more space between gas particles (so fewer collisions slow them down)"], ref="1.3"),
    D(s="Steam condenses on a cold window. Explain what happens to the water particles.", m=3,
      p=["particles lose (kinetic) energy (to the cold glass)", "particles move more slowly",
         "particles come closer together / attractive forces hold them as a liquid"], ref="1.2"),
    D(s="A smell from a perfume bottle opened at the front of a room takes a few minutes to reach the back. Explain why it "
        "is not instant even though the particles move at hundreds of metres per second.", m=2,
      p=["perfume particles collide with air particles", "so they move in random / zig-zag paths (and take longer)"], ref="1.3", d="7-9"),
])

SALTS_SOL = {  # approx solubility in g per 100 g water at 0, 20, 40, 60, 80 °C
    "potassium nitrate": [13, 32, 64, 110, 169],
    "ammonium chloride": [29, 37, 46, 55, 66],
    "potassium chloride": [28, 34, 40, 46, 51],
    "sodium nitrate": [73, 88, 104, 124, 148],
    "copper(II) sulfate": [14, 20, 29, 40, 55],
    "potassium chlorate": [3, 7, 14, 24, 38],
    "lead(II) nitrate": [38, 54, 72, 91, 111],
    "potassium sulfate": [7, 11, 15, 18, 21],
}
TS = [0, 20, 40, 60, 80]


def sol_at(salt, T):
    """Piecewise-quadratic interpolation through the table values (as read from a smooth curve)."""
    v = SALTS_SOL[salt]
    i = min(int(T // 20), 3)
    if i >= 3:
        i = 2
    xs, ys = TS[i:i + 3], v[i:i + 3]
    tot = 0
    for j in range(3):
        term = ys[j]
        for k in range(3):
            if k != j:
                term *= (T - xs[k]) / (xs[j] - xs[k])
        tot += term
    return tot


@tpl(ST, "calculation", 16)
def states_sol_calc(r, k):
    kind = k % 4
    if kind == 0:
        w = r.choice([20, 25, 40, 50, 80])
        s = r.choice([12, 18, 24, 30, 36, 45, 52, 64])
        m = Fr(s * w, 100)
        T_ = r.choice([20, 30, 40, 50])
        stem = (f"A student finds that {num(m)} g of a salt is the maximum mass that dissolves in {w} g of water at {T_} °C.\n\n"
                "Calculate the solubility of the salt at this temperature in g per 100 g of water.")
        rows = [row("", f"M1 {num(m)} × 100 ÷ {w}", 1, "ALLOW scaling factor shown e.g. ×" + num(Fr(100, w)), "AO2"),
                row("", f"M2 {s} (g per 100 g of water)", 1, "Correct answer without working scores 2", "AO2")]
        return Q("Calculate", "1-3", [P("", stem, 2, space="working", answer_prefix="solubility = ", lines=4)], rows,
                 ["1.5C"], ans=("mass × 100 / mass of water", {"solubility": s}), ao=["AO2"])
    if kind == 1:
        dish = round(r.uniform(28, 45), 2)
        sol = round(r.uniform(15, 30), 2)
        s = r.choice([25, 30, 36, 40, 48, 55, 60])
        solid = round(sol * s / (100 + s), 2)
        water = round(sol - solid, 2)
        sv = round(solid / water * 100, 1)
        intro = ("A student evaporates a saturated solution of a salt to dryness to find its solubility at 25 °C. "
                 "These are the results.")
        tb = table(["Measurement", "Mass in g"], [["evaporating basin", f"{dish:.2f}"],
                                                 ["basin + saturated solution", f"{dish + sol:.2f}"],
                                                 ["basin + dry salt", f"{dish + solid:.2f}"]])
        parts = [P("a", "Calculate the mass of water that evaporated.", 1, space="working", answer_prefix="mass = ", lines=2),
                 P("b", "Calculate the solubility of the salt in g per 100 g of water. Give your answer to 3 significant figures.",
                   3, space="working", answer_prefix="solubility = ", lines=6)]
        rows = [row("a", f"{water:.2f} (g)", 1, None, "AO2"),
                row("b", f"M1 mass of salt = {solid:.2f} (g)", 1, None, "AO2"),
                row("b", f"M2 {solid:.2f} × 100 ÷ {water:.2f}", 1, "ALLOW ecf from (a)", "AO2"),
                row("b", f"M3 {num(sv, sf=3)} (g per 100 g of water)", 1, "ALLOW ecf; must be 3 sf for M3", "AO2")]
        return Q("Calculate", "4-6", parts, rows, ["1.5C", "1.7C"], intro=intro, figs=[tb],
                 ans=("(salt/water)×100", {"water": water, "solubility": float(num(sv, sf=3))}), ao=["AO2", "AO3"])
    if kind == 2:
        salt = r.choice(list(SALTS_SOL))
        t1, t2 = r.choice([(80, 20), (60, 20), (80, 40), (60, 0), (40, 0), (80, 0)])
        s1, s2 = SALTS_SOL[salt][TS.index(t1)], SALTS_SOL[salt][TS.index(t2)]
        w = r.choice([50, 100, 200, 25])
        cr = Fr((s1 - s2) * w, 100)
        stem = (f"The solubility of {salt} is {s1} g per 100 g of water at {t1} °C and {s2} g per 100 g of water at {t2} °C.\n\n"
                f"A saturated solution of {salt} in {w} g of water at {t1} °C is cooled to {t2} °C.\n\n"
                "Calculate the mass of crystals that form.")
        rows = [row("", f"M1 {s1} − {s2} = {s1 - s2} (g per 100 g)", 1, "ALLOW masses dissolved in "
                    f"{w} g at each temperature: {num(Fr(s1 * w, 100))} and {num(Fr(s2 * w, 100))}", "AO2"),
                row("", f"M2 {s1 - s2} × {w} ÷ 100", 1, None, "AO2"),
                row("", f"M3 {num(cr)} g", 1, "Correct answer with no working scores 3", "AO2")]
        if w == 100:
            rows = [row("", f"M1 {s1} − {s2}", 1, None, "AO2"), row("", f"M2 {num(cr)} g", 1, "ALLOW 2 marks for correct answer", "AO2")]
        mk = 2 if w == 100 else 3
        return Q("Calculate", "4-6" if w == 100 else "7-9", [P("", stem, mk, space="working", answer_prefix="mass = ", lines=6)],
                 rows, ["1.5C", "1.6C"], ans=("(s1-s2)*w/100", {"crystals_g": float(cr)}), ao=["AO2"])
    # kind 3: mass of salt in a given mass of saturated solution
    s = r.choice([20, 25, 40, 50, 60, 75, 80])
    tot = r.choice([30, 60, 90, 120, 150, 180])
    solute = Fr(tot * s, 100 + s)
    if solute.denominator > 100:
        return None
    stem = (f"The solubility of a salt at 30 °C is {s} g per 100 g of water.\n\n"
            f"Calculate the mass of salt dissolved in {tot} g of saturated solution at 30 °C. Give your answer to 2 decimal places.")
    rows = [row("", f"M1 {100 + s} g of solution contains {s} g of salt", 1, None, "AO2"),
            row("", f"M2 {s} × {tot} ÷ {100 + s}", 1, None, "AO2"),
            row("", f"M3 {num(float(solute), dp=2)} g", 1, "REJECT " + num(Fr(s * tot, 100), dp=2) + " (uses mass of water)", "AO2")]
    return Q("Calculate", "7-9", [P("", stem, 3, space="working", answer_prefix="mass = ", lines=6)], rows, ["1.5C"],
             ans=("s/(100+s) × mass of solution", {"salt_g": float(num(float(solute), dp=2))}), ao=["AO2"])


@tpl(ST, "data", 14)
def states_sol_curve(r, k):
    salts = list(SALTS_SOL)
    salt = salts[k % len(salts)]
    v = SALTS_SOL[salt]
    style = (k // len(salts)) % 2
    tb = table(["Temperature in °C"] + [str(t) for t in TS], [["Solubility in g per 100 g water"] + [str(x) for x in v]],
               caption=f"Solubility of {salt}")
    T1 = r.choice([10, 30, 50, 70])
    sT1 = sol_at(salt, T1)
    target = r.choice([v[1] + (v[2] - v[1]) // 2, v[2] + (v[3] - v[2]) // 2])
    # temperature where curve reaches target (search)
    Tt = min((abs(sol_at(salt, t / 10) - target), t / 10) for t in range(0, 801))[1]
    smax = max(sol_at(salt, t) for t in range(0, 81, 5))
    ystep = 20 if smax > 100 else 10
    ymax_ = ystep * math.ceil(smax / ystep)
    rows = []
    if style == 0:
        parts = [P("a", "Plot the data on the grid and draw a smooth curve of best fit.", 3, space="graph"),
                 P("b", f"Use your graph to find the solubility of {salt} at {T1} °C.", 1, answer_prefix="solubility = ", lines=1),
                 P("c", f"Use your graph to find the temperature at which the solubility is {target} g per 100 g of water.", 1,
                   answer_prefix="temperature = ", lines=1)]
        rows += [row("a", "M1 suitable linear scales using at least half the grid, axes labelled with units\n"
                          "M2 all five points plotted to ±½ small square\nM3 smooth curve through the points", 3,
                     "M2 dep on sensible scale; ALLOW one plotting error for M2", "AO3")]
        lab_b, lab_c = "b", "c"
        figs = [tb]
    else:
        g = graph("temperature in °C", "solubility in g per 100 g water",
                  [[(t, sol_at(salt, t)) for t in range(0, 81, 5)]], xmax=80, xstep=10, ystep=ystep, ymax=ymax_, markers=False)
        figs = [fig(g, 120, caption=f"Solubility curve for {salt}")]
        parts = [P("a", f"Use the graph to find the solubility of {salt} at {T1} °C.", 1, answer_prefix="solubility = ", lines=1),
                 P("b", f"Use the graph to find the temperature at which the solubility is {target} g per 100 g of water.", 1,
                   answer_prefix="temperature = ", lines=1),
                 P("c", f"Describe how the solubility of {salt} changes as temperature increases.", 1, lines=2)]
        lab_b, lab_c = "a", "b"
    ysq = ystep / 5  # one small square on the y-axis
    xsq = 10 / 5
    sv, tv = round(sT1, 1), round(Tt, 1)
    rows.append(row(lab_b, f"{num(sv)} g per 100 g water", 1,
                    f"ALLOW {num(round(sv - 2 * ysq, 1))} to {num(round(sv + 2 * ysq, 1))} (±2 small squares); ALLOW ecf from candidate's curve", "AO3"))
    rows.append(row(lab_c, f"{num(tv)} °C", 1, f"ALLOW {num(round(tv - 2 * xsq, 1))} to {num(round(tv + 2 * xsq, 1))} (±2 small squares)", "AO3"))
    if style == 1:
        rows.append(row("c", "solubility increases (as temperature increases)", 1,
                        "ALLOW increases more steeply at higher temperatures" if v[4] - v[3] > v[1] - v[0] + 5 else None, "AO3"))
    cool_from, cool_to = r.choice([(80, 20), (60, 20), (80, 40)])
    cr = v[TS.index(cool_from)] - v[TS.index(cool_to)]
    parts.append(P("d", f"A saturated solution of {salt} in 100 g of water is cooled from {cool_from} °C to {cool_to} °C. "
                        "Calculate the mass of solid that crystallises.", 2, space="working", answer_prefix="mass = ", lines=4))
    rows += [row("d", f"M1 {v[TS.index(cool_from)]} − {v[TS.index(cool_to)]}", 1, None, "AO2"),
             row("d", f"M2 {cr} g", 1, "ALLOW ecf from readings", "AO2")]
    return Q("Use", "4-6" if style else "7-9", parts, rows, ["1.6C", "1.5C"], figs=figs,
             ans=("interpolated curve", {"s_T1": round(sT1, 1), "T_target": round(Tt, 1), "crystals": cr}), ao=["AO3", "AO2"])


items(ST, "practical", "1.7C", [
    D(intro="A student finds the solubility of potassium chloride in water at 40 °C. She stirs excess solid into 50 g of water "
            "held at 40 °C in a water bath, filters off the undissolved solid and evaporates a weighed sample of the filtrate to dryness.",
      s="Explain why she uses excess solid and why the water bath must be kept at 40 °C.", m=2,
      p=["excess solid ensures the solution is saturated", "solubility depends on temperature (so temperature must stay constant)"], d="4-6"),
    D(s="In a solubility experiment the dish of salt is heated, cooled and weighed several times until the mass stops changing. "
        "Explain why this is done.", m=2, p=["to make sure all the water has evaporated", "so the mass recorded is the mass of dry salt only"], d="4-6"),
    D(s="Suggest why a saturated solution should be filtered through a warm funnel before its mass is measured in a solubility "
        "experiment carried out at 60 °C.", m=2, p=["to stop the solution cooling", "so that crystals do not form in the funnel / solution stays saturated at 60 °C"], d="7-9"),
    D(s="Give two safety precautions when evaporating a salt solution to dryness over a Bunsen burner.", m=2,
      p=["wear eye protection / goggles", "heat gently / stop heating before all water has gone to avoid spitting",
         "use tongs to handle the hot dish", "keep hair tied back"], any=True, d="1-3"),
    D(s="A student wants to find the solubility of a salt at 20 °C. Describe a method she could use.", m=4,
      p=["add salt to a known mass/volume of water at 20 °C and stir until no more dissolves / some solid remains",
         "filter off the undissolved solid", "weigh an evaporating basin, add the saturated solution and weigh again",
         "evaporate to dryness and weigh the solid (heat to constant mass)", "solubility = mass of solid ÷ mass of water × 100"],
      any=True, d="7-9"),
    D(intro="A student investigates how solubility changes with temperature. He dissolves a known mass of potassium nitrate "
            "in 10 cm³ of water in a boiling tube by warming, then lets the tube cool while stirring with a thermometer.",
      s="State what he should record and how he would know when the solution becomes saturated.", m=2,
      p=["record the temperature", "at which crystals first appear"], d="4-6"),
    D(s="In the experiment in which crystals first appear as a solution cools, suggest one reason why the temperature "
        "recorded may not be accurate, and how to improve it.", m=2,
      p=["crystals are hard to see first forming / solution cools fast / temperature not even", "repeat the cooling and take a mean / stir continuously / use a lens"], d="7-9"),
    D(s="Name the independent and dependent variables in an experiment to find how the solubility of a salt changes with temperature.", m=2,
      p=["independent: temperature", "dependent: mass of salt that dissolves (in 100 g of water) / solubility"], d="4-6"),
    D(intro="A teacher demonstrates diffusion by placing a crystal of a coloured salt in a beaker of water and leaving it undisturbed.",
      s="Give two variables that should be controlled if the experiment is repeated with water at a higher temperature.", m=2,
      p=["size/mass of crystal", "volume of water", "same salt", "same beaker / not stirring / same time"], any=True, ref="1.3", d="4-6"),
    D(s="Explain why the beaker should not be stirred or moved in an experiment to show diffusion of a coloured substance in water.", m=2,
      p=["stirring would mix the particles", "so the spreading would not be due to (random movement in) diffusion alone"], ref="1.3"),
    D(s="Suggest why the diffusion of ammonia and hydrogen chloride along a glass tube is done in a fume cupboard.", m=1,
      p=["the gases are toxic / harmful / corrosive"], ref="1.3", d="1-3"),
    D(s="Describe how you could show that the volume of water used in a solubility experiment does not affect the calculated "
        "solubility in g per 100 g of water.", m=2,
      p=["repeat the experiment with different (measured) masses of water at the same temperature",
         "the calculated solubility (mass ÷ mass of water × 100) should be the same"], d="7-9"),
])


@tpl(ST, "mcq", 6)
def states_state_mcq(r, k):
    subs = [("ethanol", -114, 78), ("bromine", -7, 59), ("mercury", -39, 357), ("chlorine", -101, -34),
            ("sodium", 98, 883), ("sulfur", 115, 445), ("ammonia", -78, -33), ("iodine", 114, 184),
            ("methane", -182, -162), ("phenol", 41, 182), ("hexane", -95, 69), ("gallium", 30, 2400)]
    name, mp, bp = subs[k % len(subs)]
    T_ = r.choice([-50, 0, 25, 50, 100, 150, 200, 300])
    st = "solid" if T_ < mp else ("liquid" if T_ < bp else "gas")
    if T_ in (mp, bp):
        return None
    part, rw = mcq(r, f"{name.capitalize()} melts at {mp} °C and boils at {bp} °C. What is its state at {T_} °C?", st,
                   [x for x in ["solid", "liquid", "gas", "a mixture of solid and gas"] if x != st])
    part["label"] = ""
    return Q("What", "1-3" if T_ == 25 else "4-6", [part], [rw], ["1.1"], ao=["AO2"], style="mcq",
             ans=("compare T with mp/bp", {"state": st}))


# =================================================================== 1(b) mixtures
facts(MX, "1.10", [
    D(mq="Which substance is a compound?", c="sodium chloride", w=["air", "sea water", "oxygen", "copper"], ref="1.8"),
    D(mq="Which substance is a mixture?", c="air", w=["water", "carbon dioxide", "magnesium oxide", "iron"], ref="1.8"),
    D(mq="Which method is best for obtaining pure water from sea water?", c="simple distillation",
      w=["filtration", "crystallisation", "paper chromatography"]),
    D(mq="Which method separates ethanol from a mixture of ethanol and water?", c="fractional distillation",
      w=["filtration", "simple distillation", "crystallisation"], d="4-6"),
    D(mq="Which method separates sand from a mixture of sand and water?", c="filtration",
      w=["crystallisation", "fractional distillation", "chromatography"]),
    D(mq="A sample of a solid melts over the range 112–118 °C. What does this show?", c="the solid is impure / a mixture",
      w=["the solid is pure", "the solid is an element", "the solid is a compound"], ref="1.9", d="4-6"),
    D(mq="Which method would be used to obtain copper(II) sulfate crystals from copper(II) sulfate solution?",
      c="crystallisation", w=["filtration", "simple distillation", "paper chromatography"]),
    D(mq="In paper chromatography, why is the baseline drawn in pencil?", c="pencil (graphite) does not dissolve in the solvent",
      w=["ink would be easier to see", "pencil marks travel up with the solvent", "pencil absorbs the solvent"], ref="1.13", d="4-6"),
    D(mq="A dye travels 3.6 cm and the solvent front travels 9.0 cm. What is the Rf value of the dye?", c="0.40",
      w=["0.36", "2.5", "5.4"], ref="1.12", d="4-6"),
    D(mq="What does a single spot on a chromatogram suggest about a dye?", c="it may be a pure substance",
      w=["it is a mixture of two dyes", "it is insoluble in the solvent", "it is an element"], ref="1.11"),
    D(mq="Which of these is an element?", c="nitrogen", w=["ammonia", "water", "air", "methane"], ref="1.8"),
    D(mq="Which liquid has a fixed boiling point of 100 °C at normal pressure?", c="pure water",
      w=["sea water", "salt solution", "ethanol"], ref="1.9"),
    D(mq="What is the name of the solid left on the filter paper after filtration?", c="residue",
      w=["filtrate", "solute", "distillate"]),
    D(mq="Which statement about fractional distillation is correct?", c="it separates liquids with different boiling points",
      w=["it separates a solid from a liquid", "it separates insoluble solids", "it separates dyes in ink"]),
], intro="This question is about elements, compounds and mixtures.")

facts(MX, "1.10", [
    D(q="State what is meant by the term **compound**.", a="a substance containing two or more elements chemically combined",
      n="REJECT mixed", ref="1.8"),
    D(q="State what is meant by the term **mixture**.", a="two or more substances not chemically combined / that can be separated by physical methods", ref="1.8"),
    D(q="Hexane and octane are miscible liquids that boil at 69 °C and 126 °C. Name the technique that would separate them.", a="fractional distillation"),
    D(q="Name the liquid that passes through the filter paper during filtration.", a="filtrate"),
    D(q="Give the name of the apparatus used to cool and condense the vapour in distillation.", a="(Liebig) condenser"),
    D(q="State how a melting point measurement shows that a solid is pure.", a="it melts at a single, fixed (sharp) temperature (matching data)", ref="1.9"),
    D(q="Name the method used to separate the coloured dyes in a sample of ink.", a="(paper) chromatography"),
    D(q="Give the equation used to calculate an Rf value.", a="Rf = (baseline to centre of spot) ÷ (baseline to solvent front)",
      n="both distances must be measured from the baseline", ref="1.12"),
    D(q="Give two reasons why the baseline in a chromatography experiment must be above the level of the solvent.", m=2,
      pts=["so the spots do not dissolve / wash into the solvent", "so the substances move up the paper with the solvent"], ref="1.13", d="4-6"),
    D(q="Name the method used to obtain salt crystals from salt solution.", a="crystallisation", n="ALLOW evaporation"),
    D(q="Name the type of glassware in which the liquid is boiled during simple distillation.", a="(round-bottomed / distillation) flask"),
    D(q="State why a fractionating column is needed when separating ethanol from water but not when separating water from salt.",
      a="ethanol and water have boiling points that are close together", d="7-9"),
    D(q="State the purpose of the thermometer at the top of the fractionating column.", a="to measure the boiling point of the vapour / show which liquid is distilling", d="4-6"),
], intro="This question is about separating mixtures.")

items(MX, "describe", "1.10", [
    D(s="Describe how a sample of pure water could be obtained from sea water in the laboratory.", m=3,
      p=["heat/boil the sea water (in a flask)", "water vapour/steam passes into a condenser", "vapour condenses and is collected (as distillate)"]),
    D(s="Describe how a mixture of sand and salt could be separated to give a dry sample of sand.", m=3,
      p=["add water and stir (to dissolve the salt)", "filter", "wash the sand (residue) with water and leave to dry / dry in a warm oven"]),
    D(s="Describe how crystals of {salt} can be obtained from a solution of {salt}.", m=3,
      p=["heat to evaporate some of the water (until crystals start to form / saturated)", "leave the solution to cool (and crystallise)",
         "filter off the crystals and dry them (between filter paper)"],
      v=[{"salt": "copper(II) sulfate"}, {"salt": "potassium nitrate"}, {"salt": "zinc sulfate"}]),
    D(s="Describe how fractional distillation separates a mixture of ethanol (boiling point 78 °C) and water.", m=4,
      p=["heat the mixture", "ethanol vapour (lower boiling point) rises up the fractionating column",
         "water condenses in the column and drips back", "ethanol passes into the condenser and is collected (at 78 °C)"], d="4-6"),
    D(s="Describe how you would carry out paper chromatography to find out how many dyes are in a black ink.", m=4,
      p=["draw a pencil baseline near the bottom of the paper and put a spot of ink on it",
         "place the paper in a beaker of solvent with the solvent below the baseline", "allow the solvent to rise up the paper (then remove)",
         "count the number of spots formed"], ref="1.13", d="4-6"),
    D(s="Describe how you could test whether a sample of a white solid is pure.", m=2,
      p=["measure its melting point", "pure if it melts at a sharp/fixed temperature (that matches the data value)"], ref="1.9"),
    D(s="Describe what happens to the vapour in the condenser during simple distillation.", m=2,
      p=["vapour is cooled (by the cold water)", "vapour condenses / turns to liquid"]),
    D(s="Describe how you would separate a mixture of iron filings and sulfur powder.", m=2,
      p=["use a magnet", "iron is attracted / pulled out, sulfur is left"], ref="1.8", d="1-3"),
    D(s="Describe how you would obtain a dry sample of chalk (calcium carbonate) from a mixture of chalk and water.", m=2,
      p=["filter the mixture", "dry the residue (in a warm oven / leave to dry)"]),
    D(s="Describe how a chromatogram of an unknown food colouring could be used to show it contains the dye E133.", m=2,
      p=["run a spot of E133 next to the unknown on the same paper", "a spot in the unknown at the same height / Rf as E133"], ref="1.11", d="4-6"),
    D(s="Describe one difference between how a pure substance and a mixture behave when heated until they boil.", m=2,
      p=["pure substance boils at a fixed temperature", "a mixture boils over a range of temperatures"], ref="1.9"),
    D(s="Describe how you could obtain pure, dry crystals of benzoic acid from a mixture of benzoic acid and sand. "
        "Benzoic acid dissolves well in hot water but only slightly in cold water.", m=4,
      p=["add hot water and stir (to dissolve the benzoic acid)", "filter (while hot) to remove the sand",
         "cool the filtrate so crystals form", "filter and dry the crystals"], d="7-9"),
])

items(MX, "explain", "1.10", [
    D(s="Explain why the spots on a chromatogram must be placed above the level of the solvent.", m=2,
      p=["otherwise the dyes would dissolve in the solvent (in the beaker)", "and would not move up the paper / no separation"], ref="1.13"),
    D(s="Explain why the baseline on chromatography paper is drawn in pencil and not in ink.", m=2,
      p=["pencil/graphite is insoluble in the solvent / will not move", "ink would dissolve and separate (and confuse the result)"], ref="1.13"),
    D(s="Explain how paper chromatography separates the dyes in a mixture.", m=2,
      p=["dyes have different solubilities in the solvent / different attractions to the paper", "so they move up the paper different distances"], ref="1.11", d="7-9"),
    D(s="Explain why the water in a condenser enters at the bottom and leaves at the top.", m=2,
      p=["the condenser fills completely with cold water", "so cooling is more efficient"], d="7-9"),
    D(s="Explain why a mixture of {a} and {b} can be separated by filtration.", m=2,
      p=["{a} is insoluble (in {b})", "so it is trapped by the filter paper while {b} passes through"],
      v=[{"a": "sand", "b": "water"}, {"a": "copper(II) oxide", "b": "copper(II) sulfate solution"}, {"a": "chalk", "b": "water"}]),
    D(s="Explain why simple distillation cannot be used to separate a mixture of two liquids whose boiling points are close together.", m=2,
      p=["both liquids evaporate / boil at about the same time", "so the distillate is still a mixture"], d="4-6"),
    D(s="Explain why the fractionating column is packed with glass beads.", m=2,
      p=["increases the surface area for condensation", "so the liquids separate better / repeated evaporation and condensation"], d="7-9"),
    D(s="A student says that a dye which gives a single spot with one solvent must be a pure substance. Explain why this may not be correct.", m=2,
      p=["two dyes could have the same Rf / move the same distance in that solvent", "(so) repeat with a different solvent (to check)"], ref="1.11", d="7-9"),
    D(s="Explain why a spot that stays on the baseline does not dissolve in the solvent and what this means for identifying it.", m=2,
      p=["the substance is insoluble in that solvent", "so a different solvent is needed to separate / identify it"], ref="1.11", d="7-9"),
    D(s="Explain why crystallisation is used instead of evaporating to dryness to obtain crystals of hydrated copper(II) sulfate.", m=2,
      p=["evaporating to dryness would remove the water of crystallisation", "so only anhydrous (white) powder / no proper crystals would form"], d="7-9"),
    D(s="Explain why the melting point of an impure solid is not a single temperature.", m=2,
      p=["impurities change / lower the melting point", "different substances melt at different temperatures so it melts over a range"], ref="1.9", d="4-6"),
    D(s="Explain why a lid is placed on the chromatography tank.", m=2,
      p=["keeps the air in the tank saturated with solvent vapour", "so the solvent does not evaporate from the paper (and rises evenly)"], ref="1.13", d="7-9"),
])

DYES = ["A", "B", "C", "D", "E", "F", "G", "H", "J", "K"]


@tpl(MX, "calculation", 16)
def mixtures_rf_calc(r, k):
    front = r.choice([6.0, 7.5, 8.0, 9.0, 10.0, 12.0, 6.4, 8.5])
    nd = 1 + k % 3
    dists = sorted(r.sample([round(front * x / 20, 1) for x in range(3, 19)], nd))
    rfs = [Fr(str(d)) / Fr(str(front)) for d in dists]
    lab = r.sample(DYES, nd)
    if nd == 1:
        stem = (f"In a chromatography experiment the solvent front moves {num(front)} cm from the baseline. Dye {lab[0]} "
                f"moves {num(dists[0])} cm from the baseline.\n\nCalculate the Rf value of dye {lab[0]}. Give your answer to 2 decimal places.")
        rows = [row("", f"M1 {num(dists[0])} ÷ {num(front)}", 1, None, "AO2"),
                row("", f"M2 {num(float(rfs[0]), dp=2)}", 1, "Correct answer without working scores 2; REJECT answers with units", "AO2")]
        return Q("Calculate", "1-3", [P("", stem, 2, space="working", answer_prefix="Rf = ", lines=4)], rows, ["1.12"],
                 ans=("d/front", {"Rf": float(num(float(rfs[0]), dp=2))}), ao=["AO2"])
    db = {"0.15": "tartrazine-like yellow", }
    known = [("red R", None), ("blue B", None)]
    tb = table(["Dye", "Distance moved from baseline in cm"], [[f"dye {l}", num(d)] for l, d in zip(lab, dists)] +
               [["solvent front", num(front)]])
    parts = [P("a", f"Calculate the Rf value of each dye. Give your answers to 2 decimal places.", nd, space="working", lines=4 * nd)]
    rows = [row("a", f"dye {l}: {num(d)} ÷ {num(front)} = {num(float(x), dp=2)}", 1, "ALLOW 2 or more dp if rounding correct", "AO2")
            for l, d, x in zip(lab, dists, rfs)]
    tgt = r.choice(range(nd))
    refdye = r.choice(["Ponceau", "Sunset", "Azure", "Indigo carmine", "Quinoline"])
    parts.append(P("b", f"A reference dye, {refdye}, has an Rf value of {num(float(rfs[tgt]), dp=2)} in this solvent. "
                        f"State which dye could be {refdye}.", 1, lines=1))
    rows.append(row("b", f"dye {lab[tgt]}", 1, "ALLOW ecf from (a)", "AO2"))
    return Q("Calculate", "4-6" if nd == 2 else "7-9", parts, rows, ["1.12", "1.11"], figs=[tb],
             intro="A student separates the dyes in a food colouring by paper chromatography. The table shows the results.",
             ans=("d/front", {f"Rf_{l}": float(num(float(x), dp=2)) for l, x in zip(lab, rfs)}), ao=["AO2", "AO3"])


@tpl(MX, "data", 16)
def mixtures_chromatogram(r, k):
    # unknown mixture X compared with reference dyes
    nref = 4
    front = 80
    refh = sorted(r.sample(range(12, 74, 4), nref))
    refs = r.sample(["P", "Q", "R", "S", "T", "U", "V", "W"], nref)
    contains = sorted(r.sample(range(nref), r.choice([2, 2, 3])))
    extra = r.random() < 0.4
    xcol = [refh[i] for i in contains] + ([r.choice([h for h in range(8, 76, 4) if h not in refh])] if extra else [])
    cols = [[h] for h in refh] + [xcol]
    labs = refs + ["X"]
    s = S.chromatogram(cols, labs, front_mm=front)
    dyes = ", ".join(refs[:-1]) + " and " + refs[-1]
    parts = [P("a", "State how many substances are present in mixture X.", 1, lines=1),
             P("b", f"Identify which of the dyes {dyes} are present in X. Give a reason for your answer.", 2, lines=4)]
    rows = [row("a", str(len(xcol)), 1, None, "AO3"),
            row("b", f"M1 {' and '.join(refs[i] for i in contains)}", 1, "all correct, no extras", "AO3"),
            row("b", "M2 spots (in X) at the same height / same Rf as these dyes", 1, None, "AO3")]
    if extra:
        parts.append(P("c", "Give evidence from the chromatogram that X contains a substance not shown in the reference dyes.", 1, lines=2))
        rows.append(row("c", "X has a spot at a height that does not match any reference spot", 1, None, "AO3"))
    h = r.choice(refh)
    who = refs[refh.index(h)]
    parts.append(P("d" if extra else "c", f"The spot for dye {who} is {h / 10:.1f} cm above the baseline and the solvent front is "
                                           f"{front / 10:.1f} cm above the baseline. Calculate the Rf value of dye {who}.", 2,
                   space="working", answer_prefix="Rf = ", lines=4))
    rf = Fr(h, front)
    rows += [row("d" if extra else "c", f"M1 {h / 10:.1f} ÷ {front / 10:.1f}", 1, None, "AO2"),
             row("d" if extra else "c", f"M2 {num(float(rf), dp=2)}", 1, "ALLOW correct to 2 or more sf", "AO2")]
    return Q("Use", "4-6", parts, rows, ["1.11", "1.12"], figs=[fig(s, 110, caption="Chromatogram (drawn to scale)")],
             intro=f"A food scientist uses paper chromatography to compare a mixture X with four reference dyes, {dyes}. The diagram shows the chromatogram.",
             ans=("count/match spots", {"n_substances": len(xcol), "Rf": float(num(float(rf), dp=2))}), ao=["AO3"])


items(MX, "practical", "1.13", [
    D(s="State why a pencil, not a pen, is used to draw the baseline in a chromatography experiment.", m=1,
      p=["pencil (graphite) does not dissolve / move with the solvent"], d="1-3"),
    D(s="Give two ways of making sure the results of a chromatography experiment are valid when comparing an unknown dye with known dyes.", m=2,
      p=["use the same solvent", "use the same piece of paper / same baseline", "spots the same size", "same time / same temperature"], any=True, d="4-6"),
    D(s="A student's spots smeared into long streaks up the paper. Suggest one cause and how to avoid it.", m=2,
      p=["spot too large / too concentrated / too much ink", "use a small spot (with a fine capillary tube) and let it dry"], d="7-9"),
    D(s="Suggest why a lid is placed over the beaker during paper chromatography.", m=1,
      p=["to stop the solvent evaporating (so it rises evenly)"], d="4-6"),
    D(s="State why the paper must be removed before the solvent reaches the top.", m=1,
      p=["so the solvent front can be marked / measured (to calculate Rf)"], d="4-6"),
    D(s="Some food colourings do not move from the baseline with water as the solvent. Suggest what the student should do.", m=1,
      p=["use a different solvent (e.g. ethanol)"], d="4-6"),
    D(s="Describe how to measure the distances needed to work out an Rf value.", m=2,
      p=["measure from the baseline to the centre of the spot", "measure from the baseline to the solvent front"], ref="1.12", d="4-6"),
    D(s="Give one safety precaution when using ethanol as a chromatography solvent.", m=1,
      p=["keep away from flames (flammable)", "use in a well-ventilated room"], any=True, d="1-3"),
    D(s="Explain why the dots of ink should be small and dried before the paper is put into the solvent.", m=2,
      p=["small spots give clear / separate spots", "drying stops the ink spreading / running"], d="7-9"),
    D(s="In a distillation experiment, suggest why anti-bumping granules are added to the flask.", m=1,
      p=["to give smooth boiling / stop violent boiling"], ref="1.10", d="4-6"),
    D(s="In a distillation experiment, explain why the bulb of the thermometer is placed level with the side arm.", m=2,
      p=["measures the temperature of the vapour entering the condenser", "to show which substance is distilling / its boiling point"], ref="1.10", d="7-9"),
    D(s="A student uses filtration followed by evaporation to get salt from rock salt. Suggest why her mass of salt was lower than expected.", m=2,
      p=["not all the salt dissolved (not enough water / stirring)", "some salt left in the residue / solution spat out on heating / lost on transfer"], any=True, d="7-9"),
])

MIXES = [
    ("salt from a mixture of salt and sand", ["add water and stir to dissolve the salt", "sand is insoluble", "filter the mixture",
     "sand stays on the filter paper as the residue; salt solution is the filtrate", "heat the filtrate to evaporate some water then leave to crystallise",
     "filter off and dry the salt crystals / evaporate to dryness"]),
    ("pure water and solid copper(II) sulfate from copper(II) sulfate solution", ["heat the solution in a flask (simple distillation)",
     "water boils / evaporates and the vapour passes into a condenser", "vapour condenses and pure water is collected",
     "copper(II) sulfate stays in the flask", "for crystals: stop heating when saturated and leave to cool / crystallise",
     "filter and dry the crystals"]),
    ("ethanol from a mixture of ethanol and water", ["heat the mixture in a flask fitted with a fractionating column",
     "ethanol has the lower boiling point (78 °C)", "vapours rise; water (higher boiling point) condenses in the column and returns",
     "thermometer at the top reads 78 °C while ethanol distils", "ethanol vapour condenses in the condenser and is collected",
     "change the collecting flask when the temperature rises above 78 °C"]),
    ("the dyes in a green food colouring and identify them", ["pencil baseline; spot of the colouring and spots of known dyes",
     "stand the paper in solvent below the baseline", "lid on; allow solvent to rise most of the way", "remove and mark the solvent front; dry",
     "compare heights of spots / calculate Rf values", "dyes with the same Rf / height as known dyes are present"]),
    ("iron filings, salt and sand from a mixture of all three", ["use a magnet to remove the iron filings", "add water to the rest and stir to dissolve the salt",
     "filter: sand is the residue", "wash and dry the sand", "evaporate / crystallise the filtrate to get salt", "dry the salt crystals"]),
    ("pure, dry potassium nitrate crystals from a mixture of potassium nitrate and charcoal powder",
     ["add (warm) water and stir to dissolve potassium nitrate", "charcoal is insoluble", "filter to remove charcoal",
      "warm the filtrate to evaporate some water until saturated", "cool to crystallise (solubility falls on cooling)", "filter and dry the crystals between filter paper"]),
    ("hexane (boiling point 69 °C) and heptane (boiling point 98 °C) from a mixture of the two",
     ["fractional distillation", "heat the mixture gently in a flask with a fractionating column", "hexane vapour reaches the top first (lower boiling point)",
      "collect the distillate while the thermometer reads about 69 °C", "change the receiver when the temperature rises", "collect heptane at about 98 °C"]),
    ("a sample of pure water from muddy sea water", ["filter to remove the mud (insoluble)", "the filtrate still contains dissolved salts",
     "distil the filtrate: heat to boil the water", "steam passes into a condenser cooled by water", "condenses to pure water which is collected",
     "test purity: boils at exactly 100 °C"]),
    ("zinc sulfate crystals from a mixture of zinc sulfate solution and unreacted zinc powder",
     ["filter to remove excess zinc (insoluble)", "collect zinc sulfate solution as the filtrate", "heat the filtrate to evaporate some water",
      "until crystals appear on a cold glass rod / saturated", "leave to cool and crystallise", "filter off and dry the crystals"]),
    ("the coloured substances in a leaf extract", ["crush the leaf with a solvent (e.g. propanone) and filter", "put a concentrated spot on a pencil baseline",
     "place the paper in a tank of solvent below the baseline", "let the solvent travel up the paper; mark the solvent front", "different pigments travel different distances",
     "calculate Rf values / count spots"]),
    ("sugar from a mixture of sugar and powdered glass", ["add water and stir to dissolve the sugar", "glass is insoluble",
     "filter: glass is the residue", "warm the filtrate to remove some water", "leave to cool to form sugar crystals (do not overheat / char)", "filter and dry the crystals"]),
    ("pure water from a solution of blue ink", ["simple distillation", "heat the ink in a flask", "water evaporates; dye particles stay behind",
     "vapour passes through a water-cooled condenser", "colourless water collected in a beaker", "check purity: boiling point 100 °C"]),
]

extended(MX, "1.10", [
    D(s=f"Describe how you would obtain {m}.", ind=p, title="Separation of a mixture", d="7-9" if i % 3 == 2 else "4-6",
      ao="AO1 4, AO3 2", ref=["1.10", "1.11"] if "dye" in m or "colour" in m else "1.10") for i, (m, p) in enumerate(MIXES)
])

# =================================================================== 1(c) atomic structure
facts(AT, "1.15", [
    D(mq="What is the relative mass of a neutron?", c="1", w=["0", "1/1836", "−1"]),
    D(mq="What is the relative charge of an electron?", c="−1", w=["0", "+1", "1/1836"]),
    D(mq="Where are the neutrons in an atom?", c="in the nucleus", w=["in the shells", "orbiting the nucleus", "spread evenly through the atom"]),
    D(mq="What is the mass number of an atom?", c="the number of protons plus neutrons", w=["the number of protons", "the number of neutrons",
      "the number of protons plus electrons"], ref="1.16"),
    D(mq="Atoms of isotopes of the same element have different numbers of", c="neutrons", w=["protons", "electrons", "shells"], ref="1.16"),
    D(mq="Why do isotopes of an element have the same chemical properties?", c="they have the same electronic configuration",
      w=["they have the same mass number", "they have the same number of neutrons", "they have the same density"], ref="1.16", d="7-9"),
    D(mq="What is the relative charge of a proton?", c="+1", w=["−1", "0", "+2"]),
    D(mq="Which particle has a very small relative mass?", c="electron", w=["neutron", "proton", "nucleus"]),
    D(mq="What is a molecule?", c="two or more atoms chemically bonded together", w=["a single atom", "a charged atom", "a mixture of atoms"], ref="1.14"),
    D(mq="Why is an atom electrically neutral overall?", c="it has equal numbers of protons and electrons",
      w=["it has equal numbers of protons and neutrons", "neutrons cancel the charge of the electrons", "it has no charged particles"], d="4-6"),
    D(mq="Relative atomic mass is compared with the mass of an atom of", c="carbon-12", w=["hydrogen-1", "oxygen-16", "helium-4"], ref="1.16", d="7-9"),
    D(mq="What is the atomic number of an element?", c="the number of protons in an atom", w=["the number of neutrons in an atom",
      "the number of protons and neutrons", "the number of shells"], ref="1.16"),
])

ISOS = [("C", 12, 6), ("O", 16, 8), ("Na", 23, 11), ("Cl", 37, 17), ("Cl", 35, 17), ("K", 39, 19), ("Ca", 40, 20), ("Al", 27, 13),
        ("Mg", 26, 12), ("S", 34, 16), ("Fe", 56, 26), ("Cu", 65, 29), ("Br", 81, 35), ("U", 238, 92), ("Li", 6, 3), ("Ar", 40, 18),
        ("Zn", 64, 30), ("Ne", 22, 10), ("B", 10, 5), ("Ag", 107, 47)]
EL["U"] = (92, "238", "uranium")


@tpl(AT, "mcq", 6)
def atoms_particle_mcq(r, k):
    sym, A, Z = ISOS[(k * 7) % len(ISOS)]
    ask = r.choice(["neutrons", "protons", "electrons"])
    ans = {"neutrons": A - Z, "protons": Z, "electrons": Z}[ask]
    wrong = sorted({A, A - Z, Z, A + Z, A - 2 * Z if A - 2 * Z > 0 else Z + 1} - {ans})
    part, rw = mcq(r, f"An atom of {EL[sym][2]} has mass number {A} and atomic number {Z}. How many {ask} does it have?",
                   str(ans), [str(w) for w in wrong])
    part["label"] = ""
    return Q("What", "1-3", [part], [rw], ["1.16"], style="mcq", ans=("A-Z", {ask: ans}), ao=["AO2"])


@tpl(AT, "recall", 14)
def atoms_table_recall(r, k):
    picks = r.sample(ISOS, 3)
    ions = {"Na": 1, "Mg": 2, "Al": 3, "K": 1, "Ca": 2, "Li": 1, "Cl": -1, "O": -2, "S": -2, "Br": -1}
    rows_t, rows_ms = [], []
    for sym, A, Z in picks:
        q = 0
        if r.random() < 0.4 and sym in ions:
            q = ions[sym]
        e = Z - q
        label = f"{sym}" + (("^" + (str(abs(q)) if abs(q) > 1 else "") + ("+" if q > 0 else "-")) if q else "")
        name = F(f"{A}{label}") if False else (f"{EL[sym][2]}-{A}" + (f" ion, {F(label)}" if q else " atom"))
        hide = r.sample(["p", "n", "e"], 2)
        cells = {"p": str(Z), "n": str(A - Z), "e": str(e)}
        rows_t.append([name] + [("[[blank]]" if c in hide else cells[c]) for c in "pne"])
        rows_ms.append(f"{name}: " + ", ".join(f"{dict(p='protons', n='neutrons', e='electrons')[c]} = {cells[c]}" for c in hide))
    tb = table(["Particle", "Number of protons", "Number of neutrons", "Number of electrons"], rows_t)
    part = P("", "Complete the table.", 3, space="table")
    part["figures"] = [tb]
    rws = [row("", x, 1, "both numbers needed for the mark", "AO1") for x in rows_ms]
    has_ion = any("ion" in x for x in rows_ms)
    return Q("Complete", "4-6" if has_ion else "1-3", [part], rws, ["1.15", "1.16"],
             ans=("Z, A-Z, Z-charge", {"rows": rows_ms}), ao=["AO1", "AO2"])


items(AT, "explain", "1.16", [
    D(s="Explain why chlorine-35 and chlorine-37 are isotopes of the same element.", m=2,
      p=["same number of protons (17) / same atomic number", "different numbers of neutrons (18 and 20) / different mass numbers"]),
    D(s="Explain why isotopes of an element have the same chemical properties.", m=2,
      p=["they have the same number of electrons / electronic configuration", "chemical reactions involve electrons (in the outer shell)"], d="7-9"),
    D(s="Explain why the relative atomic mass of chlorine is not a whole number.", m=2,
      p=["chlorine exists as a mixture of isotopes", "Ar is a (weighted) average of their masses (based on abundance)"], ref="1.17", d="4-6"),
    D(s="Explain why an atom of {el} has no overall charge.", m=2,
      p=["it has {z} protons (positive) and {z} electrons (negative)", "the charges cancel out"],
      v=[{"el": "sodium", "z": 11}, {"el": "sulfur", "z": 16}, {"el": "calcium", "z": 20}]),
    D(s="Explain why almost all the mass of an atom is in its nucleus.", m=2,
      p=["protons and neutrons (in the nucleus) have relative mass 1", "electrons have a very small mass (about 1/1836)"], ref="1.15", d="4-6"),
    D(s="Explain why a magnesium ion, Mg^2+, has a positive charge.", m=2,
      p=["it has lost two electrons", "so it has 12 protons but only 10 electrons / more protons than electrons"], ref="1.15", d="4-6"),
    D(s="Explain the difference between an atom and a molecule, using oxygen as an example.", m=2,
      p=["an atom is the smallest particle of an element (O)", "a molecule is two or more atoms bonded together (O2)"], ref="1.14"),
    D(s="Hydrogen has three isotopes: hydrogen-1, hydrogen-2 and hydrogen-3. Explain how their atoms differ and how they are alike.", m=3,
      p=["all have one proton / one electron", "they have 0, 1 and 2 neutrons respectively", "so mass numbers are 1, 2 and 3"], d="7-9"),
    D(s="The relative atomic mass of {el} is {ar}. Explain what this shows about the most common isotope.", m=2,
      p=["Ar is close to {near}", "so the isotope with mass number {near} is the most abundant"],
      v=[{"el": "boron", "ar": "10.8", "near": 11}, {"el": "copper", "ar": "63.5", "near": 63}, {"el": "magnesium", "ar": "24.3", "near": 24}],
      ref="1.17", d="7-9"),
    D(s="Explain why the atomic number, not the mass number, identifies an element.", m=2,
      p=["all atoms of an element have the same number of protons", "mass number can differ between isotopes (different neutrons)"], d="7-9"),
])


AR_DATA = [("chlorine", [(35, 75), (37, 25)]), ("boron", [(10, 20), (11, 80)]), ("copper", [(63, 69), (65, 31)]),
           ("lithium", [(6, 7.5), (7, 92.5)]), ("gallium", [(69, 60), (71, 40)]), ("bromine", [(79, 51), (81, 49)]),
           ("magnesium", [(24, 79), (25, 10), (26, 11)]), ("silicon", [(28, 92), (29, 5), (30, 3)]),
           ("neon", [(20, 90.5), (21, 0.3), (22, 9.2)]), ("rubidium", [(85, 72), (87, 28)]), ("silver", [(107, 52), (109, 48)]),
           ("potassium", [(39, 93), (41, 7)]), ("antimony", [(121, 57), (123, 43)]), ("europium", [(151, 48), (153, 52)])]


@tpl(AT, "calculation", 20)
def atoms_ar_calc(r, k):
    name, iso = AR_DATA[k % len(AR_DATA)]
    iso = [(m, ab) for m, ab in iso]
    if k >= len(AR_DATA):  # a sample with altered abundances
        tot = 100
        if len(iso) == 2:
            a = r.choice(range(15, 86, 5))
            iso = [(iso[0][0], a), (iso[1][0], tot - a)]
        else:
            a, b = r.choice([(70, 20), (80, 12), (75, 15), (60, 25)])
            iso = [(iso[0][0], a), (iso[1][0], b), (iso[2][0], tot - a - b)]
    if k % 3 == 2 and len(iso) == 2 and k >= len(AR_DATA):
        # reverse: find abundance from Ar
        ar = Fr(iso[0][0] * Fr(str(iso[0][1])) + iso[1][0] * Fr(str(iso[1][1])), 100)
        x = Fr(str(iso[0][1]))
        stem = (f"A sample of {name} contains only the isotopes {name}-{iso[0][0]} and {name}-{iso[1][0]}. Its relative atomic mass "
                f"is {num(float(ar), dp=2)}.\n\nCalculate the percentage abundance of {name}-{iso[0][0]} in the sample.")
        if Fr(num(float(ar), dp=2)) != ar:
            return None
        rows = [row("", f"M1 let abundance of {name}-{iso[0][0]} = x %; then {iso[1][0]} has (100 − x) %", 1, None, "AO2"),
                row("", f"M2 {iso[0][0]}x + {iso[1][0]}(100 − x) = {num(float(ar * 100))}", 1, None, "AO2"),
                row("", f"M3 x = {num(x)} (%)", 1, "Correct answer without working scores 1 only", "AO2")]
        return Q("Calculate", "7-9", [P("", stem, 3, space="working", answer_prefix="abundance = ", lines=6)], rows, ["1.17"],
                 ans=("solve weighted mean", {"abundance": float(x)}), ao=["AO2"])
    ar = sum(m * Fr(str(a)) for m, a in iso) / sum(Fr(str(a)) for _, a in iso)
    tb = table(["Isotope", "Mass number", "Percentage abundance"], [[f"{name}-{m}", str(m), num(a)] for m, a in iso])
    stem = f"Work out the relative atomic mass of {name} in this sample from the data in the table. Give your answer to 1 decimal place."
    prod = " + ".join(f"({m} × {num(a)})" for m, a in iso)
    rows = [row("", f"M1 {prod}", 1, None, "AO2"),
            row("", f"M2 ÷ 100 (= {num(float(ar), dp=3) if ar.denominator != 1 else num(ar)})", 1, "M1 and M2 can be scored in one step", "AO2"),
            row("", f"M3 {num(float(ar), dp=1)}", 1, "Correct answer without working scores 3; ALLOW ecf for 1 dp rounding of a wrong value", "AO2")]
    return Q("Calculate", "4-6" if len(iso) == 2 else "7-9", [P("", stem, 3, space="working", answer_prefix="relative atomic mass = ", lines=6)],
             rows, ["1.17"], figs=[tb], intro=f"The table shows the isotopes in a sample of {name}.",
             ans=("weighted mean", {"Ar": float(num(float(ar), dp=1))}), ao=["AO2"])


# =================================================================== 1(d) periodic table
facts(PT, "1.18", [
    D(mq="How are the elements arranged in the Periodic Table?", c="in order of increasing atomic number",
      w=["in order of increasing mass number", "in alphabetical order", "in order of the date they were discovered"]),
    D(mq="What name is given to a vertical column of the Periodic Table?", c="group", w=["period", "series", "block"]),
    D(mq="Why do elements in the same group have similar chemical properties?", c="they have the same number of outer electrons",
      w=["they have the same number of shells", "they have the same number of neutrons", "they have the same atomic mass"], ref="1.23"),
    D(mq="Why are the noble gases unreactive?", c="their outer shells are full", w=["they are gases", "they have no electrons",
      "they have an even number of protons"], ref="1.24"),
    D(mq="An element has an acidic oxide and does not conduct electricity. What is it most likely to be?", c="a non-metal",
      w=["a metal", "a noble gas", "a transition metal"], ref="1.20", d="4-6"),
    D(mq="Which property is typical of a metal?", c="it forms a basic oxide", w=["it forms an acidic oxide", "it is a poor conductor of heat",
      "it has a low density and is brittle"], ref="1.20"),
    D(mq="What is the electronic configuration of an atom of magnesium?", c="2.8.2", w=["2.8", "2.2.8", "2.8.8.2"], ref="1.19"),
    D(mq="Which element is in Group 6 and Period 3?", c="sulfur", w=["oxygen", "selenium", "phosphorus"], ref="1.22", d="4-6"),
    D(mq="Elements on which side of the Periodic Table are metals?", c="the left-hand side and centre", w=["the right-hand side", "the top row only", "Group 0"], ref="1.21"),
    D(mq="Which element has the electronic configuration 2.8.7?", c="chlorine", w=["fluorine", "argon", "sulfur"], ref="1.19"),
    D(mq="Sulfur dioxide dissolves in water to give a solution of pH 3. What does this tell you about sulfur?",
      c="it is a non-metal because it forms an acidic oxide", w=["it is a metal because it forms an acidic oxide",
      "it is a metal because the oxide dissolves", "it is a noble gas"], ref="1.20", d="7-9"),
    D(mq="What does the period number of an element tell you?", c="the number of occupied electron shells",
      w=["the number of outer electrons", "the number of neutrons", "the charge on its ion"], ref="1.22"),
])

Z20 = [s for s in EL if EL[s][0] <= 20]


@tpl(PT, "mcq", 8)
def periodic_config_mcq(r, k):
    sym = Z20[(k * 3 + 2) % 20]
    z = EL[sym][0]
    if r.random() < 0.5:
        c = config(z)
        wrong = {config(z + 1) if z < 20 else "2.8.8.3", config(z - 1) if z > 1 else "2", c[::-1] if len(c) > 1 else "1.1",
                 ".".join(reversed(c.split(".")))}
        wrong.discard(c)
        part, rw = mcq(r, f"What is the electronic configuration of an atom of {EL[sym][2]}?", c, sorted(wrong))
        ans = {"config": c}
    else:
        g, p = GROUP[sym], PERIOD[sym]
        c = f"Group {g}, Period {p}"
        wrong = {f"Group {p}, Period {g}", f"Group {g}, Period {p + 1}", f"Group {(g % 7) + 1}, Period {p}"}
        wrong.discard(c)
        if len(wrong) < 3:
            wrong.add(f"Group {g + 1 if g < 7 else 1}, Period {p + 1}")
        part, rw = mcq(r, f"An atom of element Z has the electronic configuration {config(z)}. Where is Z in the Periodic Table?", c, sorted(wrong))
        ans = {"group": g, "period": p}
    part["label"] = ""
    return Q("What", "1-3", [part], [rw], ["1.19", "1.22"], style="mcq", ans=("config", ans), ao=["AO2"])


@tpl(PT, "recall", 16)
def periodic_use_table(r, k):
    syms = r.sample([s for s in Z20 if s not in ("H", "He")], 3)
    a, b, c = syms
    parts = [P("a", f"Give the name of the element with atomic number {EL[a][0]}.", 1, lines=1),
             P("b", f"Give the electronic configuration of an atom of {EL[b][2]}.", 1, lines=1),
             P("c", f"Give the number of the group and the number of the period that contain {EL[c][2]}.", 2, lines=2)]
    gc = "0" if GROUP[c] == 0 else str(GROUP[c])
    rows = [row("a", EL[a][2], 1, f"ALLOW {a}", "AO1"), row("b", config(EL[b][0]), 1, "ALLOW any separator", "AO1"),
            row("c", f"Group {gc}", 1, "ALLOW 8 for Group 0" if gc == "0" else None, "AO1"), row("c", f"Period {PERIOD[c]}", 1, None, "AO1")]
    mt = r.choice([s for s in Z20 if s not in syms])
    is_metal = mt in ("Li", "Be", "Na", "Mg", "Al", "K", "Ca")
    parts.append(P("d", f"State whether {EL[mt][2]} is a metal or a non-metal.", 1, lines=1))
    rows.append(row("d", "metal" if is_metal else "non-metal", 1, None, "AO1"))
    return Q("Give", "1-3", parts, rows, ["1.18", "1.19", "1.21"], intro="Use the Periodic Table to help you answer this question.",
             ans=("lookup", {"a": EL[a][2], "b": config(EL[b][0]), "group": gc, "period": PERIOD[c]}), ao=["AO1"])


items(PT, "explain", "1.23", [
    D(s="Explain why {a} and {b} have similar chemical properties.", m=2,
      p=["both are in Group {g}", "both have {g} electron(s) in the outer shell"],
      v=[{"a": "lithium", "b": "sodium", "g": 1}, {"a": "fluorine", "b": "chlorine", "g": 7}, {"a": "magnesium", "b": "calcium", "g": 2},
         {"a": "oxygen", "b": "sulfur", "g": 6}]),
    D(s="Explain why argon is unreactive.", m=2, p=["argon has a full outer shell (of 8 electrons)", "so it does not need to gain, lose or share electrons"], ref="1.24"),
    D(s="Explain how the electronic configuration of {el} shows its position in the Periodic Table.", m=2,
      p=["{n} shells (occupied) so Period {p}", "{o} outer electron(s) so Group {g}"],
      v=[{"el": "aluminium", "n": 3, "p": 3, "o": 3, "g": 3}, {"el": "potassium", "n": 4, "p": 4, "o": 1, "g": 1},
         {"el": "nitrogen", "n": 2, "p": 2, "o": 5, "g": 5}], ref="1.22", d="4-6"),
    D(s="A student burns an element in oxygen and dissolves the oxide in water. The solution turns universal indicator blue. "
        "Explain what this shows about the element.", m=2,
      p=["the oxide is basic / alkaline", "so the element is a metal"], ref="1.20", d="4-6"),
    D(s="Explain how you could use a simple circuit to decide whether a solid element is a metal or a non-metal.", m=2,
      p=["connect the solid into a circuit with a bulb / ammeter", "if it conducts (bulb lights) it is a metal (graphite is an exception)"], ref="1.20", d="4-6"),
    D(s="Explain why helium is placed in Group 0 even though it has only two outer electrons.", m=2,
      p=["its outer (first) shell is full", "so it is unreactive like the other noble gases"], ref="1.24", d="7-9"),
    D(s="Explain why the element with atomic number 19 is placed directly below sodium in the Periodic Table.", m=2,
      p=["its configuration is 2.8.8.1", "it has one outer electron like sodium (2.8.1) so is in Group 1"], ref="1.19", d="4-6"),
    D(s="Explain why the elements in the Periodic Table are arranged in order of atomic number rather than relative atomic mass.", m=2,
      p=["atomic number (protons) is unique to each element", "elements then fall into groups with the same outer electrons / similar properties"], ref="1.18", d="7-9"),
    D(s="Element E is a dull, brittle yellow solid that does not conduct electricity. Its oxide dissolves in water to form an acidic solution. "
        "Explain which side of the Periodic Table E is found on.", m=2,
      p=["E is a non-metal (non-conductor, acidic oxide)", "so E is on the right-hand side"], ref="1.21", d="4-6"),
    D(s="Explain why neon does not form compounds but fluorine is very reactive, even though their atomic numbers differ by only one.", m=3,
      p=["neon has a full outer shell (2.8)", "fluorine (2.7) needs to gain one electron to fill its outer shell", "so fluorine reacts readily"], ref="1.24", d="7-9"),
])


# =================================================================== 1(e) formulae, equations, calculations
COMPOUNDS = ["H2O", "CO2", "NaCl", "MgO", "CaCO3", "H2SO4", "NaOH", "NH3", "CH4", "C2H5OH", "CuSO4", "Ca(OH)2", "Al2O3",
             "Fe2O3", "(NH4)2SO4", "Mg(NO3)2", "K2CO3", "Na2SO4", "CuO", "ZnCl2", "HNO3", "C6H12O6", "Al2(SO4)3", "CuSO4·5H2O",
             "C3H8", "Pb(NO3)2", "KMnO4", "NaHCO3", "MgCl2", "Ca3(PO4)2"]


@tpl(FO, "mcq", 14)
def formulae_mr_mcq(r, k):
    f = COMPOUNDS[(k * 7) % len(COMPOUNDS)]
    kind = k % 3
    if kind == 0:
        m = Mr(f)
        wrong = {num(m + r.choice([2, 16, 17, 18])), num(m - r.choice([1, 12, 16]) if m > 20 else m + 1), num(m * 2), num(m + 32)}
        wrong.discard(num(m))
        part, rw = mcq(r, f"What is the relative formula mass (Mr) of {F(f)}?", num(m), sorted(wrong, key=float))
        ans = {"Mr": float(m)}
        refs = ["1.26"]
    elif kind == 1:
        m = Mr(f)
        mol = r.choice([Fr(1, 10), Fr(1, 4), Fr(1, 2), Fr(2), Fr(1, 5), Fr(3, 2)])
        mass = m * mol
        wrong = {num(float(mass / mol / mol)) if mol != 1 else num(m + 1), num(float(m / mol)) if mol != 1 else "2", num(float(mass * 2)), num(float(m))}
        wrong.discard(num(float(mass)))
        part, rw = mcq(r, f"What is the mass of {num(float(mol))} mol of {F(f)}? [Mr = {num(m)}]", num(float(mass)) + " g",
                       [w + " g" for w in sorted(wrong, key=float)][:3])
        ans = {"mass": float(mass)}
        refs = ["1.28"]
    else:
        at = __import__("chemistry_util").atoms(f)
        n = sum(at.values())
        wrong = {n + 1, n - 1, len(at), n + 2}
        wrong.discard(n)
        part, rw = mcq(r, f"How many atoms are shown in the formula {F(f)}?", str(n), [str(x) for x in sorted(wrong)])
        ans = {"atoms": n}
        refs = ["1.26"]
    part["label"] = ""
    return Q("What", "1-3" if kind != 1 else "4-6", [part], [rw], refs, style="mcq", ans=("Mr", ans), ao=["AO2"])


# equations database: (word equation, symbol equation with states)
EQNS = [
    ("magnesium + oxygen → magnesium oxide", "2Mg(s) + O2(g) -> 2MgO(s)"),
    ("sodium + water → sodium hydroxide + hydrogen", "2Na(s) + 2H2O(l) -> 2NaOH(aq) + H2(g)"),
    ("calcium carbonate → calcium oxide + carbon dioxide", "CaCO3(s) -> CaO(s) + CO2(g)"),
    ("methane + oxygen → carbon dioxide + water", "CH4(g) + 2O2(g) -> CO2(g) + 2H2O(l)"),
    ("zinc + hydrochloric acid → zinc chloride + hydrogen", "Zn(s) + 2HCl(aq) -> ZnCl2(aq) + H2(g)"),
    ("aluminium + oxygen → aluminium oxide", "4Al(s) + 3O2(g) -> 2Al2O3(s)"),
    ("iron(III) oxide + carbon monoxide → iron + carbon dioxide", "Fe2O3(s) + 3CO(g) -> 2Fe(l) + 3CO2(g)"),
    ("propane + oxygen → carbon dioxide + water", "C3H8(g) + 5O2(g) -> 3CO2(g) + 4H2O(l)"),
    ("sodium hydroxide + sulfuric acid → sodium sulfate + water", "2NaOH(aq) + H2SO4(aq) -> Na2SO4(aq) + 2H2O(l)"),
    ("copper(II) oxide + sulfuric acid → copper(II) sulfate + water", "CuO(s) + H2SO4(aq) -> CuSO4(aq) + H2O(l)"),
    ("calcium carbonate + hydrochloric acid → calcium chloride + water + carbon dioxide", "CaCO3(s) + 2HCl(aq) -> CaCl2(aq) + H2O(l) + CO2(g)"),
    ("potassium + water → potassium hydroxide + hydrogen", "2K(s) + 2H2O(l) -> 2KOH(aq) + H2(g)"),
    ("hydrogen + oxygen → water", "2H2(g) + O2(g) -> 2H2O(l)"),
    ("lithium + oxygen → lithium oxide", "4Li(s) + O2(g) -> 2Li2O(s)"),
    ("chlorine + potassium bromide → potassium chloride + bromine", "Cl2(aq) + 2KBr(aq) -> 2KCl(aq) + Br2(aq)"),
    ("ethane + oxygen → carbon dioxide + water", "2C2H6(g) + 7O2(g) -> 4CO2(g) + 6H2O(l)"),
    ("iron + chlorine → iron(III) chloride", "2Fe(s) + 3Cl2(g) -> 2FeCl3(s)"),
    ("sodium carbonate + nitric acid → sodium nitrate + water + carbon dioxide", "Na2CO3(aq) + 2HNO3(aq) -> 2NaNO3(aq) + H2O(l) + CO2(g)"),
    ("magnesium + steam → magnesium oxide + hydrogen", "Mg(s) + H2O(g) -> MgO(s) + H2(g)"),
    ("copper(II) carbonate → copper(II) oxide + carbon dioxide", "CuCO3(s) -> CuO(s) + CO2(g)"),
    ("ammonia + oxygen → nitrogen monoxide + water", "4NH3(g) + 5O2(g) -> 4NO(g) + 6H2O(g)"),
    ("lead(II) nitrate + potassium iodide → lead(II) iodide + potassium nitrate", "Pb(NO3)2(aq) + 2KI(aq) -> PbI2(s) + 2KNO3(aq)"),
    ("aluminium + iron(III) oxide → aluminium oxide + iron", "2Al(s) + Fe2O3(s) -> Al2O3(s) + 2Fe(l)"),
    ("butane + oxygen → carbon dioxide + water", "2C4H10(g) + 13O2(g) -> 8CO2(g) + 10H2O(l)"),
    ("calcium + water → calcium hydroxide + hydrogen", "Ca(s) + 2H2O(l) -> Ca(OH)2(aq) + H2(g)"),
    ("sulfur dioxide + oxygen → sulfur trioxide", "2SO2(g) + O2(g) -> 2SO3(g)"),
    ("silver nitrate + sodium chloride → silver chloride + sodium nitrate", "AgNO3(aq) + NaCl(aq) -> AgCl(s) + NaNO3(aq)"),
    ("magnesium + hydrochloric acid → magnesium chloride + hydrogen", "Mg(s) + 2HCl(aq) -> MgCl2(aq) + H2(g)"),
    ("nitrogen + hydrogen → ammonia", "N2(g) + 3H2(g) -> 2NH3(g)"),
    ("titanium(IV) chloride + sodium → titanium + sodium chloride", "TiCl4(l) + 4Na(l) -> Ti(s) + 4NaCl(s)"),
]


@tpl(FO, "equation", 40)
def formulae_equations(r, k):
    word, sym = EQNS[k % len(EQNS)]
    mode = (k // len(EQNS)) % 3
    L_, R_ = __import__("chemistry_util").eq_terms(sym)
    skel = __import__("chemistry_util").unbalanced_skeleton(sym)
    unfamiliar = any(x in word for x in ("titanium", "ammonia + oxygen", "lead(II) nitrate", "silver nitrate"))
    if mode == 0:
        stem = f"Write the balanced chemical equation for this reaction. Include state symbols.\n\n{word}"
        rows = [row("", f"M1 all formulae correct: {skel}", 1, None, "AO2"),
                row("", f"M2 balancing: {EQ(sym, states=False)}", 1, "M2 dep on M1; ALLOW multiples and fractions", "AO2"),
                row("", f"M3 state symbols: {EQ(sym)}", 1, "M3 independent of balancing if formulae correct", "AO2")]
        mk, d = 3, "7-9" if unfamiliar else "4-6"
    elif mode == 1:
        if all(c == 1 for c, _, _ in L_ + R_):
            return None  # nothing to balance
        stem = f"Balance the equation.\n\n{skel.replace('(s)', '').replace('(l)', '').replace('(g)', '').replace('(aq)', '')}"
        rows = [row("", EQ(sym, states=False), 1, "ALLOW multiples", "AO2")]
        mk, d = 1, "1-3" if len(L_) + len(R_) <= 3 else "4-6"
    else:
        stem = (f"The symbol equation for a reaction is shown.\n\n{EQ(sym, states=False)}\n\n"
                "(i) Write the word equation for this reaction.\n\n(ii) Add state symbols to the equation.")
        st = ", ".join(f"{F(t)}({s})" for side in (L_, R_) for _, t, s in side)
        rows = [row("", f"M1 {word}", 1, "IGNORE state symbols in the word equation", "AO1"),
                row("", f"M2 {st}", 1, "all state symbols needed", "AO2")]
        mk, d = 2, "4-6"
    return Q("Write", d, [P("", stem, mk, lines=3 if mk > 1 else 2)], rows, ["1.25"], ao=["AO2"],
             ans=("atom-count balance check", {"equation": EQ(sym)}))


def _mass_calc(r):
    # reacting masses from equation
    choices = [("CaCO3(s) -> CaO(s) + CO2(g)", "CaCO3", "CaO"), ("2Mg(s) + O2(g) -> 2MgO(s)", "Mg", "MgO"),
               ("CuCO3(s) -> CuO(s) + CO2(g)", "CuCO3", "CuO"), ("Fe2O3(s) + 3CO(g) -> 2Fe(l) + 3CO2(g)", "Fe2O3", "Fe"),
               ("2Al(s) + Fe2O3(s) -> Al2O3(s) + 2Fe(l)", "Fe2O3", "Fe"), ("Zn(s) + 2HCl(aq) -> ZnCl2(aq) + H2(g)", "Zn", "ZnCl2"),
               ("CuO(s) + H2SO4(aq) -> CuSO4(aq) + H2O(l)", "CuO", "CuSO4"), ("2NaHCO3(s) -> Na2CO3(s) + H2O(l) + CO2(g)", "NaHCO3", "Na2CO3"),
               ("4Al(s) + 3O2(g) -> 2Al2O3(s)", "Al", "Al2O3"), ("Mg(s) + 2HCl(aq) -> MgCl2(aq) + H2(g)", "Mg", "MgCl2"),
               ("2KClO3(s) -> 2KCl(s) + 3O2(g)", "KClO3", "O2"), ("CH4(g) + 2O2(g) -> CO2(g) + 2H2O(l)", "CH4", "H2O")]
    return r.choice(choices)


@tpl(FO, "calculation", 60)
def formulae_calcs(r, k):
    import chemistry_util as U
    kind = k % 6
    if kind == 0:  # reacting mass
        eq, a, b = _mass_calc(r)
        L_, R_ = U.eq_terms(eq)
        ca = [c for c, t, _ in L_ + R_ if t == a][0]
        cb = [c for c, t, _ in L_ + R_ if t == b][0]
        ma = r.choice([2.4, 4.8, 6.0, 10.0, 12.5, 25.0, 3.2, 8.0, 16.0, 5.0, 1.2, 50.0])
        na = Fr(str(ma)) / Mr(a)
        nb = na * cb / ca
        mb = nb * Mr(b)
        stem = (f"Calculate the mass of {F(b)} formed from {num(ma)} g of {F(a)}.\n\n{EQ(eq)}\n\n"
                f"[Mr of {F(a)} = {num(Mr(a))}, Mr of {F(b)} = {num(Mr(b))}]\n\nGive your answer to 3 significant figures.")
        rows = [row("", f"M1 moles of {F(a)} = {num(ma)} ÷ {num(Mr(a))} = {num(float(na), sf=3)}", 1, None, "AO2"),
                row("", f"M2 moles of {F(b)} = {num(float(na), sf=3)} × {num(cb)}/{num(ca)} = {num(float(nb), sf=3)}", 1, "ALLOW ecf", "AO2"),
                row("", f"M3 mass = {num(float(nb), sf=3)} × {num(Mr(b))} = {num(float(mb), sf=3)} g", 1,
                    "ALLOW ecf; correct answer without working scores 3", "AO2")]
        return Q("Calculate", "4-6" if ca == cb else "7-9", [P("", stem, 3, space="working", answer_prefix="mass = ", lines=6)],
                 rows, ["1.29", "1.28"], ans=("n=m/Mr, ratio, m=nMr", {"mass": float(num(float(mb), sf=3))}))
    if kind == 1:  # percentage yield
        eq, a, b = _mass_calc(r)
        L_, R_ = U.eq_terms(eq)
        ca = [c for c, t, _ in L_ + R_ if t == a][0]
        cb = [c for c, t, _ in L_ + R_ if t == b][0]
        ma = r.choice([5.0, 10.0, 20.0, 4.0, 8.0, 12.0, 2.5])
        th = Fr(str(ma)) / Mr(a) * cb / ca * Mr(b)
        frac = Fr(r.choice(range(55, 96, 3)), 100)
        actual = Fr(num(float(th * frac), sf=3))
        y = actual / th * 100
        stem = (f"A student heats/reacts {num(ma)} g of {F(a)} and obtains {num(actual)} g of {F(b)}.\n\n{EQ(eq)}\n\n"
                f"The theoretical (maximum) yield of {F(b)} is {num(float(th), sf=3)} g.\n\nCalculate the percentage yield. "
                "Give your answer to 3 significant figures.")
        if r.random() < 0.5:
            stem = (f"In a reaction, {num(ma)} g of {F(a)} produced {num(actual)} g of {F(b)}.\n\n{EQ(eq)}\n\n"
                    f"[Mr of {F(a)} = {num(Mr(a))}, Mr of {F(b)} = {num(Mr(b))}]\n\n"
                    "(i) Calculate the maximum (theoretical) mass of product.\n\n(ii) Calculate the percentage yield. Give your answer to 3 significant figures.")
            rows = [row("", f"M1 moles {F(a)} = {num(ma)} ÷ {num(Mr(a))}", 1, None, "AO2"),
                    row("", f"M2 theoretical mass = {num(float(th), sf=3)} g", 1, "ALLOW ecf", "AO2"),
                    row("", f"M3 {num(actual)} ÷ {num(float(th), sf=3)} × 100", 1, "ALLOW ecf", "AO2"),
                    row("", f"M4 {num(float(y), sf=3)} %", 1, None, "AO2")]
            return Q("Calculate", "7-9", [P("", stem, 4, space="working", lines=8)], rows, ["1.30", "1.29"],
                     ans=("yield", {"theoretical": float(num(float(th), sf=3)), "yield": float(num(float(y), sf=3))}))
        rows = [row("", f"M1 {num(actual)} ÷ {num(float(th), sf=3)} × 100", 1, None, "AO2"),
                row("", f"M2 {num(float(y), sf=3)} (%)", 1, "Correct answer without working scores 2", "AO2")]
        return Q("Calculate", "1-3", [P("", stem, 2, space="working", answer_prefix="percentage yield = ", lines=4)], rows, ["1.30"],
                 ans=("actual/theoretical×100", {"yield": float(num(float(y), sf=3))}))
    if kind == 2:  # empirical formula
        cases = [({"C": 1, "H": 4}, 1), ({"C": 1, "H": 2}, r.choice([2, 3, 4])), ({"C": 2, "H": 5}, 2), ({"Fe": 2, "O": 3}, 1),
                 ({"Mg": 1, "O": 1}, 1), ({"C": 1, "H": 2, "O": 1}, r.choice([1, 2, 6])), ({"N": 1, "O": 2}, r.choice([1, 2])),
                 ({"Cu": 2, "O": 1}, 1), ({"Al": 2, "O": 3}, 1), ({"C": 3, "H": 8}, 1), ({"P": 2, "O": 5}, 2), ({"C": 1, "H": 1}, r.choice([2, 6])),
                 ({"Na": 2, "S": 1, "O": 4}, 1), ({"Ca": 1, "Cl": 2}, 1), ({"Pb": 3, "O": 4}, 1), ({"S": 1, "O": 3}, 1)]
        emp, mult = r.choice(cases)
        tot = sum(AR(e) * n for e, n in emp.items())
        pct = {e: AR(e) * n / tot * 100 for e, n in emp.items()}
        pct_s = {e: num(float(v), dp=1) for e, v in pct.items()}
        # recompute with rounded percentages
        ratios = {e: Fr(pct_s[e]) / AR(e) for e in emp}
        mn = min(ratios.values())
        simp = {e: float(v / mn) for e, v in ratios.items()}
        ok = all(abs(simp[e] - emp[e] / min(emp.values())) < 0.05 for e in emp)
        if not ok or any(abs(v - round(v)) > 0.06 for v in simp.values()):
            return None
        ef = "".join(e + (str(n) if n > 1 else "") for e, n in emp.items())
        if "C" in emp and "H" in emp:
            ef = "".join(e + (str(emp[e]) if emp[e] > 1 else "") for e in sorted(emp, key=lambda x: "CHO".index(x) if x in "CHO" else 9))
        mf = "".join(e + (str(n * mult) if n * mult > 1 else "") for e, n in (sorted(emp.items(), key=lambda x: "CHO".index(x[0]) if x[0] in "CHO" else 9)))
        desc = ", ".join(f"{EL[e][2]} {pct_s[e]} %" for e in emp)
        stem = f"A compound contains, by mass: {desc}.\n\nCalculate the empirical formula of the compound."
        rows = [row("", "M1 divide each % by Ar: " + ", ".join(f"{pct_s[e]} ÷ {num(AR(e))} = {num(float(ratios[e]), sf=3)}" for e in emp), 1, None, "AO2"),
                row("", "M2 divide by smallest: " + " : ".join(num(round(v, 2)) for v in simp.values()), 1, "ALLOW ecf", "AO2"),
                row("", f"M3 {F(ef)}", 1, "No ecf for M3 if ratio not whole numbers; correct formula with no working scores 1", "AO2")]
        parts = [P("a" if mult > 1 else "", stem, 3, space="working", answer_prefix="empirical formula = ", lines=6)]
        values = {"empirical": ef}
        if mult > 1:
            mrm = Mr(mf)
            parts.append(P("b", f"The relative formula mass of the compound is {num(mrm)}. Deduce its molecular formula.", 2,
                           space="working", answer_prefix="molecular formula = ", lines=3))
            rows = [dict(x, part="a") for x in rows]
            rows += [row("b", f"M1 {num(mrm)} ÷ {num(tot)} = {mult}", 1, "ALLOW ecf from (a)", "AO2"), row("b", f"M2 {F(mf)}", 1, None, "AO2")]
            values["molecular"] = mf
        return Q("Calculate", "7-9" if mult > 1 else "4-6", parts, rows, ["1.33", "1.32"], ans=("mole ratio", values))
    if kind == 3:  # water of crystallisation
        salts = [("CuSO4", 5), ("MgSO4", 7), ("Na2CO3", 10), ("BaCl2", 2), ("FeSO4", 7), ("ZnSO4", 7), ("CoCl2", 6), ("Na2SO4", 10), ("CaCl2", 6)]
        s, x = r.choice(salts)
        mhyd = r.choice([2.50, 5.00, 3.00, 4.00, 6.00, 7.50, 10.0])
        manh = Fr(str(mhyd)) * Mr(s) / (Mr(s) + x * 18)
        manh_r = Fr(num(float(manh), dp=2))
        mw = Fr(str(mhyd)) - manh_r
        ns = manh_r / Mr(s)
        nw = mw / 18
        xv = nw / ns
        if abs(float(xv) - x) > 0.15:
            return None
        stem = (f"A student heats {num(mhyd, dp=2)} g of hydrated {F(s)} crystals, {F(s)}·xH₂O, until all the water of crystallisation "
                f"is removed. The mass of anhydrous {F(s)} left is {num(float(manh_r), dp=2)} g.\n\n"
                f"Calculate the value of x. [Mr of {F(s)} = {num(Mr(s))}, Mr of H₂O = 18]")
        rows = [row("", f"M1 mass of water = {num(mhyd, dp=2)} − {num(float(manh_r), dp=2)} = {num(float(mw), dp=2)} g", 1, None, "AO2"),
                row("", f"M2 moles of {F(s)} = {num(float(manh_r), dp=2)} ÷ {num(Mr(s))} = {num(float(ns), sf=3)}", 1, None, "AO2"),
                row("", f"M3 moles of water = {num(float(mw), dp=2)} ÷ 18 = {num(float(nw), sf=3)}", 1, None, "AO2"),
                row("", f"M4 x = {x}", 1, "ALLOW ecf; must be a whole number", "AO2")]
        return Q("Calculate", "7-9", [P("", stem, 4, space="working", answer_prefix="x = ", lines=8)], rows, ["1.31", "1.28"],
                 ans=("mole ratio water:salt", {"x": x}))
    if kind == 4:  # concentration (C)
        acid = r.choice([("NaOH", "sodium hydroxide"), ("HCl", "hydrochloric acid"), ("KOH", "potassium hydroxide"), ("NaCl", "sodium chloride"),
                         ("CuSO4", "copper(II) sulfate"), ("H2SO4", "sulfuric acid"), ("Na2CO3", "sodium carbonate")])
        sub = r.choice(["mass", "mol", "vol"])
        f, nm = acid
        v = r.choice([25.0, 50.0, 100.0, 200.0, 250.0, 500.0])
        c = r.choice([Fr(1, 10), Fr(1, 5), Fr(1, 2), Fr(1, 4), Fr(2), Fr(1, 20), Fr(3, 2)])
        n = c * Fr(str(v)) / 1000
        if sub == "mol":
            stem = f"Calculate the amount, in moles, of {nm} in {num(v)} cm³ of a {num(float(c))} mol/dm³ solution."
            rows = [row("", f"M1 {num(v)} ÷ 1000 = {num(v / 1000)} dm³", 1, None, "AO2"),
                    row("", f"M2 {num(float(c))} × {num(v / 1000)} = {num(float(n), sf=3)} mol", 1, None, "AO2")]
            return Q("Calculate", "4-6", [P("", stem, 2, space="working", answer_prefix="amount = ", lines=4)], rows, ["1.34C"],
                     ans=("n=cV", {"mol": float(n)}))
        if sub == "mass":
            m = n * Mr(f)
            stem = (f"A student dissolves {num(float(m), sf=3)} g of {nm}, {F(f)}, in water and makes the solution up to {num(v)} cm³.\n\n"
                    f"Calculate the concentration of the solution in mol/dm³. [Mr of {F(f)} = {num(Mr(f))}]")
            if f in ("HCl", "H2SO4"):
                return None
            rows = [row("", f"M1 moles = {num(float(m), sf=3)} ÷ {num(Mr(f))} = {num(float(n), sf=3)}", 1, None, "AO2"),
                    row("", f"M2 volume = {num(v / 1000)} dm³", 1, None, "AO2"),
                    row("", f"M3 concentration = {num(float(c), sf=3)} mol/dm³", 1, "ALLOW ecf", "AO2")]
            return Q("Calculate", "7-9", [P("", stem, 3, space="working", answer_prefix="concentration = ", lines=6)], rows, ["1.34C", "1.28"],
                     ans=("c=n/V", {"conc": float(c)}))
        stem = (f"Calculate the volume, in cm³, of {num(float(c))} mol/dm³ {nm} that contains {num(float(n), sf=3)} mol of {F(f)}.")
        rows = [row("", f"M1 {num(float(n), sf=3)} ÷ {num(float(c))} = {num(float(n / c), sf=3)} dm³", 1, None, "AO2"),
                row("", f"M2 {num(v)} cm³", 1, "ALLOW ecf for ×1000", "AO2")]
        return Q("Calculate", "4-6", [P("", stem, 2, space="working", answer_prefix="volume = ", lines=4)], rows, ["1.34C"],
                 ans=("V=n/c", {"vol_cm3": v}))
    # kind 5: gas volumes (C)
    eqs = [("Mg(s) + 2HCl(aq) -> MgCl2(aq) + H2(g)", "Mg", "H2"), ("CaCO3(s) + 2HCl(aq) -> CaCl2(aq) + H2O(l) + CO2(g)", "CaCO3", "CO2"),
           ("Zn(s) + H2SO4(aq) -> ZnSO4(aq) + H2(g)", "Zn", "H2"), ("2H2O2(aq) -> 2H2O(l) + O2(g)", "H2O2", "O2"),
           ("CuCO3(s) -> CuO(s) + CO2(g)", "CuCO3", "CO2"), ("2KClO3(s) -> 2KCl(s) + 3O2(g)", "KClO3", "O2"),
           ("Na2CO3(s) + 2HCl(aq) -> 2NaCl(aq) + H2O(l) + CO2(g)", "Na2CO3", "CO2"), ("2Na(s) + 2H2O(l) -> 2NaOH(aq) + H2(g)", "Na", "H2")]
    eq, a, g = r.choice(eqs)
    L_, R_ = U.eq_terms(eq)
    ca = [c for c, t, _ in L_ if t == a][0]
    cg = [c for c, t, _ in R_ if t == g][0]
    ma = r.choice([0.12, 0.24, 0.48, 1.00, 2.00, 0.36, 0.65, 1.30, 0.50, 2.50, 0.69, 0.46])
    n = Fr(str(ma)) / Mr(a) * cg / ca
    vol = n * 24000
    units = r.choice(["cm³", "dm³"])
    vv = vol if units == "cm³" else vol / 1000
    stem = (f"Calculate the volume of {F(g)}, in {units}, produced at room temperature and pressure (rtp) when {num(ma)} g of {F(a)} "
            f"reacts completely.\n\n{EQ(eq)}\n\n[Mr of {F(a)} = {num(Mr(a))}; one mole of any gas occupies 24 dm³ at rtp]\n\n"
            "Give your answer to 3 significant figures.")
    rows = [row("", f"M1 moles of {F(a)} = {num(ma)} ÷ {num(Mr(a))} = {num(float(Fr(str(ma)) / Mr(a)), sf=3)}", 1, None, "AO2"),
            row("", f"M2 moles of {F(g)} = {num(float(n), sf=3)}", 1, "ALLOW ecf", "AO2"),
            row("", f"M3 volume = {num(float(n), sf=3)} × {24000 if units == 'cm³' else 24} = {num(float(vv), sf=3)} {units}", 1,
                "ALLOW ecf; penalise wrong unit conversion once", "AO2")]
    return Q("Calculate", "7-9" if ca != cg else "4-6", [P("", stem, 3, space="working", answer_prefix="volume = ", lines=6)], rows,
             ["1.35C", "1.28"], ans=("n × 24", {"volume": float(num(float(vv), sf=3)), "units": units}))


items(FO, "practical", "1.36", [
    D(intro="A student heats a known mass of magnesium ribbon in a crucible with a lid to find the formula of magnesium oxide.",
      s="Explain why the lid is lifted from time to time during heating.", m=2,
      p=["to let oxygen / air in (so all the magnesium reacts)", "while keeping the magnesium oxide smoke / solid in the crucible"], d="4-6"),
    D(intro="A student heats a known mass of magnesium ribbon in a crucible with a lid to find the formula of magnesium oxide.",
      s="State how the student knows that all the magnesium has reacted.", m=1,
      p=["the mass stops changing / constant mass on repeated heating"], d="4-6"),
    D(s="Give two reasons why the mass of magnesium oxide obtained may be less than expected.", m=2,
      p=["some magnesium oxide (smoke) escapes", "not all the magnesium has reacted / lid not lifted enough", "magnesium reacted with nitrogen"], any=True, d="7-9"),
    D(intro="Copper(II) oxide can be reduced to copper by heating it in a stream of hydrogen or methane gas in a combustion tube.",
      s="Give two safety precautions needed in this experiment.", m=2,
      p=["burn off the excess gas at the end of the tube", "make sure air is flushed out before lighting / heating (to avoid explosion)",
         "wear eye protection", "keep gas flowing while the copper cools"], any=True, d="4-6"),
    D(intro="Copper(II) oxide can be reduced to copper by heating it in a stream of hydrogen or methane gas in a combustion tube.",
      s="Explain why the gas is kept flowing while the copper cools down.", m=2,
      p=["stops air / oxygen getting in", "so hot copper is not re-oxidised to copper(II) oxide"], d="7-9"),
    D(s="Describe how a student could find the mass of water in a sample of hydrated copper(II) sulfate crystals.", m=3,
      p=["weigh an empty crucible / evaporating basin and then with crystals", "heat until the blue crystals turn white / constant mass",
         "reweigh; loss in mass = mass of water"], ref="1.31", d="4-6"),
    D(s="Explain why the crucible is weighed after cooling and not while hot.", m=2,
      p=["hot objects cause air currents that make the balance reading inaccurate", "(and) anhydrous salt may absorb water if left — so cool in a desiccator / quickly"], ref="1.31", d="7-9"),
    D(s="Suggest why the magnesium ribbon is cleaned with sandpaper before the experiment.", m=1,
      p=["to remove the oxide layer (so the mass measured is magnesium only)"], d="4-6"),
    D(s="Suggest why a pipe-clay triangle is used to support the crucible when heating.", m=1,
      p=["it holds the crucible securely / can withstand high temperature"], d="1-3"),
    D(s="State the measurements needed to find the empirical formula of a metal oxide by burning the metal.", m=3,
      p=["mass of empty crucible (and lid)", "mass of crucible + metal before heating", "mass of crucible + oxide after heating (to constant mass)"], d="4-6"),
    D(s="Explain why heating to constant mass improves the accuracy of a water of crystallisation experiment.", m=2,
      p=["ensures all the water has been driven off", "so the mass of water calculated is not too small"], ref="1.31", d="7-9"),
    D(s="A student heats hydrated copper(II) sulfate too strongly and the powder turns black. Explain how this affects the value of x calculated.", m=2,
      p=["copper(II) sulfate has decomposed (lost extra mass)", "so the mass loss is too large and x is too high"], ref="1.31", d="7-9"),
])


@tpl(FO, "data", 14)
def formulae_mgo_data(r, k):
    pairs = [("magnesium", "Mg", "MgO"), ("calcium", "Ca", "CaO"), ("zinc", "Zn", "ZnO"), ("copper", "Cu", "CuO"), ("iron", "Fe", "Fe2O3")]
    nm, m, ox = pairs[k % len(pairs)]
    at = __import__("chemistry_util").atoms(ox)
    ratio = AR("O") * at["O"] / (AR(m) * at[m])
    masses = sorted(r.sample([0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50], 5))
    bad = r.randrange(5)
    data = []
    for i, mm in enumerate(masses):
        mo = float(Fr(str(mm)) * ratio)
        if i == bad:
            mo *= 0.75
        data.append((mm, round(mo, 3)))
    tb = table(["Mass of metal in g"] + [num(x) for x, _ in data], [["Mass of oxygen combined in g"] + [f"{y:.3f}" for _, y in data]])
    parts = [P("a", "Plot the results on the grid and draw a straight line of best fit through the origin.", 3, space="graph"),
             P("b", "Identify the anomalous result and suggest a reason for it.", 2, lines=3),
             P("c", f"Use the mass of oxygen that combines with {num(masses[(bad + 2) % 5])} g of {nm} to calculate the empirical formula of the oxide. "
                    f"Show your working.", 3, space="working", answer_prefix="formula = ", lines=6)]
    good = data[(bad + 2) % 5]
    nmet = Fr(str(good[0])) / AR(m)
    nO = Fr(str(good[1])) / 16
    rows = [row("a", "M1 sensible scales, axes labelled\nM2 points correctly plotted\nM3 straight line through origin ignoring the anomaly", 3, None, "AO3"),
            row("b", f"M1 the result for {num(data[bad][0])} g (oxygen too low)", 1, None, "AO3"),
            row("b", "M2 metal did not all react / oxide smoke escaped", 1, "ALLOW lid not lifted / not heated to constant mass", "AO3"),
            row("c", f"M1 moles {m} = {num(good[0])} ÷ {num(AR(m))} = {num(float(nmet), sf=3)}", 1, None, "AO2"),
            row("c", f"M2 moles O = {good[1]:.3f} ÷ 16 = {num(float(nO), sf=3)}", 1, None, "AO2"),
            row("c", f"M3 ratio {num(float(nmet / min(nmet, nO)), sf=2)} : {num(float(nO / min(nmet, nO)), sf=2)} so {F(ox)}", 1, None, "AO2")]
    return Q("Plot", "7-9", parts, rows, ["1.36", "1.33"], figs=[tb],
             intro=f"Students heat different masses of {nm} in air and find the mass of oxygen that combines in each case.",
             ans=("ratio", {"formula": ox, "anomaly": data[bad][0]}), ao=["AO3", "AO2"])


# =================================================================== 1(f) ionic bonding
CAT = {"Na": ("sodium", 1), "K": ("potassium", 1), "Li": ("lithium", 1), "Mg": ("magnesium", 2), "Ca": ("calcium", 2),
       "Al": ("aluminium", 3), "Ag": ("silver", 1), "Cu": ("copper(II)", 2), "Fe2": ("iron(II)", 2), "Fe3": ("iron(III)", 3),
       "Pb": ("lead(II)", 2), "Zn": ("zinc", 2), "NH4": ("ammonium", 1), "H": ("hydrogen", 1), "Ba": ("barium", 2)}
AN = {"Cl": ("chloride", 1), "Br": ("bromide", 1), "I": ("iodide", 1), "F": ("fluoride", 1), "O": ("oxide", 2), "S": ("sulfide", 2),
      "N": ("nitride", 3), "OH": ("hydroxide", 1), "NO3": ("nitrate", 1), "SO4": ("sulfate", 2), "CO3": ("carbonate", 2)}


def ion_formula(c, a):
    qc, qa = CAT[c][1], AN[a][1]
    from math import gcd
    g = gcd(qc, qa)
    nc, na = qa // g, qc // g
    cs = "Fe" if c.startswith("Fe") else c
    cpart = (f"({cs}){nc}" if len(cs) > 2 and nc > 1 else f"{cs}{nc if nc > 1 else ''}")
    apoly = len(a) > 2 or a in ("OH",)
    apart = (f"({a}){na}" if apoly and na > 1 else f"{a}{na if na > 1 else ''}")
    return cpart + apart


def ion_sym(sym, q, neg=False):
    s = "Fe" if sym.startswith("Fe") else sym
    return F(f"{s}^{q if q > 1 else ''}{'-' if neg else '+'}")


PAIRS = [(c, a) for c in CAT for a in AN if not (c == "H" and a in ("O", "S", "N", "OH")) and not (c == "NH4" and a in ("O", "S", "N", "OH"))
         and not (a == "N" and c not in ("Mg", "Li", "Ca", "Al"))]


@tpl(IO, "mcq", 16)
def ionic_formula_mcq(r, k):
    c, a = PAIRS[(k * 11) % len(PAIRS)]
    f = ion_formula(c, a)
    nm = f"{CAT[c][0]} {AN[a][0]}"
    alts = set()
    for c2 in [ion_formula(c, a2) for a2 in AN if AN[a2][1] != AN[a][1]][:2] + [f.replace("2", "3") if "2" in f else f + "2", f.replace(")", "")]:
        pass
    qc, qa = CAT[c][1], AN[a][1]
    cs = "Fe" if c.startswith("Fe") else c
    cand = [f"{cs}{a}", f"{cs}{qc if qc > 1 else ''}{a}{qa if qa > 1 else ''}", f"{cs}{qa if qa > 1 else ''}{a}{qc if qc > 1 else ''}",
            f"{cs}2{a}", f"{cs}{a}2", f"{cs}{a}3", f"{cs}3{a}2"]
    if len(a) > 2 or a == "OH":
        cand += [f"{cs}({a})2", f"{cs}{a}2" if a != "OH" else f"{cs}O2H2"]
    if len(cs) > 2:
        cand += [f"({cs})2{a}", f"{cs}{a}"]
    wrong = [F(x) for x in dict.fromkeys(cand) if Mr(x) != Mr(f)]
    if len(wrong) < 3:
        return None
    part, rw = mcq(r, f"What is the formula of {nm}?", F(f), wrong)
    part["label"] = ""
    return Q("What", "4-6" if (len(a) > 2 or qc != qa) else "1-3", [part], [rw], ["1.39", "1.38"], style="mcq",
             ans=("charge balance", {"formula": f}), ao=["AO2"])


@tpl(IO, "recall", 16)
def ionic_formula_recall(r, k):
    ps = r.sample(PAIRS, 3)
    parts, rows = [], []
    for i, (c, a) in enumerate(ps):
        nm = f"{CAT[c][0]} {AN[a][0]}"
        parts.append(P("abc"[i], f"Give the formula of {nm}.", 1, lines=1))
        rows.append(row("abc"[i], F(ion_formula(c, a)), 1, "Penalise incorrect case / missing brackets", "AO1"))
    c, a = r.choice(ps)
    parts.append(P("d", f"Give the formula, including charge, of the {AN[a][0]} ion.", 1, lines=1))
    an_q = AN[a][1]
    rows.append(row("d", ion_sym(a, an_q, True), 1, None, "AO1"))
    return Q("Give", "4-6", parts, rows, ["1.38", "1.39"], intro="This question is about the formulae of ionic compounds.",
             ans=("charge balance", {"formulae": [ion_formula(c_, a_) for c_, a_ in ps]}), ao=["AO1"])


SIMPLE_IONIC = [(m, n) for m in ("Na", "K", "Li", "Mg", "Ca", "Al") for n in ("Cl", "F", "O", "S", "Br", "N")
                if not (n == "N" and m not in ("Li", "Mg", "Ca", "Al"))]


@tpl(IO, "describe", 24)
def ionic_describe_formation(r, k):
    m, n = SIMPLE_IONIC[k % len(SIMPLE_IONIC)]
    qm, qn = CAT[m][1], AN[n][1]
    from math import gcd
    g = gcd(qm, qn)
    nm_, nn = qn // g, qm // g
    f = ion_formula(m, n)
    comp = f"{CAT[m][0]} {AN[n][0]}"
    if (k // len(SIMPLE_IONIC)) % 2 == 0:
        stem = f"Describe, in terms of electrons, how {comp} is formed from atoms of {CAT[m][0]} and {EL[n][2]}."
        rows = [row("", f"M1 each {CAT[m][0]} atom loses {qm} electron(s)", 1, None, "AO1"),
                row("", f"M2 each {EL[n][2]} atom gains {qn} electron(s)", 1, None, "AO1"),
                row("", f"M3 electrons transferred from {CAT[m][0]} to {EL[n][2]} ({nm_} {CAT[m][0]} : {nn} {EL[n][2]})", 1,
                    "ALLOW correct ratio of atoms" if (nm_, nn) != (1, 1) else "ALLOW transfer stated", "AO2"),
                row("", f"M4 forming {ion_sym(m, qm)} and {ion_sym(n, qn, True)} ions (with full outer shells)", 1,
                    "REJECT reference to sharing / covalent bonds for whole question", "AO1")]
        return Q("Describe", "4-6" if nm_ == nn else "7-9", [P("", stem, 4, lines=9)], rows, ["1.37", "1.40"],
                 ans=("electron transfer", {"formula": f, "cation": ion_sym(m, qm), "anion": ion_sym(n, qn, True)}), ao=["AO1", "AO2"])
    stem = (f"Draw a dot-and-cross diagram to show the ions in {comp}, {F(f)}.\n\nShow outer electrons only and the charges on the ions.")
    rows = [row("", f"M1 {nm_} {CAT[m][0]} ion(s) with no outer electrons shown (or full shell of 8 crosses)", 1, None, "AO2"),
            row("", f"M2 {nn} {EL[n][2]} ion(s) with 8 outer electrons, {qn if nm_ * qm == qn * nn else qn} of them shown as crosses (from the metal)", 1, None, "AO2"),
            row("", f"M3 charges: {ion_sym(m, qm)} and {ion_sym(n, qn, True)}", 1, "ALLOW square brackets; IGNORE inner shells if correct", "AO2")]
    return Q("Draw", "7-9" if nm_ != nn else "4-6", [P("", stem, 3, space="box")], rows, ["1.40"],
             ans=("electron transfer", {"formula": f}), ao=["AO2"])


facts(IO, "1.41", [
    D(mq="What is an ion?", c="an atom or group of atoms with an electric charge", w=["an atom with extra neutrons", "a neutral molecule", "a type of isotope"], ref="1.37"),
    D(mq="What happens when a sodium atom forms a sodium ion?", c="it loses one electron", w=["it gains one electron", "it loses one proton", "it gains one proton"], ref="1.37"),
    D(mq="What is the charge on an ion of an element in Group 6?", c="2−", w=["2+", "6+", "6−"], ref="1.38"),
    D(mq="What holds the ions together in sodium chloride?", c="strong electrostatic attraction between oppositely charged ions",
      w=["shared pairs of electrons", "weak forces between molecules", "a sea of delocalised electrons"]),
    D(mq="Why does solid sodium chloride not conduct electricity?", c="its ions cannot move", w=["it has no ions", "its electrons are too tightly held",
      "it is a covalent compound"], ref="1.43", d="4-6"),
    D(mq="Which compound has a giant ionic lattice?", c="magnesium oxide", w=["carbon dioxide", "methane", "water"], ref="1.42"),
    D(mq="What is the formula of the ammonium ion?", c="NH4^+", w=["NH3^+", "NH4^-", "NH^4+"], ref="1.38"),
    D(mq="What is the formula of the sulfate ion?", c="SO4^2-", w=["SO3^2-", "SO4^-", "S^2-"], ref="1.38"),
    D(mq="When is sodium chloride able to conduct electricity?", c="when molten or dissolved in water", w=["only when solid", "never",
      "only when it is a powder"], ref="1.43"),
    D(mq="Why does magnesium oxide have a higher melting point than sodium chloride?", c="its ions have higher charges so attractions are stronger",
      w=["it has covalent bonds", "it has more delocalised electrons", "its ions are larger"], ref="1.42", d="7-9"),
    D(mq="What is the formula of the ion formed by aluminium?", c="Al^3+", w=["Al^3-", "Al^+", "Al^2+"], ref="1.38"),
    D(mq="Which pair of elements would form an ionic compound?", c="potassium and bromine", w=["carbon and oxygen", "hydrogen and chlorine", "nitrogen and hydrogen"], ref="1.37"),
])

items(IO, "explain", "1.42", [
    D(s="Explain why {c} has a high melting point.", m=3,
      p=["giant (ionic) lattice / structure", "strong electrostatic attraction between oppositely charged ions", "lots of energy needed to overcome these attractions"],
      v=[{"c": "sodium chloride"}, {"c": "magnesium oxide"}, {"c": "calcium fluoride"}, {"c": "potassium bromide"}],
      n="REJECT intermolecular forces / covalent bonds / molecules for M2 and M3"),
    D(s="Explain why solid {c} does not conduct electricity but molten {c} does.", m=2,
      p=["in the solid the ions are fixed in place / cannot move", "when molten the ions can move (and carry charge)"],
      v=[{"c": "lead(II) bromide"}, {"c": "sodium chloride"}, {"c": "zinc chloride"}], ref="1.43",
      n="REJECT electrons moving for M2"),
    D(s="Explain why magnesium oxide has a much higher melting point than sodium chloride.", m=2,
      p=["Mg²⁺ and O²⁻ ions have larger charges than Na⁺ and Cl⁻", "so the electrostatic attractions are stronger / need more energy to overcome"], d="7-9"),
    D(s="Explain how a calcium atom becomes a calcium ion and why the ion has a 2+ charge.", m=3,
      p=["calcium atom (2.8.8.2) loses two electrons", "to get a full outer shell (2.8.8)", "now has 20 protons but 18 electrons so charge 2+"], ref="1.37", d="4-6"),
    D(s="Explain why a solution of copper(II) chloride conducts electricity.", m=2,
      p=["contains ions (Cu²⁺ and Cl⁻)", "ions are free to move in the solution"], ref="1.43"),
    D(s="Explain why the ions in a sodium chloride crystal are arranged in a regular pattern.", m=2,
      p=["each ion is surrounded by ions of opposite charge", "attractions in all directions form a regular (giant) lattice"], ref="1.41", d="7-9"),
    D(s="Explain why ionic compounds are usually solids at room temperature.", m=2,
      p=["strong electrostatic forces between ions in a giant lattice", "room temperature does not provide enough energy to overcome them"], ref="1.42"),
    D(s="Explain why an oxide ion has a 2− charge.", m=2,
      p=["an oxygen atom (2.6) gains two electrons", "so it has 8 protons and 10 electrons"], ref="1.37", d="4-6"),
    D(s="Explain why the formula of aluminium oxide is Al₂O₃.", m=2,
      p=["aluminium ions are Al³⁺ and oxide ions are O²⁻", "two Al³⁺ (6+) balance three O²⁻ (6−)"], ref="1.39", d="7-9"),
    D(s="Explain what is meant by ionic bonding.", m=2,
      p=["electrostatic attraction", "between oppositely charged ions"], ref="1.41", d="1-3"),
    D(s="A substance melts at 801 °C and conducts electricity only when molten or in solution. Explain what type of structure it has.", m=2,
      p=["giant ionic (lattice)", "high melting point (strong attractions); ions mobile only when molten / dissolved"], ref="1.43", d="4-6"),
    D(s="Explain why ionic compounds are brittle.", m=2,
      p=["a force shifts layers of ions so like charges line up", "the like charges repel and the crystal splits"], ref="1.41", d="7-9"),
])

# =================================================================== 1(g) covalent
facts(CO, "1.44", [
    D(mq="What is a covalent bond?", c="a shared pair of electrons", w=["a transferred electron", "an attraction between ions", "a sea of delocalised electrons"]),
    D(mq="How many covalent bonds are there in a molecule of ammonia, NH3?", c="3", w=["1", "4", "6"], ref="1.46"),
    D(mq="How many pairs of electrons are shared between the two atoms in a nitrogen molecule?", c="3", w=["1", "2", "6"], ref="1.46", d="4-6"),
    D(mq="Why does methane have a low boiling point?", c="the forces of attraction between its molecules are weak",
      w=["its covalent bonds are weak", "it has a giant structure", "its ions cannot move"], ref="1.47"),
    D(mq="Which substance has a giant covalent structure?", c="silicon dioxide", w=["carbon dioxide", "water", "sodium chloride"], ref="1.49"),
    D(mq="Why does graphite conduct electricity?", c="it has delocalised electrons that can move", w=["it has ions that can move",
      "it is a metal", "its layers can slide"], ref="1.50", d="4-6"),
    D(mq="Why is diamond very hard?", c="each carbon atom forms four strong covalent bonds in a giant structure",
      w=["it has weak forces between layers", "it has delocalised electrons", "it is made of molecules"], ref="1.50"),
    D(mq="What is the formula of buckminsterfullerene?", c="C60", w=["C6", "C12", "C600"], ref="1.50"),
    D(mq="Which statement explains why the boiling points of the halogens increase down the group?",
      c="the intermolecular forces get stronger as the molecules get bigger", w=["the covalent bonds get stronger", "the molecules become ions",
      "the atoms lose electrons more easily"], ref="1.48", d="7-9"),
    D(mq="How many electrons are shared in the double bond in an oxygen molecule?", c="4", w=["2", "6", "8"], ref="1.46", d="4-6"),
    D(mq="Which substance does not conduct electricity when molten?", c="sulfur", w=["sodium chloride", "copper", "lead(II) bromide"], ref="1.51", d="4-6"),
    D(mq="Why is graphite soft and slippery?", c="its layers are held by weak forces and can slide", w=["its covalent bonds are weak",
      "it has free ions", "each atom forms four bonds"], ref="1.50"),
    D(mq="What holds the atoms together in a covalent bond?", c="attraction between the shared electrons and both nuclei",
      w=["attraction between positive and negative ions", "attraction between molecules", "repulsion between nuclei"], ref="1.45", d="7-9"),
])

facts(CO, "1.44", [
    D(q="Hydrogen atoms join to form H2 molecules. State what holds the two atoms together.", a="a covalent bond: a pair of electrons shared between the atoms", n="REJECT transfer of electrons"),
    D(q="Name the type of force that holds molecules of iodine together in the solid.", a="intermolecular forces (of attraction)",
      n="REJECT covalent bonds", ref="1.47"),
    D(q="Give the number of covalent bonds formed by each carbon atom in diamond.", a="4", ref="1.50"),
    D(q="Give the number of covalent bonds formed by each carbon atom in graphite.", a="3", ref="1.50"),
    D(q="Give one use of graphite that depends on its ability to conduct electricity.", a="electrodes / brushes in motors", ref="1.50"),
    D(q="Give one use of diamond that depends on its hardness.", a="cutting tools / drill tips / saw blades", ref="1.50"),
    D(q="State why most covalent substances do not conduct electricity.", a="they have no ions or free/delocalised electrons", ref="1.51"),
    D(q="Name a substance with a giant covalent structure other than a form of carbon.", a="silicon dioxide / silica / sand", ref="1.49"),
    D(q="State the type of structure of carbon dioxide.", a="simple molecular", n="ALLOW simple covalent", ref="1.47"),
    D(q="Give two physical properties of a simple molecular substance.", m=2,
      pts=["low melting point / boiling point", "does not conduct electricity", "often a gas or liquid at room temperature", "soft (if solid)"], ref="1.47"),
    D(q="State how the boiling points of simple molecular substances change as their relative molecular mass increases.", a="they increase", ref="1.48"),
], intro="This question is about covalent substances.")

MOLS = {"H2": ("hydrogen", "M1 one shared pair between the two H atoms", "M2 no other electrons"),
        "Cl2": ("chlorine", "M1 one shared pair between the Cl atoms", "M2 three non-bonding pairs on each Cl"),
        "HCl": ("hydrogen chloride", "M1 one shared pair between H and Cl", "M2 three non-bonding pairs on Cl"),
        "H2O": ("water", "M1 two shared pairs, one between O and each H", "M2 two non-bonding pairs on O"),
        "NH3": ("ammonia", "M1 three shared pairs, one between N and each H", "M2 one non-bonding pair on N"),
        "CH4": ("methane", "M1 four shared pairs between C and each H", "M2 no non-bonding pairs"),
        "CO2": ("carbon dioxide", "M1 two shared pairs between C and each O (double bonds)", "M2 two non-bonding pairs on each O"),
        "O2": ("oxygen", "M1 two shared pairs between the O atoms", "M2 two non-bonding pairs on each O"),
        "N2": ("nitrogen", "M1 three shared pairs between the N atoms", "M2 one non-bonding pair on each N"),
        "C2H4": ("ethene", "M1 two shared pairs between the C atoms", "M2 one shared pair between each C and each of 4 H"),
        "C2H6": ("ethane", "M1 one shared pair between the C atoms", "M2 one shared pair between each C and each of 6 H"),
        "HF": ("hydrogen fluoride", "M1 one shared pair between H and F", "M2 three non-bonding pairs on F"),
        "CH3Cl": ("chloromethane", "M1 one shared pair C–Cl and three C–H", "M2 three non-bonding pairs on Cl"),
        "Br2": ("bromine", "M1 one shared pair between the Br atoms", "M2 three non-bonding pairs on each Br")}


@tpl(CO, "recall", 14)
def covalent_dotcross(r, k):
    f = list(MOLS)[k % len(MOLS)]
    nm, m1, m2 = MOLS[f]
    return Q("Draw", "4-6" if f in ("CO2", "N2", "O2", "C2H4") else "1-3",
             [P("", f"Using dots and crosses, show how the outer-shell electrons are arranged in one {nm} molecule, {F(f)}.", 2, space="box")],
             [row("", m1, 1, "ALLOW any combination of dots and crosses", "AO1"), row("", m2, 1, "M2 dep on M1", "AO1")],
             ["1.46"], ao=["AO1"], ans=("bonding pairs", {"molecule": f}))


items(CO, "explain", "1.47", [
    D(s="Explain why {c} has a low boiling point.", m=2,
      p=["(simple molecular so) weak forces of attraction between molecules", "little energy needed to overcome them"],
      v=[{"c": "methane"}, {"c": "ammonia"}, {"c": "hydrogen chloride"}, {"c": "chlorine"}],
      n="REJECT breaking covalent bonds"),
    D(s="Explain why diamond has a very high melting point.", m=3,
      p=["giant covalent structure", "many strong covalent bonds", "lots of energy needed to break them"], ref="1.49"),
    D(s="Explain why graphite conducts electricity but diamond does not.", m=3,
      p=["in graphite each carbon forms 3 bonds", "leaving one delocalised electron per atom that can move", "in diamond all 4 outer electrons are used in bonds / none free"], ref="1.50", d="7-9"),
    D(s="Explain why graphite is soft and can be used as a lubricant.", m=2,
      p=["layers held together by weak forces", "so layers can slide over each other"], ref="1.50"),
    D(s="Explain why the boiling point of bromine is higher than the boiling point of chlorine.", m=2,
      p=["bromine has a larger relative molecular mass / bigger molecules", "so stronger intermolecular forces need more energy to overcome"], ref="1.48", d="7-9"),
    D(s="Explain why C₆₀ fullerene has a much lower melting point than diamond.", m=3,
      p=["C₆₀ is made of (simple) molecules", "weak intermolecular forces between molecules are overcome on melting",
         "diamond requires strong covalent bonds to be broken"], ref="1.50", d="7-9"),
    D(s="Explain why silicon dioxide is used to make the lining of furnaces.", m=2,
      p=["giant covalent structure with many strong bonds", "so very high melting point"], ref="1.49", d="4-6"),
    D(s="Explain, in terms of electrostatic attraction, how a covalent bond holds two atoms together.", m=2,
      p=["the shared pair of electrons is attracted to both nuclei", "this attraction holds the nuclei together"], ref="1.45", d="7-9"),
    D(s="Explain why water does not conduct electricity well even though it is a liquid.", m=2,
      p=["water is covalent / made of molecules", "no ions or delocalised electrons to carry charge"], ref="1.51", d="4-6"),
    D(s="Explain why the boiling points of the alkanes increase from methane to octane.", m=2,
      p=["molecules get larger / higher Mr", "intermolecular forces stronger so more energy needed"], ref="1.48", d="4-6"),
    D(s="Explain why ice melts at 0 °C but sodium chloride melts at 801 °C.", m=3,
      p=["ice is simple molecular: weak intermolecular forces overcome", "sodium chloride is a giant ionic lattice",
         "strong electrostatic attractions between ions need much more energy"], d="7-9"),
])

STRUCT = [("A", 3550, 4827, "no", "no", "insoluble", "giant covalent"), ("B", -101, -34, "no", "no", "slightly", "simple molecular"),
          ("C", 801, 1413, "no", "yes", "soluble", "giant ionic"), ("D", 1085, 2562, "yes", "yes", "insoluble", "metallic"),
          ("E", 114, 184, "no", "no", "insoluble", "simple molecular"), ("F", 1710, 2230, "no", "no", "insoluble", "giant covalent"),
          ("G", 2852, 3600, "no", "yes", "insoluble", "giant ionic"), ("H", 660, 2519, "yes", "yes", "insoluble", "metallic"),
          ("J", -182, -162, "no", "no", "insoluble", "simple molecular"), ("K", 770, 1420, "no", "yes", "soluble", "giant ionic"),
          ("L", 98, 883, "yes", "yes", "reacts", "metallic"), ("M", 5, 80, "no", "no", "insoluble", "simple molecular")]


@tpl(CO, "data", 16)
def covalent_structure_table(r, k):
    sel = r.sample(STRUCT, 4)
    if len({s[6] for s in sel}) < 3:
        return None
    letters = r.sample(["P", "Q", "R", "S", "T", "W", "X", "Y", "Z"], 4)
    rows_t = [[L_, str(s[1]), str(s[2]), s[3], s[4], s[5]] for L_, s in zip(letters, sel)]
    tb = table(["Substance", "Melting point in °C", "Boiling point in °C", "Conducts when solid?", "Conducts when molten?", "Solubility in water"], rows_t)
    want = r.choice(sorted({s[6] for s in sel}))
    which = [L_ for L_, s in zip(letters, sel) if s[6] == want]
    parts = [P("a", f"Give the letter of a substance that has a {want} structure.", 1, lines=1),
             P("b", "Give the letter of every substance in the table that is a gas at 20 °C, or write 'none'. Explain your answer.", 2, lines=3)]
    gas = [L_ for L_, s in zip(letters, sel) if s[2] < 20]
    rows = [row("a", " or ".join(which), 1, None, "AO3")]
    if gas:
        bps = ", ".join(f"{L_} {s[2]} °C" for L_, s in zip(letters, sel) if L_ in gas)
        rows += [row("b", f"M1 {' and '.join(gas)}" + (" (both needed)" if len(gas) > 1 else ""), 1, "REJECT if any other letter is included", "AO3"),
                 row("b", f"M2 boiling point{'s' if len(gas) > 1 else ''} below 20 °C ({bps})", 1, None, "AO3")]
    else:
        rows += [row("b", "M1 none of them", 1, None, "AO3"), row("b", "M2 all boiling points are above 20 °C", 1, None, "AO3")]
    lab = [(L_, s) for L_, s in zip(letters, sel)]
    L2, s2 = r.choice(lab)
    parts.append(P("c", f"Deduce the type of structure of substance {L2}. Use evidence from the table.", 3, lines=5))
    ev = {"giant covalent": "very high melting point and does not conduct when solid or molten",
          "simple molecular": "low melting/boiling point and does not conduct",
          "giant ionic": "high melting point and conducts only when molten (not solid)",
          "metallic": "conducts when solid (and molten) and has a high/moderate melting point"}[s2[6]]
    rows += [row("c", f"M1 {s2[6]}", 1, None, "AO3"), row("c", "M2 & M3 " + ev, 2, "one mark for each correct piece of evidence", "AO3")]
    return Q("Deduce", "4-6", parts, rows, ["1.47", "1.49", "1.43"], figs=[tb], intro="The table shows some properties of four substances.",
             ans=("lookup", {"structure": s2[6]}), ao=["AO3", "AO2"])


extended(CO, "1.50", [
    D(s="Diamond and graphite are both forms of carbon. Explain, in terms of structure and bonding, why diamond is used in cutting "
        "tools and graphite is used in electrodes.",
      ind=["both are giant covalent structures", "in diamond each carbon atom is bonded to four others", "strong covalent bonds throughout / rigid 3D network so very hard",
           "no free electrons so diamond does not conduct", "in graphite each carbon atom is bonded to three others in layers",
           "one delocalised electron per atom can move through the layers so graphite conducts", "layers held by weak forces (slide) but high melting point because of covalent bonds"]),
    D(s="Explain why {a} is a gas at room temperature but {b} is a solid with a very high melting point, even though both are oxides of Group 4 elements.",
      ind=["{a} is simple molecular", "each molecule has strong covalent bonds within it", "but weak intermolecular forces between molecules",
           "little energy needed to separate molecules so low boiling point", "{b} has a giant covalent structure",
           "every atom joined by strong covalent bonds in a 3D network", "lots of energy needed to break many bonds so very high melting point"],
      v=[{"a": "carbon dioxide", "b": "silicon dioxide"}], d="7-9"),
    D(s="Compare the structures of diamond and C₆₀ fullerene and explain how their structures affect their melting points and hardness.",
      ind=["diamond: giant covalent, each C bonded to 4 others", "very many strong covalent bonds must be broken so very high melting point",
           "rigid network so very hard", "C₆₀: simple molecules of 60 carbon atoms (spheres)", "strong covalent bonds within each molecule",
           "weak intermolecular forces between molecules so relatively low melting point / sublimes", "C₆₀ is soft / slippery as molecules can move past each other"]),
    D(s="Sodium chloride melts at 801 °C and hydrogen chloride boils at −85 °C. Explain this difference in terms of structure and bonding.",
      ind=["sodium chloride is a giant ionic lattice", "Na⁺ and Cl⁻ held by strong electrostatic attraction in all directions",
           "much energy needed to overcome these attractions", "hydrogen chloride is made of simple molecules", "H–Cl covalent bond is strong but is not broken on boiling",
           "intermolecular forces are weak", "little energy needed so very low boiling point"], d="7-9"),
    D(intro="The table shows the boiling points of four halogens.",
      figs=[table(["Halogen", "Relative molecular mass", "Boiling point in °C"], [["fluorine", "38", "−188"], ["chlorine", "71", "−34"],
                                                                               ["bromine", "160", "59"], ["iodine", "254", "184"]])],
      s="Describe the trend in boiling points and explain it in terms of structure and bonding. Use the data in your answer.",
      ind=["boiling point increases down the group / as Mr increases", "e.g. fluorine −188 °C to iodine 184 °C", "halogens are simple molecular (diatomic molecules)",
           "covalent bond within each molecule (not broken on boiling)", "weak intermolecular forces between molecules",
           "intermolecular forces stronger for larger molecules / higher Mr", "so more energy needed to separate the molecules"], ref="1.48", d="4-6"),
    D(s="Explain why graphite can be used both as a lubricant and as an electrode, but diamond can be used for neither.",
      ind=["graphite: layers of carbon atoms in hexagons", "each carbon bonded to 3 others", "weak forces between layers so layers slide: lubricant",
           "one delocalised electron per carbon free to move: conducts so electrode", "high melting point so withstands heat in electrolysis",
           "diamond: each carbon bonded to 4 others in rigid network", "no free electrons so non-conductor; does not slide"]),
    D(s="Methane, CH₄, and ammonia, NH₃, are both simple molecular substances. Describe the bonding within the molecules and explain why both are gases at room temperature.",
      ind=["covalent bonds = shared pairs of electrons", "methane: four C–H shared pairs; no lone pairs on C",
           "ammonia: three N–H shared pairs; one lone pair on N", "bonds held by attraction of nuclei to shared electrons",
           "weak intermolecular forces between molecules", "little energy needed to overcome so low boiling points", "below room temperature so gases"], ref=["1.46", "1.47"], d="4-6"),
    D(intro="Substance X melts at 1610 °C, is insoluble in water and does not conduct electricity when solid or molten. Substance Y melts at 113 °C, "
            "is insoluble in water and does not conduct electricity when solid or molten.",
      s="Deduce the type of structure of X and of Y. Explain how their structures account for these properties.",
      ind=["X is giant covalent", "high melting point because many strong covalent bonds must be broken", "no ions or delocalised electrons so does not conduct",
           "Y is simple molecular", "low melting point: weak intermolecular forces", "no ions or free electrons so does not conduct", "neither dissolves as they do not form ions in water"], ref=["1.47", "1.49", "1.51"]),
    D(s="Explain why the melting points of simple molecular substances are generally low and why they increase as the size of the molecules increases. Use examples in your answer.",
      ind=["molecules held together by weak intermolecular forces", "covalent bonds inside molecules are not broken on melting", "little energy needed so low melting points",
           "larger molecules (higher Mr) have stronger intermolecular forces", "more energy needed so higher melting/boiling points",
           "example: methane gas, octane liquid, wax solid / chlorine gas, bromine liquid, iodine solid"], ref=["1.47", "1.48"], d="4-6"),
    D(s="Explain why poly(ethene) and diamond, which both contain only covalent bonds, have very different melting points.",
      ind=["diamond is giant covalent: every atom covalently bonded in a network", "melting requires breaking many strong covalent bonds: very high melting point",
           "poly(ethene) is made of long-chain molecules", "covalent bonds within chains", "only intermolecular forces between chains",
           "these are weaker (though stronger than in small molecules) so it softens at low temperature"], ref=["1.47", "1.49"], d="7-9"),
    D(s="Explain, using ideas about electrons, why graphite conducts electricity but iodine does not.",
      ind=["graphite: giant covalent layers", "each carbon atom uses only three outer electrons in bonding", "fourth electron delocalised", "delocalised electrons move through the layers carrying charge",
           "iodine: simple diatomic molecules", "all outer electrons are in bonds or lone pairs (localised)", "no ions or free electrons so no conduction"], ref=["1.50", "1.51"], d="7-9"),
    D(s="Compare the properties of a substance with a giant covalent structure and one with a simple molecular structure, and explain the differences.",
      ind=["giant covalent: very high melting/boiling point", "many strong covalent bonds to break", "usually hard", "simple molecular: low melting/boiling point",
           "weak intermolecular forces", "often gases or liquids", "neither usually conducts (no ions/free electrons) – graphite exception"], ref=["1.47", "1.49"], d="4-6"),
])

# =================================================================== 1(h) metallic (C)
facts(ME, "1.53C", [
    D(mq="What is metallic bonding?", c="attraction between positive metal ions and delocalised electrons",
      w=["attraction between positive and negative ions", "a shared pair of electrons", "weak forces between molecules"]),
    D(mq="Why can metals conduct electricity?", c="delocalised electrons can move through the structure", w=["positive ions can move", "they contain molecules",
      "the atoms share electron pairs"], ref="1.54C"),
    D(mq="Why are metals malleable?", c="layers of ions can slide over each other", w=["their electrons are fixed in place", "they have weak bonds",
      "they contain ions that repel"], ref="1.54C"),
    D(mq="In a metal lattice, what are the particles with a positive charge?", c="metal ions", w=["protons only", "delocalised electrons", "neutrons"], ref="1.52C"),
    D(mq="Which property of copper makes it suitable for electrical wiring?", c="it is a good electrical conductor", w=["it is very hard", "it has a low density", "it is magnetic"], ref="1.54C"),
    D(mq="Why do most metals have high melting points?", c="the attraction between ions and delocalised electrons is strong",
      w=["the forces between molecules are strong", "metals contain covalent bonds", "electrons are fixed between atoms"], d="4-6"),
    D(mq="Why does magnesium form Mg²⁺ ions in its lattice?", c="each atom gives two outer electrons to the sea of delocalised electrons",
      w=["each atom gains two electrons", "each atom shares two electrons", "each atom loses two protons"], ref="1.52C", d="7-9"),
    D(mq="Which statement about the electrons in a metal is correct?", c="they are delocalised and free to move",
      w=["they are fixed between pairs of atoms", "they are transferred to non-metal atoms", "they are all in the nucleus"]),
    D(mq="Why is a metal a good conductor of heat?", c="delocalised electrons carry energy through the metal", w=["ions move freely through the metal",
      "it has strong intermolecular forces", "it has a giant covalent structure"], ref="1.54C", d="4-6"),
    D(mq="What is meant by ductile?", c="able to be drawn into wires", w=["able to conduct electricity", "able to be hammered into shape only", "shiny when cut"], ref="1.54C"),
    D(mq="What does the 'sea' in a sea of electrons refer to?", c="electrons spread through the whole lattice", w=["water in which metal dissolves", "a layer of ions",
      "electrons held in the nucleus"], ref="1.52C"),
    D(mq="What happens to a metal lattice when it is hammered?", c="layers slide but the metallic bonding is kept",
      w=["the bonds break and it shatters", "the ions become atoms", "electrons are lost from the metal"], ref="1.54C", d="7-9"),
])

facts(ME, "1.53C", [
    D(q="State what is meant by **metallic bonding**.", a="electrostatic attraction between positive (metal) ions and delocalised electrons", n="REJECT ions and electrons attracting each other in pairs"),
    D(q="Give the name for the electrons that move freely through a metal lattice.", a="delocalised electrons", n="ALLOW free electrons / sea of electrons"),
    D(q="Draw a labelled diagram to show the arrangement of particles in a metal such as sodium.", a="", m=2,
      pts=["regular rows of positive ions labelled (e.g. Na⁺)", "electrons shown between the ions / labelled delocalised electrons"], ref="1.52C"),
    D(q="State the charge on the ions in a lattice of aluminium.", a="3+", ref="1.52C"),
    D(q="Give two physical properties of metals that can be explained by metallic bonding.", m=2,
      pts=["conduct electricity", "conduct heat", "malleable / ductile", "high melting point"], ref="1.54C"),
    D(q="State why a metal conducts electricity when solid.", a="delocalised electrons are free to move (and carry charge)", ref="1.54C"),
    D(q="State what is meant by the term **malleable**.", a="can be hammered / bent into shape without breaking", ref="1.54C"),
    D(q="Name the particles that carry the current in a copper wire.", a="(delocalised) electrons", ref="1.54C"),
    D(q="State the type of structure found in all metals.", a="giant (metallic) lattice"),
    D(q="Give one reason why metals have high melting points.", a="strong attraction between positive ions and delocalised electrons (much energy to overcome)"),
    D(q="State how the number of delocalised electrons per atom in magnesium compares with that in sodium.", a="magnesium has two per atom, sodium has one", d="4-6"),
    D(q="Explain the meaning of the word delocalised in metallic bonding.", a="the electrons are not attached to any one atom / spread through the structure", d="4-6"),
], intro="This question is about metals.")

items(ME, "explain", "1.54C", [
    D(s="Explain why {m} conducts electricity.", m=2, p=["contains delocalised electrons", "which can move through the structure (carrying charge)"],
      v=[{"m": "copper"}, {"m": "aluminium"}, {"m": "iron"}, {"m": "magnesium"}], n="REJECT ions moving"),
    D(s="Explain why metals are malleable.", m=2, p=["layers of (positive) ions", "can slide over each other (without breaking the metallic bonding)"]),
    D(s="Explain why metals usually have high melting points.", m=2, p=["strong electrostatic attraction between positive ions and delocalised electrons", "lots of energy needed to overcome it"], ref="1.53C"),
    D(s="Explain why magnesium has a higher melting point than sodium.", m=3,
      p=["magnesium ions are Mg²⁺ but sodium ions are Na⁺", "magnesium has two delocalised electrons per atom, sodium one",
         "so the attraction between ions and electrons is stronger in magnesium"], ref="1.53C", d="7-9"),
    D(s="Explain why a metal can be hammered into a thin sheet but an ionic crystal shatters.", m=3,
      p=["in a metal layers of ions slide and the delocalised electrons keep holding them together", "in an ionic crystal moving layers brings like charges together",
         "the like charges repel and it splits"], d="7-9"),
    D(s="Explain why copper is used for electrical wires.", m=2, p=["good conductor (delocalised electrons)", "ductile / can be drawn into wires"], d="4-6"),
    D(s="Describe and explain the structure of a metal in terms of its particles.", m=3,
      p=["giant lattice / regular arrangement of positive ions", "surrounded by a sea of delocalised electrons", "held by electrostatic attraction between them"], ref="1.52C"),
    D(s="Explain why metals are good conductors of heat.", m=2, p=["delocalised electrons can move", "and transfer (kinetic) energy through the metal"]),
    D(s="Explain why aluminium is a better electrical conductor than sodium, per atom.", m=2,
      p=["aluminium releases three outer electrons per atom", "more delocalised electrons to carry charge"], ref="1.53C", d="7-9"),
    D(s="Explain why metals conduct electricity in both the solid and liquid state, while ionic compounds conduct only as liquids.", m=3,
      p=["metals have delocalised electrons in both states", "ionic solids have ions fixed in a lattice", "ions only move when molten / dissolved"], d="7-9"),
])

# =================================================================== 1(i) electrolysis (C)
ELYTES = {  # name: (formula label, molten?, cathode product, anode product, cathode half, anode half)
    "molten lead(II) bromide": ("PbBr2", True, "lead", "bromine", "Pb^2+ + 2e^- -> Pb", "2Br^- -> Br2 + 2e^-"),
    "molten sodium chloride": ("NaCl", True, "sodium", "chlorine", "Na^+ + e^- -> Na", "2Cl^- -> Cl2 + 2e^-"),
    "molten zinc chloride": ("ZnCl2", True, "zinc", "chlorine", "Zn^2+ + 2e^- -> Zn", "2Cl^- -> Cl2 + 2e^-"),
    "molten potassium iodide": ("KI", True, "potassium", "iodine", "K^+ + e^- -> K", "2I^- -> I2 + 2e^-"),
    "molten lithium bromide": ("LiBr", True, "lithium", "bromine", "Li^+ + e^- -> Li", "2Br^- -> Br2 + 2e^-"),
    "molten calcium chloride": ("CaCl2", True, "calcium", "chlorine", "Ca^2+ + 2e^- -> Ca", "2Cl^- -> Cl2 + 2e^-"),
    "concentrated sodium chloride solution": ("NaCl(aq)", False, "hydrogen", "chlorine", "2H^+ + 2e^- -> H2", "2Cl^- -> Cl2 + 2e^-"),
    "copper(II) sulfate solution": ("CuSO4(aq)", False, "copper", "oxygen", "Cu^2+ + 2e^- -> Cu", "4OH^- -> O2 + 2H2O + 4e^-"),
    "dilute sulfuric acid": ("H2SO4(aq)", False, "hydrogen", "oxygen", "2H^+ + 2e^- -> H2", "4OH^- -> O2 + 2H2O + 4e^-"),
    "copper(II) chloride solution": ("CuCl2(aq)", False, "copper", "chlorine", "Cu^2+ + 2e^- -> Cu", "2Cl^- -> Cl2 + 2e^-"),
    "potassium bromide solution": ("KBr(aq)", False, "hydrogen", "bromine", "2H^+ + 2e^- -> H2", "2Br^- -> Br2 + 2e^-"),
    "silver nitrate solution": ("AgNO3(aq)", False, "silver", "oxygen", "Ag^+ + e^- -> Ag", "4OH^- -> O2 + 2H2O + 4e^-"),
    "sodium sulfate solution": ("Na2SO4(aq)", False, "hydrogen", "oxygen", "2H^+ + 2e^- -> H2", "4OH^- -> O2 + 2H2O + 4e^-"),
    "dilute hydrochloric acid": ("HCl(aq)", False, "hydrogen", "chlorine", "2H^+ + 2e^- -> H2", "2Cl^- -> Cl2 + 2e^-"),
    "potassium iodide solution": ("KI(aq)", False, "hydrogen", "iodine", "2H^+ + 2e^- -> H2", "2I^- -> I2 + 2e^-"),
    "sodium hydroxide solution": ("NaOH(aq)", False, "hydrogen", "oxygen", "2H^+ + 2e^- -> H2", "4OH^- -> O2 + 2H2O + 4e^-"),
    "magnesium sulfate solution": ("MgSO4(aq)", False, "hydrogen", "oxygen", "2H^+ + 2e^- -> H2", "4OH^- -> O2 + 2H2O + 4e^-"),
    "molten aluminium oxide": ("Al2O3", True, "aluminium", "oxygen", "Al^3+ + 3e^- -> Al", "2O^2- -> O2 + 4e^-"),
}
EL_NAMES = list(ELYTES)


@tpl(EL_, "mcq", 10)
def electrolysis_product_mcq(r, k):
    nm = EL_NAMES[(k * 5) % len(EL_NAMES)]
    _, mol, cat, an, *_ = ELYTES[nm]
    which = r.choice(["cathode", "anode"])
    ans = cat if which == "cathode" else an
    opts = ["hydrogen", "oxygen", "chlorine", "copper", "sodium", "bromine", "lead", "silver", "potassium", "iodine", "sulfur", "zinc"]
    wrong = [o for o in opts if o != ans and o != (an if which == "cathode" else cat)]
    r.shuffle(wrong)
    part, rw = mcq(r, f"{nm[0].upper() + nm[1:]} is electrolysed using inert electrodes. What is formed at the {which}?", ans, wrong[:3])
    part["label"] = ""
    return Q("What", "4-6" if not mol else "1-3", [part], [rw], ["1.58C"], style="mcq", ans=("discharge rules", {which: ans}), ao=["AO2"])


facts(EL_, "1.57C", [
    D(mq="What is an anion?", c="a negative ion", w=["a positive ion", "a negative electrode", "a neutral atom"]),
    D(mq="To which electrode do cations move during electrolysis?", c="the cathode (negative electrode)", w=["the anode (positive electrode)", "both electrodes", "neither electrode"]),
    D(mq="Why must lead(II) bromide be molten to be electrolysed?", c="so that its ions are free to move", w=["so that it forms molecules", "so that electrons can flow through it", "so that it dissolves"], ref="1.56C"),
    D(mq="What type of reaction happens at the anode?", c="oxidation", w=["reduction", "neutralisation", "displacement"], ref="1.59C"),
    D(mq="Which substance conducts electricity and is decomposed by it?", c="molten zinc chloride", w=["copper", "liquid ethanol", "graphite"], ref="1.56C", d="4-6"),
    D(mq="Why does pure liquid sulfur not conduct electricity?", c="it is covalent and has no ions or free electrons", w=["its ions cannot move", "it is a metal", "it is not hot enough"], ref="1.55C", d="4-6"),
    D(mq="Which half-equation shows a reduction?", c="Cu^2+ + 2e^- → Cu", w=["2Cl^- → Cl2 + 2e^-", "Fe → Fe^2+ + 2e^-", "2Br^- → Br2 + 2e^-"], ref="1.59C", d="7-9"),
    D(mq="Which electrodes are inert?", c="platinum and graphite", w=["copper and zinc", "iron and steel", "magnesium and aluminium"], ref="1.58C"),
    D(mq="What is a cation?", c="a positive ion", w=["a negative ion", "a positive electrode", "an uncharged particle"]),
    D(mq="Which test identifies the gas formed at the anode in the electrolysis of concentrated sodium chloride solution?", c="it bleaches damp blue litmus paper",
      w=["it relights a glowing splint", "it gives a squeaky pop with a lit splint", "it turns limewater milky"], ref="1.58C", d="4-6"),
    D(mq="In the electrolysis of dilute sulfuric acid, what is the ratio of the volume of hydrogen to the volume of oxygen?", c="2 : 1", w=["1 : 1", "1 : 2", "4 : 1"], ref="1.58C", d="7-9"),
    D(mq="Why is hydrogen, not sodium, formed at the cathode when sodium chloride solution is electrolysed?", c="hydrogen is less reactive than sodium",
      w=["sodium is less reactive than hydrogen", "sodium ions are not attracted to the cathode", "sodium dissolves in water"], ref="1.58C", d="7-9"),
])


@tpl(EL_, "recall", 16)
def electrolysis_products_recall(r, k):
    nm = EL_NAMES[k % len(EL_NAMES)]
    f, mol, cat, an, ch, ah = ELYTES[nm]
    parts = [P("a", f"Name the product formed at the cathode (negative electrode) when {nm} is electrolysed with inert electrodes.", 1, lines=1),
             P("b", "Name the product formed at the anode (positive electrode).", 1, lines=1)]
    rows = [row("a", cat, 1, "ALLOW formula" + ("; REJECT sodium" if cat == "hydrogen" and "sodium" in nm else ""), "AO1"),
            row("b", an, 1, "ALLOW formula; REJECT atomic symbols for gases e.g. O / Cl", "AO1")]
    if r.random() < 0.6:
        obs = {"bromine": "brown/orange vapour or liquid", "chlorine": "bubbles of pale green gas", "oxygen": "bubbles of colourless gas",
               "hydrogen": "bubbles of colourless gas", "copper": "pink/brown solid coats the electrode", "lead": "silvery/grey liquid metal forms",
               "iodine": "brown solution / black solid near the electrode", "silver": "grey/silver solid deposits", "sodium": "silvery liquid metal",
               "zinc": "grey solid", "potassium": "silvery metal", "lithium": "silvery metal", "calcium": "grey solid", "aluminium": "molten aluminium collects"}
        parts.append(P("c", "Give one observation at the anode.", 1, lines=2))
        rows.append(row("c", obs[an], 1, None, "AO1"))
    return Q("Name", "1-3" if mol else "4-6", parts, rows, ["1.58C"], ans=("discharge rules", {"cathode": cat, "anode": an}), ao=["AO1"])


@tpl(EL_, "equation", 24)
def electrolysis_half_eq(r, k):
    nm = EL_NAMES[k % len(EL_NAMES)]
    f, mol, cat, an, ch, ah = ELYTES[nm]
    which = "cathode" if (k // len(EL_NAMES)) % 2 == 0 else "anode"
    eq = ch if which == "cathode" else ah
    redox = "reduction" if which == "cathode" else "oxidation"
    parts = [P("a", f"Write the ionic half-equation for the reaction at the {which} during the electrolysis of {nm}.", 2, lines=2),
             P("b", f"State whether the reaction at the {which} is oxidation or reduction. Give a reason.", 2, lines=3)]
    rows = [row("a", f"M1 correct species: {EQ(eq)}", 1, "ALLOW e for e⁻; IGNORE state symbols", "AO2"),
            row("a", "M2 balanced (atoms and charge)", 1, "M2 dep on M1; ALLOW multiples", "AO2"),
            row("b", f"M1 {redox}", 1, None, "AO1"),
            row("b", "M2 " + ("electrons are gained" if redox == "reduction" else "electrons are lost"), 1, "M2 dep on M1", "AO1")]
    if which == "anode" and "OH" in eq:
        rows[0]["notes"] = "ALLOW 2H2O → O2 + 4H⁺ + 4e⁻"
    return Q("Write", "7-9" if "OH" in eq or "O^2-" in eq else "4-6", parts, rows, ["1.59C"], ao=["AO2"],
             ans=("balanced half-equation", {"half": EQ(eq)}))


items(EL_, "explain", "1.56C", [
    D(s="Explain why solid {c} does not conduct electricity but becomes a conductor when it is {how}.", m=3,
      p=["{c} is ionic", "in the solid the ions are held in fixed positions / cannot move", "when {how} the ions are free to move (and carry charge)"],
      v=[{"c": "lead(II) bromide", "how": "melted"}, {"c": "sodium chloride", "how": "dissolved in water"}, {"c": "copper(II) sulfate", "how": "dissolved in water"}]),
    D(s="Explain why hydrogen is formed at the cathode instead of {m} when {s} is electrolysed.", m=2,
      p=["{m} is more reactive than hydrogen", "so hydrogen ions are discharged instead (gain electrons more easily)"],
      v=[{"m": "sodium", "s": "sodium chloride solution"}, {"m": "potassium", "s": "potassium bromide solution"}, {"m": "magnesium", "s": "magnesium sulfate solution"}], ref="1.58C", d="7-9"),
    D(s="Explain why the reaction at the cathode is described as reduction.", m=2, p=["positive ions gain electrons at the cathode", "gain of electrons is reduction"], ref="1.59C"),
    D(s="Explain why the blue colour of copper(II) sulfate solution fades during electrolysis with inert electrodes.", m=2,
      p=["Cu²⁺ ions (which cause the blue colour) are discharged at the cathode", "so the concentration of Cu²⁺ ions in solution falls"], d="7-9"),
    D(s="Explain why covalent compounds such as ethanol do not conduct electricity.", m=2, p=["they are made of molecules", "no ions or delocalised electrons to carry charge"], ref="1.55C"),
    D(s="Explain why the solution near the cathode becomes alkaline during the electrolysis of concentrated sodium chloride solution.", m=2,
      p=["hydrogen ions are discharged / removed (as H₂)", "hydroxide ions (and Na⁺) remain, forming sodium hydroxide"], ref="1.58C", d="7-9"),
    D(s="Explain why bromide ions move towards the anode.", m=2, p=["bromide ions are negative (anions)", "attracted to the positive electrode (opposite charges attract)"], ref="1.57C"),
    D(s="Explain why the electrolysis of molten lead(II) bromide must be done in a fume cupboard.", m=2, p=["bromine is produced", "bromine (vapour) is toxic"], ref="1.58C"),
    D(s="Explain why twice the volume of hydrogen is produced compared with oxygen when dilute sulfuric acid is electrolysed.", m=2,
      p=["4 electrons are needed to form one O₂ but only 2 for one H₂", "so for the same number of electrons, two moles of H₂ form for each mole of O₂"], ref="1.59C", d="7-9"),
    D(s="Explain why graphite is often used for electrodes in electrolysis.", m=2, p=["it conducts electricity (delocalised electrons)", "it is inert / unreactive / high melting point"], d="4-6"),
    D(s="Explain why oxygen and not sulfur dioxide is formed at the anode when copper(II) sulfate solution is electrolysed.", m=2,
      p=["sulfate ions are not discharged", "hydroxide ions (from water) are discharged instead, forming oxygen"], ref="1.58C", d="7-9"),
    D(s="Explain why aluminium oxide must be molten before it can be electrolysed to form aluminium.", m=2,
      p=["aluminium oxide is ionic", "ions only free to move when molten"], ref="1.56C", d="4-6"),
])

items(EL_, "practical", "1.60C", [
    D(s="Describe how you would collect and test the gas produced at the anode during the electrolysis of dilute sulfuric acid.", m=3,
      p=["fill a test tube with the solution and invert it over the anode", "collect the gas by displacement", "test with a glowing splint: relights (oxygen)"], d="4-6"),
    D(s="Describe how you could show that hydrogen is produced at the cathode when sodium chloride solution is electrolysed.", m=2,
      p=["collect the gas in an inverted test tube", "lit splint gives a squeaky pop"], ref="1.58C"),
    D(s="Give two safety precautions when electrolysing concentrated sodium chloride solution.", m=2,
      p=["use a fume cupboard / well-ventilated room (chlorine is toxic)", "wear eye protection", "low voltage supply", "turn off power before touching electrodes"], any=True),
    D(s="Suggest why inert electrodes are used when investigating the products of electrolysis of aqueous solutions.", m=1,
      p=["they do not react / take part in the reaction (so products come only from the solution)"]),
    D(intro="A student electrolyses copper(II) sulfate solution with graphite electrodes. She weighs the cathode before and after passing a current for 20 minutes.",
      s="Describe how she should treat the cathode before weighing it again.", m=2,
      p=["rinse with distilled water (then propanone)", "dry it carefully before weighing / do not rub off the copper"], d="7-9"),
    D(intro="A student electrolyses copper(II) sulfate solution with graphite electrodes. She weighs the cathode before and after passing a current for 20 minutes.",
      s="State two variables she should control if she repeats the experiment at a higher current.", m=2,
      p=["time", "concentration of solution", "volume of solution", "temperature", "size/distance of electrodes"], any=True, d="4-6"),
    D(s="Suggest why a few drops of universal indicator added to sodium chloride solution change colour near the electrodes during electrolysis.", m=2,
      p=["near the cathode it turns blue/purple because hydroxide ions build up / alkali", "near the anode it is bleached by chlorine"], d="7-9"),
    D(s="Explain why the electrolysis of molten salts is usually demonstrated by the teacher rather than done by students.", m=2,
      p=["very high temperatures are needed", "toxic products / molten salts can burn"], d="4-6"),
    D(s="Describe what you would see at each electrode when copper(II) chloride solution is electrolysed with graphite electrodes.", m=2,
      p=["cathode: pink/brown coating of copper", "anode: bubbles of (pale green) gas / smell of chlorine"], ref="1.58C"),
    D(s="Describe how the volume of gas at each electrode can be measured during electrolysis of a solution.", m=2,
      p=["use (graduated) inverted tubes / gas syringes over each electrode", "read the volume collected at set times"], d="4-6"),
    D(s="A student does not get any gas when he electrolyses pure water. Suggest why and how to fix this.", m=2,
      p=["pure water contains very few ions / is a very poor conductor", "add a little dilute sulfuric acid / sodium sulfate"], d="7-9"),
    D(s="Draw a labelled diagram of the apparatus for electrolysing a solution and collecting the gases formed.", m=3,
      p=["beaker/cell containing electrolyte with two electrodes", "electrodes connected to a d.c. power supply", "inverted test tubes over each electrode"], space="box", d="4-6"),
])

extended(EL_, "1.58C", [
    D(s=f"Describe what happens when {nm} is electrolysed using inert electrodes. Include the products at each electrode, half-equations "
        f"and how you could identify any gaseous products.",
      ind=[f"electrolyte contains ions that move when {'molten' if v[1] else 'in solution'}",
           f"positive ions move to the cathode; {v[2]} formed", f"cathode: {EQ(v[4])} (reduction)",
           f"negative ions move to the anode; {v[3]} formed", f"anode: {EQ(v[5])} (oxidation)",
           {"hydrogen": "hydrogen test: lit splint – squeaky pop", "copper": "copper: pink/brown deposit", "sodium": "sodium: silvery metal",
            "lead": "lead: molten grey metal at bottom", "silver": "silver: grey deposit", "zinc": "zinc: grey metal", "potassium": "potassium: silvery metal",
            "calcium": "calcium: grey metal", "lithium": "lithium: silvery metal", "aluminium": "aluminium: molten metal"}[v[2]],
           {"oxygen": "oxygen test: relights a glowing splint", "chlorine": "chlorine test: bleaches damp (blue) litmus paper",
            "bromine": "bromine: orange/brown vapour", "iodine": "iodine: brown solution / black solid"}[v[3]]],
      ao="AO1 3, AO2 3", d="7-9" if not v[1] else "4-6",
      ref=["1.58C", "1.59C"]) for nm, v in ELYTES.items() if nm not in ("molten lithium bromide", "molten calcium chloride", "magnesium sulfate solution", "sodium hydroxide solution")
])
