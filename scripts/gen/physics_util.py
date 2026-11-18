"""Shared machinery for the physics generator.

* T(sub, qtype, n)  - register a parametric template: fn(r) -> question dict
* kb(sub, ...)       - register knowledge items (recall/describe/explain/mcq/extended)
                       which `kb_questions` combines into multi-part questions
* calc rows, number formatting, levels grid
"""
import itertools
import math
import random
import re
import sys
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import row, levels  # noqa: E402,F401

TEMPLATES = []          # (sub, qtype, n, name, fn)
KB = {}                 # sub -> {"themes": [...], qtype: [items]}


def T(sub, qtype, n=13, name=None):
    def deco(fn):
        TEMPLATES.append((sub, qtype, n, name or fn.__name__, fn))
        return fn
    return deco


# ------------------------------------------------------------------ numbers

SUP = str.maketrans("-0123456789", "⁻⁰¹²³⁴⁵⁶⁷⁸⁹")


def sf(x, n=3):
    """Round to n significant figures and return a plain string (no float noise)."""
    if x == 0:
        return "0"
    d = n - int(math.floor(math.log10(abs(x)))) - 1
    q = Decimal(repr(float(x))).quantize(Decimal(1).scaleb(-d), rounding=ROUND_HALF_UP) if d > 0 else \
        (Decimal(repr(float(x))) / Decimal(10) ** (-d)).quantize(Decimal(1), rounding=ROUND_HALF_UP) * Decimal(10) ** (-d)
    if d > 0:
        return f"{q:.{d}f}"
    return str(int(q))


def num(x, n=3, std=None):
    """Formatted number; uses standard form (plain text with ×10ⁿ) for very large/small values."""
    if x == 0:
        return "0"
    e = int(math.floor(math.log10(abs(x))))
    if std or (std is None and (e >= 6 or e <= -4)):
        m = x / 10 ** e
        ms = sf(m, n)
        if ms.startswith("10"):
            e += 1
            ms = sf(x / 10 ** e, n)
        return f"{ms} × 10{str(e).translate(SUP)}"
    return sf(x, n)


def clean(x):
    """Exact-looking string for a given quantity (strip float noise)."""
    if abs(x - round(x)) < 1e-9:
        return str(int(round(x)))
    return f"{x:.6g}"


def alts(x, unit="", ns=(2, 3, 4)):
    """'allow' string listing the value at several s.f."""
    vals = []
    for n in ns:
        s = num(x, n)
        if s not in vals:
            vals.append(s)
    return "allow " + ", ".join(vals)


# ------------------------------------------------------------------ mark-scheme helpers

def calc_rows(label, eq, working, ans, unit, rearr=True, notes=None, pot=True, subst=True):
    rows = []
    if subst:
        rows.append(row(label, f"substitution into {eq};", 1))
    if rearr:
        rows.append(row(label, "rearrangement;", 1))
    ev = "evaluation;\ne.g.\n" + "\n".join(working) + f"\n(answer =) {ans}" + (f" ({unit})" if unit else "")
    nt = [n for n in [notes, "-1 for POT error" if pot else None] if n]
    rows.append(row(label, ev, 1, "; ".join(nt) if nt else None))
    return rows


def eq_row(label, eq, extra=None):
    n = "allow rearrangements and standard symbols"
    if extra:
        n += "; " + extra
    n += "; reject an equation written only in units"
    return row(label, eq, 1, n)


def work_part(label, text, marks, prefix, lines=None):
    p = {"label": label, "text": text, "marks": marks, "space": "working", "answer_prefix": prefix}
    if lines:
        p["lines"] = lines
    return p


def line_part(label, text, marks, lines=None, prefix=None):
    p = {"label": label, "text": text, "marks": marks, "space": "lines", "lines": lines if lines is not None else max(1, marks + 1)}
    if prefix:
        p["answer_prefix"] = prefix
    return p


def mcq_part(label, text, choices):
    return {"label": label, "text": text, "marks": 1, "space": "mcq", "choices": choices}


LEVELS6 = [
    ("0", "0", "No rewardable material."),
    ("1", "1-2", "Isolated relevant physics points; ideas are not linked and key terms are used loosely or wrongly. Answer covers only a small part of the question."),
    ("2", "3-4", "Several relevant points with some linked reasoning; most terms used correctly. Some aspects of the question are missing or underdeveloped."),
    ("3", "5-6", "Detailed, logically ordered answer covering all the main aspects of the question; points are linked by clear physics reasoning and terms are used precisely."),
]


def levels6(part, indicative, title=None):
    return levels(part, LEVELS6, indicative, title=title, ao_split="AO1 3, AO2 3")


# ------------------------------------------------------------------ knowledge items

def K(t, m, pts, r, cmd=None, d="1-3", lines=None, ao="AO1", fig=None):
    """Short-answer knowledge item. pts: 'answer | notes' strings. More points than marks = 'any m from'."""
    if cmd is None:
        cmd = t.split()[0].strip(",.")
    return {"t": t, "m": m, "pts": pts, "r": r.split() if isinstance(r, str) else r, "cmd": cmd, "d": d,
            "lines": lines, "ao": ao, "fig": fig}


def M(stem, choices, r, ans=0, why=None, ordered=False, d="1-3", ao="AO1", fig=None):
    """Multiple-choice item; the correct answer is choices[ans]."""
    return {"stem": stem, "ch": choices, "a": ans, "r": r.split() if isinstance(r, str) else r, "why": why,
            "ordered": ordered, "d": d, "ao": ao, "fig": fig}


def X(t, indicative, r, d="7-9", fig=None, title=None):
    """Six-mark extended-response prompt."""
    return {"t": t, "ind": indicative, "r": r.split() if isinstance(r, str) else r, "d": d, "fig": fig, "title": title}


def kb(sub, themes, **pools):
    KB.setdefault(sub, {"themes": []})
    KB[sub]["themes"] += themes
    for k, v in pools.items():
        KB[sub].setdefault(k, []).extend(v)


def split_pt(p):
    if " | " in p:
        a, n = p.split(" | ", 1)
        return a, n
    return p, None


def item_rows(label, it):
    pts = it["pts"]
    m = it["m"]
    if len(pts) > m:
        ans = f"any {['zero', 'one', 'two', 'three', 'four', 'five', 'six'][m]} from:\n" + "\n".join(
            f"MP{i + 1}. {split_pt(p)[0]};" for i, p in enumerate(pts))
        notes = "; ".join(f"MP{i + 1}: {split_pt(p)[1]}" for i, p in enumerate(pts) if split_pt(p)[1])
        return [row(label, ans, m, notes or None, it["ao"])]
    assert len(pts) == m, (it["t"], m, pts)
    out = []
    for p in pts:
        a, n = split_pt(p)
        out.append(row(label, a + ";", 1, n, it["ao"]))
    return out


def item_part(label, it):
    p = line_part(label, it["t"], it["m"], it["lines"] if it["lines"] is not None else (it["m"] * 2 if it["m"] > 1 else 1))
    if it.get("fig"):
        p["figures"] = [it["fig"]]
    return p


def mcq_build(label, it, r):
    ch = list(it["ch"])
    correct = ch[it["a"]]
    if not it["ordered"]:
        r.shuffle(ch)
    letter = "ABCD"[ch.index(correct)]
    p = mcq_part(label, it["stem"] + "\n\nPut a cross ( ☒ ) in the box next to your answer.", ch)
    if it.get("fig"):
        p["figures"] = [it["fig"]]
    notes = it["why"] or None
    return p, row(label, f"{letter} ({correct});", 1, notes, it["ao"]), letter


DIFF_ORDER = ["1-3", "4-6", "7-9"]


def combine_diff(ds):
    idx = sorted(DIFF_ORDER.index(d) for d in ds)
    return DIFF_ORDER[idx[len(idx) // 2]] if len(idx) < 3 else DIFF_ORDER[idx[-2]]


LAB = "abcdefgh"


def kb_questions(sub, qtype, n, seed):
    """Combine knowledge items into n distinct multi-part questions."""
    pool = KB.get(sub, {})
    # The intro is neutral (the subtopic's own title), so it can never name a context
    # that the randomly combined parts do not ask about.
    import physics_spec
    titles = {sid: st for _, _, _, subs in physics_spec.TOPICS for sid, _, st, *_ in subs}
    title = titles.get(sub, "this topic")
    title = title[0].lower() + title[1:] if not title[:2].isupper() else title
    r = random.Random(seed)
    out = []
    if qtype == "mcq":
        items = pool.get("mcq", [])
        combos = [(i,) for i in range(len(items))] + list(itertools.combinations(range(len(items)), 2)) + \
            list(itertools.combinations(range(len(items)), 3))
        sizes = None
    elif qtype == "extended":
        items = pool.get("extended", [])
        leads = pool.get("recall", []) + pool.get("describe", [])
        leads = [x for x in leads if x["m"] <= 3]
        combos = [("x", i, None) for i in range(len(items))] + [("x", i, j) for i in range(len(items)) for j in range(len(leads))]
    else:
        items = pool.get(qtype, [])
        idx = range(len(items))
        combos = [(i,) for i in idx if items[i]["m"] >= 2] + list(itertools.combinations(idx, 2)) + list(itertools.combinations(idx, 3))
        combos = [c for c in combos if sum(items[i]["m"] for i in c) <= 9]
    head = combos[:len(items)] if qtype != "extended" else combos[:len(items)]
    rest = combos[len(head):]
    r.shuffle(rest)
    combos = head + rest
    for ci, c in enumerate(combos):
        if len(out) >= n:
            break
        intro = f"This question is about {title}."
        if qtype == "mcq":
            its = [items[i] for i in c]
            parts, rows, refs, ds, figs = [], [], [], [], []
            letters = {}
            for k, it in enumerate(its):
                lab = LAB[k] if len(its) > 1 else ""
                p, rw, let = mcq_build(lab, it, r)
                rw["part"] = f"({lab})" if lab else ""
                parts.append(p)
                rows.append(rw)
                refs += it["r"]
                ds.append(it["d"])
                letters[lab or "answer"] = let
            q = dict(parts=parts, rows=rows, refs=refs, cmd="Which", d=combine_diff(ds), ao=sorted({i["ao"] for i in its}),
                     intro=intro, style="mcq", answer={"method": "fixed key", "values": letters, "checked": True})
            out.append(q)
        elif qtype == "extended":
            _, i, j = c
            x = items[i]
            parts, rows, refs = [], [], list(x["r"])
            ao = ["AO1", "AO2"]
            if j is not None:
                ld = leads[j]
                parts.append(item_part("a", ld))
                rows += item_rows("(a)", ld)
                refs += ld["r"]
                xl = "b"
            else:
                xl = ""
            xp = line_part(xl, x["t"], 6, 12)
            if x.get("fig"):
                xp["figures"] = [x["fig"]]
            parts.append(xp)
            n_ind = len(x["ind"])
            mps = "\n".join(f"MP{k + 1}. {p};" for k, p in enumerate(x["ind"]))
            rows.append(row(f"({xl})" if xl else "", f"any six from:\n{mps}", 6,
                            "max 6; credit any other valid, relevant physics point; points must relate to the context of the question"))
            q = dict(parts=parts, rows=rows, refs=refs, cmd=x["t"].split()[0].strip(",."), d=x["d"], ao=ao, intro=intro,
                     style="points", answer={"method": "point list", "values": {"points_available": n_ind}, "checked": True})
            out.append(q)
        else:
            its = [items[i] for i in c]
            parts, rows, refs, ds, aos = [], [], [], [], set()
            for k, it in enumerate(its):
                lab = LAB[k] if len(its) > 1 else ""
                parts.append(item_part(lab, it))
                rows += item_rows(f"({lab})" if lab else "", it)
                refs += it["r"]
                ds.append(it["d"])
                aos.add(it["ao"])
            q = dict(parts=parts, rows=rows, refs=refs, cmd=its[0]["cmd"], d=combine_diff(ds), ao=sorted(aos), intro=intro)
            out.append(q)
    return out


def pick(r, seq):
    return seq[r.randrange(len(seq))]


def nice(r, lo, hi, step):
    k = r.randint(int(round(lo / step)), int(round(hi / step)))
    v = k * step
    return round(v, 10)


def sigtext(q):
    bits = [q.get("intro", "")]

    def walk(ps):
        for p in ps:
            bits.append(p.get("text", ""))
            bits.extend(p.get("choices", []) or [])
            walk(p.get("parts", []) or [])
    walk(q["parts"])
    for fg in q.get("figures", []) or []:
        for rr in fg.get("rows", []) or []:
            bits.extend(rr)
    return re.sub(r"\s+", " ", " ".join(bits).lower())


def calc_q(*, intro, text, eq, working, ans, unit, prefix, refs, d, values, rearr=True, state=None, notes=None,
           figs=None, pre_parts=None, pre_rows=None, ao=("AO2",), cmd="Calculate", subst=True, lines=None):
    """Build a calculation question.

    state = (linking_words, equation_text, extra_note) adds a 1-mark 'State the equation' part first.
    pre_parts/pre_rows: extra parts before the calculation (already labelled).
    """
    parts, rows = list(pre_parts or []), list(pre_rows or [])
    labs = [p["label"] for p in parts]
    nxt = LAB[len(labs)]
    if state:
        link, eqt, extra = state
        parts.append(line_part(nxt, f"State the equation linking {link}.", 1, 1))
        rows.append(eq_row(f"({nxt})", eqt, extra))
        nxt = LAB[len(parts)]
    m = (1 if subst else 0) + (1 if rearr else 0) + 1
    if not parts:
        nxt = ""
    parts.append(work_part(nxt, text, m, prefix, lines))
    rows += calc_rows(f"({nxt})" if nxt else "", eq, working, ans, unit, rearr=rearr, notes=notes, subst=subst)
    q = dict(parts=parts, rows=rows, refs=refs, cmd=cmd, d=d, ao=list(ao), intro=intro,
             answer={"method": "python exact arithmetic", "values": values, "checked": True})
    if figs:
        q["figures"] = figs
    return q


def relabel(parts, rows, start=0):
    """Give flat parts labels a, b, c... starting at index `start` and fix row labels."""
    mp = {}
    for i, p in enumerate(parts):
        new = LAB[start + i]
        mp[p.get("label", "")] = new
        p["label"] = new
    for rw in rows:
        key = rw["part"].strip("()")
        if key in mp:
            rw["part"] = f"({mp[key]})"
    return parts, rows
