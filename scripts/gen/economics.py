#!/usr/bin/env python3
"""Generator for the economics (4EC1-style) question bank.

    .venv/bin/python scripts/gen/economics.py

Builds data/spec/economics.json and data/bank/economics/<topic>.json. Deterministic (seeded).
All contexts are fictional and all wording is original; see style-guides/economics.md.
"""
import math
import random
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import Bank, row, levels  # noqa: E402
import economics_spec as SP  # noqa: E402
from economics_util import new_ctx, fill, cap, mcq_parts  # noqa: E402
from economics_calc import GEN  # noqa: E402
from economics_data import DGEN  # noqa: E402
from economics_diag import DIAG  # noqa: E402
import economics_kb1, economics_kb2, economics_kb3, economics_kb4  # noqa: E402,E401
import economics_kbfix  # noqa: E402
import economics_kbint  # noqa: E402
from economics_extracts import extend  # noqa: E402

KB = {}
for m in (economics_kb1, economics_kb2, economics_kb3, economics_kb4):
    KB.update(m.KB)
economics_kbfix.apply(KB)

TARGET = 14          # aim per subtopic x qtype cell (validator minimum is 12)
R = random.Random(40112)

# ---------------------------------------------------------------- levels grids (own wording)
L0 = ("Level 0", "0", "No rewardable material.")
GRID6 = [L0,
         ("Level 1", "1–2", "Some relevant knowledge and understanding of economic ideas, with little application to the context. Reasoning is asserted or made of separate points rather than linked chains."),
         ("Level 2", "3–4", "Accurate knowledge and understanding, applied to the context for most of the answer. Chains of reasoning are developed, although some steps may be missing or generic."),
         ("Level 3", "5–6", "Accurate knowledge and understanding, applied consistently to the context and to the data where relevant. Analysis is coherent, with well-developed and logical chains of reasoning.")]
GRID9 = [L0,
         ("Level 1", "1–3", "Isolated knowledge with limited application of economic terms and concepts to the context (AO2). Little use of the information; chains of reasoning are attempted but not developed (AO3). Only one side of the argument is considered, so the answer is unbalanced (AO4)."),
         ("Level 2", "4–6", "Some accurate knowledge applied to the context (AO2). Some use of the information, with chains of reasoning that are developed in places (AO3). Arguments for and against are given, but one side is much weaker or less developed than the other (AO4)."),
         ("Level 3", "7–9", "Accurate knowledge applied throughout, with appropriate use of economic terms and concepts (AO2). The information is used selectively and well, with logical, developed chains of reasoning (AO3). Developed arguments for and against are given; the answer is well balanced and coherent (AO4). A conclusion is not required.")]
GRID12 = [L0,
          ("Level 1", "1–4", "Some relevant knowledge with limited or no application to the context. Reasoning is simple, often a list of points. Any judgement is asserted and unsupported."),
          ("Level 2", "5–8", "Accurate knowledge applied to the context, with developed chains of reasoning, though the answer may lack balance. Evaluation considers alternative views and may reach a judgement, but the support for it is partial."),
          ("Level 3", "9–12", "Accurate knowledge applied consistently, making effective use of the context and data. Chains of reasoning are well developed and balanced. Evaluation is sustained and reaches a clear, supported judgement, for example by weighing short-run against long-run effects or considering what the outcome depends on.")]
CREDIT = "This indicative content is not exhaustive: credit any other valid economic points that are relevant to the question."
GENERAL6 = "Marks are awarded on a best-fit basis using the level descriptors. Answers do not need to be balanced for this question: one-sided, well-developed analysis can reach Level 3. Copying data without using it limits the answer to Level 1."
GENERAL9 = "Marks are awarded on a best-fit basis. An assess question needs arguments for and against: a one-sided answer cannot go beyond Level 1. A final conclusion or judgement is NOT required for 9 marks; Level 3 is reached by a well-balanced answer that develops both sides and uses the information in the extract. Do not reward an overall conclusion on its own."
GENERAL12 = "Marks are awarded on a best-fit basis. Level 3 requires balanced, developed analysis and a supported judgement that follows from the arguments made. Unsupported conclusions such as 'overall it is good' do not lift an answer out of Level 2."

# ---------------------------------------------------------------- bookkeeping
B = Bank("economics")
SUBS = SP.sub_index()
SEEN = set()


def norm(*bits):
    t = " ".join(b for b in bits if b).lower()
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9%.]", " ", t)).strip()


def add(sid, qtype, cw, diff, parts, rows, template, ao, levels_=None, intro=None, figures=None, answer=None, general=None, style=None, key_text=None):
    s = SUBS[sid]
    k = (sid, key_text or norm(intro or "", *[p.get("text", "") for p in parts], *[c for p in parts for c in p.get("choices", [])],
                               *[str(rw) for f in (figures or []) for rw in f.get("rows", [])]))
    if k in SEEN:
        return False
    SEEN.add(k)
    ms = {"style": style or ("levels" if levels_ and not rows else "mixed" if levels_ else "points"), "rows": rows}
    if levels_:
        ms["levels"] = levels_
    if general:
        ms["general"] = general
    B.add(topic=s["topic"], subtopic=sid, qtype=qtype, command_word=cw, difficulty=diff, parts=parts, markscheme=ms,
          spec_refs=s["points"], paper=[s["paper"]], ao=ao, template=template, intro=intro, figures=figures,
          calculator=True, answer=answer)
    return True


SUFFIX = ""   # appended to template ids for supplementary builds


def tk(sid):
    return subkey(sid) + SUFFIX


def subkey(sid):
    return sid.split(".")[-1]


def fills(n, fn):
    """Call fn(ctx) up to n*4 times until n successes."""
    ok = tries = 0
    while ok < n and tries < n * 6:
        tries += 1
        if fn(new_ctx(R)):
            ok += 1
    return ok


# ---------------------------------------------------------------- builders

def b_define(sid, kb):
    for term, p1, p2 in kb["terms"]:
        add(sid, "define", "Define", "1-3", [{"label": "", "text": f"Define the term **{term}**.", "marks": 1, "lines": 2}],
            [row("", f"{cap(p1)} {p2}.", 1, notes="Award 1 mark for a precise definition. Do not award the mark for an example alone.", ao="AO1")],
            f"{tk(sid)}-define1", ["AO1"])
        add(sid, "define", "What is meant by", "1-3", [{"label": "", "text": f"What is meant by the term **{term}**?", "marks": 2, "lines": 4}],
            [row("", f"{cap(p1)} (1) {p2} (1).", 2, notes="Award 1 mark for the key idea of the definition and 1 mark for a valid developing point, which may be a relevant example such as the one shown. An example given without the key idea gains a maximum of 1 mark.", ao="AO1")],
            f"{tk(sid)}-define2", ["AO1"])


# Terms whose definitions overlap: none of them may be used as a distractor for another in the same group,
# otherwise a "wrong" option is also a correct description (e.g. effective demand for demand).
DEF_CLUSTERS = [
    {"demand", "effective demand"},
    {"scarcity", "the economic problem"},
    {"equilibrium price", "market equilibrium"},
    {"externality", "negative externality", "positive externality"}, {"negative externality", "external cost"},
    {"social cost", "external cost"},
    {"productivity", "labour productivity"},
    {"division of labour", "specialisation"},
    {"external growth", "merger"},
    {"economies of scale", "internal economies of scale"},
    {"monopoly", "price maker"}, {"competitive market", "price taker"},
    {"trade union", "collective bargaining", "industrial action"},
    {"regulation", "competition policy"},
    {"economic growth", "real GDP", "gross domestic product (GDP)"}, {"GDP per capita", "standard of living"},
    {"unemployment", "unemployment rate"},
    {"inflation", "consumer price index (CPI)"},
    {"current account deficit", "imports"},
    {"free trade", "international trade"}, {"specialisation (between countries)", "comparative advantage", "absolute advantage"},
    {"subsidy", "a subsidy"}, {"monetary policy", "interest rate"},
]


def overlaps(t1, t2):
    return any(t1 in g and t2 in g for g in DEF_CLUSTERS)


def b_mcq(sid, kb):
    k = tk(sid)
    terms = kb.get("terms", [])
    # definition items
    if len(terms) >= 4:
        for i, (term, p1, p2) in enumerate(terms):
            others = [t for j, t in enumerate(terms) if j != i and not overlaps(term, t[0])]
            if len(others) < 3:
                continue
            pick = R.sample(others, 3)
            parts, rows, vals = mcq_parts(f"Which one of the following best describes **{term}**?", cap(f"{p1} {p2}"),
                                          [cap(f"{o[1]} {o[2]}") for o in pick], R, reasons=[f"that is the meaning of {o[0]}" for o in pick])
            add(sid, "mcq", "Which one", "1-3", parts, rows, f"{k}-mcq-def", ["AO1"], answer={"method": "key", "values": vals, "checked": True})
    # authored
    for stem, correct, ds, reasons in kb.get("mcq", []):
        parts, rows, vals = mcq_parts(stem, correct, ds, R, reasons=reasons, ao="AO1")
        add(sid, "mcq", "Which one", "1-3" if reasons is None else "4-6", parts, rows, f"{k}-mcq-auth", ["AO1", "AO2"],
            answer={"method": "key", "values": vals, "checked": True})
    # classification items
    for cl in kb.get("classes", []):
        cats = cl["cats"]
        if len(cats) < 2 or "{cat}" not in cl["mcq"]:
            continue
        for cat, exs in cats.items():
            others = [(oc, e) for oc, es in cats.items() if oc != cat for e in es]
            if len(others) < 3:
                continue
            for ex in exs:
                pick = R.sample(others, 3)
                stem = cl["mcq"].replace("{cat}", cat)
                parts, rows, vals = mcq_parts(stem, ex, [p[1] for p in pick], R,
                                              reasons=[f"this is linked to {p[0]} rather than {cat}" for p in pick], ao="AO2")
                add(sid, "mcq", "Which one", "4-6", parts, rows, f"{k}-mcq-class", ["AO1", "AO2"], answer={"method": "key", "values": vals, "checked": True})


ITEM_SUBS = [("Demand for which one of the following", "Demand for the item below"), ("The supply of which one of the following", "The supply of the item below"),
             ("For a country, which one of the following", "For a country, the item below"), ("Which one of the following occupations", "The occupation below"),
             ("Which one of the following business activities", "The business activity below"), ("Which one of the following", "The item below")]


def b_state(sid, kb):
    k = tk(sid)
    for q, answers, ctx in kb.get("state", []):
        for i in range(3):
            c = new_ctx(R)
            lead = fill(ctx or lead_for(sid), c, R) if i > 0 else None
            text = q if not lead else f"{lead}\n\n{q}"
            add(sid, "state", "State", "1-3", [{"label": "", "text": fill(text, c, R), "marks": 1, "lines": 2}],
                [row("", "Award 1 mark for any one of: " + "; ".join(answers) + ".", 1, notes="Accept any other appropriate response.", ao="AO1")],
                f"{k}-state", ["AO1"])
    for cl in kb.get("classes", []):
        cats = cl["cats"]
        if cl.get("state"):
            for cat, exs in cats.items():
                stext = re.sub(r"\bone (?:a|an) ", "one ", cl["state"].replace("{cat}", cat))   # "State one a benefit" -> "State one benefit"
                add(sid, "state", "State", "1-3", [{"label": "", "text": stext, "marks": 1, "lines": 2}],
                    [row("", "Award 1 mark for any one of: " + "; ".join(e[0].lower() + e[1:] for e in exs) + ".", 1, notes="Accept any other appropriate example.", ao="AO1")],
                    f"{k}-state-class", ["AO1"])
        if len(cats) >= 2 and "{cat}" in cl["mcq"]:
            stem = cl["mcq"]
            for a, b in ITEM_SUBS:
                if a in stem:
                    stem = stem.replace(a, b)
                    break
            stem = stem.replace("{cat}", "...").rstrip("?").rstrip()
            opts = list(cats)
            for cat, exs in cats.items():
                for ex in exs:
                    text = (f"Item: *{ex}*\n\nComplete the statement below by stating which one of the following fills the gap: "
                            + "; ".join(opts) + f".\n\n{stem}")
                    add(sid, "state", "Identify", "1-3", [{"label": "", "text": text, "marks": 1, "lines": 1}],
                        [row("", cap(cat), 1, ao="AO1")], f"{k}-state-id", ["AO1"])


def lead_for(sid):
    t = SUBS[sid]["topic"]
    if t in ("market-system", "business"):
        return R.choice(["{firm} is a business based in {city}.", "{name} is studying how businesses in {city} make decisions.",
                         "{name} runs a small business in {city}."])
    return R.choice(["The government of {nation} is reviewing its economic policies.", "{nation} is a middle-income country with a growing population.",
                     "Economists are studying recent changes in the economy of {nation}."])


def b_describe(sid, kb):
    k = tk(sid)
    for q, pts, ctx in kb.get("describe", []):
        for i in range(3):
            c = new_ctx(R)
            if i == 0:
                text = q
            else:
                text = f"{fill(ctx if ctx else lead_for(sid), c, R)}\n\n{q}"
            add(sid, "describe", "Describe", "4-6", [{"label": "", "text": fill(text, c, R), "marks": 2, "lines": 4}],
                [row("", "Award 1 mark for a relevant point and 1 mark for a linked development, for example:\n" + "\n".join("- " + fill(p, c, R) for p in pts), 2,
                     notes="Only one point should be credited. A second, undeveloped point does not gain the development mark.", ao="AO1")],
                f"{k}-describe", ["AO1"])


def b_explain(sid, kb):
    k = tk(sid)
    items = kb.get("explain", [])
    if not items:
        return
    per = math.ceil(TARGET / len(items)) + 1
    for ctx_t, q_t, ex in items:
        def one(c):
            ctx = fill(ctx_t, c, R)
            q = fill(q_t, c, R)
            exs = [fill(e, c, R) for e in ex]
            return add(sid, "explain", "Explain", "4-6", [{"label": "", "text": f"{ctx}\n\n{q}", "marks": 3, "lines": 6}],
                       [row("", "Award 1 mark for identifying a relevant point, 1 mark for developing it and 1 mark for applying it to the context.\n\nExample:\n"
                            + "\n".join("- " + e for e in exs), 3, notes="Accept any other valid explanation. Answers with no reference to the context cannot gain the third mark.", ao="AO2")],
                       f"{k}-explain", ["AO2"])
        fills(per, one)


def issue_texts(iss, c):
    ctx = fill(iss["ctx"], c, R)
    a = fill(iss["a"], c, R)
    j = fill(iss["j"], c, R)
    pro = [fill(p, c, R) for p in iss["pro"]]
    con = [fill(p, c, R) for p in iss["con"]]
    return ctx, a, j, pro, con


def directed(iss, c, pro, con):
    """Content matched to each prompt: (analyse points, judge AO2/AO3 points, judge AO4 points)."""
    ap = [fill(p, c, R) for p in iss["a_points"]] if iss.get("a_points") else pro
    jp = [fill(p, c, R) for p in iss["j_pro"]] if iss.get("j_pro") else pro
    jc = [fill(p, c, R) for p in iss["j_con"]] if iss.get("j_con") else con
    return ap, jp, jc


def ext_key(sid):
    return subkey(sid) + ("-pol" if SUFFIX == "-pol" else "")


def b_levels(sid, kb, qtype):
    k = tk(sid)
    issues = kb.get("issues", [])
    if not issues:
        return
    per = math.ceil(TARGET / len(issues)) + 1
    for n, iss in enumerate(issues):
        def one(c):
            ctx, a, j, pro, con = issue_texts(iss, c)
            ap, jp, jc = directed(iss, c, pro, con)
            pro, con = (ap, con) if qtype == "analyse" else (jp, jc)
            figs = None
            if qtype in ("assess", "evaluate"):
                more, tbl = extend(ext_key(sid), n, ctx, c, qtype)
                ctx = "\n\n".join([ctx] + more)
                figs = [tbl] if tbl else None
            if qtype == "analyse":
                text, grid, aos, cw, diff, split, gen = f"With reference to the information above, analyse {a}.", GRID6, ["AO2", "AO3"], "Analyse", R.choice(["4-6", "7-9"]), "AO2 3 marks, AO3 3 marks", GENERAL6
                ind = ["AO2/AO3: " + p for p in pro]
            elif qtype == "assess":
                data = "the data above"
                text, grid, aos, cw, diff, split, gen = f"With reference to {data} and your knowledge of economics, assess {j}.", GRID9, ["AO2", "AO3", "AO4"], "Assess", "7-9", "AO2 3 marks, AO3 3 marks, AO4 3 marks", GENERAL9
                ind = ["AO2/AO3 (arguments for): " + p for p in pro] + ["AO4 (arguments against / counter-arguments): " + p for p in con]
            else:
                data = "the data above"
                text, grid, aos, cw, diff, split, gen = f"With reference to {data} and your knowledge of economics, evaluate {j}.", GRID12, ["AO2", "AO3", "AO4"], "Evaluate", "7-9", "AO2 4 marks, AO3 4 marks, AO4 4 marks", GENERAL12
                ind = ["AO2/AO3: " + p for p in pro] + ["AO4: " + p for p in con] + ["AO4: A supported judgement, for example stating what the outcome depends on or which argument is stronger and why."]
            marks = {"analyse": 6, "assess": 9, "evaluate": 12}[qtype]
            return add(sid, qtype, cw, diff, [{"label": "", "text": text, "marks": marks, "lines": {"analyse": 14, "assess": 22, "evaluate": 30}[qtype]}], [], f"{k}-{qtype}-{n + 1}", aos,
                       levels_=[levels("", grid, ind, ao_split=split, credit_note=CREDIT)], intro=ctx, general=gen, figures=figs)
        fills(per, one)


def calc_rows(res, part=""):
    return [row(part, f"Working: {res['working']}", 1, notes="Award 1 mark for a correct method shown. No mark for writing a formula without using the data.", ao="AO2"),
            row(part, f"Answer: {res['answer']}", 1, notes="Award 2 marks for the correct answer, with or without working. Units or currency must be given where relevant.", ao="AO2")]


def b_calc(sid, kb):
    k = tk(sid)
    gen = GEN[subkey(sid)]

    def one(c):
        res = gen(R, c)
        figs = [res["table"]] if res.get("table") else None
        return add(sid, "calculate", "Calculate", res.get("diff", "4-6"), [{"label": "", "text": res["text"], "marks": 2, "space": "working", "lines": 4}],
                   calc_rows(res), f"{k}-calc", ["AO2"], figures=figs,
                   answer={"method": "exact rational arithmetic (fractions)", "values": res["values"], "checked": True})
    fills(TARGET + 4, one)


def b_diagram(sid, kb):
    k = tk(sid)
    fn = DIAG[k]

    def one(c):
        d = fn(R, c)
        rows = [row("", ans, 1, notes=nt, ao="AO2") for ans, nt in d["rows"]]
        return add(sid, "diagram", "Draw" if "draw" in d["text"].lower() else "Label", d["diff"],
                   [{"label": "", "text": d["text"], "marks": 3, "space": "none", "lines": 0}], rows, f"{k}-diagram", ["AO2"],
                   figures=[{"type": "svg", "svg": d["svg"], "width": 85, "caption": "Figure 1"}])
    fills(TARGET + 4, one)


def b_data(sid, kb):
    k = tk(sid)
    issues = kb.get("issues", [])
    per = math.ceil((TARGET + 2) / len(issues))
    for ia, iss in enumerate(issues):
        same = fill(iss["a"], {}, R) == fill(iss["j"], {}, R) or iss["a"] == iss["j"]
        ib = (ia + 1) % len(issues) if same else ia

        def one(c):
            ca = dict(c)
            ctxA, a, j, proA, conA = issue_texts(iss, ca)
            apA, proA, conA = directed(iss, ca, proA, conA)
            moreA, tblA = extend(ext_key(sid), ia, ctxA, ca, "data-A")
            ctxA_long = "\n\n".join([ctxA] + moreA)
            figs = [{"type": "source", "label": "Extract A", "text": ctxA_long, "inline": True, "provenance": "Original fictional extract written for this question bank."}]
            proB, conB, ref = proA, conA, "Extract A"
            if ib != ia:
                cb = dict(c)
                ctxB, _, j, proB, conB = issue_texts(issues[ib], cb)
                _, proB, conB = directed(issues[ib], cb, proB, conB)
                moreB, _tB = extend(ext_key(sid), ib, ctxB, cb, "data-B")
                ctxB = "\n\n".join([ctxB] + moreB)
                figs.append({"type": "source", "label": "Extract B", "text": ctxB, "inline": True, "provenance": "Original fictional extract written for this question bank."})
                ref = "Extract B"
            res = DGEN[k][ia](R, dict(ca)) if k in DGEN else GEN[k](R, dict(ca))   # part (a) built from Extract A's own figures
            if res.get("table"):
                figs.append(res["table"])
            if tblA:
                fno = "Figure 2" if res.get("table") else "Figure 1"
                tblA = dict(tblA, caption=tblA["caption"].replace("Figure 1", fno, 1))
                figs.append(tblA)
            nfig = sum(1 for f in figs if f.get("type") == "table")
            other = " and Figure 1" if nfig == 1 else " and Figures 1 and 2" if nfig == 2 else ""
            parts = [{"label": "a", "text": res["text"], "marks": 2, "space": "working", "lines": 4},
                     {"label": "b", "text": f"With reference to Extract A, analyse {a}.", "marks": 6, "lines": 14},
                     {"label": "c", "text": f"With reference to {ref}{other} and your knowledge of economics, evaluate {j}.", "marks": 12, "lines": 30}]
            lv = [levels("b", GRID6, ["AO2/AO3: " + p for p in apA], ao_split="AO2 3 marks, AO3 3 marks", credit_note=CREDIT),
                  levels("c", GRID12, ["AO2/AO3: " + p for p in proB] + ["AO4: " + p for p in conB]
                         + ["AO4: A supported judgement, for example stating what the outcome depends on or which argument is stronger and why."],
                         ao_split="AO2 4 marks, AO3 4 marks, AO4 4 marks", credit_note=CREDIT)]
            return add(sid, "data-response", "Evaluate", "7-9", parts, calc_rows(res, "a"), f"{k}-data", ["AO2", "AO3", "AO4"], levels_=lv,
                       figures=figs, answer={"method": "exact rational arithmetic (fractions)", "values": res["values"], "checked": True},
                       general="(a) is point marked. (b) and (c) are levels marked on a best-fit basis. " + GENERAL12,
                       key_text=norm(ctxA, res["text"], a, j))
        fills(per, one)


BUILD = {"mcq": b_mcq, "state": b_state, "define": b_define, "describe": b_describe, "calculate": b_calc, "diagram": b_diagram,
         "explain": b_explain, "analyse": lambda s, kb: b_levels(s, kb, "analyse"), "assess": lambda s, kb: b_levels(s, kb, "assess"),
         "evaluate": lambda s, kb: b_levels(s, kb, "evaluate"), "data-response": b_data}


def main():
    SP.build_spec()
    for sid, s in SUBS.items():
        kb = KB[subkey(sid)]
        for qt in s["qtypes"]:
            BUILD[qt](sid, kb)
    replace_price_controls()
    B.save()


PRICE_CONTROL = re.compile(r"maximum price|minimum price|maximum rent|price ceiling|price floor|Pmax|Pmin|legal cap|legal floor|"
                           r"floor price|guaranteed price|ceiling on|cap on rents|limit on the price", re.I)


def replace_price_controls():
    """Maximum/minimum prices are outside the 4EC1 content (only the minimum wage is). Drop those
    intervention items and add spec-based policy items (1.2.6(a)-(b)) built with a separate RNG, so
    every other question keeps its id and content."""
    global R, SUFFIX
    import json
    sid = "economics.market-system.intervention"
    for t, qs in B.by_topic.items():
        B.by_topic[t] = [q for q in qs if not (q["subtopic"] == sid and PRICE_CONTROL.search(json.dumps(q, ensure_ascii=False)))]
    R, SUFFIX = random.Random(41206), "-pol"
    kb = economics_kbint.KB
    for qt in ("define", "mcq", "explain", "diagram", "analyse", "assess", "evaluate"):
        BUILD[qt](sid, kb)
    SUFFIX = ""


if __name__ == "__main__":
    main()
