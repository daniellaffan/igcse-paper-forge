#!/usr/bin/env python3
"""Deterministic generator for the 4PH1 physics bank.

    .venv/bin/python scripts/gen/physics.py

Writes data/spec/physics.json, data/reference/physics-equations.json and
data/bank/physics/<topic>.json.  Content lives in physics_t_*.py modules:
knowledge items (registered with kb()) are combined into multi-part recall /
describe / explain / multiple-choice / extended questions; parametric templates
(registered with @T) build calculations, practical, data and diagram questions
with every numerical answer computed in code.
"""
import json
import random
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from common import Bank  # noqa: E402
import physics_spec  # noqa: E402
import physics_util as U  # noqa: E402
import physics_t_forces  # noqa: E402,F401
import physics_t_elec  # noqa: E402,F401
import physics_t_waves  # noqa: E402,F401
import physics_t_energy  # noqa: E402,F401
import physics_t_matter  # noqa: E402,F401
import physics_t_magnet  # noqa: E402,F401
import physics_t_radio  # noqa: E402,F401
import physics_t_astro  # noqa: E402,F401
import physics_reference  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
TOKEN = re.compile(r"\b([MABPC])(\d+)\b")
KB_TYPES = ("mcq", "recall", "describe", "explain", "extended")
KB_N = 14


def leaf(parts, pre=""):
    out = []
    for p in parts:
        lab = pre + (p.get("label") or "")
        if p.get("parts"):
            out += leaf(p["parts"], lab)
        else:
            out.append((re.sub(r"[^a-z0-9]", "", lab.lower()), p["marks"]))
    return out


def check(q, name):
    lv = leaf(q["parts"])
    lvp = {re.sub(r"[^a-z0-9]", "", x["part"].lower()) for x in q.get("levels", [])}
    got = Counter()
    for r in q["rows"]:
        got[re.sub(r"[^a-z0-9]", "", r["part"].lower())] += int(r["marks"])
    if len(lv) == 1 and lv[0][0] == "" and "" not in lvp:
        assert sum(got.values()) == lv[0][1], (name, lv, got)
    else:
        for lab, m in lv:
            if lab in lvp:
                continue
            assert got[lab] == m, (name, lab, m, dict(got), q["parts"])


def main():
    spec = physics_spec.build()
    physics_spec.write()
    physics_reference.write()
    idx = physics_spec.subtopic_index()
    allrefs = {r for v in idx.values() for r in v["refs"]}
    bank = Bank("physics")
    seen = set()
    cells = Counter()

    unit_re = re.compile(r"^(.*?)\s*\(([^()]+)\)\s*=\s*$")

    def suffixes(ps):
        for pt in ps:
            pre = pt.get("answer_prefix")
            if pre:
                mt = unit_re.match(pre)
                if mt:
                    pt["answer_prefix"] = mt.group(1) + " = "
                    pt["answer_suffix"] = mt.group(2)
            suffixes(pt.get("parts") or [])

    def add(q, sub, qtype, tname):
        check(q, tname)
        if re.match(r"This question is about", q.get("intro") or ""):
            q = {k: v for k, v in q.items() if k != "intro"}   # real 4PH1 papers don't open every question this way
        suffixes(q["parts"])
        sig = (sub, U.sigtext(q), json.dumps(q.get("answer", {}).get("values"), sort_keys=True))
        if sig in seen:
            return False
        seen.add(sig)
        info = idx[sub]
        refs = []
        for r in q["refs"]:
            if r not in refs:
                refs.append(r)
        bad = [r for r in refs if r not in allrefs]
        assert not bad, (tname, bad)
        assert qtype in info["qtypes"], (tname, qtype, sub)
        p2 = any(r.endswith("P") for r in refs)
        ms = {"style": q.get("style", "points"), "rows": q["rows"]}
        if q.get("levels"):
            ms["levels"] = q["levels"]
        if q.get("general"):
            ms["general"] = q["general"]
        bank.add(topic=info["topic"], subtopic=sub, qtype=qtype, command_word=q["cmd"], difficulty=q["d"],
                 parts=q["parts"], markscheme=ms, spec_refs=refs, paper=["2P"] if p2 else ["1P", "2P"],
                 ao=q["ao"], template=tname, intro=q.get("intro"), figures=q.get("figures"), calculator=True,
                 answer=q.get("answer"), paper2_only=True if p2 else None, tags=q.get("tags"))
        cells[(sub, qtype)] += 1
        return True

    # knowledge-item questions
    for sub, pool in U.KB.items():
        for qt in KB_TYPES:
            if qt in idx[sub]["qtypes"] and pool.get(qt):
                short = sub.split(".", 1)[1].replace(".", "-")
                for q in U.kb_questions(sub, qt, KB_N, f"{sub}-{qt}"):
                    add(q, sub, qt, f"{short}-{qt}-kb")
    # parametric templates
    for sub, qt, n, name, fn in U.TEMPLATES:
        made, k = 0, 0
        while made < n and k < n * 40:
            q = fn(random.Random(f"{name}-{k}"))
            k += 1
            if q is None:
                continue
            if add(q, sub, qt, name):
                made += 1
        if made < n:
            print(f"WARN template {name} produced only {made}/{n}")
    thin = []
    for sub, info in idx.items():
        for qt in info["qtypes"]:
            if cells[(sub, qt)] < 12:
                thin.append(f"{sub}/{qt}={cells[(sub, qt)]}")
    if thin:
        print("THIN:", ", ".join(thin))
    bank.save()
    print("templates:", len(U.TEMPLATES), "kb subtopics:", len(U.KB))


if __name__ == "__main__":
    main()
