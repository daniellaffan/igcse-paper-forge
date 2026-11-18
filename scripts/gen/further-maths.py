#!/usr/bin/env python3
"""Deterministic generator for the 4PM1 Further Pure Mathematics bank.

    .venv/bin/python scripts/gen/further-maths.py

Writes data/spec/further-maths.json, data/reference/further-maths-formulae.json
and data/bank/further-maths/<topic>.json.  Templates live in
further_maths_<area>.py modules and register with @tpl(subtopic, qtype, n).
Each template is run with seeds "<template>-<k>" until it has produced n
distinct questions.  Every answer is computed with sympy inside the template.
"""
import random
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from common import Bank  # noqa: E402
import further_maths_spec as SPEC  # noqa: E402
import further_maths_util as U  # noqa: E402
import further_maths_alg  # noqa: E402,F401
import further_maths_series  # noqa: E402,F401
import further_maths_geom  # noqa: E402,F401
import further_maths_calc  # noqa: E402,F401
import further_maths_trig  # noqa: E402,F401

TOKEN = re.compile(r"\b([MABPC])(\d+)\b")
AO = {"short": ["AO1"], "multi-part": ["AO1", "AO3"], "show-that": ["AO3", "AO1"], "graph": ["AO1", "AO3"],
      "applied": ["AO2", "AO3"]}


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
        toks = TOKEN.findall(r["marks"])
        assert toks, (name, r)
        got[re.sub(r"[^a-z0-9]", "", r["part"].lower())] += sum(int(v) for _, v in toks)
    if len(lv) == 1 and lv[0][0] == "":
        assert sum(got.values()) == lv[0][1], (name, lv, dict(got))
    else:
        for lab, m in lv:
            assert got[lab] == m, (name, lab, m, dict(got))
        assert set(got) <= {lab for lab, _ in lv}, (name, dict(got), lv)


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
    t = " ".join(bits).lower()
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9%.\-+=/ ]", " ", t)).strip()


def main(only=None):
    spec = SPEC.build()
    refs, subs = set(), {}
    for tp in spec["topics"]:
        for st in tp["subtopics"]:
            subs[st["id"]] = (tp["id"], st)
            refs.update(p["ref"] for p in st["points"])
    bank = Bank("further-maths")
    seen = set()
    cells = Counter()
    variants = set()
    for tm in U.TEMPLATES:
        if only and not any(o in tm["name"] for o in only):
            continue
        tid, st = subs[tm["sub"]]
        assert tm["qtype"] in st["qtypes"], (tm["name"], tm["qtype"], tm["sub"])
        made, kk = 0, 0
        while made < tm["n"] and kk < tm["n"] * 30:
            r = random.Random(f"{tm['name']}-{kk}")
            kk += 1
            q = tm["f"](r)
            if q is None:
                continue
            s = (tm["sub"], sig(q))
            if s in seen:
                continue
            check_marks(q, tm["name"])
            for ref in q["spec_refs"]:
                assert ref in refs, (tm["name"], ref)
            seen.add(s)
            made += 1
            tname = tm["name"].replace("_", "-")
            if q.get("variant"):
                tname += "-" + q["variant"]
            variants.add(tname)
            bank.add(topic=tid, subtopic=tm["sub"], qtype=tm["qtype"], command_word=q["command_word"],
                     difficulty=q["difficulty"], parts=q["parts"], markscheme=q["markscheme"],
                     spec_refs=q["spec_refs"], paper=["p1", "p2"], ao=q.get("ao") or AO[tm["qtype"]],
                     template=tname, intro=q.get("intro"), figures=q.get("figures"), calculator=True,
                     answer=q["answer"], tags=q.get("tags"),
                     id=f"further-maths.{tm['name'].replace('_', '-')}.{made:04d}")
            cells[(tm["sub"], tm["qtype"])] += 1
        if made < tm["n"]:
            print(f"WARN template {tm['name']} produced only {made}/{tm['n']}")
    if not only:
        for sid, (tid, st) in subs.items():
            for qt in st["qtypes"]:
                if cells[(sid, qt)] < 12:
                    print("THIN", sid, qt, cells[(sid, qt)])
    # bank files are named by the short topic id
    for topic in list(bank.by_topic):
        bank.by_topic[topic.split(".", 1)[1]] = bank.by_topic.pop(topic)
    total = bank.save()
    d = Counter(q["difficulty"] for qs in bank.by_topic.values() for q in qs)
    qt = Counter(q["qtype"] for qs in bank.by_topic.values() for q in qs)
    print("template functions", len([t for t in U.TEMPLATES]), "variants", len(variants))
    print("difficulty", dict(d), "qtypes", dict(qt), "total", total)


if __name__ == "__main__":
    main(sys.argv[1:] or None)
