"""
Shared helpers for question generators.

Each subject has a generator `scripts/gen/<subject>.py` that builds question
records (see docs/DATA_FORMAT.md) and calls `write_topic()` once per topic.

    from common import Bank
    bank = Bank("maths")
    bank.add(topic="number", subtopic="maths.number.fractions", ...)   # returns record
    bank.save()          # writes data/bank/maths/<topic>.json + progress

Generators must be deterministic (seeded RNG) so re-running reproduces the
same bank; ids are stable.
"""
import json
import random
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BANK = ROOT / "data" / "bank"
SPEC = ROOT / "data" / "spec"
PROGRESS = BANK / "progress.json"

MINUTES_PER_MARK = {
    "maths": 1.2, "further-maths": 1.33, "physics": 1.09, "chemistry": 1.09, "biology": 1.09,
    "economics": 1.2, "history": 1.5, "english-language": 1.5, "english-literature": 1.5, "spanish": 1.2,
}


def part_marks(parts):
    t = 0
    for p in parts:
        if p.get("parts"):
            t += part_marks(p["parts"])
        else:
            t += int(p.get("marks", 0))
    return t


def rng(seed):
    return random.Random(seed)


def load_spec(subject):
    return json.loads((SPEC / f"{subject}.json").read_text())


class Bank:
    def __init__(self, subject):
        self.subject = subject
        self.by_topic = defaultdict(list)
        self.ids = set()
        self.counter = defaultdict(int)

    def add(self, *, topic, subtopic, qtype, command_word, difficulty, parts, markscheme, spec_refs,
            paper, ao, template, intro=None, figures=None, minutes=None, calculator=None, answer=None,
            provenance=None, option=None, section=None, tags=None, paper2_only=None, id=None):
        marks = part_marks(parts)
        if id is None:
            self.counter[template] += 1
            id = f"{self.subject}.{template}.{self.counter[template]:04d}"
        id = re.sub(r"[^a-z0-9._-]", "-", id.lower())
        assert id not in self.ids, f"duplicate id {id}"
        self.ids.add(id)
        rec = {
            "id": id, "subject": self.subject, "paper": list(paper), "spec_refs": list(spec_refs),
            "topic": topic, "subtopic": subtopic, "qtype": qtype, "command_word": command_word,
            "marks": marks, "difficulty": difficulty,
            "minutes": minutes if minutes is not None else round(marks * MINUTES_PER_MARK[self.subject], 1),
            "parts": parts, "markscheme": markscheme, "ao": list(ao), "template": template,
        }
        for k, v in (("intro", intro), ("figures", figures), ("calculator", calculator), ("answer", answer),
                     ("provenance", provenance), ("option", option), ("section", section), ("tags", tags),
                     ("paper2_only", paper2_only)):
            if v is not None:
                rec[k] = v
        self.by_topic[topic].append(rec)
        return rec

    def save(self):
        d = BANK / self.subject
        d.mkdir(parents=True, exist_ok=True)
        for old in d.glob("*.json"):
            old.unlink()
        total = 0
        for topic, qs in self.by_topic.items():
            qs = [tidy_question(q) for q in qs]
            (d / f"{topic}.json").write_text(json.dumps(qs, ensure_ascii=False, indent=1))
            total += len(qs)
        prog = json.loads(PROGRESS.read_text()) if PROGRESS.exists() else {}
        prog[self.subject] = {"questions": total, "topics": {t: len(q) for t, q in self.by_topic.items()}}
        PROGRESS.write_text(json.dumps(prog, indent=1, sort_keys=True))
        print(f"{self.subject}: wrote {total} questions in {len(self.by_topic)} topic files")
        return total



# ---------------------------------------------------------------- final tidy applied to every saved question

_TEXT = re.compile(r"<text\b([^>]*)>(.*?)</text>", re.S)


def _attr(a, k, d=None):
    m = re.search(rf'\b{k}="([^"]*)"', a)
    return m.group(1) if m else d


def _text_width(s, size):
    s = re.sub(r"<[^>]+>", "", s)
    s = re.sub(r"&\w+;|&#\d+;", "x", s)
    return sum(0.3 if c in "il.,:;'|!1 " else 0.75 if c.isupper() or c in "mw" else 0.52 for c in s) * size


def text_boxes(svg):
    """Estimated bounding boxes (x0, y0, x1, y1) of the unrotated <text> labels in an SVG."""
    head = re.search(r"<svg\b[^>]*>", svg)
    base = float(_attr(head.group(0), "font-size", "12") or 12) if head else 12.0
    out = []
    for a, t in _TEXT.findall(svg):
        if "rotate" in (_attr(a, "transform", "") or ""):
            continue
        try:
            x, y = float(_attr(a, "x", "0")), float(_attr(a, "y", "0"))
            size = float(_attr(a, "font-size", base) or base)
        except ValueError:
            continue
        w = _text_width(t, size)
        anchor = _attr(a, "text-anchor", "start")
        x0 = x - w / 2 if anchor == "middle" else x - w if anchor == "end" else x
        if "middle" in (_attr(a, "dominant-baseline", "") or ""):
            y0, y1 = y - size * 0.55, y + size * 0.55
        else:
            y0, y1 = y - size * 0.85, y + size * 0.3
        out.append((x0, y0, x0 + w, y1))
    return out


def fit_svg(svg):
    """Grow the viewBox so every label lies inside it (labels outside are clipped on the page)."""
    m = re.search(r'viewBox="([\d.\-]+)[ ,]+([\d.\-]+)[ ,]+([\d.]+)[ ,]+([\d.]+)"', svg)
    if not m:
        return svg
    x0, y0, w, h = map(float, m.groups())
    boxes = text_boxes(svg)
    if not boxes:
        return svg
    pad = 3
    nx0 = min([x0] + [b[0] - pad for b in boxes])
    ny0 = min([y0] + [b[1] - pad for b in boxes])
    nx1 = max([x0 + w] + [b[2] + pad for b in boxes])
    ny1 = max([y0 + h] + [b[3] + pad for b in boxes])
    if (nx0, ny0, nx1, ny1) == (x0, y0, x0 + w, y0 + h):
        return svg
    nw, nh = nx1 - nx0, ny1 - ny0
    svg = svg.replace(m.group(0), f'viewBox="{nx0:g} {ny0:g} {nw:g} {nh:g}"', 1)
    # keep an explicit width/height (if any) in proportion
    head = re.search(r"<svg\b[^>]*>", svg).group(0)
    new = head
    for k, old, newv in (("width", w, nw), ("height", h, nh)):
        v = _attr(head, k)
        if v and re.fullmatch(r"[\d.]+", v):
            new = re.sub(rf'\b{k}="[^"]*"', f'{k}="{float(v) * newv / old:g}"', new, count=1)
    return svg.replace(head, new, 1)


_BARE_UNIT = re.compile(r"^\s*[a-zA-Z°£€%²³/ ()]+\s*$")


def _tidy_parts(parts):
    for p in parts or []:
        pre = p.get("answer_prefix")
        # a bare unit belongs after the answer dots ("........ cm"), as on the real papers
        if pre and _BARE_UNIT.match(pre) and "=" not in pre and not p.get("answer_suffix"):
            p["answer_suffix"] = pre.strip()
            del p["answer_prefix"]
        for f in p.get("figures") or []:
            if f.get("type") == "svg" and f.get("svg"):
                f["svg"] = fit_svg(f["svg"])
        _tidy_parts(p.get("parts"))


def tidy_question(q):
    for f in q.get("figures") or []:
        if f.get("type") == "svg" and f.get("svg"):
            f["svg"] = fit_svg(f["svg"])
    _tidy_parts(q.get("parts"))
    return q


# ---------------------------------------------------------------- small helpers

def row(part, answer, marks, notes=None, ao=None):
    r = {"part": part, "answer": answer, "marks": str(marks)}
    if notes:
        r["notes"] = notes
    if ao:
        r["ao"] = ao
    return r


def levels(part, grid, indicative, title=None, ao_split=None,
           credit_note="Indicative content is not exhaustive: credit any other valid points."):
    lv = {"part": part, "grid": [{"level": g[0], "marks": g[1], "descriptor": g[2]} for g in grid],
          "indicative": indicative, "credit_note": credit_note}
    if title:
        lv["title"] = title
    if ao_split:
        lv["ao_split"] = ao_split
    return lv


def band(score):
    """Map a 0-1 difficulty score to a grade band."""
    return "1-3" if score < 0.34 else ("4-6" if score < 0.67 else "7-9")


def fmt_num(x, dp=None, sf=None):
    """Format a number without float noise. dp = decimal places, sf = significant figures."""
    from decimal import Decimal, ROUND_HALF_UP
    if sf is not None:
        if x == 0:
            return "0"
        import math
        d = sf - int(math.floor(math.log10(abs(x)))) - 1
        q = Decimal(str(x)).quantize(Decimal(1).scaleb(-d) if d > 0 else Decimal(1), rounding=ROUND_HALF_UP)
        if d <= 0:
            q = (Decimal(str(x)) / Decimal(10) ** (-d)).quantize(Decimal(1), rounding=ROUND_HALF_UP) * Decimal(10) ** (-d)
            return str(int(q))
        return f"{q:.{d}f}"
    if dp is not None:
        q = Decimal(str(x)).quantize(Decimal(1).scaleb(-dp), rounding=ROUND_HALF_UP)
        return f"{q:.{dp}f}"
    s = f"{x:.10g}"
    return s
