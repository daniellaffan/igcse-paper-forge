#!/usr/bin/env python3
"""Generator for Pearson Edexcel International GCSE English Literature 4ET1, Paper 1.

  .venv/bin/python scripts/gen/english-literature.py

Writes data/spec/english-literature.json and data/bank/english-literature/*.json.
Deterministic (seeded). Content modules:
  english_literature_unseen_orig.py  original unseen poems (Section A)
  english_literature_unseen_pd.py    public-domain unseen poems (Section A)
  english_literature_anthology.py    anthology poem notes (Section B; poems never printed)
  english_literature_prose.py        Of Mice and Men notes (Section C; novel never quoted)
  english_literature_spec.py         spec tree
"""
import itertools
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import Bank, levels, rng, SPEC  # noqa: E402
from english_literature_unseen_orig import ORIGINAL_POEMS, PROV  # noqa: E402
from english_literature_unseen_pd import PD_POEMS  # noqa: E402
from english_literature_anthology import POEMS, THEMES  # noqa: E402
from english_literature_prose import ENTITIES  # noqa: E402
from english_literature_spec import build_spec  # noqa: E402

SUBJ = "english-literature"
R = rng(4041)
BUL = "\u2022\u00a0"

# --------------------------------------------------------------- level grids (paraphrased)
GRID_A = [
    ("0", "0", "No rewardable material."),
    ("Level 1", "1-4", "A simple response that identifies very little of the writer's use of language, form and structure. Little relevant evidence is used in support."),
    ("Level 2", "5-8", "A largely descriptive response with some comment on the writer's language, form and structure. Some relevant examples are used in support."),
    ("Level 3", "9-12", "Shows understanding of a range of the writer's choices of language, form and structure and links them to their effect on the reader. Examples are clearly relevant."),
    ("Level 4", "13-16", "A focused, detailed response that sustains analysis of the writer's language, form and structure and their effect on the reader. Examples are fully relevant."),
    ("Level 5", "17-20", "A cohesive evaluation of how the writer's language, form and structure work together and affect the reader. Examples are chosen with discrimination."),
]
GRID_B = [
    ("0", "0", "No rewardable material."),
    ("Level 1", "1-6", "A simple response with minimal identification of language, form and structure. Little or no comparison of the two poems. Little relevant evidence."),
    ("Level 2", "7-12", "A largely descriptive response with some comment on language, form and structure. Some undeveloped comparison, noting obvious similarities and/or differences. Some relevant examples. NB: an answer that considers only ONE poem cannot go above the top of Level 2."),
    ("Level 3", "13-18", "Shows understanding of a range of language, form and structure, linked to effects on the reader. Compares and contrasts a range of points, considering some similarities and/or differences. Clearly relevant examples."),
    ("Level 4", "19-24", "Focused and detailed, with sustained analysis of language, form and structure and their effects. Compares and contrasts effectively, across a wide range of similarities and/or differences. Fully relevant examples."),
    ("Level 5", "25-30", "A cohesive evaluation of how language, form and structure work together to affect the reader. Perceptive comparison covering a varied and comprehensive range of similarities and/or differences. Discriminating use of examples."),
]
GRID_C = [
    ("0", "0", "No rewardable material."),
    ("Level 1", "1-8", "Limited knowledge and understanding of the text. A simple response with little personal engagement or critical style. Little comment on the relationship between text and context. Limited use of relevant examples."),
    ("Level 2", "9-16", "Some knowledge and understanding of the text. Largely narrative, with some personal engagement or critical style. Some comment on the relationship between text and context. Some relevant examples."),
    ("Level 3", "17-24", "Sound knowledge and understanding of the text. Relevant personal engagement and an appropriate critical style. Relevant comment on the relationship between text and context. Clearly relevant examples."),
    ("Level 4", "25-32", "Thorough knowledge and understanding of the text. Thorough personal engagement and a sustained critical style. Detailed awareness of the relationship between text and context. Fully relevant examples."),
    ("Level 5", "33-40", "Assured knowledge and understanding of the text. Assured personal engagement and a perceptive critical style. Understanding of the relationship between text and context is convincingly integrated into the response. Discriminating use of examples."),
]

GEN_A = ("Mark with the levels grid using a best-fit approach, then use the indicative content as a guide to what candidates may say. "
         "Reward points that are firmly grounded in the poem and show some personal response. Summary, paraphrase or a list of "
         "techniques without comment on effect should not be highly rewarded.")
GEN_B = ("Mark with the levels grid using a best-fit approach. AO2 and AO3 are equally weighted. Reward comparison that is developed "
         "and supported by close reference to both poems; the comparison may be integrated throughout or organised poem by poem with "
         "explicit links. Summary or feature-spotting without comment on effect should not be highly rewarded.")
GEN_C = ("Mark with the levels grid using a best-fit approach. AO1 and AO4 are equally weighted. Reward knowledge of the whole novel, "
         "a clear line of argument that answers the question, and context that is woven into the discussion rather than added on. "
         "Retelling the story without argument should not be highly rewarded. This is a closed-book paper, so close reference to "
         "events may be as effective as quotation.")
CREDIT = "These points are suggestions only. Credit any other valid responses that are supported by the text."


def italic_omam(s):
    return s.replace("Of Mice and Men", "*Of Mice and Men*")


# --------------------------------------------------------------- Section A
def poem_text(p):
    t = p["text"]
    if p.get("gloss"):
        t += "\n\n" + "\n".join("*" + g for g in p["gloss"])
    return t


def gen_unseen(bank):
    poems = [dict(p, author=None, pd=False) for p in ORIGINAL_POEMS] + [dict(p, pd=True) for p in PD_POEMS]
    for p in poems:
        if p["pd"]:
            prov = (f"{p['title']} by {p['author']} ({p['life']}), {p['date']}. Public domain: the poet died more than "
                    f"70 years ago and the poem was published before 1929.")
            byline = f"{p['author']} ({p['date']})"
        else:
            prov = PROV
            byline = "Original poem written for this practice bank"
        for sub, focus, diff, fpoint in p["focuses"]:
            text = (f"Explore how the writer presents {focus} in this poem.\n\n"
                    f"In your answer, you should consider the writer's:\n{BUL}descriptive skills\n{BUL}choice of language\n"
                    f"{BUL}use of form and structure.\n\nSupport your answer with examples from the poem.")
            ind = [f"**Focus:** {fpoint[0].upper() + fpoint[1:]}."]
            ind += [f"**Descriptive skills:** {x}" for x in p["desc"]]
            ind += [f"**Language choices:** {x}" for x in p["lang"]]
            ind += [f"**Form and structure:** {x}" for x in p["form"]]
            bank.add(
                topic="unseen", subtopic=f"unseen.{sub}", qtype="unseen-poem", command_word="Explore",
                difficulty=diff, paper=["p1"], section="A", ao=["AO2"],
                spec_refs=[next(r for s, r in SUB_REFS if s == f"unseen.{sub}")],
                template=f"unseen-{p['id']}", minutes=35,
                intro="Read the following poem.",
                figures=[{"type": "poem", "title": p["title"], "text": poem_text(p) + f"\n\n*{byline}*",
                          "numbered": True, "provenance": prov}],
                parts=[{"label": "", "text": text, "marks": 20, "space": "lines", "lines": 45}],
                markscheme={"style": "levels", "rows": [], "general": GEN_A,
                            "levels": [levels("", GRID_A, ind, title="AO2 Analyse the language, form and structure used by a writer to create meanings and effects (20 marks)",
                                              ao_split="AO2 20", credit_note=CREDIT)]},
                provenance=prov, tags=["public-domain" if p["pd"] else "original-poem"],
            )


# --------------------------------------------------------------- Section B
PAIR_STEMS = ["Compare how the poets present {f} in these two poems.",
              "Compare the ways in which the two poets present {f}.",
              "Compare how {f} is explored by the poets in these two poems."]
OPEN_STEMS = ["Compare how the poets present {f} in {a} and in one other poem of your choice from the collection.",
              "Choose one other poem from the collection. Compare the ways in which {f} is presented in {a} and in your chosen poem.",
              "Compare how {f} is explored in {a} and in one other poem of your choice from the collection."]
TAIL_B = "\n\nIn your answer, you should refer to each poet's use of language, form and structure.\n\nSupport your answer with examples from both poems."


def ao3_points(a, b, focus, th):
    A, B = POEMS[a], POEMS[b]
    sa, sb = th["poems"][a][0], th["poems"][b][0]
    return [
        f"**AO3:** Both poems are concerned with {focus}, but *{A['title']}* {sa}, whereas *{B['title']}* {sb}.",
        f"**AO3:** *{A['title']}* is {A['form']}, while *{B['title']}* is {B['form']}; candidates may compare how each form shapes the presentation of {focus}.",
        f"**AO3:** The voice of *{A['title']}* is {A['voice']}; in *{B['title']}* it is {B['voice']}, which changes how directly the reader is involved.",
        f"**AO3:** The tone of *{A['title']}* is {A['tone']}, compared with the {B['tone']} tone of *{B['title']}*.",
        f"**AO3:** Endings could be contrasted: *{A['title']}* closes with {A['ending']}, whereas *{B['title']}* closes with {B['ending']}.",
    ]


def ao2_points(p, th):
    T = POEMS[p]["title"]
    return [f"**AO2 – *{T}*:** {n}" for n in th["poems"][p][1]]


def diff_b(i, a, b=None):
    old = {"s116", "belle", "tyger", "duchess", "remember", "if"}
    score = (i % 3) + (1 if a in old else 0) + (1 if b in old else 0)
    return "1-3" if score <= 0 else ("4-6" if score <= 2 else "7-9")


def bank_b(bank, sid, th, qtype, text, ind, refs, diff, tmpl):
    bank.add(topic="anthology", subtopic=sid, qtype=qtype, command_word="Compare", difficulty=diff,
             paper=["p1"], section="B", ao=["AO2", "AO3"], spec_refs=refs, template=tmpl, minutes=40,
             parts=[{"label": "", "text": text, "marks": 30, "space": "lines", "lines": 55}],
             markscheme={"style": "levels", "rows": [], "general": GEN_B,
                         "levels": [levels("", GRID_B, ind,
                                           title="AO2 Analyse the language, form and structure used by a writer to create meanings and effects (15 marks); AO3 Explore links and connections between texts (15 marks)",
                                           ao_split="AO2 15, AO3 15", credit_note=CREDIT)]},
             tags=["anthology"])


def gen_anthology(bank, target=16):
    for ti, (sid, th) in enumerate(THEMES.items()):
        sref = next(r for s, r in SUB_REFS if s == sid)
        poems = list(th["poems"])
        pairs = list(itertools.combinations(poems, 2))
        R.shuffle(pairs)
        foc = th["focuses"]
        made, i = set(), 0
        while len([k for k in made if k[0] == "pair"]) < target:
            a, b = pairs[i % len(pairs)]
            f = foc[(i // len(pairs) + i) % len(foc)]
            key = ("pair", a, b, f)
            i += 1
            if key in made:
                continue
            made.add(key)
            A, B = POEMS[a]["title"], POEMS[b]["title"]
            stem = PAIR_STEMS[i % len(PAIR_STEMS)].format(f=f, a=A, b=B)
            text = f"Look again at {A} and {B} in the collection.\n\n{stem}{TAIL_B}"
            ind = ao2_points(a, th) + ao2_points(b, th) + ao3_points(a, b, f, th)
            bank_b(bank, sid, th, "anthology-pair", text, ind, [sref, POEMS[a]["ref"], POEMS[b]["ref"]],
                   diff_b(i, a, b), f"anth-pair-{sid.split('.')[1]}")
        j = 0
        n_open = 0
        while n_open < target:
            a = poems[j % len(poems)]
            f = foc[(j // len(poems) + ti + j) % len(foc)]
            j += 1
            key = ("open", a, f)
            if key in made:
                continue
            made.add(key)
            n_open += 1
            A = POEMS[a]["title"]
            others = [p for p in poems if p != a]
            R.shuffle(others)
            sugg = others[:3]
            stem = OPEN_STEMS[j % len(OPEN_STEMS)].format(f=f, a=A)
            text = f"Look again at {A} in the collection.\n\n{stem}{TAIL_B}"
            ind = ao2_points(a, th)
            ind.append("**Second poem:** candidates may choose any poem from the anthology that allows a valid comparison. Suitable choices might include "
                       + ", ".join(f"*{POEMS[p]['title']}* (which {th['poems'][p][0]})" for p in sugg) + ".")
            for p in sugg[:2]:
                ind.append(f"**AO2 – *{POEMS[p]['title']}* (if chosen):** {th['poems'][p][1][0]}")
            ind += ao3_points(a, sugg[0], f, th)[:4]
            ind.append("**AO3:** Whichever poem is chosen, the best answers keep both poems in view throughout and explain how the writers' methods create different effects.")
            bank_b(bank, sid, th, "anthology-open", text, ind, [sref, POEMS[a]["ref"]], diff_b(j, a),
                   f"anth-open-{sid.split('.')[1]}")


# --------------------------------------------------------------- Section C
def gen_prose(bank):
    for e in ENTITIES:
        sref = next(r for s, r in SUB_REFS if s == e["sub"])
        for k, st in enumerate(e["stems"]):
            stem, diff = st[0], st[1]
            ao1 = st[2] if len(st) > 2 else e["ao1"]  # per-stem points (e.g. one specific setting)
            text = italic_omam(stem) + "\n\nYou must consider the context of the novel in your answer."
            ind = []
            if "How far do you agree" in stem:
                ind.append("**Approach:** candidates may agree, disagree or argue a balanced case; any judgement is acceptable if it is supported by close reference to the novel.")
            elif stem.startswith("Which one character") or "one character" in stem or "one minor character" in stem:
                ind.append("**Approach:** any character may be chosen; credit the quality of the justification rather than the choice itself.")
            ind += [f"**AO1:** {x}" for x in ao1]
            ind += [f"**AO4:** {x}" for x in e["ao4"]]
            cw = stem.split()[0].strip("'\u2018")
            if stem.startswith("'"):
                cw = "How far"
            elif cw == "In":
                cw = "In what ways"
            elif cw == "Which":
                cw = "Which one"
            bank.add(topic="prose", subtopic=e["sub"], qtype=e["qtype"], command_word=cw, difficulty=diff,
                     paper=["p1"], section="C", ao=["AO1", "AO4"], spec_refs=[sref],
                     template=f"omam-{e['sub'].split('.')[1]}", minutes=45,
                     intro="*Of Mice and Men*, John Steinbeck",
                     parts=[{"label": "", "text": text, "marks": 40, "space": "lines", "lines": 65}],
                     markscheme={"style": "levels", "rows": [], "general": GEN_C,
                                 "levels": [levels("", GRID_C, ind,
                                                   title="AO1 Demonstrate a close knowledge and understanding of texts, maintaining a critical style and presenting an informed personal engagement (20 marks); AO4 Show understanding of the relationships between texts and the contexts in which they were written (20 marks)",
                                                   ao_split="AO1 20, AO4 20", credit_note=CREDIT)]},
                     tags=["of-mice-and-men"])


def main():
    spec = build_spec()
    (SPEC / f"{SUBJ}.json").write_text(json.dumps(spec, ensure_ascii=False, indent=1))
    global SUB_REFS
    SUB_REFS = [(st["id"], st["ref"]) for t in spec["topics"] for st in t["subtopics"]]
    bank = Bank(SUBJ)
    gen_unseen(bank)
    gen_anthology(bank)
    gen_prose(bank)
    bank.save()


SUB_REFS = []

if __name__ == "__main__":
    main()
