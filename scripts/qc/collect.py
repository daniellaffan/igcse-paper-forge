#!/usr/bin/env python3
"""
Collect cold-check results into data/bank/qc/coldcheck.json and update progress.json.

  .venv/bin/python scripts/qc/collect.py

Reports, per subject: questions sampled, pass, fail, pass rate, and the failing ids
with the checker's notes (so the template can be fixed or the questions deleted).
A failing id that no longer exists in the bank (deleted), or whose template has
since been marked fixed in data/bank/qc/fixes.json, is counted under "resolved".
"""
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
QC = ROOT / "data" / "bank" / "qc"


def main():
    prog = json.loads((QC / "progress.json").read_text())
    fixes = json.loads((QC / "fixes.json").read_text()) if (QC / "fixes.json").exists() else {}
    fixes2 = {"after_recheck": fixes.get("_after_recheck", {})}
    bank_ids = set()
    for d in (ROOT / "data" / "bank").iterdir():
        if d.is_dir() and d.name != "qc":
            for f in d.glob("*.json"):
                bank_ids |= {q["id"] for q in json.loads(f.read_text())}
    out = defaultdict(lambda: {"sampled": 0, "pass": 0, "fail": 0, "resolved": 0, "failures": [],
                               "recheck_sampled": 0, "recheck_pass": 0, "recheck_failures": []})
    for name, b in prog["batches"].items():
        p = QC / "answers" / f"{name}.json"
        if not p.exists():
            continue
        r = json.loads(p.read_text())
        v = r.get("verdicts") or {}
        if not v:
            continue
        b["status"] = "answered"
        s = out[b["subject"]]
        recheck = "-recheck-" in name  # second check after fixes: reported separately from the first-check rate
        for qid in b["ids"]:
            res = v.get(qid)
            if not res or res.get("result") == "void":  # void = fault in the QC export, re-checked elsewhere
                continue
            if recheck:
                s["recheck_sampled"] += 1
                if res.get("result") == "pass":
                    s["recheck_pass"] += 1
                else:
                    s["recheck_failures"].append({"id": qid, "problem": res.get("problem"), "fix": res.get("fix"),
                                                  "fixed_after_recheck": qid.rsplit(".", 1)[0] in fixes2.get("after_recheck", {})})
                continue
            s["sampled"] += 1
            if res.get("result") == "pass":
                s["pass"] += 1
            else:
                s["fail"] += 1
                tmpl = qid.rsplit(".", 1)[0]
                resolved = qid not in bank_ids or tmpl in fixes
                s["resolved"] += resolved
                s["failures"].append({"id": qid, "problem": res.get("problem"), "fix": res.get("fix"),
                                      "resolved": resolved, "how": fixes.get(tmpl) or ("deleted" if qid not in bank_ids else None)})
    for s in out.values():
        s["pass_rate_first_check"] = round(s["pass"] / s["sampled"], 3) if s["sampled"] else None
        s["unresolved"] = s["fail"] - s["resolved"]
    (QC / "coldcheck.json").write_text(json.dumps(out, indent=1))
    (QC / "progress.json").write_text(json.dumps(prog, indent=1))
    for k, s in out.items():
        print(f"{k}: sampled {s['sampled']} pass {s['pass']} fail {s['fail']} unresolved {s['unresolved']}"
              f" | recheck {s['recheck_pass']}/{s['recheck_sampled']}")


if __name__ == "__main__":
    main()
