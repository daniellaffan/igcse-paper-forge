#!/usr/bin/env python3
"""
Validate the question bank and spec files.

  python scripts/validate_bank.py            # all subjects, exits 1 on any error
  python scripts/validate_bank.py maths      # one subject
  python scripts/validate_bank.py --report   # also write data/bank/qc/validation.json

Checks
  1. JSON schema validity (question + spec schemas)
  2. marks add up: question.marks == sum of part marks; mark-scheme marks per
     part == part marks (levels-marked parts are covered by their grid)
  3. every spec_ref exists in the subject's spec; topic/subtopic/qtype exist
     and the qtype is allowed for that subtopic
  4. ids unique; no near-duplicates (same normalised text inside a subtopic)
  5. coverage: each subtopic x allowed qtype has >= MIN_PER_CELL questions
  6. scale targets per subject and overall
Only needs the standard library + jsonschema.
"""
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

try:
    import jsonschema
except ImportError:  # CI installs it; fall back to structural checks only
    jsonschema = None

ROOT = Path(__file__).resolve().parent.parent
BANK = ROOT / "data" / "bank"
SPEC = ROOT / "data" / "spec"
SCHEMA = ROOT / "data" / "schema"
MIN_PER_CELL = 12
TARGETS = {"maths": 1500, "further-maths": 1500, "physics": 1500, "chemistry": 1500, "biology": 1500,
           "economics": 1500, "spanish": 1200, "history": 600, "english-language": 400,
           "english-literature": 400}
TOTAL_TARGET = 12000
HISTORY_PER_OPTION = 150
SUBJECTS = list(TARGETS)

MARK_TOKEN = re.compile(r"(?<![A-Za-z])d?([MABPC])(\d+)(?=ft|oe|cao|dep|\b)")  # also dM1, A1ft, B1oe, A1cao


def ms_marks(s):
    """Marks represented by a mark-scheme 'marks' cell: '3', 'M1 A1', 'B2', '1+1'."""
    s = str(s).strip()
    toks = MARK_TOKEN.findall(s)
    if toks:
        # 'dep' / 'oe' text is ignored; M marks count once each
        return sum(int(n) for _, n in toks)
    nums = re.findall(r"\d+", s)
    if re.fullmatch(r"\s*\d+(\s*\+\s*\d+)*\s*", s):
        return sum(int(n) for n in nums)
    if re.fullmatch(r"\s*\d+\s*", s):
        return int(s)
    return None


def leaf_parts(parts, prefix=""):
    out = []
    for p in parts:
        lab = prefix + (p.get("label") or "")
        if p.get("parts"):
            out += leaf_parts(p["parts"], lab)
        else:
            out.append((lab, int(p.get("marks", 0))))
    return out


def norm_label(s):
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())


def norm_text(q):
    bits = [q.get("intro", "")]

    def walk(ps):
        for p in ps:
            bits.append(p.get("text", ""))
            bits.extend(p.get("choices", []) or [])
            walk(p.get("parts", []) or [])
    walk(q["parts"])
    for f in q.get("figures", []) or []:
        bits.append(f.get("text", "") or f.get("transcript", "") or "")
        for r in f.get("rows", []) or []:
            bits.extend(r)
    t = " ".join(bits).lower()
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9áéíóúñü%.\-+=/ ]", " ", t)).strip()


def check_subject(subject, errors, warnings, stats, q_schema, s_schema):
    sp_path = SPEC / f"{subject}.json"
    if not sp_path.exists():
        errors.append(f"{subject}: missing spec file")
        return []
    spec = json.loads(sp_path.read_text())
    if jsonschema:
        for e in jsonschema.Draft202012Validator(s_schema).iter_errors(spec):
            errors.append(f"{subject} spec: {e.message} at {list(e.path)[:6]}")
    qtypes = {t["id"] for t in spec["qtypes"]}
    papers = {p["id"] for p in spec["papers"]}
    refs, subs, topics = set(), {}, {}
    for t in spec["topics"]:
        topics[t["id"]] = t
        refs.add(t["ref"])
        for st in t["subtopics"]:
            subs[st["id"]] = (t["id"], st)
            refs.add(st["ref"])
            for pt in st["points"]:
                refs.add(pt["ref"])
            for qt in st["qtypes"]:
                if qt not in qtypes:
                    errors.append(f"{subject} spec: subtopic {st['id']} uses unknown qtype {qt}")
    qs = []
    d = BANK / subject
    for f in sorted(d.glob("*.json")) if d.exists() else []:
        try:
            data = json.loads(f.read_text())
        except Exception as e:
            errors.append(f"{f.name}: bad JSON {e}")
            continue
        qs += data
    validator = jsonschema.Draft202012Validator(q_schema) if jsonschema else None
    ids = Counter(q.get("id") for q in qs)
    for i, n in ids.items():
        if n > 1:
            errors.append(f"{subject}: duplicate id {i} x{n}")
    cells = Counter()
    seen_text = {}
    dups = 0
    for q in qs:
        qid = q.get("id", "?")
        if validator:
            errs = list(validator.iter_errors(q))
            for e in errs[:3]:
                errors.append(f"{qid}: schema: {e.message} at {list(e.path)[:6]}")
            if errs:
                continue
        # marks
        leaves = leaf_parts(q["parts"])
        total = sum(m for _, m in leaves)
        if total != q["marks"]:
            errors.append(f"{qid}: marks {q['marks']} != sum of parts {total}")
        ms = q["markscheme"]
        lv_parts = {norm_label(l["part"]) for l in ms.get("levels", []) or []}
        by_part = defaultdict(int)
        unparsed = False
        for r in ms["rows"]:
            m = ms_marks(r["marks"])
            if m is None:
                unparsed = True
                continue
            by_part[norm_label(r["part"])] += m
        if not unparsed:
            for lab, m in leaves:
                nl = norm_label(lab)
                if nl in lv_parts or (not nl and "" in lv_parts):
                    continue
                if len(leaves) == 1 and not nl:
                    got = sum(by_part.values())
                else:
                    got = by_part.get(nl, 0)
                if got != m:
                    errors.append(f"{qid}: part '{lab}' worth {m} but mark scheme gives {got}")
        else:
            warnings.append(f"{qid}: unparsed mark cell")
        # spec links
        for r in q["spec_refs"]:
            if r not in refs:
                errors.append(f"{qid}: unknown spec ref {r}")
        if q["subtopic"] not in subs:
            errors.append(f"{qid}: unknown subtopic {q['subtopic']}")
        else:
            tid, st = subs[q["subtopic"]]
            if tid != q["topic"]:
                errors.append(f"{qid}: topic {q['topic']} but subtopic belongs to {tid}")
            if q["qtype"] not in st["qtypes"]:
                errors.append(f"{qid}: qtype {q['qtype']} not allowed for {q['subtopic']}")
        if q["qtype"] not in qtypes:
            errors.append(f"{qid}: unknown qtype {q['qtype']}")
        for p in q["paper"]:
            if p not in papers:
                errors.append(f"{qid}: unknown paper {p}")
        cells[(q["subtopic"], q["qtype"])] += 1
        key = (q["subtopic"], norm_text(q), json.dumps(q.get("answer", {}).get("values"), sort_keys=True))
        if key in seen_text:
            dups += 1
            errors.append(f"{qid}: near-duplicate of {seen_text[key]}")
        else:
            seen_text[key] = qid
    # coverage
    thin = []
    for sid, (tid, st) in subs.items():
        for qt in st["qtypes"]:
            n = cells[(sid, qt)]
            if n < MIN_PER_CELL:
                thin.append(f"{sid}/{qt}={n}")
    if thin:
        errors.append(f"{subject}: {len(thin)} subtopic x qtype cells below {MIN_PER_CELL}: " + ", ".join(thin[:15]))
    if len(qs) < TARGETS[subject]:
        errors.append(f"{subject}: {len(qs)} questions < target {TARGETS[subject]}")
    if subject == "history":
        per_opt = Counter(q.get("option") for q in qs)
        for o in [x["id"] for x in spec.get("options", [])]:
            if per_opt[o] < HISTORY_PER_OPTION:
                errors.append(f"history: option {o} has {per_opt[o]} < {HISTORY_PER_OPTION}")
        stats.setdefault("history_options", dict(per_opt))
    stats[subject] = {"questions": len(qs), "cells": len(cells), "thin_cells": len(thin), "duplicates": dups}
    return qs


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    subjects = args or SUBJECTS
    q_schema = json.loads((SCHEMA / "question.schema.json").read_text())
    s_schema = json.loads((SCHEMA / "spec.schema.json").read_text())
    errors, warnings, stats = [], [], {}
    total = 0
    for s in subjects:
        total += len(check_subject(s, errors, warnings, stats, q_schema, s_schema))
    if not args and total < TOTAL_TARGET:
        errors.append(f"whole bank {total} < {TOTAL_TARGET}")
    stats["total"] = total
    print(json.dumps(stats, indent=1))
    for w in warnings[:20]:
        print("WARN", w)
    if len(warnings) > 20:
        print(f"... {len(warnings)} warnings")
    for e in errors[:200]:
        print("ERROR", e)
    if len(errors) > 200:
        print(f"... {len(errors)} errors in total")
    if "--report" in sys.argv:
        (BANK / "qc").mkdir(parents=True, exist_ok=True)
        (BANK / "qc" / "validation.json").write_text(json.dumps(
            {"stats": stats, "errors": len(errors), "warnings": len(warnings),
             "error_samples": errors[:50]}, indent=1))
    print("OK" if not errors else f"FAILED with {len(errors)} errors")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
