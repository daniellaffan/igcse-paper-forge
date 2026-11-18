"""Simplified specification for 4ET1 Paper 1 (Poetry and Modern Prose), written as data.

The 4ET1 specification has no numbered content points, so references here are
our own scheme: 1A/1B/1C = Component 1 Sections A/B/C; P3.nn = poem nn in the
anthology poetry collection (in the order the specification lists them).
"""
from english_literature_anthology import POEMS, THEMES

UNSEEN_SUBS = [
 ("unseen.nature", "1A.1", "Nature, seasons and the natural world",
  "Unseen poems about landscapes, weather, plants, animals and the seasons.",
  [("1A.1.a", "Explain how imagery and description bring a natural scene to life."),
   ("1A.1.b", "Show how a poet uses nature to suggest feelings or ideas.")]),
 ("unseen.family", "1A.2", "Family, childhood and growing up",
  "Unseen poems about parents, grandparents, siblings and childhood experiences.",
  [("1A.2.a", "Analyse how a poet presents a relationship between family members."),
   ("1A.2.b", "Comment on how a child's point of view or growing up is shown.")]),
 ("unseen.memory", "1A.3", "Memory, time and change",
  "Unseen poems that look back, reflect on ageing or show how time changes things.",
  [("1A.3.a", "Explain how structure and tense shifts move between past and present."),
   ("1A.3.b", "Analyse how a poet presents the effects of time.")]),
 ("unseen.place", "1A.4", "Places, journeys and home",
  "Unseen poems about cities, homes, journeys and being away from home.",
  [("1A.4.a", "Analyse how a poet creates a sense of place."),
   ("1A.4.b", "Comment on how a journey or a home is given wider meaning.")]),
 ("unseen.feelings", "1A.5", "Love, loss and strong feelings",
  "Unseen poems expressing joy, grief, fear, hope, loneliness or love.",
  [("1A.5.a", "Explain how language choices convey strong emotion."),
   ("1A.5.b", "Analyse how form and structure shape a poem's emotional effect.")]),
 ("unseen.society", "1A.6", "People, society and the wider world",
  "Unseen poems about communities, work, war, power and freedom.",
  [("1A.6.a", "Analyse how a poet presents a community or a social issue."),
   ("1A.6.b", "Comment on the poet's attitude and how it is conveyed.")]),
]

ANTH_SUMMARY = {
 "anth.identity": "Comparing poems about who we are: culture, language, heritage and belonging.",
 "anth.love": "Comparing poems about love, marriage, family bonds and controlling relationships.",
 "anth.death": "Comparing poems about dying, mourning, loss and how people respond to death.",
 "anth.memory": "Comparing poems that look back to childhood or reflect on the passing of time.",
 "anth.power": "Comparing poems about power, control, conflict and those who hold or resist it.",
 "anth.advice": "Comparing poems with a strong persuasive voice giving advice or arguing a view.",
 "anth.experience": "Comparing poems that capture a vivid event, a moment, or the experience of suffering.",
}

PROSE_SUBS = [
 ("omam.george-lennie", "1C.1", "George, Lennie and their friendship", "prose-character",
  "The two central characters and the bond that sets them apart from other ranch workers.",
  [("1C.1.a", "Know how George and Lennie are presented and how they change."),
   ("1C.1.b", "Explain why their friendship is unusual and how it ends.")]),
 ("omam.curley-wife", "1C.2", "Curley and Curley's wife", "prose-character",
  "The boss's son, his unnamed wife and their unhappy marriage.",
  [("1C.2.a", "Explain how Curley's insecurity and aggression drive events."),
   ("1C.2.b", "Discuss how Curley's wife is presented as both threat and victim.")]),
 ("omam.outsiders", "1C.3", "Candy, Crooks and the outsiders", "prose-character",
  "Characters pushed to the edge of ranch life by age, injury, race or gender.",
  [("1C.3.a", "Know the roles of Candy and Crooks and the scene in Crooks's room."),
   ("1C.3.b", "Link each outsider to attitudes of the 1930s.")]),
 ("omam.ranch", "1C.4", "Slim, Carlson and choosing a character", "prose-character",
  "Other ranch workers and the 'which one character' style of question.",
  [("1C.4.a", "Know the roles of Slim, Carlson, the boss and Whit."),
   ("1C.4.b", "Choose and justify one character against others.")]),
 ("omam.dreams", "1C.5", "Dreams, money and happiness", "prose-theme",
  "The dream farm, other characters' hopes, wages and the American Dream.",
  [("1C.5.a", "Explain how the dream is presented and why it fails."),
   ("1C.5.b", "Link the dream to the Depression and the American Dream.")]),
 ("omam.loneliness", "1C.6", "Loneliness, friendship and love", "prose-theme",
  "Isolation on the ranch and the rare relationships that resist it.",
  [("1C.6.a", "Show how most characters are lonely and why."),
   ("1C.6.b", "Discuss the forms of friendship, loyalty and love in the novel.")]),
 ("omam.power", "1C.7", "Power, prejudice and violence", "prose-theme",
  "Who holds power on the ranch, how outsiders are treated, and the novel's violence.",
  [("1C.7.a", "Explain how power and respect work in the ranch hierarchy."),
   ("1C.7.b", "Discuss prejudice (race, gender, age, disability) and violence.")]),
 ("omam.death", "1C.8", "Death, loss and fate", "prose-theme",
  "The chain of deaths, what characters lose, and the sense that the ending is inevitable.",
  [("1C.8.a", "Trace the deaths and how each foreshadows the next."),
   ("1C.8.b", "Discuss fate, responsibility, guilt and memory.")]),
 ("omam.setting", "1C.9", "Setting, nature and structure", "prose-theme",
  "Steinbeck's methods: locations, animals, foreshadowing and the circular, play-like structure.",
  [("1C.9.a", "Explain the importance of the pool, bunkhouse, Crooks's room and barn."),
   ("1C.9.b", "Analyse the use of animals, foreshadowing and structure.")]),
]


def build_spec():
    anth_subs = []
    for i, (sid, th) in enumerate(THEMES.items(), 1):
        anth_subs.append({
            "id": sid, "ref": f"1B.{i}", "title": th["title"], "summary": ANTH_SUMMARY[sid],
            "papers": ["p1"], "qtypes": ["anthology-pair", "anthology-open"],
            "points": [{"ref": POEMS[p]["ref"], "summary": f"{POEMS[p]['title']} ({POEMS[p]['poet']})"} for p in th["poems"]],
        })
    return {
        "subject": "english-literature",
        "code": "4ET1",
        "board": "Pearson Edexcel",
        "title": "Pearson Edexcel International GCSE (9-1) English Literature 4ET1",
        "short": "English Literature",
        "official_url": "https://qualifications.pearson.com/en/qualifications/edexcel-international-gcses/international-gcse-english-literature-2016.coursematerials.html",
        "spec_url": "https://qualifications.pearson.com/en/qualifications/edexcel-international-gcses/international-gcse-english-literature-2016.html",
        "papers": [{
            "id": "p1", "name": "Paper 1: Poetry and Modern Prose", "paper_code": "4ET1/01",
            "minutes": 120, "marks": 90, "calculator": None, "answer_style": "separate-booklet",
            "materials": "A clean copy of the anthology poems is provided for use with Section B.",
            "instructions": [
                "Use black ink or ball-point pen.",
                "Answer THREE questions: the question in Section A, ONE question from Section B and ONE question from Section C.",
                "Write your answers in the spaces provided; you may not need all the space.",
                "Copies of the set texts and of the anthology may not be brought into the examination.",
            ],
            "information": [
                "The total mark for this paper is 90.",
                "The number of marks for each question is shown in brackets: use it as a guide to timing.",
                "Section A is worth 20 marks, Section B 30 marks and Section C 40 marks.",
            ],
            "advice": [
                "Read each question carefully before you start to write.",
                "Plan your time: about 35 minutes for Section A, 40 for Section B and 45 for Section C.",
                "Check your answers if you have time at the end.",
            ],
            "sections": [
                {"id": "A", "title": "SECTION A: Unseen Poetry", "marks": 20,
                 "instructions": "Answer the question in this section. You should spend 35 minutes on this question.",
                 "slots": [{"label": "Question 1", "qtypes": ["unseen-poem"], "marks": 20}]},
                {"id": "B", "title": "SECTION B: Anthology Poetry", "marks": 30,
                 "instructions": "Answer ONE question from this section. You should spend 40 minutes on your chosen question.",
                 "slots": [{"label": "Question 2 (EITHER)", "qtypes": ["anthology-pair"], "marks": 30},
                           {"label": "Question 3 (OR)", "qtypes": ["anthology-open"], "marks": 30}]},
                {"id": "C", "title": "SECTION C: Modern Prose - Of Mice and Men, John Steinbeck", "marks": 40,
                 "instructions": "Answer ONE question from this section. You should spend 45 minutes on this section.",
                 "slots": [{"label": "Question 6 (EITHER)", "qtypes": ["prose-character"], "marks": 40},
                           {"label": "Question 7 (OR)", "qtypes": ["prose-theme"], "marks": 40}]},
            ],
        }],
        "qtypes": [
            {"id": "unseen-poem", "label": "Unseen poem essay", "marks": "20",
             "description": "Explore how the writer presents a given focus in a poem printed on the paper (AO2)."},
            {"id": "anthology-pair", "label": "Anthology comparison: two named poems", "marks": "30",
             "description": "Compare how two named anthology poems present a theme (AO2 + AO3)."},
            {"id": "anthology-open", "label": "Anthology comparison: one named poem + one of your choice", "marks": "30",
             "description": "Compare a named anthology poem with another poem you choose (AO2 + AO3)."},
            {"id": "prose-character", "label": "Of Mice and Men: character essay", "marks": "40",
             "description": "Essay on a character or relationship, with context (AO1 + AO4)."},
            {"id": "prose-theme", "label": "Of Mice and Men: theme or methods essay", "marks": "40",
             "description": "Essay on a theme, setting or Steinbeck's methods, with context (AO1 + AO4)."},
        ],
        "topics": [
            {"id": "unseen", "ref": "1A", "title": "Section A: Unseen poetry", "papers": ["p1"],
             "subtopics": [{"id": s, "ref": r, "title": t, "summary": su, "papers": ["p1"], "qtypes": ["unseen-poem"],
                            "points": [{"ref": a, "summary": b} for a, b in pts]} for s, r, t, su, pts in UNSEEN_SUBS]},
            {"id": "anthology", "ref": "1B", "title": "Section B: Anthology poetry (comparison)", "papers": ["p1"],
             "subtopics": anth_subs},
            {"id": "prose", "ref": "1C", "title": "Section C: Modern prose - Of Mice and Men", "papers": ["p1"],
             "subtopics": [{"id": s, "ref": r, "title": t, "summary": su, "papers": ["p1"], "qtypes": [qt],
                            "points": [{"ref": a, "summary": b} for a, b in pts]} for s, r, t, qt, su, pts in PROSE_SUBS]},
        ],
    }
