"""Shared helpers for the economics generator: context pools and a tiny template filler.

Template syntax used in the knowledge-base modules:
  {name} {name2} {city} {country} {ccy} {firm} {nation} {ncy} {ncity}  context values
  ({ncity} is a fictional city in {nation}; never pair a real {city} with a fictional {nation})
  {=var:a|b|c}   choose one option, print it and remember it as {var}
  {#var:lo-hi}   random integer in [lo, hi], printed and remembered as {var}
  {a|b|c}        anonymous choice
All contexts are fictional: invented people, invented firms, invented countries.
"""
import re

NAMES = ["Amira", "Kofi", "Priya", "Mateo", "Lena", "Tariq", "Mei", "Dmitri", "Aisha", "Rohan", "Sofia",
         "Kwame", "Yusuf", "Elena", "Hiroshi", "Zara", "Diego", "Nadia", "Farid", "Chloe", "Jonas", "Leila",
         "Arjun", "Ines", "Tomasz", "Ama", "Hassan", "Rina", "Oskar", "Thandiwe", "Bilal", "Marisol", "Kenji",
         "Fatima", "Pavel", "Nia", "Omar", "Svetlana", "Ravi", "Lucia"]

# city, country, currency prefix (literal dollar written as \$)
PLACES = [("Manchester", "the UK", "£"), ("Leeds", "the UK", "£"), ("Glasgow", "the UK", "£"), ("Lyon", "France", "€"),
          ("Valencia", "Spain", "€"), ("Porto", "Portugal", "€"), ("Munich", "Germany", "€"), ("Lisbon", "Portugal", "€"),
          ("Dublin", "Ireland", "€"), ("Penang", "Malaysia", "RM"), ("Kuala Lumpur", "Malaysia", "RM"), ("Dubai", "the UAE", "AED "),
          ("Doha", "Qatar", "QR "), ("Toronto", "Canada", "C\\$"), ("Auckland", "New Zealand", "NZ\\$"), ("Perth", "Australia", "A\\$"),
          ("Singapore", "Singapore", "S\\$"), ("Muscat", "Oman", "OMR "), ("Amman", "Jordan", "JD "), ("Zurich", "Switzerland", "CHF ")]

# fictional countries for macroeconomic data (so no invented 'facts' about real economies)
NATIONS = [("Tavrinia", "T\\$"), ("Belmora", "B£"), ("Corvana", "C€"), ("Eskaria", "E\\$"), ("Lumera", "L£"),
           ("Pradesia", "P\\$"), ("Quorvia", "Q€"), ("Sundara", "S£"), ("Valdoria", "V\\$"), ("Zentara", "Z£"),
           ("Marrenia", "M\\$"), ("Ostrelia", "O£"), ("Halvoria", "H€"), ("Rendova", "R\\$"), ("Kaleda", "K£"),
           ("Novaris", "N€"), ("Istrova", "I\\$"), ("Gallendra", "G£")]

# one fictional city per fictional country, used whenever a context names {nation} and a city ({ncity})
NATION_CITY = {"Tavrinia": "Port Tavrin", "Belmora": "Belhaven", "Corvana": "Corvane", "Eskaria": "Eskarion", "Lumera": "Lumeris",
               "Pradesia": "Pradon", "Quorvia": "Quorbridge", "Sundara": "Sundapur", "Valdoria": "Valdenburg", "Zentara": "Zentaro",
               "Marrenia": "Marrenford", "Ostrelia": "Ostrel", "Halvoria": "Halvik", "Rendova": "Rendport", "Kaleda": "Kaledon",
               "Novaris": "Novagrad", "Istrova": "Istrovik", "Gallendra": "Gallen"}

FIRM_A = ["Kora", "Velto", "Brightway", "Sunvale", "Orbis", "Tamarind", "Northgate", "Lumo", "Riverstone",
          "Cobalt", "Juniper", "Amberline", "Pinecrest", "Saffron", "Halcyon", "Meridian", "Zephyr", "Baobab",
          "Coral Bay", "Ironbark", "Silverleaf", "Kestrel", "Marlin", "Redwood"]
FIRM_B = ["Group", "Holdings", "Ltd", "& Co", "Enterprises", "Partners", "Company", "plc"]  # sector-neutral


def new_ctx(r):
    city, country, ccy = r.choice(PLACES)
    nation, ncy = r.choice(NATIONS)
    n1, n2 = r.sample(NAMES, 2)
    return {"name": n1, "name2": n2, "city": city, "country": country, "ccy": ccy,
            "firm": f"{r.choice(FIRM_A)} {r.choice(FIRM_B)}", "nation": nation, "ncy": ncy, "ncity": NATION_CITY[nation],
            "year": str(r.randint(2019, 2026))}


_TOK = re.compile(r"\{([=#]?)([^{}]*)\}")


def fill(t, ctx, r):
    """Fill a template string in place (ctx is updated with any defined vars)."""
    if t is None:
        return None

    def sub(m):
        kind, body = m.group(1), m.group(2)
        if kind == "=":
            var, opts = body.split(":", 1)
            if var not in ctx:
                ctx[var] = r.choice(opts.split("|"))
            return ctx[var]
        if kind == "#":
            var, rng_ = body.split(":", 1)
            if var not in ctx:
                lo, hi = rng_.split("-")
                ctx[var] = str(r.randint(int(lo), int(hi)))
            return ctx[var]
        if "|" in body:
            return r.choice(body.split("|"))
        if body in ctx:
            return ctx[body]
        return m.group(0)
    prev = None
    while prev != t:
        prev, t = t, _TOK.sub(sub, t)
    return t


def cap(s):
    return s[:1].upper() + s[1:] if s else s


def a_an(word):
    return ("an " if word[:1].lower() in "aeiou" else "a ") + word


LETTERS = "ABCD"


def mcq_parts(stem, correct, distractors, r, reasons=None, ao="AO1"):
    """Return (parts, rows, values) for a 4-option multiple-choice item, options shuffled."""
    opts = [(correct, None)] + list(zip(distractors, reasons or [None] * len(distractors)))
    r.shuffle(opts)
    k = [o[0] for o in opts].index(correct)
    lines = [f"Correct option: **{LETTERS[k]}** ({correct})"]
    for i, (txt, why) in enumerate(opts):
        if i == k:
            continue
        lines.append(f"{LETTERS[i]}: incorrect, {why}" if why else f"{LETTERS[i]}: incorrect")
    parts = [{"label": "", "text": stem, "marks": 1, "space": "mcq", "choices": [o[0] for o in opts]}]
    rows = [{"part": "", "answer": "\n".join(lines), "marks": "1", "ao": ao}]
    return parts, rows, {"key": LETTERS[k]}
