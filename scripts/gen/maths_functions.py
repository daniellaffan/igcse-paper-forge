"""Sequences, functions and graphs templates (spec section 3)."""
import math
from fractions import Fraction as F

import sympy as sp

from maths_util import (tpl, P, R, Q, sf, dp, num, ftex, poly_tex, lin_tex, name, fig, table, grid_fig, curve,
                        PL, L, T, DOT, ARROW, NOT_ACC)
from maths_algebra import nz, lx

x, t = sp.symbols("x t")


# ---------------------------------------------------------------- 3.1 sequences
@tpl("functions.sequences", "short", n=14)
def nth_term(r):
    a, d = nz(r, -10, 15), nz(r, -7, 9)
    terms = [a + d * i for i in range(5)]
    c = a - d
    k = r.randint(20, 60)
    kind = r.choice(["nth", "nth", "term"])
    if kind == "nth":
        return Q(intro=f"Here are the first five terms of an arithmetic sequence.\n\n$${', \\;'.join(map(str, terms))}, \\;\\ldots$$",
                 parts=[P("a", "Find an expression, in terms of $n$, for the $n$th term of this sequence.", 2, prefix=""),
                        P("b", f"Work out the {k}th term of the sequence.", 1, prefix="")],
                 rows=[R("a", f"${d}n + k$ for any $k$", "M1", "or $" + f"{a} + (n - 1) \\times {d}" + "$"),
                       R("a", f"${lin_tex(d, c, 'n')}$", "A1", "oe"),
                       R("b", str(a + d * (k - 1)), "B1", "ft their (a)")],
                 values={"nth": f"{d}n+{c}", "term": a + d * (k - 1)}, diff="4-6", cw="Find", refs=["F3.1C", "H3.1B"])
    val = a + d * (k - 1)
    return Q(intro=f"The $n$th term of a sequence is ${lin_tex(d, c, 'n')}$.",
             parts=[P("a", "Write down the first three terms of the sequence.", 1, space="lines", lines=1),
                    P("b", f"Is {val + (1 if r.random() < 0.5 else 0)} a term of the sequence? Show how you decide.", 2, space="lines", lines=2)],
             rows=[R("a", ", ".join(map(str, terms[:3])), "B1", ""),
                   R("b", f"${lin_tex(d, c, 'n')} = $ the given number solved for $n$", "M1", "or listing terms either side"),
                   R("b", "correct conclusion with correct value of $n$ (or the terms either side)", "A1", "")],
             values={"terms": terms[:3]}, diff="4-6", cw="Write down", refs=["F3.1A", "F3.1C"])


@tpl("functions.sequences", "problem", n=7)
def ap_two_terms(r):
    a, d = nz(r, -10, 20), nz(r, -6, 9)
    p, q = sorted(r.sample(range(2, 12), 2))
    tp, tq = a + (p - 1) * d, a + (q - 1) * d
    N = r.randint(20, 60)
    S = F(N, 2) * (2 * a + (N - 1) * d)
    return Q(intro=f"The {_ord(p)} term of an arithmetic sequence is {tp}.\n\nThe {_ord(q)} term of the sequence is {tq}.",
             parts=[P("", f"Find the sum of the first {N} terms of the sequence.", 4, prefix="")],
             rows=[R("", f"$a + {p - 1}d = {tp}$ and $a + {q - 1}d = {tq}$", "M1", "for two correct equations or $(" + f"{tq} - {tp}) \\div {q - p}" + "$"),
                   R("", f"$d = {d}$, $a = {a}$", "A1", "for both values"),
                   R("", f"$\\frac{{{N}}}{{2}}[2 \\times {a} + ({N} - 1) \\times {d}]$", "M1", "ft their $a$ and $d$"),
                   R("", str(S), "A1", "cao")],
             values={"a": a, "d": d, "sum": S}, diff="7-9", cw="Find", refs=["H3.1A", "H3.1C"])


def _ord(n):
    return f"{n}{'th' if 10 <= n % 100 <= 20 else {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')}"


@tpl("functions.sequences", "problem", n=7)
def ap_context(r):
    a, d = r.randint(5, 40), r.randint(2, 8)
    target = r.randint(800, 4000)
    # least n with S_n > target
    n_ = 1
    while F(n_, 2) * (2 * a + (n_ - 1) * d) <= target:
        n_ += 1
    nm = name(r)
    ctx = r.choice([("saves", "in week 1", "more each week than the week before", "weeks", "saved"),
                    ("runs", "on day 1", "further each day than the day before", "days", "run")])
    unit = " km" if ctx[0] == "runs" else ""
    if ctx[0] == "runs":
        a, d = r.randint(2, 6), r.choice([F(1, 2), 1])
        target = r.randint(60, 300)
        n_ = 1
        while F(n_, 2) * (2 * a + (n_ - 1) * d) <= target:
            n_ += 1
    s1 = F(n_ - 1, 2) * (2 * a + (n_ - 2) * d)
    s2 = F(n_, 2) * (2 * a + (n_ - 1) * d)
    curw = "" if ctx[0] == "runs" else " " + r.choice(["dollars", "euros", "rupees"])
    return Q(intro=f"{nm} {ctx[0]} {num(float(a))}{unit}{curw} {ctx[1]}. Each {ctx[3][:-1]} {nm} {ctx[0]} {num(float(d))}{unit}{curw} {ctx[2]}.",
             parts=[P("", f"Work out the least number of {ctx[3]} it takes for the total amount {ctx[4]} to be more than {target}{unit}{curw}.", 4, prefix="")],
             rows=[R("", f"$\\frac{{n}}{{2}}[2 \\times {num(float(a))} + (n - 1) \\times {num(float(d))}] > {target}$", "M1", "or a list of cumulative totals with at least 4 correct"),
                   R("", f"$S_{{{n_ - 1}}} = {num(float(s1))}$ or $S_{{{n_}}} = {num(float(s2))}$", "M1", "for evaluating the sum for a value of $n$ near the answer, or solving the quadratic"),
                   R("", f"$S_{{{n_ - 1}}} = {num(float(s1))}$ and $S_{{{n_}}} = {num(float(s2))}$", "A1", "for showing the values either side of the target"),
                   R("", str(n_), "A1", "cao")],
             values={"n": n_}, diff="7-9", cw="Work out", refs=["H3.1C", "H3.1A"])


@tpl("functions.sequences", "proof", n=7)
def ap_show_sum(r):
    a, d = r.randint(1, 12), r.randint(2, 9)
    Sn = sp.expand(sp.Rational(1, 2) * sp.Symbol("n") * (2 * a + (sp.Symbol("n") - 1) * d))
    n = sp.Symbol("n")
    g = sp.factor(Sn)
    terms = [a + d * i for i in range(4)]
    return Q(intro=f"Here are the first four terms of an arithmetic series.\n\n$${' + '.join(map(str, terms))} + \\ldots$$",
             parts=[P("", f"Show that the sum of the first $n$ terms of the series is $${lx(g)}$$", 2, space="working")],
             rows=[R("", f"$\\frac{{n}}{{2}}[2 \\times {a} + (n - 1) \\times {d}]$", "M1", "for correct substitution into the formula for $S_n$"),
                   R("", f"$\\frac{{n}}{{2}}({lin_tex(d, 2 * a - d, 'n')})$ leading to ${lx(g)}$", "A1", "dep on M1, with correct simplification shown")],
             values={"Sn": str(Sn)}, diff="7-9", cw="Show that", refs=["H3.1C"])


@tpl("functions.sequences", "proof", n=7)
def ap_not_term(r):
    a, d = r.randint(2, 15), r.randint(3, 9)
    c = a - d
    k = r.randint(30, 120)
    val = a + d * k + r.randint(1, d - 1)
    return Q(intro=f"The $n$th term of an arithmetic sequence is ${lin_tex(d, c, 'n')}$.",
             parts=[P("", f"Show that {val} cannot be a term of this sequence.", 2, space="working")],
             rows=[R("", f"${lin_tex(d, c, 'n')} = {val}$ so $n = {ftex(F(val - c, d))}$", "M1", "for setting up and solving an equation, or finding the terms either side, eg " +
                     f"{a + d * (k - 1)} and {a + d * k}"),
                   R("", "$n$ is not a whole number, so it is not a term", "A1", "dep on M1; conclusion required")],
             values={"n": F(val - c, d)}, diff="4-6", cw="Show that", refs=["F3.1C", "H3.1B"])


# ---------------------------------------------------------------- 3.2 functions
def fpick(r):
    kind = r.choice(["lin", "lin", "quad", "recip", "root"])
    if kind == "lin":
        a, b = nz(r, -5, 6, (0, 1)), nz(r, -9, 9)
        return a * x + b, kind
    if kind == "quad":
        a, b = r.choice([1, 2, 3]), nz(r, -9, 9)
        return a * x ** 2 + b, kind
    if kind == "recip":
        a, b = r.randint(1, 9), nz(r, -6, 6)
        return sp.Integer(a) / (x + b), kind
    a = r.randint(1, 9)
    return sp.sqrt(x + a), kind


@tpl("functions.functions", "short", n=14)
def f_evaluate(r):
    f, kf = fpick(r)
    g, kg = fpick(r)
    if kf == kg:
        return None
    v1 = r.randint(-4, 6)
    v2 = r.randint(-3, 5)
    try:
        fv = f.subs(x, v1)
        gv = g.subs(x, v2)
        fgv = f.subs(x, gv)
    except Exception:
        return None
    if any(not e.is_real or e.has(sp.zoo) or e.has(sp.nan) for e in (fv, gv, fgv)):
        return None
    if any((not e.is_rational) for e in (fv, gv, fgv)):
        return None
    return Q(intro=f"$\\mathrm{{f}}(x) = {lx(f)}$\n\n$\\mathrm{{g}}(x) = {lx(g)}$",
             parts=[P("a", f"Find $\\mathrm{{f}}({v1})$", 1, prefix=""),
                    P("b", f"Find $\\mathrm{{fg}}({v2})$", 2, prefix="")],
             rows=[R("a", f"${lx(fv)}$", "B1", "oe"),
                   R("b", f"$\\mathrm{{g}}({v2}) = {lx(gv)}$", "M1", "or a correct expression for fg(x)"),
                   R("b", f"${lx(fgv)}$", "A1", "oe")],
             values={"f": fv, "fg": fgv}, diff="4-6", cw="Find", refs=["H3.2B", "H3.2D"])


def inverse(f):
    y_ = sp.Symbol("y")
    s = sp.solve(sp.Eq(y_, f), x)
    if len(s) != 1:
        return None
    return s[0].subs(y_, x)


@tpl("functions.functions", "algebra", n=7)
def f_inverse(r):
    kind = r.choice(["lin", "frac", "frac2"])
    if kind == "lin":
        a, b, c = nz(r, -7, 7, (0, 1)), nz(r, -9, 9), r.choice([1, 2, 3, 4, 5])
        f = (a * x + b) / c
        ftexs = f"\\frac{{{lin_tex(a, b)}}}{{{c}}}" if c != 1 else lin_tex(a, b)
    elif kind == "frac":
        a, b = r.randint(1, 9), nz(r, -6, 6)
        f = a / (x + b)
        ftexs = f"\\frac{{{a}}}{{{lin_tex(1, b)}}}"
    else:
        a, b, c = r.randint(1, 6), nz(r, -6, 6), nz(r, -5, 5)
        if a == c:
            return None
        f = (a * x + b) / (x + c) if r.random() < 0.6 else (a * x + b) / (x - c)
        ftexs = lx(f)
    inv = sp.simplify(inverse(f))
    if inv is None:
        return None
    return Q(intro=f"$\\mathrm{{f}}(x) = {ftexs}$",
             parts=[P("", "Express the inverse function $\\mathrm{f}^{-1}$ in the form $\\mathrm{f}^{-1}(x) = \\ldots$", 3 if kind != "lin" else 2, prefix="$\\mathrm{f}^{-1}(x) =$ ")],
             rows=([R("", f"$y = {ftexs}$ rearranged to make $x$ the subject, or $x = {ftexs.replace('x', 'y')}$ with a correct first step", "M1", "")] +
                   ([R("", "terms in the subject gathered and factorised", "M1", "")] if kind != "lin" else []) +
                   [R("", f"${lx(inv)}$", "A1", "oe, must be in terms of $x$")]),
             values={"inverse": str(inv)}, diff="7-9" if kind != "lin" else "4-6", cw="Express", refs=["H3.2D"])


@tpl("functions.functions", "algebra", n=7)
def f_composite_solve(r):
    a, b = nz(r, -5, 5, (0, 1)), nz(r, -8, 8)
    c = r.choice([1, 2, 3])
    d = nz(r, -6, 6)
    f = a * x + b
    g = c * x ** 2 + d if r.random() < 0.5 else (x + d) ** 2
    fg = sp.expand(f.subs(x, g))
    gf = sp.expand(g.subs(x, f))
    use = r.choice(["fg", "gf"])
    e = fg if use == "fg" else gf
    target = e.subs(x, r.randint(-4, 4))
    sols = sp.solve(sp.Eq(e, target), x)
    sols = [s for s in sols if s.is_real]
    if not sols:
        return None
    return Q(intro=f"$\\mathrm{{f}}(x) = {lx(f)}$\n\n$\\mathrm{{g}}(x) = {lx(g)}$",
             parts=[P("", f"Solve $\\mathrm{{{use}}}(x) = {target}$", 4, prefix="")],
             rows=[R("", f"$\\mathrm{{{use}}}(x) = {lx(f.subs(x, g) if use == 'fg' else g.subs(x, f))}$", "M1", "for a correct composite expression"),
                   R("", f"${lx(e)} = {target}$", "M1", "for setting up a correct equation"),
                   R("", "a correct method to solve their equation", "M1", ""),
                   R("", ", ".join(f"$x = {lx(s)}$" for s in sorted(sols, key=lambda v: float(v))), "A1", "")],
             values={"solutions": [str(s) for s in sols]}, diff="7-9", cw="Solve", refs=["H3.2D"])


@tpl("functions.functions", "structured", n=14)
def f_structured(r):
    a, b = r.randint(1, 9), nz(r, -6, 6)
    f = a / (x + b)
    c, d = nz(r, -5, 6, (0, 1)), nz(r, -8, 8)
    g = c * x + d
    v = r.choice([q for q in range(-3, 8) if q != -b])
    fv = f.subs(x, v)
    inv = sp.simplify(inverse(g))
    fg = sp.simplify(f.subs(x, g))
    excl = sp.solve(sp.Eq(g, -b), x)[0]
    return Q(intro=f"$\\mathrm{{f}}(x) = \\frac{{{a}}}{{{lin_tex(1, b)}}}$\n\n$\\mathrm{{g}}(x) = {lin_tex(c, d)}$",
             parts=[P("a", f"Find $\\mathrm{{f}}({v})$", 1, prefix=""),
                    P("b", "Which value of $x$ can never be in the domain of f?", 1, prefix=""),
                    P("c", "Find $\\mathrm{g}^{-1}(x)$", 2, prefix="$\\mathrm{g}^{-1}(x) =$ "),
                    P("d", "Find $\\mathrm{fg}(x)$. Give your answer as a single fraction.", 2, prefix="$\\mathrm{fg}(x) =$ "),
                    P("e", "Write down the value of $x$ that has to be left out of the domain of fg.", 1, prefix="")],
             rows=[R("a", f"${lx(fv)}$", "B1", "oe"), R("b", f"${-b}$", "B1", ""),
                   R("c", f"$x = {lin_tex(c, d, 'y')}$ or $\\frac{{x - ({d})}}{{{c}}}$", "M1", ""),
                   R("c", f"${lx(inv)}$", "A1", "oe"),
                   R("d", f"$\\frac{{{a}}}{{({lin_tex(c, d)}) {'+' if b > 0 else '-'} {abs(b)}}}$", "M1", ""),
                   R("d", f"${lx(fg)}$", "A1", "oe"),
                   R("e", f"${lx(excl)}$", "B1", "ft their (d)")],
             values={"f": fv, "excluded": -b, "ginv": str(inv), "fg": str(fg), "fg_excl": excl}, diff="7-9",
             cw="Find", refs=["H3.2B", "H3.2C", "H3.2D"])


# ---------------------------------------------------------------- 3.3 straight lines
@tpl("functions.straight-lines", "short", n=7)
def line_read(r):
    m, c = nz(r, -6, 6), nz(r, -9, 9)
    form = r.choice(["std", "re"])
    if form == "std":
        A, B = r.choice([2, 3, 4, 5]), nz(r, -5, 5, (0,))
        # A y = m A x + c A  -> write as  mA x - A y = - cA ... present as  "A y - mA x = cA"
        lhs = f"{A}y {'-' if m * A > 0 else '+'} {abs(m * A)}x = {c * A}"
    else:
        lhs = f"y = {lin_tex(m, c)}"
    return Q(intro=f"The equation of a straight line **L** is $${lhs}$$",
             parts=[P("a", "Find the gradient of **L**.", 1 if form == "re" else 2, prefix=""),
                    P("b", "**L** meets the $y$-axis at the point $Q$. Write down the coordinates of $Q$.", 1, prefix="")],
             rows=([R("a", f"${m}$", "B1", "")] if form == "re" else
                   [R("a", f"$y = {lin_tex(m, c)}$", "M1", "for rearranging to $y = mx + c$ form"), R("a", f"${m}$", "A1", "")]) +
                  [R("b", f"$(0, {c})$", "B1", "")],
             values={"m": m, "c": c}, diff="4-6", cw="Find", refs=["F3.3H", "F3.3G"])


@tpl("functions.straight-lines", "short", n=7)
def midpoint_grad(r):
    p1 = (nz(r, -8, 9), nz(r, -8, 9))
    p2 = (nz(r, -8, 9), nz(r, -8, 9))
    if p1[0] == p2[0]:
        return None
    A, B = r.sample(["A", "B", "P", "Q", "C", "D"], 2)
    mid = (F(p1[0] + p2[0], 2), F(p1[1] + p2[1], 2))
    g = F(p2[1] - p1[1], p2[0] - p1[0])
    return Q(intro=f"${A}$ is the point $({p1[0]}, {p1[1]})$ and ${B}$ is the point $({p2[0]}, {p2[1]})$.",
             parts=[P("a", f"Find the coordinates of the midpoint of ${A}{B}$.", 2, prefix=""),
                    P("b", f"Find the gradient of the line ${A}{B}$.", 1, prefix="")],
             rows=[R("a", f"$\\frac{{{p1[0]} + {p2[0]}}}{{2}}$ or $\\frac{{{p1[1]} + {p2[1]}}}{{2}}$", "M1", "for one correct coordinate"),
                   R("a", f"$({num(float(mid[0]))}, {num(float(mid[1]))})$", "A1", ""),
                   R("b", f"${ftex(g)}$", "B1", "oe")],
             values={"mid": [float(mid[0]), float(mid[1])], "gradient": g}, diff="4-6", cw="Find", refs=["F3.3E", "H3.3F"])


@tpl("functions.straight-lines", "algebra", n=7)
def line_two_points(r):
    m = nz(r, -5, 5)
    c = nz(r, -9, 9)
    x1, x2 = r.sample(range(-5, 7), 2)
    p1, p2 = (x1, m * x1 + c), (x2, m * x2 + c)
    return Q(parts=[P("", f"A straight line goes through $({p1[0]}, {p1[1]})$ and through $({p2[0]}, {p2[1]})$.\n\nFind the equation of this line.\n\nGive your answer in the form $y = mx + c$", 3, prefix="")],
             rows=[R("", f"$\\frac{{{p2[1]} - ({p1[1]})}}{{{p2[0]} - ({p1[0]})}}$ (= {m})", "M1", "for a correct method to find the gradient"),
                   R("", f"${p1[1]} = {m} \\times {p1[0]} + c$ or $y - {p1[1]} = {m}(x - {p1[0]})$", "M1", "ft their gradient"),
                   R("", f"$y = {lin_tex(m, c)}$", "A1", "")],
             values={"m": m, "c": c}, diff="4-6", cw="Find", refs=["H3.3F"])


@tpl("functions.straight-lines", "algebra", n=8)
def line_perp(r):
    m = r.choice([2, 3, 4, -2, -3, F(1, 2), F(-1, 2), F(2, 3), F(-3, 4), 5])
    m = F(m)
    c = nz(r, -8, 8)
    px, py = nz(r, -6, 6), nz(r, -8, 8)
    perp = r.random() < 0.65
    mm = -1 / m if perp else m
    cc = py - mm * px
    if cc.denominator != 1 and r.random() < 0.6:
        return None
    if m.denominator == 1:
        given = f"y = {lin_tex(int(m), c)}"
    else:
        A = m.denominator
        given = f"{A}y = {lin_tex(m.numerator, c * A)}"
    form = "Give your answer in the form $y = mx + c$" if cc.denominator == 1 else "Write your equation as $ax + by = c$, using integer values only."
    if cc.denominator == 1 and mm.denominator == 1:
        ans = f"y = {lin_tex(int(mm), int(cc))}"
    else:
        D = math.lcm(mm.denominator, cc.denominator)
        A_, C_ = mm * D, cc * D
        ans = f"{D}y = {lin_tex(int(A_), int(C_))}" if False else f"{int(-A_)}x + {D}y = {int(C_)}".replace("+ -", "- ")
    return Q(intro=f"The line **L** has equation $${given}$$",
             parts=[P("", f"Line **M** is {'perpendicular' if perp else 'parallel'} to **L**. The point $({px}, {py})$ lies on **M**.\n\nFind an equation for **M**.\n\n{form}", 3, prefix="")],
             rows=[R("", f"gradient of L $= {ftex(m)}$ and {'$-1 \\div ' + ftex(m) + ' = ' + ftex(mm) + '$' if perp else 'same gradient'}", "M1", "for the gradient of the required line"),
                   R("", f"${py} = {ftex(mm)} \\times {px} + c$ or $y - {py} = {ftex(mm)}(x - {px})$", "M1", "ft their gradient"),
                   R("", f"${ans}$", "A1", "oe")],
             values={"m": mm, "c": cc}, diff="7-9" if perp else "4-6", cw="Find", refs=["H3.3G"])


# ---------------------------------------------------------------- 3.3 graphs of functions
def _table_parts(f, xs, hide):
    vals = [f(v) for v in xs]
    row_ = [("" if i in hide else num(vals[i])) for i in range(len(xs))]
    return vals, row_


def _curve_items(f, x0, x1, ymin, ymax, extra=None):
    def it(M):
        s = curve(M, f, x0, x1, ymin, ymax)
        if extra:
            s += extra(M)
        return s
    return it


@tpl("functions.graphs", "graph", n=8)
def plot_quadratic(r):
    a, b, c = r.choice([1, 1, 2, -1]), nz(r, -4, 4), r.randint(-6, 4)
    xs = list(range(-3, 4)) if abs(b) < 3 else list(range(-1, 6)) if b < 0 else list(range(-5, 2))
    f = lambda v: a * v * v + b * v + c
    vals = [f(v) for v in xs]
    hide = r.sample(range(len(xs)), 3)
    ymin = min(vals) - 2
    ymax = max(vals) + 2
    ystep = 2 if ymax - ymin > 16 else 1
    if ymax - ymin > 36:
        return None
    k = r.randint(int(min(vals)) + 1, int(max(vals)) - 1) if max(vals) - min(vals) > 3 else None
    if k is None:
        return None
    roots = sorted(float(s) for s in sp.solve(sp.Eq(a * x ** 2 + b * x + c, k), x) if s.is_real)
    # "the solutions" means every root, so every real root must be readable on the grid
    if not roots or any(not (xs[0] <= v <= xs[-1]) for v in roots):
        return None
    g = grid_fig(xs[0], xs[-1], ymin, ymax, ystep=ystep, minor=5 if ystep == 1 else 4, w=340, h=360)
    eq = poly_tex([a, b, c])
    return Q(intro=f"Here is a table of values for $y = {eq}$",
             figs=[table(["$x$"] + [str(v) for v in xs], [["$y$"] + [("" if i in hide else str(vals[i])) for i in range(len(xs))]])],
             parts=[P("a", "Complete the table of values.", 2, space="table"),
                    P("b", f"On the grid, draw the graph of $y = {eq}$ for all values of $x$ from ${xs[0]}$ to ${xs[-1]}$", 2, space="graph",
                      figs=[fig(g, 85, note=None)]),
                    P("c", f"Use your graph to find estimates of the solutions of the equation ${eq} = {k}$", 2, prefix="")],
             rows=[R("a", ", ".join(f"{vals[i]} (at $x = {xs[i]}$)" for i in sorted(hide)), "B2", "B1 for 1 or 2 correct values"),
                   R("b", "a smooth curve through all their points", "B2", "ft their table if at least B1 scored; B1 for at least 5 points plotted correctly"),
                   R("c", f"line $y = {k}$ drawn or used", "M1", ""),
                   R("c", ", ".join(dp(v, 1) for v in roots), "A1", "ft their graph; allow ±0.2")],
             values={"table": vals, "roots": [round(v, 4) for v in roots]}, diff="4-6", cw="Complete", refs=["F3.3I", "H3.3E"])


@tpl("functions.graphs", "graph", n=8)
def read_cubic(r):
    p, q, s_ = sorted(r.sample(range(-3, 4), 3))
    a = r.choice([1, -1])
    f = lambda v: a * (v - p) * (v - q) * (v - s_)
    xs = [i / 10 for i in range(-35, 36)]
    ys = [f(v) for v in xs]
    ymin, ymax = math.floor(min(ys)) - 1, math.ceil(max(ys)) + 1
    if ymax - ymin > 70:
        return None
    ystep = 5 if ymax - ymin > 30 else 2
    ymin -= ymin % ystep
    ymax += (-ymax) % ystep
    k = r.randint(int(min(ys) / 2), int(max(ys) / 2))
    rts = sp.Poly(sp.expand(a * (x - p) * (x - q) * (x - s_) - k), x).nroots()
    rts = sorted(float(sp.re(z)) for z in rts if abs(sp.im(z)) < 1e-9 and -3.5 <= float(sp.re(z)) <= 3.5)
    if k == 0 or not rts or any(abs(v) > 3.35 for v in rts):
        return None
    cub = sp.expand(a * (x - p) * (x - q) * (x - s_))
    tps = [float(t) for t in sp.solve(sp.diff(cub, x), x) if t.is_real and -3.5 <= float(t) <= 3.5]
    if any(abs(k - float(cub.subs(x, t))) < ystep for t in tps):
        return None
    nsol = len(rts)
    word = "the solution" if nsol == 1 else ("both solutions" if nsol == 2 else f"all {nsol} solutions")
    eq = lx(cub)
    g = grid_fig(-3.5, 3.5, ymin, ymax, xstep=1, ystep=ystep, minor=2, w=340, h=360,
                 items=_curve_items(f, -3.5, 3.5, ymin, ymax))
    return Q(intro=f"The grid shows the graph of $y = {eq}$ for values of $x$ from $-3.5$ to $3.5$",
             figs=[fig(g, 85, note=None)],
             parts=[P("a", "Write down the coordinates of the points where the graph crosses the $x$-axis.", 2, prefix=""),
                    P("b", f"Use the graph to find {'an estimate of' if nsol == 1 else 'estimates of'} {word} of ${eq} = {k}$", 2, prefix="")],
             rows=[R("a", f"$({p}, 0)$, $({q}, 0)$, $({s_}, 0)$", "B2", "B1 for two correct points or the three $x$-values only"),
                   R("b", f"line $y = {k}$ drawn or used", "M1", ""),
                   R("b", ", ".join(dp(v, 1) for v in rts), "A1", "allow ±0.1 of each value")],
             values={"roots": [p, q, s_], "solutions": [round(v, 3) for v in rts]}, diff="4-6", cw="Write down", refs=["H3.3A", "H3.3E"])


@tpl("functions.graphs", "structured", n=7)
def graph_line_curve(r):
    a, b, c = 1, nz(r, -3, 3), r.randint(-5, 0)
    f = lambda v: a * v * v + b * v + c
    m, k = r.choice([1, 2, -1]), r.randint(-2, 3)
    xs = list(range(-4, 5))
    vals = [f(v) for v in xs]
    ymin, ymax = min(vals) - 1, max(vals) + 1
    if ymax - ymin > 40:
        return None
    ystep = 2 if ymax - ymin > 18 else 1
    hide = r.sample(range(len(xs)), 3)
    quad = sp.expand(a * x ** 2 + (b - m) * x + (c - k))
    rts = sorted(float(s) for s in sp.solve(quad, x) if s.is_real)
    if len(rts) != 2 or not all(-4 <= v <= 4 for v in rts):
        return None
    eq = poly_tex([a, b, c])
    g = grid_fig(-4, 4, ymin, ymax, ystep=ystep, minor=5 if ystep == 1 else 4, w=340, h=380)
    return Q(intro=f"Here is a table of values for $y = {eq}$",
             figs=[table(["$x$"] + [str(v) for v in xs], [["$y$"] + [("" if i in hide else str(vals[i])) for i in range(len(xs))]])],
             parts=[P("a", "Complete the table of values.", 2, space="table"),
                    P("b", f"On the grid, draw the graph of $y = {eq}$ for values of $x$ from $-4$ to $4$", 2, space="graph", figs=[fig(g, 85, note=None)]),
                    P("c", f"By drawing a suitable straight line on the grid, find estimates of the solutions of $${lx(quad)} = 0$$", 3, prefix="")],
             rows=[R("a", ", ".join(f"{vals[i]}" for i in sorted(hide)), "B2", "B1 for 1 or 2 correct values"),
                   R("b", "smooth curve through all their points", "B2", "B1 for at least 6 points plotted correctly"),
                   R("c", f"$y = {lin_tex(m, k)}$", "M1", f"for identifying the line; comes from ${eq} = {lin_tex(m, k)}$"),
                   R("c", f"line $y = {lin_tex(m, k)}$ drawn correctly", "M1", ""),
                   R("c", ", ".join(dp(v, 1) for v in rts), "A1", "allow ±0.2")],
             values={"table": vals, "line": f"y={m}x+{k}", "roots": [round(v, 4) for v in rts]}, diff="7-9",
             cw="Complete", refs=["F3.3I", "H3.3E"])


@tpl("functions.graphs", "structured", n=7)
def graph_reciprocal(r):
    a = r.choice([4, 6, 8, 10, 12])
    b = r.choice([0, 1, 2, -1])
    f = lambda v: a / v + b * v
    xs = [F(1, 2), 1, 2, 3, 4, 5, 6]
    vals = [F(a) / v + b * v for v in xs]
    hide = r.sample(range(len(xs)), 3)
    ys = [float(v) for v in vals]
    ymin, ymax = 0 if min(ys) >= 0 else math.floor(min(ys)) - 1, math.ceil(max(ys)) + 2
    if ymax > 30:
        return None
    eq = f"\\frac{{{a}}}{{x}}" + (f" {'+' if b > 0 else '-'} {'' if abs(b) == 1 else abs(b)}x" if b else "")
    g = grid_fig(0, 6, ymin, ymax, ystep=2, minor=5, w=320, h=360)
    tan_x = r.choice([1, 2, 3])
    grad = -a / tan_x ** 2 + b
    return Q(intro=f"Here is a table of values for $y = {eq}$",
             figs=[table(["$x$"] + [num(float(v)) for v in xs], [["$y$"] + [("" if i in hide else dp(float(vals[i]), 1).replace(".0", "")) for i in range(len(xs))]])],
             parts=[P("a", "Complete the table of values. Give values correct to 1 decimal place where necessary.", 2, space="table"),
                    P("b", f"On the grid, draw the graph of $y = {eq}$ for $0.5 \\leqslant x \\leqslant 6$", 2, space="graph", figs=[fig(g, 80, note=None)]),
                    P("c", f"Draw a tangent to the curve at $x = {tan_x}$ and use it to estimate the gradient there.", 3, prefix="")],
             rows=[R("a", ", ".join(dp(float(vals[i]), 1) for i in sorted(hide)), "B2", "B1 for 1 or 2 correct values"),
                   R("b", "smooth curve through all their points", "B2", "B1 for at least 5 points plotted correctly"),
                   R("c", f"tangent drawn at $x = {tan_x}$", "M1", ""),
                   R("c", "vertical change ÷ horizontal change for their tangent", "M1", "dep on first M1"),
                   R("c", f"{dp(grad, 1)}", "A1", f"accept values in the range {dp(grad - 0.6 if grad < -2 else grad - 0.3, 1)} to {dp(grad + 0.6 if grad < -2 else grad + 0.3, 1)}")],
             values={"table": [float(v) for v in vals], "gradient": grad}, diff="7-9", cw="Complete", refs=["H3.3A", "H3.3D"])


# ---------------------------------------------------------------- real-life graphs
def _dt_items(pts):
    def it(M):
        return PL([M(p) for p in pts], w=1.8)
    return it


@tpl("functions.real-life", "graph", n=7)
def distance_time(r):
    nm = name(r)
    h0 = r.choice([8, 9, 10, 13, 14])
    d1 = r.choice([10, 12, 15, 20, 24])
    t1 = r.choice([30, 45, 60])
    stop = r.choice([15, 30, 45])
    d2 = d1 + r.choice([6, 8, 10, 12])
    t2 = r.choice([30, 45, 60])
    back = r.choice([45, 60, 75, 90])
    pts = [(0, 0), (t1, d1), (t1 + stop, d1), (t1 + stop + t2, d2), (t1 + stop + t2 + 30, d2), (t1 + stop + t2 + 30 + back, 0)]
    tmax = pts[-1][0]
    xmax = math.ceil(tmax / 60) * 60
    ymax = math.ceil(d2 / 5) * 5 + 5
    if xmax > 300:
        return None
    g = grid_fig(0, xmax, 0, ymax, xstep=30, ystep=5, minor=3, xlabel="Time", ylabel="Distance from home (km)",
                 w=380, h=280, items=_dt_items(pts), xtick=60)
    g = g.replace(">0<", ">0<")
    sp1 = d1 / (t1 / 60)
    spb = d2 / (back / 60)
    return Q(intro=f"{nm} cycled from home to a lake and then back home. The travel graph shows the journey. The time axis starts at {h0}:00 and each small square on the time axis is 10 minutes.",
             figs=[fig(g, 95, note=None, caption=f"Time (minutes after {h0}:00)")],
             parts=[P("a", f"How many minutes did {nm} stop for during the first part of the journey?", 1, prefix=""),
                    P("b", f"Work out {nm}'s average speed, in km/h, for the first {t1} minutes.", 2, prefix="km/h"),
                    P("c", f"Work out {nm}'s average speed, in km/h, on the journey home.", 2, prefix="km/h")],
             rows=[R("a", str(stop), "B1", ""),
                   R("b", f"${d1} \\div {num(t1 / 60)}$", "M1", ""), R("b", num(sp1), "A1", ""),
                   R("c", f"${d2} \\div {num(back / 60)}$", "M1", "for distance ÷ time with time in hours"), R("c", sf(spb, 3), "A1", "awrt " + sf(spb, 3))],
             values={"stop": stop, "speed1": sp1, "speed_home": spb}, diff="4-6", cw="Work out", refs=["F3.3A", "H3.4A"])


@tpl("functions.real-life", "graph", n=7)
def speed_time(r):
    v = r.choice([8, 10, 12, 15, 16, 20, 24])
    t1 = r.choice([4, 5, 6, 8, 10])
    t2 = r.choice([10, 12, 15, 20])
    t3 = r.choice([5, 6, 8, 10])
    pts = [(0, 0), (t1, v), (t1 + t2, v), (t1 + t2 + t3, 0)]
    T_ = t1 + t2 + t3
    xmax = math.ceil(T_ / 5) * 5
    ymax = math.ceil(v / 5) * 5 + 5
    g = grid_fig(0, xmax, 0, ymax, xstep=5, ystep=5, minor=5, xlabel="Time (s)", ylabel="Speed (m/s)", w=380, h=260,
                 items=_dt_items(pts))
    dist = F(t1 * v, 2) + t2 * v + F(t3 * v, 2)
    acc = F(v, t1)
    return Q(intro=f"The graph shows the speed of a vehicle during the first {T_} seconds of a journey.",
             figs=[fig(g, 95, note=None)],
             parts=[P("a", f"Work out the acceleration of the vehicle during the first {t1} seconds.", 2, prefix="m/s²"),
                    P("b", f"Work out the total distance travelled by the vehicle in the {T_} seconds.", 3, prefix="m")],
             rows=[R("a", f"$\\frac{{{v}}}{{{t1}}}$", "M1", ""), R("a", num(float(acc)), "A1", "oe"),
                   R("b", f"$\\frac{{1}}{{2}} \\times {t1} \\times {v}$ or ${t2} \\times {v}$ or $\\frac{{1}}{{2}} \\times {t3} \\times {v}$", "M1", "for the area of one section"),
                   R("b", f"$\\frac{{1}}{{2}}({T_} + {t2}) \\times {v}$ or the sum of the three areas", "M1", "for a complete method"),
                   R("b", num(float(dist)), "A1", "cao")],
             values={"acceleration": acc, "distance": dist}, diff="4-6", cw="Work out", refs=["F3.3A", "H3.4A"])


@tpl("functions.real-life", "graph", n=6)
def conversion_graph(r):
    c1, c2, rate = r.choice([("pounds", "euros", F(6, 5)), ("dollars", "pesos", 18), ("litres", "gallons", F(11, 50)),
                             ("kilograms", "pounds (lb)", F(11, 5)), ("km", "miles", F(5, 8))])
    xmax = 50 if rate < 1 else (100 if rate < 3 else 10)
    ymax = float(rate * xmax)
    xstep = xmax / 10
    ystep = ymax / 10
    g = grid_fig(0, xmax, 0, ymax, xstep=xstep, ystep=ystep, minor=2, xlabel=c1, ylabel=c2, w=360, h=300,
                 items=lambda M: L(*M((0, 0)), *M((xmax, ymax)), w=1.8))
    a = r.choice([i * xstep for i in range(2, 9)])
    b = r.choice([i * ystep for i in range(2, 9)])
    big_amt = xmax * r.choice([3, 4, 5, 6])
    return Q(intro=f"The graph can be used to convert between {c1} and {c2}.",
             figs=[fig(g, 85, note=None)],
             parts=[P("a", f"Use the graph to change {num(a)} {c1} into {c2}.", 1, prefix=c2),
                    P("b", f"Use the graph to change {num(b)} {c2} into {c1}.", 1, prefix=c1),
                    P("c", f"Use the graph to change {num(big_amt)} {c1} into {c2}. Show your method.", 2, prefix=c2)],
             rows=[R("a", num(float(rate * F(a).limit_denominator(1000))), "B1", "allow ±1 small square"),
                   R("b", num(round(b / float(rate), 3)), "B1", "allow ±1 small square"),
                   R("c", f"eg ${num(xmax)}$ {c1} $= {num(ymax)}$ {c2}, multiplied by {big_amt // xmax}", "M1", "for a correct scaling method using a reading from the graph"),
                   R("c", num(float(rate) * big_amt), "A1", "allow small reading errors")],
             values={"a": float(rate) * a, "b": b / float(rate), "c": float(rate) * big_amt}, diff="1-3", cw="Use",
             refs=["F3.3F"])


# ---------------------------------------------------------------- transformations of graphs
@tpl("functions.graph-transformations", "short", n=14)
def gt_point(r):
    px, py = nz(r, -5, 6), nz(r, -6, 6)
    a = nz(r, -4, 4)
    k = r.choice([2, 3, -1, F(1, 2)])
    kinds = {"f(x) + a": (px, py + a, f"translation by $\\begin{{pmatrix}} 0 \\\\ {a} \\end{{pmatrix}}$"),
             "f(x + a)": (px - a, py, f"translation by $\\begin{{pmatrix}} {-a} \\\\ 0 \\end{{pmatrix}}$"),
             "af(x)": (px, py * k, f"stretch parallel to the $y$-axis, scale factor {ftex(k)}" if k != -1 else "reflection in the $x$-axis"),
             "f(ax)": (F(px) / k, py, f"stretch parallel to the $x$-axis, scale factor ${ftex(1 / F(k))}$" if k != -1 else "reflection in the $y$-axis"),
             "-f(x)": (px, -py, "reflection in the $x$-axis"), "f(-x)": (-px, py, "reflection in the $y$-axis")}
    two = r.sample(list(kinds), 2)

    def tx(kd):
        av = f"{'+' if a > 0 else '-'} {abs(a)}"
        return {"f(x) + a": f"y = \\mathrm{{f}}(x) {av}", "f(x + a)": f"y = \\mathrm{{f}}(x {av})",
                "af(x)": f"y = {'-' if k == -1 else ftex(k)}\\mathrm{{f}}(x)", "f(ax)": f"y = \\mathrm{{f}}({'-' if k == -1 else ftex(k)}x)",
                "-f(x)": "y = -\\mathrm{f}(x)", "f(-x)": "y = \\mathrm{f}(-x)"}[kd]
    parts, rows, vals = [], [], {}
    for lab, kd in zip("ab", two):
        nx, ny, desc = kinds[kd]
        parts.append(P(lab, f"Write down the coordinates of the image of $P$ on the graph of ${tx(kd)}$", 1, prefix=""))
        rows.append(R(lab, f"$({ftex(F(nx))}, {ftex(F(ny))})$", "B1", desc))
        vals[lab] = [str(F(nx)), str(F(ny))]
    return Q(intro=f"The point $P({px}, {py})$ lies on the graph of $y = \\mathrm{{f}}(x)$.", parts=parts, rows=rows,
             values=vals, diff="7-9", cw="Write down", refs=["H3.3B"])


def _trig_or_quad(r):
    kind = r.choice(["quad", "sin", "cos"])
    return kind


@tpl("functions.graph-transformations", "graph", n=7)
def gt_sketch(r):
    # f(x) = (x-p)^2 + q drawn; ask to draw f(x+a) or f(x)+a
    p, q = r.randint(-2, 2), r.randint(-3, 1)
    a = nz(r, -3, 3)
    f = lambda v: (v - p) ** 2 + q
    which = r.choice(["shift_y", "shift_x", "neg"])
    g = grid_fig(-6, 6, -8, 10, ystep=2, minor=2, w=340, h=360, items=_curve_items(f, -6, 6, -8, 10))
    if which == "shift_y":
        lab = f"y = \\mathrm{{f}}(x) {'+' if a > 0 else '-'} {abs(a)}"
        vx, vy = p, q + a
        desc = f"translation of $\\begin{{pmatrix}} 0 \\\\ {a} \\end{{pmatrix}}$"
    elif which == "shift_x":
        lab = f"y = \\mathrm{{f}}(x {'+' if a > 0 else '-'} {abs(a)})"
        vx, vy = p - a, q
        desc = f"translation of $\\begin{{pmatrix}} {-a} \\\\ 0 \\end{{pmatrix}}$"
    else:
        lab = "y = -\\mathrm{f}(x)"
        vx, vy = p, -q
        desc = "reflection in the $x$-axis"
    return Q(intro="The graph of $y = \\mathrm{f}(x)$ is drawn on the grid.",
             figs=[fig(g, 85, note=None)],
             parts=[P("a", "Write down the coordinates of the turning point of the graph of $y = \\mathrm{f}(x)$.", 1, prefix=""),
                    P("b", f"On the grid, draw the graph of ${lab}$", 2, space="graph")],
             rows=[R("a", f"$({p}, {q})$", "B1", ""),
                   R("b", f"curve with the same shape and turning point at $({vx}, {vy})$", "B2", f"B1 for a {desc.split(' of ')[0] if 'of' in desc else 'correct transformation'} in the wrong direction or by the wrong amount, or a correct curve with the turning point incorrect by 1 square")],
             values={"tp": [p, q], "image_tp": [vx, vy]}, diff="7-9", cw="Draw", refs=["H3.3B"])


@tpl("functions.graph-transformations", "graph", n=7)
def gt_trig(r):
    fn = r.choice(["sin", "cos"])
    a = r.choice([2, 3, -1])
    kind = r.choice(["amp", "shift", "plus"])
    sh = r.choice([30, 45, 60, 90])
    c = r.choice([1, 2, -1])
    base = (lambda d: math.sin(math.radians(d))) if fn == "sin" else (lambda d: math.cos(math.radians(d)))
    if kind == "amp":
        g_ = lambda d: a * base(d)
        eq = f"y = {'-' if a == -1 else a}\\{fn} x"
        ask = f"Write down the equation of the transformed graph, which is the graph of $y = \\{fn} x$ after a {'stretch parallel to the y-axis with scale factor ' + str(a) if a > 0 else 'reflection in the x-axis'}."
    elif kind == "shift":
        g_ = lambda d: base(d - sh)
        eq = f"y = \\{fn}(x - {sh})"
        ask = f"The graph of $y = \\{fn} x$ is translated by the vector $\\begin{{pmatrix}} {sh} \\\\ 0 \\end{{pmatrix}}$. Write down the equation of the new graph."
    else:
        g_ = lambda d: base(d) + c
        eq = f"y = \\{fn} x {'+' if c > 0 else '-'} {abs(c)}"
        ask = f"The graph of $y = \\{fn} x$ is translated by the vector $\\begin{{pmatrix}} 0 \\\\ {c} \\end{{pmatrix}}$. Write down the equation of the new graph."
    ym = 4
    g = grid_fig(0, 360, -ym, ym, xstep=90, ystep=1, minor=3, w=380, h=260,
                 items=lambda M: curve(M, base, 0, 360, -ym, ym) + curve(M, g_, 0, 360, -ym, ym, w=1.0).replace("<polyline", '<polyline stroke-dasharray="5,3"'))
    return Q(intro=f"The grid shows the graph of $y = \\{fn} x$ for $0 \\leqslant x \\leqslant 360$ (solid curve) and the graph of a transformation of it (dashed curve).",
             figs=[fig(g, 95, note=None)],
             parts=[P("", ask + "\n\nState also the coordinates of one point on the dashed curve where the solid curve has $x = 90$.", 2, prefix="")],
             rows=[R("", f"${eq}$", "B1", "oe"),
                   R("", f"$(90, {num(round(g_(90), 4))})$", "B1", "ft their equation")],
             values={"equation": eq, "point": [90, round(g_(90), 6)]}, diff="7-9", cw="Write down", refs=["H3.3B", "H3.3C", "H3.3A"])


# ---------------------------------------------------------------- calculus
def dpoly(r, deg=3):
    co = [nz(r, -5, 5) if i == 0 else r.randint(-9, 9) for i in range(deg + 1)]
    return sum(c * x ** (deg - i) for i, c in enumerate(co))


@tpl("functions.calculus", "algebra", n=7)
def diff_basic(r):
    a, b, c = nz(r, -6, 6), nz(r, -9, 9), r.randint(1, 9)
    p1 = r.choice([3, 4, 5])
    neg = r.choice([-1, -2])
    e = a * x ** p1 + b * x + sp.Integer(c) * x ** neg
    d = sp.diff(e, x)
    xv = r.choice([1, 2, -1])
    grad = d.subs(x, xv)
    return Q(intro=f"A curve has equation $y = {lx(e)}$",
             parts=[P("a", "Find $\\dfrac{\\mathrm{d}y}{\\mathrm{d}x}$", 2, prefix="$\\dfrac{\\mathrm{d}y}{\\mathrm{d}x} =$ "),
                    P("b", f"Find the gradient of the curve when $x = {xv}$", 1, prefix="")],
             rows=[R("a", "at least two terms correct", "M1", "the term in $x^{" + str(neg) + "}$ may be written first as a power"),
                   R("a", f"${lx(d)}$", "A1", "oe"),
                   R("b", f"${lx(grad)}$", "B1", "ft their derivative")],
             values={"dydx": str(d), "gradient": grad}, diff="7-9", cw="Find", refs=["H3.4B", "H3.4C"])


@tpl("functions.calculus", "algebra", n=7)
def diff_tangent_point(r):
    a, b, c = r.choice([1, 2, 3]), r.randint(-9, 9), r.randint(-9, 9)
    e = a * x ** 3 + b * x ** 2 + c * x + r.randint(-5, 5)
    g = r.randint(-10, 30)
    sols = sp.solve(sp.Eq(sp.diff(e, x), g), x)
    sols = [s for s in sols if s.is_rational]
    if not sols:
        return None
    pts = [(s, e.subs(x, s)) for s in sorted(sols)]
    return Q(intro=f"A curve has equation $y = {lx(e)}$",
             parts=[P("", f"Find the coordinates of the points on the curve where the gradient is ${g}$", 4, prefix="")],
             rows=[R("", f"$\\frac{{\\mathrm{{d}}y}}{{\\mathrm{{d}}x}} = {lx(sp.diff(e, x))}$", "M1", "for at least two terms correct"),
                   R("", f"${lx(sp.diff(e, x))} = {g}$", "M1", ""),
                   R("", ", ".join(f"$x = {lx(p[0])}$" for p in pts), "A1", ""),
                   R("", ", ".join(f"$({lx(p[0])}, {lx(p[1])})$" for p in pts), "A1", "")],
             values={"points": [[str(p[0]), str(p[1])] for p in pts]}, diff="7-9", cw="Find", refs=["H3.4C"])


@tpl("functions.calculus", "problem", n=7)
def turning_points(r):
    p, q = sorted(r.sample(range(-4, 5), 2))
    a = r.choice([1, 1, 2, -1])
    # derivative 3a(x-p)(x-q)
    d = 3 * a * (x - p) * (x - q)
    e = sp.integrate(sp.expand(d), x) + r.randint(-8, 8)
    co = sp.Poly(e, x).all_coeffs()
    if any(sp.denom(c) != 1 for c in co):
        return None
    pts = [(p, e.subs(x, p)), (q, e.subs(x, q))]
    maxp = pts[0] if a > 0 else pts[1]
    minp = pts[1] if a > 0 else pts[0]
    return Q(intro=f"The curve **C** has equation $y = {lx(e)}$",
             parts=[P("", "Find the coordinates of the turning points on **C** and state which is a maximum and which is a minimum.\n\nShow clear algebraic working.", 6, prefix="")],
             rows=[R("", f"$\\frac{{\\mathrm{{d}}y}}{{\\mathrm{{d}}x}} = {lx(sp.expand(d))}$", "M1", "for at least two terms correct"),
                   R("", f"${lx(sp.expand(d))} = 0$", "M1", "for setting their derivative equal to 0"),
                   R("", f"$x = {p}$, $x = {q}$", "A1", ""),
                   R("", f"substituting $x = {p}$ or $x = {q}$ into the equation of the curve", "M1", ""),
                   R("", f"$({p}, {pts[0][1]})$ and $({q}, {pts[1][1]})$", "A1", ""),
                   R("", f"maximum $({maxp[0]}, {maxp[1]})$, minimum $({minp[0]}, {minp[1]})$", "B1", "from the shape of a cubic or a second derivative / gradient test")],
             values={"max": [maxp[0], int(maxp[1])], "min": [minp[0], int(minp[1])]}, diff="7-9", cw="Find",
             refs=["H3.4C", "H3.4D"])


@tpl("functions.calculus", "problem", n=7)
def kinematics(r):
    a, b, c = r.choice([1, 2]), r.randint(1, 9), r.randint(1, 20)
    s_ = a * t ** 3 - b * t ** 2 + c * t if r.random() < 0.5 else -a * t ** 3 + b * t ** 2 * 3 + c * t
    v = sp.diff(s_, t)
    acc = sp.diff(v, t)
    T_ = r.randint(2, 6)
    vt = v.subs(t, T_)
    at_zero = sp.solve(sp.Eq(acc, 0), t)
    if not at_zero or at_zero[0] <= 0:
        return None
    tz = at_zero[0]
    return Q(intro=f"A particle moves along a straight line. The displacement, $s$ metres, of the particle from a fixed point $O$ at time $t$ seconds is given by $$s = {lx(s_)}$$",
             parts=[P("", f"Find the velocity of the particle at the time when its acceleration is zero.", 4, prefix="m/s")],
             rows=[R("", f"$v = \\frac{{\\mathrm{{d}}s}}{{\\mathrm{{d}}t}} = {lx(v)}$", "M1", "for differentiating with at least two terms correct"),
                   R("", f"$a = \\frac{{\\mathrm{{d}}v}}{{\\mathrm{{d}}t}} = {lx(acc)}$", "M1", "ft their $v$"),
                   R("", f"${lx(acc)} = 0$ so $t = {lx(tz)}$", "M1", ""),
                   R("", f"${lx(v.subs(t, tz))}$", "A1", "oe")],
             values={"t": tz, "v": v.subs(t, tz)}, diff="7-9", cw="Find", refs=["H3.4E"])


@tpl("functions.calculus", "structured", n=7)
def optimise_box(r):
    S = r.choice([24, 48, 54, 96, 150, 216, 294, 384])  # open box square base side x, height h, surface area x^2 + 4xh = S
    kind = r.choice(["box", "fence"])
    if kind == "box":
        h = (S - x ** 2) / (4 * x)
        V = sp.expand(x ** 2 * h)
        dV = sp.diff(V, x)
        xs = [s for s in sp.solve(dV, x) if s > 0][0]
        Vm = V.subs(x, xs)
        intro = f"An open box has a square base of side $x$ cm and a height of $h$ cm. The box has no lid. The total surface area of the box is {S} cm²."
        pa = (P("a", f"Show that the volume, $V$ cm³, of the box is given by $V = {lx(V)}$", 3, space="working"),
              [R("a", f"$x^2 + 4xh = {S}$", "M1", ""), R("a", f"$h = \\frac{{{S} - x^2}}{{4x}}$", "M1", ""),
               R("a", f"$V = x^2 \\times \\frac{{{S} - x^2}}{{4x}} = {lx(V)}$", "A1", "dep on M2")])
    else:
        Lf = S
        V = sp.expand(x * (Lf - 2 * x))
        dV = sp.diff(V, x)
        xs = sp.solve(dV, x)[0]
        Vm = V.subs(x, xs)
        intro = f"A farmer uses {Lf} m of fencing to make three sides of a rectangular pen. The fourth side is a wall. The two sides of the pen at right angles to the wall each have length $x$ metres."
        pa = (P("a", f"Show that the area, $A$ m², of the pen is given by $A = {lx(V)}$", 2, space="working"),
              [R("a", f"length parallel to wall $= {Lf} - 2x$", "M1", ""), R("a", f"$A = x({Lf} - 2x) = {lx(V)}$", "A1", "")])
    lab = "V" if kind == "box" else "A"
    return Q(intro=intro,
             parts=[pa[0],
                    P("b", f"Find $\\dfrac{{\\mathrm{{d}}{lab}}}{{\\mathrm{{d}}x}}$", 1, prefix=""),
                    P("c", f"Find the maximum value of ${lab}$. Show your working clearly.", 3, prefix="")],
             rows=pa[1] + [R("b", f"${lx(dV)}$", "B1", ""),
                           R("c", f"${lx(dV)} = 0$", "M1", "ft their (b)"),
                           R("c", f"$x = {lx(xs)}$", "A1", ""),
                           R("c", f"{num(float(Vm))}", "A1", "cao")],
             values={"derivative": str(dV), "x": xs, "max": Vm}, diff="7-9", cw="Show that", refs=["H3.4C", "H3.4E"])


@tpl("functions.calculus", "structured", n=7)
def calc_structured(r):
    p, q = sorted(r.sample(range(-3, 5), 2))
    d = 3 * (x - p) * (x - q)
    k = r.randint(-6, 6)
    e = sp.expand(sp.integrate(sp.expand(d), x) + k)
    co = sp.Poly(e, x).all_coeffs()
    if any(sp.denom(c) != 1 for c in co):
        return None
    xv = r.choice([v for v in range(-3, 5) if v not in (p, q)])
    m = sp.diff(e, x).subs(x, xv)
    yv = e.subs(x, xv)
    c_ = yv - m * xv
    return Q(intro=f"A curve has equation $y = {lx(e)}$",
             parts=[P("a", "Find $\\dfrac{\\mathrm{d}y}{\\mathrm{d}x}$", 2, prefix=""),
                    P("b", f"Find the equation of the tangent to the curve at the point where $x = {xv}$\n\nGive your answer in the form $y = mx + c$", 3, prefix=""),
                    P("c", "Find the $x$-coordinates of the turning points of the curve.", 2, prefix="")],
             rows=[R("a", "two terms correct", "M1", ""), R("a", f"${lx(sp.diff(e, x))}$", "A1", ""),
                   R("b", f"gradient $= {m}$", "M1", "ft their (a)"),
                   R("b", f"point $({xv}, {yv})$ and $y - {yv} = {m}(x - {xv})$", "M1", ""),
                   R("b", f"$y = {lin_tex(int(m), int(c_))}$" if m != 0 else f"$y = {c_}$", "A1", ""),
                   R("c", f"${lx(sp.diff(e, x))} = 0$", "M1", ""), R("c", f"$x = {p}$, $x = {q}$", "A1", "")],
             values={"tangent": [int(m), int(c_)], "tp_x": [p, q]}, diff="7-9", cw="Find", refs=["H3.4B", "H3.4C"])
