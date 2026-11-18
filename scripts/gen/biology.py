#!/usr/bin/env python3
"""Deterministic generator for the 4BI1 biology bank.

    .venv/bin/python scripts/gen/biology.py

Writes data/spec/biology.json and data/bank/biology/<topic>.json.
Short-answer questions (mcq/recall/describe/explain) come from the knowledge bases in
biology_kb*.py via biology_short; calculations, practicals, data, diagrams, genetics and
extended responses come from template modules that register factories with @reg.
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from common import Bank  # noqa: E402
import biology_spec  # noqa: E402
from biology_lib import REGISTRY, papers_for, S  # noqa: E402
import biology_short  # noqa: E402
import biology_kb1, biology_kb2, biology_kb3, biology_kb4, biology_kb5  # noqa: E402,F401
import biology_calc, biology_prac, biology_data, biology_diag, biology_gen, biology_ext, biology_comp  # noqa: E402,F401

AO_DEFAULT = {"mcq": ["AO1"], "recall": ["AO1"], "describe": ["AO1"], "explain": ["AO1", "AO2"],
              "calculation": ["AO2"], "genetics": ["AO2"], "practical": ["AO3"], "data": ["AO2", "AO3"],
              "diagram": ["AO1"], "extended": ["AO1", "AO2"], "comprehension": ["AO1", "AO2", "AO3"]}


def sig(parts, intro, figures):
    bits = [intro or ""]

    def walk(ps):
        for p in ps:
            bits.append(p.get("text", ""))
            bits.extend(p.get("choices", []) or [])
            allf.extend(p.get("figures", []) or [])
            walk(p.get("parts", []) or [])
    allf = list(figures or [])
    walk(parts)
    for f in allf:
        bits.append(f.get("text", "") or "")
        bits.append(f.get("svg", "") if f.get("type") == "svg" else "")
        for r in f.get("rows", []) or []:
            bits.extend(r)
    return re.sub(r"\s+", " ", " ".join(bits).lower())


def main():
    spec = biology_spec.build()
    look = biology_spec.sub_lookup()
    bank = Bank("biology")
    seen = set()
    skipped = Counter()

    def emit(sub, qtype, template, parts, rows, refs, cw, diff, intro=None, figures=None, levels=None,
             answer=None, ao=None, general=None, style=None):
        sub = S(sub)
        topic, prefs, qts = look[sub]
        assert qtype in qts, (sub, qtype)
        allrefs = {r for v in look.values() for r in v[1]}
        for r in refs:
            # comprehension (Paper 2 Q1) is synoptic: it may cite points from any subtopic
            assert (r in allrefs) if qtype == "comprehension" else (r in prefs), (sub, r, template)
        key = (sub, sig(parts, intro, figures))
        if key in seen:
            skipped[template] += 1
            return None
        seen.add(key)
        paper, p2 = papers_for(refs)
        if qtype == "comprehension":
            paper, p2 = ["2B"], True
        ms = {"style": style or ("levels" if levels else ("mcq" if qtype == "mcq" else "points")), "rows": rows}
        if levels:
            ms["levels"] = levels
        if general:
            ms["general"] = general
        return bank.add(topic=topic, subtopic=sub, qtype=qtype, command_word=cw, difficulty=diff,
                        parts=parts, markscheme=ms, spec_refs=refs, paper=paper,
                        ao=ao or AO_DEFAULT[qtype], template=template, intro=intro, figures=figures,
                        calculator=True, answer=answer, paper2_only=True if p2 else None)

    for st in [s for t in spec["topics"] for s in t["subtopics"]]:
        biology_short.build_short(st["id"], st["qtypes"], emit)
    for sub, qtype, template, fn in REGISTRY:
        for item in fn():
            item.setdefault("template", template)
            emit(sub, qtype, **item)
    total = bank.save()
    cells = Counter((q["subtopic"], q["qtype"]) for qs in bank.by_topic.values() for q in qs)
    thin = [(k, v) for k, v in cells.items() if v < 12]
    for st in [s for t in spec["topics"] for s in t["subtopics"]]:
        for qt in st["qtypes"]:
            if cells[(st["id"], qt)] < 12:
                print("THIN", st["id"], qt, cells[(st["id"], qt)])
    templates = {q["template"] for qs in bank.by_topic.values() for q in qs}
    diffs = Counter(q["difficulty"] for qs in bank.by_topic.values() for q in qs)
    print(f"templates: {len(templates)}  difficulty: {dict(diffs)}  skipped dups: {sum(skipped.values())}")
    return total


if __name__ == "__main__":
    main()
