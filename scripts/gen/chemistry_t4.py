"""Topic 4 templates: organic chemistry (4(a) to 4(h))."""
from fractions import Fraction as Fr

from chemistry_util import tpl, mcq, P, F, row, Q, num, Mr, EQ, fig, table
from chemistry_kb import facts, items, extended
import chemistry_svg as S

IN = "chemistry.organic.intro"
CR = "chemistry.organic.crude"
AK = "chemistry.organic.alkanes"
AE = "chemistry.organic.alkenes"
AL = "chemistry.organic.alcohols"
CA = "chemistry.organic.acids"
ES = "chemistry.organic.esters"
PO = "chemistry.organic.polymers"

STEM = {1: "meth", 2: "eth", 3: "prop", 4: "but", 5: "pent", 6: "hex", 7: "hept", 8: "oct"}


def D(**k):
    return k


def alkane(n):
    return f"C{n if n > 1 else ''}H{2 * n + 2}".replace("C1H", "CH")


def alkene(n):
    return f"C{n}H{2 * n}"


def cf(n, h, extra=""):
    return f"C{n if n > 1 else ''}H{h}{extra}"


# =================================================================== 4(a) introduction
facts(IN, "4.1", [
    D(mq="What is a hydrocarbon?", c="a compound of hydrogen and carbon only", w=["a compound containing carbon, hydrogen and oxygen", "a mixture of hydrogen and carbon",
      "any compound containing carbon"]),
    D(mq="What is the general formula of the alkanes?", c="CnH2n+2", w=["CnH2n", "CnH2n-2", "CnH2n+1OH"], ref="4.19"),
    D(mq="Two compounds both have the formula C₅H₁₂ but their atoms are joined in different ways. What are they called?", c="isomers", w=["isotopes", "homologues", "polymers"], ref="4.3"),
    D(mq="What is a functional group?", c="an atom or group of atoms that determines the reactions of a compound", w=["the carbon chain of a molecule",
      "any hydrogen atom", "a group of compounds with the same formula"], ref="4.3"),
    D(mq="Which statement about members of a homologous series is correct?", c="each member differs from the next by CH2", w=["they have the same molecular formula",
      "they have the same boiling point", "they have different functional groups"], ref="4.3", d="4-6"),
    D(mq="What is the empirical formula of butane, C4H10?", c="C2H5", w=["C4H10", "CH2", "CH3"], ref="4.2", d="4-6"),
    D(mq="Which type of reaction is CH4 + Cl2 → CH3Cl + HCl?", c="substitution", w=["addition", "combustion", "polymerisation"], ref="4.6"),
    D(mq="Which type of reaction is C2H4 + Br2 → C2H4Br2?", c="addition", w=["substitution", "combustion", "cracking"], ref="4.6"),
    D(mq="What is the name of CH3CH2CH2CH3?", c="butane", w=["propane", "but-1-ene", "pentane"], ref="4.4"),
    D(mq="What is the name of CH2=CHCH3?", c="propene", w=["propane", "ethene", "propan-1-ol"], ref="4.4"),
    D(mq="How many structural isomers have the formula C4H10?", c="2", w=["1", "3", "4"], ref="4.5", d="7-9"),
    D(mq="Which formula is a general formula?", c="CnH2n", w=["C2H4", "CH2", "CH2=CH2"], ref="4.2"),
    D(mq="Which formula is a structural formula?", c="CH3CH2OH", w=["C2H6O", "C2H5OH (molecular)", "CnH2n+1OH"], ref="4.2", d="4-6"),
], intro="This question is about organic compounds.", tag="org_intro")


@tpl(IN, "recall", 16)
def intro_formula_recall(r, k):
    n = 1 + k % 6
    kind = (k // 6) % 3
    fam = ["alkane", "alkene", "alcohol"][kind]
    if fam == "alkene" and n == 1:
        n = 2
    if fam == "alkane":
        mf, name, gf = alkane(n), STEM[n] + "ane", "CnH2n+2"
        sf = "CH3" + "CH2" * (n - 2) + "CH3" if n > 1 else "CH4"
    elif fam == "alkene":
        mf, name, gf = alkene(n), STEM[n] + "ene" if n < 4 else STEM[n] + "-1-ene", "CnH2n"
        sf = "CH2=CH" + "CH2" * (n - 3) + ("CH3" if n > 2 else "") if n > 2 else "CH2=CH2"
    else:
        mf, name, gf = cf(n, 2 * n + 1, "OH"), STEM[n] + ("anol" if n < 3 else "an-1-ol"), "CnH2n+1OH"
        sf = "CH3" + "CH2" * (n - 1) + "OH"
    from math import gcd
    import chemistry_util as U
    at = U.atoms(mf)
    g = 0
    for v in at.values():
        g = gcd(g, v)
    ef = "".join(e + (str(at[e] // g) if at[e] // g > 1 else "") for e in ("C", "H", "O") if e in at)
    parts = [P("a", f"Give the molecular formula of {name}.", 1, lines=1), P("b", f"Give the general formula of the homologous series that contains {name}.", 1, lines=1),
             P("c", f"Give the structural formula of {name}.", 1, lines=1), P("d", f"Give the empirical formula of {name}.", 1, lines=1)]
    rows = [row("a", F(mf), 1, None, "AO1"), row("b", F(gf), 1, None, "AO1"), row("c", F(sf), 1, "ALLOW displayed formula", "AO1"), row("d", F(ef), 1, None, "AO2")]
    refs = ["4.2", "4.4"] + (["4.30C"] if fam == "alcohol" else [])
    return Q("Give", "4-6" if fam != "alcohol" else "7-9", parts, rows, refs, intro=f"This question is about {name}.", ao=["AO1", "AO2"],
             ans=("formula rules", {"molecular": mf, "empirical": ef}))


items(IN, "explain", "4.3", [
    D(s="Explain why ethane and propane are members of the same homologous series.", m=2, p=["same general formula (CnH2n+2)", "differ by CH₂ / similar chemical properties"]),
    D(s="Explain why butane and methylpropane are isomers.", m=2, p=["same molecular formula (C₄H₁₀)", "different structural formulae / arrangement of atoms"], ref="4.5"),
    D(s="Explain why the members of a homologous series have similar chemical properties.", m=2, p=["same functional group", "the functional group determines the reactions"]),
    D(s="Explain why the boiling points of members of a homologous series increase as the chain gets longer.", m=2, p=["larger molecules / higher Mr", "stronger intermolecular forces"]),
    D(s="Explain why the reaction of methane with bromine in UV light is called a substitution reaction.", m=2, p=["a hydrogen atom is replaced", "by a bromine atom"], ref="4.6"),
    D(s="Explain why the reaction of ethene with hydrogen is called an addition reaction.", m=2, p=["two molecules join to form one product", "hydrogen adds across the C=C double bond"], ref="4.6"),
    D(s="Explain why C₂H₄ and C₃H₆ have the same empirical formula.", m=2, p=["ratio of C:H is 1:2 in both", "so empirical formula CH₂"], ref="4.2", d="7-9"),
    D(s="Explain why but-1-ene and but-2-ene are isomers.", m=2, p=["both C₄H₈", "the double bond is in a different position"], ref="4.5", d="7-9"),
    D(s="Explain why pentane has three structural isomers but propane has none.", m=2, p=["pentane has enough carbons to branch in different ways", "propane's three carbons can only be arranged in one chain"], ref="4.5", d="7-9"),
    D(s="Explain how a displayed formula differs from a structural formula.", m=2, p=["displayed shows every atom and every bond", "structural shows how atoms are grouped / arranged without all bonds"], ref="4.2", d="4-6"),
    D(s="Explain why ethanol and propan-1-ol react in a similar way with sodium.", m=2, p=["both contain the –OH functional group", "both are in the same homologous series (alcohols)"], ref="4.29C"),
    D(s="Explain why the combustion of hydrocarbons is not classed as substitution or addition.", m=2, p=["the molecules are broken up completely", "into carbon dioxide and water (oxidation)"], ref="4.6", d="7-9"),
], tag="org_intro")

# =================================================================== 4(b) crude oil
FRACS = [("refinery gases", "domestic heating and cooking / bottled gas"), ("gasoline", "fuel for cars / petrol"), ("kerosene", "fuel for aircraft"),
         ("diesel", "fuel for lorries / trains / some cars"), ("fuel oil", "fuel for ships / power stations"), ("bitumen", "road surfaces / roofing")]

facts(CR, "4.7", [
    D(mq="What is crude oil?", c="a mixture of hydrocarbons", w=["a pure compound", "a single alkane", "a mixture of elements"]),
    D(mq="Which fraction is used to surface roads?", c="bitumen", w=["kerosene", "diesel", "gasoline"], ref="4.9"),
    D(mq="Which fraction is used as fuel for aircraft?", c="kerosene", w=["bitumen", "fuel oil", "refinery gases"], ref="4.9"),
    D(mq="How does viscosity change from refinery gases to bitumen?", c="it increases", w=["it decreases", "it stays the same", "it increases then decreases"], ref="4.10"),
    D(mq="Where do the fractions with the lowest boiling points leave the fractionating column?", c="at the top", w=["at the bottom", "in the middle", "they are not collected"], ref="4.8"),
    D(mq="Which gas is toxic and is formed by incomplete combustion?", c="carbon monoxide", w=["carbon dioxide", "nitrogen", "water vapour"], ref="4.13"),
    D(mq="Why is carbon monoxide toxic?", c="it reduces the capacity of the blood to carry oxygen", w=["it is acidic", "it causes global warming", "it makes the blood alkaline"], ref="4.13", d="4-6"),
    D(mq="Which pollutant is formed from impurities in fuels?", c="sulfur dioxide", w=["carbon monoxide", "nitrogen monoxide", "water"], ref="4.15"),
    D(mq="Why do nitrogen oxides form in car engines?", c="the high temperature makes nitrogen and oxygen from the air react", w=["fuel contains nitrogen", "nitrogen is formed by cracking",
      "petrol contains nitrogen compounds"], ref="4.14", d="4-6"),
    D(mq="What are the conditions for catalytic cracking?", c="about 600–700 °C with a silica or alumina catalyst", w=["room temperature with a nickel catalyst",
      "high pressure with yeast", "UV light"], ref="4.17", d="4-6"),
    D(mq="What are the products of cracking a long-chain alkane?", c="shorter alkanes and alkenes", w=["only alkenes", "carbon dioxide and water", "only methane"], ref="4.17"),
    D(mq="Why is cracking carried out?", c="to match supply of fractions with demand for them", w=["to make crude oil", "to remove sulfur", "to make longer chains"], ref="4.18"),
    D(mq="Which property increases from the gasoline fraction to the fuel oil fraction?", c="boiling point", w=["flammability", "volatility", "how easily it ignites"], ref="4.10", d="4-6"),
], intro="This question is about crude oil and fuels.", tag="org_crude")

facts(CR, "4.7", [
    D(q="An oil refinery splits crude oil into groups of hydrocarbons with similar boiling points. Name this process.", a="fractional distillation"),
    D(q="State what is meant by a **fuel**.", a="a substance that releases heat energy when it is burned", ref="4.11"),
    D(q="Name the products of the complete combustion of a hydrocarbon.", m=2, pts=["carbon dioxide", "water"], ref="4.12"),
    D(q="Name two products of the incomplete combustion of a hydrocarbon that are not formed in complete combustion.", m=2, pts=["carbon monoxide", "carbon / soot"], ref="4.12"),
    D(q="Ships and some power stations burn one of the heavier crude oil fractions. Name this fraction.", a="fuel oil", ref="4.9"),
    D(q="Give one use of the refinery gases fraction.", a="bottled gas / cooking / heating", ref="4.9"),
    D(q="Name the two pollutant gases that cause acid rain.", m=2, pts=["sulfur dioxide", "nitrogen oxides"], ref="4.16"),
    D(q="Give one problem caused by acid rain.", a="damages buildings/statues / kills fish/trees / acidifies lakes", ref="4.16"),
    D(q="Give the colour trend of the fractions from refinery gases to bitumen.", a="they get darker (colourless/pale to black)", ref="4.10"),
    D(q="Name the catalyst used in catalytic cracking.", a="silica / alumina / zeolite", ref="4.17"),
    D(q="Give one reason why the gasoline fraction is in high demand.", a="it is used as fuel for cars (petrol)", ref="4.18"),
], intro="This question is about fractions from crude oil.", tag="org_crude2")

items(CR, "describe", "4.8", [
    D(s="Describe how crude oil is separated into fractions.", m=4,
      p=["crude oil is heated / vaporised", "vapour rises up the fractionating column", "column is hotter at the bottom and cooler at the top",
         "fractions condense at different heights according to boiling point"], figs=[fig(S.fractional_column(), 90, caption="Fractionating column")]),
    D(s="Describe how the boiling point, colour and viscosity change from the gasoline fraction to the bitumen fraction.", m=3,
      p=["boiling point increases", "colour gets darker", "viscosity increases / gets thicker"], ref="4.10"),
    D(s="Describe how sulfur dioxide from burning fuels leads to acid rain.", m=3, p=["sulfur impurities in fuel burn to form sulfur dioxide", "sulfur dioxide dissolves in rain water", "forming acidic solution (sulfurous / sulfuric acid)"], ref=["4.15", "4.16"]),
    D(s="Describe how cracking is carried out in industry.", m=3, p=["long-chain alkanes are heated / vaporised", "passed over a catalyst of silica or alumina", "at about 600–700 °C"], ref="4.17"),
    D(s="Describe how nitrogen oxides are formed in a car engine.", m=2, p=["nitrogen and oxygen from the air", "react at the high temperatures in the engine"], ref="4.14"),
    D(s="Describe what you would see if a candle is burned with a limited supply of air.", m=2, p=["yellow / smoky flame", "black soot forms"], ref="4.12", d="4-6"),
    D(s="Describe how you could show in the laboratory that a long-chain alkane can be cracked.", m=3,
      p=["heat liquid paraffin (on mineral wool) and pass the vapour over hot broken porcelain / aluminium oxide", "collect the gas over water", "gas decolourises bromine water: an alkene is formed"], ref="4.17", d="7-9"),
    D(s="Describe the difference between complete and incomplete combustion of a hydrocarbon.", m=3, p=["complete: plenty of oxygen, forms CO₂ and H₂O", "incomplete: limited oxygen", "forms carbon monoxide and/or carbon (soot) and water"], ref="4.12"),
    D(s="Describe why a fractionating column has a temperature gradient.", m=2, p=["hot at the bottom where crude oil vapour enters", "cooler at the top, so each fraction condenses at its own level"], ref="4.8", d="4-6"),
    D(s="Describe two effects of acid rain on the environment.", m=2, p=["lakes become acidic / fish die", "trees damaged / leaves die", "limestone buildings / statues corrode", "metal structures corrode"], any=True, ref="4.16"),
], tag="org_crude")

items(CR, "explain", "4.10", [
    D(s="Explain why the different fractions condense at different heights in the fractionating column.", m=2, p=["they have different boiling points", "each condenses when the temperature falls below its boiling point"], ref="4.8"),
    D(s="Explain why bitumen has a higher boiling point than gasoline.", m=2, p=["bitumen molecules are larger / longer chains", "stronger intermolecular forces to overcome"]),
    D(s="Explain why carbon monoxide is dangerous.", m=2, p=["it is colourless and odourless so cannot be detected", "it combines with haemoglobin, reducing oxygen carried by the blood"], ref="4.13"),
    D(s="Explain why cracking is needed in an oil refinery.", m=2, p=["more long-chain fractions are produced than are needed", "short-chain fractions such as gasoline are in greater demand"], ref="4.18"),
    D(s="Explain why cracking produces alkenes as well as alkanes.", m=2, p=["there are not enough hydrogen atoms to make only alkanes", "so some products must have C=C double bonds"], ref="4.17", d="7-9"),
    D(s="Explain why fuels with short chains are more flammable than those with long chains.", m=2, p=["short chains have lower boiling points / are more volatile", "they vaporise easily and ignite"], d="4-6"),
    D(s="Explain why incomplete combustion occurs in a gas fire with a blocked air vent.", m=2, p=["not enough oxygen reaches the fuel", "so carbon monoxide / soot forms instead of carbon dioxide"], ref="4.12", d="4-6"),
    D(s="Explain how catalytic converters reduce pollution from cars.", m=2, p=["convert carbon monoxide to carbon dioxide", "convert nitrogen oxides to nitrogen (and oxygen)"], ref="4.14", d="7-9"),
    D(s="Explain why removing sulfur from fuels reduces acid rain.", m=2, p=["less sulfur dioxide is produced when the fuel burns", "so less acid forms in rain water"], ref="4.16"),
    D(s="Explain why the gases at the top of the column are not liquids at room temperature.", m=2, p=["they have very small molecules / short chains", "boiling points below room temperature"], ref="4.10", d="4-6"),
    D(s="Explain why burning fuels with a smoky flame wastes energy.", m=2, p=["incomplete combustion", "less energy is released than in complete combustion"], ref="4.12", d="7-9"),
], tag="org_crude")

CRACK = [(10, 8, 2), (12, 8, 4), (14, 10, 4), (16, 12, 4), (10, 6, 4), (12, 10, 2), (8, 6, 2), (14, 8, 6), (18, 14, 4), (15, 11, 4),
         (13, 9, 4), (11, 7, 4)]


@tpl(CR, "equation", 30)
def crude_equations(r, k):
    kind = k % 3
    if kind == 0:  # cracking (C)
        n, a, e = CRACK[(k // 3) % len(CRACK)]
        if e == 4 and r.random() < 0.5:
            eq = f"{alkane(n)}(g) -> {alkane(a)}(g) + 2{alkene(2)}(g)"
        elif e == 6:
            eq = f"{alkane(n)}(g) -> {alkane(a)}(g) + 2{alkene(3)}(g)"
        else:
            eq = f"{alkane(n)}(g) -> {alkane(a)}(g) + {alkene(e)}(g)"
        import chemistry_util as U
        L_, R_ = U.eq_terms(eq)
        unk = R_[-1][1]
        shown = eq.replace(f"{R_[-1][1]}(g)", "X")
        stem = (f"A molecule of {F(alkane(n))} is cracked:\n\n{F(shown.replace('->', '→').replace('(g)', ''))}\n\n"
                "(i) Deduce the formula of X.\n\n(ii) State the homologous series to which X belongs.")
        rows = [row("", f"M1 {F(unk)}", 1, "use of atom conservation", "AO2"), row("", "M2 alkenes", 1, None, "AO1")]
        return Q("Deduce", "4-6", [P("", stem, 2, lines=3)], rows, ["4.17"], ao=["AO2"], ans=("atom balance", {"X": unk, "eq": EQ(eq)}))
    if kind == 1:  # complete combustion
        n = 1 + (k // 3) % 8
        h = 2 * n + 2
        o2 = Fr(2 * n + (n + 1), 2)
        eq = f"{'2' if o2.denominator == 2 else ''}{alkane(n)}(g) + {num(o2 * (2 if o2.denominator == 2 else 1))}O2(g) -> {n * (2 if o2.denominator == 2 else 1)}CO2(g) + {(n + 1) * (2 if o2.denominator == 2 else 1)}H2O(l)"
        eq = eq.replace(" 1O2", " O2").replace("> 1CO2", "> CO2")
        name = STEM[n] + "ane"
        stem = f"Write a balanced equation for the complete combustion of {name}, {F(alkane(n))}."
        rows = [row("", f"M1 formulae of products CO₂ and H₂O", 1, None, "AO2"), row("", f"M2 {EQ(eq, states=False)}", 1, "ALLOW fractions / multiples; IGNORE state symbols", "AO2")]
        return Q("Write", "4-6" if n < 4 else "7-9", [P("", stem, 2, lines=2)], rows, ["4.12", "4.19"], ao=["AO2"], ans=("balance", {"equation": EQ(eq, states=False)}))
    # incomplete combustion to CO
    n = 1 + (k // 3) % 6
    o2 = Fr(n + (n + 1), 2)
    m = 2 if o2.denominator == 2 else 1
    eq = f"{m if m > 1 else ''}{alkane(n)}(g) + {num(o2 * m)}O2(g) -> {n * m}CO(g) + {(n + 1) * m}H2O(l)"
    eq = eq.replace(" 1O2", " O2").replace("> 1CO", "> CO")
    stem = f"Write a balanced equation for the incomplete combustion of {STEM[n]}ane, {F(alkane(n))}, to form carbon monoxide and water only."
    rows = [row("", f"M1 CO and H₂O as products", 1, None, "AO2"), row("", f"M2 {EQ(eq, states=False)}", 1, "ALLOW multiples / fractions", "AO2")]
    return Q("Write", "7-9", [P("", stem, 2, lines=2)], rows, ["4.12", "4.13"], ao=["AO2"], ans=("balance", {"equation": EQ(eq, states=False)}))


extended(CR, "4.8", [
    D(s="Describe how crude oil is separated into useful fractions and explain why the fractions have different properties.",
      ind=["crude oil heated until most vaporises", "vapour enters near the bottom of a fractionating column", "temperature decreases up the column", "hydrocarbons condense when they reach a level below their boiling point",
           "small molecules (refinery gases) leave at the top; bitumen at the bottom", "larger molecules: stronger intermolecular forces, higher boiling points", "larger molecules are more viscous and darker"]),
    D(s="Explain how burning fossil fuels causes environmental problems. Include the pollutants formed and how each is produced.",
      ind=["complete combustion releases carbon dioxide: greenhouse gas / climate change", "incomplete combustion gives carbon monoxide: toxic", "and soot / particulates", "sulfur impurities burn to sulfur dioxide",
           "high engine temperatures: nitrogen + oxygen form nitrogen oxides", "sulfur dioxide and nitrogen oxides dissolve in rain: acid rain", "effects of acid rain on lakes, trees, buildings"], ref=["4.12", "4.14", "4.15", "4.16"], d="7-9"),
    D(s="Explain why cracking is carried out, describe the conditions used and give an example equation.",
      ind=["fractional distillation gives more long-chain hydrocarbons than needed", "demand is greater for shorter fractions such as gasoline", "cracking breaks long alkanes into shorter alkanes and alkenes",
           "conditions: 600–700 °C, silica or alumina catalyst", "e.g. C₁₀H₂₂ → C₈H₁₈ + C₂H₄", "alkenes used to make polymers", "matches supply with demand"], ref=["4.17", "4.18"]),
    D(intro="The table shows the supply and demand for some crude oil fractions, as a percentage of the total.",
      figs=[table(["Fraction", "Supply in %", "Demand in %"], [["refinery gases", "4", "6"], ["gasoline", "16", "29"], ["kerosene", "13", "9"], ["diesel", "19", "26"], ["fuel oil and bitumen", "48", "30"]])],
      s="Use the data to explain why oil companies crack some fractions. Describe how cracking is done and what is formed.",
      ind=["demand for gasoline (29%) and diesel greater than supply", "supply of fuel oil and bitumen (48%) greater than demand (30%)", "cracking breaks the surplus long chains into shorter, more useful molecules",
           "heat and vaporise, pass over hot silica / alumina catalyst at about 650 °C", "products: shorter alkanes (e.g. for petrol) and alkenes", "alkenes used to make polymers / ethanol", "e.g. C₁₂H₂₆ → C₁₀H₂₂ + C₂H₄"], ref=["4.17", "4.18"], d="7-9"),
    D(s="Compare complete and incomplete combustion of hydrocarbon fuels and explain why incomplete combustion is dangerous and wasteful.",
      ind=["complete: excess oxygen; products CO₂ and H₂O", "e.g. CH₄ + 2O₂ → CO₂ + 2H₂O", "incomplete: limited oxygen; products CO and/or C and H₂O", "carbon monoxide is toxic: binds to haemoglobin, less oxygen carried",
           "CO is colourless and odourless", "soot: blackens appliances and can cause breathing problems", "less energy released per gram of fuel"], ref=["4.12", "4.13"], d="4-6"),
    D(s="Describe the names, uses and trend in properties of the main fractions obtained from crude oil.",
      ind=["refinery gases: bottled gas / heating", "gasoline: petrol for cars", "kerosene: aircraft fuel", "diesel: lorries / trains", "fuel oil: ships / power stations", "bitumen: roads / roofs",
           "from top to bottom: boiling point and viscosity increase, colour darker, chains longer"], ref=["4.9", "4.10"], d="4-6"),
    D(s="Explain how acid rain forms and describe ways of reducing it.",
      ind=["fuels contain sulfur impurities", "sulfur burns to sulfur dioxide", "nitrogen oxides form in hot engines", "these dissolve in rainwater forming acids", "remove sulfur from fuels before burning",
           "catalytic converters remove nitrogen oxides", "use renewable energy / burn less fossil fuel"], ref=["4.14", "4.15", "4.16"], d="4-6"),
    D(s="A student says that diesel is a better fuel than refinery gases because it has longer molecules. Evaluate this statement by comparing the properties of the two fractions.",
      ind=["diesel has longer chains so releases more energy per molecule", "refinery gases ignite easily (low boiling point, very volatile)", "diesel is less flammable / harder to ignite: safer to store",
           "diesel is a liquid: easy to transport in tanks", "gases need pressurised cylinders", "longer chains more likely to burn incompletely: soot, CO", "best fuel depends on use; both release CO₂"], ref=["4.10", "4.11"], d="7-9"),
    D(s="Describe an experiment to crack liquid paraffin in the laboratory, including how to test the gaseous product and the safety precautions.",
      ind=["paraffin soaked into mineral wool in a boiling tube", "strongly heat broken porcelain / aluminium oxide catalyst", "vapour passes over hot catalyst", "collect gas in test tubes over water",
           "add bromine water: orange to colourless shows an alkene", "remove delivery tube from water before stopping heating (suck back)", "eye protection; flammable gas"], ref="4.17", d="7-9"),
    D(s="Explain why the boiling point of hydrocarbons increases with chain length and how this allows crude oil to be separated.",
      ind=["longer chains have higher relative molecular mass", "stronger intermolecular forces", "more energy needed to separate molecules: higher boiling point", "crude oil is a mixture with a range of boiling points",
           "fractionating column is hot at bottom and cool at top", "each fraction condenses where the temperature equals its boiling range", "fractions are mixtures of hydrocarbons with similar chain lengths"], ref=["4.8", "4.10"], d="7-9"),
    D(s="Explain why it is important that gas boilers in homes are serviced regularly.",
      ind=["methane burns completely in plenty of air: CO₂ and H₂O", "blocked vents / faulty burner reduce air supply", "incomplete combustion produces carbon monoxide", "CO is toxic: reduces oxygen carried by blood",
           "CO cannot be seen or smelled: detectors needed", "soot builds up, reducing efficiency", "wasted energy and higher cost"], ref=["4.12", "4.13"], d="4-6"),
    D(s="Explain how the use of fossil fuels contributes to climate change and suggest how emissions could be reduced.",
      ind=["burning hydrocarbons produces carbon dioxide", "CO₂ is a greenhouse gas", "absorbs infrared radiation from the Earth", "increased CO₂ levels linked to rising temperatures",
           "consequences: sea level rise, extreme weather", "reduce by using renewable energy / electric vehicles", "improve efficiency / carbon capture"], ref=["4.12", "2.13"], d="4-6"),
], tag="crude")

# =================================================================== 4(c) alkanes
facts(AK, "4.19", [
    D(mq="What is the molecular formula of the alkane with five carbon atoms?", c="C5H12", w=["C5H10", "C5H8", "C5H14"]),
    D(mq="Why are alkanes described as saturated?", c="they contain only single carbon–carbon bonds", w=["they contain a double bond", "they dissolve in water", "they are fully oxidised"], ref="4.20"),
    D(mq="What is needed for methane to react with chlorine?", c="ultraviolet light", w=["a nickel catalyst", "a temperature of 1000 °C", "yeast"], ref="4.22"),
    D(mq="What are the products when methane reacts with bromine in UV light?", c="bromomethane and hydrogen bromide", w=["bromomethane and hydrogen", "dibromoethane only", "carbon dioxide and water"], ref="4.22", d="4-6"),
    D(mq="How many hydrogen atoms are in a molecule of octane?", c="18", w=["16", "8", "20"], d="4-6"),
    D(mq="Which compound is an alkane?", c="C3H8", w=["C3H6", "C2H4", "C4H8"]),
    D(mq="What is the name of the alkane with four carbon atoms?", c="butane", w=["propane", "pentane", "butene"], ref="4.21"),
    D(mq="Which is the name of the branched isomer of butane?", c="methylpropane", w=["2-methylbutane", "ethylethane", "dimethylethane"], ref="4.21", d="7-9"),
    D(mq="Which statement about alkanes is correct?", c="they burn to form carbon dioxide and water", w=["they decolourise bromine water quickly", "they polymerise easily", "they react with water to form alcohols"]),
    D(mq="Which type of reaction occurs between an alkane and a halogen?", c="substitution", w=["addition", "neutralisation", "polymerisation"], ref="4.22"),
    D(mq="What is the formula of the product when one hydrogen in ethane is replaced by chlorine?", c="C2H5Cl", w=["C2H6Cl", "C2H4Cl", "CH3Cl"], ref="4.22", d="4-6"),
    D(mq="What is the Mr of propane, C3H8?", c="44", w=["42", "36", "46"], d="1-3"),
], intro="This question is about the alkanes.", tag="org_alk")


@tpl(AK, "recall", 14)
def alkanes_recall(r, k):
    n = 1 + k % 7
    nm = STEM[n] + "ane"
    parts = [P("a", f"Give the molecular formula of {nm}.", 1, lines=1),
             P("b", f"Draw the displayed formula of {nm}.", 1, space="box"),
             P("c", f"Name the product, other than hydrogen chloride, formed when {nm} reacts with chlorine in UV light (one hydrogen replaced).", 1, lines=1)]
    pref = {1: "chloromethane", 2: "chloroethane", 3: "1-chloropropane", 4: "1-chlorobutane", 5: "1-chloropentane", 6: "1-chlorohexane", 7: "1-chloroheptane"}[n]
    rows = [row("a", F(alkane(n)), 1, None, "AO1"), row("b", f"all {n} C atoms in a chain with single bonds and {2 * n + 2} H atoms, each H with one bond", 1, "IGNORE bond angles", "AO1"),
            row("c", pref, 1, "ALLOW other isomers for n ≥ 3, e.g. 2-chloro..." if n >= 3 else None, "AO2")]
    if k >= 7:
        parts[1] = P("b", f"State why {nm} is described as saturated.", 1, lines=2)
        rows[1] = row("b", "only single (C–C) bonds / no double bonds", 1, None, "AO1")
    return Q("Give", "4-6", parts, rows, ["4.19", "4.21", "4.22"], ao=["AO1"], ans=("rules", {"formula": alkane(n), "product": pref}))


items(AK, "explain", "4.20", [
    D(s="Explain why alkanes are described as saturated hydrocarbons.", m=2, p=["contain only carbon and hydrogen", "only single bonds between carbon atoms"]),
    D(s="Explain why the reaction between methane and chlorine needs UV light.", m=2, p=["UV light provides energy", "to break the Cl–Cl bond / start the reaction"], ref="4.22", d="7-9"),
    D(s="Explain why the reaction between ethane and bromine can give a mixture of products.", m=2, p=["more than one hydrogen can be substituted", "giving C₂H₅Br, C₂H₄Br₂ etc."], ref="4.22", d="7-9"),
    D(s="Explain why alkanes are used as fuels but not as starting materials for making polymers.", m=2, p=["alkanes release lots of energy when burned", "they are saturated / have no C=C so cannot undergo addition polymerisation"], d="4-6"),
    D(s="Explain why alkanes do not decolourise bromine water in the dark.", m=2, p=["alkanes are saturated / no C=C double bond", "so no addition reaction can occur"], ref="4.28"),
    D(s="Explain why pentane and 2-methylbutane have different boiling points.", m=2, p=["they have different shapes / branched vs straight chain", "different strength of intermolecular forces (branched lower)"], ref="4.21", d="7-9"),
    D(s="Explain why the formula C₄H₁₀ represents more than one compound.", m=2, p=["the atoms can be arranged in different ways", "straight-chain butane and branched methylpropane / isomers"], ref="4.21"),
    D(s="Explain how you know that C₉H₂₀ is an alkane.", m=2, p=["fits the general formula CnH2n+2", "2 × 9 + 2 = 20"], d="4-6"),
    D(s="Explain why the reaction of methane with chlorine is a substitution reaction.", m=2, p=["a hydrogen atom in methane is replaced", "by a chlorine atom"], ref="4.22"),
    D(s="Explain why the boiling points of the alkanes increase with the number of carbon atoms.", m=2, p=["molecules get bigger", "stronger intermolecular forces need more energy to overcome"]),
    D(s="Explain why alkanes are fairly unreactive compared with alkenes.", m=2, p=["C–C and C–H single bonds are strong / no double bond", "alkenes have a reactive C=C that allows addition"], d="7-9"),
    D(s="Explain why hexane is a liquid at room temperature but methane is a gas.", m=2, p=["hexane molecules are larger", "stronger intermolecular forces so higher boiling point (above room temperature)"], d="4-6"),
], tag="org_alk")

HALS = [("Cl", "chlorine", "chloro", "hydrogen chloride"), ("Br", "bromine", "bromo", "hydrogen bromide")]


@tpl(AK, "equation", 16)
def alkanes_subst_eq(r, k):
    n = 1 + k % 4
    hx, hn, pre, hhx = HALS[(k // 4) % 2]
    prod = cf(n, 2 * n + 1, hx)
    eq = f"{alkane(n)}(g) + {hx}2(g) -> {prod}(g) + H{hx}(g)"
    name = ("" if n < 3 else "1-") + pre + STEM[n] + "ane"
    if (k // 8) % 2 == 0:
        stem = f"Write the equation for the reaction of {STEM[n]}ane with {hn} in ultraviolet light to form {name}."
        rows = [row("", f"M1 {F(prod)} and H{hx}", 1, None, "AO2"), row("", f"M2 {EQ(eq, states=False)}", 1, "IGNORE state symbols", "AO2")]
        return Q("Write", "4-6", [P("", stem, 2, lines=2)], rows, ["4.22"], ao=["AO2"], ans=("balance", {"equation": EQ(eq, states=False)}))
    stem = (f"{STEM[n].capitalize()}ane reacts with {hn} in ultraviolet light.\n\n(i) Name the type of reaction.\n\n"
            f"(ii) Write the equation for the reaction that forms one organic product with one {hn} atom.\n\n(iii) Name the inorganic product.")
    rows = [row("", "M1 (i) substitution", 1, None, "AO1"), row("", f"M2 (ii) {EQ(eq, states=False)}", 1, None, "AO2"), row("", f"M3 (iii) {hhx}", 1, None, "AO1")]
    return Q("Write", "4-6", [P("", stem, 3, lines=5)], rows, ["4.22", "4.6"], ao=["AO2"], ans=("balance", {"equation": EQ(eq, states=False)}))


# =================================================================== 4(d) alkenes
facts(AE, "4.23", [
    D(mq="What is the functional group of the alkenes?", c="C=C", w=["C–C", "–OH", "–COOH"]),
    D(mq="What is the general formula of the alkenes?", c="CnH2n", w=["CnH2n+2", "CnH2n+1OH", "CnH2n-2"], ref="4.24"),
    D(mq="What is observed when ethene is bubbled through bromine water?", c="orange to colourless", w=["colourless to orange", "no change", "orange to purple"], ref="4.28"),
    D(mq="What is the product when ethene reacts with bromine?", c="1,2-dibromoethane", w=["bromoethane", "1,1-dibromoethane", "ethane"], ref="4.27", d="4-6"),
    D(mq="Why are alkenes described as unsaturated?", c="they contain a carbon–carbon double bond", w=["they contain only single bonds", "they contain oxygen", "they are not soluble"], ref="4.25"),
    D(mq="What is the molecular formula of butene?", c="C4H8", w=["C4H10", "C4H6", "C3H6"], ref="4.24"),
    D(mq="Which compound decolourises bromine water?", c="propene", w=["propane", "ethane", "methane"], ref="4.28"),
    D(mq="Which is the name of CH3CH=CHCH3?", c="but-2-ene", w=["but-1-ene", "butane", "propene"], ref="4.26", d="4-6"),
    D(mq="What type of reaction occurs between an alkene and bromine?", c="addition", w=["substitution", "combustion", "cracking"], ref="4.27"),
    D(mq="How many straight-chain isomers of pentene are there?", c="2", w=["1", "3", "4"], ref="4.26", d="7-9"),
    D(mq="What is the formula of the product of propene and bromine?", c="C3H6Br2", w=["C3H7Br", "C3H8Br2", "C3H5Br"], ref="4.27", d="4-6"),
    D(mq="Which hydrocarbon is an alkene?", c="C5H10", w=["C5H12", "C6H14", "C2H6"], ref="4.24"),
], intro="This question is about the alkenes.", tag="org_ene")


@tpl(AE, "recall", 20)
def alkenes_recall(r, k):
    n = 2 + k % 5
    pos = 1 if n < 4 or (k // 5) % 2 == 0 else 2
    if k >= 10:
        n = 2 + (k - 10) % 5
        pos = 1 if n < 4 or (k - 10) // 5 == 0 else 2
    nm = STEM[n] + ("ene" if n < 4 else f"-{pos}-ene")
    at, bonds = S.chain(n, double_at=pos - 1)
    svg = S.displayed(at, bonds)
    prod = {2: "1,2-dibromoethane", 3: "1,2-dibromopropane"}.get(n, f"{pos},{pos + 1}-dibromo{STEM[n]}ane")
    cq = "Name the product formed when it reacts with bromine."
    if k >= 10:
        cq, prod = "Name the product formed when it reacts with hydrogen in the presence of a nickel catalyst.", STEM[n] + "ane"
    parts = [P("a", "Name this compound.", 1, lines=1), P("b", "Give its molecular formula.", 1, lines=1), P("c", cq, 1, lines=1)]
    rows = [row("a", nm, 1, "IGNORE missing hyphens" if n >= 4 else None, "AO1"), row("b", F(alkene(n)), 1, None, "AO1"), row("c", prod, 1, None, "AO2")]
    parts[0]["figures"] = [fig(svg, 70)]
    return Q("Name", "4-6" if n > 3 else "1-3", parts, rows, ["4.26", "4.27"], ao=["AO1"], ans=("rules", {"name": nm, "product": prod}),
             intro="The displayed formula of a hydrocarbon is shown.")


items(AE, "describe", "4.28", [
    D(s="Describe how bromine water can be used to distinguish between {a} and {b}.", m=3, p=["add bromine water to each and shake", "{b} turns it from orange to colourless", "{a}: stays orange"],
      v=[{"a": "hexane", "b": "hex-1-ene"}, {"a": "ethane", "b": "ethene"}, {"a": "propane", "b": "propene"}, {"a": "pentane", "b": "pent-2-ene"}]),
    D(s="Describe the structure of an ethene molecule.", m=2, p=["two carbon atoms joined by a double bond", "each carbon bonded to two hydrogen atoms"], ref="4.23"),
    D(s="Describe what happens to the bonding when ethene reacts with bromine.", m=2, p=["the double bond breaks / becomes a single bond", "one bromine atom adds to each carbon atom"], ref="4.27", d="4-6"),
    D(s="Describe the differences between an alkane and an alkene with the same number of carbon atoms.", m=3,
      p=["alkene has a C=C double bond, alkane only single bonds", "alkene has two fewer hydrogen atoms (CnH2n vs CnH2n+2)", "alkene decolourises bromine water; alkane does not"], d="4-6"),
    D(s="Describe how you could show that the gas formed by cracking contains an alkene.", m=2, p=["bubble the gas through bromine water", "orange colour disappears"], ref="4.28"),
    D(s="Describe the structural isomers of butene that have straight chains.", m=2, p=["but-1-ene: double bond between C1 and C2", "but-2-ene: double bond between C2 and C3"], ref="4.26", d="7-9"),
    D(s="Describe the meaning of the number in the name pent-2-ene.", m=1, p=["the double bond starts at carbon atom 2"], ref="4.26", d="4-6"),
    D(s="Describe how the formula of an alkene changes as you go from one member of the series to the next.", m=1, p=["it increases by CH₂"], ref="4.24"),
    D(s="Describe one industrial use of alkenes.", m=1, p=["making polymers / poly(ethene)", "making ethanol"], any=True),
    D(s="Describe the result of adding bromine water to a sample of cyclohexane and of hex-1-ene. Explain the difference.", m=3,
      p=["cyclohexane: no change, stays orange", "hex-1-ene: decolourised", "hex-1-ene is unsaturated (C=C); cyclohexane saturated"], ref="4.28", d="7-9"),
], tag="org_ene")


@tpl(AE, "equation", 16)
def alkenes_add_eq(r, k):
    n = 2 + k % 4
    kind = (k // 4) % 4
    a = alkene(n)
    if kind == 0:
        eq, nm, cond = f"{a}(g) + Br2(aq) -> {cf(n, 2 * n, 'Br2')}(l)", "bromine", None
    elif kind == 1:
        eq, nm, cond = f"{a}(g) + H2(g) -> {alkane(n)}(g)", "hydrogen", "nickel catalyst, about 150 °C"
    elif kind == 2:
        eq, nm, cond = f"{a}(g) + H2O(g) -> {cf(n, 2 * n + 1, 'OH')}(g)", "steam", "phosphoric acid catalyst, 300 °C, 60–70 atm"
    else:
        eq, nm, cond = f"{a}(g) + 3{'/2' if False else ''}O2(g) -> 2CO2(g) + 2H2O(l)" if n == 2 else f"2{a}(g) + {3 * n}O2(g) -> {2 * n}CO2(g) + {2 * n}H2O(l)", "oxygen", None
    name = STEM[n] + ("ene" if n < 4 else "-1-ene")
    stem = f"Write a balanced equation for the reaction of {name} with {nm}" + (f" ({cond})." if cond else ".")
    if kind == 2:
        refs = ["4.32C"]
    elif kind == 0:
        refs = ["4.27"]
    else:
        refs = ["4.23", "4.12"] if kind == 3 else ["4.23"]
    rows = [row("", f"M1 correct product formula(e)", 1, None, "AO2"), row("", f"M2 {EQ(eq, states=False)}", 1, "ALLOW structural formulae; IGNORE state symbols", "AO2")]
    return Q("Write", "4-6", [P("", stem, 2, lines=2)], rows, refs, ao=["AO2"], ans=("balance", {"equation": EQ(eq, states=False)}))


# =================================================================== 4(e) alcohols (C)
facts(AL, "4.29C", [
    D(mq="What is the functional group of the alcohols?", c="–OH", w=["–COOH", "C=C", "–COO–"]),
    D(mq="Which is the formula of propan-1-ol?", c="CH3CH2CH2OH", w=["CH3CH2OH", "CH3CH2COOH", "CH3CH(OH)CH3"], ref="4.30C"),
    D(mq="What are the conditions for fermentation?", c="yeast, absence of air, about 30 °C", w=["phosphoric acid, 300 °C, 60 atm", "UV light", "nickel catalyst, 150 °C"], ref="4.31C"),
    D(mq="Which product is formed when ethanol is oxidised by acidified potassium dichromate(VI)?", c="ethanoic acid", w=["ethene", "ethane", "ethyl ethanoate"], ref="4.31C"),
    D(mq="What colour change is seen when ethanol is warmed with acidified potassium dichromate(VI)?", c="orange to green", w=["green to orange", "purple to colourless", "colourless to pink"], ref="4.31C", d="4-6"),
    D(mq="What is made when ethanol is heated with aluminium oxide?", c="ethene", w=["ethanoic acid", "ethane", "ethanal only"], ref="4.32C", d="4-6"),
    D(mq="Why is fermentation carried out without air?", c="to stop the ethanol being oxidised to ethanoic acid", w=["so yeast can breathe", "to speed up the reaction", "to keep the mixture warm"], ref="4.33C", d="7-9"),
    D(mq="Why is fermentation carried out at about 30 °C rather than 70 °C?", c="higher temperatures denature the enzymes in yeast", w=["ethanol boils at 30 °C", "yeast works fastest at 70 °C", "lower temperatures give oxygen"], ref="4.33C", d="4-6"),
    D(mq="What is the molecular formula of butan-1-ol?", c="C4H9OH", w=["C4H10OH", "C4H8OH", "C3H7OH"], ref="4.30C"),
    D(mq="Which gas is produced during fermentation?", c="carbon dioxide", w=["oxygen", "hydrogen", "ethene"], ref="4.32C"),
    D(mq="Which statement about making ethanol from ethene is correct?", c="it is a continuous process giving pure ethanol", w=["it uses renewable raw materials", "it needs yeast",
      "it gives a dilute solution of ethanol"], ref="4.32C", d="7-9"),
    D(mq="Which microbe oxidation product makes wine taste sour when left open?", c="ethanoic acid", w=["ethanol", "carbon dioxide", "ethene"], ref="4.31C", d="4-6"),
], intro="This question is about alcohols.", tag="org_alc")

facts(AL, "4.29C", [
    D(q="Name the alcohol with the formula CH₃OH.", a="methanol", ref="4.30C"),
    D(q="Give the three conditions needed for fermentation.", m=3, pts=["yeast", "no air / anaerobic", "about 30 °C (25–40 °C)"], ref="4.33C"),
    D(q="Name the catalyst used when ethene reacts with steam.", a="phosphoric acid", ref="4.32C"),
    D(q="Give the temperature and pressure used for the hydration of ethene.", m=2, pts=["300 °C", "60–70 atm"], ref="4.32C"),
    D(q="Name the reagent used to oxidise ethanol to ethanoic acid in the laboratory.", a="acidified potassium dichromate(VI)", ref="4.31C"),
    D(q="Name the products of the complete combustion of ethanol.", m=2, pts=["carbon dioxide", "water"], ref="4.31C"),
    D(q="Give one advantage of making ethanol by fermentation rather than from ethene.", a="uses renewable raw materials (sugar) / low temperature (less energy)", ref="4.32C", d="4-6"),
    D(q="Give one advantage of making ethanol from ethene rather than by fermentation.", a="fast / continuous / pure product", ref="4.32C", d="4-6"),
    D(q="Name the catalyst used to dehydrate ethanol to ethene.", a="(hot) aluminium oxide / alumina", ref="4.32C"),
    D(q="Name the process used to obtain more concentrated ethanol from the fermented mixture.", a="fractional distillation"),
], intro="This question is about ethanol.", tag="org_alc2")

items(AL, "explain", "4.33C", [
    D(s="Explain why fermentation is carried out at about 30 °C.", m=2, p=["at lower temperatures the reaction is too slow", "at higher temperatures enzymes in yeast are denatured"]),
    D(s="Explain why air is kept out of the fermentation vessel.", m=2, p=["oxygen / microbes in air would oxidise ethanol", "to ethanoic acid (vinegar)"]),
    D(s="Explain why fermentation stops when the ethanol concentration reaches about 15%.", m=2, p=["ethanol is toxic to yeast", "yeast dies / enzymes stop working"], d="7-9"),
    D(s="Explain why ethanol made from ethene is not a renewable fuel but ethanol from sugar cane is.", m=2, p=["ethene comes from crude oil, which is finite", "sugar cane can be regrown"], ref="4.32C"),
    D(s="Explain why the reaction of ethene with steam is described as an addition reaction.", m=2, p=["two molecules combine to make one product", "water adds across the C=C"], ref="4.32C"),
    D(s="Explain why the dehydration of ethanol is the reverse of the hydration of ethene.", m=2, p=["dehydration removes water from ethanol to give ethene", "hydration adds water to ethene to give ethanol"], ref="4.32C", d="7-9"),
    D(s="Explain why propan-1-ol has similar chemical reactions to ethanol.", m=2, p=["both contain the –OH functional group", "same homologous series"], ref="4.29C"),
    D(s="Explain why the colour change with acidified potassium dichromate(VI) shows that ethanol has been oxidised.", m=2, p=["dichromate(VI) is an oxidising agent", "orange dichromate is reduced to green chromium(III) as ethanol is oxidised"], ref="4.31C", d="7-9"),
    D(s="Explain why a fermentation flask is fitted with an airlock or a delivery tube into limewater.", m=2, p=["lets carbon dioxide escape (or shows it is made)", "but stops air getting in"], d="4-6"),
    D(s="Explain why ethanol burns with a clean, blue flame.", m=2, p=["complete combustion", "it already contains oxygen / small molecule so little soot"], ref="4.31C", d="7-9"),
], tag="org_alc")

ALC = [(1, "methanol"), (2, "ethanol"), (3, "propan-1-ol"), (4, "butan-1-ol")]


@tpl(AL, "equation", 24)
def alcohols_eq(r, k):
    n, nm = ALC[k % 4]
    a = cf(n, 2 * n + 1, "OH")
    kind = (k // 4) % 6
    if kind == 4:
        o2 = Fr(3 * n, 2)
        m = 2 if o2.denominator == 2 else 1
        eq = f"{m if m > 1 else ''}{a}(l) + {num(o2 * m)}O2(g) -> {n * m if n * m > 1 else ''}CO2(g) + {(n + 1) * m}H2O(l)"
        rows = [row("", "M1 correct formulae", 1, None, "AO2"), row("", "M2 balancing", 1, "ALLOW multiples / fractions", "AO2"), row("", f"M3 state symbols: {EQ(eq)}", 1, None, "AO2")]
        return Q("Write", "7-9", [P("", f"Write a balanced equation, including state symbols, for the burning of liquid {nm} in plenty of air.", 3, lines=2)],
                 rows, ["4.31C"], ao=["AO2"], ans=("balance", {"equation": EQ(eq)}))
    if kind == 5:
        o2 = Fr(2 * n, 2) + Fr(n, 2) - Fr(1, 2) if False else Fr(n + (n + 1) - 1, 2)
        m = 2 if o2.denominator == 2 else 1
        eq = f"{m if m > 1 else ''}{a}(l) + {num(o2 * m)}O2(g) -> {n * m if n * m > 1 else ''}CO(g) + {(n + 1) * m}H2O(l)"
        eq = eq.replace(" 1O2", " O2")
        rows = [row("", "M1 CO and H₂O as products", 1, None, "AO2"), row("", f"M2 {EQ(eq, states=False)}", 1, "ALLOW multiples / fractions", "AO2")]
        return Q("Write", "7-9", [P("", f"In a limited supply of air, {nm} burns to form carbon monoxide and water only. Write a balanced equation for this reaction.", 2, lines=2)],
                 rows, ["4.31C", "4.12"], ao=["AO2"], ans=("balance", {"equation": EQ(eq, states=False)}))
    if kind == 0:
        o2 = Fr(3 * n, 2)
        m = 2 if o2.denominator == 2 else 1
        eq = f"{m if m > 1 else ''}{a}(l) + {num(o2 * m)}O2(g) -> {n * m if n * m > 1 else ''}CO2(g) + {(n + 1) * m}H2O(l)"
        stem = f"Write a balanced equation for the complete combustion of {nm}."
        ref = ["4.31C"]
    elif kind == 1:
        if n == 1:
            return None
        eq = f"{alkene(n)}(g) + H2O(g) -> {a}(g)"
        stem = f"Write an equation for the formation of {nm} by the hydration of an alkene."
        ref = ["4.32C"]
    elif kind == 2:
        if n == 1:
            return None
        eq = f"{a}(g) -> {alkene(n)}(g) + H2O(g)"
        stem = f"Write an equation for the dehydration of {nm} over hot aluminium oxide."
        ref = ["4.32C"]
    else:
        eq = "C6H12O6(aq) -> 2C2H5OH(aq) + 2CO2(g)"
        stem = "Write a balanced equation for the fermentation of glucose, C₆H₁₂O₆."
        ref = ["4.32C"]
        if n != 2:
            stem = f"Write a balanced equation, with state symbols, for the fermentation of glucose, C₆H₁₂O₆. (version {n})"
            return None
    rows = [row("", "M1 correct formulae", 1, None, "AO2"), row("", f"M2 {EQ(eq, states=False)}", 1, "ALLOW multiples; IGNORE state symbols", "AO2")]
    return Q("Write", "4-6" if kind else "7-9", [P("", stem, 2, lines=2)], rows, ref, ao=["AO2"], ans=("balance", {"equation": EQ(eq, states=False)}))


@tpl(AL, "recall", 8)
def alcohols_name_recall(r, k):
    n, nm = ALC[k % 4]
    at, bonds = S.chain(n, subs={(n - 1, "right"): "OH"})
    svg = S.displayed(at, bonds)
    parts = [P("a", "Name the compound shown.", 1, lines=1), P("b", "Give its molecular formula.", 1, lines=1),
             P("c", "Name the organic product of its oxidation by acidified potassium dichromate(VI).", 1, lines=1)]
    acid = {1: "methanoic acid", 2: "ethanoic acid", 3: "propanoic acid", 4: "butanoic acid"}[n]
    parts[0]["figures"] = [fig(svg, 75)]
    if k >= 4:
        parts[2] = P("c", "Name the functional group present.", 1, lines=1)
    rows = [row("a", nm, 1, None, "AO1"), row("b", F(cf(n, 2 * n + 1, "OH")), 1, f"ALLOW {F(cf(n, 2 * n + 2, 'O'))}", "AO1"),
            row("c", acid if k < 4 else "hydroxyl (–OH)", 1, None, "AO2")]
    return Q("Name", "4-6", parts, rows, ["4.30C", "4.31C"], ao=["AO1"], ans=("rules", {"name": nm}))


extended(AL, "4.32C", [
    D(s="Ethanol can be made by fermentation of sugars or by the hydration of ethene. Compare the two methods.",
      ind=["fermentation: glucose → ethanol + carbon dioxide", "yeast, about 30 °C, no air", "slow batch process; impure (dilute) product needs fractional distillation", "uses renewable raw material (sugar cane)",
           "hydration: ethene + steam → ethanol", "phosphoric acid catalyst, 300 °C, 60–70 atm", "fast continuous process; pure product; uses non-renewable crude oil; high energy cost"]),
    D(s="Describe the reactions in which ethanol is oxidised, giving the conditions, observations and products.",
      ind=["combustion in air: burns with a blue flame", "products carbon dioxide and water", "C₂H₅OH + 3O₂ → 2CO₂ + 3H₂O", "microbial oxidation in air: ethanol → ethanoic acid (vinegar)",
           "wine left open turns sour", "acidified potassium dichromate(VI), warm", "orange to green; ethanoic acid formed"], ref="4.31C"),
    D(s="Explain the conditions used for fermentation and describe how a more concentrated solution of ethanol can be obtained from the product.",
      ind=["yeast provides enzymes", "about 30 °C: fast enough but enzymes not denatured", "absence of air: prevents oxidation to ethanoic acid / yeast respires anaerobically", "aqueous solution of sugar",
           "fermentation stops at about 15% ethanol", "fractional distillation separates ethanol (78 °C) from water", "collect fraction at about 78 °C"], ref=["4.33C", "4.32C"]),
    D(s="Describe how ethene can be made from ethanol and how ethanol can be made from ethene. Explain why these reactions are the reverse of each other.",
      ind=["dehydration: pass ethanol vapour over hot aluminium oxide", "C₂H₅OH → C₂H₄ + H₂O", "collect ethene over water; test with bromine water", "hydration: ethene with steam",
           "phosphoric acid catalyst, 300 °C, 60–70 atm", "C₂H₄ + H₂O → C₂H₅OH", "one removes water, the other adds it"], ref="4.32C", d="7-9"),
    D(s="A country has large sugar cane farms but no oil. Evaluate which method of making ethanol fuel it should use.",
      ind=["fermentation uses sugar cane – locally available, renewable", "low temperature: low energy cost", "batch process, slow", "product dilute: needs distillation (energy)", "hydration needs ethene from crude oil – would need imports",
           "hydration is fast and continuous with pure product but high pressure costs", "conclusion: fermentation better for this country; crops grown on farmland is a concern"], ref="4.32C", d="7-9"),
    D(s="Compare the structures and reactions of methanol, ethanol and propan-1-ol.",
      ind=["all contain the –OH functional group", "homologous series: CnH2n+1OH", "each differs by CH₂", "draw displayed formulae / structural formulae", "all burn to carbon dioxide and water",
           "all oxidised by acidified dichromate (orange to green) to carboxylic acids", "boiling points increase with chain length"], ref=["4.29C", "4.30C", "4.31C"], d="4-6"),
    D(s="Describe how you could make a sample of ethanol by fermentation in the laboratory and show that carbon dioxide is produced.",
      ind=["dissolve sugar/glucose in warm water in a conical flask", "add yeast", "fit an airlock / delivery tube into limewater", "keep at about 30 °C for several days",
           "limewater turns milky showing CO₂", "filter off yeast", "distil to obtain ethanol"], ref=["4.32C", "4.33C"], d="4-6"),
    D(s="Explain why ethanol is used as a fuel and discuss its advantages and disadvantages compared with petrol.",
      ind=["ethanol burns: C₂H₅OH + 3O₂ → 2CO₂ + 3H₂O", "releases heat energy", "clean flame; little soot or sulfur dioxide", "from sugar cane: renewable; CO₂ absorbed while plants grow", "less energy per litre than petrol",
           "land used for fuel rather than food", "absorbs water; engines may need changes"], ref=["4.31C", "4.32C"], d="7-9"),
    D(s="Describe and explain what happens to wine left in an open glass for several days, and how the same product can be made quickly in a laboratory.",
      ind=["wine contains ethanol", "microbes in air (bacteria) oxidise ethanol", "using oxygen from the air", "to ethanoic acid – wine tastes sour / vinegar", "laboratory: warm ethanol with acidified potassium dichromate(VI)",
           "orange solution turns green", "ethanoic acid can be detected with a carbonate (fizzing)"], ref=["4.31C", "4.37C"], d="4-6"),
    D(s="Explain why the yield of ethanol from fermentation depends on temperature and on oxygen, and describe what would happen if the temperature were raised to 60 °C.",
      ind=["fermentation is catalysed by enzymes in yeast", "rate increases with temperature up to about 30–40 °C", "at 60 °C the enzymes are denatured: active site changes shape", "fermentation stops",
           "oxygen allows aerobic respiration: less ethanol", "oxygen allows ethanol to be oxidised to ethanoic acid", "so anaerobic, warm (≈30 °C) conditions give the best yield"], ref="4.33C", d="7-9"),
    D(s="Describe how to compare the energy released by burning methanol, ethanol and propan-1-ol.",
      ind=["spirit burner of each alcohol; weigh before and after", "heat a fixed mass of water in a copper can", "same distance from flame; draught shield", "measure temperature rise",
           "calculate energy per gram or per mole (Q = mcΔT)", "propan-1-ol releases most energy per mole", "more bonds broken and made as chain gets longer"], ref=["4.31C", "3.2"], d="7-9"),
    D(s="Explain why but-1-ol is not a correct name and describe the structures of the four alcohols from methanol to butan-1-ol.",
      ind=["names use the stem for number of carbons + 'an' + position + 'ol'", "butan-1-ol: four carbons, –OH on carbon 1", "methanol CH₃OH", "ethanol CH₃CH₂OH",
           "propan-1-ol CH₃CH₂CH₂OH", "butan-1-ol CH₃CH₂CH₂CH₂OH", "each has the –OH functional group; differ by CH₂"], ref="4.30C", d="4-6"),
], tag="alcohols")

# =================================================================== 4(f) carboxylic acids (C)
ACIDS = [(1, "methanoic acid", "HCOOH"), (2, "ethanoic acid", "CH3COOH"), (3, "propanoic acid", "CH3CH2COOH"), (4, "butanoic acid", "CH3CH2CH2COOH")]

facts(CA, "4.34C", [
    D(mq="What is the functional group of the carboxylic acids?", c="–COOH", w=["–OH", "C=C", "–COO–"]),
    D(mq="What is vinegar?", c="a solution of ethanoic acid in water", w=["pure ethanol", "a solution of ethanol in water", "an ester"], ref="4.37C"),
    D(mq="What is formed when ethanoic acid reacts with sodium carbonate?", c="sodium ethanoate, water and carbon dioxide", w=["sodium ethanoate and hydrogen", "ethanol and carbon dioxide", "ethyl ethanoate and water"], ref="4.36C"),
    D(mq="What is formed when ethanoic acid reacts with magnesium?", c="magnesium ethanoate and hydrogen", w=["magnesium ethanoate and water", "magnesium oxide and ethanol", "magnesium ethanoate and carbon dioxide"], ref="4.36C"),
    D(mq="What is the formula of propanoic acid?", c="CH3CH2COOH", w=["CH3COOH", "CH3CH2CH2OH", "CH3CH2COOCH3"], ref="4.35C"),
    D(mq="How many carbon atoms are in a molecule of butanoic acid?", c="4", w=["3", "5", "2"], ref="4.35C"),
    D(mq="Which compound is a carboxylic acid?", c="HCOOH", w=["CH3OH", "HCOOCH3", "C2H4"], ref="4.35C", d="4-6"),
    D(mq="What is seen when ethanoic acid is added to calcium carbonate?", c="fizzing", w=["a white precipitate", "a purple colour", "no change"], ref="4.36C"),
    D(mq="Which gas is made when ethanoic acid reacts with zinc?", c="hydrogen", w=["carbon dioxide", "oxygen", "methane"], ref="4.36C"),
    D(mq="What is the pH of dilute ethanoic acid likely to be?", c="3", w=["7", "11", "14"], d="4-6"),
    D(mq="Which salt is formed when propanoic acid reacts with potassium hydroxide?", c="potassium propanoate", w=["potassium propoxide", "propyl potassium", "potassium propanol"], ref="4.36C", d="7-9"),
    D(mq="Which statement about carboxylic acid solutions is correct?", c="they react with carbonates to give carbon dioxide", w=["they are alkaline", "they decolourise bromine water", "they do not react with metals"], ref="4.36C"),
], intro="This question is about carboxylic acids.", tag="org_acid")


@tpl(CA, "recall", 14)
def acids_recall(r, k):
    n, nm, sf = ACIDS[k % 4]
    kind = (k // 4) % 4
    if kind == 0:
        parts = [P("a", f"Give the structural formula of {nm}.", 1, lines=1), P("b", f"Name the functional group in {nm}.", 1, lines=1),
                 P("c", f"Name the salt formed when {nm} reacts with sodium carbonate.", 1, lines=1)]
        salt = "sodium " + nm.replace("ic acid", "ate")
        rows = [row("a", F(sf), 1, "ALLOW displayed formula", "AO1"), row("b", "carboxyl / –COOH", 1, None, "AO1"), row("c", salt, 1, None, "AO2")]
        return Q("Give", "4-6", parts, rows, ["4.35C", "4.36C"], ao=["AO1"], ans=("rules", {"salt": salt}))
    at, bonds = S.chain(n, subs={(n - 1, "up"): "=O", (n - 1, "down"): None, (n - 1, "right"): "OH"}) if n > 1 else (
        [{"el": "C", "left": "H", "up": "=O", "right": "OH"}], [])
    if n > 1:
        at[-1]["down"] = None
    svg = S.displayed(at, bonds)
    metal = ["magnesium", "zinc", "calcium"][kind - 1]
    parts = [P("a", "Name the compound shown.", 1, lines=1), P("b", f"Name the two products when it reacts with {metal}.", 2, lines=2)]
    parts[0]["figures"] = [fig(svg, 75)]
    rows = [row("a", nm, 1, None, "AO1"), row("b", f"M1 {metal} {nm.replace('ic acid', 'ate')}", 1, None, "AO2"), row("b", "M2 hydrogen", 1, None, "AO1")]
    return Q("Name", "4-6", parts, rows, ["4.35C", "4.36C"], ao=["AO1", "AO2"], ans=("rules", {"name": nm}))


@tpl(CA, "equation", 16)
def acids_eq(r, k):
    n, nm, sf = ACIDS[k % 4]
    mol = cf(n - 1, 2 * n - 1, "COOH") if n > 1 else "HCOOH"
    an = (cf(n - 1, 2 * n - 1, "COO") if n > 1 else "HCOO")
    kind = (k // 4) % 4
    if kind == 0:
        eq = f"2{mol}(aq) + Mg(s) -> ({an})2Mg(aq) + H2(g)"
        word = f"{nm} + magnesium → magnesium {nm.replace('ic acid', 'ate')} + hydrogen"
    elif kind == 1:
        eq = f"2{mol}(aq) + Na2CO3(s) -> 2{an}Na(aq) + H2O(l) + CO2(g)"
        word = f"{nm} + sodium carbonate → sodium {nm.replace('ic acid', 'ate')} + water + carbon dioxide"
    elif kind == 2:
        eq = f"{mol}(aq) + NaOH(aq) -> {an}Na(aq) + H2O(l)"
        word = f"{nm} + sodium hydroxide → sodium {nm.replace('ic acid', 'ate')} + water"
    else:
        eq = f"2{mol}(aq) + CaCO3(s) -> ({an})2Ca(aq) + H2O(l) + CO2(g)"
        word = f"{nm} + calcium carbonate → calcium {nm.replace('ic acid', 'ate')} + water + carbon dioxide"
    stem = f"Complete the word equation and write the balanced symbol equation.\n\n{word.split('→')[0]}→ [[dots]]"
    rows = [row("", f"M1 {word}", 1, None, "AO1"), row("", f"M2 {EQ(eq, states=False)}", 1, "ALLOW ions shown / any correct order of atoms in the salt", "AO2")]
    return Q("Complete", "7-9", [P("", stem, 2, lines=3)], rows, ["4.36C"], ao=["AO2"], ans=("balance", {"equation": EQ(eq, states=False)}))


# =================================================================== 4(g) esters (C)
ESTERS = [("methanol", "ethanoic acid", "methyl ethanoate", "CH3COOCH3"), ("ethanol", "ethanoic acid", "ethyl ethanoate", "CH3COOC2H5"),
          ("ethanol", "methanoic acid", "ethyl methanoate", "HCOOC2H5"), ("propan-1-ol", "ethanoic acid", "propyl ethanoate", "CH3COOC3H7"),
          ("methanol", "propanoic acid", "methyl propanoate", "C2H5COOCH3"), ("ethanol", "propanoic acid", "ethyl propanoate", "C2H5COOC2H5"),
          ("butan-1-ol", "ethanoic acid", "butyl ethanoate", "CH3COOC4H9"), ("methanol", "butanoic acid", "methyl butanoate", "C3H7COOCH3"),
          ("ethanol", "butanoic acid", "ethyl butanoate", "C3H7COOC2H5"), ("propan-1-ol", "methanoic acid", "propyl methanoate", "HCOOC3H7")]
ALCF = {"methanol": "CH3OH", "ethanol": "C2H5OH", "propan-1-ol": "C3H7OH", "butan-1-ol": "C4H9OH"}
ACF = {"methanoic acid": "HCOOH", "ethanoic acid": "CH3COOH", "propanoic acid": "C2H5COOH", "butanoic acid": "C3H7COOH"}

facts(ES, "4.38C", [
    D(mq="What is the functional group of an ester?", c="–COO–", w=["–COOH", "–OH", "C=C"]),
    D(mq="Which two substances react to form ethyl ethanoate?", c="ethanol and ethanoic acid", w=["ethene and ethanoic acid", "ethanol and ethene", "methanol and ethanoic acid"], ref="4.39C"),
    D(mq="Which catalyst is used to make an ester?", c="concentrated sulfuric acid", w=["yeast", "nickel", "manganese(IV) oxide"], ref="4.39C"),
    D(mq="What is a typical use of esters?", c="food flavourings and perfumes", w=["fuels for aircraft", "fertilisers", "making plastics bags"], ref="4.42C"),
    D(mq="Why are esters used in perfumes?", c="they are volatile and have pleasant smells", w=["they are acidic", "they are very soluble in water", "they have high boiling points"], ref="4.42C", d="4-6"),
    D(mq="What is the other product when an ester is made from an alcohol and a carboxylic acid?", c="water", w=["hydrogen", "carbon dioxide", "oxygen"], ref="4.39C"),
    D(mq="Which ester is made from methanol and ethanoic acid?", c="methyl ethanoate", w=["ethyl methanoate", "methyl methanoate", "ethyl ethanoate"], ref="4.41C", d="4-6"),
    D(mq="Which is the structural formula of ethyl ethanoate?", c="CH3COOCH2CH3", w=["CH3CH2COOCH3", "CH3COOH", "CH3CH2OH"], ref="4.40C", d="4-6"),
    D(mq="Which alcohol and acid form propyl methanoate?", c="propan-1-ol and methanoic acid", w=["methanol and propanoic acid", "propan-1-ol and propanoic acid", "methanol and methanoic acid"], ref="4.41C", d="7-9"),
    D(mq="How can you tell that an ester has been made in a test tube?", c="a fruity smell", w=["a colour change to green", "fizzing", "a white precipitate"], ref="4.43C"),
    D(mq="What type of reaction forms an ester and water?", c="condensation", w=["addition", "substitution", "cracking"], ref="4.39C", d="7-9"),
    D(mq="Ethyl ethanoate is described as volatile. What does this mean?", c="it evaporates easily", w=["it explodes easily", "it is very reactive", "it dissolves in water"], ref="4.42C"),
], intro="This question is about esters.", tag="org_est")

facts(ES, "4.38C", [
    D(q="Name the ester formed from ethanol and ethanoic acid.", a="ethyl ethanoate", ref="4.39C"),
    D(q="Name the catalyst used when making an ester.", a="concentrated sulfuric acid", ref="4.39C"),
    D(q="Give one use of esters.", a="flavourings / perfumes / solvents", ref="4.42C"),
    D(q="Give two physical properties of esters that make them suitable for perfumes.", m=2, pts=["volatile / evaporate easily", "distinctive / pleasant smell"], ref="4.42C"),
    D(q="Name the functional group in esters.", a="ester group, –COO–"),
    D(q="Name the alcohol needed to make methyl propanoate.", a="methanol", ref="4.41C"),
    D(q="Name the acid needed to make ethyl butanoate.", a="butanoic acid", ref="4.41C"),
    D(q="Give the molecular formula of ethyl ethanoate.", a="C4H8O2", ref="4.40C", d="4-6"),
    D(q="State how the smell of an ester can be detected safely.", a="waft the vapour towards the nose", ref="4.43C"),
    D(q="Name the other product formed with an ester in an esterification reaction.", a="water", ref="4.39C"),
], intro="This question is about esters and their uses.", tag="org_est2")


@tpl(ES, "equation", 20)
def esters_eq(r, k):
    al, ac, es, ef = ESTERS[k % len(ESTERS)]
    eq = f"{ACF[ac]}(l) + {ALCF[al]}(l) <=> {ef}(l) + H2O(l)"
    if (k // len(ESTERS)) % 2 == 0:
        stem = f"Write an equation, using structural or condensed formulae, for the reaction between {al} and {ac} to form an ester. Name the ester."
        rows = [row("", f"M1 {EQ(eq, states=False)}", 1, "ALLOW → for ⇌; ALLOW fully structural formulae", "AO2"), row("", f"M2 {es}", 1, None, "AO2")]
        return Q("Write", "7-9", [P("", stem, 2, lines=3)], rows, ["4.39C", "4.41C"], ao=["AO2"], ans=("balance", {"equation": EQ(eq, states=False), "ester": es}))
    stem = f"An ester called {es} is used as a flavouring.\n\nName the alcohol and the carboxylic acid used to make it, and give the structural formula of the ester."
    rows = [row("", f"M1 alcohol: {al}", 1, None, "AO2"), row("", f"M2 acid: {ac}", 1, None, "AO2"), row("", f"M3 {F(ef)}", 1, "ALLOW displayed formula", "AO2")]
    return Q("Deduce", "7-9", [P("", stem, 3, lines=4)], rows, ["4.41C", "4.40C"], ao=["AO2"], ans=("rules", {"alcohol": al, "acid": ac}))


@tpl(ES, "recall", 6)
def esters_name_recall(r, k):
    al, ac, es, ef = ESTERS[(k * 3) % len(ESTERS)]
    parts = [P("a", f"Name the ester formed from {al} and {ac}.", 1, lines=1), P("b", "Give the structural formula of this ester.", 1, lines=1)]
    rows = [row("a", es, 1, None, "AO2"), row("b", F(ef), 1, None, "AO2")]
    return Q("Name", "7-9", parts, rows, ["4.41C"], ao=["AO2"], ans=("rules", {"ester": es}))


items(ES, "practical", "4.43C", [
    D(s="Describe how to prepare a small sample of ethyl ethanoate in a test tube.", m=4,
      p=["mix ethanol and ethanoic acid in a test tube", "add a few drops of concentrated sulfuric acid", "warm in a water bath (not a flame)", "pour into sodium carbonate solution / water and smell (waft)"]),
    D(s="Explain why a water bath, not a Bunsen burner, is used to warm the mixture when making an ester.", m=2, p=["ethanol / ester is flammable", "a water bath has no naked flame"], d="4-6"),
    D(s="Explain why the reaction mixture is poured into sodium carbonate solution after making an ester.", m=2, p=["neutralises the excess acid", "so the ester smell can be detected / ester forms a separate layer"], d="7-9"),
    D(s="Give two safety precautions when making an ester.", m=2, p=["eye protection (concentrated acid is corrosive)", "no naked flames", "waft to smell; do not sniff directly", "gloves when handling concentrated sulfuric acid"], any=True),
    D(s="State the role of concentrated sulfuric acid when making an ester.", m=1, p=["catalyst"], d="1-3"),
    D(s="Describe how you could tell that an ester has formed.", m=1, p=["a sweet / fruity smell", "an oily layer on the surface of the water"], any=True, d="1-3"),
    D(s="Suggest why esters with small molecules are used in nail varnish remover.", m=2, p=["they are good solvents", "volatile so evaporate quickly"], ref="4.42C", d="7-9"),
    D(s="Suggest why the smell of the ester is easier to detect after the mixture is poured into water.", m=2, p=["the ester does not dissolve and floats", "the vinegar / acid smell is reduced"], d="7-9"),
    D(s="A student wants to make methyl butanoate. Name the two organic reagents she needs.", m=2, p=["methanol", "butanoic acid"], ref="4.41C", d="4-6"),
    D(s="Explain why the ester is made using only a few drops of each liquid.", m=2, p=["reagents are flammable / corrosive", "small amounts are safer and enough to smell"], d="4-6"),
    D(s="Suggest why the reaction mixture is warmed for several minutes rather than mixed cold.", m=2, p=["the reaction is slow at room temperature", "warming increases the rate"], d="4-6"),
    D(s="Explain why the yield of ester is never 100% even if the reaction is left for a long time.", m=2, p=["the reaction is reversible", "an equilibrium is reached"], d="7-9"),
], tag="org_est")

# =================================================================== 4(h) polymers
MONO = [("ethene", "poly(ethene)", {"up": "H", "down": "H"}, {"up": "H", "down": "H"}, "plastic bags / bottles"),
        ("propene", "poly(propene)", {"up": "H", "down": "H"}, {"up": "H", "down": "CH3"}, "crates / ropes"),
        ("chloroethene", "poly(chloroethene) (PVC)", {"up": "H", "down": "H"}, {"up": "H", "down": "Cl"}, "window frames / pipes / insulation"),
        ("tetrafluoroethene", "poly(tetrafluoroethene) (PTFE)", {"up": "F", "down": "F"}, {"up": "F", "down": "F"}, "non-stick pan coatings")]

facts(PO, "4.44", [
    D(mq="What is a polymer?", c="a very large molecule made by joining many small molecules", w=["a small molecule with a double bond", "a mixture of alkanes", "an ionic compound"]),
    D(mq="Which monomer is used to make PVC?", c="chloroethene", w=["ethene", "propene", "tetrafluoroethene"], ref="4.45"),
    D(mq="Why can ethene form a polymer but ethane cannot?", c="ethene has a C=C double bond", w=["ethane has a double bond", "ethene has more hydrogen atoms", "ethane is a gas"], d="4-6"),
    D(mq="Why are addition polymers difficult to dispose of?", c="they are inert and non-biodegradable", w=["they are very reactive", "they dissolve in water", "they are biodegradable"], ref="4.47"),
    D(mq="What problem is caused by burning addition polymers?", c="toxic gases may be produced", w=["they produce no products", "they release oxygen", "they form alkenes"], ref="4.47"),
    D(mq="What type of polymerisation makes a polyester?", c="condensation polymerisation", w=["addition polymerisation", "cracking", "fermentation"], ref="4.48C", d="4-6"),
    D(mq="Which small molecule is lost when a polyester is formed?", c="water", w=["hydrogen", "carbon dioxide", "ethene"], ref="4.48C", d="4-6"),
    D(mq="Which monomers form a polyester?", c="a dicarboxylic acid and a diol", w=["two alkenes", "an alkane and an alcohol", "a carboxylic acid and an alkene"], ref="4.48C", d="7-9"),
    D(mq="What is meant by biodegradable?", c="broken down by microorganisms", w=["can be recycled", "burns easily", "melts at a low temperature"], ref="4.50C"),
    D(mq="What is the name of the polymer made from propene?", c="poly(propene)", w=["poly(ethene)", "propane", "PVC"], ref="4.45"),
    D(mq="Which use is typical of PTFE?", c="non-stick coatings on pans", w=["food packaging film", "carrier bags", "window frames"], ref="4.45", d="4-6"),
    D(mq="How many products are formed in an addition polymerisation?", c="one", w=["two", "three", "it depends on the monomer"], ref="4.44", d="4-6"),
], intro="This question is about polymers.", tag="org_poly")


@tpl(PO, "recall", 12)
def polymers_recall(r, k):
    mono, poly, a1, a2, use = MONO[k % 4]
    at = [{"el": "C", **a1}, {"el": "C", **a2}]
    svg = S.displayed(at, ["1"], bracket=True)
    kind = (k // 4) % 3
    if kind == 0:
        parts = [P("a", "Name the polymer with this repeat unit.", 1, lines=1), P("b", "Name the monomer used to make it.", 1, lines=1), P("c", "Give one use of the polymer.", 1, lines=1)]
        rows = [row("a", poly, 1, None, "AO1"), row("b", mono, 1, None, "AO1"), row("c", use, 1, None, "AO1")]
        parts[0]["figures"] = [fig(svg, 70)]
        return Q("Name", "4-6", parts, rows, ["4.45", "4.46"], ao=["AO1"], ans=("rules", {"polymer": poly, "monomer": mono}))
    sv2 = S.displayed([{"el": "C", "left": a1["up"], "up": a1["down"]}, {"el": "C", "up": a2["down"], "right": a2["up"]}], ["2"])
    if kind == 1:
        parts = [P("a", f"Name this monomer.", 1, lines=1), P("b", f"Draw the repeat unit of the polymer formed from it.", 2, space="box")]
        parts[0]["figures"] = [fig(sv2, 60)]
        rows = [row("a", mono, 1, None, "AO1"), row("b", "M1 two carbons joined by a single bond with the same four substituents\nM2 extension bonds through brackets and n", 2, None, "AO2")]
        return Q("Draw", "4-6", parts, rows, ["4.45", "4.46"], ao=["AO2"], ans=("rules", {"monomer": mono}))
    parts = [P("a", f"State why {poly.split(' (')[0]} is difficult to dispose of in landfill.", 1, lines=2), P("b", f"Give one problem with disposing of {poly.split(' (')[0]} by burning.", 1, lines=2),
             P("c", "State the type of polymerisation used to make it.", 1, lines=1)]
    rows = [row("a", "non-biodegradable / inert so does not break down", 1, None, "AO1"),
            row("b", "toxic gases (e.g. HCl from PVC) / carbon dioxide (greenhouse) / carbon monoxide" if "chloro" in mono else "releases carbon dioxide / toxic gases / carbon monoxide", 1, None, "AO1"),
            row("c", "addition", 1, None, "AO1")]
    return Q("State", "1-3", parts, rows, ["4.47", "4.44"], ao=["AO1"], ans=("rules", {"type": "addition"}))


items(PO, "explain", "4.47", [
    D(s="Explain why addition polymers cause problems when disposed of in landfill sites.", m=2, p=["they are non-biodegradable / inert", "so they remain for a very long time / take up space"]),
    D(s="Explain why burning PVC is a particular problem.", m=2, p=["produces toxic gases", "such as hydrogen chloride"], d="4-6"),
    D(s="Explain why an alkene can form an addition polymer.", m=2, p=["it has a C=C double bond", "which opens so monomers join together in a chain"], ref="4.44"),
    D(s="Explain why poly(ethene) is described as saturated even though it is made from an unsaturated monomer.", m=2, p=["the C=C bonds become single bonds during polymerisation", "the polymer has only single C–C bonds"], ref="4.44", d="7-9"),
    D(s="Explain the difference between addition polymerisation and condensation polymerisation.", m=3,
      p=["addition: monomers with C=C join, only one product", "condensation: monomers with two functional groups join", "a small molecule (water) is also formed"], ref="4.48C", d="7-9"),
    D(s="Explain why some polyesters are more environmentally friendly than poly(ethene).", m=2, p=["some polyesters are biodegradable", "broken down by microorganisms so less waste"], ref="4.50C"),
    D(s="Explain why recycling polymers is better than burning them.", m=2, p=["saves crude oil / raw materials", "no toxic gases / less carbon dioxide released"], ref="4.47", d="4-6"),
    D(s="Explain why the polymer made from propene has a methyl group on every other carbon atom.", m=2, p=["each propene monomer contributes two carbons to the chain", "the CH₃ group is attached to one of these"], ref="4.46", d="7-9"),
    D(s="Explain why a polyester needs two different types of monomer, or one monomer with two different groups.", m=2, p=["an acid group reacts with an alcohol group", "each monomer needs two groups to link in both directions to form a chain"], ref="4.48C", d="7-9"),
    D(s="Explain why the polymer formed from tetrafluoroethene is very unreactive.", m=2, p=["strong C–F and C–C single bonds", "no double bond to react"], ref="4.47", d="7-9"),
], tag="org_poly")


@tpl(PO, "equation", 16)
def polymers_eq(r, k):
    mono, poly, a1, a2, use = MONO[k % 4]
    monof = {"ethene": "CH2=CH2", "propene": "CH2=CHCH3", "chloroethene": "CH2=CHCl", "tetrafluoroethene": "CF2=CF2"}[mono]
    rep = {"ethene": "–CH2–CH2–", "propene": "–CH2–CH(CH3)–", "chloroethene": "–CH2–CHCl–", "tetrafluoroethene": "–CF2–CF2–"}[mono]
    kind = (k // 4) % 4
    if kind == 1:
        stem = f"{mono.capitalize()}, {F(monof)}, forms an addition polymer.\n\n(i) Name the polymer.\n\n(ii) Draw the repeat unit of the polymer.\n\n(iii) Give one use of the polymer."
        rows = [row("", f"M1 {poly}", 1, None, "AO1"), row("", f"M2 {F(rep)} in brackets with extension bonds", 1, None, "AO2"), row("", f"M3 {use}", 1, None, "AO1")]
        return Q("Draw", "4-6", [P("", stem, 3, space="box")], rows, ["4.45", "4.46"], ao=["AO2"], ans=("rules", {"repeat": rep}))
    if kind < 2:
        stem = f"Complete the equation for the polymerisation of {mono}, using displayed formulae.\n\nn {F(monof)} → [[dots]]"
        rows = [row("", f"M1 repeat unit {F(rep)} in brackets", 1, None, "AO2"), row("", "M2 extension bonds through the brackets and n after the bracket", 1, None, "AO2")]
        return Q("Complete", "4-6", [P("", stem, 2, space="box")], rows, ["4.45", "4.44"], ao=["AO2"], ans=("rules", {"repeat": rep}))
    # condensation (C)
    pairs = [("ethanedioic acid", "HOOC–COOH", "ethane-1,2-diol", "HO–CH2CH2–OH", "–OC–COO–CH2CH2–O–"),
             ("benzene-1,4-dicarboxylic acid", "HOOC–C6H4–COOH", "ethane-1,2-diol", "HO–CH2CH2–OH", "–OC–C6H4–COO–CH2CH2–O–"),
             ("butanedioic acid", "HOOC–CH2CH2–COOH", "ethane-1,2-diol", "HO–CH2CH2–OH", "–OC–CH2CH2–COO–CH2CH2–O–"),
             ("hexanedioic acid", "HOOC–(CH2)4–COOH", "propane-1,3-diol", "HO–(CH2)3–OH", "–OC–(CH2)4–COO–(CH2)3–O–")]
    a, af, d_, df, ru = pairs[k % 4]
    if kind == 3:
        stem = (f"The monomers {a} and {d_} join to make a polymer.\n\n(i) Name the type of linkage formed between the monomers.\n\n"
                "(ii) Explain why this polymer may cause fewer disposal problems than poly(ethene).")
        rows = [row("", "M1 ester (link)", 1, None, "AO1"), row("", "M2 (some) polyesters are biodegradable", 1, None, "AO1"), row("", "M3 broken down by microorganisms / hydrolysed", 1, None, "AO2")]
        return Q("Explain", "7-9", [P("", stem, 3, lines=5)], rows, ["4.48C", "4.50C"], ao=["AO1", "AO2"], ans=("rules", {"link": "ester"}))
    stem = (f"A polyester is made from {a}, {F(af)}, and {d_}, {F(df)}.\n\n(i) Give the repeat unit of the polyester.\n\n"
            "(ii) Name the other product of the reaction and state the type of polymerisation.")
    rows = [row("", f"M1 {F(ru)} in brackets with n", 1, "ALLOW boxes for carbon chains", "AO2"), row("", "M2 ester link –COO– shown correctly", 1, None, "AO2"),
            row("", "M3 water", 1, None, "AO1"), row("", "M4 condensation", 1, None, "AO1")]
    return Q("Give", "7-9", [P("", stem, 4, lines=6)], rows, ["4.49C", "4.48C"], ao=["AO2"], ans=("rules", {"repeat": ru}))
