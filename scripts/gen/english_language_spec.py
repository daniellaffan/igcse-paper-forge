"""Builds data/spec/english-language.json: Pearson Edexcel International GCSE English Language A (4EA1),
Component 1 / Paper 1 only (Non-fiction Texts and Transactional Writing).

Refs: the specification does not number its content.  We use the component code (C1), the section
(A reading / B writing) and the assessment objective, e.g. C1.A.AO1.2; anthology texts are numbered in
the order the specification lists them (C1.A.AO2.T01-T10) and the six transactional forms in the order
the specification lists them (C1.B.F1-F6).  Summaries are our own plain-English wording.
"""
import json
from pathlib import Path

from english_language_anthology import ANTHOLOGY

ROOT = Path(__file__).resolve().parents[2]

QTYPES = [
    {"id": "select-two", "label": "Select two words or phrases (Q1)", "marks": "2",
     "description": "Pick two words or phrases from a few given lines of the unseen text."},
    {"id": "own-words", "label": "In your own words (Q2)", "marks": "4",
     "description": "Describe or explain what happens in a given section of the unseen text, in your own words."},
    {"id": "explain-five", "label": "Explain with brief quotations (Q3)", "marks": "5",
     "description": "Explain thoughts, feelings or what we learn from a given section of the unseen text."},
    {"id": "lang-structure", "label": "Language and structure, anthology text (Q4)", "marks": "12",
     "description": "Analyse how the writer of the anthology text uses language and structure for a stated effect."},
    {"id": "compare", "label": "Compare the two texts (Q5)", "marks": "22",
     "description": "Compare how the writers of the unseen and anthology texts present their ideas and perspectives."},
    {"id": "reading-section", "label": "Complete Section A (Q1-Q5)", "marks": "45",
     "description": "One unseen text and one anthology text with all five reading questions, as in the real paper."},
    {"id": "transactional", "label": "Transactional writing task", "marks": "45",
     "description": "One writing task with a given form, audience and purpose (AO4 27 + AO5 18)."},
    {"id": "transactional-choice", "label": "Section B: choice of two tasks", "marks": "45",
     "description": "Two transactional tasks in different forms; the candidate answers one."},
]

FORMS = [
    ("article", "C1.B.F1", "Article for a magazine or newspaper",
     "Write an article with a headline and an engaging opening that informs, argues or entertains readers of a named publication."),
    ("speech", "C1.B.F2", "Speech",
     "Write the text of a speech for a named audience, using direct address and rhetorical techniques."),
    ("letter", "C1.B.F3", "Letter",
     "Write a formal or informal letter to a named reader, with the right greeting, tone and sign-off."),
    ("guide", "C1.B.F4", "Guide",
     "Write a clear, well-organised guide that explains how to do something or what to know, for a named reader."),
    ("review", "C1.B.F5", "Review",
     "Write a review that describes and judges an event, place, product or experience for readers of a publication or website."),
    ("leaflet", "C1.B.F6", "Text for a leaflet",
     "Write the text of a leaflet that informs or advises a target audience, using headings and other organisational features."),
]


def build():
    papers = [{
        "id": "p1", "name": "Paper 1: Non-fiction Texts and Transactional Writing", "paper_code": "4EA1/01",
        "minutes": 135, "marks": 90, "calculator": None, "answer_style": "in-booklet",
        "materials": "Insert (Text One). Text Two is from Part 1 of the Anthology: use your own copy, as it is not reprinted in this practice paper.",
        "instructions": [
            "Use black ink or ball-point pen.",
            "Answer ALL questions in Section A and ONE question from Section B.",
            "Write your answers in the spaces provided; there may be more space than you need.",
        ],
        "information": [
            "The total mark for this paper is 90.",
            "The marks for each question are shown in brackets: use them to judge how long to spend on each question.",
            "In Section B you will be assessed on your vocabulary, spelling, punctuation and grammar as well as on your writing for the task.",
            "Dictionaries may not be used.",
        ],
        "advice": [
            "Read each question carefully before you begin your answer.",
            "Spend about 1 hour 30 minutes on Section A and about 45 minutes on Section B.",
            "Leave time at the end to check your answers.",
        ],
        "sections": [
            {"id": "A", "title": "SECTION A: Reading",
             "instructions": "Answer ALL questions in this section. You should spend about 1 hour and 30 minutes on this section. The questions are based on Text One (in the Insert) and Text Two (from Part 1 of the Anthology).",
             "marks": 45,
             "slots": [{"label": "Questions 1-5", "qtypes": ["reading-section"], "marks": 45}]},
            {"id": "B", "title": "SECTION B: Transactional Writing",
             "instructions": "Answer ONE question in this section. You should spend about 45 minutes on your chosen question.",
             "marks": 45,
             "slots": [{"label": "Questions 6-7", "qtypes": ["transactional-choice"], "marks": 45}]},
        ],
    }]
    topics = [
        {"id": "reading-retrieval", "ref": "C1.A.AO1", "title": "Reading the unseen text: retrieval and interpretation (AO1)",
         "papers": ["p1"], "subtopics": [
            {"id": "el.ao1.select", "ref": "C1.A.AO1.1", "title": "Selecting words and phrases",
             "summary": "Find two short quotations that answer the question, taken only from the lines given.",
             "papers": ["p1"], "qtypes": ["select-two"], "points": [
                {"ref": "C1.A.AO1.1a", "summary": "Stay inside the line numbers given in the question."},
                {"ref": "C1.A.AO1.1b", "summary": "Copy words or phrases exactly; no explanation is needed."}]},
            {"id": "el.ao1.describe", "ref": "C1.A.AO1.2", "title": "Describing and explaining in your own words",
             "summary": "Make four separate, accurate points about a section of the text, rephrased in your own words.",
             "papers": ["p1"], "qtypes": ["own-words"], "points": [
                {"ref": "C1.A.AO1.2a", "summary": "Pick out the key events, facts or ideas in a given section."},
                {"ref": "C1.A.AO1.2b", "summary": "Rephrase them rather than copying long chunks of the text."}]},
            {"id": "el.ao1.explain", "ref": "C1.A.AO1.3", "title": "Explaining thoughts, feelings and ideas",
             "summary": "Explain five points about what a writer thinks, feels or shows, backed by short quotations.",
             "papers": ["p1"], "qtypes": ["explain-five"], "points": [
                {"ref": "C1.A.AO1.3a", "summary": "Interpret what the writer thinks and feels, not just what happens."},
                {"ref": "C1.A.AO1.3b", "summary": "Support points with short, well-chosen quotations."}]},
         ]},
        {"id": "reading-language", "ref": "C1.A.AO2", "title": "Language and structure in the anthology texts (AO2)",
         "papers": ["p1"], "subtopics": [
            {"id": "el.ao2.anthology", "ref": "C1.A.AO2.1", "title": "Analysing language and structure in a Part 1 anthology text",
             "summary": "Explain how a writer's word choices, imagery, sentences and organisation create a stated effect on the reader.",
             "papers": ["p1"], "qtypes": ["lang-structure"], "points": [
                {"ref": a["ref"], "summary": f"{a['author']}, {a['title']}: {a['theme']}."} for a in ANTHOLOGY]},
         ]},
        {"id": "reading-comparison", "ref": "C1.A.AO3", "title": "Comparing the unseen and anthology texts (AO3)",
         "papers": ["p1"], "subtopics": [
            {"id": "el.ao3.compare", "ref": "C1.A.AO3.1", "title": "Comparing writers' ideas and perspectives",
             "summary": "Compare what two writers think and feel about a shared subject and how they get it across.",
             "papers": ["p1"], "qtypes": ["compare"], "points": [
                {"ref": "C1.A.AO3.1a", "summary": "Find similarities and differences in the writers' ideas, attitudes and experiences."},
                {"ref": "C1.A.AO3.1b", "summary": "Compare how they present them: tone, language and structure."},
                {"ref": "C1.A.AO3.1c", "summary": "Keep references balanced across both texts."}]},
         ]},
        {"id": "reading-section", "ref": "C1.A", "title": "Section A: complete reading section",
         "papers": ["p1"], "subtopics": [
            {"id": "el.reading.section", "ref": "C1.A.1", "title": "All five reading questions on one pair of texts",
             "summary": "Practise the whole of Section A: three questions on the unseen text, one on the anthology text and the comparison.",
             "papers": ["p1"], "qtypes": ["reading-section"], "points": [
                {"ref": "C1.A.1a", "summary": "Manage 90 minutes across 45 marks, giving most time to the 12- and 22-mark questions."}]},
         ]},
        {"id": "writing", "ref": "C1.B", "title": "Section B: Transactional writing (AO4, AO5)",
         "papers": ["p1"], "subtopics": [
            {"id": f"el.writing.{fid}", "ref": ref, "title": title, "summary": summ, "papers": ["p1"],
             "qtypes": ["transactional"], "points": [
                {"ref": ref + "a", "summary": "Match form, tone and register to the stated audience and purpose (AO4)."},
                {"ref": ref + "b", "summary": "Write accurately with varied vocabulary, sentences and paragraphs (AO5)."}]}
            for fid, ref, title, summ in FORMS
         ] + [
            {"id": "el.writing.choice", "ref": "C1.B.1", "title": "Choosing between two tasks",
             "summary": "Pick the better of two tasks for you, then plan and write one response in about 45 minutes.",
             "papers": ["p1"], "qtypes": ["transactional-choice"], "points": [
                {"ref": "C1.B.1a", "summary": "Choose the task whose form and topic you can develop most fully."}]},
         ]},
    ]
    spec = {
        "subject": "english-language", "code": "4EA1", "board": "Pearson Edexcel",
        "title": "Pearson Edexcel International GCSE English Language A (4EA1)", "short": "English Language A",
        "official_url": "https://qualifications.pearson.com/en/qualifications/edexcel-international-gcses/international-gcse-english-language-a-2016.coursematerials.html#filterQuery=category:Pearson-UK:Category%2FExam-materials",
        "spec_url": "https://qualifications.pearson.com/en/qualifications/edexcel-international-gcses/international-gcse-english-language-a-2016.html",
        "papers": papers, "qtypes": QTYPES, "topics": topics,
    }
    out = ROOT / "data" / "spec" / "english-language.json"
    out.write_text(json.dumps(spec, ensure_ascii=False, indent=1))
    return spec


if __name__ == "__main__":
    build()
    print("wrote spec")
