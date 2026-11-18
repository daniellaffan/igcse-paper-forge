"""Builds data/spec/spanish.json for Cambridge IGCSE Spanish (Foreign Language) 0530,
syllabus for examination in 2025, 2026 and 2027.

Refs: the syllabus (664626) groups content into five topic areas A-E, each listing
example sub-topics as bullets (no printed numbers).  We number sub-topics by area
letter and bullet order (A1 ... E2, 19 in all) and split their bracketed examples
into points (A2.a, A2.b ...).  Summaries are our own plain-English wording.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

QTYPES = [
    # Paper 1 Listening
    {"id": "l-short", "label": "Listening: short recordings, picture choice", "marks": "8",
     "description": "Eight one-line exchanges in a single everyday setting; choose the picture (A-D) that matches the key word."},
    {"id": "l-announce", "label": "Listening: announcement, multiple choice", "marks": "6",
     "description": "A short public announcement or guide's talk with a pause; six A-D items on facts, times, places and rules."},
    {"id": "l-match", "label": "Listening: match speakers to statements", "marks": "5",
     "description": "Five young people speak in turn; match each to one of six paraphrased statements (one is not needed)."},
    {"id": "l-interview-3", "label": "Listening: two-part interview (A-C)", "marks": "9",
     "description": "A longer interview in two parts; nine three-option items on information, opinions and reasons."},
    {"id": "l-interview-4", "label": "Listening: interview (A-D)", "marks": "6",
     "description": "An interview with a pause; six four-option items testing detail, explanation and attitude."},
    {"id": "l-multi", "label": "Listening: choose two statements", "marks": "6",
     "description": "An interview heard in three sections; in each, choose the two true statements from five (2 marks each)."},
    # Paper 2 Reading
    {"id": "r-pictures", "label": "Reading: match sentences to pictures", "marks": "5",
     "description": "Five short sentences; choose the matching picture from six (A-F)."},
    {"id": "r-signs", "label": "Reading: signs and notices", "marks": "5",
     "description": "Eight public signs in one setting; match five sentences that paraphrase what someone wants or must do."},
    {"id": "r-text-mcq", "label": "Reading: message or e-mail, multiple choice", "marks": "7",
     "description": "A personal e-mail or message (about 150-180 words); seven three-option items."},
    {"id": "r-short", "label": "Reading: text with short answers in Spanish", "marks": "12",
     "description": "A first-person blog or account (about 220-260 words); short answers in Spanish, changing person and tense."},
    {"id": "r-match-ads", "label": "Reading: match people to adverts", "marks": "5",
     "description": "Five people describe what they need; choose the best of eight adverts for each (three are not needed)."},
    {"id": "r-long", "label": "Reading: article with short answers in Spanish", "marks": "11",
     "description": "A longer journalistic interview article (about 280-340 words); answers in Spanish, inference and manipulation."},
    # Paper 3 Speaking
    {"id": "s-roleplay", "label": "Speaking: role play", "marks": "10",
     "description": "Candidate card with a scenario; five teacher questions (one past, one future/conditional), 2 marks each."},
    {"id": "s-conversation", "label": "Speaking: two topic conversations", "marks": "30",
     "description": "Two 4-minute conversations (one from areas A/B, one from C/D/E), five scripted questions each with alternatives; Communication 15 + Quality of Language 15."},
    # Paper 4 Writing
    {"id": "w-form", "label": "Writing: complete a form", "marks": "5",
     "description": "Fill five gaps in a form with single words or short phrases in Spanish."},
    {"id": "w-short", "label": "Writing: 80-90 words", "marks": "12",
     "description": "Four bullet prompts (five tasks); one levels grid out of 12."},
    {"id": "w-extended", "label": "Writing: 130-140 words", "marks": "28",
     "description": "E-mail, blog or article with five bullet prompts across time frames; Task completion 10, Range 10, Accuracy 8."},
]

CORE = ["l-short", "l-announce", "l-match", "l-interview-3", "l-interview-4", "l-multi",
        "r-pictures", "r-text-mcq", "r-short", "r-long", "w-form"]
TALK = ["s-conversation", "w-short", "w-extended"]

# ref, id, title, summary, extra qtypes, points
AREAS = [
 ("A", "spanish.a", "Everyday activities", [
  ("A1", "time", "Time expressions",
   "Telling the time, days, dates, months and seasons, and talking about when things happen.",
   ["r-signs", "s-roleplay"],
   [("A1.a", "Clock times, the 24-hour clock and timetables."), ("A1.b", "Days of the week, dates and months."),
    ("A1.c", "Seasons and expressions of frequency and duration.")]),
  ("A2", "food", "Food and drink",
   "Meals, fruit and vegetables, buying food and what makes a healthy diet.",
   ["r-signs", "r-match-ads", "s-roleplay"] + TALK,
   [("A2.a", "Meals and mealtimes at home."), ("A2.b", "Fruit, vegetables and everyday food shopping."),
    ("A2.c", "Healthy and unhealthy eating habits.")]),
  ("A3", "health", "The human body and health",
   "Parts of the body, illnesses and accidents, seeing a doctor, and keeping fit and well.",
   ["r-signs", "r-match-ads", "s-roleplay"] + TALK,
   [("A3.a", "Parts of the body and describing pain."), ("A3.b", "Illness, accidents and medical help."),
    ("A3.c", "Healthy lifestyle: sleep, exercise and stress.")]),
  ("A4", "transport", "Travel and transport",
   "Ways of getting about, tickets and timetables, and asking for and following directions.",
   ["r-signs", "s-roleplay"] + TALK,
   [("A4.a", "Means of transport and their pros and cons."), ("A4.b", "Buying tickets and using timetables."),
    ("A4.c", "Asking for and giving directions.")]),
 ]),
 ("B", "spanish.b", "Personal and social life", [
  ("B1", "self", "Self, family and friends",
   "Describing yourself, your family, friends and pets, and how you get on with people.",
   ["s-roleplay"] + TALK,
   [("B1.a", "Personal details, appearance and personality."), ("B1.b", "Family members and pets."),
    ("B1.c", "Friends and relationships with others.")]),
  ("B2", "home", "In the home",
   "Rooms, furniture and furnishings, the garden, household appliances, daily routine and chores.",
   ["r-signs", "r-match-ads", "s-roleplay"] + TALK,
   [("B2.a", "Rooms: living room, kitchen, bedroom, bathroom, garden."), ("B2.b", "Furniture, furnishings and household appliances."),
    ("B2.c", "Daily routine and helping at home.")]),
  ("B3", "colours", "Colours",
   "Naming colours and using them to describe things (agreement of colour adjectives).",
   ["ONLY", "l-short", "r-pictures", "w-form"],
   [("B3.a", "Colours and colour adjectives with agreement.")]),
  ("B4", "clothes", "Clothes and accessories",
   "Clothes, shoes and accessories, buying them, sizes and prices, uniform and fashion.",
   ["r-signs", "r-match-ads", "s-roleplay"] + TALK,
   [("B4.a", "Items of clothing, shoes and accessories."), ("B4.b", "Buying clothes: sizes, prices, paying."),
    ("B4.c", "Fashion, uniform and opinions about clothes.")]),
  ("B5", "leisure", "Leisure time",
   "Things to do in free time, hobbies, sport, music, cinema, going out and holidays.",
   ["r-signs", "r-match-ads", "s-roleplay"] + TALK,
   [("B5.a", "Things to do and going out."), ("B5.b", "Hobbies, music, cinema and reading."),
    ("B5.c", "Sport and physical activities.")]),
 ]),
 ("C", "spanish.c", "The world around us", [
  ("C1", "people-places", "People and places",
   "Continents, countries and nationalities, compass points, and describing where people live and come from.",
   ["s-roleplay"] + TALK,
   [("C1.a", "Continents, countries and nationalities."), ("C1.b", "Compass points and location."),
    ("C1.c", "Describing a region and the people who live there.")]),
  ("C2", "environment", "The natural world, the environment, the climate and the weather",
   "Weather and climate, landscapes and animals, and protecting the environment.",
   ["r-signs", "s-roleplay"] + TALK,
   [("C2.a", "Weather and climate."), ("C2.b", "Landscapes, wildlife and the countryside."),
    ("C2.c", "Environmental problems and what people can do.")]),
  ("C3", "technology", "Communications and technology",
   "The digital world: phones, the internet and social media, messages and documents, benefits and risks.",
   ["r-match-ads", "s-roleplay"] + TALK,
   [("C3.a", "The digital world and everyday devices."), ("C3.b", "Documents, texts and online communication."),
    ("C3.c", "Advantages, dangers and screen time.")]),
  ("C4", "built", "The built environment",
   "Buildings and services, urban areas, the local area and shopping.",
   ["r-signs", "r-match-ads", "s-roleplay"] + TALK,
   [("C4.a", "Buildings and services in town."), ("C4.b", "Urban areas and the local area."),
    ("C4.c", "Shops, shopping and paying.")]),
  ("C5", "measurements", "Measurements",
   "Size, shape, length, weight and quantity.",
   ["ONLY", "l-short", "r-pictures"],
   [("C5.a", "Size and shape."), ("C5.b", "Quantities, weights and lengths.")]),
  ("C6", "materials", "Materials",
   "What things are made of: wood, metal, plastic, glass, paper, cotton and so on.",
   ["ONLY", "l-short", "r-pictures"],
   [("C6.a", "Common materials and saying what things are made of.")]),
 ]),
 ("D", "spanish.d", "The world of work", [
  ("D1", "education", "Education",
   "Learning institutions, education and training, the classroom, learning tools, subjects and studying.",
   ["r-signs", "s-roleplay"] + TALK,
   [("D1.a", "School, subjects and the classroom."), ("D1.b", "Learning tools, studying and exams."),
    ("D1.c", "Education and training after school.")]),
  ("D2", "work", "Work",
   "Jobs and careers, the workplace, part-time work and plans for the future.",
   ["r-signs", "r-match-ads", "s-roleplay"] + TALK,
   [("D2.a", "Jobs and careers."), ("D2.b", "The workplace and part-time work."),
    ("D2.c", "Future plans and ambitions.")]),
 ]),
 ("E", "spanish.e", "The international world", [
  ("E1", "countries", "Countries, nationalities and languages",
   "Visiting other countries, nationalities, learning and using languages, and travelling abroad.",
   ["r-signs", "r-match-ads", "s-roleplay"] + TALK,
   [("E1.a", "Countries and nationalities."), ("E1.b", "Languages and learning them."),
    ("E1.c", "Travelling and staying abroad.")]),
  ("E2", "culture", "Culture, customs, faiths and celebrations",
   "Festivals, traditions, customs and faiths, and how special days are celebrated.",
   ["s-roleplay"] + TALK,
   [("E2.a", "Festivals and celebrations."), ("E2.b", "Customs, traditions and faiths."),
    ("E2.c", "Family celebrations and presents.")]),
 ]),
]


def subtopics():
    """Yield (topic_id, ref, subtopic_id, title, qtypes)."""
    for area, tid, _t, subs in AREAS:
        for ref, slug, title, _s, extra, _p in subs:
            qts = [] if extra[:1] == ["ONLY"] else list(CORE)
            for q in extra:
                if q == "ONLY":
                    continue
                if q not in qts:
                    qts.append(q)
            order = [q["id"] for q in QTYPES]
            qts.sort(key=order.index)
            yield tid, ref, f"{tid}.{slug}", title, qts


SPOKEN = ["Answer all questions.", "You must answer in Spanish.", "Dictionaries are not allowed."]


def build():
    topics = []
    st_q = {sid: qts for _t, _r, sid, _ti, qts in subtopics()}
    for area, tid, title, subs in AREAS:
        sts = []
        for ref, slug, stitle, summ, _extra, pts in subs:
            sid = f"{tid}.{slug}"
            qts = st_q[sid]
            papers = sorted({{"l": "p1", "r": "p2", "s": "p3", "w": "p4"}[q[0]] for q in qts})
            sts.append({"id": sid, "ref": ref, "title": stitle, "summary": summ, "papers": papers,
                        "qtypes": qts, "points": [{"ref": r, "summary": s} for r, s in pts]})
        topics.append({"id": tid, "ref": area, "title": f"Area {area}: {title}",
                       "papers": ["p1", "p2", "p3", "p4"], "subtopics": sts})
    papers = [
        {"id": "p1", "name": "Paper 1 Listening", "paper_code": "0530/11", "minutes": 50, "marks": 40,
         "calculator": None, "answer_style": "in-booklet",
         "materials": "Multiple choice answer sheet; soft pencil; soft clean eraser.",
         "instructions": ["There are six exercises. Answer all questions.",
                          "You will hear each recording twice. Read the questions while you wait.",
                          "Mark one letter for each question, except in the final exercise, where you mark two letters for each question.",
                          "At the end you have 6 minutes to transfer your answers.", "Dictionaries are not allowed."],
         "information": ["The total mark for this paper is 40.",
                         "Each correct answer scores one mark.",
                         "The paper lasts about 50 minutes, including 6 minutes' transfer time."],
         "advice": ["Use the reading time to predict what you will hear.",
                    "Many correct answers paraphrase what is said: listen for meaning, not for the same words."],
         "sections": [{"id": "listening", "title": "Listening exercises", "slots": [
             {"label": "Questions 1-8", "qtypes": ["l-short"], "marks": 8},
             {"label": "Questions 9-14", "qtypes": ["l-announce"], "marks": 6},
             {"label": "Questions 15-19", "qtypes": ["l-match"], "marks": 5},
             {"label": "Questions 20-28", "qtypes": ["l-interview-3"], "marks": 9},
             {"label": "Questions 29-34", "qtypes": ["l-interview-4"], "marks": 6},
             {"label": "Questions 35-37", "qtypes": ["l-multi"], "marks": 6}]}]},
        {"id": "p2", "name": "Paper 2 Reading", "paper_code": "0530/21", "minutes": 60, "marks": 45,
         "calculator": None, "answer_style": "in-booklet",
         "instructions": ["Answer all questions.", "Write your answer to each question in the space provided.",
                          "Where a question asks for an answer in Spanish, write in Spanish.",
                          "Dictionaries are not allowed."],
         "information": ["The total mark for this paper is 45.",
                         "The number of marks for each question or part question is shown in brackets [ ]."],
         "advice": ["The questions follow the order of the text.",
                    "Keep written answers short and precise; copying whole sentences can add wrong information.",
                    "Answers about another person need the third person (él/ella), not 'yo'."],
         "sections": [{"id": "reading", "title": "Reading", "slots": [
             {"label": "Question 1", "qtypes": ["r-pictures"], "marks": 5},
             {"label": "Question 2", "qtypes": ["r-signs"], "marks": 5},
             {"label": "Question 3", "qtypes": ["r-text-mcq"], "marks": 7},
             {"label": "Question 4", "qtypes": ["r-short"], "marks": 12},
             {"label": "Question 5", "qtypes": ["r-match-ads"], "marks": 5},
             {"label": "Question 6", "qtypes": ["r-long"], "marks": 11}]}]},
        {"id": "p3", "name": "Paper 3 Speaking", "paper_code": "0530/03", "minutes": 10, "marks": 40,
         "calculator": None, "answer_style": "answer-lines",
         "materials": "Candidate card. 10 minutes' preparation time (no notes).",
         "instructions": ["Answer all questions. You must respond in Spanish.",
                          "You have 10 minutes to prepare the role play on your candidate card. You may not make notes.",
                          "The test has a role play (about 2 minutes) and two topic conversations (4 minutes each).",
                          "Dictionaries are not allowed."],
         "information": ["The total mark for this test is 40: role play 10, topic conversations 30.",
                         "The role play is marked out of 2 for each of five tasks.",
                         "The two conversations are marked together: Communication 15, Quality of Language 15."],
         "advice": ["In the role play a short, accurate answer gets full marks: listen for the tense of each question.",
                    "In the conversations, give opinions and reasons and use past, present and future time frames."],
         "sections": [{"id": "speaking", "title": "Speaking test", "slots": [
             {"label": "Role play", "qtypes": ["s-roleplay"], "marks": 10},
             {"label": "Topic conversations 1 and 2", "qtypes": ["s-conversation"], "marks": 30}]}]},
        {"id": "p4", "name": "Paper 4 Writing", "paper_code": "0530/41", "minutes": 60, "marks": 45,
         "calculator": None, "answer_style": "in-booklet",
         "instructions": ["Answer three questions: Question 1, Question 2 and one task for Question 3.",
                          "Write your answers in Spanish in the spaces provided.", "Dictionaries are not allowed."],
         "information": ["The total mark for this paper is 45.",
                         "The number of marks for each question or part question is shown in brackets [ ]."],
         "advice": ["Answer every bullet point, in the tense the bullet uses.",
                    "Keep to the word counts: 80-90 words for Question 2 and 130-140 words for Question 3."],
         "sections": [{"id": "writing", "title": "Writing", "slots": [
             {"label": "Question 1", "qtypes": ["w-form"], "marks": 5},
             {"label": "Question 2", "qtypes": ["w-short"], "marks": 12},
             {"label": "Question 3", "qtypes": ["w-extended"], "marks": 28}]}]},
    ]
    spec = {
        "subject": "spanish", "code": "0530", "board": "Cambridge International",
        "title": "Cambridge IGCSE Spanish (Foreign Language) 0530", "short": "Spanish",
        "official_url": "https://www.cambridgeinternational.org/programmes-and-qualifications/cambridge-igcse-spanish-foreign-language-0530/past-papers/",
        "spec_url": "https://www.cambridgeinternational.org/programmes-and-qualifications/cambridge-igcse-spanish-foreign-language-0530/",
        "papers": papers, "qtypes": QTYPES, "topics": topics,
    }
    out = ROOT / "data" / "spec" / "spanish.json"
    out.write_text(json.dumps(spec, ensure_ascii=False, indent=1))
    return spec


if __name__ == "__main__":
    build()
    print("wrote data/spec/spanish.json")
