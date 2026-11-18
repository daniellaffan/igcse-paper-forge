"""Shared helpers for the 4PM1 Further Pure Mathematics generator.

Template registry, question/part/mark-scheme builders, LaTeX formatting of
sympy objects and the SVG drawing helpers (curves, regions, triangles,
sectors, 3D solids, vectors, graph paper).  Every numeric answer is computed
in the templates with sympy / Fraction and passed in here."""
import math
import re
from fractions import Fraction as F

import sympy as sp

from common import fmt_num, row

TEMPLATES = []
NOT_ACC = "Diagram NOT accurately drawn"
x, y, t, k, n = sp.symbols("x y t k n")


def tpl(sub, qtype, n=11):
    def deco(f):
        TEMPLATES.append({"f": f, "sub": "fm." + sub, "qtype": qtype, "n": n, "name": f.__name__})
        return f
    return deco


def P(label, text, marks, prefix=None, space="working", lines=None, figs=None, parts=None):
    if parts:
        return {"label": label, "text": text, "marks": 0, "parts": parts}
    p = {"label": label, "text": text, "marks": marks, "space": space}
    if prefix is not None:
        p["answer_prefix"] = prefix
    if lines is not None:
        p["lines"] = lines
    if figs:
        p["figures"] = figs
    return p


def R(part, answer, marks, notes=None):
    return row(part, answer, marks, notes)


def Q(*, parts, rows, values, diff, cw, refs, intro=None, figs=None, general=None, ao=None,
      method="sympy (exact symbolic solution, numeric values evaluated from the exact form)"):
    ms = {"style": "maths", "rows": rows}
    if general:
        ms["general"] = general
    return {"intro": intro, "parts": parts, "markscheme": ms, "difficulty": diff, "command_word": cw,
            "spec_refs": refs, "figures": figs, "ao": ao,
            "answer": {"method": method, "values": {kk: js(v) for kk, v in values.items()}, "checked": True}}


def js(v):
    if isinstance(v, bool) or v is None or isinstance(v, (int, str)):
        return v
    if isinstance(v, float):
        return float(fmt_num(v, sf=12)) if v != 0 else 0.0
    if isinstance(v, F):
        return v.numerator if v.denominator == 1 else f"{v.numerator}/{v.denominator}"
    if isinstance(v, (list, tuple)):
        return [js(a) for a in v]
    if isinstance(v, dict):
        return {str(a): js(b) for a, b in v.items()}
    if isinstance(v, sp.Basic):
        if v.is_Integer:
            return int(v)
        return str(v)
    return str(v)


def pick(r, *opts):
    return r.choice(opts)


# ------------------------------------------------------------------ formatting

def tex(e):
    """LaTeX for a sympy expression / number, tidy for KaTeX."""
    if isinstance(e, F):
        e = sp.Rational(e.numerator, e.denominator)
    if isinstance(e, int):
        return str(e)
    s = sp.latex(sp.sympify(e))
    s = s.replace("\\left(", "(").replace("\\right)", ")").replace("\\log", "\\ln")
    s = re.sub(r"(\\(?:ln|sin|cos|tan)(?:\^\{\d+\})?)\{\((.+?) \)\}", lambda m_: f"{m_.group(1)}({m_.group(2)})"
               if len(m_.group(2).replace(" ", "")) > 1 else f"{m_.group(1)} {m_.group(2)}", s)
    return s


def sf(v, k=3):
    return fmt_num(float(v), sf=k)


def dp(v, k=2):
    return fmt_num(float(v), dp=k)


def fr(q):
    """LaTeX fraction for a rational."""
    q = sp.Rational(q)
    if q.q == 1:
        return str(q.p)
    s = "-" if q < 0 else ""
    return f"{s}\\frac{{{abs(q.p)}}}{{{q.q}}}"


def sg(c, first=False):
    """' + 3' / ' - 3' for a coefficient as a constant term."""
    c = sp.Rational(c)
    if first:
        return fr(c)
    return f" + {fr(c)}" if c >= 0 else f" - {fr(-c)}"


def poly(cs, var="x"):
    """Polynomial from coefficient list, highest power first."""
    deg = len(cs) - 1
    e = sum(sp.Rational(c) * sp.Symbol(var) ** (deg - i) for i, c in enumerate(cs))
    return tex(sp.expand(e))


def lin(a, b, var="x"):
    return tex(sp.Rational(a) * sp.Symbol(var) + sp.Rational(b))


def ordinal(k):
    """1 -> 1st, 2 -> 2nd, 3 -> 3rd, 11 -> 11th, 23 -> 23rd."""
    k = int(k)
    suf = "th" if 10 <= k % 100 <= 20 else {1: "st", 2: "nd", 3: "rd"}.get(k % 10, "th")
    return f"{k}{suf}"


def xpow(k, var="x"):
    """LaTeX for var^k with the trivial powers tidied: x^0 -> 1, x^1 -> x."""
    k = int(k)
    return "1" if k == 0 else var if k == 1 else f"{var}^{{{k}}}"


def nz(r, lo, hi, excl=(0,)):
    while True:
        v = r.randint(lo, hi)
        if v not in excl:
            return v


def deg(v):
    return f"{v}^\\circ"


def name_ctx(r):
    return r.choice(["Ama", "Bilal", "Chen", "Dimitri", "Esi", "Farah", "Goran", "Hana", "Imran", "Jun", "Kofi",
                     "Leila", "Mateo", "Nadia", "Omar", "Priya", "Rui", "Sana", "Tariq", "Yusuf", "Zara"])


# ------------------------------------------------------------------ SVG primitives

def svg(w, h, body, fs=13):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" font-family="serif" '
            f'font-size="{fs}" fill="none" stroke="currentColor" stroke-width="1.4" '
            f'stroke-linejoin="round" stroke-linecap="round">{body}</svg>')


def T(px, py, s, anchor="middle", it=False, size=None):
    st = ' font-style="italic"' if it else ""
    sz = f' font-size="{size}"' if size else ""
    s = str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return (f'<text x="{px:.1f}" y="{py:.1f}" text-anchor="{anchor}" dominant-baseline="middle" '
            f'fill="currentColor" stroke="none"{st}{sz}>{s}</text>')


def L(x1, y1, x2, y2, w=None, dash=None):
    a = f' stroke-width="{w}"' if w else ""
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}"{a}{d}/>'


def PL(pts, close=False, w=None, dash=None, fill=None, op=None):
    tag = "polygon" if close else "polyline"
    a = f' stroke-width="{w}"' if w else ""
    d = f' stroke-dasharray="{dash}"' if dash else ""
    f_ = f' fill="{fill}"' if fill else ""
    o = f' fill-opacity="{op}"' if op else ""
    ps = " ".join(f"{a_:.1f},{b_:.1f}" for a_, b_ in pts)
    return f'<{tag} points="{ps}"{a}{d}{f_}{o}/>'


def DOT(px, py, r=2.4):
    return f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{r}" fill="currentColor" stroke="none"/>'


def ARROW(x1, y1, x2, y2, head=7, mid=False):
    ang = math.atan2(y2 - y1, x2 - x1)
    hx, hy = ((x1 + x2) / 2, (y1 + y2) / 2) if mid else (x2, y2)
    if mid:
        hx += head / 2 * math.cos(ang)
        hy += head / 2 * math.sin(ang)
    p1 = (hx - head * math.cos(ang - 0.4), hy - head * math.sin(ang - 0.4))
    p2 = (hx - head * math.cos(ang + 0.4), hy - head * math.sin(ang + 0.4))
    return L(x1, y1, x2, y2) + PL([p1, (hx, hy), p2], close=True, fill="currentColor")


def fig(s, width=90, note=NOT_ACC, caption=None):
    f = {"type": "svg", "svg": s, "width": width}
    if note:
        f["note"] = note
    if caption:
        f["caption"] = caption
    return f


def table(headers, rows, caption=None):
    f = {"type": "table", "headers": [str(h) for h in headers], "rows": [[str(c) for c in r_] for r_ in rows]}
    if caption:
        f["caption"] = caption
    return f


# ------------------------------------------------------------------ curve sketches

class Axes:
    """Maps maths coordinates to an SVG box and draws curves on axes."""

    def __init__(self, xr, yr, W=320, H=240, pad=26):
        self.x0, self.x1 = xr
        self.y0, self.y1 = yr
        self.W, self.H, self.pad = W, H, pad
        self.items = []

    def X(self, v):
        return self.pad + (v - self.x0) / (self.x1 - self.x0) * (self.W - 2 * self.pad)

    def Y(self, v):
        return self.H - self.pad - (v - self.y0) / (self.y1 - self.y0) * (self.H - 2 * self.pad)

    def axes(self, origin=True, xl="x", yl="y"):
        ox = self.X(0) if self.x0 <= 0 <= self.x1 else self.X(self.x0)
        oy = self.Y(0) if self.y0 <= 0 <= self.y1 else self.Y(self.y0)
        self.items.append(ARROW(self.pad - 8, oy, self.W - self.pad + 12, oy, 6))
        self.items.append(ARROW(ox, self.H - self.pad + 8, ox, self.pad - 12, 6))
        self.items.append(T(self.W - self.pad + 16, oy + 2, xl, "start", it=True))
        self.items.append(T(ox, self.pad - 20, yl, it=True))
        if origin:
            self.items.append(T(ox - 9, oy + 11, "O"))

    def curve(self, f, a=None, b=None, nn=240, w=1.7, dash=None):
        a = self.x0 if a is None else a
        b = self.x1 if b is None else b
        seg, segs = [], []
        ylo = self.y0 - (self.y1 - self.y0) * 0.02
        yhi = self.y1 + (self.y1 - self.y0) * 0.02
        for i in range(nn + 1):
            xv = a + (b - a) * i / nn
            try:
                yv = float(f(xv))
            except (ZeroDivisionError, ValueError, OverflowError):
                yv = None
            if yv is None or not math.isfinite(yv) or yv < ylo or yv > yhi:
                if len(seg) > 1:
                    segs.append(seg)
                seg = []
                continue
            seg.append((self.X(xv), self.Y(yv)))
        if len(seg) > 1:
            segs.append(seg)
        for s_ in segs:
            self.items.append(PL(s_, w=w, dash=dash))

    def vline(self, xv, dash="5,4", label=None):
        self.items.append(L(self.X(xv), self.Y(self.y0), self.X(xv), self.Y(self.y1), w=1, dash=dash))
        if label:
            self.items.append(T(self.X(xv) + 4, self.Y(self.y1) + 6, label, "start", size=11))

    def hline(self, yv, dash="5,4", label=None):
        self.items.append(L(self.X(self.x0), self.Y(yv), self.X(self.x1), self.Y(yv), w=1, dash=dash))
        if label:
            self.items.append(T(self.X(self.x1) - 2, self.Y(yv) - 8, label, "end", size=11))

    def shade(self, f, a, b, g=None, nn=80):
        top = [(self.X(a + (b - a) * i / nn), self.Y(float(f(a + (b - a) * i / nn)))) for i in range(nn + 1)]
        if g is None:
            bot = [(self.X(b), self.Y(0)), (self.X(a), self.Y(0))]
        else:
            bot = [(self.X(a + (b - a) * i / nn), self.Y(float(g(a + (b - a) * i / nn)))) for i in range(nn, -1, -1)]
        self.items.append(PL(top + bot, close=True, w=0.01, fill="currentColor", op="0.18"))

    def line(self, m, c, w=1.4):
        self.curve(lambda v: m * v + c, w=w)

    def point(self, xv, yv, lab=None, dx=8, dy=-9, anchor="start"):
        self.items.append(DOT(self.X(xv), self.Y(yv)))
        if lab:
            self.items.append(T(self.X(xv) + dx, self.Y(yv) + dy, lab, anchor))

    def label(self, xv, yv, s, anchor="middle", it=False, size=None):
        self.items.append(T(self.X(xv), self.Y(yv), s, anchor, it=it, size=size))

    def svg(self):
        return svg(self.W, self.H, "".join(self.items))


def grid_paper(xr, yr, xstep, ystep, W=420, H=360, minor=5, xl="x", yl="y"):
    """Graph paper with labelled axes for 'draw the graph' questions."""
    pad = 34
    x0, x1 = xr
    y0, y1 = yr

    def X(v):
        return pad + (v - x0) / (x1 - x0) * (W - 2 * pad)

    def Y(v):
        return H - pad - (v - y0) / (y1 - y0) * (H - 2 * pad)
    it = []
    nx = round((x1 - x0) / xstep * minor)
    ny = round((y1 - y0) / ystep * minor)
    for i in range(nx + 1):
        xv = x0 + i * xstep / minor
        it.append(L(X(xv), Y(y0), X(xv), Y(y1), w=0.6 if i % minor == 0 else 0.2))
    for j in range(ny + 1):
        yv = y0 + j * ystep / minor
        it.append(L(X(x0), Y(yv), X(x1), Y(yv), w=0.6 if j % minor == 0 else 0.2))
    ox = X(0) if x0 <= 0 <= x1 else X(x0)
    oy = Y(0) if y0 <= 0 <= y1 else Y(y0)
    it.append(L(X(x0), oy, X(x1), oy, w=1.4))
    it.append(L(ox, Y(y0), ox, Y(y1), w=1.4))
    for i in range(round((x1 - x0) / xstep) + 1):
        xv = x0 + i * xstep
        if abs(xv) > 1e-9:
            it.append(T(X(xv), oy + 11, fmt_num(xv), size=10))
    for j in range(round((y1 - y0) / ystep) + 1):
        yv = y0 + j * ystep
        if abs(yv) > 1e-9:
            it.append(T(ox - 5, Y(yv), fmt_num(yv), "end", size=10))
    it.append(T(ox - 7, oy + 11, "O", size=10))
    it.append(T(X(x1) + 10, oy, xl, "start", it=True))
    it.append(T(ox, Y(y1) - 12, yl, it=True))
    return svg(W, H, "".join(it))


# ------------------------------------------------------------------ geometry figures

def _fit(pts, W, H, pad=30):
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    sx = (W - 2 * pad) / max(1e-9, max(xs) - min(xs))
    sy = (H - 2 * pad) / max(1e-9, max(ys) - min(ys))
    s = min(sx, sy)
    ox = (W - s * (max(xs) - min(xs))) / 2
    oy = (H - s * (max(ys) - min(ys))) / 2
    return [(ox + (p[0] - min(xs)) * s, H - (oy + (p[1] - min(ys)) * s)) for p in pts]


def _out(p, c, d=14):
    vx, vy = p[0] - c[0], p[1] - c[1]
    m = math.hypot(vx, vy) or 1
    return p[0] + vx / m * d, p[1] + vy / m * d


def triangle_fig(A, B, C, names=("A", "B", "C"), sides=None, angles=None, W=300, H=220):
    """sides: dict {(i,j): label}; angles: dict {i: label}.  Points in maths coords."""
    pts = _fit([A, B, C], W, H, pad=36)
    c = (sum(p[0] for p in pts) / 3, sum(p[1] for p in pts) / 3)
    it = [PL(pts, close=True)]
    for i, nm in enumerate(names):
        q = _out(pts[i], c, 14)
        it.append(T(q[0], q[1], nm))
    for (i, j), lab in (sides or {}).items():
        m = ((pts[i][0] + pts[j][0]) / 2, (pts[i][1] + pts[j][1]) / 2)
        q = _out(m, c, 15)
        it.append(T(q[0], q[1], lab, size=12))
    for i, lab in (angles or {}).items():
        v = pts[i]
        a1 = math.atan2(pts[(i + 1) % 3][1] - v[1], pts[(i + 1) % 3][0] - v[0])
        a2 = math.atan2(pts[(i + 2) % 3][1] - v[1], pts[(i + 2) % 3][0] - v[0])
        rr = 22
        p1 = (v[0] + rr * math.cos(a1), v[1] + rr * math.sin(a1))
        p2 = (v[0] + rr * math.cos(a2), v[1] + rr * math.sin(a2))
        da = (a2 - a1) % (2 * math.pi)
        sweep = 1 if da < math.pi else 0
        it.append(f'<path d="M{p1[0]:.1f},{p1[1]:.1f} A{rr},{rr} 0 0 {sweep} {p2[0]:.1f},{p2[1]:.1f}" stroke-width="1"/>')
        mid = a1 + (da if da < math.pi else da - 2 * math.pi) / 2
        it.append(T(v[0] + 36 * math.cos(mid), v[1] + 36 * math.sin(mid), lab, size=12))
    return svg(W, H, "".join(it))


def sector_fig(theta, r_lab, ang_lab, W=260, H=220, names=("O", "A", "B"), chord=False, shade=None,
               extra=None):
    """Sector of angle theta (radians, < 2pi) drawn with OA horizontal."""
    th = float(theta)
    R_ = 1.0
    pts = [(0, 0), (R_, 0), (R_ * math.cos(th), R_ * math.sin(th))]
    arc = [(R_ * math.cos(th * i / 60), R_ * math.sin(th * i / 60)) for i in range(61)]
    allp = pts + arc
    fp = _fit(allp, W, H, pad=34)
    O, A, B = fp[0], fp[1], fp[2]
    arcp = fp[3:]
    it = []
    if shade == "segment":
        it.append(PL(arcp, close=True, w=0.01, fill="currentColor", op="0.18"))
    elif shade == "sector":
        it.append(PL([O] + arcp, close=True, w=0.01, fill="currentColor", op="0.18"))
    it += [L(*O, *A), L(*O, *B), PL(arcp)]
    if chord:
        it.append(L(*A, *B))
    c = ((O[0] + A[0] + B[0]) / 3, (O[1] + A[1] + B[1]) / 3)
    for p, nm in zip((O, A, B), names):
        q = _out(p, c, 14)
        it.append(T(q[0], q[1], nm))
    it.append(T((O[0] + A[0]) / 2, O[1] + 13, r_lab, size=12))
    rr = 24
    it.append(f'<path d="M{O[0] + rr:.1f},{O[1]:.1f} A{rr},{rr} 0 0 0 {O[0] + rr * math.cos(th):.1f},'
              f'{O[1] - rr * math.sin(th):.1f}" stroke-width="1"/>')
    it.append(T(O[0] + 38 * math.cos(th / 2), O[1] - 38 * math.sin(th / 2), ang_lab, size=12))
    if extra:
        it.append(extra(fp))
    return svg(W, H, "".join(it))


def solid_fig(verts, edges, hidden=(), labels=None, W=320, H=250, extra_lines=(), dims=None):
    """verts: name -> (x, y, z); oblique projection; edges: list of name pairs."""
    def proj(p):
        return (p[0] + 0.45 * p[1], p[2] + 0.32 * p[1])
    names = list(verts)
    pp = _fit([proj(verts[nm]) for nm in names], W, H, pad=34)
    P2 = dict(zip(names, pp))
    cx = sum(p[0] for p in pp) / len(pp)
    cy = sum(p[1] for p in pp) / len(pp)
    it = []
    for a, b in edges:
        it.append(L(*P2[a], *P2[b], dash="5,4" if (a, b) in hidden or (b, a) in hidden else None))
    for a, b in extra_lines:
        it.append(L(*P2[a], *P2[b], w=1, dash="2,3"))
    for nm in names:
        if labels is None or nm in labels:
            q = _out(P2[nm], (cx, cy), 13)
            it.append(T(q[0], q[1], labels.get(nm, nm) if isinstance(labels, dict) else nm))
    for (a, b), lab in (dims or {}).items():
        m = ((P2[a][0] + P2[b][0]) / 2, (P2[a][1] + P2[b][1]) / 2)
        q = _out(m, (cx, cy), 14)
        it.append(T(q[0], q[1], lab, size=12))
    return svg(W, H, "".join(it))


def points_fig(pts, segs, arrows=(), W=300, H=220, labels=None, sides=None):
    """Generic 2D figure: pts name->(x,y); segs list of pairs; arrows: pairs with mid arrowheads."""
    names = list(pts)
    fp = dict(zip(names, _fit([pts[nm] for nm in names], W, H, pad=34)))
    cx = sum(p[0] for p in fp.values()) / len(fp)
    cy = sum(p[1] for p in fp.values()) / len(fp)
    it = []
    for a, b in segs:
        if (a, b) in arrows:
            it.append(ARROW(*fp[a], *fp[b], 7, mid=True))
        else:
            it.append(L(*fp[a], *fp[b]))
    for nm in names:
        q = _out(fp[nm], (cx, cy), 13)
        it.append(T(q[0], q[1], (labels or {}).get(nm, nm)))
    for (a, b), lab in (sides or {}).items():
        m = ((fp[a][0] + fp[b][0]) / 2, (fp[a][1] + fp[b][1]) / 2)
        q = _out(m, (cx, cy), 15)
        it.append(T(q[0], q[1], lab, size=12, it=True))
    return svg(W, H, "".join(it))


def lin2(a, b, c=0, u="x", v="y"):
    """a x + b y (+ c) without '1x' or '+ -'."""
    return tex(sp.Rational(a) * sp.Symbol(u) + sp.Rational(b) * sp.Symbol(v) + sp.Rational(c))


def kq(A, B, C, var="x"):
    """Quadratic in x whose coefficients are expressions in k, printed in descending powers of x."""
    out = []
    for e, pw in ((A, 2), (B, 1), (C, 0)):
        e = sp.expand(e)
        if e == 0:
            continue
        xs = {2: f"{var}^2", 1: var, 0: ""}[pw]
        if pw == 0:
            s = tex(e)
            out.append(s if s.startswith("-") else "+ " + s)
            continue
        if e.is_number:
            s = "" if e == 1 else ("-" if e == -1 else tex(e))
            out.append((s if s.startswith("-") else "+ " + s) + xs)
        else:
            out.append(f"+ ({tex(e)}){xs}")
    s = " ".join(out).strip()
    if s.startswith("+ "):
        s = s[2:]
    return s.replace("+ -", "- ")


def logx(base, val):
    """'\\log_b v' for a rational v."""
    return f"\\log_{{{base}}} {fr(val) if sp.Rational(val).q == 1 else '\\left(' + fr(val) + '\\right)'}"
