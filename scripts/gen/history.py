"""History (International GCSE 4HI1) generator: Dan's four options only.

Paper 1 depth studies: Germany 1918-45 (option 3) and A world divided 1943-72 (option 6).
Paper 2 Section A investigation: Russia and the Soviet Union 1905-24 (A2).
Paper 2 Section B breadth study: America 1783-1877 (B1).

Writes data/spec/history.json and data/bank/history/<topic>.json. Deterministic.
Every extract and source is original (see the content modules) and carries provenance.
"""
import json
import sys
from itertools import combinations
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import Bank, SPEC, levels  # noqa: E402
import history_germany as GER  # noqa: E402
import history_cold_war as CW  # noqa: E402
import history_russia as RUS  # noqa: E402
import history_america as AM  # noqa: E402

LINES = {6: 14, 8: 18, 16: 40}

# ------------------------------------------------------------------ spec

QTYPES = [
    {"id": "impression", "label": "Impression from an extract (6 marks)", "marks": "6",
     "description": "Paper 1 (a): what impression the author of an extract gives about an issue (AO4)."},
    {"id": "explain-effects", "label": "Explain two effects (8 marks)", "marks": "8",
     "description": "Paper 1 (b): explain two effects of an event or development (AO1, AO2)."},
    {"id": "judgement", "label": "How far do you agree? (16 marks)", "marks": "16",
     "description": "Paper 1 (c): judge a statement using two stimulus points and own knowledge (AO1, AO2)."},
    {"id": "describe-two", "label": "Describe two features (6 marks)", "marks": "6",
     "description": "Paper 2 Section A (a): describe two features of one of two named topics (AO1)."},
    {"id": "source-support", "label": "How far does Source A support Source B? (8 marks)", "marks": "8",
     "description": "Paper 2 Section A (b): cross-reference two sources for agreement and difference (AO3)."},
    {"id": "interpretation", "label": "Evaluate an interpretation (16 marks)", "marks": "16",
     "description": "Paper 2 Section A (c): judge the view in Extract C using the sources and own knowledge (AO3, AO4)."},
    {"id": "investigation", "label": "Source investigation (8 + 16 marks)", "marks": "24",
     "description": "Paper 2 Section A (b) and (c) together, sharing Sources A and B and Extract C, as they appear on the paper."},
    {"id": "explain-difference", "label": "Explain two differences (6 marks)", "marks": "6",
     "description": "Paper 2 Section B (a): explain two ways in which something was different at two points in time (AO1, AO2)."},
    {"id": "explain-causes", "label": "Explain two causes (8 marks)", "marks": "8",
     "description": "Paper 2 Section B (b): explain two causes of an event or development (AO1, AO2)."},
    {"id": "breadth-judgement", "label": "How far / how significant? (16 marks)", "marks": "16",
     "description": "Paper 2 Section B (c): judgement across at least 25 years using two stimulus points and own knowledge (AO1, AO2)."},
]

P1_Q = ["impression", "explain-effects", "judgement"]
P2A_Q = ["describe-two", "source-support", "interpretation", "investigation"]
P2B_Q = ["explain-difference", "explain-causes", "breadth-judgement"]

OPTIONS = [
    {"id": "germany", "name": "Germany: development of dictatorship, 1918–45", "paper": "p1", "section": "depth-germany"},
    {"id": "world-divided", "name": "A world divided: superpower relations, 1943–72", "paper": "p1", "section": "depth-world-divided"},
    {"id": "russia", "name": "Russia and the Soviet Union, 1905–24", "paper": "p2", "section": "A"},
    {"id": "america", "name": "America: from new nation to divided union, 1783–1877", "paper": "p2", "section": "B"},
]
OPT = {o["id"]: o for o in OPTIONS}

# (topic id, ref, option, qtypes, [(key, ref, title, summary, [point summaries])])
TOPICS = [
("germany", "3", "germany", P1_Q, [
 ("weimar", "3.1", "The establishment of the Weimar Republic and its early problems",
  "How the Kaiser fell, how the new republic was set up and the crises it faced up to 1923.",
  ["The end of the monarchy and the revolution of 1918–19.", "How the Weimar Constitution worked and its weaknesses.",
   "German reactions to the Treaty of Versailles.", "Threats from the left and right, such as the Spartacists and the Kapp Putsch.",
   "The occupation of the Ruhr in 1923.", "Hyperinflation and its effects on different groups."]),
 ("recovery", "3.2", "The recovery of Germany, 1924–29",
  "How Stresemann helped Germany recover at home and abroad in the 'golden years'.",
  ["Stresemann's role and achievements.", "Economic recovery: the Rentenmark, the Dawes and Young Plans and American loans.",
   "Foreign policy: Locarno, the League of Nations and the Kellogg–Briand Pact."]),
 ("rise", "3.3", "The rise of Hitler and the Nazis to January 1933",
  "How the Nazi Party grew from a tiny group into the largest party and Hitler became Chancellor.",
  ["The origins of the Nazi Party.", "Changes to the party in 1920–22.", "The Munich Putsch and its consequences.",
   "Reorganising the party after 1924.", "The impact of the Great Depression.", "Nazi methods, propaganda and the SA.",
   "Political deals of 1932 to January 1933."]),
 ("nazi", "3.4", "Nazi Germany 1933–39",
  "How Hitler created a dictatorship and controlled German society and the economy.",
  ["Steps to dictatorship, 1933–34.", "Methods of control: the police state, censorship and propaganda.",
   "Policies towards education, young people, women and the Churches.", "Racial policy and the persecution of Jews.",
   "Economic policy: reducing unemployment, the RAD, the DAF and Strength Through Joy."]),
 ("war", "3.5", "Germany and the occupied territories during the Second World War",
  "Life in Germany during the war, the Holocaust, opposition and the collapse of the Reich.",
  ["The treatment of Jews: ghettos, the Einsatzgruppen and the Final Solution.", "The impact of war on the home front.",
   "Opposition and resistance to the Nazis.", "The defeat of Germany and the end of the Third Reich."]),
]),
("world-divided", "6", "world-divided", P1_Q, [
 ("reasons", "6.1", "Reasons for the Cold War",
  "Why the wartime alliance broke down, including ideology, the conferences and Soviet control of Eastern Europe.",
  ["Long-term rivalry and ideological differences.", "Tensions within the wartime alliance.",
   "The Tehran, Yalta and Potsdam conferences.", "Soviet expansion in Eastern Europe.", "The attitudes of Truman and Stalin."]),
 ("early", "6.2", "Early developments in the Cold War, 1945–49",
  "How Europe divided into two blocs, from the 'iron curtain' to the Berlin Crisis and NATO.",
  ["Soviet expansion and satellite states.", "The 'iron curtain' speech.", "The Truman Doctrine and the Marshall Plan.",
   "Cominform and Comecon.", "Disagreements over Germany and the creation of Bizonia.",
   "The Berlin Crisis, NATO and the creation of two German states."]),
 ("fifties", "6.3", "The Cold War in the 1950s",
  "The arms race, Khrushchev's peaceful co-existence and the crushing of the Hungarian Rising.",
  ["The Korean War and the Warsaw Pact.", "Khrushchev and peaceful co-existence.",
   "Rákosi's rule and the causes of the Hungarian Rising.", "The Soviet invasion of Hungary and its effects.", "The nuclear arms race."]),
 ("crises", "6.4", "Three Cold War crises: Berlin, Cuba and Czechoslovakia, c1957–69",
  "The Berlin Wall, the Cuban Missile Crisis and the Prague Spring, and what they show about superpower relations.",
  ["The U2 incident and the Paris Summit.", "Reasons for building the Berlin Wall.", "Effects of the Berlin Wall.",
   "The Bay of Pigs and the Cuban Missile Crisis.", "The Prague Spring, the invasion of Czechoslovakia and the Brezhnev Doctrine."]),
 ("detente", "6.5", "The thaw and moves towards détente, 1963–72",
  "How the superpowers tried to reduce tension after 1962, through to SALT I.",
  ["The Hotline and the arms treaties of the 1960s.", "Reasons for détente.", "The SALT talks and SALT I.",
   "How far relations had improved by 1972."]),
]),
("russia", "A2", "russia", P2A_Q, [
 ("tsarist", "A2.1", "Tsarist rule in Russia, 1905–14",
  "The 1905 Revolution, the Dumas, Stolypin and growing discontent before the First World War.",
  ["The nature of Tsarist rule and discontent.", "Bloody Sunday, the Potemkin mutiny and the soviets.",
   "The October Manifesto and why the Tsar survived 1905.", "The Dumas and their limits.", "Opposition groups.",
   "Stolypin's repression and reforms.", "The Lena Goldfields Massacre and rising unrest."]),
 ("war-feb", "A2.2", "Opposition to Tsarist rule, 1914–17",
  "How the First World War weakened the Tsar and led to the February Revolution and his abdication.",
  ["Effects of the war on the army and the home front.", "Rasputin and the Tsarina.", "Causes and events of the February Revolution.",
   "Army mutiny and the Tsar's abdication.", "The setting up of the Provisional Government."]),
 ("provisional", "A2.3", "Provisional Government and the Bolshevik revolution, 1917",
  "Why the Provisional Government failed and how the Bolsheviks seized power in October 1917.",
  ["Weaknesses of the Provisional Government.", "The Petrograd Soviet and Dual Power.", "The April Theses and the July Days.",
   "The Kornilov Affair.", "The Bolshevik seizure of power.", "Reasons for success, including Lenin and Trotsky."]),
 ("civil-war", "A2.4", "The Bolshevic consolidation of power and the Civil War, 1917–21".replace("Bolshevic", "Bolshevik"),
  "How the Bolsheviks kept power: early decrees, the Constituent Assembly, Brest-Litovsk and the Civil War.",
  ["Early Bolshevik decrees.", "The closing of the Constituent Assembly.", "The Treaty of Brest-Litovsk.",
   "The two sides in the Civil War.", "Events of the Civil War and reasons for Bolshevik victory."]),
 ("nep", "A2.5", "War Communism and the New Economic Policy, 1918–24",
  "Why War Communism was replaced by the NEP, opposition to it and Lenin's achievements by 1924.",
  ["War Communism and its effects.", "The Kronstadt Rising.", "The New Economic Policy.", "Opposition to the NEP.",
   "Lenin's achievements by 1924."]),
]),
("america", "B1", "america", P2B_Q, [
 ("new-nation", "B1.1", "A new nation, 1783–1803",
  "How the United States created its Constitution and system of government, and the divisions this caused.",
  ["Large and small states and the question of slavery.", "Shays' Rebellion.", "The Constitutional Convention and the Connecticut Compromise.",
   "Federalists, Anti-federalists and the Bill of Rights.", "Strict and loose constructionists.", "Jefferson's presidency."]),
 ("westward", "B1.2", "Westward expansion, 1803–53",
  "How and why the USA expanded across the continent, and the impact on Native Americans and slavery.",
  ["Opposition to expansion.", "The Louisiana Purchase, the Transcontinental Treaty and Texas.", "The Missouri Compromise.",
   "Indian Removal and the Trail of Tears.", "Manifest Destiny, Oregon, the Mexican War and the Gold Rush."]),
 ("slavery", "B1.3", "The road to civil war, 1850–61",
  "How disputes over slavery and the territories divided North and South and led to secession.",
  ["The Compromise of 1850.", "The Kansas–Nebraska Act and Bleeding Kansas.", "The Dred Scott decision.",
   "Economic differences between North and South.", "John Brown, Lincoln's election, secession and Fort Sumter."]),
 ("civil-war", "B1.4", "The Civil War, 1861–65",
  "Why the Union won, the leaders on each side and the effects of the war on the South.",
  ["Reasons for Union victory and the role of generals.", "The Union blockade.", "Lincoln, Davis, the Emancipation Proclamation and the Gettysburg Address.",
   "Key battles and campaigns: Gettysburg, Vicksburg and the March through Georgia.", "The impact of the war on the Southern economy."]),
 ("reconstruction", "B1.5", "Reconstruction, 1865–77",
  "How the South was rebuilt, what freedom meant for African Americans, and policy towards Native Americans.",
  ["Johnson and the Reconstruction Acts.", "The Freedmen's Bureau and the Black Codes.",
   "The Civil Rights Acts and the 13th–15th Amendments.", "The Peace Policy and the Battle of the Little Bighorn."]),
]),
]

TOPIC_TITLES = {o["id"]: o["name"] for o in OPTIONS}

P_COMMON_INFO = ["The total mark for this paper is 60.",
                 "The marks for each question are shown in brackets: use this as a guide to how much time to spend on each question."]
PAPERS = [
 {"id": "p1", "name": "Paper 1 Depth Studies", "paper_code": "4HI1/01", "minutes": 90, "marks": 60, "calculator": None,
  "answer_style": "separate-booklet", "materials": "Sources/extracts booklet (inserted); answer booklet.",
  "instructions": ["Use black ink or ball-point pen.", "Answer questions from TWO depth studies: one question for each depth study.",
                   "In part (c) of each question, answer EITHER (i) OR (ii).",
                   "Write your answers in the separate answer booklet.", "Fill in the boxes on the front of the answer booklet."],
  "information": P_COMMON_INFO + ["Spend about 45 minutes on each depth study."],
  "advice": ["Read each question carefully before you start to answer it.",
             "In part (a), refer closely to the extract and how the author presents the topic.",
             "Check your answers if you have time at the end."],
  "sections": [
   {"id": "depth-germany", "title": "Germany: development of dictatorship, 1918–45", "marks": 30,
    "instructions": "Answer parts (a) and (b), and EITHER (c)(i) OR (c)(ii).",
    "slots": [{"label": "(a)", "qtypes": ["impression"], "marks": 6, "option": "germany"},
              {"label": "(b)", "qtypes": ["explain-effects"], "marks": 8, "option": "germany"},
              {"label": "(c)", "qtypes": ["judgement"], "marks": 16, "choice": 2, "option": "germany"}]},
   {"id": "depth-world-divided", "title": "A world divided: superpower relations, 1943–72", "marks": 30,
    "instructions": "Answer parts (a) and (b), and EITHER (c)(i) OR (c)(ii).",
    "slots": [{"label": "(a)", "qtypes": ["impression"], "marks": 6, "option": "world-divided"},
              {"label": "(b)", "qtypes": ["explain-effects"], "marks": 8, "option": "world-divided"},
              {"label": "(c)", "qtypes": ["judgement"], "marks": 16, "choice": 2, "option": "world-divided"}]},
  ]},
 {"id": "p2", "name": "Paper 2 Investigation and Breadth Studies", "paper_code": "4HI1/02", "minutes": 90, "marks": 60, "calculator": None,
  "answer_style": "separate-booklet", "materials": "Sources and extracts booklet (inserted); answer booklet.",
  "instructions": ["Use black ink or ball-point pen.", "Answer ONE question from Section A and ONE question from Section B.",
                   "In Section B part (c), answer EITHER (i) OR (ii).",
                   "Write your answers in the separate answer booklet.", "Fill in the boxes on the front of the answer booklet."],
  "information": P_COMMON_INFO + ["Spend about 45 minutes on each section."],
  "advice": ["Read each question carefully before you start to answer it.",
             "In Section A, use the sources and the extract as the question directs.",
             "Check your answers if you have time at the end."],
  "sections": [
   {"id": "A", "title": "Section A: Historical investigation — Russia and the Soviet Union, 1905–24", "marks": 30,
    "instructions": "Answer all parts of the question.",
    "slots": [{"label": "(a)", "qtypes": ["describe-two"], "marks": 6, "option": "russia"},
              {"label": "(b)–(c)", "qtypes": ["investigation"], "marks": 24, "option": "russia"}]},
   {"id": "B", "title": "Section B: Breadth study in change — America: from new nation to divided union, 1783–1877", "marks": 30,
    "instructions": "Answer parts (a) and (b), and EITHER (c)(i) OR (c)(ii).",
    "slots": [{"label": "(a)", "qtypes": ["explain-difference"], "marks": 6, "option": "america"},
              {"label": "(b)", "qtypes": ["explain-causes"], "marks": 8, "option": "america"},
              {"label": "(c)", "qtypes": ["breadth-judgement"], "marks": 16, "choice": 2, "option": "america"}]},
  ]},
]


def build_spec():
    topics = []
    for tid, tref, opt, qts, subs in TOPICS:
        paper = OPT[opt]["paper"]
        sts = []
        for key, ref, title, summary, pts in subs:
            sts.append({"id": f"history.{tid}.{key}", "ref": ref, "title": title, "summary": summary,
                        "papers": [paper], "qtypes": list(qts),
                        "points": [{"ref": f"{ref}{chr(97 + i)}", "summary": s} for i, s in enumerate(pts)]})
        topics.append({"id": tid, "ref": tref, "title": TOPIC_TITLES[opt], "papers": [paper], "option": opt, "subtopics": sts})
    spec = {"subject": "history", "code": "4HI1", "board": "Pearson Edexcel",
            "title": "Pearson Edexcel International GCSE (9–1) History 4HI1", "short": "History",
            "official_url": "https://qualifications.pearson.com/en/qualifications/edexcel-international-gcses/international-gcse-history-2017.html",
            "spec_url": "https://qualifications.pearson.com/en/qualifications/edexcel-international-gcses/international-gcse-history-2017.html",
            "papers": PAPERS, "qtypes": QTYPES, "options": OPTIONS, "topics": topics}
    (SPEC / "history.json").write_text(json.dumps(spec, ensure_ascii=False, indent=1))
    return spec


# ------------------------------------------------------------------ level grids (paraphrased)

G_IMPRESSION = [
 ("Level 1", "1–2", "A simple comment on the extract. The impression is stated or implied but is supported only by general or surface detail."),
 ("Level 2", "3–4", "A developed explanation of the impression, supported by relevant material chosen from the extract."),
 ("Level 3", "5–6", "An analysis of the impression that explains how the author creates it, for example through choice of detail, emphasis, language or omission, with well-chosen support from the extract."),
]
G_EXPLAIN8 = [
 ("Level 1", "1–2", "A simple or generalised answer, with little development. Limited, mostly accurate knowledge."),
 ("Level 2", "3–5", "An explanation showing some analysis, with some development of at least one {x}. Accurate and relevant knowledge is used to support it."),
 ("Level 3", "6–8", "An analytical explanation of two {x}s that is clearly linked to the question. Accurate and relevant knowledge is used well to support it."),
]
G_SIX = [
 ("Level 1", "1–2", "A simple answer giving one or more {x}s with little or no supporting detail."),
 ("Level 2", "3–4", "A developed answer: {x}s are explained with some accurate supporting knowledge. Maximum 3 marks if only one {x} is given."),
 ("Level 3", "5–6", "A well-developed answer: two {x}s are explained, each supported with accurate and relevant knowledge."),
]
G_SIXTEEN = [
 ("Level 1", "1–4", "A simple or generalised answer with little analysis. Limited knowledge. A judgement may be given but is asserted rather than supported."),
 ("Level 2", "5–8", "An explanation showing some analysis, but it may lack focus or balance. Accurate knowledge is used to support it. A judgement is given but is only partly supported."),
 ("Level 3", "9–12", "An analytical explanation directed at the question, considering more than one side. Accurate and relevant knowledge is used effectively. The judgement is linked to criteria but is not fully justified."),
 ("Level 4", "13–16", "A sustained analytical explanation clearly focused on the question, weighing different factors. Wide-ranging, precise knowledge is used throughout. The judgement is reached using clear criteria and is fully justified."),
]
G_DESCRIBE = [
 ("Level 1", "1–2", "Simple features are given, with little supporting detail."),
 ("Level 2", "3–4", "Features are described with some accurate supporting detail. Maximum 3 marks if only one feature is described."),
 ("Level 3", "5–6", "Two features are described, each developed with accurate and relevant detail."),
]
G_SUPPORT = [
 ("Level 1", "1–2", "A simple comparison based on surface details of the sources, with little support taken from them."),
 ("Level 2", "3–5", "A developed comparison identifying agreement and/or difference, supported with detail from both sources. Maximum 4 marks unless both agreement and difference are considered."),
 ("Level 3", "6–8", "An analytical comparison of agreement and difference, well supported from both sources, with a reasoned overall judgement on how far Source A supports Source B."),
]
G_INTERP = [
 ("Level 1", "1–4", "A simple answer that paraphrases or selects from the material. Little use of own knowledge. A judgement may be asserted."),
 ("Level 2", "5–8", "A developed answer that uses the extract, the sources and some own knowledge to comment on the interpretation, but may be one-sided. A judgement is given but is only partly supported."),
 ("Level 3", "9–12", "An analytical answer that considers evidence both for and against the interpretation from the sources and own knowledge. The judgement is linked to the evidence but is not fully sustained."),
 ("Level 4", "13–16", "A sustained evaluation that weighs evidence from the sources and precise own knowledge against the interpretation. A clear, fully justified judgement is reached and maintained."),
]

GEN_IMPRESSION = ("This question tests AO4 (how and why an interpretation is formed). Own knowledge is not needed and is not credited for its own sake. "
                  "Answers that only describe or paraphrase the extract without identifying an impression stay in Level 1.")
GEN_EXPLAIN = ("Maximum 4 marks if only one {x} is explained; an answer explaining only one {x} cannot reach Level 3. "
               "Narrative that is not linked to the {x}s is not rewarded beyond Level 1.")
GEN_SIXTEEN = ("An answer that does not go beyond the two stimulus points can reach at most 6 marks in Level 2 and at most 10 marks in Level 3. "
               "Level 4 needs at least three aspects, at least one of them from the candidate's own knowledge, and a supported judgement.")
GEN_SUPPORT = ("This question tests AO3 (analysing and comparing sources). Comments on the reliability or provenance of the sources are not required "
               "and gain credit only where they are used to explain the extent of support.")
GEN_INTERP = ("The extract cannot be used to support itself: support or challenge must come from Sources A and B and own knowledge. "
              "Answers that use only the extract and sources, with no own knowledge, are limited to Level 2. "
              "A clear judgement on how far the candidate agrees should be stated and sustained.")


def grid(g, x=""):
    return [(a, b, c.replace("{x}", x)) for a, b, c in g]


def cap(s):
    return s[0].upper() + s[1:] if s else s


def band(i, mod, lo, hi, first=0):
    return lo if i % mod == first else hi


# ------------------------------------------------------------------ Paper 1

EXT_PROV = "Original extract written for this practice question in the style of a modern history book; it is not taken from any published work."
SRC_PROV = ("Original source written for this practice question. It is attributed to an invented, unnamed person of the period and "
            "is not a real historical document.")


def p1(bank, tid, opt, content):
    sec = OPT[opt]["section"]
    sub_refs = {key: ref for t in TOPICS if t[0] == tid for key, ref, *_ in t[4]}
    for key, ref in sub_refs.items():
        st = f"history.{tid}.{key}"
        common = dict(topic=tid, subtopic=st, spec_refs=[ref], paper=["p1"], option=opt, section=sec)
        # (a) impression
        i = 0
        for line, text, foci in content.EXTRACTS[key]:
            for focus, impression, quotes, note in foci:
                for q in quotes:
                    assert q in text, (key, q)
                fig = {"type": "source", "label": f"Extract A: {line}", "text": text, "provenance": EXT_PROV}
                ind = [f"The impression created is that {impression}."]
                ind += [f"The impression is supported by the author's wording, for example ‘{q}’." for q in quotes]
                ind.append(note)
                ind.append("A Level 3 answer explains how the author's selection and treatment of material create the impression, not just what the extract says.")
                bank.add(**common, qtype="impression", command_word="What impression", template=f"{opt}-impression",
                         difficulty=band(i, 4, "1-3", "4-6"), ao=["AO4"], figures=[fig], provenance=EXT_PROV,
                         parts=[{"text": f"Study Extract A.\nWhat impression does the author give about {focus}?\n"
                                         "You must use Extract A to explain your answer.", "marks": 6, "lines": LINES[6]}],
                         markscheme={"style": "levels", "rows": [], "general": GEN_IMPRESSION,
                                     "levels": [levels("", G_IMPRESSION, ind, title="Impression", ao_split="AO4 (6)")]})
                i += 1
        # (b) explain effects
        for i, (event, effects) in enumerate(content.EFFECTS[key]):
            ind = [f"An effect was that {e}: for example, {ex}." for e, ex in effects]
            ind.append("Each effect should be explained in terms of its outcome, not just described.")
            bank.add(**common, qtype="explain-effects", command_word="Explain", template=f"{opt}-effects",
                     difficulty=band(i, 5, "1-3", "4-6"), ao=["AO1", "AO2"],
                     parts=[{"text": f"Explain two effects of {event}.", "marks": 8, "lines": LINES[8]}],
                     markscheme={"style": "levels", "rows": [], "general": GEN_EXPLAIN.replace("{x}", "effect"),
                                 "levels": [levels("", grid(G_EXPLAIN8, "effect"), ind, title="Consequence",
                                                   ao_split="AO1 (4), AO2 (4)")]})
        # (c) judgement
        judgement(bank, common, content.ISSUES[key], f"{opt}-judgement", "judgement", paper1=True)


BULLET_DATES = {
    "the Reichstag Fire": "the Reichstag Fire of February 1933",
    "the Enabling Act": "the Enabling Act of March 1933",
    "the Truman Doctrine": "the Truman Doctrine of March 1947",
    "the Soviet invasion of Hungary": "the Soviet invasion of Hungary in November 1956",
    "the SALT talks and treaty": "the SALT talks of 1969–72 and the SALT I treaty",
    "the Test Ban Treaty": "the Partial Test Ban Treaty of 1963",
}


def judgement(bank, common, issues, template, qtype, paper1):
    i = 0
    for iss in issues:
        if iss.get("skip"):
            continue
        facs = iss["factors"]
        for j, (name, pts) in enumerate(facs):
            stem = iss["stems"][j % len(iss["stems"])]
            other = facs[(j + 1) % len(facs)]
            statement = stem.replace("{f}", name)
            if statement.startswith("‘"):
                statement = "‘" + cap(statement[1:])
            else:
                statement = cap(statement)
            # short noun phrases naming the factors (a few carry a date to stay distinct from real papers)
            bullets = [BULLET_DATES.get(name, name), BULLET_DATES.get(other[0], other[0])]
            if paper1:
                text = (f"{statement}\nHow far do you agree? Explain your answer.\n"
                        f"You may use the following in your answer:\n• {bullets[0]}\n• {bullets[1]}\n"
                        "You must also use information of your own.")
            else:
                text = (f"{statement}\nExplain your answer.\n"
                        f"You may use the following in your answer:\n• {bullets[0]}\n• {bullets[1]}\n"
                        "You must also use information of your own.")
            ind = [f"Evidence supporting the importance of {name}: {p}." for p in pts]
            for oname, opts in facs:
                if oname == name:
                    continue
                ind.append(f"Other factors to weigh against it — {oname}: " + "; ".join(opts[:2]) + ".")
            ind.append(f"A supported judgement should weigh {name} against at least one other factor using clear criteria, "
                       "such as how long-lasting or widespread its impact was, or whether other factors depended on it.")
            bank.add(**common, qtype=qtype, command_word="How far" if "How far" in text or paper1 else "How significant",
                     template=template, difficulty=band(i, 4, "4-6", "7-9"), ao=["AO1", "AO2"],
                     parts=[{"text": text, "marks": 16, "lines": LINES[16]}],
                     markscheme={"style": "levels", "rows": [], "general": GEN_SIXTEEN,
                                 "levels": [levels("", G_SIXTEEN, ind, title="Judgement", ao_split="AO1 (7), AO2 (9)")]})
            i += 1


# ------------------------------------------------------------------ Paper 2 Section A (Russia)

def stance_text(cl, asp, st):
    return cl["aspects"][asp][st]


def compare(cl, a, b):
    """Return (agreements, differences) between source a and b claims."""
    agree, diff = [], []
    ca, cb = a[2], b[2]
    # every aspect a source's text addresses must be tagged (an untagged aspect is reported as "not
    # mentioned"), and one piece of evidence may back only one aspect, so no bullet repeats another
    for s in (a, b):
        evs = [ev for _, ev in s[2].values()]
        assert len(evs) == len(set(evs)), ("evidence reused across aspects", s[0])
    for asp in cl["aspects"]:
        if asp in ca and asp in cb:
            (sa, ea), (sb, eb) = ca[asp], cb[asp]
            if sa == sb:
                agree.append(f"Agreement: both sources suggest that {stance_text(cl, asp, sa)}. Source A: {ea}. Source B: {eb}.")
            else:
                diff.append(f"Difference: Source A suggests that {stance_text(cl, asp, sa)} ({ea}), whereas Source B suggests that "
                            f"{stance_text(cl, asp, sb)} ({eb}).")
        elif asp in ca:
            sa, ea = ca[asp]
            diff.append(f"Difference: Source A suggests that {stance_text(cl, asp, sa)} ({ea}); Source B does not support this point.")
        elif asp in cb:
            sb, eb = cb[asp]
            diff.append(f"Difference: Source B suggests that {stance_text(cl, asp, sb)} ({eb}), which Source A does not mention.")
    assert len(set(agree + diff)) == len(agree + diff), ("duplicate bullet", a[0], b[0])
    return agree, diff


def src_fig(s, label):
    return {"type": "source", "label": f"Source {label}: {s[0]}", "text": s[1], "provenance": SRC_PROV}


def support_ind(cl, a, b):
    agree, diff = compare(cl, a, b)
    assert agree, ("no agreement", cl["focus"], a[0], b[0])
    if len(agree) > len(diff):
        ext = "Overall, Source A gives strong support to Source B, although there are some differences of emphasis."
    elif len(agree) == len(diff):
        ext = "Overall, Source A supports Source B in part: they agree on some points but differ on others."
    else:
        ext = "Overall, Source A gives only limited support to Source B: they share some ground but differ on several points."
    return agree + diff + [ext]


def interp_ind(cl, a, b, ext_view):
    v = ext_view
    ind = [f"Extract C argues that {v['view']}; it says that " + " and ".join(v["ext"]) + "."]
    # Only aspects that bear on THIS view are classified: "pro" aspects support it when the source takes
    # the given stance and challenge it otherwise; "alt" aspects challenge it (another factor) only when
    # the source takes the given stance. Every other source point is irrelevant here and is left out.
    nsrc = 0
    for lab, s in (("A", a), ("B", b)):
        for asp, (st, ev) in s[2].items():
            if asp in v["pro"]:
                kind = "Support" if st == v["pro"][asp] else "Challenge"
                ind.append(f"{kind} from Source {lab}: it suggests that {stance_text(cl, asp, st)} ({ev}).")
                nsrc += 1
            elif v.get("alt", {}).get(asp) == st:
                ind.append(f"Challenge from Source {lab}: it points to a different factor, suggesting that "
                           f"{stance_text(cl, asp, st)} ({ev}).")
                nsrc += 1
    if not nsrc:
        ind.append("Sources A and B do not bear directly on this interpretation: credit candidates who explain their "
                   "limited relevance and base the judgement mainly on Extract C and own knowledge.")
    ind += [f"Own knowledge supporting the interpretation: {x}." for x in v["own_for"]]
    ind += [f"Own knowledge challenging the interpretation: {x}." for x in v["own_against"]]
    ind.append("A Level 4 answer reaches a clear judgement on how far it agrees, weighing the evidence of the sources and own knowledge against the view in Extract C.")
    return ind


def russia(bank):
    opt, tid = "russia", "russia"
    sec = OPT[opt]["section"]
    for key, ref, *_ in [t for t in TOPICS if t[0] == tid][0][4]:
        st = f"history.{tid}.{key}"
        common = dict(topic=tid, subtopic=st, spec_refs=[ref], paper=["p2"], option=opt, section=sec)
        # (a) describe two features
        feats = RUS.FEATURES[key]
        n = len(feats)
        i = 0
        for step in (1, 2):
            for k in range(n):
                x, y = feats[k], feats[(k + step) % n]
                ind = []
                for name, fl in (x, y):
                    ind += [f"{cap(name)}: {f}, for example {d}." for f, d in fl]
                ind.append("Candidates answer on only ONE of the two topics; credit each feature that is described and supported with relevant detail.")
                bank.add(**common, qtype="describe-two", command_word="Describe", template="russia-describe",
                         difficulty=band(i, 2, "1-3", "4-6"), ao=["AO1"],
                         parts=[{"text": f"Describe TWO features of EITHER {x[0]} OR {y[0]}.", "marks": 6, "lines": LINES[6]}],
                         markscheme={"style": "levels", "rows": [],
                                     "general": "Answers on both topics are marked on the better one. Maximum 3 marks if only one feature is described.",
                                     "levels": [levels("", G_DESCRIBE, ind, title="Features", ao_split="AO1 (6)")]})
                i += 1
        # (b) source-support, (c) interpretation, investigation
        i = j = 0
        for cl in RUS.CLUSTERS[key]:
            srcs = cl["sources"]
            pairs = list(combinations(range(len(srcs)), 2))
            for pa, pb in pairs:
                a, b = srcs[pa], srcs[pb]
                figs = [src_fig(a, "A"), src_fig(b, "B")]
                bank.add(**common, qtype="source-support", command_word="How far", template="russia-support",
                         difficulty=band(i, 3, "7-9", "4-6"), ao=["AO3"], figures=figs, provenance=SRC_PROV,
                         parts=[{"text": f"Study Sources A and B.\nHow far does Source A support the evidence of Source B about {cl['focus']}?\n"
                                         "Explain your answer.", "marks": 8, "lines": LINES[8]}],
                         markscheme={"style": "levels", "rows": [], "general": GEN_SUPPORT,
                                     "levels": [levels("", G_SUPPORT, support_ind(cl, a, b), title="Cross-reference", ao_split="AO3 (8)")]})
                i += 1
            vk = 0
            for eline, etext, views in cl["extracts"]:
                efig = {"type": "source", "label": f"Extract C: {eline}", "text": etext, "provenance": EXT_PROV}
                for v in views:
                    # rotate through the pairs as before, but prefer pairs in which both sources bear on
                    # this view (and then pairs with more relevant points), so part (c) uses the sources
                    rel = lambda s: sum(1 for asp, (st, _) in s[2].items()
                                        if asp in v["pro"] or v.get("alt", {}).get(asp) == st)
                    score = lambda p: (min(rel(srcs[p[0]]), rel(srcs[p[1]])) > 0, rel(srcs[p[0]]) + rel(srcs[p[1]]))
                    order = [pairs[(vk * 2 + k) % len(pairs)] for k in range(len(pairs))]
                    ranked = sorted(order, key=score, reverse=True)  # stable: keeps rotation order among ties
                    (pa, pb), (qa, qb) = ranked[0], ranked[1]
                    vk += 1
                    a, b = srcs[pa], srcs[pb]
                    figs = [src_fig(a, "A"), src_fig(b, "B"), efig]
                    itext = (f"Study Extract C.\nExtract C suggests that {v['view']}.\nHow far do you agree with this interpretation?\n"
                             "Use Extract C, Sources A and B and your own knowledge to explain your answer.")
                    bank.add(**common, qtype="interpretation", command_word="How far", template="russia-interpretation",
                             difficulty=band(j, 4, "4-6", "7-9"), ao=["AO3", "AO4"], figures=figs,
                             provenance=SRC_PROV + " " + EXT_PROV,
                             parts=[{"text": itext, "marks": 16, "lines": LINES[16]}],
                             markscheme={"style": "levels", "rows": [], "general": GEN_INTERP,
                                         "levels": [levels("", G_INTERP, interp_ind(cl, a, b, v), title="Interpretation",
                                                           ao_split="AO3 (10), AO4 (6)")]})
                    # investigation uses a second pair so it is a different combination
                    a2, b2 = srcs[qa], srcs[qb]
                    figs2 = [src_fig(a2, "A"), src_fig(b2, "B"), efig]
                    bank.add(**common, qtype="investigation", command_word="How far", template="russia-investigation",
                             difficulty=band(j, 4, "4-6", "7-9"), ao=["AO3", "AO4"], figures=figs2,
                             provenance=SRC_PROV + " " + EXT_PROV,
                             parts=[{"label": "b", "text": f"Study Sources A and B.\nHow far does Source A support the evidence of Source B about {cl['focus']}?\n"
                                                           "Explain your answer.", "marks": 8, "lines": LINES[8]},
                                    {"label": "c", "text": itext, "marks": 16, "lines": LINES[16]}],
                             markscheme={"style": "levels", "rows": [], "general": "(b): " + GEN_SUPPORT + " (c): " + GEN_INTERP,
                                         "levels": [levels("b", G_SUPPORT, support_ind(cl, a2, b2), title="Cross-reference", ao_split="AO3 (8)"),
                                                    levels("c", G_INTERP, interp_ind(cl, a2, b2, v), title="Interpretation",
                                                           ao_split="AO3 (10), AO4 (6)")]})
                    j += 1


# ------------------------------------------------------------------ Paper 2 Section B (America)

def america(bank):
    opt, tid = "america", "america"
    sec = OPT[opt]["section"]
    for key, ref, *_ in [t for t in TOPICS if t[0] == tid][0][4]:
        st = f"history.{tid}.{key}"
        common = dict(topic=tid, subtopic=st, spec_refs=[ref], paper=["p2"], option=opt, section=sec)
        for i, (subj, t1, t2, diffs) in enumerate(AM.DIFFERENCES[key]):
            ind = [f"{cap(d)} (for example, {ex})." for d, ex in diffs]
            ind.append("Answers should make the comparison explicit, using comparative language such as 'whereas' or 'by contrast'.")
            bank.add(**common, qtype="explain-difference", command_word="Explain", template="america-difference",
                     difficulty=band(i, 4, "1-3", "4-6"), ao=["AO1", "AO2"],
                     parts=[{"text": f"Explain two ways in which {subj} in {t1} was different from {subj} in {t2}.", "marks": 6, "lines": LINES[6]}],
                     markscheme={"style": "levels", "rows": [],
                                 "general": "Maximum 3 marks if only one difference is explained. Description of one period without comparison stays in Level 1.",
                                 "levels": [levels("", grid(G_SIX, "difference"), ind, title="Difference", ao_split="AO1 (2), AO2 (4)")]})
        for i, (event, causes) in enumerate(AM.CAUSES[key]):
            ind = [f"A cause was that {c}: for example, {ex}." for c, ex in causes]
            ind.append("Each cause should be linked clearly to the outcome, not just described.")
            bank.add(**common, qtype="explain-causes", command_word="Explain", template="america-causes",
                     difficulty=band(i, 5, "1-3", "4-6"), ao=["AO1", "AO2"],
                     parts=[{"text": f"Explain two causes of {event}.", "marks": 8, "lines": LINES[8]}],
                     markscheme={"style": "levels", "rows": [], "general": GEN_EXPLAIN.replace("{x}", "cause"),
                                 "levels": [levels("", grid(G_EXPLAIN8, "cause"), ind, title="Causation", ao_split="AO1 (4), AO2 (4)")]})
        judgement(bank, common, AM.ISSUES[key], "america-judgement", "breadth-judgement", paper1=False)


def main():
    build_spec()
    bank = Bank("history")
    p1(bank, "germany", "germany", GER)
    p1(bank, "world-divided", "world-divided", CW)
    russia(bank)
    america(bank)
    bank.save()


if __name__ == "__main__":
    main()
