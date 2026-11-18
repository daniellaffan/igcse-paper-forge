"""Shared builders for the biology generator (4BI1).

Content modules register question factories with @reg(subtopic, qtype).  Each factory is a
generator function yielding dicts that `emit()` turns into bank records.
"""
import math
import random
import re
from collections import defaultdict

from common import fmt_num

LETTERS = "ABCD"
REGISTRY = []          # (sub, qtype, template, fn)
SUB_PREFIX = "biology."


def reg(sub, qtype, template=None):
    def deco(fn):
        REGISTRY.append((sub, qtype, template or fn.__name__, fn))
        return fn
    return deco


def S(short):
    """'structures.cells' -> 'biology.structures.cells'"""
    return short if short.startswith(SUB_PREFIX) else SUB_PREFIX + short


def is_b(ref):
    return ref.endswith("B")


def papers_for(refs):
    p2 = any(is_b(r) for r in refs)
    return (["2B"] if p2 else ["1B", "2B"]), p2


def lines_for(marks):
    if marks <= 1:
        return 2
    return marks * 2 + (2 if marks >= 5 else 0)


def nf(x, dp=None, sf=None):
    return fmt_num(x, dp=dp, sf=sf)


def sfig(x, n=3):
    """Round to n significant figures and format without float noise."""
    return fmt_num(float(x), sf=n)


WORDNUM = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight"}

CW_NOUN = {"Explain": "An explanation", "Describe": "A description", "Suggest": "An answer",
           "Discuss": "A discussion", "Comment": "An answer", "Give": "An answer", "State": "An answer",
           "Compare": "A comparison", "Evaluate": "An evaluation", "Name": "An answer"}


def points_row(part, marks, points, cw="Explain", notes=None, ao=None):
    """Board-style point table row: one row, 'any n of the following' list."""
    noun = CW_NOUN.get(cw, "An answer")
    if len(points) > marks:
        head = f"{noun} that makes reference to {WORDNUM.get(marks, marks)} of the following:"
    elif len(points) == 1:
        return row_(part, points[0] + " (1)" if marks == 1 else points[0], marks, notes, ao)
    else:
        head = f"{noun} that makes reference to the following:"
    body = "\n".join(f"• {p} (1)" for p in points)
    return row_(part, head + "\n" + body, marks, notes, ao)


def row_(part, answer, marks, notes=None, ao=None):
    r = {"part": part, "answer": answer, "marks": str(marks)}
    if notes:
        r["notes"] = notes
    if ao:
        r["ao"] = ao
    return r


def mcq_part(rng, label, stem, correct, distractors, why=None, figures=None):
    """Build an MCQ part; returns (part, row).  Options are shuffled deterministically."""
    opts = [correct] + list(distractors[:3])
    assert len(set(opts)) == 4, (stem, opts)
    order = list(range(4))
    rng.shuffle(order)
    choices = [opts[i] for i in order]
    k = choices.index(correct)
    letter = LETTERS[k]
    ans = f"The only correct answer is {letter} ({correct})"
    others = [LETTERS[i] for i in range(4) if i != k]
    if why:
        note = why
    else:
        note = f"{', '.join(others[:-1])} and {others[-1]} are incorrect."
    p = {"label": label, "text": stem, "marks": 1, "space": "mcq", "choices": choices}
    if figures:
        p["figures"] = figures
    return p, row_(label, ans, 1, note, "AO1")


def text_part(label, text, marks, lines=None, prefix=None, space=None, figures=None):
    p = {"label": label, "text": text, "marks": marks}
    if space:
        p["space"] = space
    if space not in ("mcq", "graph", "table", "none"):
        p["lines"] = lines if lines is not None else lines_for(marks)
    if prefix:
        p["answer_prefix"] = prefix
    if figures:
        p["figures"] = figures
    return p


def calc_part(label, text, marks, prefix, lines=None, suffix=None):
    p = {"label": label, "text": text, "marks": marks, "space": "working",
         "lines": lines if lines is not None else max(3, marks * 2), "answer_prefix": prefix}
    if suffix:
        p["answer_suffix"] = suffix
    return p


def unit_of(final):
    """Unit text after the number in a final answer string, e.g. '12.5 cm³ per minute' -> 'cm³ per minute'."""
    import re as _re
    m = _re.match(r"^\s*[×x]?[-+−]?[\d.,]+(?:\s*\(.*?\))?\s*(.*)$", final)
    if not m:
        return None
    u = m.group(1).strip()
    if not u or u.startswith(":") or u.startswith("("):
        return None
    return u


def table_fig(headers, rows, caption=None, note=None):
    f = {"type": "table", "headers": headers, "rows": [[str(c) for c in r] for r in rows]}
    if caption:
        f["caption"] = caption
    if note:
        f["note"] = note
    return f


def svg_fig(svg, width=110, caption=None, note=None):
    f = {"type": "svg", "svg": svg, "width": width}
    if caption:
        f["caption"] = caption
    if note:
        f["note"] = note
    return f


def pick(rng, seq, k):
    seq = list(seq)
    rng.shuffle(seq)
    return seq[:k]


def label_seq(n):
    return [chr(97 + i) for i in range(n)]


ROMAN = ["(i)", "(ii)", "(iii)", "(iv)", "(v)"]


def cap(s):
    return s[:1].upper() + s[1:] if s else s


def a_an(word):
    return "an" if word[:1].lower() in "aeiou" else "a"


# ------------------------------------------------------------------ SVG graphs

def _nice_step(span, ticks=5):
    raw = span / ticks
    mag = 10 ** math.floor(math.log10(raw))
    for m in (1, 2, 2.5, 5, 10):
        if raw <= m * mag:
            return m * mag
    return 10 * mag


def _fmt_tick(v):
    if abs(v - round(v)) < 1e-9:
        return str(int(round(v)))
    return f"{v:.10g}"


def line_graph(series, xlabel, ylabel, xmax=None, ymax=None, xmin=0, ymin=0, curve=False,
               points=True, w=420, h=300, legend=None, xticks=None):
    """series: list of (name, [(x, y), ...]).  Black-and-white line graph with grid and axes."""
    allx = [x for _, pts in series for x, _ in pts]
    ally = [y for _, pts in series for _, y in pts]
    xmax = xmax if xmax is not None else max(allx)
    ymax = ymax if ymax is not None else max(ally) * 1.1
    xs = _nice_step(xmax - xmin)
    ys = _nice_step(ymax - ymin)
    xmax = math.ceil((xmax - xmin) / xs - 1e-9) * xs + xmin
    ymax = math.ceil((ymax - ymin) / ys - 1e-9) * ys + ymin
    L, R, T, B = 62, 18, 14, 48
    pw, ph = w - L - R, h - T - B

    def X(x):
        return L + (x - xmin) / (xmax - xmin) * pw

    def Y(y):
        return T + ph - (y - ymin) / (ymax - ymin) * ph
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" font-family="sans-serif" font-size="11">']
    # minor grid
    nx = int(round((xmax - xmin) / xs)) * 5
    ny = int(round((ymax - ymin) / ys)) * 5
    for i in range(nx + 1):
        x = L + pw * i / nx
        out.append(f'<line x1="{x:.1f}" y1="{T}" x2="{x:.1f}" y2="{T+ph}" stroke="currentColor" stroke-width="{0.5 if i % 5 == 0 else 0.15}" opacity="0.6"/>')
    for j in range(ny + 1):
        y = T + ph * j / ny
        out.append(f'<line x1="{L}" y1="{y:.1f}" x2="{L+pw}" y2="{y:.1f}" stroke="currentColor" stroke-width="{0.5 if j % 5 == 0 else 0.15}" opacity="0.6"/>')
    out.append(f'<line x1="{L}" y1="{T+ph}" x2="{L+pw}" y2="{T+ph}" stroke="currentColor" stroke-width="1.2"/>')
    out.append(f'<line x1="{L}" y1="{T}" x2="{L}" y2="{T+ph}" stroke="currentColor" stroke-width="1.2"/>')
    v = xmin
    while v <= xmax + 1e-9:
        out.append(f'<text x="{X(v):.1f}" y="{T+ph+14}" text-anchor="middle" fill="currentColor">{_fmt_tick(v)}</text>')
        v += xs
    v = ymin
    while v <= ymax + 1e-9:
        out.append(f'<text x="{L-5}" y="{Y(v)+4:.1f}" text-anchor="end" fill="currentColor">{_fmt_tick(v)}</text>')
        v += ys
    out.append(f'<text x="{L+pw/2:.1f}" y="{h-8}" text-anchor="middle" fill="currentColor">{esc(xlabel)}</text>')
    out.append(f'<text x="14" y="{T+ph/2:.1f}" text-anchor="middle" fill="currentColor" transform="rotate(-90 14 {T+ph/2:.1f})">{esc(ylabel)}</text>')
    dashes = ["", "6 3", "2 2", "8 3 2 3"]
    marks = ["x", "o", "s", "t"]
    for si, (name, pts) in enumerate(series):
        pts = sorted(pts)
        d = dashes[si % 4]
        if curve and len(pts) > 2:
            path = _smooth([(X(x), Y(y)) for x, y in pts])
        else:
            path = "M " + " L ".join(f"{X(x):.1f} {Y(y):.1f}" for x, y in pts)
        out.append(f'<path d="{path}" fill="none" stroke="currentColor" stroke-width="1.3"' + (f' stroke-dasharray="{d}"' if d else "") + "/>")
        if points:
            for x, y in pts:
                out.append(_marker(marks[si % 4], X(x), Y(y)))
        if legend and len(series) > 1:
            lx, ly = L + 10, T + 12 + si * 14
            out.append(f'<line x1="{lx}" y1="{ly}" x2="{lx+22}" y2="{ly}" stroke="currentColor" stroke-width="1.3"' + (f' stroke-dasharray="{d}"' if d else "") + "/>")
            out.append(f'<text x="{lx+27}" y="{ly+4}" fill="currentColor">{esc(name)}</text>')
    out.append("</svg>")
    return "".join(out)


def _marker(kind, x, y):
    if kind == "x":
        return (f'<path d="M {x-3:.1f} {y-3:.1f} L {x+3:.1f} {y+3:.1f} M {x-3:.1f} {y+3:.1f} L {x+3:.1f} {y-3:.1f}" '
                f'stroke="currentColor" stroke-width="1.2"/>')
    if kind == "o":
        return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2.8" fill="none" stroke="currentColor" stroke-width="1.1"/>'
    if kind == "s":
        return f'<rect x="{x-2.6:.1f}" y="{y-2.6:.1f}" width="5.2" height="5.2" fill="currentColor"/>'
    return f'<path d="M {x:.1f} {y-3.2:.1f} L {x+3:.1f} {y+2.6:.1f} L {x-3:.1f} {y+2.6:.1f} Z" fill="currentColor"/>'


def _smooth(P):
    d = f"M {P[0][0]:.1f} {P[0][1]:.1f}"
    for i in range(len(P) - 1):
        p0 = P[i - 1] if i > 0 else P[i]
        p1, p2 = P[i], P[i + 1]
        p3 = P[i + 2] if i + 2 < len(P) else p2
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d += f" C {c1[0]:.1f} {c1[1]:.1f} {c2[0]:.1f} {c2[1]:.1f} {p2[0]:.1f} {p2[1]:.1f}"
    return d


def bar_chart(cats, vals, ylabel, xlabel="", w=420, h=300, ymax=None, groups=None):
    """Vertical bar chart. groups: optional list of series names when vals is list of lists."""
    multi = isinstance(vals[0], (list, tuple))
    allv = [v for vs in vals for v in vs] if multi else vals
    ymax = ymax or max(allv) * 1.15
    ys = _nice_step(ymax)
    ymax = math.ceil(ymax / ys) * ys
    L, R, T, B = 62, 14, 14, 56
    pw, ph = w - L - R, h - T - B

    def Y(y):
        return T + ph - y / ymax * ph
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" font-family="sans-serif" font-size="11">']
    v = 0
    while v <= ymax + 1e-9:
        out.append(f'<line x1="{L}" y1="{Y(v):.1f}" x2="{L+pw}" y2="{Y(v):.1f}" stroke="currentColor" stroke-width="0.3" opacity="0.6"/>')
        out.append(f'<text x="{L-5}" y="{Y(v)+4:.1f}" text-anchor="end" fill="currentColor">{_fmt_tick(v)}</text>')
        v += ys
    out.append(f'<line x1="{L}" y1="{T+ph}" x2="{L+pw}" y2="{T+ph}" stroke="currentColor" stroke-width="1.2"/>')
    out.append(f'<line x1="{L}" y1="{T}" x2="{L}" y2="{T+ph}" stroke="currentColor" stroke-width="1.2"/>')
    n = len(cats)
    slot = pw / n
    fills = ["currentColor", "none", "url(#hatch)"]
    out.insert(1, '<defs><pattern id="hatch" width="5" height="5" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
               '<line x1="0" y1="0" x2="0" y2="5" stroke="currentColor" stroke-width="1.2"/></pattern></defs>')
    for i, c in enumerate(cats):
        vs = vals[i] if multi else [vals[i]]
        bw = slot * 0.6 / len(vs)
        x0 = L + slot * i + slot * 0.2
        for j, vv in enumerate(vs):
            f = fills[j % 3]
            out.append(f'<rect x="{x0 + j*bw:.1f}" y="{Y(vv):.1f}" width="{bw:.1f}" height="{T+ph-Y(vv):.1f}" '
                       f'fill="{f}" fill-opacity="{0.35 if f == "currentColor" else 1}" stroke="currentColor" stroke-width="1"/>')
        out.append(f'<text x="{L + slot*i + slot/2:.1f}" y="{T+ph+14}" text-anchor="middle" fill="currentColor">{esc(c)}</text>')
    if xlabel:
        out.append(f'<text x="{L+pw/2:.1f}" y="{h-10}" text-anchor="middle" fill="currentColor">{esc(xlabel)}</text>')
    out.append(f'<text x="14" y="{T+ph/2:.1f}" text-anchor="middle" fill="currentColor" transform="rotate(-90 14 {T+ph/2:.1f})">{esc(ylabel)}</text>')
    if multi and groups:
        for j, g in enumerate(groups):
            lx, ly = L + pw - 120, T + 8 + j * 15
            f = fills[j % 3]
            out.append(f'<rect x="{lx}" y="{ly}" width="12" height="9" fill="{f}" fill-opacity="{0.35 if f == "currentColor" else 1}" stroke="currentColor"/>')
            out.append(f'<text x="{lx+17}" y="{ly+8}" fill="currentColor">{esc(g)}</text>')
    out.append("</svg>")
    return "".join(out)


def esc(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            .replace("³", "<tspan baseline-shift='super' font-size='8'>3</tspan>")
            .replace("²", "<tspan baseline-shift='super' font-size='8'>2</tspan>"))


def graph_ms(part, xname, yname):
    """Board-style plotting mark rows (axes, scale, plotting, line)."""
    return [
        row_(part, f"axes the right way round ({xname} on the x-axis) and both labelled with units (1)", 1,
             "Accept axes labelled with the table headings", "AO3"),
        row_(part, "suitable linear scale using at least half the grid on each axis (1)", 1,
             "Reject scales with uneven intervals", "AO3"),
        row_(part, "all points plotted correctly to within half a small square (1)", 1, None, "AO3"),
        row_(part, "points joined with straight lines or a smooth curve of best fit (1)", 1,
             "Ignore extrapolation beyond the plotted points; reject a line drawn to the origin unless it is a data point", "AO3"),
    ]


def pct_change(a, b):
    return (b - a) / a * 100


def mean(xs):
    return sum(xs) / len(xs)
