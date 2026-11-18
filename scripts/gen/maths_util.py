"""Shared helpers for the 4MA1 maths generator: template registry, question
builder, number formatting and SVG drawing helpers.  All numeric answers are
computed in the templates with sympy / fractions and passed through here."""
import math
from fractions import Fraction as F
from html import escape

import sympy as sp

from common import fmt_num, row  # noqa: F401  (re-exported)

TEMPLATES = []

NOT_ACC = "Diagram NOT accurately drawn"


def tpl(sub, qtype, n=12, refs=None):
    """Register a template.  sub = short subtopic id (without 'maths.')."""
    def deco(f):
        TEMPLATES.append({"f": f, "sub": "maths." + sub, "qtype": qtype, "n": n, "name": f.__name__,
                          "refs": refs})
        return f
    return deco


def P(label, text, marks, prefix=None, space="working", lines=None, figs=None, parts=None):
    p = {"label": label, "text": text, "marks": marks}
    if parts:
        p = {"label": label, "text": text, "marks": 0, "parts": parts}
        return p
    p["space"] = space
    if prefix is not None:
        p["answer_prefix"] = prefix
    if lines is not None:
        p["lines"] = lines
    if figs:
        p["figures"] = figs
    return p


def R(part, answer, marks, notes=None):
    return row(part, answer, marks, notes)


def Q(*, parts, rows, values, diff, cw, refs, intro=None, figs=None, method="sympy exact arithmetic",
      general=None, tags=None):
    ms = {"style": "maths", "rows": rows}
    if general:
        ms["general"] = general
    return {"intro": intro, "parts": parts, "markscheme": ms, "difficulty": diff, "command_word": cw,
            "spec_refs": refs, "figures": figs,
            "answer": {"method": method, "values": {k: _jsonable(v) for k, v in values.items()}, "checked": True},
            "tags": tags}


def _jsonable(v):
    if isinstance(v, (int, str, bool)) or v is None:
        return v
    if isinstance(v, float):
        return float(fmt_num(v, sf=12)) if v != 0 else 0.0
    if isinstance(v, F):
        return str(v) if v.denominator != 1 else v.numerator
    if isinstance(v, (list, tuple)):
        return [_jsonable(x) for x in v]
    if isinstance(v, sp.Basic):
        if v.is_Integer:
            return int(v)
        return str(v)
    return str(v)


# ------------------------------------------------------------------ numbers

def sf(x, n=3):
    return fmt_num(float(x), sf=n)


def dp(x, n=2):
    return fmt_num(float(x), dp=n)


def money(x):
    return fmt_num(float(x), dp=2)


def num(x):
    """Exact-looking string for int / Fraction / float without noise."""
    if isinstance(x, F):
        if x.denominator == 1:
            return str(x.numerator)
        return f"{x.numerator}/{x.denominator}"
    if isinstance(x, float):
        if abs(x - round(x)) < 1e-9:
            return str(int(round(x)))
        return fmt_num(x, sf=10).rstrip("0").rstrip(".") if "." in fmt_num(x, sf=10) else fmt_num(x, sf=10)
    if isinstance(x, sp.Basic):
        return str(x)
    return str(x)


def big(n):
    """Integer with thin-space thousands separators as on the paper (e.g. 12 500)."""
    s = f"{int(n):,}".replace(",", " ")
    return s if abs(int(n)) >= 10000 else str(int(n))


def ftex(x):
    """LaTeX for a Fraction / int (negative sign outside)."""
    x = F(x)
    if x.denominator == 1:
        return str(x.numerator)
    s = "-" if x < 0 else ""
    return f"{s}\\frac{{{abs(x.numerator)}}}{{{x.denominator}}}"


def mixed_tex(x):
    x = F(x)
    if x.denominator == 1 or abs(x) < 1:
        return ftex(x)
    w = int(abs(x)) * (1 if x > 0 else -1)
    rem = abs(x) - abs(w)
    return f"{w}\\frac{{{rem.numerator}}}{{{rem.denominator}}}"


def tex(e):
    return sp.latex(e)


def poly_tex(coeffs, var="x"):
    """coeffs high->low ints -> latex string like 3x^2 - 5x + 2."""
    n = len(coeffs) - 1
    out = ""
    for i, c in enumerate(coeffs):
        p = n - i
        if c == 0:
            continue
        sign = "-" if c < 0 else "+"
        a = abs(c)
        if p == 0:
            body = str(a)
        else:
            body = ("" if a == 1 else str(a)) + var + (f"^{{{p}}}" if p > 1 else "")
        if out == "":
            out = ("-" if c < 0 else "") + body
        else:
            out += f" {sign} {body}"
    return out or "0"


def lin_tex(a, b, var="x"):
    return poly_tex([a, b], var)


def signed(c):
    return f"+ {c}" if c >= 0 else f"- {abs(c)}"


def bracket(a, b, var="x"):
    """(ax + b) as latex"""
    return f"({lin_tex(a, b, var)})"


# ------------------------------------------------------------------ contexts

NAMES = ["Amira", "Ben", "Chen", "Daniela", "Eko", "Farah", "Gustavo", "Hana", "Isaac", "Jaya", "Kofi", "Leila",
         "Mateo", "Nadia", "Omar", "Priya", "Quentin", "Rosa", "Sanjay", "Tomasz", "Uma", "Viktor", "Wen", "Yusuf",
         "Zara", "Arjun", "Bianca", "Dev", "Elena", "Femi", "Grace", "Hamid", "Ines", "Joel", "Keiko", "Luca",
         "Maya", "Nikhil", "Olga", "Pablo", "Ravi", "Sofia", "Tariq", "Valentina", "Xavier", "Yara"]
CURRENCIES = [("dollars", "\\$", "$"), ("euros", "€", "€"), ("pounds", "£", "£")]
CUR_WORDS = ["dollars", "euros", "rupees", "riyals", "dirhams", "pesos", "rand", "francs", "yuan", "lira"]


def name(r, k=1):
    s = r.sample(NAMES, k)
    return s[0] if k == 1 else s


def cur(r):
    return r.choice(CUR_WORDS)


# ------------------------------------------------------------------ SVG

def svg(w, h, body, fs=13):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:g} {h:g}" font-family="serif" '
            f'font-size="{fs}" fill="none" stroke="currentColor" stroke-width="1.4" '
            f'stroke-linejoin="round" stroke-linecap="round">{body}</svg>')


def T(x, y, s, anchor="middle", it=False, size=None, weight=None):
    a = f' font-size="{size}"' if size else ""
    if it:
        a += ' font-style="italic"'
    if weight:
        a += f' font-weight="{weight}"'
    return (f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" dominant-baseline="middle" '
            f'fill="currentColor" stroke="none"{a}>{escape(str(s))}</text>')


def L(x1, y1, x2, y2, w=None, dash=None):
    a = f' stroke-width="{w}"' if w else ""
    if dash:
        a += f' stroke-dasharray="{dash}"'
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}"{a}/>'


def PL(pts, close=False, w=None, dash=None, fill=None):
    s = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    tag = "polygon" if close else "polyline"
    a = f' stroke-width="{w}"' if w else ""
    if dash:
        a += f' stroke-dasharray="{dash}"'
    if fill:
        a += f' fill="{fill}"'
    return f'<{tag} points="{s}"{a}/>'


def C(cx, cy, r, w=None, fill=None, dash=None):
    a = f' stroke-width="{w}"' if w else ""
    if fill:
        a += f' fill="{fill}"'
    if dash:
        a += f' stroke-dasharray="{dash}"'
    return f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}"{a}/>'


def DOT(x, y, r=2.4):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="currentColor" stroke="none"/>'


def ARC(cx, cy, r, a1, a2, w=None):
    """Arc from screen-angle a1 to a2 (degrees, counter-clockwise in maths sense)."""
    x1, y1 = cx + r * math.cos(math.radians(a1)), cy - r * math.sin(math.radians(a1))
    x2, y2 = cx + r * math.cos(math.radians(a2)), cy - r * math.sin(math.radians(a2))
    sweep = (a2 - a1) % 360
    large = 1 if sweep > 180 else 0
    a = f' stroke-width="{w}"' if w else ""
    return f'<path d="M{x1:.1f},{y1:.1f} A{r:.1f},{r:.1f} 0 {large} 0 {x2:.1f},{y2:.1f}"{a}/>'


def ARROW(x1, y1, x2, y2, head=7):
    ang = math.atan2(y2 - y1, x2 - x1)
    a1 = (x2 - head * math.cos(ang - 0.4), y2 - head * math.sin(ang - 0.4))
    a2 = (x2 - head * math.cos(ang + 0.4), y2 - head * math.sin(ang + 0.4))
    return L(x1, y1, x2, y2) + PL([a1, (x2, y2), a2], close=True, fill="currentColor")


def fig(svgs, width=90, note=NOT_ACC, caption=None):
    f = {"type": "svg", "svg": svgs, "width": width}
    if note:
        f["note"] = note
    if caption:
        f["caption"] = caption
    return f


def table(headers, rows, caption=None):
    t = {"type": "table", "headers": [str(h) for h in headers], "rows": [[str(c) for c in r] for r in rows]}
    if caption:
        t["caption"] = caption
    return t


class Frame:
    """Maps maths coordinates into a w x h box with margin, y up."""

    def __init__(self, pts, w=320, h=230, m=34):
        xs = [p[0] for p in pts]
        ys = [p[1] for p in pts]
        self.x0, self.x1, self.y0, self.y1 = min(xs), max(xs), min(ys), max(ys)
        dx = max(self.x1 - self.x0, 1e-9)
        dy = max(self.y1 - self.y0, 1e-9)
        self.k = min((w - 2 * m) / dx, (h - 2 * m) / dy)
        self.w = dx * self.k + 2 * m
        self.h = dy * self.k + 2 * m
        self.m = m

    def __call__(self, p):
        return (self.m + (p[0] - self.x0) * self.k, self.m + (self.y1 - p[1]) * self.k)


def _unit(dx, dy):
    d = math.hypot(dx, dy) or 1
    return dx / d, dy / d


def polygon_fig(pts, names=None, sides=None, angles=None, right=None, w=320, h=230, extra=None,
                marks_parallel=None, dots=None, closed=True):
    """pts: maths coords.  names: vertex labels.  sides: {(i,j): label}.
    angles: {i: label} drawn inside at vertex i.  right: [i] right-angle squares."""
    fr = Frame(pts + (extra or {}).get("pts", []), w, h)
    S = [fr(p) for p in pts]
    cx = sum(p[0] for p in S) / len(S)
    cy = sum(p[1] for p in S) / len(S)
    body = PL(S, close=closed)
    for i, nm in enumerate(names or []):
        if not nm:
            continue
        ux, uy = _unit(S[i][0] - cx, S[i][1] - cy)
        body += T(S[i][0] + 13 * ux, S[i][1] + 13 * uy, nm, it=False)
    for (i, j), lab in (sides or {}).items():
        mx, my = (S[i][0] + S[j][0]) / 2, (S[i][1] + S[j][1]) / 2
        dx, dy = S[j][0] - S[i][0], S[j][1] - S[i][1]
        nx, ny = _unit(-dy, dx)
        if (mx + nx - cx) ** 2 + (my + ny - cy) ** 2 < (mx - cx) ** 2 + (my - cy) ** 2:
            nx, ny = -nx, -ny
        off = 10 + 3.2 * len(lab)
        body += T(mx + off * nx, my + off * ny, lab)
    n = len(S)
    for i, lab in (angles or {}).items():
        a, b, c = S[(i - 1) % n], S[i], S[(i + 1) % n]
        body += angle_mark(b, a, c, lab)
    for i in right or []:
        a, b, c = S[(i - 1) % n], S[i], S[(i + 1) % n]
        body += right_mark(b, a, c)
    if extra and extra.get("body"):
        body += extra["body"](fr)
    return svg(fr.w, fr.h, body)


def angle_mark(v, p, q, lab, r=20):
    """Arc at vertex v between rays to p and q (screen coords), label along bisector."""
    a1 = math.degrees(math.atan2(-(p[1] - v[1]), p[0] - v[0]))
    a2 = math.degrees(math.atan2(-(q[1] - v[1]), q[0] - v[0]))
    d = (a2 - a1) % 360
    if d > 180:
        a1, a2 = a2, a1
        d = 360 - d
    out = ARC(v[0], v[1], r, a1, a1 + d, w=1)
    mid = math.radians(a1 + d / 2)
    rr = r + 9 + (4 if d < 40 else 0) + 2.5 * max(0, len(lab) - 2)
    if lab:
        out += T(v[0] + rr * math.cos(mid), v[1] - rr * math.sin(mid), lab, size=12)
    return out


def right_mark(v, p, q, s=10):
    u = _unit(p[0] - v[0], p[1] - v[1])
    t = _unit(q[0] - v[0], q[1] - v[1])
    a = (v[0] + s * u[0], v[1] + s * u[1])
    b = (v[0] + s * (u[0] + t[0]), v[1] + s * (u[1] + t[1]))
    c = (v[0] + s * t[0], v[1] + s * t[1])
    return PL([a, b, c], w=1)


def grid_fig(xmin, xmax, ymin, ymax, cell=None, step=1, xstep=None, ystep=None, minor=1, items="",
             xlabel="x", ylabel="y", axes_at_zero=True, numbers=True, w=360, h=320, ytick=None, xtick=None):
    """Graph-paper grid; returns (svg_string_builder, mapper).  items: callable(mapper)->svg"""
    xstep = xstep or step
    ystep = ystep or step
    xtick = xtick or xstep
    ytick = ytick or ystep
    sx = (w - 50) / (xmax - xmin)
    sy = (h - 40) / (ymax - ymin)
    ox, oy = 35, 15

    def M(p):
        return (ox + (p[0] - xmin) * sx, oy + (ymax - p[1]) * sy)

    b = ""
    # minor grid
    nx = int(round((xmax - xmin) / (xstep / minor)))
    for i in range(nx + 1):
        x = xmin + i * xstep / minor
        X = M((x, 0))[0]
        major = abs((x - xmin) / xstep - round((x - xmin) / xstep)) < 1e-9
        b += L(X, M((0, ymin))[1], X, M((0, ymax))[1], w=0.6 if major else 0.25)
    ny = int(round((ymax - ymin) / (ystep / minor)))
    for i in range(ny + 1):
        y = ymin + i * ystep / minor
        Y = M((0, y))[1]
        major = abs((y - ymin) / ystep - round((y - ymin) / ystep)) < 1e-9
        b += L(M((xmin, 0))[0], Y, M((xmax, 0))[0], Y, w=0.6 if major else 0.25)
    ax_y = 0 if (axes_at_zero and ymin <= 0 <= ymax) else ymin
    ax_x = 0 if (axes_at_zero and xmin <= 0 <= xmax) else xmin
    X0, Y0 = M((ax_x, ax_y))
    b += L(M((xmin, ax_y))[0], Y0, M((xmax, ax_y))[0] + 8, Y0, w=1.4)
    b += L(X0, M((ax_x, ymin))[1], X0, M((ax_x, ymax))[1] - 8, w=1.4)
    b += T(M((xmax, ax_y))[0] + 14, Y0, xlabel, it=True)
    b += T(X0, M((ax_x, ymax))[1] - 12, ylabel, it=True)
    if numbers:
        k = 0
        x = xmin
        while x <= xmax + 1e-9:
            if abs(x - ax_x) > 1e-9 or not (axes_at_zero and ymin <= 0 <= ymax):
                b += T(M((x, ax_y))[0], Y0 + 11, _tick(x), size=10)
            k += 1
            x = xmin + k * xtick
        k = 0
        y = ymin
        while y <= ymax + 1e-9:
            if abs(y - ax_y) > 1e-9 or not (axes_at_zero and xmin <= 0 <= xmax):
                b += T(X0 - 5, M((ax_x, y))[1], _tick(y), anchor="end", size=10)
            k += 1
            y = ymin + k * ytick
        if axes_at_zero and xmin <= 0 <= xmax and ymin <= 0 <= ymax:
            b += T(X0 - 6, Y0 + 10, "O", anchor="end", size=10)
    if callable(items):
        b += items(M)
    else:
        b += items
    return svg(w + 10, h + 5, b, fs=12)


def _tick(v):
    if abs(v - round(v)) < 1e-9:
        return str(int(round(v)))
    return fmt_num(v, sf=6).rstrip("0").rstrip(".")


def curve(M, f, x0, x1, ymin, ymax, n=200, w=1.6):
    pts, segs = [], []
    for i in range(n + 1):
        x = x0 + (x1 - x0) * i / n
        try:
            y = f(x)
        except ZeroDivisionError:
            y = None
        if y is None or y != y or y < ymin - 1e-9 or y > ymax + 1e-9:
            if len(pts) > 1:
                segs.append(pts)
            pts = []
            continue
        pts.append(M((x, y)))
    if len(pts) > 1:
        segs.append(pts)
    return "".join(PL(s, w=w) for s in segs)


def tree_fig(first, second, labels1, labels2, outcomes=False, w=360, h=230):
    """first: [p, p]; second: [[p,p],[p,p]] label strings (may be '' for blank)."""
    b = ""
    x0, x1, x2 = 20, 150, 290
    ys1 = [h * 0.27, h * 0.73]
    for i, (p, lab) in enumerate(zip(first, labels1)):
        y = ys1[i]
        b += L(x0, h / 2, x1 - 30, y)
        b += T(x1 - 18, y, lab, anchor="start")
        mx, my = (x0 + x1 - 30) / 2, (h / 2 + y) / 2
        b += T(mx - 4, my + (-10 if i == 0 else 12), p if p else "........", anchor="end", size=12)
        for j, (q, lab2) in enumerate(zip(second[i], labels2[i])):
            yy = y + (-1 if j == 0 else 1) * h * 0.13
            b += L(x1 + 30, y, x2 - 20, yy)
            b += T(x2 - 12, yy, lab2, anchor="start")
            mx2, my2 = (x1 + 30 + x2 - 20) / 2, (y + yy) / 2
            b += T(mx2 - 2, my2 + (-9 if j == 0 else 11), q if q else "........", anchor="end", size=12)
    return svg(w, h, b)


def venn_fig(labels, regions, outside=None, three=False, w=330, h=220, set_names=None):
    """2-set regions: [A only, both, B only]; 3-set: [A,B,C,AB,AC,BC,ABC] strings."""
    b = f'<rect x="8" y="8" width="{w - 16}" height="{h - 16}"/>'
    b += T(22, 22, "ℰ", size=15)
    if not three:
        b += C(w * 0.39, h / 2, h * 0.33) + C(w * 0.61, h / 2, h * 0.33)
        b += T(w * 0.23, h * 0.14, labels[0], it=True) + T(w * 0.77, h * 0.14, labels[1], it=True)
        b += T(w * 0.31, h / 2, regions[0]) + T(w / 2, h / 2, regions[1]) + T(w * 0.69, h / 2, regions[2])
    else:
        r = h * 0.27
        ca, cb, cc = (w * 0.41, h * 0.38), (w * 0.59, h * 0.38), (w * 0.5, h * 0.63)
        b += C(*ca, r) + C(*cb, r) + C(*cc, r)
        b += T(ca[0] - r * 0.9, ca[1] - r * 0.9, labels[0], it=True)
        b += T(cb[0] + r * 0.9, cb[1] - r * 0.9, labels[1], it=True)
        b += T(cc[0] + r * 1.05, cc[1] + r * 0.75, labels[2], it=True)
        A, B, Cc, AB, AC, BC, ABC = regions
        b += T(ca[0] - r * 0.45, ca[1] - r * 0.15, A) + T(cb[0] + r * 0.45, cb[1] - r * 0.15, B)
        b += T(cc[0], cc[1] + r * 0.5, Cc) + T(w * 0.5, ca[1] - r * 0.45, AB)
        b += T(ca[0] - r * 0.2, cc[1] - r * 0.05, AC) + T(cb[0] + r * 0.2, cc[1] - r * 0.05, BC)
        b += T(w * 0.5, h * 0.48, ABC)
    if outside is not None:
        b += T(w - 30, h - 24, outside)
    return svg(w, h, b)


def circle_fig(points, chords=(), centre=None, tangents=(), angles=None, w=300, h=280, R=100, extra_lines=(),
               labels_extra=None, right=()):
    """points: {name: angle_deg on circle} or {name:(x,y)} off-circle (maths units of R=1).
    chords: [(n1,n2)], tangents: [(name, length_left, length_right, end_labels)]
    angles: {(vertex, p, q): label}"""
    cx, cy = w / 2, h / 2
    pos = {}
    for k, v in points.items():
        if isinstance(v, tuple):
            pos[k] = (cx + R * v[0], cy - R * v[1])
        else:
            pos[k] = (cx + R * math.cos(math.radians(v)), cy - R * math.sin(math.radians(v)))
    if centre:
        pos[centre] = (cx, cy)
    b = C(cx, cy, R)
    if centre:
        b += DOT(cx, cy, 2)
    for a, c in chords:
        b += L(*pos[a], *pos[c])
    for nm, l1, l2, ends in tangents:
        x, y = pos[nm]
        dx, dy = _unit(x - cx, y - cy)
        tx, ty = -dy, dx
        e1 = (x + tx * l1, y + ty * l1)
        e2 = (x - tx * l2, y - ty * l2)
        b += L(*e1, *e2)
        if ends:
            if ends[0]:
                pos[ends[0]] = e1
            if ends[1]:
                pos[ends[1]] = e2
    for a, c in extra_lines:
        b += L(*pos[a], *pos[c])
    for k, (x, y) in pos.items():
        if k.startswith("_"):
            continue
        dx, dy = _unit(x - cx, y - cy)
        if k == centre:
            b += T(x + 10, y + 10, k)
        else:
            b += T(x + 14 * dx, y + 14 * dy, k)
    for (v, p, q), lab in (angles or {}).items():
        b += angle_mark(pos[v], pos[p], pos[q], lab, r=18)
    for (v, p, q) in right:
        b += right_mark(pos[v], pos[p], pos[q])
    return svg(w, h, b), pos


def cuboid_fig(l, w_, h_, labels=("A", "B", "C", "D", "E", "F", "G", "H"), dims=None, diag=None, W=320, H=240):
    """Oblique cuboid.  Bottom ABCD (front-left A), top EFGH above.  dims: (lab_l, lab_w, lab_h)."""
    k = min(180 / (l + 0.6 * w_), 160 / (h_ + 0.45 * w_))
    ox, oy = 40, H - 30
    dx, dy = 0.6 * w_ * k, -0.45 * w_ * k

    def p(x, y, z):  # x along l, y depth, z up
        return (ox + x * k + y / w_ * dx if w_ else ox + x * k, oy - z * k + (y / w_ * dy if w_ else 0))
    A, B, Cc, D = p(0, 0, 0), p(l, 0, 0), p(l, w_, 0), p(0, w_, 0)
    E, Fv, G, Hh = p(0, 0, h_), p(l, 0, h_), p(l, w_, h_), p(0, w_, h_)
    b = PL([A, B, Fv, E], close=True) + PL([B, Cc, G, Fv], close=True) + PL([E, Fv, G, Hh], close=True)
    b += L(*A, *D, dash="4,3") + L(*D, *Cc, dash="4,3") + L(*D, *Hh, dash="4,3")
    P_ = dict(zip(labels, [A, B, Cc, D, E, Fv, G, Hh]))
    offs = {labels[0]: (-10, 8), labels[1]: (8, 10), labels[2]: (10, 4), labels[3]: (-8, -8),
            labels[4]: (-10, -6), labels[5]: (2, -10), labels[6]: (10, -6), labels[7]: (-6, -10)}
    for nm, pt in P_.items():
        b += T(pt[0] + offs[nm][0], pt[1] + offs[nm][1], nm)
    if dims:
        if dims[0]:
            b += T((A[0] + B[0]) / 2, A[1] + 14, dims[0])
        if dims[1]:
            b += T((B[0] + Cc[0]) / 2 + 18, (B[1] + Cc[1]) / 2 + 6, dims[1])
        if dims[2]:
            b += T(A[0] - 22, (A[1] + E[1]) / 2, dims[2])
    for a, c in diag or []:
        b += L(*P_[a], *P_[c], dash="2,2" if False else None)
    return svg(W, H, b), P_


def cone_fig(r_lab, h_lab=None, l_lab=None, W=200, H=220, kind="cone"):
    cx, top, base = W / 2, 25, H - 45
    rx, ry = 60, 16
    b = f'<ellipse cx="{cx}" cy="{base}" rx="{rx}" ry="{ry}"/>'
    if kind == "cone":
        b += L(cx - rx, base, cx, top) + L(cx + rx, base, cx, top)
        if h_lab:
            b += L(cx, top, cx, base, dash="4,3") + right_mark((cx, base), (cx, top), (cx + rx, base))
            b += T(cx - 14, (top + base) / 2, h_lab, anchor="end")
        if l_lab:
            b += T(cx + rx / 2 + 16, (top + base) / 2 - 6, l_lab, anchor="start")
        b += L(cx, base, cx + rx, base, dash="4,3") + T(cx + rx / 2, base + 12, r_lab)
    elif kind == "cylinder":
        b += f'<ellipse cx="{cx}" cy="{top + 10}" rx="{rx}" ry="{ry}"/>'
        b += L(cx - rx, top + 10, cx - rx, base) + L(cx + rx, top + 10, cx + rx, base)
        b += L(cx, top + 10, cx + rx, top + 10, dash="4,3") + T(cx + rx / 2, top + 1, r_lab)
        if h_lab:
            b += T(cx + rx + 8, (top + base) / 2, h_lab, anchor="start")
    return svg(W + 40, H, b)


def sphere_fig(r_lab, hemi=False, W=200, H=180):
    cx, cy, R = W / 2, H / 2 + (20 if hemi else 0), 65
    if hemi:
        b = ARC(cx, cy, R, 0, 180) + f'<ellipse cx="{cx}" cy="{cy}" rx="{R}" ry="15"/>'
    else:
        b = C(cx, cy, R) + f'<path d="M{cx - R},{cy} A{R},15 0 0 0 {cx + R},{cy}"/>' + \
            f'<path d="M{cx - R},{cy} A{R},15 0 0 1 {cx + R},{cy}" stroke-dasharray="4,3"/>'
    b += DOT(cx, cy, 2) + L(cx, cy, cx + R, cy) + T(cx + R / 2, cy - 9, r_lab)
    return svg(W, H, b)


def sector_fig(r_lab, ang, ang_lab, W=260, H=230, names=("O", "A", "B")):
    R = 150 if ang <= 100 else 95
    start = 90 - ang / 2 if ang < 180 else -ang / 2 + 90
    pts = [(0, 0), (math.cos(math.radians(start)), math.sin(math.radians(start))),
           (math.cos(math.radians(start + ang)), math.sin(math.radians(start + ang)))]
    allp = pts + [(math.cos(math.radians(a)), math.sin(math.radians(a)))
                  for a in range(int(start), int(start + ang) + 1, 5)]
    fr = Frame(allp, W, H)
    O, A, B = [fr(p) for p in pts]
    rr = fr.k
    b = L(*O, *A) + L(*O, *B) + ARC(O[0], O[1], rr, start, start + ang)
    b += angle_mark(O, A, B, ang_lab, r=22)
    b += T(O[0], O[1] + 14, names[0])
    ux, uy = _unit(A[0] - O[0], A[1] - O[1])
    b += T(A[0] + 12 * ux, A[1] + 12 * uy, names[1])
    ux, uy = _unit(B[0] - O[0], B[1] - O[1])
    b += T(B[0] + 12 * ux, B[1] + 12 * uy, names[2])
    mx, my = (O[0] + A[0]) / 2, (O[1] + A[1]) / 2
    nx, ny = _unit(A[1] - O[1], -(A[0] - O[0]))
    b += T(mx + 14 * nx, my + 14 * ny, r_lab)
    return svg(fr.w, fr.h, b)


def numberline_fig(lo, hi, marks=(), W=340, H=60):
    """marks: list of (value, filled, direction) direction -1 left arrow, 1 right, or (a, b) segment"""
    sx = (W - 40) / (hi - lo)

    def X(v):
        return 20 + (v - lo) * sx
    b = L(10, 30, W - 10, 30)
    for v in range(lo, hi + 1):
        b += L(X(v), 25, X(v), 35) + T(X(v), 47, str(v), size=11)
    return svg(W, H, b)
