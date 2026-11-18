#!/usr/bin/env python3
"""Deterministic generator for the 4CH1 chemistry bank.

    .venv/bin/python scripts/gen/chemistry.py

Writes data/spec/chemistry.json and data/reference/chemistry-periodic-table.json
(chemistry_spec), then data/bank/chemistry/<topic>.json.  Templates live in
chemistry_t1..t4 (one module per specification topic) and register with
@tpl(subtopic, qtype, n); knowledge-item templates are built by chemistry_kb.
Each template is called with random.Random("<name>-<k>") and k = 0, 1, 2 ...
until it has produced n distinct questions.

Papers: a question that uses any 'C' (bold, Paper 2-only) statement is put on
["2C"] and tagged paper2_only; everything else can appear on ["1C", "2C"].
"""
import random
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from common import Bank  # noqa: E402
import chemistry_spec  # noqa: E402
import chemistry_util as U  # noqa: E402
import chemistry_t1  # noqa: E402,F401
import chemistry_t2  # noqa: E402,F401
import chemistry_t3  # noqa: E402,F401
import chemistry_t4  # noqa: E402,F401

TOKEN = re.compile(r"\b([MABPC])(\d+)\b")


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
    lvp = {re.sub(r"[^a-z0-9]", "", x["part"].lower()) for x in q["markscheme"].get("levels", [])}
    got = Counter()
    for r in q["markscheme"]["rows"]:
        t = TOKEN.findall(r["marks"])
        got[re.sub(r"[^a-z0-9]", "", r["part"].lower())] += sum(int(n) for _, n in t) if t else int(r["marks"])
    for lab, m in lv:
        if lab in lvp:
            continue
        g = sum(got.values()) if (len(lv) == 1 and lab == "") else got[lab]
        assert g == m, (name, lab, m, dict(got))


def sig(q):
    bits = [q.get("intro") or ""]

    def walk(ps):
        for p in ps:
            bits.append(p["text"])
            bits.extend(p.get("choices", []) or [])
            walk(p.get("parts", []) or [])
    walk(q["parts"])
    for f in q.get("figures") or []:
        bits.append(f.get("text", "") or "")
        for r in f.get("rows", []) or []:
            bits.extend(r)
    t = " ".join(bits).lower()
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9%.\-+=/ ]", " ", t)).strip()


def main():
    spec = chemistry_spec.build()
    refs, subs = set(), {}
    for t in spec["topics"]:
        for st in t["subtopics"]:
            subs[st["id"]] = (t["id"], st)
            refs.update(p["ref"] for p in st["points"])
    bank = Bank("chemistry")
    seen, cells = set(), Counter()
    names = Counter(t["name"] for t in U.TEMPLATES)
    dupn = [n for n, c in names.items() if c > 1]
    assert not dupn, dupn
    for t in U.TEMPLATES:
        assert t["sub"] in subs, (t["name"], t["sub"])
        tid, st = subs[t["sub"]]
        assert t["qtype"] in st["qtypes"], (t["name"], t["qtype"], t["sub"])
        made, k = 0, 0
        while made < t["n"] and k < t["n"] * 30:
            r = random.Random(f"{t['name']}-{k}")
            q = t["f"](r, k)
            k += 1
            if q is None:
                continue
            s = (t["sub"], sig(q), str(q.get("answer", {}).get("values")))
            if s in seen:
                continue
            check_marks(q, t["name"])
            for ref in q["spec_refs"]:
                assert ref in refs, (t["name"], ref)
            seen.add(s)
            made += 1
            p2 = any(x.endswith("C") for x in q["spec_refs"])
            bank.add(topic=tid.split(".")[1], subtopic=t["sub"], qtype=t["qtype"], command_word=q["command_word"],
                     difficulty=q["difficulty"], parts=q["parts"], markscheme=q["markscheme"],
                     spec_refs=q["spec_refs"], paper=["2C"] if p2 else ["1C", "2C"], ao=q.get("ao") or ["AO1"],
                     template=t["name"].replace("_", "-"), intro=q.get("intro") or None,
                     figures=q.get("figures") or None, calculator=True, answer=q.get("answer"),
                     tags=q.get("tags"), paper2_only=True if p2 else None)
            cells[(t["sub"], t["qtype"])] += 1
        if made < t["n"]:
            print(f"WARN template {t['name']} produced only {made}/{t['n']}")
    for topic, qs in bank.by_topic.items():
        for q in qs:
            q["topic"] = "chemistry." + topic
    thin = [(s, qt, cells[(s, qt)]) for s, (tid, st) in subs.items() for qt in st["qtypes"] if cells[(s, qt)] < 12]
    for x in thin:
        print("THIN", x)
    bank.save()
    allq = [q for qs in bank.by_topic.values() for q in qs]
    print("templates", len(U.TEMPLATES), "difficulty", dict(Counter(q["difficulty"] for q in allq)),
          "paper2_only", sum(1 for q in allq if q.get("paper2_only")))
    print("qtypes", dict(Counter(q["qtype"] for q in allq)))


if __name__ == "__main__":
    main()
