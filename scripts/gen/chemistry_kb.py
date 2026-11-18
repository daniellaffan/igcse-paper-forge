"""Engines that turn hand-written knowledge items into templates.

facts(sub, list)        -> an MCQ template and a recall template
items(sub, qtype, list) -> describe / explain / practical / data templates
extended(sub, list)     -> 6-mark levels-marked templates

Item dictionaries (all text is our own):
  fact:  q (recall stem) a (answer) m (marks) n (notes) ref d
         mq (MCQ stem) c (MCQ key, default a) w (distractors) intro
  item:  s (stem) m (marks) p (points) any (bool) n (notes) ref d intro figs cw lines
         v (list of dicts substituted into s / p / intro with str.format)
  ext:   s intro figs ind (indicative points) ref d ao title
"""
from chemistry_util import tpl, mcq, pts, anyof, lv6, LV_GENERAL, P, F, row

AO = {"mcq": ["AO1"], "recall": ["AO1"], "describe": ["AO1"], "explain": ["AO1", "AO2"],
      "calculation": ["AO2"], "equation": ["AO1", "AO2"], "practical": ["AO3"], "data": ["AO2", "AO3"],
      "extended": ["AO1", "AO2"]}
LAB = "abcdefgh"


def _refs(x, default):
    if x is None:
        return [default]
    return [x] if isinstance(x, str) else list(x)


def _cw(stem, default="Give"):
    w = stem.split()[0].strip("*") if stem else default
    return w if w in ("Give", "State", "Name", "Explain", "Describe", "Suggest", "Identify", "Deduce",
                      "Calculate", "Complete", "Draw", "Predict", "Determine", "Write", "Compare", "Show",
                      "Use", "Plot", "What", "Which", "Evaluate", "Comment") else default


def facts(sub, ref0, flist, intro=None, mcq_n=12, recall_n=12, tag=None):
    tag = tag or sub.split(".")[-1]
    mq = [f for f in flist if f.get("mq")]
    rq = [f for f in flist if f.get("q")]

    def make_mcq(r, k):
        if k >= len(mq):
            return None
        f = mq[k]
        part, rw = mcq(r, F(f["mq"]), F(f.get("c", f.get("a"))), [F(x) for x in f["w"]], notes=f.get("mn"))
        part["label"] = ""
        return {"command_word": _cw(f["mq"], "What"), "difficulty": f.get("d", "1-3"), "parts": [part],
                "markscheme": {"style": "mcq", "rows": [rw]}, "spec_refs": _refs(f.get("ref"), ref0),
                "intro": F(f["intro"]) if f.get("intro") else None, "ao": ["AO1"]}

    def make_recall(r, k):
        if not rq:
            return None
        if k < len(rq):
            chosen = [rq[k]]
        else:
            n = 2 if len(rq) < 6 or r.random() < 0.6 else 3
            chosen = r.sample(rq, min(n, len(rq)))
        parts, rows, refs, ds = [], [], [], []
        multi = len(chosen) > 1
        for i, f in enumerate(chosen):
            lab = LAB[i] if multi else ""
            m = f.get("m", 1)
            parts.append(P(lab, F(f["q"]), m, **({"lines": f["lines"]} if f.get("lines") else {})))
            if m == 1 or not f.get("pts"):
                rows.append(row(lab, F(f["a"]), m, F(f["n"]) if f.get("n") else None, "AO1"))
            elif len(f["pts"]) > m or f.get("any"):
                rows += anyof(lab, m, [F(x) for x in f["pts"]], F(f["n"]) if f.get("n") else None, ao="AO1")
            else:
                rows += pts(lab, [F(x) for x in f["pts"]], ({m - 1: F(f["n"])} if f.get("n") else None), ao="AO1")
            for x in _refs(f.get("ref"), ref0):
                if x not in refs:
                    refs.append(x)
            ds.append(f.get("d", "1-3"))
        order = ["1-3", "4-6", "7-9"]
        d = max(ds, key=order.index)
        it = intro if multi else (chosen[0].get("intro") or None)
        return {"command_word": _cw(chosen[0]["q"]), "difficulty": d, "parts": parts,
                "markscheme": {"style": "points", "rows": rows}, "spec_refs": refs,
                "intro": F(it) if it else None, "ao": ["AO1"]}

    make_mcq.__name__ = f"{tag}_mcq_facts"
    make_recall.__name__ = f"{tag}_recall_facts"
    if mq:
        tpl(sub, "mcq", min(mcq_n, len(mq)))(make_mcq)
    if rq:
        tpl(sub, "recall", recall_n)(make_recall)


def _expand(ilist):
    out = []
    for it in ilist:
        for v in it.get("v", [None]):
            out.append((it, v or {}))
    return out


def _fmt(s, v):
    return s.format(**v) if v and s else s


def _item_q(it, v, lab, qtype):
    m = it["m"]
    stem = F(_fmt(it["s"], v))
    p = [F(_fmt(x, v)) for x in it["p"]]
    notes = it.get("n")
    notes = F(_fmt(notes, v)) if isinstance(notes, str) else notes
    kw = {}
    for k in ("lines", "space", "answer_prefix", "choices"):
        if k in it:
            kw[k] = it[k]
    part = P(lab, stem, m, **kw)
    if it.get("pfigs"):
        part["figures"] = it["pfigs"](v) if callable(it["pfigs"]) else it["pfigs"]
    ao = AO[qtype][-1]
    if it.get("any") or len(p) != m:
        rows = anyof(lab, m, p, notes if isinstance(notes, str) else None, lead=it.get("lead"), ao=ao)
    else:
        lead = it.get("lead") or ({"explain": "Explanation linking (one mark each)",
                                   "describe": "Description covering (one mark each)"}
                                  .get(qtype) if m > 1 else None)
        rows = pts(lab, p, notes if isinstance(notes, dict) else ({len(p) - 1: notes} if notes else None),
                   lead=lead, ao=ao)
    return part, rows


def items(sub, qtype, ref0, ilist, n=12, tag=None, intro=None, pair=True):
    tag = tag or sub.split(".")[-1]
    ex = _expand(ilist)

    def make(r, k):
        if k < len(ex):
            chosen = [ex[k]]
        elif pair and len(ex) >= 2:
            chosen = r.sample(ex, 2)
            # avoid two variants of the same item
            if chosen[0][0] is chosen[1][0]:
                return None
        else:
            return None
        parts, rows, refs, ds, figs = [], [], [], [], []
        multi = len(chosen) > 1
        intros = []
        for i, (it, v) in enumerate(chosen):
            lab = LAB[i] if multi else ""
            part, rw = _item_q(it, v, lab, qtype)
            if multi and it.get("intro"):
                # move the item's context into the part so that each part keeps its own stem
                part["text"] = F(_fmt(it["intro"], v)) + "\n\n" + part["text"]
                if it.get("figs"):
                    part["figures"] = (part.get("figures") or []) + (it["figs"](v) if callable(it["figs"]) else it["figs"])
            elif it.get("intro"):
                intros.append(F(_fmt(it["intro"], v)))
                if it.get("figs"):
                    figs += it["figs"](v) if callable(it["figs"]) else it["figs"]
            elif it.get("figs"):
                figs += it["figs"](v) if callable(it["figs"]) else it["figs"]
            parts.append(part)
            rows += rw
            for x in _refs(it.get("ref"), ref0):
                if x not in refs:
                    refs.append(x)
            ds.append(it.get("d", "4-6"))
        order = ["1-3", "4-6", "7-9"]
        it0 = chosen[0][0]
        q = {"command_word": it0.get("cw") or _cw(it0["s"], "Explain" if qtype == "explain" else "Describe"),
             "difficulty": max(ds, key=order.index), "parts": parts,
             "markscheme": {"style": "points", "rows": rows}, "spec_refs": refs, "ao": AO[qtype]}
        it_text = "\n\n".join(intros) if intros else (intro if multi else None)
        if it_text:
            q["intro"] = it_text
        if figs:
            q["figures"] = figs
        return q

    make.__name__ = f"{tag}_{qtype}_items"
    tpl(sub, qtype, max(n, len(ex)))(make)


def extended(sub, ref0, elist, tag=None, n=None):
    tag = tag or sub.split(".")[-1]
    ex = _expand(elist)

    def make(r, k):
        if k >= len(ex):
            return None
        it, v = ex[k]
        ind = [F(_fmt(x, v)) for x in it["ind"]]
        part = P("", F(_fmt(it["s"], v)), 6, lines=16)
        q = {"command_word": it.get("cw") or _cw(it["s"], "Describe"), "difficulty": it.get("d", "7-9"),
             "parts": [part],
             "markscheme": {"style": "points", "rows": [row(
                 "", "any six from:\n" + "\n".join(f"M{i + 1} {x}" for i, x in enumerate(ind)), 6,
                 "max 6; one mark for each distinct creditworthy point; credit any other valid chemistry relevant to the question; "
                 "IGNORE repetition of the same point")]},
             "spec_refs": _refs(it.get("ref"), ref0), "ao": ["AO1", "AO2"] if "AO3" not in it.get("ao", "") else ["AO1", "AO3"]}
        if it.get("intro"):
            q["intro"] = F(_fmt(it["intro"], v))
        if it.get("figs"):
            q["figures"] = it["figs"](v) if callable(it["figs"]) else it["figs"]
        return q

    make.__name__ = f"{tag}_extended_items"
    tpl(sub, "extended", n or len(ex))(make)
