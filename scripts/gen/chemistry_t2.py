"""Topic 2 templates: inorganic chemistry (2(a) to 2(i))."""
from fractions import Fraction as Fr

from chemistry_util import tpl, mcq, P, F, row, Q, num, Mr, AR, EQ, eq_terms, unbalanced_skeleton, fig, table, graph
from chemistry_kb import facts, items, extended
import chemistry_svg as S

G1 = "chemistry.inorganic.group1"
G7 = "chemistry.inorganic.group7"
AI = "chemistry.inorganic.air"
RE = "chemistry.inorganic.reactivity"
EX = "chemistry.inorganic.extraction"
AC = "chemistry.inorganic.acids"
SA = "chemistry.inorganic.salts"
TE = "chemistry.inorganic.tests"


def D(**k):
    return k


def eq_q(word, sym, ref, d="4-6", mode=0, extra_note=None):
    """Shared equation question: mode 0 full symbol equation with states, 1 balance, 2 word + states, 3 ionic from full."""
    skel = unbalanced_skeleton(sym)
    L_, R_ = eq_terms(sym)
    if mode == 0:
        stem = f"Write a balanced equation, with state symbols, for this reaction.\n\n{word}"
        rows = [row("", f"M1 correct formulae: {skel}", 1, None, "AO2"),
                row("", f"M2 balanced: {EQ(sym, states=False)}", 1, "M2 dep on M1; ALLOW multiples / fractions", "AO2"),
                row("", f"M3 state symbols: {EQ(sym)}", 1, extra_note or "M3 dep on correct formulae", "AO2")]
        return Q("Write", d, [P("", stem, 3, lines=3)], rows, ref, ao=["AO2"], ans=("atom and charge balance", {"equation": EQ(sym)}))
    if mode == 1:
        if all(c == 1 for c, _, _ in L_ + R_):
            return None
        bare = skel
        for s_ in ("(s)", "(l)", "(g)", "(aq)"):
            bare = bare.replace(s_, "")
        stem = f"Balance the equation for this reaction.\n\n{bare}"
        return Q("Balance", "1-3" if len(L_ + R_) <= 3 else "4-6", [P("", stem, 1, lines=2)],
                 [row("", EQ(sym, states=False), 1, "ALLOW multiples", "AO2")], ref, ao=["AO2"],
                 ans=("atom balance", {"equation": EQ(sym, states=False)}))
    stem = f"The equation for a reaction is\n\n{EQ(sym, states=False)}\n\nWrite the word equation and add state symbols to the symbol equation."
    st = ", ".join(f"{F(t)}({s})" for side in (L_, R_) for _, t, s in side)
    rows = [row("", f"M1 {word}", 1, "IGNORE state symbols in word equation", "AO1"),
            row("", f"M2 {st}", 1, "all state symbols correct", "AO2")]
    return Q("Write", d, [P("", stem, 2, lines=4)], rows, ref, ao=["AO2"], ans=("states", {"equation": EQ(sym)}))


# =================================================================== 2(a) group 1
ALK = [("Li", "lithium"), ("Na", "sodium"), ("K", "potassium"), ("Rb", "rubidium"), ("Cs", "caesium")]

facts(G1, "2.1", [
    D(mq="Which gas is given off when sodium reacts with water?", c="hydrogen", w=["oxygen", "carbon dioxide", "chlorine"]),
    D(mq="What is the pH of the solution formed when potassium reacts with water?", c="13", w=["1", "4", "7"], d="4-6"),
    D(mq="Which alkali metal reacts most vigorously with water?", c="potassium", w=["lithium", "sodium", "all react equally"], ref="2.2"),
    D(mq="Why are lithium, sodium and potassium stored under oil?", c="to stop them reacting with air and water", w=["to keep them cool",
      "to stop them melting", "to make them softer"]),
    D(mq="Which observation is made when lithium is added to water?", c="it fizzes steadily and floats", w=["it explodes", "it sinks and does not react",
      "it melts into a ball and burns with a lilac flame"], ref="2.2"),
    D(mq="Which observation shows that potassium is more reactive than sodium?", c="potassium burns with a lilac flame on water",
      w=["potassium floats", "potassium forms an alkaline solution", "potassium gives off a gas"], ref="2.2", d="4-6"),
    D(mq="Which is the formula of the compound formed when sodium burns in chlorine?", c="NaCl", w=["NaCl2", "Na2Cl", "Na2Cl2"]),
    D(mq="What happens to the melting point of the alkali metals down the group?", c="it decreases", w=["it increases", "it stays the same",
      "it increases then decreases"], ref="2.3", d="4-6"),
    D(mq="Why does a freshly cut piece of sodium soon lose its shine?", c="it reacts with oxygen in the air", w=["it dissolves in the air",
      "it reacts with nitrogen in the air", "it melts"], ref="2.2"),
    D(mq="Rubidium is below potassium in Group 1. How will rubidium react with water?", c="more vigorously than potassium",
      w=["less vigorously than lithium", "it will not react", "at the same rate as sodium"], ref="2.3", d="4-6"),
    D(mq="Why does reactivity increase down Group 1?", c="the outer electron is further from the nucleus and is lost more easily",
      w=["the atoms have more outer electrons", "the nucleus has fewer protons", "the atoms gain electrons more easily"], ref="2.4C", d="7-9"),
    D(mq="Which property is shown by all the Group 1 metals?", c="they are soft and can be cut with a knife", w=["they are very dense",
      "they have high melting points", "they sink in water"]),
    D(mq="What colour does universal indicator turn in the solution left after sodium reacts with water?", c="purple", w=["red", "green", "orange"], d="4-6"),
], intro="This question is about the alkali metals.")

facts(G1, "2.1", [
    D(q="Name the two products formed when lithium reacts with water.", m=2, pts=["lithium hydroxide", "hydrogen"]),
    D(q="Give two observations when a small piece of sodium is dropped into a trough of water.", m=2,
      pts=["floats", "fizzes / bubbles", "melts into a ball", "moves around (on the surface)", "gets smaller / disappears"], ref="2.2"),
    D(q="A tiny piece of potassium is placed on water. Give one observation that is not seen with sodium.", a="lilac flame / burns", ref="2.2"),
    D(q="State why the solution formed when sodium reacts with water is alkaline.", a="sodium hydroxide forms, which contains OH⁻ ions"),
    D(q="Predict how the density of caesium compares with that of potassium.", a="caesium is denser", n="ALLOW higher density", ref="2.3", d="4-6"),
    D(q="Give the name of the compound that forms on the surface of lithium when it is cut and left in air.", a="lithium oxide", ref="2.2"),
    D(q="Give the electronic configuration of a potassium ion.", a="2.8.8", ref="2.4C", d="4-6"),
    D(q="Rubidium chloride is a white solid. Predict its formula and whether it dissolves in water.", m=2, pts=["RbCl", "soluble"], ref="2.3", d="4-6"),
    D(q="Name the substance under which sodium is kept in the laboratory.", a="oil / paraffin oil"),
    D(q="State why Group 1 elements are called alkali metals.", a="they react with water to form alkaline solutions / hydroxides"),
    D(q="Give one safety precaution when a teacher demonstrates potassium reacting with water.", a="safety screen / use a very small piece / goggles"),
], intro="This question is about lithium, sodium and potassium.")

items(G1, "describe", "2.2", [
    D(s="Describe what you would see when {m} is added to cold water.", m=3, p=["{a}", "{b}", "{c}"],
      v=[{"m": "lithium", "a": "floats", "b": "fizzes steadily / bubbles", "c": "slowly gets smaller / disappears"},
         {"m": "sodium", "a": "floats and melts into a ball", "b": "fizzes rapidly / moves around the surface", "c": "disappears quickly"},
         {"m": "potassium", "a": "floats and melts", "b": "lilac flame / burns", "c": "moves very rapidly / may spark or explode"}]),
    D(s="Describe how you could show that the solution formed when {m} reacts with water is alkaline.", m=2,
      p=["add universal indicator (or red litmus)", "turns blue/purple (litmus turns blue)"], v=[{"m": "lithium"}, {"m": "sodium"}], ref="2.1"),
    D(s="Describe the trend in reactivity of the Group 1 metals with water and give evidence from observations.", m=3,
      p=["reactivity increases down the group", "lithium fizzes slowly while sodium melts and moves quickly", "potassium ignites with a lilac flame"], d="4-6"),
    D(s="Describe how you could test the gas produced when sodium reacts with water.", m=2, p=["hold a lighted splint near the gas", "squeaky pop shows hydrogen"]),
    D(s="Describe what happens when a freshly cut surface of sodium is left exposed to air.", m=2, p=["shiny surface", "quickly goes dull / tarnishes (as an oxide forms)"]),
    D(s="Describe how sodium reacts with chlorine gas and name the product.", m=2, p=["burns with a bright (yellow) flame", "forms white solid sodium chloride"], ref="2.1", d="4-6"),
    D(s="Describe how the reaction of {m} with water would be different from that of potassium.", m=2, p=["{x}", "{y}"],
      v=[{"m": "rubidium", "x": "more violent / explodes", "y": "reacts faster than potassium"},
         {"m": "lithium", "x": "much less vigorous / slower fizzing", "y": "does not melt / no flame"}], ref="2.3", d="4-6"),
    D(s="Describe how the hardness of the alkali metals changes down the group, and how you could show this.", m=2,
      p=["they get softer down the group", "compare how easily each is cut with a knife"], ref="2.3", d="4-6"),
    D(s="Describe how a sample of solid lithium hydroxide could be obtained after lithium reacts with water.", m=2,
      p=["heat the solution to evaporate the water", "white solid remains"], d="7-9"),
    D(s="Describe the safety precautions needed when a teacher shows students how sodium reacts with water.", m=3,
      p=["use a small piece", "safety screen between metal and students", "goggles / handle with tongs / not with fingers"], any=True),
])

items(G1, "explain", "2.4C", [
    D(s="Explain why potassium is more reactive than sodium.", m=3,
      p=["potassium atom is larger / has more shells", "outer electron further from nucleus / more shielding", "weaker attraction so electron lost more easily"]),
    D(s="Explain why the alkali metals have similar reactions with water.", m=2, p=["all have one electron in their outer shell", "all lose one electron to form 1+ ions"], ref="2.1"),
    D(s="Explain why lithium is the least reactive alkali metal.", m=3, p=["lithium has the fewest shells / smallest atom", "outer electron closest to nucleus",
      "strongest attraction so hardest to lose"], d="7-9"),
    D(s="Explain why caesium is expected to react explosively with water.", m=2, p=["caesium is lower in Group 1", "its outer electron is lost very easily (far from the nucleus)"], ref="2.3", d="4-6"),
    D(s="Explain why sodium floats on water.", m=1, p=["it is less dense than water"], ref="2.2", d="1-3"),
    D(s="Explain why sodium forms an ion with a charge of 1+.", m=2, p=["it loses its single outer electron", "11 protons and 10 electrons"], d="4-6"),
    D(s="Explain why the reactions of the alkali metals with water are described as exothermic, using an observation.", m=2,
      p=["heat is given out", "sodium/potassium melts / potassium catches fire"], ref="2.2", d="4-6"),
    D(s="Explain why the alkali metals must be stored away from water and air.", m=2, p=["they react with oxygen and with water", "to stop them forming oxides / hydroxides (losing the metal)"]),
    D(s="Explain why the melting points of the alkali metals decrease down the group.", m=2,
      p=["atoms/ions get larger down the group", "weaker attraction between ions and delocalised electrons"], ref="2.3", d="7-9"),
    D(s="Explain why francium would be the most reactive Group 1 metal.", m=2, p=["it has the most shells / largest atoms", "outer electron lost most easily"], ref="2.3", d="7-9"),
])

G1_EQ = []
for s_, n_ in ALK:
    G1_EQ.append((f"{n_} + water → {n_} hydroxide + hydrogen", f"2{s_}(s) + 2H2O(l) -> 2{s_}OH(aq) + H2(g)"))
    G1_EQ.append((f"{n_} + oxygen → {n_} oxide", f"4{s_}(s) + O2(g) -> 2{s_}2O(s)"))
    G1_EQ.append((f"{n_} + chlorine → {n_} chloride", f"2{s_}(s) + Cl2(g) -> 2{s_}Cl(s)"))


@tpl(G1, "equation", 24)
def group1_equations(r, k):
    word, sym = G1_EQ[k % len(G1_EQ)]
    mode = (k // len(G1_EQ)) % 3
    q = eq_q(word, sym, ["2.1", "2.3"] if any(x in word for x in ("rubidium", "caesium")) else ["2.1"],
             d="7-9" if "oxide" in word and mode == 0 else "4-6", mode=mode)
    return q


G1_DATA = {"lithium": (181, 1342, 0.53), "sodium": (98, 883, 0.97), "potassium": (63, 759, 0.86), "rubidium": (39, 688, 1.53), "caesium": (29, 671, 1.93)}


@tpl(G1, "data", 14)
def group1_trend_data(r, k):
    names = list(G1_DATA)
    hide = names[k % 5]
    prop = ["melting point in °C", "boiling point in °C"][(k // 5) % 2]
    idx = 0 if "melting" in prop else 1
    rows_t = [[n, ("?" if n == hide else str(G1_DATA[n][idx])), ("?" if n == hide else str(G1_DATA[n][2]))] for n in names]
    tb = table(["Metal", prop.capitalize(), "Density in g/cm³"], rows_t)
    i = names.index(hide)
    nb = [G1_DATA[names[j]][idx] for j in (i - 1, i + 1) if 0 <= j < 5]
    lo, hi = (min(nb), max(nb)) if len(nb) == 2 else ((nb[0] - 80, nb[0] - 5) if i == 4 else (nb[0] + 5, nb[0] + 150))
    parts = [P("a", f"Describe the trend in {prop.split(' in')[0]} down Group 1.", 1, lines=2),
             P("b", f"Predict a value for the {prop.split(' in')[0]} of {hide}.", 1, answer_prefix="", lines=1),
             P("c", "State one way in which the density values do not follow a simple trend.", 1, lines=2),
             P("d", "Which of these metals would sink in water? Give a reason.", 2, lines=3)]
    sink = [n for n in names if G1_DATA[n][2] > 1 and n != hide]
    rows = [row("a", "decreases (down the group)", 1, None, "AO3"),
            row("b", f"any value from {lo} to {hi} °C", 1, f"actual value {G1_DATA[hide][idx]} °C", "AO3"),
            row("c", "potassium is less dense than sodium (density does not increase steadily)" if hide not in ("sodium", "potassium")
                else "density generally increases but one value breaks the pattern / lithium is least dense", 1, None, "AO3"),
            row("d", f"M1 {' and '.join(sink) if sink else 'none'}", 1, None, "AO3"),
            row("d", "M2 density greater than 1.0 g/cm³ (density of water)", 1, None, "AO3")]
    if k >= 10:
        parts.append(P("e", "Francium is below caesium in Group 1. Predict how its reaction with water compares with that of caesium.", 1, lines=2))
        rows.append(row("e", "more vigorous / explosive (faster)", 1, None, "AO3"))
    return Q("Predict", "4-6", parts, rows, ["2.3"], figs=[tb], intro="The table shows some properties of the Group 1 metals.",
             ans=("trend", {"predict_range": [lo, hi], "actual": G1_DATA[hide][idx]}), ao=["AO3"])


# =================================================================== 2(b) group 7
HAL = [("F", "fluorine", "pale yellow", "gas"), ("Cl", "chlorine", "pale green / yellow-green", "gas"),
       ("Br", "bromine", "red-brown", "liquid"), ("I", "iodine", "dark grey / black", "solid"), ("At", "astatine", "black", "solid")]

facts(G7, "2.5", [
    D(mq="What is the colour of chlorine gas?", c="pale yellow-green", w=["red-brown", "purple", "colourless"]),
    D(mq="What is the state of bromine at room temperature?", c="liquid", w=["solid", "gas", "it sublimes"]),
    D(mq="What colour is iodine vapour?", c="purple", w=["green", "orange", "colourless"], d="4-6"),
    D(mq="Which halogen is the most reactive?", c="fluorine", w=["chlorine", "bromine", "iodine"], ref="2.6"),
    D(mq="What colour is the solution when chlorine water is added to potassium iodide solution?", c="brown", w=["colourless", "green", "purple"], ref="2.7", d="4-6"),
    D(mq="Which pair of substances react together?", c="bromine and potassium iodide", w=["iodine and potassium bromide", "bromine and potassium chloride",
      "iodine and sodium chloride"], ref="2.7", d="4-6"),
    D(mq="Astatine is below iodine in Group 7. What is astatine most likely to be at room temperature?", c="a black solid",
      w=["a pale yellow gas", "a red-brown liquid", "a colourless gas"], ref="2.6", d="4-6"),
    D(mq="What is formed when chlorine reacts with sodium bromide solution?", c="sodium chloride and bromine", w=["sodium chlorate and bromine",
      "no reaction", "sodium and bromine chloride"], ref="2.7"),
    D(mq="Why does reactivity decrease down Group 7?", c="it is harder for the atoms to gain an electron as the outer shell gets further from the nucleus",
      w=["the atoms lose electrons less easily", "the atoms have more outer electrons", "the molecules get smaller"], ref="2.8C", d="7-9"),
    D(mq="Which halogen exists as diatomic molecules?", c="all of them", w=["only fluorine and chlorine", "only iodine", "none of them"]),
    D(mq="In the reaction Cl₂ + 2Br⁻ → 2Cl⁻ + Br₂, which species is oxidised?", c="Br⁻", w=["Cl₂", "Cl⁻", "Br₂"], ref="2.8C", d="7-9"),
    D(mq="What happens to the boiling points of the halogens down the group?", c="they increase", w=["they decrease", "they stay the same", "they decrease then increase"], ref="2.6"),
], intro="This question is about the halogens.")

facts(G7, "2.5", [
    D(q="Give the colour and physical state of bromine at room temperature.", m=2, pts=["red-brown / orange-brown", "liquid"]),
    D(q="Give the colour and physical state of iodine at room temperature.", m=2, pts=["grey-black / dark grey", "solid"]),
    D(q="Give the colour of chlorine gas.", a="pale green / yellow-green"),
    D(q="Predict the state of astatine at room temperature.", a="solid", ref="2.6", d="4-6"),
    D(q="Name the products when chlorine water is added to potassium iodide solution.", m=2, pts=["potassium chloride", "iodine"], ref="2.7"),
    D(q="Give the formula of a molecule of bromine.", a="Br2"),
    D(q="Name the halogen that would displace bromine from sodium bromide solution.", a="chlorine / fluorine", ref="2.7"),
    D(q="State why iodine solution does not react with potassium chloride solution.", a="iodine is less reactive than chlorine", ref="2.7", d="4-6"),
    D(q="Give the colour change when chlorine water is added to sodium bromide solution.", a="colourless to orange / yellow-orange", ref="2.7", d="4-6"),
    D(q="Give the charge on a halide ion.", a="1− / −1"),
    D(q="Predict the colour of astatine.", a="black", ref="2.6"),
], intro="This question is about the elements in Group 7.")

items(G7, "explain", "2.8C", [
    D(s="Explain why chlorine is more reactive than bromine.", m=3,
      p=["chlorine atoms are smaller / have fewer shells", "outer shell closer to the nucleus / less shielding", "so an electron is gained more easily"]),
    D(s="Explain why bromine water does not react with potassium chloride solution.", m=2, p=["bromine is less reactive than chlorine", "so cannot displace chloride / chlorine"], ref="2.7"),
    D(s="Explain why the halogens have similar chemical reactions.", m=2, p=["all have seven outer electrons", "all gain one electron to form 1− ions"], ref="2.6"),
    D(s="Explain, in terms of electrons, why the reaction between chlorine and potassium iodide is a redox reaction.", m=3,
      p=["chlorine gains electrons / is reduced to chloride ions", "iodide ions lose electrons / are oxidised to iodine", "both oxidation and reduction occur"], d="7-9"),
    D(s="Explain why the boiling point of iodine is higher than that of chlorine.", m=2, p=["iodine molecules are larger / higher Mr", "stronger intermolecular forces"], ref="2.6", d="4-6"),
    D(s="Explain why fluorine is the most reactive halogen.", m=2, p=["smallest atom / outer shell closest to nucleus", "strongest attraction for an extra electron"], d="7-9"),
    D(s="Predict and explain whether astatine would displace iodine from potassium iodide solution.", m=2, p=["no reaction", "astatine is less reactive than iodine"], ref="2.6", d="4-6"),
    D(s="Explain why a solution of chlorine in water is used to identify bromide ions in a mixture.", m=2,
      p=["chlorine displaces bromine from bromide ions", "orange colour of bromine appears"], ref="2.7", d="7-9"),
    D(s="Explain why chlorine is described as an oxidising agent in its reaction with iron(II) ions.", m=2,
      p=["chlorine gains electrons / is reduced", "it causes iron(II) to lose an electron / be oxidised to iron(III)"], ref="2.8C", d="7-9"),
    D(s="Describe the trend in the colour of the halogen elements from fluorine to iodine.", m=1, p=["they get darker (pale yellow → yellow-green → red-brown → dark grey/purple-black)"], ref="2.6", d="4-6",
      n="ALLOW 'get darker' without the individual colours"),
])

HD = [("Cl", "chlorine", "Br", "bromide", "bromine"), ("Cl", "chlorine", "I", "iodide", "iodine"), ("Br", "bromine", "I", "iodide", "iodine")]
CATS = [("K", "potassium"), ("Na", "sodium"), ("Li", "lithium"), ("Mg", "magnesium"), ("Ca", "calcium")]


@tpl(G7, "equation", 24)
def group7_displacement_eq(r, k):
    hx, hn, yx, yn, yel = HD[k % 3]
    cs, cn = CATS[(k // 3) % 5]
    if cs in ("Mg", "Ca"):
        sym = f"{hx}2(aq) + {cs}{yx}2(aq) -> {cs}{hx}2(aq) + {yx}2(aq)"
    else:
        sym = f"{hx}2(aq) + 2{cs}{yx}(aq) -> 2{cs}{hx}(aq) + {yx}2(aq)"
    ion = f"{hx}2(aq) + 2{yx}^-(aq) -> 2{hx}^-(aq) + {yx}2(aq)"
    word = f"{hn} + {cn} {yn} → {cn} {hn[:-3] if hn.endswith('ine') else hn}ide + {yel}"
    word = word.replace("chloride", "chloride").replace("brominide", "bromide")
    word = f"{hn} + {cn} {yn} → {cn} {'chloride' if hx == 'Cl' else 'bromide'} + {yel}"
    if (k // 15) % 2 == 0:
        return eq_q(word, sym, ["2.7"], d="4-6", mode=0)
    parts = [P("a", f"Write the ionic equation for the reaction between {hn} and {yn} ions.", 2, lines=2),
             P("b", "Identify the species that is reduced. Give a reason.", 2, lines=3)]
    rows = [row("a", f"M1 correct species {F(hx + '2')}, {F(yx + '^-')}, {F(hx + '^-')}, {F(yx + '2')}", 1, "IGNORE state symbols", "AO2"),
            row("a", f"M2 balanced: {EQ(ion, states=False)}", 1, None, "AO2"),
            row("b", f"M1 {F(hx + '2')} / {hn}", 1, None, "AO2"),
            row("b", "M2 gains electrons", 1, "ALLOW oxidation number decreases", "AO2")]
    return Q("Write", "7-9", parts, rows, ["2.7", "2.8C"], intro=f"Aqueous {hn} is added to {cn} {yn} solution.", ao=["AO2"],
             ans=("ionic", {"ionic": EQ(ion)}))


items(G7, "practical", "2.7", [
    D(s="Describe how you could use displacement reactions to put chlorine, bromine and iodine in order of reactivity.", m=4,
      p=["add each halogen solution to solutions of the other halides (e.g. potassium chloride, bromide, iodide)", "look for a colour change",
         "a colour change shows the halogen is more reactive than the halogen in the halide", "chlorine displaces both, bromine displaces iodine only"], any=True, d="7-9"),
    D(s="Give two safety precautions when using chlorine water in displacement experiments.", m=2, p=["fume cupboard / ventilated room", "eye protection", "avoid skin contact / gloves"], any=True),
    D(s="Suggest why an organic solvent such as cyclohexane is sometimes shaken with the mixture after a halogen displacement reaction.", m=2,
      p=["the halogen dissolves in the organic layer", "colours are clearer (bromine orange, iodine purple) so easier to identify"], d="7-9"),
    D(s="State the variables that should be kept the same in a halogen displacement experiment.", m=2,
      p=["volume of halide solution", "concentration of solutions", "volume of halogen water", "temperature"], any=True, d="4-6"),
    D(s="A student adds bromine water to potassium iodide solution. State what she would see and name the product that causes the colour.", m=2,
      p=["solution turns brown", "iodine"]),
    D(s="A student adds iodine solution to potassium bromide solution. Describe and explain the result.", m=2,
      p=["no change (stays brown/iodine colour)", "iodine is less reactive than bromine so no displacement"], d="4-6"),
    D(s="Suggest why it can be hard to tell whether bromine water has reacted with potassium iodide solution, and how to make it clearer.", m=2,
      p=["orange bromine and brown iodine look similar", "add starch (blue-black with iodine) / shake with organic solvent"], d="7-9"),
    D(s="Suggest why the experiments are done in spotting tiles or small test tubes with only a few drops of each solution.", m=2,
      p=["halogens are toxic / harmful", "small volumes reduce exposure / waste"], d="4-6"),
    D(s="Explain why the student uses solutions of halides of the same metal, such as potassium, in a halogen displacement experiment.", m=2,
      p=["so the only variable changed is the halide", "so the metal ion does not affect the result (fair test)"], d="7-9"),
    D(s="Draw a results grid that a student could use to record the results of reacting three halogens with three halide solutions.", m=2,
      p=["grid with halogens on one side and halide solutions on the other", "cells for halogen with its own halide marked as not needed / X"], space="box", d="4-6"),
    D(s="Describe a test to show that a gas is chlorine.", m=2, p=["damp (blue) litmus paper", "turns red then bleaches / white"], ref="2.44", d="1-3"),
    D(s="Suggest why chlorine water stored in a clear bottle gradually loses its colour.", m=1, p=["chlorine reacts with water (in light) / escapes as a gas"], d="7-9"),
])


@tpl(G7, "data", 14)
def group7_trend_data(r, k):
    data = [("fluorine", 9, -220, -188), ("chlorine", 17, -101, -34), ("bromine", 35, -7, 59), ("iodine", 53, 114, 184), ("astatine", 85, None, None)]
    hide = [1, 2, 3, 4][k % 4]
    rows_t = []
    for i, (n, z, mp, bp) in enumerate(data):
        if i == 4 or i == hide:
            rows_t.append([n, str(z), "?", "?"])
        else:
            rows_t.append([n, str(z), str(mp), str(bp)])
    tb = table(["Element", "Atomic number", "Melting point in °C", "Boiling point in °C"], rows_t)
    hn = data[hide][0]
    parts = [P("a", "Describe the trend in boiling point down the group.", 1, lines=2)]
    rows = [row("a", "increases (down the group)", 1, None, "AO3")]
    if hide < 4:
        lo = data[hide - 1][3] + 1
        hi = data[hide + 1][3] - 1 if hide + 1 < 4 else 250
        parts.append(P("b", f"Predict the boiling point of {hn}.", 1, lines=1))
        rows.append(row("b", f"any value from {lo} to {hi} °C", 1, f"actual value {data[hide][3]} °C", "AO3"))
    parts.append(P("c", "Predict the state of astatine at room temperature. Explain your answer.", 2, lines=3))
    rows += [row("c", "M1 solid", 1, None, "AO3"), row("c", "M2 melting point would be above room temperature / higher than iodine's (114 °C)", 1, None, "AO3")]
    t_ = r.choice([-50, 0, 30, 100])
    states = []
    for n, z, mp, bp in data[:4]:
        states.append((n, "solid" if t_ < mp else ("liquid" if t_ < bp else "gas")))
    who = r.choice(states)
    parts.append(P("d", f"Give the state of {who[0]} at {t_} °C.", 1, lines=1))
    rows.append(row("d", who[1], 1, None, "AO3"))
    return Q("Predict", "4-6", parts, rows, ["2.6", "2.5"], figs=[tb], intro="The table gives information about the halogens.",
             ans=("trend", {"state": who[1]}), ao=["AO3"])


# =================================================================== 2(c) gases in the atmosphere
facts(AI, "2.9", [
    D(mq="What is the approximate percentage of nitrogen in dry air?", c="78%", w=["21%", "1%", "0.04%"]),
    D(mq="What is the approximate percentage of oxygen in dry air?", c="21%", w=["78%", "1%", "50%"]),
    D(mq="Which gas makes up about 0.9% of dry air?", c="argon", w=["carbon dioxide", "oxygen", "nitrogen"]),
    D(mq="What colour is the flame when magnesium burns in oxygen?", c="bright white", w=["blue", "lilac", "yellow"], ref="2.11"),
    D(mq="What is the colour of the flame when sulfur burns in oxygen?", c="blue", w=["bright white", "orange", "green"], ref="2.11", d="4-6"),
    D(mq="Sulfur dioxide dissolves in water containing universal indicator. What colour does the indicator turn?", c="red / orange",
      w=["purple", "green", "blue"], ref="2.11", d="4-6"),
    D(mq="What forms when copper(II) carbonate is heated strongly?", c="copper(II) oxide and carbon dioxide", w=["copper and carbon dioxide",
      "copper(II) oxide and oxygen", "copper and oxygen"], ref="2.12"),
    D(mq="What colour change is seen when green copper(II) carbonate is heated?", c="green to black", w=["blue to white", "black to green", "white to yellow"], ref="2.12"),
    D(mq="Which gas is a greenhouse gas?", c="carbon dioxide", w=["nitrogen", "oxygen", "argon"], ref="2.13"),
    D(mq="Which statement about the effect of rising carbon dioxide levels is correct?", c="they may lead to climate change", w=["they destroy the ozone layer",
      "they make rain alkaline", "they reduce the temperature of the Earth"], ref="2.13"),
    D(mq="What is the approximate percentage of carbon dioxide in dry air?", c="0.04%", w=["4%", "21%", "1%"], d="4-6"),
    D(mq="Hydrogen burns in oxygen. What is the product?", c="water", w=["hydrogen peroxide", "hydrogen oxide gas only", "carbon dioxide"], ref="2.11"),
], intro="This question is about the gases in the atmosphere.")

facts(AI, "2.9", [
    D(q="Give the approximate percentages of nitrogen and oxygen in dry air.", m=2, pts=["nitrogen 78%", "oxygen 21%"]),
    D(q="Name the noble gas that is present in the air in the largest amount.", a="argon"),
    D(q="Give the name of the product formed when magnesium burns in air.", a="magnesium oxide", ref="2.11"),
    D(q="Name the gas produced when calcium carbonate is decomposed by heating.", a="carbon dioxide", ref="2.12"),
    D(q="State the name of this type of reaction, in which a single compound breaks down on heating.", a="thermal decomposition", ref="2.12"),
    D(q="Give one way in which human activity increases the amount of carbon dioxide in the air.", a="burning fossil fuels / deforestation", ref="2.13"),
    D(q="Give one possible effect of climate change.", a="rising sea levels / flooding / melting ice caps / extreme weather / changes to habitats", ref="2.13"),
    D(q="Describe the appearance of the product when magnesium burns.", a="white powder / solid", ref="2.11"),
    D(q="Give the type of oxide formed when sulfur burns, and the effect on pH when it dissolves.", m=2, pts=["acidic oxide", "lowers pH / pH below 7"], ref="2.11", d="4-6"),
    D(q="Explain why greenhouse gases keep the Earth warm.", m=2, pts=["they absorb (infrared / heat) radiation emitted from the Earth", "and re-emit it, so less escapes to space"], ref="2.13", d="7-9"),
], intro="This question is about air and combustion.")

items(AI, "describe", "2.11", [
    D(s="Describe what you would see when magnesium ribbon burns in air.", m=2, p=["very bright white flame / light", "white powder / ash forms"]),
    D(s="Describe what you would see when sulfur is burned in a gas jar of oxygen.", m=2, p=["sulfur melts / burns with a blue flame", "choking / pungent gas / fumes form"]),
    D(s="Describe how hydrogen burns in air and how you could show that the product is water.", m=3,
      p=["burns with a (pale) blue flame / squeaky pop", "product condenses as a colourless liquid", "turns anhydrous copper(II) sulfate from white to blue"], ref=["2.11", "2.49"], d="4-6"),
    D(s="Describe how you could show that copper(II) carbonate gives off carbon dioxide when heated.", m=3,
      p=["heat in a boiling tube fitted with a delivery tube", "bubble the gas through limewater", "limewater turns milky / cloudy"], ref="2.12"),
    D(s="Describe how you could compare the acidity of the oxides formed when magnesium and sulfur burn.", m=3,
      p=["dissolve / shake each oxide with water", "add universal indicator", "magnesium oxide gives blue/purple (alkaline), sulfur dioxide gives red/orange (acidic)"], d="7-9"),
    D(s="Describe the trend in the amount of carbon dioxide in the atmosphere over the last 150 years and give one reason for it.", m=2,
      p=["it has increased", "more fossil fuels burned / deforestation"], ref="2.13"),
    D(s="Describe how the greenhouse effect warms the Earth.", m=3,
      p=["the Sun's radiation warms the Earth's surface", "the Earth emits infrared radiation", "greenhouse gases absorb it and re-emit some back to the Earth"], ref="2.13", d="7-9"),
    D(s="Describe what happens when a lit splint is put into a test tube of hydrogen and air.", m=2, p=["squeaky pop", "hydrogen reacts with oxygen (to form water)"], ref="2.11"),
    D(s="Describe how the appearance of zinc carbonate changes when it is heated strongly and then cooled.", m=2,
      p=["white solid turns yellow when hot (zinc oxide)", "turns white again on cooling"], ref="2.12", d="7-9"),
    D(s="Describe how to carry out a fair comparison of how easily two metal carbonates decompose.", m=3,
      p=["same mass of each carbonate", "same heating (Bunsen flame) and same volume of limewater", "time how long until limewater turns milky"], ref="2.12", d="7-9"),
])

AI_EQ = [("magnesium + oxygen → magnesium oxide", "2Mg(s) + O2(g) -> 2MgO(s)"),
         ("hydrogen + oxygen → water", "2H2(g) + O2(g) -> 2H2O(l)"),
         ("sulfur + oxygen → sulfur dioxide", "S(s) + O2(g) -> SO2(g)"),
         ("carbon + oxygen → carbon dioxide", "C(s) + O2(g) -> CO2(g)"),
         ("copper(II) carbonate → copper(II) oxide + carbon dioxide", "CuCO3(s) -> CuO(s) + CO2(g)"),
         ("calcium carbonate → calcium oxide + carbon dioxide", "CaCO3(s) -> CaO(s) + CO2(g)"),
         ("zinc carbonate → zinc oxide + carbon dioxide", "ZnCO3(s) -> ZnO(s) + CO2(g)"),
         ("magnesium carbonate → magnesium oxide + carbon dioxide", "MgCO3(s) -> MgO(s) + CO2(g)"),
         ("copper + oxygen → copper(II) oxide", "2Cu(s) + O2(g) -> 2CuO(s)"),
         ("iron + oxygen → iron(III) oxide", "4Fe(s) + 3O2(g) -> 2Fe2O3(s)"),
         ("phosphorus + oxygen → phosphorus(V) oxide", "4P(s) + 5O2(g) -> P4O10(s)"),
         ("sulfur dioxide + water → sulfurous acid", "SO2(g) + H2O(l) -> H2SO3(aq)"),
         ("calcium + oxygen → calcium oxide", "2Ca(s) + O2(g) -> 2CaO(s)"),
         ("sodium hydrogencarbonate → sodium carbonate + water + carbon dioxide", "2NaHCO3(s) -> Na2CO3(s) + H2O(l) + CO2(g)")]


@tpl(AI, "equation", 26)
def air_equations(r, k):
    word, sym = AI_EQ[k % len(AI_EQ)]
    mode = [0, 2, 1][(k // len(AI_EQ)) % 3]
    return eq_q(word, sym, ["2.12"] if "carbonate" in word else ["2.11"], d="4-6", mode=mode)


@tpl(AI, "calculation", 18)
def air_oxygen_calc(r, k):
    kind = k % 3
    if kind == 0:
        v0 = r.choice([80, 90, 100, 95, 120, 150])
        frac = Fr(r.choice([19, 20, 21, 22]), 100)
        v1 = round(v0 * (1 - frac), 1)
        pct = (v0 - v1) / v0 * 100
        stem = (f"A student passes {v0} cm³ of air backwards and forwards over heated copper until the volume stops changing. "
                f"When cool, the final volume of gas is {num(v1)} cm³.\n\nCalculate the percentage of oxygen in this sample of air. "
                "Give your answer to 3 significant figures.")
        rows = [row("", f"M1 {v0} − {num(v1)} = {num(round(v0 - v1, 1))} cm³ (oxygen used)", 1, None, "AO2"),
                row("", f"M2 {num(round(v0 - v1, 1))} ÷ {v0} × 100", 1, None, "AO2"),
                row("", f"M3 {num(pct, sf=3)} %", 1, "ALLOW ecf", "AO2")]
        return Q("Calculate", "4-6", [P("", stem, 3, space="working", answer_prefix="percentage = ", lines=6)], rows, ["2.10", "2.14"],
                 figs=[fig(S.iron_wool_syringes(), 120, caption="Apparatus (not to scale)")] if r.random() < 0.3 else None,
                 ans=("(v0-v1)/v0", {"percent": float(num(pct, sf=3))}), ao=["AO2"])
    if kind == 1:
        h0 = r.choice([100, 120, 150, 160, 200])
        frac = Fr(r.choice([18, 19, 20, 21]), 100)
        days = [0, 1, 2, 3, 4, 5, 6]
        vals = []
        for d in days:
            vals.append(round(h0 * (1 - float(frac) * (1 - 0.5 ** (d * 1.2))), 0))
        vals[-1] = vals[-2]
        tb = table(["Day"] + [str(d) for d in days], [["Volume of air in cm³"] + [num(v) for v in vals]])
        pct = (h0 - vals[-1]) / h0 * 100
        parts = [P("a", "Explain why the volume stops changing after a few days.", 2, lines=3),
                 P("b", "Calculate the percentage of oxygen in the air. Give your answer to 2 significant figures.", 2, space="working",
                   answer_prefix="percentage = ", lines=4)]
        rows = [row("a", "M1 all the oxygen has reacted / been used up", 1, None, "AO3"),
                row("a", "M2 (iron) rusting uses oxygen; nitrogen/other gases do not react", 1, None, "AO3"),
                row("b", f"M1 ({h0} − {num(vals[-1])}) ÷ {h0} × 100", 1, None, "AO2"),
                row("b", f"M2 {num(pct, sf=2)} %", 1, None, "AO2")]
        return Q("Calculate", "4-6", parts, rows, ["2.10", "2.14"], figs=[tb],
                 intro=f"Damp iron wool is placed in a tube containing {h0} cm³ of air, sealed over water. The table shows the volume of air each day.",
                 ans=("(h0-vf)/h0", {"percent": float(num(pct, sf=2))}), ao=["AO2", "AO3"])
    # kind 2: mass of CO2 from carbonate decomposition
    carb = r.choice(["CuCO3", "CaCO3", "ZnCO3", "MgCO3"])
    oxide = carb.replace("CO3", "O")
    m = r.choice([2.47, 5.00, 6.25, 10.0, 4.20, 1.25, 12.5, 3.08])
    n = Fr(str(m)) / Mr(carb)
    loss = n * 44
    stem = (f"A student heats {num(m)} g of {F(carb)} until it has completely decomposed.\n\n{EQ(f'{carb}(s) -> {oxide}(s) + CO2(g)')}\n\n"
            f"Calculate the loss in mass. Give your answer to 3 significant figures. [Mr: {F(carb)} = {num(Mr(carb))}, CO₂ = 44]")
    rows = [row("", f"M1 moles {F(carb)} = {num(m)} ÷ {num(Mr(carb))} = {num(float(n), sf=3)}", 1, None, "AO2"),
            row("", "M2 moles CO₂ = moles carbonate (1 : 1)", 1, None, "AO2"),
            row("", f"M3 mass CO₂ lost = {num(float(n), sf=3)} × 44 = {num(float(loss), sf=3)} g", 1, "ALLOW ecf", "AO2")]
    return Q("Calculate", "7-9", [P("", stem, 3, space="working", answer_prefix="loss in mass = ", lines=6)], rows, ["2.12", "1.29"],
             ans=("n×44", {"loss_g": float(num(float(loss), sf=3))}), ao=["AO2"])


items(AI, "practical", "2.14", [
    D(intro="Two gas syringes are joined by a tube packed with copper powder. 100 cm³ of air is pushed back and forth over the heated copper.",
      figs=[fig(S.iron_wool_syringes(), 120, caption="Apparatus")],
      s="Explain why the gas is passed over the copper many times and allowed to cool before measuring the final volume.", m=3,
      p=["so all the oxygen reacts with the copper", "gas expands when hot", "so volume must be measured at room temperature for a fair comparison"], d="7-9"),
    D(s="State what you would see happen to the copper powder in the experiment to find the percentage of oxygen in air.", m=1, p=["pink-brown copper turns black"], d="4-6"),
    D(s="Give two reasons why the measured percentage of oxygen might be lower than 21%.", m=2,
      p=["not all the oxygen reacted (not enough copper / passes)", "gas still warm when measured / leak in apparatus", "copper coated with oxide so stops reacting"], any=True, d="7-9"),
    D(s="Describe how damp iron wool can be used to find the percentage of oxygen in air.", m=4,
      p=["put damp iron wool at the top of a measuring cylinder / graduated tube", "invert in a trough of water and record the initial volume of air",
         "leave for several days until the water level stops rising", "measure the final volume; % = decrease ÷ initial volume × 100"], d="7-9"),
    D(s="Explain why the water rises up the tube in the iron wool experiment.", m=2, p=["oxygen is used up as the iron rusts", "water rises to take its place / pressure inside falls"], d="4-6"),
    D(s="Suggest why the iron wool must be damp.", m=1, p=["rusting needs water (as well as oxygen)"], ref="2.18", d="1-3"),
    D(s="Suggest one advantage of using phosphorus rather than iron wool to remove oxygen from a sample of air.", m=1, p=["reacts much faster (results in minutes not days)"], d="7-9"),
    D(s="Suggest why the level of water inside and outside the tube should be the same when each volume is read.", m=2,
      p=["so the gas is at atmospheric pressure", "so the volume readings are comparable"], d="7-9"),
    D(s="State why the volume of gas left at the end of the experiment does not fall to zero.", m=1, p=["nitrogen / argon / other gases in air do not react"], d="4-6"),
    D(s="A student finds that the percentage of oxygen in air is 25%. Suggest one error that could cause a result that is too high.", m=1,
      p=["gas measured while still cold / temperature lower at end", "misreading the initial volume / gas leaked out"], any=True, d="7-9"),
    D(s="Give one safety precaution when heating copper in a stream of air in a tube.", m=1, p=["clamp the tube / do not touch hot glass / eye protection"], d="1-3"),
    D(s="Describe how to collect a sample of the gas given off when a metal carbonate is heated, so that its volume can be measured.", m=2,
      p=["delivery tube from the heated tube to a gas syringe / inverted measuring cylinder over water", "read the volume when no more gas is produced"], ref="2.12", d="4-6"),
])


# =================================================================== 2(d) reactivity series
SERIES = ["potassium", "sodium", "lithium", "calcium", "magnesium", "aluminium", "zinc", "iron", "copper", "silver", "gold"]
SYM = {"potassium": "K", "sodium": "Na", "lithium": "Li", "calcium": "Ca", "magnesium": "Mg", "aluminium": "Al", "zinc": "Zn", "iron": "Fe",
       "copper": "Cu", "silver": "Ag", "gold": "Au"}

facts(RE, "2.15", [
    D(mq="Which metal is the most reactive?", c="magnesium", w=["zinc", "iron", "copper"], ref="2.17"),
    D(mq="Which metal does not react with dilute hydrochloric acid?", c="copper", w=["zinc", "magnesium", "iron"]),
    D(mq="What are the two conditions needed for iron to rust?", c="water and oxygen", w=["water and carbon dioxide", "oxygen only", "salt and heat"], ref="2.18"),
    D(mq="Galvanising protects iron by coating it with", c="zinc", w=["tin", "copper", "paint"], ref="2.19"),
    D(mq="What is reduction in terms of oxygen?", c="loss of oxygen", w=["gain of oxygen", "gain of hydrogen ions", "loss of electrons"], ref="2.20"),
    D(mq="In which mixture will a reaction take place?", c="zinc and copper(II) sulfate solution", w=["copper and zinc sulfate solution",
      "iron and magnesium sulfate solution", "silver and copper(II) nitrate solution"], ref="2.16", d="4-6"),
    D(mq="Why does zinc protect iron even when the zinc coating is scratched?", c="zinc is more reactive so it corrodes instead of iron",
      w=["zinc is less reactive than iron", "zinc stops water reaching the iron", "zinc reacts with the rust"], ref="2.19", d="7-9"),
    D(mq="What is the formula of rust?", c="Fe2O3·xH2O", w=["FeO", "Fe(OH)2", "FeCO3"], ref="2.18", d="4-6"),
    D(mq="In Fe₂O₃ + 2Al → Al₂O₃ + 2Fe, which substance is the reducing agent?", c="Al", w=["Fe2O3", "Al2O3", "Fe"], ref="2.20", d="7-9"),
    D(mq="Which statement describes oxidation in terms of electrons?", c="loss of electrons", w=["gain of electrons", "gain of protons", "loss of neutrons"], ref="2.20"),
    D(mq="Which method of rust prevention is sacrificial protection?", c="attaching blocks of magnesium to a steel hull", w=["painting a bridge",
      "oiling a bicycle chain", "coating a car in plastic"], ref="2.19", d="4-6"),
    D(mq="A metal X displaces copper from copper(II) sulfate solution but does not displace zinc from zinc sulfate. Which could X be?", c="iron",
      w=["magnesium", "silver", "gold"], ref="2.16", d="7-9"),
    D(mq="Which metal reacts with cold water to give a gas?", c="calcium", w=["zinc", "copper", "iron"], ref="2.15"),
], intro="This question is about the reactivity of metals.")

facts(RE, "2.15", [
    D(q="State what is meant by **oxidation** in terms of electrons.", a="loss of electrons", n="ALLOW gain of oxygen if electrons not asked", ref="2.20"),
    D(q="State what is meant by a **redox** reaction.", a="a reaction in which oxidation and reduction both take place", ref="2.20"),
    D(q="Name the two substances that must be present for iron to rust.", m=2, pts=["water", "oxygen"], ref="2.18"),
    D(q="Give two ways of preventing iron from rusting by forming a barrier.", m=2, pts=["painting", "oiling / greasing", "coating with plastic", "galvanising / plating"], ref="2.19"),
    D(q="Name a metal that could be used for the sacrificial protection of steel.", a="zinc / magnesium", ref="2.19"),
    D(q="State what is meant by an **oxidising agent**.", a="a substance that oxidises another substance / accepts electrons (and is itself reduced)", ref="2.20", d="4-6"),
    D(q="Name the gas produced when calcium reacts with water.", a="hydrogen"),
    D(q="Name the products when zinc reacts with copper(II) sulfate solution.", m=2, pts=["zinc sulfate", "copper"], ref="2.16"),
    D(q="Give the colour change seen when magnesium is added to copper(II) sulfate solution.", a="blue to colourless (pink-brown solid forms)", ref="2.16", d="4-6"),
    D(q="State one reason why gold is found uncombined in the Earth.", a="it is very unreactive", ref="2.22C"),
    D(q="Name the type of reaction in which a more reactive metal takes the place of a less reactive metal in a compound.", a="displacement", ref="2.16"),
], intro="This question is about reactivity, rusting and redox.")

items(RE, "explain", "2.16", [
    D(s="Explain why a reaction occurs when {a} is added to {b} solution.", m=2, p=["{a} is more reactive than {c}", "so it displaces {c} from its compound"],
      v=[{"a": "magnesium", "b": "zinc sulfate", "c": "zinc"}, {"a": "iron", "b": "copper(II) sulfate", "c": "copper"},
         {"a": "copper", "b": "silver nitrate", "c": "silver"}, {"a": "zinc", "b": "iron(II) sulfate", "c": "iron"}]),
    D(s="Explain why no reaction occurs when copper is added to magnesium sulfate solution.", m=2, p=["copper is less reactive than magnesium", "so it cannot displace magnesium"]),
    D(s="Explain why galvanised iron does not rust even when the zinc coating is scratched.", m=3,
      p=["zinc is more reactive than iron", "zinc loses electrons / is oxidised in preference", "sacrificial protection: iron does not oxidise"], ref="2.19", d="7-9"),
    D(s="Explain why painting a steel gate prevents it from rusting.", m=2, p=["paint forms a barrier", "keeps out water and/or oxygen"], ref="2.19"),
    D(s="Explain, in terms of electrons, why the reaction between magnesium and copper(II) ions is a redox reaction.", m=3,
      p=["magnesium atoms lose two electrons (oxidised)", "copper(II) ions gain two electrons (reduced)", "both happen together"], ref="2.20", d="7-9"),
    D(s="Explain why the temperature rise is greater when magnesium is added to copper(II) sulfate than when iron is added.", m=2,
      p=["magnesium is more reactive than iron", "the bigger the difference in reactivity, the more energy released"], d="7-9"),
    D(s="Explain why a nail in a test tube of boiled water with a layer of oil on top does not rust.", m=2,
      p=["boiling removes dissolved air / oxygen", "oil stops air dissolving back in"], ref="2.18", d="4-6"),
    D(s="Explain why aluminium appears to be less reactive than its position in the reactivity series suggests.", m=2,
      p=["aluminium is coated with a layer of aluminium oxide", "which stops it reacting"], d="7-9"),
    D(s="Explain why carbon can be used to extract zinc from zinc oxide.", m=2, p=["carbon is more reactive than zinc", "so carbon removes oxygen from zinc oxide / reduces it"], ref="2.16", d="4-6"),
    D(s="Explain why salt water makes cars rust faster.", m=2, p=["salt solution conducts / contains ions", "speeds up the transfer of electrons in rusting"], ref="2.18", d="7-9"),
    D(s="Explain why the thermite reaction between aluminium and iron(III) oxide is a redox reaction.", m=2,
      p=["aluminium gains oxygen / is oxidised", "iron(III) oxide loses oxygen / is reduced"], ref="2.20", d="4-6"),
])

DISP = [("Mg", "Cu", 2, 2), ("Zn", "Cu", 2, 2), ("Fe", "Cu", 2, 2), ("Mg", "Zn", 2, 2), ("Cu", "Ag", 2, 1), ("Zn", "Fe", 2, 2),
        ("Mg", "Fe", 2, 2), ("Al", "Cu", 3, 2), ("Zn", "Ag", 2, 1), ("Mg", "Ag", 2, 1), ("Fe", "Ag", 2, 1), ("Al", "Zn", 3, 2)]
NM = {v: k for k, v in SYM.items()}


def _disp_eq(a, b, qa, qb):
    if qa == qb:
        return f"{a}(s) + {b}^2+(aq) -> {a}^2+(aq) + {b}(s)"
    if (qa, qb) == (2, 1):
        return f"{a}(s) + 2{b}^+(aq) -> {a}^2+(aq) + 2{b}(s)"
    return f"2{a}(s) + 3{b}^2+(aq) -> 2{a}^3+(aq) + 3{b}(s)"


@tpl(RE, "equation", 24)
def reactivity_displacement_eq(r, k):
    a, b, qa, qb = DISP[k % len(DISP)]
    ion = _disp_eq(a, b, qa, qb)
    salt = {"Cu": ("copper(II) sulfate", "CuSO4"), "Zn": ("zinc sulfate", "ZnSO4"), "Fe": ("iron(II) sulfate", "FeSO4"), "Ag": ("silver nitrate", "AgNO3")}[b]
    if (k // len(DISP)) % 2 == 0:
        prod = {"Mg": "magnesium", "Zn": "zinc", "Fe": "iron(II)", "Cu": "copper(II)", "Al": "aluminium"}[a]
        anion = "sulfate" if b != "Ag" else "nitrate"
        if b == "Ag":
            full = {"Cu": "Cu(s) + 2AgNO3(aq) -> Cu(NO3)2(aq) + 2Ag(s)", "Zn": "Zn(s) + 2AgNO3(aq) -> Zn(NO3)2(aq) + 2Ag(s)",
                    "Mg": "Mg(s) + 2AgNO3(aq) -> Mg(NO3)2(aq) + 2Ag(s)", "Fe": "Fe(s) + 2AgNO3(aq) -> Fe(NO3)2(aq) + 2Ag(s)"}[a]
        elif a == "Al":
            full = f"2Al(s) + 3{salt[1]}(aq) -> Al2(SO4)3(aq) + 3{b}(s)"
        else:
            full = f"{a}(s) + {salt[1]}(aq) -> {a}SO4(aq) + {b}(s)"
        word = f"{NM[a]} + {salt[0]} → {prod} {anion} + {NM[b]}"
        return eq_q(word, full, ["2.16"], d="7-9" if a == "Al" or b == "Ag" else "4-6", mode=0)
    parts = [P("a", f"Write the ionic equation for the reaction of {NM[a]} with {salt[0]} solution.", 2, lines=2),
             P("b", "State which species is oxidised. Give a reason.", 2, lines=3)]
    rows = [row("a", f"M1 correct species: {F(a)}, {F(b + ('^+' if qb == 1 else '^2+'))}, {F(a + ('^3+' if qa == 3 else '^2+'))}, {F(b)}", 1,
                "IGNORE state symbols; IGNORE spectator ions only if cancelled", "AO2"),
            row("a", f"M2 balanced: {EQ(ion, states=False)}", 1, "charge must balance", "AO2"),
            row("b", f"M1 {F(a)} / {NM[a]} (atoms)", 1, None, "AO2"), row("b", "M2 loses electrons", 1, None, "AO2")]
    return Q("Write", "7-9", parts, rows, ["2.16", "2.20"], ao=["AO2"], ans=("ionic", {"ionic": EQ(ion)}))


items(RE, "practical", "2.21", [
    D(s="Describe how you could use dilute hydrochloric acid to put magnesium, zinc and iron in order of reactivity.", m=4,
      p=["add the same mass / size of each metal to the same volume and concentration of acid", "same temperature / same surface area (powder or ribbon)",
         "observe the rate of bubbling / measure temperature rise / volume of gas in a set time", "fastest bubbling / largest temperature rise = most reactive"], d="7-9"),
    D(s="Give two variables that must be controlled when comparing the reactions of metals with dilute acid.", m=2,
      p=["volume of acid", "concentration of acid", "mass / surface area of metal", "starting temperature"], any=True, d="4-6"),
    D(s="Suggest why measuring the temperature rise gives a better comparison of reactivity than watching the bubbles.", m=2,
      p=["it gives a numerical / quantitative result", "observation of bubbles is subjective / hard to judge"], d="7-9"),
    D(s="Suggest why the metals should be cleaned with emery paper before the experiment.", m=1, p=["to remove the oxide layer (so the metal reacts directly)"], d="4-6"),
    D(intro="A student adds metal powders to copper(II) sulfate solution in a polystyrene cup and records the temperature rise.",
      s="Explain why a polystyrene cup is used and why the powder is added in excess.", m=2,
      p=["polystyrene is an insulator so reduces heat loss", "excess metal ensures all the copper(II) sulfate reacts (same amount reacts each time)"], d="7-9"),
    D(s="Describe how you would set up an experiment to show that both air and water are needed for rusting.", m=4,
      p=["nail in a test tube with tap water and air (rusts)", "nail in boiled water with oil layer (no air)", "nail in a tube with anhydrous calcium chloride (dry air)",
         "leave for several days and compare"], ref="2.18", d="7-9"),
    D(s="State the purpose of the anhydrous calcium chloride in an experiment on rusting.", m=1, p=["to absorb water / keep the air dry"], ref="2.18", d="4-6"),
    D(s="State the purpose of the layer of oil in a rusting experiment.", m=1, p=["stops air / oxygen dissolving in the water"], ref="2.18"),
    D(s="Give one safety precaution when reacting metals with dilute acids.", m=1, p=["eye protection", "no naked flames near hydrogen", "small amounts"], any=True, d="1-3"),
    D(s="Explain why a student should use metal powders of the same particle size in a displacement experiment.", m=2,
      p=["surface area affects the rate (and hence the observed temperature rise)", "so differences are due only to the metal used"], d="7-9"),
    D(s="Describe what you would see when iron filings are added to copper(II) sulfate solution.", m=2, p=["blue colour fades / turns pale green", "pink-brown solid forms"], d="4-6"),
    D(s="Suggest how the results of a metal–acid reactivity experiment could be made more reliable.", m=1, p=["repeat each test and calculate a mean"], d="1-3"),
])


@tpl(RE, "data", 16)
def reactivity_temp_data(r, k):
    metals = ["magnesium", "zinc", "iron", "copper", "tin", "nickel"]
    order = {"magnesium": 1, "zinc": 3, "iron": 4, "tin": 5, "nickel": 4.5, "copper": 7, "silver": 8}
    solns = [("copper(II) sulfate", "copper", 7), ("silver nitrate", "silver", 8)]
    sol, sm, so = solns[k % 2]
    ms = r.sample([m for m in metals if m != sm], 4)
    base = r.choice([18.5, 19.0, 20.0, 21.5, 22.0])
    rows_t, rises = [], {}
    for m in ms:
        diff = so - order[m]
        rise = round(max(0.0, diff) * r.uniform(5.5, 6.5), 1) if diff > 0 else 0.0
        rises[m] = rise
        rows_t.append([m, f"{base:.1f}", f"{base + rise:.1f}", "[[blank]]" if r.random() < 0.3 else f"{rise:.1f}"])
    tb = table(["Metal", "Start temperature in °C", "Highest temperature in °C", "Temperature rise in °C"], rows_t)
    rank = sorted(ms, key=lambda m: -rises[m])
    parts = [P("a", "Complete the table.", 1, space="table"),
             P("b", "Use the results to place the metals in order of reactivity, most reactive first.", 2, lines=2),
             P("c", "Explain why one metal gave no temperature rise." if 0.0 in rises.values() else
                    "Explain why all the metals gave a temperature rise.", 2, lines=3)]
    no = [m for m in ms if rises[m] == 0.0]
    rows = [row("a", "all blank rises correctly calculated (highest − start)", 1, None, "AO3"),
            row("b", " > ".join(rank), 2, "1 mark if one pair reversed", "AO3"),
            row("c", (f"M1 {no[0]} is less reactive than {sm}" if no else f"M1 all are more reactive than {sm}"), 1, None, "AO3"),
            row("c", "M2 so no displacement / no reaction" if no else "M2 so each displaces it and gives out heat", 1, None, "AO3")]
    if not any("[[blank]]" in x for x in sum(rows_t, [])):
        parts = parts[1:]
        rows = rows[1:]
    return Q("Use", "4-6", parts, rows, ["2.15", "2.16"], figs=[tb],
             intro=f"A student adds an excess of four metal powders, one at a time, to 25 cm³ of {sol} solution and measures the temperature rise.",
             ans=("rank", {"order": rank, "rises": rises}), ao=["AO3"])


extended(RE, "2.18", [
    D(s="Describe an investigation to show that iron needs both oxygen and water to rust. Include the expected results.",
      ind=["three (or more) test tubes each with an iron nail", "tube A: nail in tap water open to air – rusts", "tube B: nail in boiled water with an oil layer – no air – no rust",
           "tube C: nail in dry air with anhydrous calcium chloride and a bung – no water – no rust", "leave for about a week", "compare: only nail with both water and air rusts",
           "control variables: same type/size of nail, same temperature"], ao="AO1 2, AO3 4"),
    D(s="Explain the different methods of preventing iron and steel from rusting. Include barrier methods and sacrificial protection.",
      ind=["rusting needs oxygen and water", "barrier: paint, oil, grease, plastic coating keep out air and water", "examples: oil on bicycle chains, paint on bridges",
           "galvanising: coat with zinc (barrier and sacrificial)", "sacrificial: attach more reactive metal (zinc/magnesium)", "more reactive metal loses electrons / is oxidised instead of iron",
           "works even if coating damaged; blocks need replacing"], ref=["2.18", "2.19"]),
    D(s="Describe how displacement reactions can be used to find the order of reactivity of magnesium, zinc, copper and a metal X.",
      ind=["add each metal to solutions of the salts of the others", "use small pieces / powder and equal volumes and concentrations", "look for a coating of metal / colour change / temperature rise",
           "a reaction means the added metal is more reactive", "count the number of reactions for each metal", "most reactions = most reactive", "e.g. magnesium displaces all; copper displaces none"], ref=["2.16", "2.21"]),
    D(s="Explain, using examples, how oxidation and reduction can be defined in terms of oxygen and in terms of electrons.",
      ind=["oxidation is gain of oxygen; reduction is loss of oxygen", "e.g. CuO + H₂ → Cu + H₂O: CuO reduced, H₂ oxidised", "oxidation is loss of electrons; reduction is gain of electrons",
           "e.g. Mg + Cu²⁺ → Mg²⁺ + Cu: Mg loses electrons, Cu²⁺ gains electrons", "redox = both at once", "oxidising agent accepts electrons; reducing agent donates electrons"], ref="2.20", d="7-9"),
    D(intro="A student is given three unlabelled metals: magnesium, zinc and copper. She also has dilute hydrochloric acid.",
      s="Describe how she could identify each metal using the acid. Explain the expected observations.",
      ind=["add a small piece of each metal to separate tubes of the same volume and concentration of acid", "same size pieces / same temperature",
           "magnesium: vigorous fizzing, gets warm, dissolves quickly", "zinc: slower bubbling", "copper: no reaction / no bubbles",
           "explanation: reactivity order Mg > Zn > H > Cu", "test gas: squeaky pop shows hydrogen"], ref=["2.15", "2.21"], d="4-6"),
    D(s="Describe and explain what you would observe when an iron nail is placed in copper(II) sulfate solution and left for an hour.",
      ind=["pink-brown / copper-coloured coating forms on the nail", "blue colour of solution fades", "solution becomes pale green (iron(II) sulfate)", "nail gets thinner over time",
           "iron is more reactive than copper so displaces it", "Fe + CuSO₄ → FeSO₄ + Cu", "iron is oxidised (loses electrons); copper ions reduced"], ref=["2.16", "2.20"], d="4-6"),
])

extended(RE, "2.18", [
    D(s="A metal X reacts slowly with dilute hydrochloric acid, does not react with cold water, and displaces copper but not zinc from solutions of their salts. "
        "Deduce where X is in the reactivity series and explain your reasoning, suggesting further tests to confirm it.",
      ind=["X reacts with acid so X is above hydrogen", "no reaction with cold water so below calcium/magnesium (less reactive)", "displaces copper so more reactive than copper",
           "does not displace zinc so less reactive than zinc", "so X lies between zinc and copper (e.g. iron / tin / lead)", "further test: add X to iron(II) sulfate / add iron to a salt of X",
           "compare temperature rises or rate of bubbling with iron under the same conditions"], ref=["2.15", "2.16"], d="7-9"),
    D(s="Describe how you could use temperature changes to compare the reactivity of zinc, iron and magnesium using copper(II) sulfate solution.",
      ind=["measure a fixed volume (e.g. 25 cm³) of copper(II) sulfate solution into a polystyrene cup", "record the starting temperature", "add an excess of metal powder (same mass/particle size)",
           "stir and record the highest temperature", "repeat for each metal with fresh solution", "larger temperature rise = more reactive metal", "expected order magnesium > zinc > iron"], ref=["2.16", "2.21"], d="4-6"),
    D(s="Iron objects such as ships, cars and bridges are protected from rusting in different ways. Explain the chemistry of rusting and evaluate the methods used for each object.",
      ind=["iron reacts with oxygen and water to form hydrated iron(III) oxide", "rusting is an oxidation: iron loses electrons", "salt water speeds up rusting (ships)",
           "ships: blocks of zinc/magnesium attached – sacrificial, works below the waterline", "cars: paint / galvanised panels – barrier plus sacrificial if scratched",
           "bridges: thick paint – cheap barrier but must be renewed if damaged", "oil/grease for moving parts like chains"], ref=["2.18", "2.19", "2.20"], d="7-9"),
    D(s="Explain, using the reactivity series, why some metals react with cold water, some react only with steam and some do not react with water at all. Give examples and word equations.",
      ind=["potassium, sodium, lithium, calcium react with cold water", "e.g. sodium + water → sodium hydroxide + hydrogen", "magnesium, zinc, iron react with steam",
           "e.g. magnesium + steam → magnesium oxide + hydrogen", "copper, silver, gold do not react with water or steam", "the more reactive the metal, the more easily it loses electrons / reacts",
           "metals above hydrogen can displace it from water"], ref=["2.15", "2.17"], d="4-6"),
    D(s="Describe how you could show which of two metals, P and Q, is more reactive using displacement reactions and using metal oxides. Explain each result.",
      ind=["add P to a solution of a salt of Q (and Q to a salt of P)", "a coating / colour change shows a reaction", "the metal that displaces the other is more reactive",
           "heat a mixture of P with the oxide of Q (and vice versa)", "a glow / reaction shows P takes the oxygen from Q's oxide", "this is a redox reaction: the more reactive metal is oxidised",
           "use small amounts and eye protection; control mass / particle size"], ref=["2.16", "2.20"], d="7-9"),
    D(s="Describe and explain the thermite reaction between aluminium and iron(III) oxide, including the type of reaction and a use.",
      ind=["mixture of aluminium powder and iron(III) oxide is ignited", "very exothermic: bright light, sparks, molten iron forms", "2Al + Fe₂O₃ → Al₂O₃ + 2Fe",
           "aluminium is more reactive than iron so takes the oxygen", "aluminium is oxidised; iron(III) oxide is reduced: redox", "aluminium is the reducing agent",
           "used to weld railway lines"], ref=["2.16", "2.20"], d="4-6"),
], tag="reactivity2")

# =================================================================== 2(e) extraction (C)
facts(EX, "2.22C", [
    D(mq="Which metal is extracted from its ore by electrolysis?", c="aluminium", w=["iron", "zinc", "copper"], ref="2.23C"),
    D(mq="Which metal is found uncombined in the Earth's crust?", c="gold", w=["sodium", "iron", "aluminium"]),
    D(mq="What is an ore?", c="a rock containing enough of a metal compound to make extraction worthwhile", w=["a pure metal", "any rock",
      "a mixture of metals"]),
    D(mq="Which element is used to reduce iron(III) oxide in the blast furnace?", c="carbon (as carbon monoxide)", w=["aluminium", "hydrogen", "sodium"], ref="2.23C"),
    D(mq="Why is aluminium used to make aircraft bodies?", c="it has low density and resists corrosion", w=["it is very dense", "it is magnetic", "it is the cheapest metal"], ref="2.25C"),
    D(mq="What is an alloy?", c="a mixture of a metal with one or more other elements", w=["a compound of two metals", "a pure metal",
      "a metal oxide"], ref="2.26C"),
    D(mq="Why are alloys harder than pure metals?", c="different sized atoms disrupt the layers so they cannot slide easily",
      w=["alloys contain ionic bonds", "the atoms in alloys are all the same size", "alloys have no delocalised electrons"], ref="2.27C", d="4-6"),
    D(mq="Why is copper used for water pipes?", c="it does not react with water", w=["it is very reactive", "it is a poor conductor", "it is magnetic"], ref="2.25C"),
    D(mq="Low-carbon (mild) steel is used for car bodies because it is", c="easily shaped", w=["very brittle", "very hard", "resistant to all corrosion"], ref="2.25C", d="4-6"),
    D(mq="Why can aluminium not be extracted by heating its oxide with carbon?", c="aluminium is more reactive than carbon", w=["carbon is more reactive than aluminium",
      "aluminium oxide does not contain oxygen", "aluminium has a low melting point"], ref="2.23C", d="4-6"),
    D(mq="Which property makes stainless steel suitable for cutlery?", c="it resists corrosion", w=["it is a good conductor", "it is very soft", "it is magnetic"], ref="2.25C"),
    D(mq="Which metals are extracted by heating their oxides with carbon?", c="metals below carbon in the reactivity series, such as zinc and iron",
      w=["metals above carbon, such as aluminium", "only gold and silver", "all metals"], ref="2.23C"),
], intro="This question is about extracting and using metals.")

facts(EX, "2.22C", [
    D(q="State why gold can be found as the element in the Earth's crust.", a="it is very unreactive"),
    D(q="Name the method used to extract metals more reactive than carbon.", a="electrolysis", ref="2.23C"),
    D(q="Name the method used to extract metals less reactive than carbon from their oxides.", a="heating with carbon / reduction with carbon", ref="2.23C"),
    D(q="Give one use of aluminium and the property that makes it suitable.", m=2, pts=["e.g. aircraft / drinks cans / overhead cables", "low density / resists corrosion / good conductor"], ref="2.25C"),
    D(q="Give one use of copper and the property that makes it suitable.", m=2, pts=["electrical wiring / water pipes", "good conductor / ductile / unreactive with water"], ref="2.25C"),
    D(q="State what is meant by an **alloy**.", a="a mixture of a metal with at least one other element", ref="2.26C"),
    D(q="Give one use of high-carbon steel and a reason for the use.", m=2, pts=["cutting tools / blades", "hard / strong"], ref="2.25C", d="4-6"),
    D(q="Name the gas that reduces iron(III) oxide in the blast furnace.", a="carbon monoxide", ref="2.23C", d="4-6"),
    D(q="Name the type of reaction when a metal oxide loses oxygen.", a="reduction"),
    D(q="Give one reason why recycling aluminium is better than extracting new aluminium.", a="uses less energy / saves ore / less mining / less waste", ref="2.23C", d="4-6"),
    D(q="Name the metal added to iron to make stainless steel.", a="chromium (and/or nickel)", ref="2.26C", d="4-6"),
], intro="This question is about metals and alloys.")

items(EX, "explain", "2.23C", [
    D(s="Explain why aluminium is extracted by electrolysis but iron is extracted by heating with carbon.", m=3,
      p=["aluminium is more reactive than carbon", "so carbon cannot reduce aluminium oxide", "iron is less reactive than carbon so carbon can remove the oxygen"]),
    D(s="Explain why extracting aluminium is expensive.", m=2, p=["electrolysis uses large amounts of electricity", "high temperature needed to melt the ore"], d="4-6"),
    D(s="Explain why an alloy of {m} is harder than pure {m}.", m=3, p=["atoms of the other element are a different size", "disrupt the regular layers of {m} atoms", "layers cannot slide over each other easily"],
      v=[{"m": "copper"}, {"m": "iron"}, {"m": "aluminium"}, {"m": "gold"}], ref="2.27C"),
    D(s="Explain why pure iron is soft.", m=2, p=["atoms are all the same size in regular layers", "layers slide over each other easily"], ref="2.27C"),
    D(s="Explain why aluminium is used for overhead power cables even though copper is a better conductor.", m=2, p=["aluminium has a lower density / is lighter", "so pylons can be further apart / need less support"], ref="2.25C", d="7-9"),
    D(s="Explain why the method used to extract a metal depends on its position in the reactivity series.", m=2,
      p=["metals more reactive than carbon need electrolysis", "metals less reactive than carbon can be reduced by carbon (cheaper)"]),
    D(s="Explain why silver and gold are found native but sodium is never found uncombined.", m=2, p=["silver and gold are very unreactive", "sodium is very reactive so is always combined in compounds"], ref="2.22C"),
    D(s="Explain why aluminium does not corrode even though it is a reactive metal.", m=2, p=["it forms a thin layer of aluminium oxide", "which stops air and water reaching the metal underneath"], ref="2.25C", d="7-9"),
    D(s="Explain why bronze (copper and tin) is used for statues rather than pure copper.", m=2, p=["harder / stronger", "resists corrosion"], ref="2.26C", d="4-6"),
    D(s="Explain why the extraction of iron from iron(III) oxide is a reduction.", m=2, p=["iron(III) oxide loses oxygen", "iron ions gain electrons"], d="7-9"),
])


@tpl(EX, "data", 14)
def extraction_data(r, k):
    metals = [("aluminium", "Al", 2.7, 660, "excellent", "very good", "electrolysis"), ("copper", "Cu", 8.9, 1085, "excellent", "good", "carbon / other"),
              ("iron", "Fe", 7.9, 1538, "good", "poor", "carbon"), ("titanium", "Ti", 4.5, 1668, "poor", "excellent", "via sodium / magnesium"),
              ("magnesium", "Mg", 1.7, 650, "good", "fair", "electrolysis"), ("lead", "Pb", 11.3, 327, "fair", "good", "carbon"),
              ("zinc", "Zn", 7.1, 420, "good", "good", "carbon"), ("gold", "Au", 19.3, 1064, "excellent", "excellent", "found native")]
    sel = r.sample(metals, 4)
    rows_t = [[m[0], str(m[2]), str(m[3]), m[4], m[5]] for m in sel]
    tb = table(["Metal", "Density in g/cm³", "Melting point in °C", "Electrical conductivity", "Resistance to corrosion"], rows_t)
    light = min(sel, key=lambda m: m[2])
    best = [m for m in sel if m[5] in ("excellent", "very good")]
    parts = [P("a", "Which metal would be most suitable for a part of an aircraft where low mass is important? Give a reason.", 2, lines=3),
             P("b", "Suggest which metal would be best for a roof that is exposed to rain for many years. Give a reason.", 2, lines=3),
             P("c", "Suggest why a steel bridge is painted but a gold ornament is not.", 2, lines=3)]
    rows = [row("a", f"M1 {light[0]}", 1, None, "AO3"), row("a", f"M2 lowest density ({light[2]} g/cm³)", 1, None, "AO3"),
            row("b", f"M1 {' or '.join(m[0] for m in best) if best else 'the metal with the best corrosion resistance'}", 1, None, "AO3"),
            row("b", "M2 high resistance to corrosion", 1, "ALLOW comment on cost / density for a sensible choice", "AO3"),
            row("c", "M1 iron (in steel) rusts / corrodes; paint keeps out air and water", 1, None, "AO2"),
            row("c", "M2 gold is very unreactive so does not corrode", 1, None, "AO2")]
    return Q("Suggest", "4-6", parts, rows, ["2.25C", "2.24C"], figs=[tb], intro="The table shows some properties of four metals.",
             ans=("lookup", {"lightest": light[0]}), ao=["AO3"])


# =================================================================== 2(f) acids, alkalis, titrations
facts(AC, "2.28", [
    D(mq="What colour is methyl orange in an alkaline solution?", c="yellow", w=["red", "colourless", "pink"]),
    D(mq="What colour is phenolphthalein in an acidic solution?", c="colourless", w=["pink", "yellow", "red"]),
    D(mq="What colour is phenolphthalein in an alkaline solution?", c="pink", w=["colourless", "yellow", "blue"]),
    D(mq="Which pH value shows a strongly acidic solution?", c="1", w=["6", "7", "13"], ref="2.29"),
    D(mq="Which ion is present in all acidic solutions?", c="H^+", w=["OH^-", "Cl^-", "Na^+"], ref="2.31"),
    D(mq="Which ion is present in all alkaline solutions?", c="OH^-", w=["H^+", "O^2-", "Na^+"], ref="2.31"),
    D(mq="What colour is universal indicator in a neutral solution?", c="green", w=["red", "purple", "yellow"], ref="2.30"),
    D(mq="Which piece of apparatus is used to add acid drop by drop in a titration?", c="burette", w=["pipette", "measuring cylinder", "conical flask"], ref="2.33C"),
    D(mq="Which piece of apparatus measures exactly 25.0 cm³ of alkali for a titration?", c="pipette", w=["burette", "beaker", "measuring cylinder"], ref="2.33C"),
    D(mq="What colour is red litmus in an alkali?", c="blue", w=["red", "colourless", "green"]),
    D(mq="What is the ionic equation for neutralisation?", c="H^+ + OH^- → H2O", w=["H^+ + Cl^- → HCl", "Na^+ + OH^- → NaOH", "2H^+ + O^2- → H2O2"], ref="2.32", d="4-6"),
    D(mq="Why is universal indicator not used in titrations?", c="its colour changes gradually, so there is no sharp end-point", w=["it is too expensive",
      "it reacts with the acid", "it only works with alkalis"], ref="2.33C", d="7-9"),
], intro="This question is about acids and alkalis.")

facts(AC, "2.28", [
    D(q="Give the colour of methyl orange in an acidic solution.", a="red", n="ALLOW pink"),
    D(q="Give the colour of litmus in an acidic solution.", a="red"),
    D(q="Name the ion produced by all acids in water.", a="hydrogen ion / H⁺", ref="2.31"),
    D(q="Name the ion produced by all alkalis in water.", a="hydroxide ion / OH⁻", ref="2.31"),
    D(q="Give the pH of a neutral solution.", a="7", ref="2.29"),
    D(q="State the range of pH values for a weakly alkaline solution.", a="8–10 (accept 8–11)", ref="2.29", d="4-6"),
    D(q="Give the colour of universal indicator in a solution of pH 1.", a="red", ref="2.30"),
    D(q="Name a suitable indicator for an acid–alkali titration.", a="phenolphthalein / methyl orange", ref="2.33C"),
    D(q="State what is meant by the end-point of a titration.", a="the point where the indicator just changes colour (acid has exactly neutralised the alkali)", ref="2.33C", d="4-6"),
    D(q="Name the type of reaction between an acid and an alkali.", a="neutralisation", ref="2.32"),
    D(q="State what is meant by **concordant** titres.", a="titres within 0.20 cm³ (or 0.10 cm³) of each other", ref="2.33C", d="7-9"),
], intro="This question is about acids, alkalis and indicators.")

items(AC, "describe", "2.33C", [
    D(s="Describe how to carry out a titration to find the volume of hydrochloric acid needed to neutralise 25.0 cm³ of sodium hydroxide solution.", m=5,
      p=["use a pipette (and filler) to put 25.0 cm³ of alkali in a conical flask", "add a few drops of indicator (e.g. phenolphthalein)", "fill the burette with acid and read the initial volume",
         "add acid while swirling, dropwise near the end-point, until the indicator just changes colour", "read the final volume; repeat until concordant titres"],
      figs=[fig(S.titration(), 90, caption="Titration apparatus")]),
    D(s="Describe how to use universal indicator to find the pH of a solution.", m=2, p=["add a few drops of indicator (or dip indicator paper)", "compare the colour with a pH colour chart"], ref="2.30"),
    D(s="Describe how you could use two indicators to show whether a colourless solution is acidic, neutral or alkaline.", m=3,
      p=["add litmus / methyl orange to one sample", "add phenolphthalein to another sample", "e.g. methyl orange red = acid; phenolphthalein pink = alkali; neither = neutral"], ref="2.28", d="7-9"),
    D(s="Describe how the pH changes as an alkali is added slowly to an acid until the alkali is in excess.", m=3,
      p=["pH starts low (about 1)", "pH rises slowly then rapidly near neutralisation (pH 7)", "ends high (about 13) when alkali in excess"], ref="2.32", d="7-9"),
    D(s="Describe how to rinse and fill a burette before a titration.", m=3, p=["rinse with distilled water then with the acid", "fill using a funnel; remove the funnel",
      "run some acid through so the tip is filled / no air bubbles"], d="7-9"),
    D(s="Describe how to read a burette accurately.", m=2, p=["read at eye level", "read the bottom of the meniscus (to 0.05 cm³)"], d="4-6"),
    D(s="Describe what happens to the hydrogen ions and hydroxide ions during neutralisation.", m=2, p=["H⁺ ions react with OH⁻ ions", "to form water (H₂O)"], ref="2.32"),
    D(s="Describe the colour change at the end-point when hydrochloric acid is added to sodium hydroxide containing {i}.", m=1, p=["{c}"],
      v=[{"i": "phenolphthalein", "c": "pink to colourless"}, {"i": "methyl orange", "c": "yellow to orange/red"}], d="4-6"),
    D(s="Describe how a student could find the exact volume of acid for neutralisation in a quicker way after a first rough titration.", m=2,
      p=["add acid quickly to about 1 cm³ before the rough end-point", "then add drop by drop until colour changes"], d="7-9"),
    D(s="Describe how to classify a solution with pH 4 and one with pH 13.", m=2, p=["pH 4: weakly acidic", "pH 13: strongly alkaline"], ref="2.29"),
])

ACID_ALK = [("HCl", "NaOH", 1, 1, "hydrochloric acid", "sodium hydroxide"), ("HNO3", "KOH", 1, 1, "nitric acid", "potassium hydroxide"),
            ("H2SO4", "NaOH", 1, 2, "sulfuric acid", "sodium hydroxide"), ("H2SO4", "KOH", 1, 2, "sulfuric acid", "potassium hydroxide"),
            ("HCl", "Na2CO3", 2, 1, "hydrochloric acid", "sodium carbonate"), ("HCl", "KOH", 1, 1, "hydrochloric acid", "potassium hydroxide"),
            ("HNO3", "NaOH", 1, 1, "nitric acid", "sodium hydroxide"), ("H2SO4", "Na2CO3", 1, 1, "sulfuric acid", "sodium carbonate")]
EQS = {("HCl", "NaOH"): "HCl(aq) + NaOH(aq) -> NaCl(aq) + H2O(l)", ("HNO3", "KOH"): "HNO3(aq) + KOH(aq) -> KNO3(aq) + H2O(l)",
       ("H2SO4", "NaOH"): "H2SO4(aq) + 2NaOH(aq) -> Na2SO4(aq) + 2H2O(l)", ("H2SO4", "KOH"): "H2SO4(aq) + 2KOH(aq) -> K2SO4(aq) + 2H2O(l)",
       ("HCl", "Na2CO3"): "2HCl(aq) + Na2CO3(aq) -> 2NaCl(aq) + H2O(l) + CO2(g)", ("HCl", "KOH"): "HCl(aq) + KOH(aq) -> KCl(aq) + H2O(l)",
       ("HNO3", "NaOH"): "HNO3(aq) + NaOH(aq) -> NaNO3(aq) + H2O(l)", ("H2SO4", "Na2CO3"): "H2SO4(aq) + Na2CO3(aq) -> Na2SO4(aq) + H2O(l) + CO2(g)"}


@tpl(AC, "calculation", 30)
def acids_titration_calc(r, k):
    acid, base, na, nb, an, bn = ACID_ALK[k % len(ACID_ALK)]
    eq = EQS[(acid, base)]
    vb = 25.0
    cb = r.choice([Fr(1, 10), Fr(1, 5), Fr(1, 4), Fr(1, 2), Fr(3, 20), Fr(2, 25)])
    nbm = cb * Fr(25, 1000)
    nam = nbm * na / nb
    # choose acid conc so titre is reasonable
    ca = r.choice([Fr(1, 10), Fr(1, 5), Fr(1, 4), Fr(1, 2), Fr(3, 20), Fr(2, 25), Fr(1, 8)])
    titre = nam / ca * 1000
    if not (10 <= titre <= 45):
        return None
    tt = float(titre)
    style = (k // len(ACID_ALK)) % 3
    if style == 0:
        # results table: rough + 3 accurate, two concordant
        t1 = round(tt + r.choice([0.6, 0.8, 1.0]), 2)
        a1 = round(tt + r.choice([-0.05, 0.0, 0.05]), 2)
        a2 = round(2 * tt - a1, 2)
        a3 = round(tt + r.choice([0.35, 0.45, -0.40]), 2)
        mean = (a1 + a2) / 2
        if abs(mean - tt) > 0.001:
            return None
        starts = [round(r.choice([0.00, 0.50, 1.00, 0.10, 0.20, 0.40]), 2) for _ in range(4)]
        tb = table(["", "Rough", "1", "2", "3"], [["Final reading in cm³"] + [f"{s + v:.2f}" for s, v in zip(starts, [t1, a1, a3, a2])],
                                                  ["Initial reading in cm³"] + [f"{s:.2f}" for s in starts],
                                                  ["Titre in cm³"] + [f"{t1:.2f}", f"{a1:.2f}", "[[blank]]", "[[blank]]"]])
        parts = [P("a", "Complete the table.", 1, space="table"),
                 P("b", "Calculate the mean titre using only the concordant results.", 2, space="working", answer_prefix="mean titre = ", lines=3),
                 P("c", f"Calculate the concentration of the {an} in mol/dm³. Give your answer to 3 significant figures.", 3, space="working",
                   answer_prefix="concentration = ", lines=6)]
        rows = [row("a", f"{a3:.2f} and {a2:.2f}", 1, "both needed", "AO3"),
                row("b", f"M1 uses titres {a1:.2f} and {a2:.2f} only", 1, "ALLOW ecf from (a)", "AO3"),
                row("b", f"M2 {mean:.2f} cm³", 1, None, "AO2"),
                row("c", f"M1 moles {F(base)} = {num(float(cb))} × 25.0 ÷ 1000 = {num(float(nbm), sf=3)}", 1, None, "AO2"),
                row("c", f"M2 moles {F(acid)} = {num(float(nam), sf=3)}", 1, f"ratio {na}:{nb} from equation; ALLOW ecf", "AO2"),
                row("c", f"M3 {num(float(nam), sf=3)} ÷ ({mean:.2f} ÷ 1000) = {num(float(ca), sf=3)} mol/dm³", 1, "ALLOW ecf from (b)", "AO2")]
        intro = (f"A student titrates 25.0 cm³ of {num(float(cb))} mol/dm³ {bn} solution with {an}.\n\n{EQ(eq)}\n\nThe table shows her results.")
        return Q("Calculate", "7-9", parts, rows, ["2.33C", "1.34C"], figs=[tb], intro=intro,
                 ans=("n=cV, ratio, c=n/V", {"titre3": a3, "titre2": a2, "mean": round(mean, 2), "conc": float(num(float(ca), sf=3))}), ao=["AO2", "AO3"])
    if style == 1:
        stem = (f"{num(tt, dp=2)} cm³ of {an} exactly neutralises 25.0 cm³ of {num(float(cb))} mol/dm³ {bn} solution.\n\n{EQ(eq)}\n\n"
                f"Calculate the concentration of the {an} in mol/dm³. Give your answer to 3 significant figures.")
        rows = [row("", f"M1 moles {F(base)} = {num(float(cb))} × 25.0 ÷ 1000 = {num(float(nbm), sf=3)}", 1, None, "AO2"),
                row("", f"M2 moles {F(acid)} = {num(float(nam), sf=3)}", 1, f"uses {na}:{nb} ratio", "AO2"),
                row("", f"M3 concentration = {num(float(nam), sf=3)} ÷ {num(tt / 1000, sf=4)} = {num(float(ca), sf=3)} mol/dm³", 1, "ALLOW ecf", "AO2")]
        return Q("Calculate", "7-9" if na != nb else "4-6", [P("", stem, 3, space="working", answer_prefix="concentration = ", lines=6)], rows,
                 ["2.33C", "1.34C"], ans=("c=n/V", {"conc": float(num(float(ca), sf=3))}), ao=["AO2"])
    # style 2: mass concentration of base in g/dm3
    gdm = cb * Mr(base)
    stem = (f"A solution of {bn} has a concentration of {num(float(cb))} mol/dm³.\n\nCalculate its concentration in g/dm³. "
            f"[Mr of {F(base)} = {num(Mr(base))}]")
    rows = [row("", f"M1 {num(float(cb))} × {num(Mr(base))}", 1, None, "AO2"), row("", f"M2 {num(float(gdm), sf=3)} g/dm³", 1, None, "AO2")]
    return Q("Calculate", "4-6", [P("", stem, 2, space="working", answer_prefix="concentration = ", lines=3)], rows, ["1.34C"],
             ans=("c×Mr", {"g_dm3": float(num(float(gdm), sf=3))}), ao=["AO2"])


items(AC, "practical", "2.33C", [
    D(s="Explain why the conical flask is swirled during a titration.", m=1, p=["to mix the acid and alkali (so the end-point is not overshot)"], d="1-3"),
    D(s="Explain why the burette tap is opened to fill the jet before the first reading is taken.", m=2, p=["otherwise an air bubble in the jet", "would give a titre that is too large / inaccurate"], d="7-9"),
    D(s="Suggest why a white tile is placed under the conical flask.", m=1, p=["to see the colour change (end-point) more clearly"]),
    D(s="Explain why the pipette should be rinsed with the alkali solution rather than water before use.", m=2, p=["water would dilute the alkali", "so fewer moles would be in 25.0 cm³ / titre too small"], d="7-9"),
    D(s="Explain why the conical flask may be rinsed with distilled water but it does not matter if some water is left in it.", m=2,
      p=["the amount (moles) of alkali added from the pipette is unchanged", "so the volume of acid needed is the same"], d="7-9"),
    D(s="Give two reasons why a student repeats a titration.", m=2, p=["to get concordant results", "to identify / exclude anomalies", "so a reliable mean can be calculated"], any=True, d="4-6"),
    D(s="Suggest why the first titration is called a rough titration and is not used in the mean.", m=2, p=["acid is added quickly to find the approximate end-point", "so the end-point is likely overshot"], d="4-6"),
    D(s="State the resolution of a burette and how titres should be recorded.", m=2, p=["readings to the nearest 0.05 cm³", "to 2 decimal places"], d="4-6"),
    D(s="Give two safety precautions when carrying out a titration with sodium hydroxide and hydrochloric acid.", m=2,
      p=["eye protection", "use a pipette filler (never mouth)", "fill the burette below eye level / remove funnel"], any=True, d="1-3"),
    D(s="A student leaves the funnel in the top of the burette during the titration. Explain how this could affect the result.", m=2,
      p=["drops of acid may fall from the funnel into the burette", "the reading would change, giving an inaccurate titre"], d="7-9"),
    D(s="Suggest how a student could make a pure sample of sodium chloride using the titration result.", m=3,
      p=["repeat the titration with the same volumes but no indicator", "evaporate some water from the neutral solution", "leave to crystallise; filter and dry"], ref="2.40C", d="7-9"),
    D(s="Explain why methyl orange gives a sharper end-point than universal indicator.", m=2, p=["methyl orange has one sharp colour change", "universal indicator changes through many colours gradually"], d="7-9"),
])

# =================================================================== 2(g) salts
facts(SA, "2.34", [
    D(mq="Which of these salts is insoluble in water?", c="silver chloride", w=["sodium chloride", "potassium nitrate", "ammonium sulfate"]),
    D(mq="Which of these salts is insoluble in water?", c="barium sulfate", w=["copper(II) sulfate", "zinc chloride", "sodium carbonate"]),
    D(mq="Which statement about the solubility of nitrates is correct?", c="all common nitrates are soluble", w=["all nitrates are insoluble",
      "only sodium nitrate is soluble", "lead(II) nitrate is insoluble"]),
    D(mq="Which carbonate is soluble in water?", c="potassium carbonate", w=["calcium carbonate", "copper(II) carbonate", "zinc carbonate"]),
    D(mq="Which hydroxide is soluble in water?", c="sodium hydroxide", w=["copper(II) hydroxide", "iron(III) hydroxide", "magnesium hydroxide"], d="4-6"),
    D(mq="What is produced when an acid reacts with a metal carbonate?", c="a salt, water and carbon dioxide", w=["a salt and hydrogen",
      "a salt and water only", "a metal oxide and carbon dioxide"], ref="2.37"),
    D(mq="What is a base?", c="a substance that accepts protons (H⁺ ions)", w=["a substance that donates protons", "a soluble acid", "any metal"], ref="2.36"),
    D(mq="Which salt is made from zinc oxide and nitric acid?", c="zinc nitrate", w=["zinc sulfate", "zinc chloride", "zinc nitride"], ref="2.37"),
    D(mq="Which method is used to make an insoluble salt?", c="precipitation by mixing two solutions", w=["titration", "adding excess metal oxide to acid then filtering off the oxide",
      "crystallisation of the acid"], ref="2.41C", d="4-6"),
    D(mq="Why is excess copper(II) oxide added to sulfuric acid when making copper(II) sulfate?", c="to make sure all the acid reacts",
      w=["to speed up crystallisation", "to make the solution more acidic", "to dissolve the copper"], ref="2.39", d="4-6"),
    D(mq="Which pair of solutions forms a precipitate of lead(II) sulfate?", c="lead(II) nitrate and sodium sulfate", w=["lead(II) nitrate and sodium nitrate",
      "sodium sulfate and potassium chloride", "lead(II) sulfate and water"], ref="2.43C", d="7-9"),
    D(mq="Which salt is formed when ammonia solution reacts with nitric acid?", c="ammonium nitrate", w=["ammonium nitrite", "nitrogen nitrate", "ammonia nitrate"], ref="2.38"),
    D(mq="Which substance is an alkali?", c="potassium hydroxide", w=["copper(II) oxide", "iron(III) hydroxide", "zinc carbonate"], ref="2.38"),
], intro="This question is about salts.")

facts(SA, "2.34", [
    D(q="Name the gas produced when zinc reacts with dilute sulfuric acid.", a="hydrogen", ref="2.37"),
    D(q="Name the salt formed when magnesium oxide reacts with hydrochloric acid.", a="magnesium chloride", ref="2.37"),
    D(q="State what is meant by a **base**.", a="a proton (H⁺) acceptor", n="ALLOW substance that neutralises an acid to form a salt and water", ref="2.36"),
    D(q="State what is meant by an **acid** in terms of protons.", a="a proton (H⁺) donor", ref="2.36"),
    D(q="Name the two insoluble chlorides.", m=2, pts=["silver chloride", "lead(II) chloride"]),
    D(q="Name three insoluble sulfates.", m=3, pts=["barium sulfate", "calcium sulfate", "lead(II) sulfate"]),
    D(q="Give the names of the products when calcium carbonate reacts with nitric acid.", m=3, pts=["calcium nitrate", "water", "carbon dioxide"], ref="2.37"),
    D(q="State what is meant by an **alkali**.", a="a soluble base / a base that dissolves in water to give OH⁻ ions", ref="2.38"),
    D(q="Name the acid needed to make potassium sulfate from potassium hydroxide.", a="sulfuric acid", ref="2.40C"),
    D(q="Name a pair of solutions that could be mixed to make a precipitate of barium sulfate.", m=2, pts=["barium chloride / barium nitrate solution", "sodium sulfate / any soluble sulfate / sulfuric acid"], ref="2.41C", d="4-6"),
    D(q="State which group of salts are all soluble in water, whatever the negative ion.", a="sodium / potassium / ammonium salts (or nitrates)"),
], intro="This question is about making salts.")

SALT_EQ = [
    ("zinc + hydrochloric acid → zinc chloride + hydrogen", "Zn(s) + 2HCl(aq) -> ZnCl2(aq) + H2(g)"),
    ("magnesium + sulfuric acid → magnesium sulfate + hydrogen", "Mg(s) + H2SO4(aq) -> MgSO4(aq) + H2(g)"),
    ("copper(II) oxide + sulfuric acid → copper(II) sulfate + water", "CuO(s) + H2SO4(aq) -> CuSO4(aq) + H2O(l)"),
    ("zinc oxide + nitric acid → zinc nitrate + water", "ZnO(s) + 2HNO3(aq) -> Zn(NO3)2(aq) + H2O(l)"),
    ("magnesium carbonate + hydrochloric acid → magnesium chloride + water + carbon dioxide", "MgCO3(s) + 2HCl(aq) -> MgCl2(aq) + H2O(l) + CO2(g)"),
    ("calcium carbonate + nitric acid → calcium nitrate + water + carbon dioxide", "CaCO3(s) + 2HNO3(aq) -> Ca(NO3)2(aq) + H2O(l) + CO2(g)"),
    ("potassium hydroxide + sulfuric acid → potassium sulfate + water", "2KOH(aq) + H2SO4(aq) -> K2SO4(aq) + 2H2O(l)"),
    ("ammonia + hydrochloric acid → ammonium chloride", "NH3(aq) + HCl(aq) -> NH4Cl(aq)"),
    ("ammonia + sulfuric acid → ammonium sulfate", "2NH3(aq) + H2SO4(aq) -> (NH4)2SO4(aq)"),
    ("copper(II) carbonate + sulfuric acid → copper(II) sulfate + water + carbon dioxide", "CuCO3(s) + H2SO4(aq) -> CuSO4(aq) + H2O(l) + CO2(g)"),
    ("lead(II) nitrate + sodium sulfate → lead(II) sulfate + sodium nitrate", "Pb(NO3)2(aq) + Na2SO4(aq) -> PbSO4(s) + 2NaNO3(aq)"),
    ("barium chloride + sodium sulfate → barium sulfate + sodium chloride", "BaCl2(aq) + Na2SO4(aq) -> BaSO4(s) + 2NaCl(aq)"),
    ("silver nitrate + potassium bromide → silver bromide + potassium nitrate", "AgNO3(aq) + KBr(aq) -> AgBr(s) + KNO3(aq)"),
    ("iron(III) oxide + hydrochloric acid → iron(III) chloride + water", "Fe2O3(s) + 6HCl(aq) -> 2FeCl3(aq) + 3H2O(l)"),
    ("aluminium + hydrochloric acid → aluminium chloride + hydrogen", "2Al(s) + 6HCl(aq) -> 2AlCl3(aq) + 3H2(g)"),
    ("calcium hydroxide + nitric acid → calcium nitrate + water", "Ca(OH)2(aq) + 2HNO3(aq) -> Ca(NO3)2(aq) + 2H2O(l)"),
]
PRECIP_ION = [("lead(II) sulfate", "Pb^2+(aq) + SO4^2-(aq) -> PbSO4(s)"), ("barium sulfate", "Ba^2+(aq) + SO4^2-(aq) -> BaSO4(s)"),
              ("silver chloride", "Ag^+(aq) + Cl^-(aq) -> AgCl(s)"), ("silver iodide", "Ag^+(aq) + I^-(aq) -> AgI(s)"),
              ("lead(II) iodide", "Pb^2+(aq) + 2I^-(aq) -> PbI2(s)"), ("calcium carbonate", "Ca^2+(aq) + CO3^2-(aq) -> CaCO3(s)"),
              ("copper(II) hydroxide", "Cu^2+(aq) + 2OH^-(aq) -> Cu(OH)2(s)"), ("iron(III) hydroxide", "Fe^3+(aq) + 3OH^-(aq) -> Fe(OH)3(s)"),
              ("lead(II) chloride", "Pb^2+(aq) + 2Cl^-(aq) -> PbCl2(s)"), ("silver bromide", "Ag^+(aq) + Br^-(aq) -> AgBr(s)")]


@tpl(SA, "equation", 40)
def salts_equations(r, k):
    if k % 4 == 3:
        nm, ion = PRECIP_ION[(k // 4) % len(PRECIP_ION)]
        stem = f"Write the ionic equation, with state symbols, for the formation of a precipitate of {nm}."
        rows = [row("", f"M1 correct ions and product: {EQ(ion, states=False)}", 1, "ALLOW balanced multiples", "AO2"),
                row("", f"M2 state symbols: {EQ(ion)}", 1, "M2 dep on M1", "AO2")]
        return Q("Write", "7-9", [P("", stem, 2, lines=2)], rows, ["2.41C"], ao=["AO2"], ans=("ionic", {"ionic": EQ(ion)}))
    word, sym = SALT_EQ[k % len(SALT_EQ)]
    mode = [0, 2, 1][(k // len(SALT_EQ)) % 3]
    ref = ["2.41C"] if "(s) +" not in sym and "PbSO4(s)" in sym or "BaSO4(s)" in sym or "AgBr(s)" in sym else ["2.37"]
    return eq_q(word, sym, ref, d="7-9" if ("Fe2O3" in sym or "2Al" in sym) else "4-6", mode=mode)


items(SA, "practical", "2.42", [
    D(s="Describe how to prepare pure, dry crystals of hydrated copper(II) sulfate from copper(II) oxide and dilute sulfuric acid.", m=6,
      p=["warm the sulfuric acid", "add copper(II) oxide a little at a time with stirring until in excess (no more dissolves)", "filter to remove excess copper(II) oxide",
         "heat the filtrate to evaporate some water / until crystals form on a glass rod", "leave to cool and crystallise", "filter off crystals and dry between filter paper / in a warm oven"]),
    D(s="Explain why the excess copper(II) oxide is removed by filtration.", m=2, p=["copper(II) oxide is insoluble", "so the salt solution is not contaminated"], ref="2.39"),
    D(s="Explain how you know that all the acid has reacted when making copper(II) sulfate from copper(II) oxide.", m=1, p=["black solid remains / no more dissolves"], ref="2.39", d="4-6"),
    D(s="Describe how to make a pure, dry sample of lead(II) sulfate.", m=4,
      p=["mix solutions of lead(II) nitrate and a soluble sulfate (e.g. sodium sulfate)", "filter off the white precipitate", "wash with distilled water",
         "dry in a warm oven / between filter paper"], ref="2.43C", d="7-9"),
    D(s="Explain why the precipitate of an insoluble salt is washed with distilled water.", m=2, p=["to remove the soluble impurities / other ions", "distilled so no new ions are added"], ref="2.41C", d="7-9"),
    D(s="Explain why crystals are dried between filter paper and not by strong heating.", m=2, p=["strong heating would remove water of crystallisation", "the crystals would turn into a powder / decompose"], d="7-9"),
    D(s="Give two safety precautions when preparing copper(II) sulfate from warm sulfuric acid.", m=2, p=["eye protection", "do not boil the acid / heat gently", "copper(II) sulfate is harmful – avoid skin contact"], any=True),
    D(s="Explain why a titration is used to make sodium sulfate from sodium hydroxide and sulfuric acid, but not to make copper(II) sulfate from copper(II) oxide.", m=3,
      p=["both sodium hydroxide and sodium sulfate are soluble", "so excess cannot be filtered off / need exact amounts", "copper(II) oxide is insoluble so excess can be filtered off"], ref="2.40C", d="7-9"),
    D(s="Suggest why copper(II) carbonate fizzes when added to sulfuric acid but copper(II) oxide does not.", m=2, p=["carbonate gives carbon dioxide", "oxide reacts to give only salt and water"], ref="2.37", d="4-6"),
    D(s="Describe how to test that a solution of copper(II) sulfate is saturated enough to crystallise.", m=2, p=["dip a glass rod into the solution and remove it", "crystals form on the rod as it cools"], d="7-9"),
    D(s="Suggest why the mass of crystals obtained is less than the theoretical yield.", m=2,
      p=["some salt remains in solution", "losses when filtering / transferring", "some crystals stick to the filter paper"], any=True, d="4-6"),
    D(s="Explain why magnesium powder rather than magnesium ribbon could be used when making magnesium sulfate from magnesium and sulfuric acid.", m=2,
      p=["powder has a larger surface area", "so reacts faster"], d="4-6"),
])

SALT_PREPS = [
    ("pure, dry crystals of zinc sulfate from zinc oxide", "insoluble base", "zinc oxide", "sulfuric acid"),
    ("pure, dry crystals of magnesium chloride from magnesium carbonate", "insoluble carbonate", "magnesium carbonate", "hydrochloric acid"),
    ("pure, dry crystals of copper(II) nitrate from copper(II) carbonate", "insoluble carbonate", "copper(II) carbonate", "nitric acid"),
    ("pure, dry crystals of potassium nitrate", "titration", "potassium hydroxide solution", "nitric acid"),
    ("pure, dry crystals of sodium sulfate", "titration", "sodium hydroxide solution", "sulfuric acid"),
    ("a pure, dry sample of barium sulfate", "precipitation", "barium chloride solution", "sodium sulfate solution"),
    ("a pure, dry sample of silver chloride", "precipitation", "silver nitrate solution", "sodium chloride solution"),
    ("a pure, dry sample of calcium carbonate", "precipitation", "calcium chloride solution", "sodium carbonate solution"),
    ("pure, dry crystals of ammonium sulfate", "titration", "ammonia solution", "sulfuric acid"),
    ("pure, dry crystals of iron(II) sulfate from iron powder", "metal", "iron powder", "sulfuric acid"),
    ("a pure, dry sample of lead(II) iodide", "precipitation", "lead(II) nitrate solution", "potassium iodide solution"),
    ("pure, dry crystals of magnesium sulfate from magnesium oxide", "insoluble base", "magnesium oxide", "sulfuric acid"),
]


def _salt_ind(kind, a, b):
    if kind in ("insoluble base", "insoluble carbonate", "metal"):
        return [f"warm the {b} (gently)", f"add {a} a little at a time with stirring" + (" (fizzing)" if kind != "insoluble base" else ""),
                f"until {a} is in excess / no more reacts" + (" / no more bubbles" if kind != "insoluble base" else ""), f"filter off excess {a}",
                "heat the filtrate to evaporate some water until saturated / crystals on a glass rod", "leave to cool and crystallise", "filter and dry crystals between filter paper / warm oven"]
    if kind == "titration":
        return [f"pipette 25.0 cm³ of {a} into a conical flask with a few drops of indicator", f"add {b} from a burette until the indicator just changes colour",
                "record the volume of acid", "repeat with the same volumes but without indicator (or remove indicator with charcoal)",
                "evaporate some water to concentrate the solution", "leave to cool and crystallise", "filter and dry the crystals"]
    return [f"mix {a} with {b}", "a precipitate forms (the insoluble salt)", "stir to ensure complete reaction", "filter the mixture to collect the precipitate",
            "wash the residue with distilled water", "dry in a warm oven / between filter paper", "the other product stays dissolved in the filtrate"]


extended(SA, "2.39", [
    D(s=f"Describe how you would prepare {m}. In your answer, name the reagents and give the essential steps.", ind=_salt_ind(kd, a, b),
      ref={"titration": "2.40C", "precipitation": "2.41C"}.get(kd, "2.39"), ao="AO1 3, AO3 3", d="7-9" if kd != "insoluble base" else "4-6")
    for m, kd, a, b in SALT_PREPS
])

# =================================================================== 2(i) chemical tests
facts(TE, "2.44", [
    D(mq="Which gas relights a glowing splint?", c="oxygen", w=["hydrogen", "carbon dioxide", "chlorine"]),
    D(mq="Which gas turns limewater milky?", c="carbon dioxide", w=["oxygen", "ammonia", "hydrogen"]),
    D(mq="Which gas turns damp red litmus paper blue?", c="ammonia", w=["chlorine", "hydrogen", "oxygen"]),
    D(mq="Which ion gives a lilac flame colour?", c="K^+", w=["Na^+", "Li^+", "Cu^2+"], ref="2.46"),
    D(mq="Which ion gives a blue-green flame colour?", c="Cu^2+", w=["Ca^2+", "K^+", "Li^+"], ref="2.46"),
    D(mq="Which ion gives an orange-red flame colour?", c="Ca^2+", w=["K^+", "Na^+", "Cu^2+"], ref="2.46"),
    D(mq="What colour is the precipitate when sodium hydroxide solution is added to a solution of iron(III) ions?", c="brown", w=["green", "blue", "white"], ref="2.47"),
    D(mq="What colour is the precipitate when sodium hydroxide solution is added to a solution of iron(II) ions?", c="green", w=["brown", "blue", "white"], ref="2.47"),
    D(mq="Which reagents test for a sulfate ion?", c="dilute hydrochloric acid and barium chloride solution", w=["dilute nitric acid and silver nitrate solution",
      "sodium hydroxide solution and warming", "limewater"], ref="2.48"),
    D(mq="A halide solution gives a cream precipitate with acidified silver nitrate. Which ion is present?", c="Br^-", w=["Cl^-", "I^-", "SO4^2-"], ref="2.48", d="4-6"),
    D(mq="What colour change shows that water is present when it is added to anhydrous copper(II) sulfate?", c="white to blue", w=["blue to white", "pink to blue", "green to brown"], ref="2.49"),
    D(mq="How can you show that a sample of water is pure?", c="it boils at exactly 100 °C", w=["it turns copper(II) sulfate blue", "it is colourless", "it has pH 7"], ref="2.50", d="4-6"),
    D(mq="Which test identifies ammonium ions?", c="warm with sodium hydroxide solution and test the gas with damp red litmus", w=["add silver nitrate solution",
      "add barium chloride solution", "do a flame test"], ref="2.47", d="4-6"),
], intro="This question is about chemical tests.")

facts(TE, "2.44", [
    D(q="Describe the test for hydrogen.", m=2, pts=["lighted splint", "squeaky pop"]),
    D(q="Describe the test for oxygen.", m=2, pts=["glowing splint", "relights"]),
    D(q="Describe the test for carbon dioxide.", m=2, pts=["bubble through limewater", "limewater turns milky / cloudy"]),
    D(q="Describe the test for chlorine.", m=2, pts=["damp (blue) litmus paper", "turns red then bleaches / white"]),
    D(q="Describe the test for ammonia gas.", m=2, pts=["damp red litmus paper", "turns blue"]),
    D(q="Give the flame colour of lithium ions.", a="red / crimson", ref="2.46"),
    D(q="Give the flame colour of sodium ions.", a="yellow", ref="2.46"),
    D(q="Give the colour of the precipitate formed when sodium hydroxide is added to copper(II) ions.", a="blue", ref="2.47"),
    D(q="Give the colour of the precipitate formed when acidified silver nitrate is added to iodide ions.", a="yellow", ref="2.48"),
    D(q="Name the gas formed when dilute acid is added to a carbonate.", a="carbon dioxide", ref="2.48"),
    D(q="Name a chemical used to test for the presence of water.", a="anhydrous copper(II) sulfate / cobalt chloride paper", ref="2.49"),
    D(q="State why nitric acid is added before silver nitrate in the test for halide ions.", a="to remove carbonate ions (which would also give a precipitate)", ref="2.48", d="7-9"),
], intro="This question is about identifying ions and gases.")

items(TE, "describe", "2.45", [
    D(s="Describe how to carry out a flame test on a solid sample.", m=3,
      p=["dip a clean (nichrome/platinum) wire loop in concentrated hydrochloric acid", "dip into the solid", "hold in a blue (roaring) Bunsen flame and observe the colour"]),
    D(s="A solution may contain {ion} ions. Describe how you would confirm this, stating the positive result.", m=3, p=["{a}", "{b}", "{c}"],
      v=[{"ion": "chloride", "a": "add dilute nitric acid", "b": "add silver nitrate solution", "c": "white precipitate"},
         {"ion": "sulfate", "a": "add dilute hydrochloric acid", "b": "add barium chloride solution", "c": "white precipitate"},
         {"ion": "carbonate", "a": "add dilute (hydrochloric) acid", "b": "bubble the gas through limewater", "c": "fizzing and limewater turns milky"},
         {"ion": "ammonium", "a": "add sodium hydroxide solution and warm", "b": "hold moist red litmus paper in the gas given off", "c": "the litmus goes blue"},
         {"ion": "iodide", "a": "add dilute nitric acid", "b": "add silver nitrate solution", "c": "yellow precipitate"}], ref="2.48"),
    D(s="Describe how sodium hydroxide solution can be used to distinguish between solutions containing Fe²⁺ and Fe³⁺ ions.", m=3,
      p=["add a few drops of sodium hydroxide solution to each", "Fe²⁺ gives a green precipitate", "Fe³⁺ gives a brown precipitate"], ref="2.47"),
    D(s="Describe how to show that a colourless liquid contains water and how to show that it is pure water.", m=4,
      p=["add anhydrous copper(II) sulfate", "turns from white to blue", "measure the boiling point", "pure water boils at 100 °C (at 1 atm)"], ref=["2.49", "2.50"], d="7-9"),
    D(s="Describe why the wire loop must be cleaned before a flame test.", m=1, p=["to remove traces of other substances that would affect the flame colour"], d="4-6"),
    D(s="Describe the results of adding sodium hydroxide solution to separate solutions of copper(II) sulfate and iron(III) chloride.", m=2,
      p=["copper(II) sulfate: blue precipitate", "iron(III) chloride: brown / orange-brown precipitate"], ref="2.47"),
    D(s="Describe how to identify the gas given off when an ammonium compound is warmed with sodium hydroxide solution.", m=2, p=["hold damp red litmus at the mouth of the tube", "turns blue: ammonia"], ref="2.47"),
    D(s="Describe how you could distinguish between solutions of sodium chloride and sodium bromide.", m=3,
      p=["add dilute nitric acid then silver nitrate solution", "chloride: white precipitate", "bromide: cream precipitate"], ref="2.48", d="4-6"),
    D(s="Describe how you could distinguish between potassium carbonate and potassium sulfate solid samples.", m=3,
      p=["add dilute hydrochloric acid", "carbonate fizzes / gas turns limewater milky", "sulfate: no fizzing (then gives white precipitate with barium chloride)"], ref="2.48", d="7-9"),
    D(s="Describe how you could show that a white solid is calcium carbonate.", m=4,
      p=["flame test", "orange-red flame shows calcium", "add dilute acid: fizzes", "gas turns limewater milky shows carbonate"], ref=["2.46", "2.48"], d="7-9"),
])

IONS_C = [("Li^+", "lithium", "red flame", None), ("Na^+", "sodium", "yellow flame", None), ("K^+", "potassium", "lilac flame", None),
          ("Ca^2+", "calcium", "orange-red flame", None), ("Cu^2+", "copper(II)", "blue-green flame", "blue precipitate"),
          ("Fe^2+", "iron(II)", None, "green precipitate"), ("Fe^3+", "iron(III)", None, "brown precipitate"), ("NH4^+", "ammonium", None, "gas turns damp red litmus blue on warming")]
IONS_A = [("Cl^-", "chloride", "white precipitate", None), ("Br^-", "bromide", "cream precipitate", None), ("I^-", "iodide", "yellow precipitate", None),
          ("SO4^2-", "sulfate", None, "white precipitate"), ("CO3^2-", "carbonate", None, None)]


def _soluble_salt(cat, an):
    """True for a stable salt that dissolves in water (IGCSE solubility rules)."""
    if an == "CO3^2-":
        return cat in ("Li^+", "Na^+", "K^+", "NH4^+")
    if an == "SO4^2-" and cat == "Ca^2+":
        return False  # only slightly soluble
    if an == "I^-" and cat in ("Cu^2+", "Fe^3+"):
        return False  # not stable: iodide is oxidised
    return True


@tpl(TE, "data", 16)
def tests_identify_data(r, k):
    cats = r.sample(IONS_C, 3)
    ans = []
    for c in cats:  # only real, water-soluble salts
        ok = [a for a in IONS_A if a not in ans and _soluble_salt(c[0], a[0])]
        ans.append(r.choice(ok))
    letters = ["P", "Q", "R"]
    rows_t, names = [], []
    for L_, c, a in zip(letters, cats, ans):
        flame = c[2] or "no distinctive colour"
        naoh = c[3] or "no precipitate"
        if c[0] == "Ca^2+":
            naoh = "white precipitate"
        ag = a[2] or "no precipitate"
        ba = a[3] or "no precipitate"
        acid = "fizzes; gas turns limewater milky" if a[0] == "CO3^2-" else "no reaction"
        rows_t.append([L_, flame, naoh, acid, ag, ba])
        names.append(f"{c[1]} {a[1]}")
    tb = table(["Solid", "Flame test", "Add NaOH(aq)", "Add dilute HCl", "Add HNO₃ then AgNO₃(aq)", "Add HCl then BaCl₂(aq)"], rows_t)
    parts, rows = [], []
    for i, (L_, nm) in enumerate(zip(letters, names)):
        parts.append(P("abc"[i], f"Identify solid {L_}.", 2, lines=1))
        c, a = cats[i][1], ans[i][1]
        rows += [row("abc"[i], f"M1 {c} (ion)", 1, None, "AO3"), row("abc"[i], f"M2 {a} (ion)", 1, None, "AO3")]
    note = "Each solid is soluble in water and is dissolved before the tests (except the flame test)."
    return Q("Identify", "4-6" if not any(c[0].startswith("Fe") or c[0] == "NH4^+" for c in cats) else "7-9", parts, rows,
             ["2.46", "2.47", "2.48"], figs=[tb], intro="A student carries out tests on three solids, P, Q and R. " + note,
             ans=("lookup", {"P": names[0], "Q": names[1], "R": names[2]}), ao=["AO3"])


UNKNOWN = [("iron(II) sulfate", ["dissolve in water", "add sodium hydroxide solution: green precipitate shows Fe²⁺", "precipitate turns brown on standing (oxidised)",
            "add dilute hydrochloric acid then barium chloride solution", "white precipitate shows sulfate", "results together identify iron(II) sulfate"]),
           ("ammonium chloride", ["dissolve in water", "add sodium hydroxide solution and warm", "ammonia gas turns damp red litmus blue: NH₄⁺",
            "to a fresh sample add dilute nitric acid then silver nitrate solution", "white precipitate shows chloride", "both results identify ammonium chloride"]),
           ("potassium iodide", ["flame test with clean wire loop", "lilac flame shows K⁺", "dissolve in water and add dilute nitric acid",
            "add silver nitrate solution", "yellow precipitate shows iodide", "identify as potassium iodide"]),
           ("copper(II) carbonate", ["flame test: blue-green flame shows Cu²⁺", "add dilute acid: fizzing", "bubble gas through limewater: milky shows CO₂ / carbonate",
            "solution formed is blue", "add sodium hydroxide: blue precipitate confirms Cu²⁺", "identify as copper(II) carbonate"]),
           ("calcium bromide", ["flame test: orange-red flame shows Ca²⁺", "clean the wire in acid first", "dissolve and add dilute nitric acid",
            "add silver nitrate solution", "cream precipitate shows bromide", "identify as calcium bromide"]),
           ("iron(III) chloride", ["dissolve in water", "add sodium hydroxide solution", "brown precipitate shows Fe³⁺",
            "fresh sample: add dilute nitric acid then silver nitrate", "white precipitate shows Cl⁻", "identify as iron(III) chloride"]),
           ("sodium sulfate", ["flame test", "yellow flame shows Na⁺", "dissolve and add dilute hydrochloric acid (no fizzing so not carbonate)",
            "add barium chloride solution", "white precipitate shows sulfate", "identify as sodium sulfate"]),
           ("lithium carbonate", ["flame test", "red flame shows Li⁺", "add dilute hydrochloric acid: fizzing", "test gas with limewater",
            "limewater turns milky: carbonate", "identify as lithium carbonate"]),
           ("copper(II) sulfate", ["dissolve: blue solution", "add sodium hydroxide: blue precipitate shows Cu²⁺", "OR flame test blue-green",
            "add dilute hydrochloric acid then barium chloride", "white precipitate: sulfate", "identify as copper(II) sulfate"]),
           ("potassium carbonate", ["flame test: lilac flame shows K⁺", "use clean nichrome wire in roaring flame", "add dilute acid: fizzing",
            "gas turns limewater milky: CO₂", "so carbonate ion present", "identify as potassium carbonate"]),
           ("ammonium sulfate", ["warm with sodium hydroxide solution", "gas turns damp red litmus blue: ammonium", "dissolve fresh sample in water",
            "add dilute hydrochloric acid and barium chloride", "white precipitate: sulfate", "identify as ammonium sulfate"]),
           ("sodium bromide", ["flame test: yellow flame", "so Na⁺ present", "dissolve and acidify with dilute nitric acid", "add silver nitrate solution",
            "cream precipitate: bromide", "identify as sodium bromide"])]

extended(TE, "2.44", [
    D(intro="A student is told that a white or coloured solid is a single salt but is not told which.",
      s=f"Describe the tests the student could do to show that the solid is {nm}. Give the expected result of each test.", ind=ind,
      ref=["2.45", "2.46", "2.47", "2.48"], ao="AO1 3, AO3 3", d="4-6" if i % 3 else "7-9") for i, (nm, ind) in enumerate(UNKNOWN)
])
