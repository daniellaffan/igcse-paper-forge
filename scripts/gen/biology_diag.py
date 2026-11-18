"""Labelled-diagram templates.  Each diagram is a schematic black-and-white SVG with letter labels
on leader lines.  Questions: name labelled parts (random pairs/triples), identify a part from its
function, MCQ "which letter", and describe the function of a labelled part."""
import itertools
import random
from collections import namedtuple

from biology_lib import reg, text_part, row_, points_row, svg_fig, mcq_part

St = namedtuple("St", "name x y side func accept")
W, H = 440, 300
STROKE = 'stroke="currentColor" fill="none" stroke-width="1.5"'


def st(name, x, y, side, func, accept=None):
    return St(name, x, y, side, func, accept)


def build_svg(body, structs, letters):
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="sans-serif" font-size="14">', body]
    for side in "LR":
        items = sorted([(s, letters[i]) for i, s in enumerate(structs) if s.side == side], key=lambda t: t[0].y)
        n = len(items)
        if not n:
            continue
        ys = []
        for j, (s, _) in enumerate(items):
            y = max(s.y, (ys[-1] + 26) if ys else 18)
            ys.append(y)
        over = ys[-1] - (H - 14) if ys else 0
        if over > 0:
            ys = [y - over for y in ys]
        lx = 28 if side == "L" else W - 28
        for (s, let), y in zip(items, ys):
            ex = lx + (10 if side == "L" else -10)
            out.append(f'<line x1="{s.x}" y1="{s.y}" x2="{ex}" y2="{y}" stroke="currentColor" stroke-width="1"/>')
            out.append(f'<circle cx="{s.x}" cy="{s.y}" r="1.8" fill="currentColor"/>')
            out.append(f'<text x="{lx}" y="{y+5}" text-anchor="middle" font-weight="bold" fill="currentColor">{let}</text>')
    out.append("</svg>")
    return "".join(out)


def assign_letters(structs):
    order = sorted(range(len(structs)), key=lambda i: (structs[i].side != "L", structs[i].y))
    letters = [""] * len(structs)
    for k, i in enumerate(order):
        letters[i] = "ABCDEFGH"[k]
    return letters


# ------------------------------------------------------------------ diagram bodies
def ell(cx, cy, rx, ry, extra=""):
    return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" {STROKE} {extra}/>'


def path(d, extra=""):
    return f'<path d="{d}" {STROKE} {extra}/>'


BACT = "".join([ell(220, 150, 150, 72), ell(220, 150, 138, 62), ell(220, 150, 130, 56),
                path("M 200 140 c 20 -30 50 10 30 30 c -20 20 -60 -5 -40 -25 c 10 -10 30 0 20 10"),
                '<circle cx="290" cy="130" r="9" stroke="currentColor" fill="none" stroke-width="1.3"/>',
                '<circle cx="150" cy="175" r="7" stroke="currentColor" fill="none" stroke-width="1.3"/>',
                path("M 370 150 c 10 -15 20 15 30 0 c 10 -15 20 15 30 0"),
                ''.join(f'<circle cx="{x}" cy="{y}" r="1.2" fill="currentColor"/>' for x, y in [(170, 130), (260, 175), (240, 120), (180, 160), (300, 165)])])
BACT_S = [st("capsule / slime coat", 220, 78, "L", "protects the cell / helps it stick to surfaces"),
          st("cell wall", 160, 95, "L", "gives support and stops the cell bursting"),
          st("cell membrane", 120, 140, "L", "controls what enters and leaves the cell"),
          st("circular DNA / chromosome", 225, 150, "R", "carries the genes that control the cell"),
          st("plasmid", 290, 130, "R", "carries extra genes, e.g. for antibiotic resistance"),
          st("flagellum", 410, 148, "R", "used for movement"),
          st("cytoplasm", 260, 180, "R", "where most chemical reactions take place")]

PLANT = "".join(['<rect x="110" y="40" width="220" height="220" rx="6" stroke="currentColor" fill="none" stroke-width="3"/>',
                 '<rect x="118" y="48" width="204" height="204" rx="4" stroke="currentColor" fill="none" stroke-width="1"/>',
                 '<rect x="150" y="90" width="140" height="130" rx="30" stroke="currentColor" fill="none" stroke-width="1.3"/>',
                 '<circle cx="140" cy="70" r="16" stroke="currentColor" fill="none" stroke-width="1.5"/>',
                 ''.join(ell(x, y, 12, 6) for x, y in [(300, 70), (305, 235), (135, 235), (300, 150)]),
                 ''.join(ell(x, y, 6, 3.5, 'stroke-dasharray="2 1"') for x, y in [(200, 65), (240, 240)])])
PLANT_S = [st("nucleus", 140, 70, "L", "contains genetic material that controls the activities of the cell"),
           st("cell wall", 112, 160, "L", "made of cellulose; strengthens the cell and gives it support"),
           st("cell membrane", 120, 200, "L", "controls the movement of substances into and out of the cell"),
           st("chloroplast", 300, 70, "R", "absorbs light energy for photosynthesis"),
           st("vacuole", 230, 160, "R", "contains cell sap; keeps the cell firm / turgid"),
           st("mitochondrion", 240, 240, "R", "site of aerobic respiration"),
           st("cytoplasm", 300, 115, "R", "where most chemical reactions take place")]

ANIMAL = "".join([path("M 120 150 C 110 70 230 40 300 70 C 360 95 350 200 300 230 C 230 270 130 240 120 150 Z"),
                  '<circle cx="230" cy="150" r="30" stroke="currentColor" fill="none" stroke-width="1.5"/>',
                  '<circle cx="232" cy="148" r="8" fill="currentColor" opacity="0.4"/>',
                  ''.join(ell(x, y, 11, 5) for x, y in [(160, 120), (290, 190), (175, 205)]),
                  ''.join(f'<circle cx="{x}" cy="{y}" r="1.6" fill="currentColor"/>' for x, y in [(280, 110), (285, 120), (292, 112), (150, 170), (158, 176)])])
ANIMAL_S = [st("cell membrane", 122, 150, "L", "controls the movement of substances into and out of the cell"),
            st("mitochondrion", 160, 120, "L", "site of aerobic respiration"),
            st("cytoplasm", 175, 175, "L", "where most chemical reactions take place"),
            st("nucleus", 250, 140, "R", "contains genetic material that controls the activities of the cell"),
            st("ribosome", 285, 115, "R", "site of protein synthesis"),
            st("mitochondrion ", 290, 190, "R", "site of aerobic respiration")][:5]

LEAF = "".join(['<rect x="80" y="40" width="280" height="6" stroke="currentColor" fill="currentColor" fill-opacity="0.2"/>',
                ''.join(f'<rect x="{80+i*28}" y="46" width="28" height="18" stroke="currentColor" fill="none" stroke-width="1"/>' for i in range(10)),
                ''.join(f'<rect x="{82+i*20}" y="66" width="16" height="56" rx="6" stroke="currentColor" fill="none" stroke-width="1"/>' for i in range(14)),
                ''.join(f'<circle cx="{x}" cy="{y}" r="2.5" fill="currentColor" opacity="0.6"/>' for i in range(14) for x, y in [(90 + i * 20, 80), (90 + i * 20, 105)]),
                ''.join(f'<circle cx="{95+((i*37)%260)}" cy="{140+((i*23)%60)}" r="11" stroke="currentColor" fill="none" stroke-width="1"/>' for i in range(16)),
                '<circle cx="220" cy="160" r="16" stroke="currentColor" fill="none" stroke-width="1.5"/>',
                ''.join(f'<rect x="{80+i*28}" y="212" width="28" height="16" stroke="currentColor" fill="none" stroke-width="1"/>' for i in range(10) if i != 6),
                ell(253, 220, 8, 6), ell(275, 220, 8, 6)])
LEAF_S = [st("waxy cuticle", 120, 42, "L", "reduces water loss by evaporation"),
          st("upper epidermis", 110, 55, "L", "transparent, so light passes through to the mesophyll"),
          st("palisade mesophyll cell", 112, 95, "L", "contains many chloroplasts; main site of photosynthesis"),
          st("spongy mesophyll", 130, 170, "L", "has air spaces that allow gases to diffuse"),
          st("xylem / vein", 220, 160, "R", "transports water and mineral ions to the leaf"),
          st("air space", 300, 185, "R", "allows carbon dioxide to diffuse to cells"),
          st("guard cell", 275, 220, "R", "opens and closes the stoma")]

GUT = "".join([path("M 220 20 L 220 90"), path("M 230 20 L 230 90"),
               path("M 220 90 C 200 110 210 150 250 150 C 300 150 320 110 300 90 C 280 70 240 80 230 90"),
               path("M 120 90 C 140 60 210 70 215 95 C 210 120 150 130 120 110 Z"),
               '<rect x="240" y="155" width="70" height="14" rx="7" stroke="currentColor" fill="none" stroke-width="1.5"/>',
               path("M 150 270 L 150 170 L 320 170 L 320 260"),
               path("M 180 190 c 20 -10 40 10 60 0 c 20 -10 40 10 60 0 M 180 215 c 20 -10 40 10 60 0 c 20 -10 40 10 60 0 M 180 240 c 20 -10 40 10 60 0 c 20 -10 40 10 60 0"),
               path("M 150 270 L 150 290")])
GUT_S = [st("oesophagus", 220, 40, "L", "carries food from the mouth to the stomach by peristalsis"),
         st("liver", 140, 95, "L", "makes bile"),
         st("large intestine / colon", 150, 220, "L", "absorbs water from undigested food"),
         st("rectum", 150, 280, "L", "stores faeces"),
         st("stomach", 280, 110, "R", "produces protease and hydrochloric acid / churns food"),
         st("pancreas", 300, 162, "R", "produces amylase, protease and lipase"),
         st("small intestine", 280, 215, "R", "completes digestion and absorbs soluble food molecules")]

THORAX = "".join([path("M 214 20 L 214 90 M 226 20 L 226 90"),
                  path("M 214 90 L 170 120 M 226 90 L 270 120"),
                  path("M 170 120 l -20 20 m 20 -20 l -5 30 M 270 120 l 20 20 m -20 -20 l 5 30"),
                  path("M 205 70 C 120 60 100 160 120 230 C 150 245 190 240 205 220 Z"),
                  path("M 235 70 C 320 60 340 160 320 230 C 290 245 250 240 235 220 Z"),
                  ''.join(path(f"M {x0} {y} q -30 -10 -50 10") for x0, y in [(110, 80), (100, 120), (95, 160), (95, 200)]),
                  ''.join(path(f"M {x0} {y} q 30 -10 50 10") for x0, y in [(330, 80), (340, 120), (345, 160), (345, 200)]),
                  path("M 90 250 C 150 210 290 210 350 250", 'stroke-width="3"'),
                  ''.join(f'<circle cx="{x}" cy="{y}" r="4" stroke="currentColor" fill="none" stroke-width="1"/>' for x, y in [(148, 150), (154, 156), (290, 150)])])
THORAX_S = [st("trachea", 214, 50, "L", "carries air to and from the lungs; held open by rings of cartilage"),
            st("bronchus", 190, 105, "L", "carries air into each lung"),
            st("rib", 75, 165, "L", "protects the lungs; moves up and out when breathing in"),
            st("alveolus / air sac", 150, 152, "L", "site of gas exchange"),
            st("bronchiole", 290, 135, "R", "carries air to the alveoli"),
            st("intercostal muscle", 368, 140, "R", "contracts to move the ribs up and out during inhalation"),
            st("diaphragm", 300, 235, "R", "contracts and flattens to increase the volume of the thorax")]

HEART = "".join([path("M 120 110 C 120 60 200 60 210 110 L 210 280 C 160 280 120 230 120 180 Z"),
                 path("M 230 110 C 240 60 320 60 320 110 L 320 180 C 320 230 280 280 230 280 Z"),
                 path("M 120 160 L 210 160 M 230 160 L 320 160"),
                 '<rect x="210" y="100" width="20" height="180" stroke="currentColor" fill="currentColor" fill-opacity="0.15" stroke-width="1"/>',
                 path("M 235 100 C 235 40 280 20 330 30 M 255 100 C 255 55 290 45 330 50"),
                 path("M 150 75 L 150 20 M 170 72 L 170 20"),
                 path("M 190 95 C 195 50 230 40 260 20 M 205 100 C 210 60 240 55 275 35"),
                 path("M 330 120 L 380 120 M 330 135 L 380 135"),
                 path("M 145 160 l 15 15 l 15 -15 M 255 160 l 15 15 l 15 -15")])
HEART_S = [st("vena cava", 160, 30, "L", "brings deoxygenated blood from the body to the heart"),
           st("right atrium", 150, 125, "L", "receives deoxygenated blood from the body"),
           st("right ventricle", 160, 220, "L", "pumps deoxygenated blood to the lungs"),
           st("aorta", 300, 38, "R", "carries oxygenated blood to the body"),
           st("pulmonary artery", 225, 55, "L", "carries deoxygenated blood to the lungs"),
           st("pulmonary vein", 360, 128, "R", "brings oxygenated blood from the lungs"),
           st("left ventricle", 280, 220, "R", "has a thick muscular wall; pumps oxygenated blood to the body"),
           st("septum", 220, 240, "R", "separates oxygenated and deoxygenated blood")]

NEPH = "".join([path("M 80 70 C 80 40 130 40 130 70 C 130 95 80 95 80 70", 'stroke-dasharray="1 0"'),
                path("M 70 70 C 70 25 140 25 140 70 C 140 85 130 95 120 100"),
                path("M 95 60 c 10 -10 20 10 10 15 c -10 5 -20 -10 -5 -15", 'stroke-width="2.5"'),
                path("M 120 100 C 160 110 140 140 180 140 C 220 140 200 100 230 110 L 230 140"),
                path("M 230 140 L 230 260 C 230 280 260 280 260 260 L 260 150"),
                path("M 260 150 C 270 120 300 140 310 110 C 320 90 340 100 350 90"),
                path("M 350 40 L 350 290 M 365 40 L 365 290")])
NEPH_S = [st("glomerulus", 102, 66, "L", "knot of capillaries where ultrafiltration happens"),
          st("Bowman's capsule", 72, 80, "L", "collects the glomerular filtrate"),
          st("proximal convoluted tubule", 160, 130, "L", "selective reabsorption of glucose"),
          st("loop of Henle", 245, 265, "L", "helps to concentrate the urine / reabsorbs water"),
          st("distal convoluted tubule", 300, 128, "R", "adjusts the ion content of the blood"),
          st("collecting duct", 365, 200, "R", "water is reabsorbed here under the control of ADH")]

EYE = "".join(['<circle cx="230" cy="150" r="110" stroke="currentColor" fill="none" stroke-width="2"/>',
               path("M 140 85 C 100 110 100 190 140 215", 'stroke-width="1.5"'),
               ell(150, 150, 14, 36),
               path("M 135 105 L 135 130 M 135 170 L 135 195", 'stroke-width="4"'),
               path("M 150 114 L 165 80 M 150 186 L 165 220", 'stroke-width="1"'),
               ell(165, 75, 10, 6), ell(165, 225, 10, 6),
               path("M 248 45 C 340 70 360 220 248 255", 'stroke-width="3"'),
               path("M 335 140 L 400 130 M 335 160 L 400 170"),
               '<circle cx="338" cy="150" r="5" fill="currentColor"/>'])
EYE_S = [st("cornea", 115, 150, "L", "refracts / bends light entering the eye"),
         st("iris", 135, 118, "L", "controls the size of the pupil"),
         st("lens", 155, 150, "L", "focuses light onto the retina"),
         st("ciliary muscle", 165, 225, "L", "contracts or relaxes to change the shape of the lens"),
         st("suspensory ligament", 160, 205, "L", "attaches the lens to the ciliary muscle"),
         st("retina", 320, 90, "R", "contains receptor cells (rods and cones) that detect light"),
         st("optic nerve", 395, 150, "R", "carries impulses from the retina to the brain"),
         st("fovea", 338, 150, "R", "part of the retina with most cones; gives sharp vision")]

FLOWER = "".join([path("M 220 290 L 220 190"), path("M 220 200 C 160 200 120 180 110 150 C 150 150 190 170 220 195"),
                  path("M 220 200 C 280 200 320 180 330 150 C 290 150 250 170 220 195"),
                  path("M 200 195 C 150 120 140 70 170 40 C 200 70 210 140 205 190"),
                  path("M 240 195 C 290 120 300 70 270 40 C 240 70 230 140 235 190"),
                  ell(220, 175, 22, 18), ell(220, 175, 4, 4), ell(212, 170, 3, 3),
                  path("M 220 157 L 220 85"), '<rect x="208" y="72" width="24" height="12" rx="4" stroke="currentColor" fill="currentColor" fill-opacity="0.2"/>',
                  path("M 200 175 L 185 90 M 240 175 L 255 90"), ell(185, 84, 9, 6), ell(255, 84, 9, 6)])
FLOWER_S = [st("petal", 160, 80, "L", "brightly coloured to attract insects"),
            st("anther", 185, 84, "L", "produces pollen grains (male gametes)"),
            st("filament", 192, 130, "L", "supports the anther"),
            st("sepal", 140, 165, "L", "protects the flower when it is a bud"),
            st("stigma", 225, 78, "R", "sticky surface that catches pollen"),
            st("style", 220, 120, "R", "connects the stigma to the ovary; pollen tube grows through it"),
            st("ovary", 238, 178, "R", "contains ovules; becomes the fruit"),
            st("ovule", 220, 175, "R", "contains the female gamete; becomes the seed")]

FEM = "".join([path("M 180 120 C 180 200 200 220 220 220 C 240 220 260 200 260 120 Z"),
               path("M 180 125 C 150 100 120 100 100 125 M 260 125 C 290 100 320 100 340 125"),
               ell(95, 145, 18, 12), ell(345, 145, 18, 12),
               path("M 210 220 L 210 240 M 230 220 L 230 240"),
               path("M 205 240 L 205 290 M 235 240 L 235 290"),
               path("M 190 130 C 190 190 205 205 220 205 C 235 205 250 190 250 130", 'stroke-dasharray="3 2"')])
FEM_S = [st("ovary", 95, 145, "L", "produces eggs and the hormones oestrogen and progesterone"),
         st("oviduct / fallopian tube", 130, 105, "L", "carries the egg to the uterus; fertilisation happens here"),
         st("cervix", 210, 232, "L", "ring of muscle at the entrance to the uterus"),
         st("vagina", 205, 270, "L", "receives sperm during intercourse"),
         st("uterus", 245, 160, "R", "where the embryo implants and develops"),
         st("uterus lining", 250, 140, "R", "thickens to receive an embryo / forms part of the placenta")]

FERM = "".join(['<rect x="140" y="50" width="160" height="220" rx="20" stroke="currentColor" fill="none" stroke-width="2"/>',
                '<rect x="128" y="70" width="184" height="190" rx="24" stroke="currentColor" fill="none" stroke-width="1" stroke-dasharray="4 3"/>',
                path("M 220 20 L 220 230"), path("M 195 150 L 245 150 M 195 210 L 245 210", 'stroke-width="4"'),
                path("M 100 250 L 180 250 L 180 240", 'stroke-width="1.5"'),
                path("M 280 20 L 280 60"), path("M 160 20 L 160 60"),
                path("M 300 120 L 340 120 M 300 180 L 340 180"),
                path("M 220 270 L 220 295"),
                path("M 270 140 L 270 100 L 340 90", 'stroke-width="1"')])
FERM_S = [st("nutrient inlet", 160, 30, "L", "adds nutrients / glucose for respiration and growth"),
          st("stirring paddles", 200, 150, "L", "mix the contents so nutrients and temperature are even"),
          st("air inlet / sparger", 110, 250, "L", "supplies oxygen for aerobic respiration"),
          st("motor shaft", 220, 40, "R", "turns the stirrer"),
          st("water jacket", 310, 120, "R", "carries cold water to remove heat and keep the temperature constant"),
          st("temperature / pH probe", 300, 95, "R", "monitors conditions so they stay at the optimum"),
          st("outlet for product", 220, 290, "R", "allows the product to be removed")]

DIAGRAMS = {
    "variety.groups": [("1.3", "The diagram shows a bacterial cell.", BACT, BACT_S)],
    "structures.cells": [("2.2", "The diagram shows a plant cell.", PLANT, PLANT_S), ("2.2", "The diagram shows an animal cell.", ANIMAL, ANIMAL_S)],
    "structures.plant-nutrition": [("2.21", "The diagram shows a section through part of a leaf.", LEAF, LEAF_S)],
    "structures.human-nutrition": [("2.27", "The diagram shows part of the human digestive system.", GUT, GUT_S)],
    "structures.gas-exchange-humans": [("2.46", "The diagram shows the human thorax.", THORAX, THORAX_S)],
    "structures.heart": [("2.65", "The diagram shows a section through the human heart.", HEART, HEART_S)],
    "structures.excretion": [("2.74B", "The diagram shows a nephron from a kidney.", NEPH, NEPH_S)],
    "structures.nervous": [("2.91", "The diagram shows a section through the human eye.", EYE, EYE_S)],
    "reproduction.plant-reproduction": [("3.3", "The diagram shows a section through an insect-pollinated flower.", FLOWER, FLOWER_S)],
    "reproduction.human-reproduction": [("3.8", "The diagram shows the female reproductive system.", FEM, FEM_S)],
    "resources.microorganisms": [("5.8", "The diagram shows an industrial fermenter.", FERM, FERM_S)],
}


def gen(sub):
    out = []
    per = 15 if len(DIAGRAMS[sub]) == 1 else 8
    for di, (ref, intro, body, structs) in enumerate(DIAGRAMS[sub]):
        letters = assign_letters(structs)
        fig = svg_fig(build_svg(body, structs, letters), 90)
        n = len(structs)
        nm = sub.split(".")[-1]
        rng = random.Random(f"{sub}-{di}")
        qs = []
        # name pairs / triples
        combos = list(itertools.combinations(range(n), 2))
        rng.shuffle(combos)
        for a, b in combos[: per // 2]:
            la, lb = letters[a], letters[b]
            p = [text_part("", f"Name the structures labelled {la} and {lb}.", 2, 2, figures=[fig])]
            r = [row_("", f"{la}: {structs[a].name.strip()} (1)\n{lb}: {structs[b].name.strip()} (1)", 2, "Ignore minor spelling errors if the meaning is clear", "AO1")]
            qs.append(dict(parts=p, rows=r, refs=[ref], cw="Name", diff="1-3", intro=intro, template=f"{nm}-diag-name"))
        # function -> letter + name
        idx = list(range(n))
        rng.shuffle(idx)
        for i in idx[: max(3, per // 4)]:
            s = structs[i]
            p = [text_part("a", f"Give the letter of the structure that {s.func.split(';')[0]}.", 1, 1, figures=[fig]),
                 text_part("b", "Name this structure.", 1, 1)]
            r = [row_("a", f"{letters[i]} (1)", 1, None, "AO1"), row_("b", f"{s.name.strip()} (1)", 1, "Allow ecf from (a) only if the name matches the letter given", "AO1")]
            qs.append(dict(parts=p, rows=r, refs=[ref], cw="Give", diff="1-3", intro=intro, template=f"{nm}-diag-func"))
        # mcq which letter
        rng.shuffle(idx)
        for i in idx[: max(2, per // 5)]:
            others = sorted({structs[j].name.strip() for j in range(n) if structs[j].name.strip() != structs[i].name.strip()})
            rng.shuffle(others)
            p, r = mcq_part(rng, "", f"Which structure is labelled {letters[i]}?", structs[i].name.strip(), others[:3], figures=[fig])
            qs.append(dict(parts=[p], rows=[r], refs=[ref], cw="Identify", diff="1-3", intro=intro, template=f"{nm}-diag-mcq", style="mcq"))
        # describe function of a labelled part
        rng.shuffle(idx)
        for i in idx[: max(2, per // 5)]:
            s = structs[i]
            other = structs[idx[(idx.index(i) + 1) % n]]
            j = structs.index(other)
            p = [text_part("a", f"Name structure {letters[i]}.", 1, 1, figures=[fig]),
                 text_part("b", f"Describe the function of structure {letters[j]}.", 2, 3)]
            fp = [x.strip() for x in other.func.split(";")]
            if len(fp) == 1:
                fp = [f"named as {other.name.strip()}", fp[0]]
            r = [row_("a", f"{s.name.strip()} (1)", 1, None, "AO1"),
                 points_row("b", 2, fp, "Describe", "First mark may be given for correctly naming the structure if the function is correct", "AO1")]
            qs.append(dict(parts=p, rows=r, refs=[ref], cw="Describe", diff="4-6", intro=intro, template=f"{nm}-diag-desc"))
        out += qs
    return out


def _make(sub):
    @reg(sub, "diagram", f"{sub.split('.')[-1]}-diag")
    def f():
        return gen(sub)
    return f


for _s in DIAGRAMS:
    _make(_s)
