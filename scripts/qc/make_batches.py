#!/usr/bin/env python3
"""
Prepare the independent answer check ("cold check").

  .venv/bin/python scripts/qc/make_batches.py [--per-template 3] [--batch 40] [subject ...]

Every question is produced by a template (generator function). A fresh agent that
did not write the questions answers a sample of questions cold, then compares
with the mark scheme. The sample covers EVERY template with `--per-template`
instances (different random values), so a bad template is caught and can be
fixed for all its questions at once.

For each batch it writes two files to data/bank/qc/batches/:
  <subject>-NNN.questions.md   question text only (what the student sees)
  <subject>-NNN.markscheme.md  the mark scheme for the same questions
The checker writes data/bank/qc/answers/<subject>-NNN.json (see AGENT_QC.md).
Progress: data/bank/qc/progress.json (resumable: batches already answered are kept).
"""
import argparse
import json
import random
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BANK = ROOT / "data" / "bank"
QC = BANK / "qc"
ORDER = ["maths", "further-maths", "physics", "chemistry", "biology", "economics", "history",
         "english-language", "english-literature", "spanish"]


def strip_svg(svg: str) -> str:
    texts = re.findall(r"<text[^>]*>(.*?)</text>", svg, flags=re.S)
    texts = [re.sub(r"<[^>]+>", "", t).strip() for t in texts]
    return "[diagram; labels: " + ", ".join(t for t in texts if t)[:600] + "]"


def fig_text(f: dict) -> str:
    t = f.get("type")
    cap = f.get("caption") or f.get("title") or ""
    if t == "svg":
        return f"{cap} {strip_svg(f.get('svg', ''))}".strip()
    if t == "table":
        rows = [" | ".join(map(str, f.get("headers") or f.get("header") or []))] + [" | ".join(map(str, r)) for r in f.get("rows") or []]
        return (cap + "\n" if cap else "") + "\n".join(rows)
    if t == "audio":
        return f"[LISTENING — transcript, heard twice]\n{f.get('transcript') or f.get('text') or ''}"
    if t in ("source", "passage", "poem"):
        head = " — ".join(x for x in [f.get("label"), f.get("title"), f.get("attribution")] if x)
        return f"{head}\n{f.get('text', '')}"
    return json.dumps({k: v for k, v in f.items() if k != "svg"})[:800]


def parts_text(parts, depth=0):
    out = []
    for p in parts or []:
        pad = "  " * depth
        line = f"{pad}{p.get('label') or ''} {p.get('text', '')} [{p.get('marks')} mark(s)]"
        out.append(line.rstrip())
        for c in p.get("choices") or []:
            out.append(f"{pad}  - {c}")
        for f in p.get("figures") or []:
            out.append(pad + fig_text(f))
        out += parts_text(p.get("parts"), depth + 1)
    return out


def question_md(q: dict) -> str:
    L = [f"### {q['id']}  ({q['marks']} marks{', calculator' if q.get('calculator') else ''})"]
    if q.get("intro"):
        L.append(q["intro"])
    for f in q.get("figures") or []:
        L.append(fig_text(f))
    L += parts_text(q["parts"])
    return "\n".join(L)


def ms_md(q: dict) -> str:
    ms = q.get("markscheme", {})
    L = [f"### {q['id']}"]
    for r in ms.get("rows") or []:
        L.append(f"- ({r.get('part') or ''}) {r.get('answer')} — {r.get('marks')}" + (f"  [{r['notes']}]" if r.get("notes") else ""))
    for lv in ms.get("levels") or []:
        L.append(f"- ({lv.get('part') or ''}) levels-marked: {lv.get('title', '')}")
        for g in lv.get("grid") or []:
            L.append(f"    L{g.get('level')} {g.get('marks')}: {g.get('descriptor', '')[:400]}")
        for i in lv.get("indicative") or []:
            L.append(f"    • {i}")
    if ms.get("general"):
        L.append(f"- general: {ms['general']}")
    if q.get("answer", {}).get("values"):
        L.append(f"- computed answer values: {q['answer']['values']}")
    return "\n".join(L)


def write_batch(name, s, chunk, prog):
    (QC / "batches" / f"{name}.questions.md").write_text(
        f"# {s} — cold check batch {name}\n\nAnswer every question as a strong student would.\n\n"
        + "\n\n".join(question_md(q) for q in chunk) + "\n")
    (QC / "batches" / f"{name}.markscheme.md").write_text(
        f"# {s} — mark scheme for batch {name}\n\n" + "\n\n".join(ms_md(q) for q in chunk) + "\n")
    prog["batches"][name] = {"subject": s, "ids": [q["id"] for q in chunk], "status": "pending"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("subjects", nargs="*")
    ap.add_argument("--per-template", type=int, default=3)
    ap.add_argument("--batch", type=int, default=40)
    ap.add_argument("--new-templates-only", action="store_true",
                    help="sample only templates not yet covered by an answered batch (after a regeneration)")
    ap.add_argument("--recheck", nargs="+", metavar="ID",
                    help="write one batch <subject>-recheck-N with just these question ids")
    a = ap.parse_args()
    (QC / "batches").mkdir(parents=True, exist_ok=True)
    (QC / "answers").mkdir(parents=True, exist_ok=True)
    prog_p = QC / "progress.json"
    prog = json.loads(prog_p.read_text()) if prog_p.exists() else {"batches": {}}
    rnd = random.Random(2027)
    if a.recheck:
        s = a.recheck[0].split(".")[0]
        qs = {q["id"]: q for f in sorted((BANK / s).glob("*.json")) for q in json.loads(f.read_text())}
        n = 1 + sum(1 for k in prog["batches"] if k.startswith(f"{s}-recheck-"))
        name = f"{s}-recheck-{n}"
        chunk = [qs[i] for i in a.recheck if i in qs]
        write_batch(name, s, chunk, prog)
        prog_p.write_text(json.dumps(prog, indent=1))
        print("wrote", name, len(chunk))
        return
    for s in a.subjects or ORDER:
        rnd = random.Random(f"2027-{s}")  # per-subject seed: a subject's sample never depends on the others
        d = BANK / s
        if not d.exists():
            continue
        qs = [q for f in sorted(d.glob("*.json")) for q in json.loads(f.read_text())]
        by_t = defaultdict(list)
        for q in qs:
            by_t[q["id"].rsplit(".", 1)[0]].append(q)
        sample = []
        done_t = set()
        if a.new_templates_only:
            for n, b in prog["batches"].items():
                if b["subject"] == s and (QC / "answers" / f"{n}.json").exists() and \
                        json.loads((QC / "answers" / f"{n}.json").read_text()).get("verdicts"):
                    done_t |= {i.rsplit(".", 1)[0] for i in b["ids"]}
            for n in [n for n, b in prog["batches"].items() if b["subject"] == s and b.get("status") != "answered"
                      and not (QC / "answers" / f"{n}.json").exists()]:
                del prog["batches"][n]
        for t in sorted(t for t in by_t if t not in done_t):
            items = by_t[t]
            sample += rnd.sample(items, min(a.per_template, len(items)))
        # keep already-answered batches; only (re)write batches not yet answered
        start = 1 + max([int(n.rsplit("-", 1)[1]) for n in prog["batches"]
                         if prog["batches"][n]["subject"] == s and n.rsplit("-", 1)[1].isdigit()] or [-1]) \
            if a.new_templates_only else 0
        for i in range(0, len(sample), a.batch):
            name = f"{s}-{start + i // a.batch:03d}"
            if prog["batches"].get(name, {}).get("status") == "answered":
                continue
            write_batch(name, s, sample[i:i + a.batch], prog)
        prog.setdefault("templates", {})[s] = len(by_t)
        prog.setdefault("questions", {})[s] = len(qs)
        print(s, len(qs), "questions,", len(by_t), "templates,", len(sample), "sampled")
    prog_p.write_text(json.dumps(prog, indent=1))


if __name__ == "__main__":
    main()
