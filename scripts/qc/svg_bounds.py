#!/usr/bin/env python3
"""
Find diagram labels that run outside their SVG's viewBox (they are clipped on the page),
and answer lines whose *prefix* is a bare unit (units belong after the dots, as on real papers).

  .venv/bin/python scripts/qc/svg_bounds.py [subject ...]
"""
import json, re, sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TEXT = re.compile(r"<text\b([^>]*)>(.*?)</text>", re.S)
attr = lambda a, k, d=None: (re.search(rf'\b{k}="([^"]*)"', a) or [None, d])[1]

def width_est(s, size):
    s = re.sub(r"<[^>]+>", "", s)
    s = re.sub(r"&\w+;|&#\d+;", "x", s)
    return sum(0.3 if c in "il.,:;'|!1 " else 0.75 if c.isupper() or c in "mw" else 0.52 for c in s) * size

def check_svg(svg):
    m = re.search(r'viewBox="([\d.\-]+)[ ,]+([\d.\-]+)[ ,]+([\d.]+)[ ,]+([\d.]+)"', svg)
    if not m:
        return []
    x0, y0, w, h = map(float, m.groups())
    base = float(attr(re.search(r"<svg\b[^>]*>", svg).group(0), "font-size", "12") or 12)
    bad = []
    for a, t in TEXT.findall(svg):
        if "transform=" in a and "rotate" in a:
            continue  # rotated labels: skip (rare)
        try:
            x = float(attr(a, "x", "0")); y = float(attr(a, "y", "0"))
        except ValueError:
            continue
        size = float(attr(a, "font-size", base) or base)
        tw = width_est(t, size)
        anchor = attr(a, "text-anchor", "start")
        left = x - tw / 2 if anchor == "middle" else x - tw if anchor == "end" else x
        right = left + tw
        top, bottom = y - size * 0.8, y + size * 0.25
        if "dominant-baseline" in a and "middle" in a:
            top, bottom = y - size * 0.5, y + size * 0.5
        over = max(x0 - left, right - (x0 + w), y0 - top, bottom - (y0 + h))
        if over > size * 0.6:
            bad.append((re.sub(r"<[^>]+>", "", t).strip()[:30], round(over, 1)))
    return bad

UNIT = re.compile(r"^\s*(\$?[a-zA-Z°£€%²³/ ()\\{}^]+)\s*$")
def main():
    subs = sys.argv[1:] or [d.name for d in (ROOT / "data" / "bank").iterdir() if d.is_dir() and d.name != "qc"]
    svg_bad, pre_bad = defaultdict(list), defaultdict(list)
    for s in subs:
        for f in (ROOT / "data" / "bank" / s).glob("*.json"):
            for q in json.loads(f.read_text()):
                tmpl = q["id"].rsplit(".", 1)[0]
                figs = list(q.get("figures") or [])
                def walk(ps):
                    for p in ps or []:
                        figs.extend(p.get("figures") or [])
                        pre = p.get("answer_prefix")
                        if pre and UNIT.match(pre) and not re.search(r"=|:|\$[a-z]\$", pre) and not p.get("answer_suffix"):
                            pre_bad[tmpl].append(pre)
                        walk(p.get("parts"))
                walk(q["parts"])
                for fg in figs:
                    if fg.get("type") == "svg":
                        b = check_svg(fg.get("svg", ""))
                        if b:
                            svg_bad[tmpl].append((q["id"], b))
    print("SVG labels outside the diagram:", sum(len(v) for v in svg_bad.values()), "questions in", len(svg_bad), "templates")
    for t, v in sorted(svg_bad.items(), key=lambda kv: -len(kv[1])):
        print(f"  {t}: {len(v)}  e.g. {v[0][0]} {v[0][1][:3]}")
    print("Bare-unit answer prefixes:", sum(len(v) for v in pre_bad.values()), "parts in", len(pre_bad), "templates")
    for t, v in sorted(pre_bad.items(), key=lambda kv: -len(kv[1])):
        print(f"  {t}: {len(v)}  e.g. {Counter(v).most_common(3)}")

if __name__ == "__main__":
    main()
