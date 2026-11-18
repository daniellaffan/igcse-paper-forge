#!/usr/bin/env python3
"""Generator for Pearson Edexcel International GCSE English Language A (4EA1), Paper 1 only.

  .venv/bin/python scripts/gen/english-language.py

Writes data/spec/english-language.json and data/bank/english-language/<topic>.json.
Deterministic: no randomness except a seeded RNG for pairing writing tasks.

Content modules (all original or referenced by title only):
  english_language_texts*.py   unseen Text One passages + Q1/Q2/Q3/Q5 marking content
  english_language_anthology.py anthology Part 1 texts (title/author only) + Q4 indicative content
  english_language_writing.py  Section B transactional tasks
"""
import re
import sys
import textwrap
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import Bank, row, levels, rng  # noqa: E402
import english_language_spec as specmod  # noqa: E402
from english_language_anthology import BY_ID as ANTH, full_title, ref_title  # noqa: E402
from english_language_writing import writing_tasks  # noqa: E402

PASSAGES = []
for mod in ("english_language_texts1", "english_language_texts2", "english_language_texts3", "english_language_texts4"):
    try:
        PASSAGES += __import__(mod).PASSAGES
    except ModuleNotFoundError:
        pass

WRAP = 84
FIG_SP, EM_SP = " ", " "
PROV_T1 = "Original text written for this practice paper; the writer and events are fictional."
MARKING_NOTE = ("Do not credit material taken from outside the lines given. Reward all valid points, "
                "including ones not listed here.")
SPAG = "Your answer will be assessed on how accurately and appropriately you use vocabulary, spelling, punctuation and grammar."

# ------------------------------------------------------------------ level grids (our own wording)
GRID_AO2 = [
    ("0", "0", "No rewardable material."),
    ("Level 1", "1-2", "Simple identification of a few language or structural features, with little understanding of how they create effects. Few references, or references that are not well chosen."),
    ("Level 2", "3-4", "Some understanding of language and structure, with some comment on effects, including word choice. References are valid but not developed."),
    ("Level 3", "5-7", "Clear explanation of how language and structure are used to create effects, including vocabulary and sentence structure. References are relevant and support the points made."),
    ("Level 4", "8-10", "Thorough exploration of how language and structure create effects, including vocabulary, sentence structure and other features. References are well chosen, detailed and fully support the points made."),
    ("Level 5", "11-12", "Perceptive, assured analysis of how language and structure work together to achieve effects, including vocabulary, sentence structure and other features. References are discriminating and sharpen the points made."),
]
GRID_AO3 = [
    ("0", "0", "No rewardable material."),
    ("Level 1", "1-4", "No real comparison. Describes the writers' ideas and perspectives, including theme, language and/or structure, in a basic way. References are few or not relevant."),
    ("Level 2", "5-8", "Makes obvious comparisons. Comments on the writers' ideas and perspectives, including theme, language and/or structure. References are valid but not developed. A response that discusses only ONE text cannot go above Level 2."),
    ("Level 3", "9-13", "Makes a range of comparisons. Explains the writers' ideas and perspectives, including theme, language and/or structure. References are relevant and support the points made."),
    ("Level 4", "14-18", "Makes a wide range of comparisons. Explores the writers' ideas and perspectives and how theme, language and/or structure are used across both texts. References are balanced between the texts and fully support the points."),
    ("Level 5", "19-22", "Makes varied, wide-ranging and sustained comparisons. Analyses the writers' ideas and perspectives and how theme, language and/or structure are used across both texts. References are balanced, discriminating and fully support the points."),
]
GRID_AO4 = [
    ("0", "0", "No rewardable material."),
    ("Level 1", "1-5", "Communication is basic and often unclear. Little awareness of the purpose of the task or of the reader. Little sense of the required form, tone or register."),
    ("Level 2", "6-11", "Communicates in a broadly suitable way. Some grasp of purpose and of what the reader needs. Form, tone and register are handled in a straightforward way."),
    ("Level 3", "12-17", "Communicates clearly. A clear sense of purpose and of what the reader expects. Form, tone and register are appropriate."),
    ("Level 4", "18-22", "Communicates successfully. Purpose and the reader's needs are securely met. Form, tone and register are used effectively."),
    ("Level 5", "23-27", "Communication is perceptive and subtle. The writing is sharply focused on purpose and on the reader. Form, tone and register are handled with sophistication."),
]
GRID_AO5 = [
    ("0", "0", "No rewardable material."),
    ("Level 1", "1-3", "Ideas are expressed with limited use of structural and grammatical features. Basic vocabulary, often misspelt. Basic control of punctuation; sentences are undeveloped and repetitive."),
    ("Level 2", "4-7", "Ideas are expressed and ordered, with paragraphs and a range of structural and grammatical features. Regular spelling patterns are mostly correct. Some control of punctuation; a range of sentence types including coordination and subordination."),
    ("Level 3", "8-11", "Ideas are developed and linked; paragraphing and grammatical features make meaning clear. Varied vocabulary; irregular spellings mostly correct. Accurate, varied punctuation; sentence structures adapted as needed."),
    ("Level 4", "12-15", "Ideas are managed cohesively, with structural and grammatical features used deliberately across the whole text. Wide, well-selected vocabulary with only occasional spelling errors. Punctuation placed for clarity; sentences controlled for deliberate effect."),
    ("Level 5", "16-18", "Complex ideas are handled with control, using a range of structural and grammatical features for coherence and cohesion. Extensive vocabulary used strategically; rare spelling slips do not affect meaning. Precise punctuation aids emphasis; a full range of sentence structures is used accurately and selectively for effect."),
]
BEST_FIT = ("Use a best-fit approach: decide which level descriptor matches the answer most closely, then place the mark "
            "within that level according to how securely each part of the descriptor is met. Indicative content shows "
            "points candidates are likely to make; it is not a checklist.")


# ------------------------------------------------------------------ passages
class Passage:
    def __init__(self, d):
        self.d = d
        self.lines = []          # (line_no, para_idx(1-based), text, start_offset_in_para)
        n = 0
        for pi, p in enumerate(d["paras"], 1):
            assert "*" not in p and "$" not in p, d["id"]
            off = 0
            for ln in textwrap.wrap(p, WRAP, break_on_hyphens=False, break_long_words=False):
                n += 1
                start = p.index(ln, off)
                self.lines.append((n, pi, ln, start))
                off = start + len(ln)
        self.nlines = n

    def text(self):
        out, cur = [], None
        for n, pi, ln, _ in self.lines:
            if cur is not None and pi != cur:
                out.append("")
            cur = pi
            num = str(n) if n % 5 == 0 else ""
            out.append(FIG_SP * (2 - len(num)) + num + EM_SP + ln)
        return "\n".join(out)

    def para_lines(self, a, b):
        ls = [n for n, pi, _, _ in self.lines if a <= pi <= b]
        return ls[0], ls[-1]

    def range_text(self, a, b):
        return " ".join(self.d["paras"][a - 1:b])

    def sentence_lines(self, sent):
        for pi, p in enumerate(self.d["paras"], 1):
            i = p.find(sent)
            if i >= 0:
                j = i + len(sent)
                ls = [n for n, q, ln, st in self.lines if q == pi and st < j and st + len(ln) > i]
                a, b = ls[0], ls[-1]
                if a == b:
                    b = a + 1 if a < self.nlines else a
                    if a == b:
                        a -= 1
                txt = " ".join(ln for n, q, ln, st in self.lines if a <= n <= b)
                return a, b, txt
        raise AssertionError(f"{self.d['id']}: sentence not found: {sent[:50]}")

    def figure(self):
        t = self.d
        return {"type": "passage", "title": f"Text One: {t['title']}", "text": self.text(), "numbered": False,
                "provenance": f"{t['intro']} ({PROV_T1})"}


def text_two_figure(a):
    return {"type": "passage", "title": f"Text Two: {full_title(a)}, {a['author']}",
            "text": "This anthology text is not reprinted in this practice paper. Use your own copy of the Anthology "
                    "(Part 1: non-fiction texts) when you answer the questions on Text Two.",
            "numbered": False, "provenance": "Copyright text from Part 1 of the Anthology: referred to by title and author only."}


QUOTE = re.compile("«([^»]+)»")


def check_quotes(points, src, pid):
    low = src.lower()
    for pt in points:
        for qt in QUOTE.findall(pt):
            assert qt.lower() in low, f"{pid}: quotation not in range: {qt}"
    return [QUOTE.sub(lambda m: "‘" + m.group(1) + "’", p) for p in points]


def bullets(items):
    return "\n".join("• " + i for i in items)


def strip_opt(a):
    return re.sub(r"\s+", " ", a.replace("(", "").replace(")", "")).strip()


# ------------------------------------------------------------------ question builders (return part + markscheme pieces)
def q1_parts(P, item, label=""):
    sent, focus, answers = item
    a, b, txt = P.sentence_lines(sent)
    for ans in answers:
        assert strip_opt(ans).lower() in txt.lower(), f"{P.d['id']}: Q1 answer outside lines: {ans}"
    part = {"label": label, "text": f"Look at lines {a}–{b}. Select **two** words or phrases from these lines that {focus}.",
            "marks": 2, "lines": 2}
    ms = row(label, "Accept any **two** of the following, 1 mark each, up to a maximum of 2 marks:\n" +
             bullets(f"‘{x}’" for x in answers), 2,
             notes=f"Answers must come from lines {a}–{b}. Words in brackets are not needed for the mark. "
                   "Candidates do not need to use their own words or explain their choices; do not credit "
                   "material from outside the given lines.", ao="AO1")
    return part, ms, (a, b)


def q2_parts(P, item, label=""):
    (pa, pb), task, points = item
    a, b = P.para_lines(pa, pb)
    part = {"label": label, "text": f"Look again at lines {a}–{b}.\n\nIn your own words, {task}.", "marks": 4, "lines": 9}
    ms = row(label, f"Accept any reasonable points in the candidate's own words, where possible, 1 mark per valid point, "
                    f"up to a maximum of 4 marks. For example:\n" + bullets(points), 4,
             notes=MARKING_NOTE + " Points should be expressed in the candidate's own words; do not credit long, "
                   "unselective copying. Comment on language (AO2) is not required.", ao="AO1")
    return part, ms, (pa, pb)


def q3_parts(P, item, label=""):
    (pa, pb), task, points = item
    a, b = P.para_lines(pa, pb)
    pts = check_quotes(points, P.range_text(pa, pb), P.d["id"])
    part = {"label": label, "text": f"From lines {a}–{b}, {task}.\n\nYou may support your points with brief quotations.",
            "marks": 5, "lines": 11}
    ms = row(label, "Accept any reasonable explanation, 1 mark per valid point, up to a maximum of 5 marks. For example:\n" +
             bullets(pts), 5,
             notes=MARKING_NOTE + " Quotations are optional; a quotation alone without an explanatory point is not "
                   "rewarded.", ao="AO1")
    return part, ms, (pa, pb)


def q4_parts(anth, focus, tags, label=""):
    pts = [t for g, t in anth["points"] if "e" in tags or set(g) & set(tags)]
    # relevant points first, then other features that also serve the focus
    for g, t in anth["points"]:
        if len(pts) >= 9:
            break
        if t not in pts:
            pts.append(t)
    part = {"label": label,
            "text": f"In Text Two, how does {anth['author']} use language and structure to {focus}?\n\n"
                    "Refer closely to the text in your answer and include brief quotations.",
            "marks": 12, "lines": 30}
    lv = levels(label, GRID_AO2,
                [f"Credit answers that analyse the writer's choices of language and structure and their effect, in relation to the "
                 f"task: to {focus}. Answers might cover some of these points:"] + pts,
                title="AO2: Understand and analyse how writers use linguistic and structural devices to achieve their effects (12 marks)",
                ao_split="AO2 12")
    return part, lv


def q5_parts(P, anth, label=""):
    focus, pts = P.d["q5"]
    part = {"label": label,
            "text": f"Compare how the writers present their ideas and perspectives about {focus}.\n\n"
                    "Support your answer with detailed examples from both texts, including brief quotations.",
            "marks": 22, "lines": 48}
    lv = levels(label, GRID_AO3,
                [f"Reward responses that compare how the writers of Text One ({P.d['writer']}) and Text Two "
                 f"({anth['author']}) present their ideas and perspectives about {focus}. Responses may include "
                 "some of the following points:"] + pts,
                title="AO3: Explore links and connections between writers' ideas and perspectives, as well as how these are conveyed (22 marks)",
                ao_split="AO3 22")
    return part, lv


def t1_intro(P):
    return f"The following question is based on Text One, *{P.d['title']}*, by {P.d['writer']}, in the Insert."


def build_reading(bank):
    for P in map(Passage, PASSAGES):
        d = P.d
        anth = ANTH[d["anth"]]
        hard = d.get("level", 1) >= 2
        base = dict(paper=["p1"], section="A", calculator=None)
        f1 = P.figure()
        for i, it in enumerate(d["q1"]):
            part, ms, _ = q1_parts(P, it)
            bank.add(topic="reading-retrieval", subtopic="el.ao1.select", qtype="select-two", command_word="select",
                     difficulty="1-3", parts=[part], markscheme={"style": "points", "rows": [ms]},
                     spec_refs=["C1.A.AO1.1", "C1.A.AO1.1a", "C1.A.AO1.1b"], ao=["AO1"], template="el-q1",
                     id=f"english-language.q1.{d['id']}.{i + 1}", intro=t1_intro(P), figures=[f1], minutes=2,
                     provenance=PROV_T1, **base)
        for i, it in enumerate(d["q2"]):
            part, ms, _ = q2_parts(P, it)
            cw = it[1].split()[0]
            bank.add(topic="reading-retrieval", subtopic="el.ao1.describe", qtype="own-words", command_word=cw,
                     difficulty="4-6" if hard else "1-3", parts=[part], markscheme={"style": "points", "rows": [ms]},
                     spec_refs=["C1.A.AO1.2", "C1.A.AO1.2a", "C1.A.AO1.2b"], ao=["AO1"], template="el-q2",
                     id=f"english-language.q2.{d['id']}.{i + 1}", intro=t1_intro(P), figures=[f1], minutes=5,
                     provenance=PROV_T1, **base)
        for i, it in enumerate(d["q3"]):
            part, ms, _ = q3_parts(P, it)
            bank.add(topic="reading-retrieval", subtopic="el.ao1.explain", qtype="explain-five", command_word="explain",
                     difficulty="4-6", parts=[part], markscheme={"style": "points", "rows": [ms]},
                     spec_refs=["C1.A.AO1.3", "C1.A.AO1.3a", "C1.A.AO1.3b"], ao=["AO1"], template="el-q3",
                     id=f"english-language.q3.{d['id']}.{i + 1}", intro=t1_intro(P), figures=[f1], minutes=6,
                     provenance=PROV_T1, **base)
        # Q5 comparison
        part, lv = q5_parts(P, anth)
        bank.add(topic="reading-comparison", subtopic="el.ao3.compare", qtype="compare", command_word="compare",
                 difficulty="7-9", parts=[part], markscheme={"style": "levels", "rows": [], "levels": [lv], "general": BEST_FIT},
                 spec_refs=["C1.A.AO3.1", "C1.A.AO3.1a", "C1.A.AO3.1b", "C1.A.AO3.1c", anth["ref"]], ao=["AO3"],
                 template="el-q5", id=f"english-language.q5.{d['id']}",
                 intro=f"This question is based on both Text One, *{d['title']}*, in the Insert, and Text Two, "
                       f"{ref_title(anth)}, from Part 1 of the Anthology.",
                 figures=[f1, text_two_figure(anth)], minutes=35, provenance=PROV_T1, **base)
        # complete Section A: choose non-overlapping Q2/Q3 combinations
        combos = []
        for i2, q2 in enumerate(d["q2"]):
            for i3, q3 in enumerate(d["q3"]):
                (a2, b2), (a3, b3) = q2[0], q3[0]
                if b2 < a3 or b3 < a2:
                    combos.append((0 if b2 < a3 else 1, i2, i3))
        combos.sort()
        assert combos, d["id"]
        nsec = min(3, max(2, len(combos)))
        for k in range(nsec):
            _, i2, i3 = combos[k % len(combos)]
            i1 = k % len(d["q1"])
            focus, tags = anth["focuses"][(k + len(bank.ids)) % len(anth["focuses"])]
            pa, ma, _ = q1_parts(P, d["q1"][i1], "a")
            pb, mb, _ = q2_parts(P, d["q2"][i2], "b")
            pc, mc, _ = q3_parts(P, d["q3"][i3], "c")
            pd, ld = q4_parts(anth, focus, tags, "d")
            pe, le = q5_parts(P, anth, "e")
            bank.add(topic="reading-section", subtopic="el.reading.section", qtype="reading-section",
                     command_word="compare", difficulty="7-9" if hard else "4-6", parts=[pa, pb, pc, pd, pe],
                     markscheme={"style": "mixed", "rows": [ma, mb, mc], "levels": [ld, le], "general": BEST_FIT},
                     spec_refs=["C1.A.1", "C1.A.1a", "C1.A.AO1.1", "C1.A.AO1.2", "C1.A.AO1.3", "C1.A.AO2.1",
                                anth["ref"], "C1.A.AO3.1"],
                     ao=["AO1", "AO2", "AO3"], template="el-secA", id=f"english-language.secA.{d['id']}.{k + 1}",
                     intro=(f"Parts (a) to (c) are based on Text One, *{d['title']}*, by {d['writer']}, in the Insert. "
                            f"Part (d) is based on Text Two, {ref_title(anth)}, from Part 1 of the Anthology "
                            f"(use your own copy). Part (e) is based on both texts."),
                     figures=[f1, text_two_figure(anth)], minutes=90, provenance=PROV_T1, **base)


def build_q4(bank):
    for anth in ANTH.values():
        for i, (focus, tags) in enumerate(anth["focuses"]):
            part, lv = q4_parts(anth, focus, tags)
            bank.add(topic="reading-language", subtopic="el.ao2.anthology", qtype="lang-structure", command_word="how",
                     difficulty="4-6" if "e" in tags else "7-9", parts=[part],
                     markscheme={"style": "levels", "rows": [], "levels": [lv], "general": BEST_FIT},
                     spec_refs=["C1.A.AO2.1", anth["ref"]], ao=["AO2"], template="el-q4",
                     id=f"english-language.q4.{anth['id']}.{i + 1}", paper=["p1"], section="A", calculator=None,
                     intro=f"Text Two is *{anth['title']}* ({anth['author']}), from Part 1 of the Anthology. Use your own copy.",
                     figures=[text_two_figure(anth)], minutes=20)


# ------------------------------------------------------------------ writing
def writing_levels(label, ind):
    return [levels(label, GRID_AO4, ind, title="AO4: Communicate effectively and imaginatively, adapting form, tone and register for purpose and audience (27 marks)", ao_split="AO4 27"),
            levels(label, GRID_AO5, ["Assess vocabulary, sentence structures, paragraphing, spelling, punctuation and grammar across the whole response."],
                   title="AO5: Write clearly, using a range of vocabulary and sentence structures, with appropriate paragraphing and accurate spelling, grammar and punctuation (18 marks)",
                   ao_split="AO5 18", credit_note="Apply the grid using best fit across the whole response.")]


def build_writing(bank):
    tasks = writing_tasks()
    singles = []
    for t in tasks:
        text = t["text"] + "\n\n" + SPAG
        ind = [f"Purpose: {t['purpose']}", f"Audience: {t['audience']}", f"Form: {t['form_note']}", "Responses may:"] + t["ideas"]
        rec = bank.add(topic="writing", subtopic=f"el.writing.{t['form']}", qtype="transactional", command_word="write",
                       difficulty=t["difficulty"], parts=[{"label": "", "text": text, "marks": 45, "lines": 50}],
                       markscheme={"style": "levels", "rows": [], "levels": writing_levels("", ind), "general": BEST_FIT},
                       spec_refs=["C1.B", specmod_ref(t["form"]), specmod_ref(t["form"]) + "a", specmod_ref(t["form"]) + "b"],
                       ao=["AO4", "AO5"], template=f"el-w-{t['form']}", id=f"english-language.w.{t['form']}.{t['key']}",
                       paper=["p1"], section="B", calculator=None, minutes=45)
        singles.append((t, rec))
    # Section B choice: pairs of tasks in different forms
    r = rng(4401)
    pool = list(singles)
    r.shuffle(pool)
    used_pairs, k = set(), 0
    for i in range(len(pool)):
        for j in range(i + 1, len(pool)):
            ta, tb = pool[i][0], pool[j][0]
            if ta["form"] == tb["form"] or ta.get("issue") and ta.get("issue") == tb.get("issue"):
                continue
            if pool[i][1]["id"] in used_pairs or pool[j][1]["id"] in used_pairs:
                continue
            used_pairs |= {pool[i][1]["id"], pool[j][1]["id"]}
            k += 1
            text = ("Answer ONE of the following tasks, (a) or (b).\n\n**EITHER**\n\n**(a)** " + ta["text"] +
                    "\n\n**OR**\n\n**(b)** " + tb["text"] + "\n\n" + SPAG)
            ind = ([f"Task (a) — Purpose: {ta['purpose']} Audience: {ta['audience']} Form: {ta['form_note']}"] +
                   ["(a) " + x for x in ta["ideas"]] +
                   [f"Task (b) — Purpose: {tb['purpose']} Audience: {tb['audience']} Form: {tb['form_note']}"] +
                   ["(b) " + x for x in tb["ideas"]])
            diff = "7-9" if "7-9" in (ta["difficulty"], tb["difficulty"]) else "4-6"
            bank.add(topic="writing", subtopic="el.writing.choice", qtype="transactional-choice", command_word="write",
                     difficulty=diff, parts=[{"label": "", "text": text, "marks": 45, "lines": 50}],
                     markscheme={"style": "levels", "rows": [], "levels": writing_levels("", ind),
                                 "general": BEST_FIT + " Mark the task the candidate has chosen; the same grids apply to both."},
                     spec_refs=["C1.B", "C1.B.1", "C1.B.1a", specmod_ref(ta["form"]), specmod_ref(tb["form"])],
                     ao=["AO4", "AO5"], template="el-w-choice", id=f"english-language.wchoice.{k:03d}",
                     paper=["p1"], section="B", calculator=None, minutes=45)
            break


def specmod_ref(form):
    return {f[0]: f[1] for f in specmod.FORMS}[form]


def main():
    specmod.build()
    bank = Bank("english-language")
    build_reading(bank)
    build_q4(bank)
    build_writing(bank)
    bank.save()


if __name__ == "__main__":
    main()
