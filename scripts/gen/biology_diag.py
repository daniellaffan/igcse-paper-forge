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


from biology_art import (BACT, BACT_S, PLANT, PLANT_S, ANIMAL, ANIMAL_S, LEAF, LEAF_S, GUT, GUT_S, THORAX, THORAX_S,
                         HEART, HEART_S, NEPH, NEPH_S, EYE, EYE_S, FLOWER, FLOWER_S, FEM, FEM_S, FERM, FERM_S)


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
