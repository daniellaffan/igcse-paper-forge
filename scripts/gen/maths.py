#!/usr/bin/env python3
"""Deterministic generator for the 4MA1 Higher maths bank.

    .venv/bin/python scripts/gen/maths.py

Writes data/spec/maths.json (via maths_spec), data/reference/maths-formulae-higher.json
and data/bank/maths/<topic>.json.  Every template lives in a maths_<area>.py module and
registers itself with @tpl(subtopic, qtype, n).  Each template is run with seeds
"<template>-<k>" until it has produced n distinct questions.
"""
import json
import random
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from common import Bank, part_marks  # noqa: E402
import maths_spec  # noqa: E402
import maths_util as U  # noqa: E402
import maths_number  # noqa: E402,F401
import maths_algebra  # noqa: E402,F401
import maths_functions  # noqa: E402,F401
import maths_geometry  # noqa: E402,F401
import maths_geometry2  # noqa: E402,F401
import maths_stats  # noqa: E402,F401
import maths_reference  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
TOKEN = re.compile(r"\b([MABPC])(\d+)\b")
AO = {"number": "AO1", "algebra": "AO1", "functions": "AO1", "geometry": "AO2", "vectors": "AO2", "stats": "AO3"}


def leaf(parts, pre=""):
    out = []
    for p in parts:
        lab = pre + (p.get("label") or "")
        if p.get("parts"):
            out += leaf(p["parts"], lab)
        else:
            out.append((re.sub(r"[^a-z0-9]", "", lab.lower()), p["marks"]))
    return out


def check_marks(q, name):
    lv = leaf(q["parts"])
    got = Counter()
    for r in q["markscheme"]["rows"]:
        got[re.sub(r"[^a-z0-9]", "", r["part"].lower())] += sum(int(n) for _, n in TOKEN.findall(r["marks"])) \
            if TOKEN.findall(r["marks"]) else int(r["marks"])
    if len(lv) == 1 and lv[0][0] == "":
        assert sum(got.values()) == lv[0][1], (name, lv, got)
    else:
        for lab, m in lv:
            assert got[lab] == m, (name, lab, m, dict(got))


def sig(q):
    bits = [q.get("intro") or ""]

    def walk(ps):
        for p in ps:
            bits.append(p["text"])
            walk(p.get("parts", []) or [])
    walk(q["parts"])
    for f in q.get("figures") or []:
        for r in f.get("rows", []) or []:
            bits.extend(r)
    bits.append(json.dumps(q["answer"]["values"], sort_keys=True))
    t = " ".join(bits).lower()
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9%.\-+=/ ]", " ", t)).strip()


def main():
    spec = maths_spec.build()
    maths_reference.build()
    refs = set()
    subs = {}
    for t in spec["topics"]:
        for st in t["subtopics"]:
            subs[st["id"]] = (t["id"], st)
            refs.add(st["ref"])
            refs.update(p["ref"] for p in st["points"])
    bank = Bank("maths")
    seen = set()
    cells = Counter()
    for t in U.TEMPLATES:
        tid, st = subs[t["sub"]]
        assert t["qtype"] in st["qtypes"], (t["name"], t["qtype"], t["sub"])
        made, k = 0, 0
        while made < t["n"] and k < t["n"] * 25:
            r = random.Random(f"{t['name']}-{k}")
            k += 1
            q = t["f"](r)
            if q is None:
                continue
            s = (t["sub"], sig(q))
            if s in seen:
                continue
            check_marks(q, t["name"])
            for ref in q["spec_refs"]:
                assert ref in refs, (t["name"], ref)
            seen.add(s)
            made += 1
            short = tid.split(".")[1]
            bank.add(topic=tid.split(".")[1], subtopic=t["sub"], qtype=t["qtype"], command_word=q["command_word"],
                     difficulty=q["difficulty"], parts=q["parts"], markscheme=q["markscheme"],
                     spec_refs=q["spec_refs"], paper=["1h", "2h"], ao=[AO[short]], template=t["name"].replace("_", "-"),
                     intro=q.get("intro"), figures=q.get("figures"), calculator=True, answer=q["answer"],
                     tags=q.get("tags"), id=None)
            cells[(t["sub"], t["qtype"])] += 1
        if made < t["n"]:
            print(f"WARN template {t['name']} produced only {made}/{t['n']}")
    # topic ids in the bank must be spec topic ids
    for topic, qs in list(bank.by_topic.items()):
        for q in qs:
            q["topic"] = "maths." + topic
    thin = [(s, qt, cells[(s, qt)]) for s, (tid, st) in subs.items() for qt in st["qtypes"] if cells[(s, qt)] < 12]
    for x in thin:
        print("THIN", x)
    bank.save()
    d = Counter(q["difficulty"] for qs in bank.by_topic.values() for q in qs)
    print("templates", len(U.TEMPLATES), "difficulty", dict(d))


if __name__ == "__main__":
    main()
