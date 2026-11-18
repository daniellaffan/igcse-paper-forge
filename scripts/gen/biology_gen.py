"""Genetics templates: monohybrid crosses with Punnett tables, ratios, probabilities, codominance,
sex determination, test crosses and pedigree diagrams (SVG).  Every ratio/probability is computed."""
import random
from collections import Counter
from fractions import Fraction

from biology_lib import reg, text_part, row_, points_row, table_fig, svg_fig, mcq_part

SUB = "reproduction.inheritance"

# (organism, letter, dominant phenotype, recessive phenotype, characteristic)
TRAITS = [
    ("pea plants", "T", "tall", "short", "height"),
    ("pea plants", "R", "round seeds", "wrinkled seeds", "seed shape"),
    ("guinea pigs", "B", "black fur", "white fur", "fur colour"),
    ("fruit flies", "N", "normal wings", "vestigial wings", "wing shape"),
    ("tomato plants", "P", "purple stems", "green stems", "stem colour"),
    ("mice", "G", "grey fur", "white fur", "fur colour"),
    ("cats", "S", "short hair", "long hair", "hair length"),
    ("maize plants", "Y", "yellow seeds", "white seeds", "seed colour"),
    ("rabbits", "D", "dark eyes", "red eyes", "eye colour"),
    ("dogs", "E", "erect ears", "drooping ears", "ear shape"),
]

CROSSES = [("Aa", "Aa"), ("Aa", "aa"), ("AA", "aa"), ("AA", "Aa")]


def gt(letter, pat):
    return "".join(letter if c == "A" else letter.lower() for c in pat)


def norm(g):
    return "".join(sorted(g, key=lambda c: (c.islower(), c)))


def cross(p1, p2):
    return [norm(a + b) for a in p1 for b in p2]


def ratio_str(counts):
    vals = list(counts)
    from math import gcd
    g = 0
    for v in vals:
        g = gcd(g, v)
    return " : ".join(str(v // g) for v in vals)


def punnett_fig(g1, g2, blank=False, kids=None):
    rows = []
    for i, a in enumerate(g2):
        rows.append([a] + ["" if blank else kids[i][j] for j in range(len(g1))])
    return table_fig(["gametes"] + list(g1), rows)


def pheno(g, dom, rec):
    return dom if any(c.isupper() for c in g) else rec


def frac_txt(fr):
    return f"{fr.numerator}/{fr.denominator}" if fr.denominator != 1 else str(fr.numerator)


def monohybrid(k):
    org, L, dom, rec, char = TRAITS[k % len(TRAITS)]
    c1, c2 = CROSSES[(k // len(TRAITS) + k) % len(CROSSES)]
    p1, p2 = gt(L, c1), gt(L, c2)
    kids = [[norm(a + b) for a in p1] for b in p2]
    flat = [x for row in kids for x in row]
    ph = Counter(pheno(g, dom, rec) for g in flat)
    gts = Counter(flat)
    nd, nr = ph.get(dom, 0), ph.get(rec, 0)
    prob_rec = Fraction(nr, 4)
    intro = (f"In {org}, the allele for {dom} ({L}) is dominant to the allele for {rec} ({L.lower()}).\n\n"
             f"A {pheno(p1, dom, rec)} plant with genotype {p1} is crossed with a {pheno(p2, dom, rec)} one with genotype {p2}."
             if "plants" in org else
             f"In {org}, the allele for {dom} ({L}) is dominant to the allele for {rec} ({L.lower()}).\n\n"
             f"An animal with genotype {p1} is bred with an animal with genotype {p2}.")
    parts = [text_part("a", "Give the gametes produced by each parent.", 2, 2),
             text_part("b", "Complete the Punnett square to show the genotypes of the offspring.", 2, space="table",
                       figures=[punnett_fig(sorted(set(p1)), sorted(set(p2)), blank=True)] if False else
                       [table_fig(["gametes", p1[0], p1[1]], [[p2[0], "", ""], [p2[1], "", ""]])]),
             text_part("c", f"Give the expected ratio of {dom} to {rec} offspring.", 1, 1),
             text_part("d", f"Give the probability that an offspring has {rec}.", 1, 1)]
    filled = table_fig(["gametes", p1[0], p1[1]], [[p2[0], kids[0][0], kids[0][1]], [p2[1], kids[1][0], kids[1][1]]])
    rows = [row_("a", f"parent 1: {' and '.join(sorted(set(p1)))} (1)\nparent 2: {' and '.join(sorted(set(p2)))} (1)", 2,
                  "Gametes may be shown circled; one mark per parent", "AO2"),
            row_("b", "correct genotypes in all four boxes: " + ", ".join(flat) + " (2)", 2,
                 "One mark for two or three correct boxes; allow ecf from (a)", "AO2"),
            row_("c", f"{nd} : {nr} (1)", 1, f"Accept equivalent, e.g. {ratio_str([nd, nr]) if nd and nr else f'{nd} : {nr}'}; allow ecf from (b)", "AO2"),
            row_("d", f"{frac_txt(prob_rec)} / {float(prob_rec)*100:g}% / {float(prob_rec):g} (1)", 1,
                 "Reject a ratio such as 1 : 3; allow ecf from (b)", "AO2")]
    ans = {"method": "Punnett square", "values": {"genotypes": dict(gts), "phenotype_ratio": [nd, nr], "p_recessive": float(prob_rec)},
           "checked": True}
    refs = ["3.23", "3.25"]
    diff = "1-3" if (c1, c2) == ("AA", "aa") else ("4-6" if (c1, c2) != ("Aa", "Aa") or k % 2 else "4-6")
    return dict(parts=parts, rows=rows, refs=refs, cw="Complete", diff=diff, intro=intro, answer=ans,
                template="inheritance-gen-punnett", figures=None, _filled=filled)


def from_offspring(k):
    """Work back from offspring numbers to parent genotypes."""
    org, L, dom, rec, char = TRAITS[(k + 3) % len(TRAITS)]
    r = random.Random(f"off-{k}")
    kind = k % 2
    total = r.choice([40, 64, 80, 96, 120, 160, 200, 248])
    if kind == 0:
        nr = round(total / 4 + r.randint(-3, 3))
        nd = total - nr
        exp = "3 : 1"
        pg = f"{L}{L.lower()} and {L}{L.lower()}"
        why = ["ratio is about 3 : 1", f"both parents are heterozygous / {L}{L.lower()}", "each parent passes on a recessive allele to some offspring"]
    else:
        nr = round(total / 2 + r.randint(-4, 4))
        nd = total - nr
        exp = "1 : 1"
        pg = f"{L}{L.lower()} and {L.lower()}{L.lower()}"
        why = ["ratio is about 1 : 1", f"one parent is heterozygous / {L}{L.lower()}", f"the other parent is homozygous recessive / {L.lower()}{L.lower()}"]
    intro = (f"In {org}, the allele for {dom} ({L}) is dominant to the allele for {rec} ({L.lower()}). Two {org} were crossed. "
             f"There were {nd} offspring with {dom} and {nr} offspring with {rec}.")
    obs = nd / nr
    parts = [text_part("a", f"Calculate the ratio of offspring with {dom} to offspring with {rec}.\n\nGive your answer in the form n : 1", 2, 3, space="working",
                       prefix="ratio = "),
             text_part("b", "Deduce the genotypes of the two parents. Explain your answer.", 3, 4),
             text_part("c", "Suggest why the observed ratio is not exactly the expected ratio.", 1, 2)]
    rows = [row_("a", f"{nd} ÷ {nr} (1)", 1, None, "AO2"),
            row_("a", f"{obs:.2f} : 1 (1)", 1, "Allow full marks for correct answer with no working", "AO2"),
            points_row("b", 3, [f"genotypes {pg}"] + why, "Explain", "Allow genotypes shown in a correct genetic diagram", "AO2"),
            row_("c", "fertilisation is random / each fertilisation is a chance event / sample size is small (1)", 1, None, "AO3")]
    ans = {"method": "ratio = dominant/recessive", "values": {"ratio": round(obs, 2), "expected": exp}, "checked": True}
    return dict(parts=parts, rows=rows, refs=["3.23", "3.25"], cw="Deduce", diff="7-9" if kind else "4-6", intro=intro, answer=ans,
                template="inheritance-gen-backcross")


def test_cross(k):
    org, L, dom, rec, char = TRAITS[k % len(TRAITS)]
    intro = f"In {org}, the allele for {dom} ({L}) is dominant to the allele for {rec} ({L.lower()}). A breeder has one of the {org} with {dom} and wants to know its genotype."
    parts = [text_part("a", "Give the two possible genotypes of this organism.", 1, 1),
             text_part("b", "Describe how a test cross could be used to find its genotype. Use a genetic diagram in your answer.", 4, 8)]
    rows = [row_("a", f"{L}{L} and {L}{L.lower()} (1)", 1, "Both needed", "AO1"),
            points_row("b", 4, [f"cross with a homozygous recessive / {L.lower()}{L.lower()} / {rec} organism",
                                f"if all offspring have {dom}, the parent is {L}{L}",
                                f"if any offspring have {rec}, the parent is {L}{L.lower()}",
                                f"genetic diagram for {L}{L.lower()} × {L.lower()}{L.lower()} giving 1 : 1",
                                "large number of offspring needed"], "Describe", "Diagram can score the corresponding marks", "AO2")]
    return dict(parts=parts, rows=rows, refs=["3.20", "3.23"], cw="Describe", diff="7-9", intro=intro, template="inheritance-gen-testcross")


CODOM = [("snapdragon plants", "flower colour", "C^R", "C^W", "red", "white", "pink"),
         ("cattle", "coat colour", "C^R", "C^W", "red", "white", "roan (red and white hairs)"),
         ("chickens", "feather colour", "C^B", "C^W", "black", "white", "blue-grey"),
         ("four o'clock plants", "flower colour", "C^R", "C^W", "red", "white", "pink"),
         ("horses", "coat colour", "C^C", "C^W", "chestnut", "white", "palomino")]


def codominance(k):
    org, char, a, b, pa, pb, het = CODOM[k % len(CODOM)]
    crossk = (k // len(CODOM)) % 3
    A, B = a.replace("^", ""), b.replace("^", "")
    pairs = [((A, B), (A, B)), ((A, B), (A, A)), ((A, B), (B, B))][crossk]
    kids = [x + y for x in pairs[0] for y in pairs[1]]
    canon = lambda g: (A + B) if set([g[:2], g[2:]]) == {A, B} else g
    cnt = Counter(canon(g) for g in kids)
    names = {A + A: pa, B + B: pb, A + B: het}
    order = [g for g in (A + A, A + B, B + B) if cnt.get(g)]
    ratio = " : ".join(f"{cnt[g]} {names[g]}" for g in order)
    pp = lambda p: names[canon(p[0] + p[1])]
    intro = (f"In {org}, {char} shows codominance. The allele {A} gives {pa} and the allele {B} gives {pb}. "
             f"Organisms with both alleles are {het}.")
    p_het = Fraction(cnt.get(A + B, 0), 4)
    parts = [text_part("a", "State what is meant by codominance.", 1, 2),
             text_part("b", f"A {pp(pairs[0])} parent is crossed with a {pp(pairs[1])} parent.\n\nDraw a genetic diagram to show the possible offspring and give the ratio of their phenotypes.", 4, 8),
             text_part("c", f"Give the probability that an offspring is {het.split(' (')[0]}.", 1, 1)]
    rows = [row_("a", "both alleles are expressed in the phenotype of a heterozygote (1)", 1, "Reject 'both alleles are dominant' unless qualified", "AO1"),
            points_row("b", 4, [f"parental genotypes {''.join(pairs[0])} and {''.join(pairs[1])}", f"gametes {', '.join(sorted(set(pairs[0])))} and {', '.join(sorted(set(pairs[1])))}",
                                "correct offspring genotypes", f"ratio {ratio}"], "Draw", "Allow ecf for ratio from offspring genotypes", "AO2"),
            row_("c", f"{frac_txt(p_het)} / {float(p_het)*100:g}% / {float(p_het):g} (1)", 1, "Allow ecf from (b)", "AO2")]
    ans = {"method": "genetic diagram", "values": {"counts": {names[g]: cnt[g] for g in order}, "p_het": float(p_het)}, "checked": True}
    return dict(parts=parts, rows=rows, refs=["3.21B", "3.23"], cw="Draw", diff="7-9", intro=intro, answer=ans, template="inheritance-gen-codom")


def sex_det(k):
    r = random.Random(f"sex-{k}")
    n = r.choice([2, 3, 4])
    kind = k % 3
    intro = "Sex in humans is determined by one pair of chromosomes."
    if kind == 0:
        parts = [text_part("a", "Give the sex chromosomes of a male and of a female.", 1, 1),
                 text_part("b", "Complete a genetic diagram to show how sex is inherited.", 3, space="table",
                           figures=[table_fig(["gametes", "X", "X"], [["X", "", ""], ["Y", "", ""]])]),
                 text_part("c", "Give the probability that a baby is a girl.", 1, 1)]
        rows = [row_("a", "male XY and female XX (1)", 1, "Both needed", "AO1"),
                row_("b", "XX, XX, XY, XY in the correct boxes (2)\n2 female : 2 male / 1 : 1 (1)", 3, "One mark for two correct boxes", "AO2"),
                row_("c", "1/2 / 50% / 0.5 (1)", 1, "Reject 1 : 1", "AO2")]
        ans = {"method": "XX × XY", "values": {"p_girl": 0.5}, "checked": True}
        return dict(parts=parts, rows=rows, refs=["3.26", "3.27"], cw="Complete", diff="1-3", intro=intro, answer=ans, template="inheritance-gen-sex")
    if kind == 1:
        p = Fraction(1, 2 ** n)
        parts = [text_part("", f"A couple already have {n} sons. Calculate the probability that their next child is also a son. Explain your answer.", 2, 3)]
        rows = [points_row("", 2, ["probability is 1/2 / 50% / 0.5", "each fertilisation is independent / sperm carry X or Y in equal numbers",
                                   "previous children do not affect the next"], "Explain", f"Reject 1/{2 ** (n + 1)} (this is the probability of {n + 1} sons in a row)", "AO2")]
        ans = {"method": "independent events", "values": {"p_next_son": 0.5, f"p_{n}_sons": float(p)}, "checked": True}
        return dict(parts=parts, rows=rows, refs=["3.26", "3.27"], cw="Explain", diff="7-9", intro=intro, answer=ans, template="inheritance-gen-sexprob")
    p = Fraction(1, 2 ** n)
    parts = [text_part("", f"Calculate the probability that a couple's first {n} children are all girls.", 2, 3, space="working", prefix="probability = ")]
    rows = [row_("", f"(1/2) multiplied {n} times / (1/2)^{n} (1)", 1, None, "AO2"),
            row_("", f"{frac_txt(p)} / {float(p):g} / {float(p)*100:g}% (1)", 1, "Allow full marks for correct answer with no working", "AO2")]
    ans = {"method": "product of independent probabilities", "values": {"p": float(p)}, "checked": True}
    return dict(parts=parts, rows=rows, refs=["3.25", "3.26"], cw="Calculate", diff="7-9", intro=intro, answer=ans, template="inheritance-gen-sexmulti")


# ------------------------------------------------------------------ pedigree SVG
DISORDERS = [("cystic fibrosis", "F"), ("albinism", "A"), ("phenylketonuria (PKU)", "P"), ("sickle-cell disease", "S"),
             ("a form of deafness", "D"), ("a muscle disorder", "M"), ("a blood-clotting disorder", "H")]


def pedigree_svg(gen1, kids, numbers):
    """gen1: [(sex, affected)] two parents; kids: [(sex, affected)]."""
    w = max(320, 90 + 70 * len(kids))
    h = 210
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h + 50}" font-family="sans-serif" font-size="12">']

    def shape(sex, aff, x, y, num):
        fill = "currentColor" if aff else "none"
        if sex == "M":
            out.append(f'<rect x="{x-14}" y="{y-14}" width="28" height="28" fill="{fill}" stroke="currentColor" stroke-width="1.5"/>')
        else:
            out.append(f'<circle cx="{x}" cy="{y}" r="14" fill="{fill}" stroke="currentColor" stroke-width="1.5"/>')
        out.append(f'<text x="{x}" y="{y+32}" text-anchor="middle" fill="currentColor">{num}</text>')
    cx = w / 2
    px = [cx - 50, cx + 50]
    for i, (s, a) in enumerate(gen1):
        shape(s, a, px[i], 40, numbers[i])
    out.append(f'<line x1="{px[0]+14}" y1="40" x2="{px[1]-14}" y2="40" stroke="currentColor" stroke-width="1.5"/>')
    out.append(f'<line x1="{cx}" y1="40" x2="{cx}" y2="95" stroke="currentColor" stroke-width="1.5"/>')
    xs = [cx + (i - (len(kids) - 1) / 2) * 70 for i in range(len(kids))]
    out.append(f'<line x1="{xs[0]}" y1="95" x2="{xs[-1]}" y2="95" stroke="currentColor" stroke-width="1.5"/>')
    for i, (s, a) in enumerate(kids):
        out.append(f'<line x1="{xs[i]}" y1="95" x2="{xs[i]}" y2="121" stroke="currentColor" stroke-width="1.5"/>')
        shape(s, a, xs[i], 135, numbers[2 + i])
    ly = h + 10
    out.append(f'<rect x="10" y="{ly}" width="14" height="14" fill="none" stroke="currentColor"/><text x="30" y="{ly+11}" fill="currentColor">unaffected male</text>')
    out.append(f'<circle cx="137" cy="{ly+7}" r="7" fill="none" stroke="currentColor"/><text x="150" y="{ly+11}" fill="currentColor">unaffected female</text>')
    out.append(f'<rect x="10" y="{ly+20}" width="14" height="14" fill="currentColor" stroke="currentColor"/><text x="30" y="{ly+31}" fill="currentColor">affected male</text>')
    out.append(f'<circle cx="137" cy="{ly+27}" r="7" fill="currentColor" stroke="currentColor"/><text x="150" y="{ly+31}" fill="currentColor">affected female</text>')
    out.append("</svg>")
    return "".join(out)


def pedigree(k):
    r = random.Random(f"ped-{k}")
    dis, L = DISORDERS[k % len(DISORDERS)]
    n = r.choice([3, 4, 5])
    kids = [(r.choice("MF"), False) for _ in range(n)]
    ai = r.randrange(n)
    kids[ai] = (kids[ai][0], True)
    if n >= 4 and k % 2:
        bi = (ai + 2) % n
        kids[bi] = (kids[bi][0], True)
    nums = list(range(1, 3 + n))
    svg = pedigree_svg([("M", False), ("F", False)], kids, nums)
    aff = [nums[2 + i] for i, (s, a) in enumerate(kids) if a]
    unaff = [nums[2 + i] for i, (s, a) in enumerate(kids) if not a]
    u = unaff[0]
    intro = f"The diagram shows the inheritance of {dis} in a family. The disorder is caused by a recessive allele ({L.lower()})."
    if k % 3 == 2:
        intro = f"The diagram shows the inheritance of {dis} in a family."
    rec = Fraction(1, 4)
    parts = []
    rows = []
    lab = iter("abcd")
    if k % 3 == 2:
        l = next(lab)
        parts.append(text_part(l, "Explain how the diagram shows that the disorder is caused by a recessive allele.", 2, 3, figures=[svg_fig(svg, 90)]))
        rows.append(points_row(l, 2, [f"individuals 1 and 2 are unaffected", f"but have an affected child ({aff[0]})", "so both parents must carry the allele / be heterozygous",
                                      "the allele is hidden / masked in the parents"], "Explain", None, "AO2"))
        first = False
    else:
        first = True
    l = next(lab)
    p = text_part(l, f"Give the genotypes of individual 1 and individual {aff[0]}.", 2, 2)
    if first:
        p["figures"] = [svg_fig(svg, 90)]
    parts.append(p)
    rows.append(row_(l, f"individual 1: {L}{L.lower()} (1)\nindividual {aff[0]}: {L.lower()}{L.lower()} (1)", 2, f"Accept other letters only if a key is given", "AO2"))
    l = next(lab)
    parts.append(text_part(l, "Individuals 1 and 2 have another child. Calculate the probability that this child will have the disorder.", 2, 3, space="working",
                           prefix="probability = "))
    rows.append(row_(l, f"genetic diagram / Punnett square for {L}{L.lower()} × {L}{L.lower()} (1)\n1/4 / 25% / 0.25 (1)", 2,
                     "Allow full marks for correct answer with no working; reject 1 : 3", "AO2"))
    l = next(lab)
    parts.append(text_part(l, f"Individual {u} is unaffected. Give the probability that individual {u} is heterozygous.", 2, 3, space="working",
                           prefix="probability = "))
    rows.append(row_(l, f"unaffected offspring are {L}{L} or {L}{L.lower()} in a ratio of 1 : 2 (1)\n2/3 / 0.67 / 67% (1)", 2,
                     "Reject 1/2 or 3/4", "AO2"))
    ans = {"method": "Aa × Aa; P(aa)=1/4; P(Aa | unaffected)=2/3", "values": {"p_affected": float(rec), "p_het_given_unaffected": round(2 / 3, 4),
                                                                              "affected": aff}, "checked": True}
    return dict(parts=parts, rows=rows, refs=["3.24", "3.25"], cw="Calculate", diff="7-9", intro=intro, answer=ans, template="inheritance-gen-pedigree")


def ratio_mcq(k):
    org, L, dom, rec, char = TRAITS[(k + 5) % len(TRAITS)]
    c1, c2 = CROSSES[k % 4]
    p1, p2 = gt(L, c1), gt(L, c2)
    flat = cross(p1, p2)
    nr = sum(1 for g in flat if g.islower())
    pc = nr / 4 * 100
    opts = ["0%", "25%", "50%", "75%", "100%"]
    correct = f"{pc:g}%"
    dist = [o for o in opts if o != correct]
    rr = random.Random(f"rmcq-{k}")
    rr.shuffle(dist)
    p, rw = mcq_part(rr, "", f"In {org}, the allele for {dom} ({L}) is dominant to the allele for {rec} ({L.lower()}). What percentage of the offspring of a cross between {p1} and {p2} are expected to have {rec}?",
                     correct, dist[:3])
    ans = {"method": "Punnett square", "values": {"percent_recessive": pc}, "checked": True}
    return dict(parts=[p], rows=[rw], refs=["3.25"], cw="Give", diff="4-6", answer=ans, template="inheritance-gen-mcq", style="mcq")


@reg(SUB, "genetics", "inheritance-gen")
def genetics():
    out = []
    for k in range(28):
        q = monohybrid(k)
        q.pop("_filled", None)
        q.pop("figures", None)
        out.append(q)
    out += [from_offspring(k) for k in range(12)]
    out += [test_cross(k) for k in range(8)]
    out += [codominance(k) for k in range(12)]
    out += [sex_det(k) for k in range(9)]
    out += [pedigree(k) for k in range(14)]
    out += [ratio_mcq(k) for k in range(12)]
    return out
