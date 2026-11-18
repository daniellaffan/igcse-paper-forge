"""Knowledge-base driven short-answer questions: mcq, recall, describe, explain.

Each subtopic KB (registered with kb(sub, ...)) holds
  facts    F(noun, ref, term, clue, accept)  -> forward MCQ, reverse MCQ, recall
  mcq      M(ref, stem, correct, d1, d2, d3)
  recall   R(ref, question, marks, points, notes)
  describe D(ref, stem, marks, points, notes, intro)
  explain  E(ref, stem, marks, points, notes, intro)
"""
import random
from collections import namedtuple

from biology_lib import mcq_part, points_row, text_part, row_, S, cap

Fact = namedtuple("Fact", "noun ref term clue accept")
Mc = namedtuple("Mc", "ref stem correct d diff")
Rc = namedtuple("Rc", "ref q marks pts notes")
Ex = namedtuple("Ex", "ref stem marks pts notes intro cw diff")

KB = {}


def F(noun, ref, term, clue, accept=None):
    return Fact(noun, ref, term, clue, accept)


def M(ref, stem, correct, d1, d2, d3, diff="1-3"):
    return Mc(ref, stem, correct, [d1, d2, d3], diff)


def R(ref, q, marks, pts, notes=None):
    if isinstance(pts, str):
        pts = [pts]
    return Rc(ref, q, marks, pts, notes)


def D(ref, stem, marks, pts, notes=None, intro=None, diff=None):
    return Ex(ref, stem, marks, pts, notes, intro, "Describe", diff)


def E(ref, stem, marks, pts, notes=None, intro=None, diff=None, cw="Explain"):
    return Ex(ref, stem, marks, pts, notes, intro, cw, diff)


def kb(sub, facts=(), mcq=(), recall=(), describe=(), explain=()):
    KB[S(sub)] = dict(facts=list(facts), mcq=list(mcq), recall=list(recall),
                      describe=list(describe), explain=list(explain))


def refs_of(s):
    return [r.strip() for r in s.split(",")]


# ------------------------------------------------------------ part builders

PAD_TERMS = ["respiration", "photosynthesis", "transpiration", "evaporation", "excretion", "digestion"]
PAD_CLUES = ["converts light energy into chemical energy", "releases energy from glucose in cells",
             "removes waste products of metabolism", "breaks large food molecules into small soluble ones"]


# same-category distractors for noun groups with fewer than four facts: noun -> (terms, clues)
NOUN_PAD = {
    "process": (["transpiration", "respiration"], ["evaporation of water from the surface of leaves", "release of energy from glucose in cells"]),
    "mineral ion": (["potassium", "calcium", "phosphate"], ["is needed to make the cellulose cell wall", "is needed to make starch"]),
    "type of respiration": (["photosynthesis"], ["produces glucose and oxygen using light energy"]),
    "gas": (["nitrogen", "water vapour", "methane"], ["is made in the leaf by respiration only in the light", "is absorbed by the leaf only at night"]),
    "substance in tobacco smoke": (["glucose", "cholesterol"], ["reduces heart rate and blood pressure", "widens the airways"]),
    "type of cell division": (["fertilisation", "mutation"], ["produces a zygote from two gametes", "joins two body cells together"]),
    "ecological pyramid": (["food web", "food chain"], ["shows the age of organisms at each trophic level", "shows the number of species in a habitat"]),
    "micro-organism": (["Penicillium", "Plasmodium"], ["is a protoctist used to make cheese", "is a virus used to make bread"]),
}


def _plural(w):
    return w + ("es" if w.endswith("s") else "s")


def noun_for(f):
    """Pluralise the noun when the clue starts with a plural verb (e.g. 'contain', 'have')."""
    w = f.clue.split()[0]
    if w.endswith("s") or w in ("is", "can", "has"):
        return f.noun
    ws = f.noun.split()
    if "of" in ws:
        ws[0] = _plural(ws[0])
    else:
        ws[-1] = _plural(ws[-1])
    return " ".join(ws)


def fact_forward(rng, f, facts, label=""):
    pool = [g.term for g in facts if g.noun == f.noun and g.term != f.term]
    rng.shuffle(pool)
    if len(pool) < 3:
        pool += [t for t in NOUN_PAD.get(f.noun, ([], []))[0] if t != f.term and t not in pool][:3 - len(pool)]
    if len(pool) < 3:
        pool += [t for t in PAD_TERMS if t != f.term and t not in pool][:3 - len(pool)]
    stem = f"Which {noun_for(f)} {f.clue}?"
    return mcq_part(rng, label, stem, f.term, pool[:3])


def opt_of(clue):
    import re as _re
    return cap(_re.sub(r"^(is|are|describes) ", "", clue))


def fact_reverse(rng, f, facts, label=""):
    pool = [opt_of(g.clue) for g in facts if g.noun == f.noun and g.term != f.term]
    rng.shuffle(pool)
    if len(pool) < 3:
        pool += [opt_of(c) for c in NOUN_PAD.get(f.noun, ([], []))[1] if opt_of(c) not in pool][:3 - len(pool)]
    if len(pool) < 3:
        pool += [opt_of(c) for c in PAD_CLUES if opt_of(c) not in pool][:3 - len(pool)]
    if "term" in f.noun:
        stem = f"Which of these is the meaning of the term *{f.term}*?"
    elif f.term[:1].isupper():
        stem = f"Which statement about {f.term} is correct?"
    else:
        stem = rng.choice([f"Which statement about the {f.term} is correct?", f"Which of these describes the {f.term}?"])
    stem = stem.replace("the the ", "the ")
    return mcq_part(rng, label, stem, opt_of(f.clue), pool[:3])


def fact_recall(f, label=""):
    q = f"Name the {noun_for(f)} that {f.clue}."
    notes = f"Accept {f.accept}" if f.accept else None
    return text_part(label, q, 1, lines=1), row_(label, f.term, 1, notes, "AO1")


def recall_part(r, label=""):
    p = text_part(label, r.q, r.marks, lines=max(1, r.marks * 2 - (1 if r.marks == 1 else 0)))
    if len(r.pts) == 1 and r.marks == 1:
        rw = row_(label, r.pts[0], 1, r.notes, "AO1")
    elif len(r.pts) == 1:
        rw = row_(label, r.pts[0], r.marks, r.notes, "AO1")
    else:
        rw = points_row(label, r.marks, r.pts, "Give", r.notes, "AO1")
    return p, rw


def ex_part(x, label=""):
    p = text_part(label, x.stem, x.marks)
    return p, points_row(label, x.marks, x.pts, x.cw, x.notes, "AO1" if x.cw == "Describe" else "AO2")


def ex_diff(x, i):
    if x.diff:
        return x.diff
    if x.marks <= 2:
        return "4-6" if x.cw == "Explain" or i % 3 else "1-3"
    return "7-9" if (x.cw == "Explain" and x.marks >= 4) or i % 4 == 3 else "4-6"


def first_word(text):
    return text.split()[0].strip(",.?")


# ------------------------------------------------------------ factories

def build_short(sub, qtypes, emit):
    k = KB.get(sub)
    if not k:
        return
    rng = random.Random("short-" + sub)
    facts, mcqs, recs, descs, expls = k["facts"], k["mcq"], k["recall"], k["describe"], k["explain"]
    short = sub.split(".")[-1]

    if "mcq" in qtypes:
        n = 0
        for f in facts:
            p, r = fact_forward(rng, f, facts)
            emit(sub, "mcq", f"{short}-mcq-fwd", [p], [r], [f.ref], "Which", "1-3")
            n += 1
        for i, f in enumerate(facts):
            p, r = fact_reverse(rng, f, facts)
            emit(sub, "mcq", f"{short}-mcq-rev", [p], [r], [f.ref], "Which", "1-3" if i % 3 else "4-6")
        for m in mcqs:
            p, r = mcq_part(rng, "", m.stem, m.correct, m.d)
            emit(sub, "mcq", f"{short}-mcq", [p], [r], refs_of(m.ref), first_word(m.stem), m.diff)

    if "recall" in qtypes:
        items = [("f", f) for f in facts] + [("r", r) for r in recs]
        for kind, it in items:
            if kind == "f":
                p, r = fact_recall(it)
                emit(sub, "recall", f"{short}-recall-fact", [p], [r], [it.ref], "Name", "1-3")
            else:
                p, r = recall_part(it)
                emit(sub, "recall", f"{short}-recall", [p], [r], refs_of(it.ref), first_word(it.q), "1-3")
        # composites: pairs and triples of distinct items
        rr = [it for kind, it in items if kind == "r"]
        ff = [it for kind, it in items if kind == "f"]
        npair = max(4, 14 - len(items))
        for j in range(npair):
            a = ff[j % len(ff)] if ff else None
            b = rr[j % len(rr)] if rr else None
            c = ff[(j + 3) % len(ff)] if len(ff) > 3 else None
            parts, rows, refs = [], [], []
            lab = iter("abc")
            if b:
                L = next(lab)
                p, r = recall_part(b, L)
                parts.append(p); rows.append(r); refs += refs_of(b.ref)
            if a:
                L = next(lab)
                p, r = fact_recall(a, L)
                parts.append(p); rows.append(r); refs.append(a.ref)
            if c and c is not a and j % 2 == 0:
                L = next(lab)
                p, r = fact_forward(rng, c, facts, L)
                parts.append(p); rows.append(r); refs.append(c.ref)
            if len(parts) >= 2:
                emit(sub, "recall", f"{short}-recall-multi", parts, rows, sorted(set(refs)),
                     first_word(parts[0]["text"]), "1-3")

    for qt, items in (("describe", descs), ("explain", expls)):
        if qt not in qtypes:
            continue
        for i, x in enumerate(items):
            p, r = ex_part(x)
            emit(sub, qt, f"{short}-{qt}", [p], [r], refs_of(x.ref), x.cw, ex_diff(x, i), intro=x.intro)
        # composites: lead-in recall/mcq part + the item
        lead = [("f", f) for f in facts] + [("r", r) for r in recs]
        if not lead:
            continue
        target = max(14, len(items) + len(items) // 2)
        combos = [(xi, li) for xi in range(len(items)) for li in range(len(lead))]
        random.Random(sub + qt).shuffle(combos)
        _cnt = {}
        _rank = []
        for c in combos:
            _cnt[c[0]] = _cnt.get(c[0], 0) + 1
            _rank.append((_cnt[c[0]], c))
        combos = [c for _, c in sorted(_rank, key=lambda t: t[0])]
        made = len(items)
        for j, (xi, li) in enumerate(combos):
            if made >= target:
                break
            x = items[xi]
            kind, it = lead[li]
            if kind == "f":
                if j % 2:
                    pa, ra = fact_forward(rng, it, facts, "a")
                else:
                    pa, ra = fact_recall(it, "a")
                ra_ref = [it.ref]
            else:
                pa, ra = recall_part(it, "a")
                ra_ref = refs_of(it.ref)
            pb, rb = ex_part(x, "b")
            intro = None
            if x.intro:
                pb["text"] = x.intro + "\n\n" + pb["text"]
            if emit(sub, qt, f"{short}-{qt}-multi", [pa, pb], [ra, rb], sorted(set(ra_ref + refs_of(x.ref))),
                    x.cw, ex_diff(x, j + 1), intro=intro):
                made += 1
