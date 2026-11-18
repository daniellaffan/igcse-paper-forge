"""Algebra templates (spec section 2)."""
import math
from fractions import Fraction as F

import sympy as sp

from maths_util import (tpl, P, R, Q, sf, dp, num, ftex, poly_tex, lin_tex, bracket, name, cur, fig,
                        grid_fig, curve, PL, L, T, DOT, NOT_ACC)

x, y, n, a_, b_ = sp.symbols("x y n a b")
VARS = ["x", "y", "a", "p", "t", "m", "k", "w"]


def lx(e):
    return sp.latex(e)


def nz(r, lo=-9, hi=9, excl=(0,)):
    while True:
        v = r.randint(lo, hi)
        if v not in excl:
            return v


def sym(v):
    return sp.Symbol(v)


def sol_tex(vals):
    return " or ".join(f"${lx(v)}$" for v in vals)


# ---------------------------------------------------------------- 2.1 indices
@tpl("algebra.indices", "short", n=8)
def idx_power(r):
    v1, v2 = r.sample(["x", "y", "a", "b", "c", "m", "p", "t"], 2)
    c = r.choice([2, 3, 4, 5])
    p, q, k = r.randint(2, 7), r.randint(1, 6), r.choice([2, 3, 4])
    coef = c ** k
    ans = f"{coef}{v1}^{{{p * k}}}{v2}^{{{q * k}}}"
    qt = "" if q == 1 else f"^{{{q}}}"
    return Q(parts=[P("", f"Simplify fully $$({c}{v1}^{{{p}}}{v2}{qt})^{{{k}}}$$", 2, prefix="")],
             rows=[R("", f"${ans}$", "B2", f"B1 for two of ${coef}$, ${v1}^{{{p * k}}}$, ${v2}^{{{q * k}}}$ in a product")],
             values={"coef": coef, "p": p * k, "q": q * k}, diff="4-6", cw="Simplify", refs=["F2.1D"])


@tpl("algebra.indices", "short", n=7)
def idx_divide(r):
    v = r.choice(["x", "y", "e", "h"])
    a1, a2 = r.randint(2, 9) * r.choice([2, 3]), r.choice([2, 3, 4, 6])
    if a1 % a2:
        return None
    p1, p2, p3 = r.randint(3, 9), r.randint(2, 6), r.randint(-4, 4)
    res = p1 + p3 - p2
    ex3 = f"{v}^{{{p3}}}" if p3 not in (0, 1) else (v if p3 == 1 else "")
    if p3 == 0 or a1 // a2 == 1:
        return None
    return Q(parts=[P("", f"Simplify $$\\frac{{{a1}{v}^{{{p1}}} \\times {ex3}}}{{{a2}{v}^{{{p2}}}}}$$", 2, prefix="")],
             rows=[R("", f"${a1 // a2}{v}^{{{res}}}$" if res not in (0, 1) else f"${a1 // a2}{v if res == 1 else ''}$", "B2",
                     f"B1 for ${a1 // a2}{v}^k$ or $c{v}^{{{res}}}$ where $c \\ne {a1 // a2}$")],
             values={"coef": a1 // a2, "power": res}, diff="4-6", cw="Simplify", refs=["F2.1D", "F2.1C"])


@tpl("algebra.indices", "algebra", n=8)
def idx_fractional(r):
    v1, v2 = r.sample(["x", "y", "a", "b", "w"], 2)
    base, root = r.choice([(8, 3), (27, 3), (64, 3), (16, 4), (81, 4), (25, 2), (49, 2), (125, 3), (32, 5)])
    rt = round(base ** (1 / root))
    num_ = r.choice([1, 2, 3]) if root != 5 else r.choice([1, 2])
    neg = r.random() < 0.5
    p, q = root * r.randint(1, 3), root * r.randint(1, 2)
    e = F(num_, root) * (-1 if neg else 1)
    cp, ep, eq = F(rt) ** num_, F(p) * e, F(q) * e
    if neg:
        ans = f"\\frac{{1}}{{{cp}{v1}^{{{ep * -1}}}{v2}^{{{eq * -1}}}}}"
        alt = f"{ftex(1 / cp)}{v1}^{{{ep}}}{v2}^{{{eq}}}"
    else:
        ans = f"{cp}{v1}^{{{ep}}}{v2}^{{{eq}}}"
        alt = ans
    ans = ans.replace("^{1}", "")
    etex = ("-" if neg else "") + f"\\frac{{{num_}}}{{{root}}}"
    return Q(parts=[P("", f"Simplify fully $$({base}{v1}^{{{p}}}{v2}^{{{q}}})^{{{etex}}}$$", 3, prefix="")],
             rows=[R("", f"${rt}$ or ${cp}$ or $\\frac{{1}}{{\\ldots}}$ or ${v1}^{{{ep}}}$ or ${v2}^{{{eq}}}$", "M1", "for one correct element"),
                   R("", "two correct elements", "M1", ""),
                   R("", f"${ans}$", "A1", f"oe, eg ${alt}$")],
             values={"coef": cp ** (-1 if neg else 1), "p": ep, "q": eq}, diff="7-9", cw="Simplify", refs=["H2.1A"])


@tpl("algebra.indices", "algebra", n=7)
def idx_solve(r):
    b = r.choice([2, 3, 5])
    k1, k2 = r.choice([(2, 3), (3, 2), (2, 1), (4, 2), (3, 1)]) if b == 2 else r.choice([(2, 1), (3, 1), (2, 3)])
    A, B = b ** k1, b ** k2
    p, q = r.randint(1, 4), nz(r, -5, 5)
    s_, t_ = r.randint(1, 3), nz(r, -5, 5)
    # A^(p x + q) = B^(s x + t)  -> k1(px+q) = k2(sx+t)
    xs = sp.solve(sp.Eq(k1 * (p * x + q), k2 * (s_ * x + t_)), x)
    if not xs or k1 * p == k2 * s_:
        return None
    sol = xs[0]
    if sp.denom(sol) > 6:
        return None
    return Q(parts=[P("", f"Solve $${A}^{{{lin_tex(p, q)}}} = {B}^{{{lin_tex(s_, t_)}}}$$", 3, prefix="$x =$ ")],
             rows=[R("", f"${b}^{{{k1}({lin_tex(p, q)})}} = {b}^{{{k2}({lin_tex(s_, t_)})}}$", "M1", "for writing both sides as powers of the same base"),
                   R("", f"${k1}({lin_tex(p, q)}) = {k2}({lin_tex(s_, t_)})$", "M1", "for equating the indices"),
                   R("", f"${lx(sol)}$", "A1", "oe")],
             values={"x": sol}, diff="7-9", cw="Solve", refs=["H2.1A", "F2.1D"])


# ---------------------------------------------------------------- 2.2 expanding/factorising
@tpl("algebra.expanding", "short", n=7)
def expand_double(r):
    v = r.choice(VARS)
    V = sym(v)
    a, b, c, d = r.choice([1, 1, 2, 3]), nz(r), r.choice([1, 1, 2, 4]), nz(r)
    e = sp.expand((a * V + b) * (c * V + d))
    co = sp.Poly(e, V).all_coeffs()
    return Q(parts=[P("", f"Expand and simplify $$({lin_tex(a, b, v)})({lin_tex(c, d, v)})$$", 2, prefix="")],
             rows=[R("", f"3 out of 4 terms correct, eg ${lx(a * c * V ** 2)} {'+' if a * d >= 0 else '-'} {lx(abs(a * d) * V)} {'+' if b * c >= 0 else '-'} {lx(abs(b * c) * V)}$", "M1", "or 4 terms correct ignoring signs"),
                   R("", f"${poly_tex(co, v)}$", "A1", "cao")],
             values={"expansion": str(e)}, diff="1-3" if a == c == 1 else "4-6", cw="Expand and simplify", refs=["F2.2E"])


@tpl("algebra.expanding", "short", n=7)
def factorise_simple(r):
    v = r.choice(VARS)
    kind = r.choice(["quad", "common", "dots"])
    V = sym(v)
    if kind == "quad":
        p, q = nz(r), nz(r)
        if p == -q:
            return None
        e = sp.expand((V + p) * (V + q))
        ans = f"({lin_tex(1, p, v)})({lin_tex(1, q, v)})"
        rows = [R("", f"$({v} \\pm {abs(p)})({v} \\pm {abs(q)})$", "M1", "or brackets that expand to give two of the three terms"),
                R("", f"${ans}$", "A1", "")]
        txt = f"Factorise $${lx(e)}$$"
    elif kind == "common":
        w = r.choice(["x", "y", "a"])
        W = sym(w)
        g = r.choice([2, 3, 4, 5, 6])
        c1, c2 = r.sample([1, 2, 3, 5, 7], 2)
        e = g * c1 * V ** 2 * W + g * c2 * V * W ** 2 if v != w else g * c1 * V ** 3 + g * c2 * V ** 2
        f_ = sp.factor(e)
        ans = lx(f_)
        rows = [R("", "a correct partial factorisation with at least two factors taken out", "M1", ""),
                R("", f"${ans}$", "A1", "")]
        txt = f"Factorise fully $${lx(e)}$$"
    else:
        a = r.choice([1, 2, 3, 4, 5])
        b = r.choice([1, 3, 5, 7, 9, 2])
        e = a * a * V ** 2 - b * b
        ans = f"({lin_tex(a, b, v)})({lin_tex(a, -b, v)})"
        rows = [R("", f"$({a if a > 1 else ''}{v} \\pm {b})(\\ldots)$", "M1", ""), R("", f"${ans}$", "A1", "")]
        txt = f"Factorise $${lx(e)}$$"
    return Q(parts=[P("", txt, 2, prefix="")], rows=rows, values={"factorised": str(sp.factor(e))},
             diff="4-6", cw="Factorise", refs=["F2.2F", "F2.2D", "H2.2B"])


@tpl("algebra.expanding", "algebra", n=8)
def expand_triple(r):
    v = r.choice(["x", "y", "n", "t"])
    V = sym(v)
    a = r.choice([1, 1, 2, 3])
    ps = [nz(r, -6, 6) for _ in range(3)]
    e = sp.expand((a * V + ps[0]) * (V + ps[1]) * (V + ps[2]))
    co = sp.Poly(e, V).all_coeffs()
    two = sp.expand((V + ps[1]) * (V + ps[2]))
    return Q(parts=[P("", f"Show that $$({lin_tex(a, ps[0], v)})({lin_tex(1, ps[1], v)})({lin_tex(1, ps[2], v)})$$ can be written in the form $a{v}^3 + b{v}^2 + c{v} + d$ where $a$, $b$, $c$ and $d$ are integers.", 3, space="working")],
             rows=[R("", f"expansion of any two brackets with at least 3 of 4 terms correct, eg ${lx(two)}$", "M1", ""),
                   R("", f"a complete expansion of all three brackets with at least 6 of 8 terms correct (ft their first product)", "M1", ""),
                   R("", f"${poly_tex(co, v)}$", "A1", "")],
             values={"coeffs": [int(c) for c in co]}, diff="7-9", cw="Show that", refs=["H2.2A"])


@tpl("algebra.expanding", "algebra", n=8)
def factorise_hard(r):
    v = r.choice(["x", "y", "a", "w"])
    V = sym(v)
    a, c = r.choice([(2, 1), (3, 1), (2, 3), (3, 2), (5, 1), (4, 3), (6, 1), (3, 4)])
    b, d = nz(r, -7, 7), nz(r, -7, 7)
    if math.gcd(a, b) != 1 or math.gcd(c, d) != 1:
        return None
    e = sp.expand((a * V + b) * (c * V + d))
    co = sp.Poly(e, V).all_coeffs()
    if 0 in co:
        return None
    also = r.random() < 0.5
    parts = [P("a", f"Factorise $${poly_tex(co, v)}$$", 2, prefix="")]
    rows = [R("a", f"$({a}{v} \\pm {abs(b)})({'' if c == 1 else c}{v} \\pm {abs(d)})$", "M1", "or two brackets that expand to give 2 of the 3 terms"),
            R("a", f"$({lin_tex(a, b, v)})({lin_tex(c, d, v)})$", "A1", "")]
    vals = {"factorised": str(sp.factor(e))}
    if also:
        roots = sorted(sp.solve(e, V))
        parts.append(P("b", f"Hence solve $${poly_tex(co, v)} = 0$$", 1, prefix=""))
        rows.append(R("b", f"${v} = {lx(roots[0])}$, ${v} = {lx(roots[1])}$", "B1", "ft their factorisation"))
        vals["roots"] = [str(t) for t in roots]
    return Q(parts=parts, rows=rows, values=vals, diff="7-9" if a * c > 4 else "4-6", cw="Factorise", refs=["H2.2B", "H2.7A"])


# ---------------------------------------------------------------- 2.2C algebraic fractions
@tpl("algebra.fractions", "algebra", n=6)
def algfrac_add(r):
    p1, p2 = r.randint(1, 5), r.randint(1, 5)
    a1, a2 = nz(r, -6, 6), nz(r, -6, 6)
    if a1 == a2:
        return None
    op = r.choice(["+", "-"])
    e = p1 / (x + a1) + (p2 if op == "+" else -p2) / (x + a2)
    tog = sp.factor(sp.together(e))
    numer, den = sp.fraction(sp.together(e))
    numer = sp.expand(numer)
    if numer == 0 or sp.degree(numer, x) < 1:
        return None
    return Q(parts=[P("", f"Write as a single fraction in its simplest form $$\\frac{{{p1}}}{{{lin_tex(1, a1)}}} {op} \\frac{{{p2}}}{{{lin_tex(1, a2)}}}$$", 3, prefix="")],
             rows=[R("", f"$\\frac{{{p1}({lin_tex(1, a2)}) {op} {p2}({lin_tex(1, a1)})}}{{({lin_tex(1, a1)})({lin_tex(1, a2)})}}$", "M1", "for a correct common denominator with at least one numerator correct"),
                   R("", f"numerator ${lx(numer)}$", "M1", "for a correctly simplified numerator"),
                   R("", f"$\\frac{{{lx(numer)}}}{{({lin_tex(1, a1)})({lin_tex(1, a2)})}}$", "A1", f"oe, eg denominator ${lx(sp.expand(den))}$")],
             values={"result": str(tog)}, diff="7-9", cw="Write", refs=["H2.2C"])


@tpl("algebra.fractions", "algebra", n=6)
def algfrac_simplify(r):
    p, q, s_ = nz(r, -6, 6), nz(r, -6, 6), nz(r, -6, 6)
    a = r.choice([1, 2, 3])
    if len({p, q, s_}) < 3 or math.gcd(a, q) != 1:
        return None
    top = sp.expand((a * x + q) * (x + p))
    bot = sp.expand((x + p) * (x + s_)) if r.random() < 0.6 else sp.expand((x + p) * (x - p))
    res = sp.cancel(top / bot)
    if sp.denom(res) == 1:
        return None
    return Q(parts=[P("", f"Simplify fully $$\\frac{{{lx(top)}}}{{{lx(bot)}}}$$", 3, prefix="")],
             rows=[R("", f"$({lin_tex(a, q)})({lin_tex(1, p)})$", "M1", "for correctly factorising the numerator"),
                   R("", f"$({lin_tex(1, p)})({lx(sp.factor(bot) / (x + p))})$", "M1", "for correctly factorising the denominator"),
                   R("", f"${lx(res)}$", "A1", "")],
             values={"result": str(res)}, diff="7-9", cw="Simplify", refs=["H2.2C", "H2.2B"])


@tpl("algebra.fractions", "algebra", n=6)
def algfrac_equation(r):
    # p/(x+a) + q/(x+b) = 1 with nice integer roots
    for _ in range(50):
        r1, r2 = nz(r, -8, 9), nz(r, -8, 9)
        a1, a2 = nz(r, -5, 5), nz(r, -5, 5)
        if a1 == a2:
            continue
        # (x+a1)(x+a2) - p(x+a2) - q(x+a1) = (x-r1)(x-r2)
        # compare: x^2 + (a1+a2-p-q)x + a1a2 - p a2 - q a1 = x^2 - (r1+r2)x + r1 r2
        M = sp.Matrix([[1, 1], [a2, a1]])
        rhs = sp.Matrix([a1 + a2 + r1 + r2, a1 * a2 - r1 * r2])
        if M.det() == 0:
            continue
        pq = M.solve(rhs)
        p, q = pq
        if not (p.is_integer and q.is_integer) or p <= 0 or q <= 0 or p > 12 or q > 12:
            continue
        if r1 in (-a1, -a2) or r2 in (-a1, -a2) or r1 == r2:
            continue
        sols = sorted(sp.solve(sp.Eq(p / (x + a1) + q / (x + a2), 1), x))
        if len(sols) != 2:
            continue
        return Q(parts=[P("", f"Solve $$\\frac{{{p}}}{{{lin_tex(1, a1)}}} + \\frac{{{q}}}{{{lin_tex(1, a2)}}} = 1$$\n\nShow clear algebraic working.", 4, prefix="")],
                 rows=[R("", f"${p}({lin_tex(1, a2)}) + {q}({lin_tex(1, a1)}) = ({lin_tex(1, a1)})({lin_tex(1, a2)})$", "M1", "for multiplying through by a common denominator"),
                       R("", f"${lx(sp.expand((x - r1) * (x - r2)))} = 0$", "A1", "for a correct 3-term quadratic in any form = 0"),
                       R("", f"$({lin_tex(1, -r1)})({lin_tex(1, -r2)}) = 0$", "M1", "for a correct method to solve their quadratic"),
                       R("", f"$x = {sols[0]}$, $x = {sols[1]}$", "A1", "dep on M1")],
                 values={"roots": [int(s) for s in sols]}, diff="7-9", cw="Solve", refs=["H2.2C", "H2.7A"])
    return None


# ---------------------------------------------------------------- 2.2D completing the square
@tpl("algebra.completing-square", "algebra", n=7)
def cts_simple(r):
    b, c = nz(r, -10, 10), nz(r, -15, 15)
    if b % 2:
        b *= 2
    h = F(b, 2)
    k = c - h * h
    return Q(parts=[P("", f"Write $x^2 {'+' if b > 0 else '-'} {abs(b)}x {'+' if c > 0 else '-'} {abs(c)}$ in the form $(x + p)^2 + q$ where $p$ and $q$ are integers.", 2, prefix="")],
             rows=[R("", f"$(x {'+' if h > 0 else '-'} {abs(h)})^2$", "M1", ""),
                   R("", f"$(x {'+' if h > 0 else '-'} {abs(h)})^2 {'+' if k >= 0 else '-'} {abs(k)}$", "A1", f"$p = {h}$, $q = {k}$")],
             values={"p": h, "q": k}, diff="4-6", cw="Write", refs=["H2.2D"])


def ac(a):
    return "-" if a == -1 else str(a)


@tpl("algebra.completing-square", "algebra", n=7)
def cts_hard(r):
    a = r.choice([2, 3, -1, -2, 4, 5])
    b = nz(r, -8, 8) * (2 if r.random() < 0.6 else 1) * abs(a)
    c = nz(r, -12, 12)
    p = F(b, 2 * a)
    q = c - a * p * p
    e = a * x ** 2 + b * x + c
    chk = sp.expand(a * (x + sp.Rational(p.numerator, p.denominator)) ** 2 + sp.Rational(q.numerator, q.denominator) - e)
    assert chk == 0
    return Q(parts=[P("", f"Write ${poly_tex([a, b, c])}$ in the form $a(x + b)^2 + c$, stating the value of each of $a$, $b$ and $c$.", 3, prefix="")],
             rows=[R("", f"${ac(a)}\\left(x^2 {'+' if b / a > 0 else '-'} {ftex(abs(F(b, a)))}x\\right) {'+' if c > 0 else '-'} {abs(c)}$", "M1", "for taking out the factor of $a$ from the first two terms"),
                   R("", f"${ac(a)}\\left(x {'+' if p > 0 else '-'} {ftex(abs(p))}\\right)^2$", "M1", ""),
                   R("", f"${ac(a)}\\left(x {'+' if p > 0 else '-'} {ftex(abs(p))}\\right)^2 {'+' if q >= 0 else '-'} {ftex(abs(q))}$", "A1", "oe")],
             values={"a": a, "b": p, "c": q}, diff="7-9", cw="Write", refs=["H2.2D"])


@tpl("algebra.completing-square", "structured", n=13)
def cts_structured(r):
    b, c = nz(r, -6, 6) * 2, nz(r, -20, 20)
    h = b // 2
    k = c - h * h
    roots_ok = k < 0
    parts = [P("a", f"Express $x^2 {'+' if b > 0 else '-'} {abs(b)}x {'+' if c > 0 else '-'} {abs(c)}$ in the form $(x + p)^2 + q$", 2, prefix=""),
             P("b", f"Hence write down the coordinates of the turning point of the curve with equation $y = x^2 {'+' if b > 0 else '-'} {abs(b)}x {'+' if c > 0 else '-'} {abs(c)}$", 1, prefix="")]
    rows = [R("a", f"$(x {'+' if h > 0 else '-'} {abs(h)})^2$", "M1", ""),
            R("a", f"$(x {'+' if h > 0 else '-'} {abs(h)})^2 {'+' if k >= 0 else '-'} {abs(k)}$", "A1", ""),
            R("b", f"$({-h}, {k})$", "B1", "ft their (a)")]
    vals = {"p": h, "q": k, "tp": [-h, k]}
    if roots_ok:
        s1 = -h + sp.sqrt(-k)
        s2 = -h - sp.sqrt(-k)
        parts.append(P("c", f"Hence solve $x^2 {'+' if b > 0 else '-'} {abs(b)}x {'+' if c > 0 else '-'} {abs(c)} = 0$, giving your answers in surd form where appropriate.", 3, prefix=""))
        rows += [R("c", f"$(x {'+' if h > 0 else '-'} {abs(h)})^2 = {-k}$", "M1", "ft their (a)"),
                 R("c", f"$x {'+' if h > 0 else '-'} {abs(h)} = \\pm\\sqrt{{{-k}}}$", "M1", ""),
                 R("c", f"${lx(sp.simplify(s1))}$, ${lx(sp.simplify(s2))}$", "A1", "oe, accept $" + f"{-h} \\pm \\sqrt{{{-k}}}" + "$")]
        vals["roots"] = [str(sp.simplify(s1)), str(sp.simplify(s2))]
    else:
        parts.append(P("c", f"Explain how your answer to part (a) shows that the equation $x^2 {'+' if b > 0 else '-'} {abs(b)}x {'+' if c > 0 else '-'} {abs(c)} = 0$ has no real solutions.", 2, space="lines", lines=2))
        rows += [R("c", f"$(x {'+' if h > 0 else '-'} {abs(h)})^2 \\geqslant 0$ for all $x$", "M1", "or the minimum value of the expression is " + str(k)),
                 R("c", f"so the expression is always at least {k}, which is greater than 0, so it can never equal 0", "A1", "complete explanation")]
    return Q(parts=parts, rows=rows, values=vals, diff="7-9", cw="Express", refs=["H2.2D", "H2.7B"])


# ---------------------------------------------------------------- 2.2E proof
PROOFS = [
    ("Prove that the sum of any three consecutive integers is a multiple of 3.",
     [("let the integers be $n$, $n + 1$, $n + 2$", "M1", "for three consecutive integers in algebraic form"),
      ("$n + n + 1 + n + 2 = 3n + 3$", "M1", "for a correct sum"),
      ("$= 3(n + 1)$ which is a multiple of 3", "A1", "for a complete proof with conclusion")], "4-6"),
    ("Prove that the difference between the squares of any two consecutive odd numbers is a multiple of 8.",
     [("$2n + 1$ and $2n + 3$ oe", "M1", "for two consecutive odd numbers in algebraic form"),
      ("$(2n + 3)^2 - (2n + 1)^2 = 4n^2 + 12n + 9 - (4n^2 + 4n + 1)$", "M1", "for correct expansions"),
      ("$= 8n + 8$", "M1", ""),
      ("$= 8(n + 1)$ which is a multiple of 8", "A1", "complete proof with conclusion")], "7-9"),
    ("Prove that the product of two odd numbers is always odd.",
     [("$2m + 1$ and $2n + 1$", "M1", "for two (not necessarily consecutive) odd numbers in algebraic form"),
      ("$(2m + 1)(2n + 1) = 4mn + 2m + 2n + 1$", "M1", ""),
      ("$= 2(2mn + m + n) + 1$ which is one more than an even number, so odd", "A1", "")], "7-9"),
    ("Prove that the sum of the squares of any two consecutive integers is always odd.",
     [("$n^2 + (n + 1)^2$", "M1", ""), ("$= 2n^2 + 2n + 1$", "M1", ""),
      ("$= 2(n^2 + n) + 1$ which is odd", "A1", "")], "7-9"),
    ("Prove that the square of any odd number is one more than a multiple of 8.",
     [("$(2n + 1)^2 = 4n^2 + 4n + 1$", "M1", ""), ("$= 4n(n + 1) + 1$", "M1", ""),
      ("one of $n$, $n + 1$ is even so $n(n + 1)$ is even and $4n(n + 1)$ is a multiple of 8", "A1", "complete argument")], "7-9"),
]


@tpl("algebra.proof", "proof", n=6)
def proof_fixed(r):
    s, rows, d = r.choice(PROOFS)
    form = r.choice(["", "\n\nShow each step of your working clearly."])
    return Q(parts=[P("", s + form, sum(int(m[1:]) for _, m, _ in rows), space="working")],
             rows=[R("", a, m, nt) for a, m, nt in rows], values={"statement": s}, diff=d, cw="Prove", refs=["H2.2E"])


@tpl("algebra.proof", "proof", n=10)
def proof_identity(r):
    a = r.randint(1, 6)
    b = r.choice([2, 3, 4, 5])
    kind = r.choice(["diffsq", "consec", "expr"])
    if kind == "diffsq":
        e = sp.expand((n + a) ** 2 - (n - a) ** 2)
        k = 4 * a
        stmt = f"Prove that $(n + {a})^2 - (n - {a})^2$ is a multiple of {k} for all integer values of $n$."
        rows = [R("", f"$n^2 + {2 * a}n + {a * a} - (n^2 - {2 * a}n + {a * a})$", "M1", "for correct expansion of both brackets"),
                R("", f"$= {k}n$", "M1", ""),
                R("", f"${k}n$ is a multiple of {k} (as $n$ is an integer)", "A1", "complete proof")]
        val = str(e)
    elif kind == "consec":
        stmt = f"Prove that the sum of {b} consecutive integers starting with an even number is " + \
               ("always odd." if b in (2,) else "a multiple of " + str(b) + " when " + ("$b$ is odd" if False else "the number of integers is odd") + ".")
        if b % 2 == 0 and b != 2:
            return None
        terms = " + ".join(f"(2n + {i})" if i else "2n" for i in range(b))
        tot = sp.expand(sum(2 * n + i for i in range(b)))
        if b == 2:
            stmt = "Prove that the sum of two consecutive integers is always odd."
            terms, tot = "n + (n + 1)", 2 * n + 1
            rows = [R("", "$n$ and $n + 1$", "M1", ""), R("", "$n + n + 1 = 2n + 1$", "M1", ""),
                    R("", "$2n$ is even so $2n + 1$ is odd", "A1", "")]
        else:
            stmt = f"Prove that the sum of any {b} consecutive integers is a multiple of {b}."
            terms = " + ".join(f"(n + {i})" if i else "n" for i in range(b))
            tot = sp.expand(sum(n + i for i in range(b)))
            rows = [R("", f"${terms}$", "M1", "for consecutive integers in algebraic form"),
                    R("", f"$= {lx(tot)}$", "M1", ""),
                    R("", f"$= {b}(n + {(b - 1) // 2})$ which is a multiple of {b}", "A1", "")]
        val = str(tot)
    else:
        c = r.randint(2, 5)
        e1 = sp.expand((2 * n + c) ** 2 - (2 * n - c) ** 2)
        k = 8 * c
        stmt = f"Prove that $(2n + {c})^2 - (2n - {c})^2$ is a multiple of {k * 1 if False else 8} for all positive integers $n$."
        rows = [R("", f"$4n^2 + {4 * c}n + {c * c} - (4n^2 - {4 * c}n + {c * c})$", "M1", ""),
                R("", f"$= {8 * c}n$", "M1", ""),
                R("", f"$= 8 \\times {c}n$, a multiple of 8", "A1", "")]
        val = str(e1)
    return Q(parts=[P("", stmt, 3, space="working")], rows=rows, values={"simplified": val}, diff="7-9", cw="Prove",
             refs=["H2.2E", "H2.2A"])


# ---------------------------------------------------------------- 2.3 formulae
@tpl("algebra.formulae", "short", n=8)
def substitute(r):
    forms = [("v = u + at", ["u", "a", "t"], lambda u, a, t: u + a * t, "v"),
             ("s = ut + \\frac{1}{2}at^2", ["u", "t", "a"], lambda u, t, a: u * t + F(1, 2) * a * t * t, "s"),
             ("E = \\frac{1}{2}mv^2", ["m", "v"], lambda m, v: F(1, 2) * m * v * v, "E"),
             ("P = \\frac{V^2}{R}", ["V", "R"], lambda V, R_: F(V * V, R_), "P"),
             ("T = \\frac{3a - b}{c}", ["a", "b", "c"], lambda a, b, c: F(3 * a - b, c), "T"),
             ("y = 2x^2 - 5x", ["x"], lambda x_: 2 * x_ * x_ - 5 * x_, "y")]
    fstr, vs, fn, subj = r.choice(forms)
    vals = {}
    for v in vs:
        vals[v] = r.choice([-6, -4, -3, -2, 2, 3, 4, 5, 7, 8, 10, F(1, 2), F(5, 2)]) if v not in ("R", "c", "m") else r.choice([2, 4, 5, 8])
    res = fn(*[vals[v] for v in vs])
    given = ", ".join(f"${v} = {ftex(vals[v])}$" for v in vs)
    sub = fstr.split("=")[1]
    return Q(parts=[P("", f"$${fstr}$$\n\nWork out the value of ${subj}$ when {given}.", 2, prefix=f"${subj} =$ ")],
             rows=[R("", "correct substitution of the values into the formula", "M1", ""), R("", f"${ftex(res)}$", "A1", "oe")],
             values={subj: res}, diff="1-3", cw="Work out", refs=["F2.3C"])


@tpl("algebra.formulae", "short", n=7)
def rearrange_simple(r):
    forms = [("v = u + at", "t", "t = \\frac{v - u}{a}", "for subtracting $u$ or dividing by $a$ as a correct first step"),
             ("A = \\pi r^2", "r", "r = \\sqrt{\\frac{A}{\\pi}}", "for $r^2 = \\frac{A}{\\pi}$"),
             ("y = \\frac{3x - 4}{5}", "x", "x = \\frac{5y + 4}{3}", "for $5y = 3x - 4$"),
             ("P = 2(l + w)", "w", "w = \\frac{P - 2l}{2}", "for $\\frac{P}{2} = l + w$ or $P - 2l = 2w$"),
             ("s = \\frac{(u + v)t}{2}", "u", "u = \\frac{2s}{t} - v", "for $2s = (u + v)t$"),
             ("E = mc^2", "c", "c = \\sqrt{\\frac{E}{m}}", "for $c^2 = \\frac{E}{m}$"),
             ("y = 4 - 3x", "x", "x = \\frac{4 - y}{3}", "for $3x = 4 - y$ oe"),
             ("V = \\frac{1}{3}\\pi r^2 h", "h", "h = \\frac{3V}{\\pi r^2}", "for $3V = \\pi r^2 h$")]
    f_, s, ans, m = r.choice(forms)
    k = r.randint(2, 9)
    if r.random() < 0.5:
        f_ = f_.replace("4", str(k))
        ans = ans.replace("4", str(k))
    return Q(parts=[P("", f"Make ${s}$ the subject of $${f_}$$", 2, prefix=f"${s} =$ ")],
             rows=[R("", m.replace("for ", "", 1), "M1", "for a correct first step"), R("", f"${ans}$", "A1", "oe")], values={"answer": ans},
             diff="4-6", cw="Make", refs=["F2.3F"])


@tpl("algebra.formulae", "algebra", n=8)
def rearrange_twice(r):
    v, s = r.choice([("y", "x"), ("p", "q"), ("t", "a"), ("w", "m")])
    a, b, c, d = r.randint(1, 6), nz(r, -9, 9), r.randint(1, 5), nz(r, -9, 9)
    if a * d == b * c:
        return None
    S, V = sym(s), sym(v)
    # V = (a S + b)/(c S + d)
    sol = sp.solve(sp.Eq(V, (a * S + b) / (c * S + d)), S)[0]
    sol = sp.simplify(sol)
    nume, den = sp.fraction(sp.together(sol))
    return Q(parts=[P("", f"Make ${s}$ the subject of the formula $${v} = \\frac{{{lin_tex(a, b, s)}}}{{{lin_tex(c, d, s)}}}$$", 4, prefix=f"${s} =$ ")],
             rows=[R("", f"${v}({lin_tex(c, d, s)}) = {lin_tex(a, b, s)}$", "M1", "for removing the fraction"),
                   R("", f"${'' if c == 1 else c}{v}{s} - {'' if a == 1 else a}{s} = {lx(sp.expand(-d * V + b))}$", "M1", "for gathering the terms in $" + s + "$ on one side and the other terms on the other side"),
                   R("", f"${s}({'' if c == 1 else c}{v} - {a}) = {lx(sp.expand(-d * V + b))}$", "M1", "for factorising"),
                   R("", f"${s} = {lx(sol)}$", "A1", "oe")],
             values={"answer": str(sol)}, diff="7-9", cw="Make", refs=["H2.3A"])


@tpl("algebra.formulae", "algebra", n=7)
def rearrange_root(r):
    kind = r.choice(["sqrt", "sq", "pend"])
    if kind == "sqrt":
        a, b = r.randint(2, 6), r.randint(1, 9)
        txt = f"$$y = \\sqrt{{\\frac{{x + {b}}}{{{a}}}}}$$"
        s = "x"
        ans = f"x = {a}y^2 - {b}"
        rows = [R("", f"$y^2 = \\frac{{x + {b}}}{{{a}}}$", "M1", ""), R("", f"${a}y^2 = x + {b}$", "M1", ""),
                R("", f"${ans}$", "A1", "oe")]
    elif kind == "sq":
        a, b = r.randint(2, 7), r.randint(2, 9)
        txt = f"$$A = {a}k^2 + {b}$$"
        s = "k"
        ans = f"k = \\pm\\sqrt{{\\frac{{A - {b}}}{{{a}}}}}"
        rows = [R("", f"$A - {b} = {a}k^2$", "M1", ""), R("", f"$k^2 = \\frac{{A - {b}}}{{{a}}}$", "M1", ""),
                R("", f"${ans}$", "A1", "oe; condone omission of $\\pm$")]
    else:
        txt = "$$T = 2\\pi\\sqrt{\\frac{l}{g}}$$"
        s = "l"
        ans = "l = \\frac{gT^2}{4\\pi^2}"
        rows = [R("", "$\\frac{T}{2\\pi} = \\sqrt{\\frac{l}{g}}$", "M1", ""), R("", "$\\frac{T^2}{4\\pi^2} = \\frac{l}{g}$", "M1", ""),
                R("", f"${ans}$", "A1", "oe")]
        if r.random() < 0.5:
            txt = txt.replace("2\\pi", "k")
            ans = "l = \\frac{gT^2}{k^2}"
            rows = [R("", "$\\frac{T}{k} = \\sqrt{\\frac{l}{g}}$", "M1", ""), R("", "$\\frac{T^2}{k^2} = \\frac{l}{g}$", "M1", ""),
                    R("", f"${ans}$", "A1", "oe")]
    return Q(parts=[P("", f"Make ${s}$ the subject of {txt}", 3, prefix=f"${s} =$ ")], rows=rows,
             values={"answer": ans}, diff="7-9", cw="Make", refs=["H2.3A"])


# ---------------------------------------------------------------- 2.4 linear
@tpl("algebra.linear", "algebra", n=7)
def linear_fraction(r):
    for _ in range(40):
        a, b, c, d = r.randint(1, 7), nz(r), r.randint(1, 7), nz(r)
        p, q = r.choice([2, 3, 4, 5]), r.choice([2, 3, 4, 6])
        if p == q:
            continue
        sol = sp.solve(sp.Eq((a * x + b) / p - (c * x + d) / q, r.randint(1, 3)), x)
        if not sol:
            continue
        s = sol[0]
        if sp.denom(s) <= 4 and abs(s) < 30:
            rhs = sp.simplify((a * s + b) / p - (c * s + d) / q)
            return Q(parts=[P("", f"Solve $$\\frac{{{lin_tex(a, b)}}}{{{p}}} - \\frac{{{lin_tex(c, d)}}}{{{q}}} = {rhs}$$\n\nShow clear algebraic working.", 3, prefix="$x =$ ")],
                     rows=[R("", f"${q}({lin_tex(a, b)}) - {p}({lin_tex(c, d)}) = {p * q * rhs}$", "M1", "for multiplying all terms by a common multiple of the denominators"),
                           R("", f"${q * a - p * c}x = {p * q * rhs - q * b + p * d}$", "M1", "for collecting terms correctly (ft their first step)"),
                           R("", f"${lx(s)}$", "A1", "oe")],
                     values={"x": s}, diff="4-6", cw="Solve", refs=["F2.4A"])
    return None


@tpl("algebra.linear", "algebra", n=7)
def linear_brackets(r):
    a, b, c, d, e = r.randint(2, 7), nz(r), r.randint(2, 5), nz(r), r.randint(1, 5)
    sol = sp.solve(sp.Eq(a * (x + b), c * (e * x + d) if r.random() < 0 else e * x + c * d + 0), x)
    v = r.choice(["x", "y", "w", "n"])
    V = sym(v)
    lhs = a * (V + b)
    rhs = c * (d - V)
    sol = sp.solve(sp.Eq(lhs, rhs), V)
    if not sol or sp.denom(sol[0]) > 5:
        return None
    s = sol[0]
    return Q(parts=[P("", f"Solve $${a}({lin_tex(1, b, v)}) = {c}({d} - {v})$$\n\nShow clear algebraic working.", 3, prefix=f"${v} =$ ")],
             rows=[R("", f"${a}{v} {'+' if a * b > 0 else '-'} {abs(a * b)} = {c * d} - {c}{v}$", "M1", "for correct expansion of at least one bracket"),
                   R("", f"${a + c}{v} = {c * d - a * b}$", "M1", "for isolating the terms in $" + v + "$"),
                   R("", f"${lx(s)}$", "A1", "oe")],
             values={v: s}, diff="4-6", cw="Solve", refs=["F2.4A"])


@tpl("algebra.linear", "problem", n=7)
def linear_angles(r):
    kind = r.choice(["tri", "quad", "perim"])
    if kind == "tri":
        a, b = r.randint(2, 4), r.randint(1, 3)
        c, d = nz(r, -20, 30), nz(r, -20, 30)
        # angles: a x + c, b x + d, x
        xs = F(180 - c - d, a + b + 1)
        if xs.denominator != 1 or xs <= 5:
            return None
        angs = [a * xs + c, b * xs + d, xs]
        if min(angs) <= 0:
            return None
        big_ = max(angs)
        txt = f"The sizes of the angles of a triangle, in degrees, are $({lin_tex(a, c)})$, $({lin_tex(b, d)})$ and $x$."
        rows = [R("", f"$({lin_tex(a, c)}) + ({lin_tex(b, d)}) + x = 180$", "M1", "for a correct equation"),
                R("", f"${a + b + 1}x = {180 - c - d}$", "M1", ""),
                R("", f"$x = {xs}$", "A1", ""),
                R("", f"{big_}", "A1", "")]
        ask = "Work out the size of the largest angle of the triangle."
        val = big_
    elif kind == "quad":
        a, b, c = r.randint(2, 3), r.randint(1, 2), nz(r, -10, 40)
        xs = F(360 - c - 90, a + b + 1)
        if xs.denominator != 1:
            return None
        angs = [a * xs, b * xs + c, xs, 90]
        if min(angs) <= 0:
            return None
        txt = f"A quadrilateral has angles $90^\\circ$, ${a}x^\\circ$, $({lin_tex(b, c)})^\\circ$ and $x^\\circ$."
        rows = [R("", f"$90 + {a}x + {lin_tex(b, c)} + x = 360$", "M1", ""), R("", f"${a + b + 1}x = {270 - c}$", "M1", ""),
                R("", f"$x = {xs}$", "A1", ""), R("", f"{b * xs + c}", "A1", "")]
        ask = f"Work out the size of the angle $({lin_tex(b, c)})^\\circ$."
        val = b * xs + c
    else:
        a, b = r.randint(2, 5), r.randint(1, 9)
        w = r.randint(3, 15)
        per = 2 * ((a * w + b) + w)
        txt = f"The length of a rectangle is $({lin_tex(a, b)})$ cm. The width of the rectangle is $x$ cm. The perimeter of the rectangle is {per} cm."
        rows = [R("", f"$2({lin_tex(a, b)}) + 2x = {per}$", "M1", ""), R("", f"${2 * a + 2}x = {per - 2 * b}$", "M1", ""),
                R("", f"$x = {w}$", "A1", ""), R("", str(w * (a * w + b)), "A1", "")]
        ask = "Work out the area of the rectangle."
        val = w * (a * w + b)
    return Q(intro=txt, parts=[P("", ask, 4, prefix="")], rows=rows, values={"answer": val}, diff="4-6",
             cw="Work out", refs=["F2.4B", "F2.4A"])


@tpl("algebra.linear", "problem", n=7)
def linear_ages(r):
    nm = name(r, 3)
    a, b = r.randint(2, 4), r.randint(2, 9)
    xa = r.randint(5, 20)
    k = r.randint(2, 10)
    tot = xa + (a * xa) + (xa + b)
    c = cur(r)
    return Q(intro=f"{nm[0]}, {nm[1]} and {nm[2]} collect money for a charity.\n\n{nm[1]} collects {a} times as much as {nm[0]}.\n{nm[2]} collects {b * k} {c} more than {nm[0]}.\n\nIn total they collect {xa * k * (a + 2) + b * k} {c}.",
             parts=[P("", f"Work out how much {nm[1]} collects.", 4, prefix="")],
             rows=[R("", f"$x + {a}x + x + {b * k}$", "M1", "for an expression for the total in terms of one unknown"),
                   R("", f"$x + {a}x + x + {b * k} = {xa * k * (a + 2) + b * k}$", "M1", "for a correct equation"),
                   R("", f"$x = {xa * k}$", "A1", ""),
                   R("", str(a * xa * k), "A1", "cao")],
             values={"answer": a * xa * k}, diff="4-6", cw="Work out", refs=["F2.4B"])


# ---------------------------------------------------------------- 2.5 proportion
PROPS = [("x", lambda v: v, "x"), ("x^2", lambda v: v * v, "the square of x"), ("x^3", lambda v: v ** 3, "the cube of x"),
         ("\\sqrt{x}", lambda v: sp.sqrt(v), "the square root of x")]


@tpl("algebra.proportion", "problem", n=14)
def proportion_find(r):
    tex_, f_, words = r.choice(PROPS)
    inv = r.random() < 0.5
    vx = r.choice([4, 9, 16, 25]) if "sqrt" in tex_ else r.choice([2, 3, 4, 5, 6])
    k = r.choice([2, 3, 4, 5, 8, 10, 12, F(1, 2), F(3, 4)])
    k = sp.Rational(str(k)) if isinstance(k, F) else sp.Integer(k)
    vy = k / f_(sp.Integer(vx)) if inv else k * f_(sp.Integer(vx))
    vx2 = r.choice([1, 36, 49, 64, 100]) if "sqrt" in tex_ else r.choice([1, 8, 10, 12, F(1, 2)])
    vx2 = sp.Rational(str(vx2))
    if vx2 == vx:
        return None
    vy2 = k / f_(vx2) if inv else k * f_(vx2)
    if sp.denom(vy) > 20 or sp.denom(vy2) > 100:
        return None
    a_, b_ = r.choice([("y", "x"), ("d", "t"), ("P", "r"), ("F", "s")])
    words_ = words.replace("x", f"${b_}$")
    rel = f"${a_}$ is {'inversely ' if inv else 'directly '}proportional to {words_}."
    tex2 = tex_.replace("x", b_)
    formula = f"{a_} = \\frac{{{lx(k)}}}{{{tex2}}}" if inv else f"{a_} = {lx(k)}{tex2}"
    return Q(intro=f"{rel}\n\n${a_} = {lx(vy)}$ when ${b_} = {vx}$.",
             parts=[P("", f"Find the value of ${a_}$ when ${b_} = {lx(vx2)}$.", 3, prefix=f"${a_} =$ ")],
             rows=[R("", f"${a_} = \\frac{{k}}{{{tex2}}}$" if inv else f"${a_} = k{tex2}$", "M1", "for a correct proportionality statement with a constant (not using =k alone)"),
                   R("", f"$k = {lx(k)}$ or ${formula}$", "M1", "for finding the value of the constant"),
                   R("", f"${lx(vy2)}$", "A1", "oe")],
             values={"k": k, "answer": vy2}, diff="7-9", cw="Find", refs=["H2.5A"])


@tpl("algebra.proportion", "structured", n=13)
def proportion_struct(r):
    tex_, f_, words = r.choice(PROPS[:3])
    inv = r.random() < 0.5
    k = sp.Integer(r.choice([2, 3, 4, 5, 6, 12, 18, 24, 36, 48, 60]))
    vx = r.choice([2, 3, 4, 6])
    vy = k / f_(sp.Integer(vx)) if inv else k * f_(sp.Integer(vx))
    vx2 = r.choice([1, 5, 8, 10])
    vy2 = k / f_(sp.Integer(vx2)) if inv else k * f_(sp.Integer(vx2))
    ty = (k / f_(sp.Integer(r.choice([2, 3]))) if inv else k * f_(sp.Integer(r.choice([2, 3]))))
    sx = sp.solve(sp.Eq(k / f_(x) if inv else k * f_(x), ty), x)
    sx = [s for s in sx if s.is_real and s > 0]
    if not sx or vx2 == vx:
        return None
    A, B = r.choice([("T", "n"), ("F", "d"), ("V", "q"), ("I", "d"), ("y", "x"), ("P", "r"), ("H", "s")])
    rel = words.replace("x", f"${B}$")
    tex2 = tex_.replace("x", B)
    formula = f"{A} = \\frac{{{lx(k)}}}{{{tex2}}}" if inv else f"{A} = {lx(k)}{tex2}"
    return Q(intro=f"${A}$ is {'inversely' if inv else 'directly'} proportional to {rel}.\n\nWhen ${B} = {vx}$, ${A} = {lx(vy)}$",
             parts=[P("a", f"Find a formula for ${A}$ in terms of ${B}$.", 3, prefix=""),
                    P("b", f"Work out the value of ${A}$ when ${B} = {vx2}$.", 1, prefix=f"${A} =$ "),
                    P("c", f"Work out the value of ${B}$ when ${A} = {lx(ty)}$.", 2, prefix=f"${B} =$ ")],
             rows=[R("a", f"${A} = \\frac{{k}}{{{tex2}}}$" if inv else f"${A} = k{tex2}$", "M1", ""),
                   R("a", f"${lx(vy)} = \\frac{{k}}{{{tex_.replace('x', str(vx))}}}$" if inv else f"${lx(vy)} = k \\times {tex_.replace('x', str(vx))}$", "M1", "for substituting to find $k$"),
                   R("a", f"${formula}$", "A1", "award 3 marks for a correct formula with no working"),
                   R("b", f"${lx(vy2)}$", "B1", "ft their formula"),
                   R("c", f"${lx(ty)} = {formula.split('=')[1]}$ rearranged for ${B}$", "M1", "ft their formula"),
                   R("c", f"${lx(sx[0])}$", "A1", "")],
             values={"k": k, "b": vy2, "c": sx[0]}, diff="7-9", cw="Find", refs=["H2.5A"])


# ---------------------------------------------------------------- 2.6 simultaneous
def simult(r, rng=8):
    for _ in range(100):
        xs, ys = nz(r, -6, 9), nz(r, -6, 9)
        a1, b1, a2, b2 = nz(r, -6, 7, (0,)), nz(r, -6, 7), nz(r, -6, 7), nz(r, -6, 7)
        if a1 * b2 - a2 * b1 == 0 or abs(a1) == abs(a2) or a1 < 0 or a2 < 0:
            continue
        return a1, b1, a1 * xs + b1 * ys, a2, b2, a2 * xs + b2 * ys, xs, ys
    return None


def eqtex(a, b, c, u="x", v="y"):
    s = poly_tex([a], "") if False else ""
    t1 = f"{'' if a == 1 else ('-' if a == -1 else a)}{u}"
    t2 = f"{'+' if b > 0 else '-'} {'' if abs(b) == 1 else abs(b)}{v}"
    return f"{t1} {t2} = {c}"


@tpl("algebra.simultaneous", "algebra", n=14)
def simult_solve(r):
    s = simult(r)
    if s is None:
        return None
    a1, b1, c1, a2, b2, c2, xs, ys = s
    u, v = r.choice([("x", "y"), ("a", "b"), ("p", "q"), ("m", "n")])
    l = a1 * a2 // math.gcd(a1, a2)
    return Q(parts=[P("", f"Solve the simultaneous equations\n\n$${eqtex(a1, b1, c1, u, v)}$$\n$${eqtex(a2, b2, c2, u, v)}$$\n\nShow clear algebraic working.", 3, prefix="")],
             rows=[R("", f"eg multiplying to make the coefficients of ${u}$ (or ${v}$) equal, eg ${l // a1}({eqtex(a1, b1, c1, u, v)})$ and ${l // a2}({eqtex(a2, b2, c2, u, v)})$, then subtracting; or a correct rearrangement and substitution", "M1",
                     "for a correct method to eliminate one variable (condone one arithmetic error)"),
                   R("", f"${u} = {xs}$ or ${v} = {ys}$", "M1", "for substituting their found value into one of the equations, dep on first M1"),
                   R("", f"${u} = {xs}$, ${v} = {ys}$", "A1", "dep on M1")],
             values={u: xs, v: ys}, diff="4-6", cw="Solve", refs=["H2.6A", "F2.6A"])


@tpl("algebra.simultaneous", "problem", n=14)
def simult_context(r):
    p1, p2 = r.randint(2, 20) * 5, r.randint(2, 20) * 5
    if p1 == p2:
        return None
    a1, b1, a2, b2 = r.randint(2, 6), r.randint(1, 5), r.randint(1, 5), r.randint(2, 6)
    if a1 * b2 - a2 * b1 == 0:
        return None
    c = cur(r)
    items = r.choice([("adult tickets", "child tickets"), ("cups of coffee", "muffins"), ("pens", "notebooks"),
                      ("kg of apples", "kg of pears")])
    t1, t2 = a1 * p1 + b1 * p2, a2 * p1 + b2 * p2
    div = r.choice([1, 100])
    unit = c if div == 1 else "cents"
    n1, n2 = name(r, 2)
    return Q(intro=f"{n1} buys {a1} {items[0]} and {b1} {items[1]}. {n1} pays {t1} {unit}.\n\n{n2} buys {a2} {items[0]} and {b2} {items[1]}. {n2} pays {t2} {unit}.",
             parts=[P("", f"Work out the cost of one of the {items[0]} and the cost of one of the {items[1]}.", 4, prefix="")],
             rows=[R("", f"${a1}a + {b1}b = {t1}$ and ${a2}a + {b2}b = {t2}$", "M1", "for setting up two correct equations"),
                   R("", "correct method to eliminate one variable", "M1", "ft their equations if linear in two unknowns"),
                   R("", f"one correct value, eg $a = {p1}$", "A1", ""),
                   R("", f"{items[0]}: {p1} {unit}, {items[1]}: {p2} {unit}", "A1", "")],
             values={"a": p1, "b": p2}, diff="4-6", cw="Work out", refs=["H2.6A", "F2.6A"])


# ---------------------------------------------------------------- 2.7 quadratics
@tpl("algebra.quadratics", "algebra", n=7)
def quad_formula(r):
    for _ in range(50):
        a, b, c = r.choice([1, 2, 3, 4, 5, -2, -3]), nz(r, -9, 9), nz(r, -12, 12)
        disc = b * b - 4 * a * c
        if disc <= 0 or math.isqrt(disc) ** 2 == disc:
            continue
        break
    else:
        return None
    s1 = (-b + math.sqrt(disc)) / (2 * a)
    s2 = (-b - math.sqrt(disc)) / (2 * a)
    lo, hi = sorted([s1, s2])
    acc = r.choice(["3sf", "2dp"])
    fmt = (lambda v: sf(v, 3)) if acc == "3sf" else (lambda v: dp(v, 2))
    accw = "3 significant figures" if acc == "3sf" else "2 decimal places"
    return Q(parts=[P("", f"Solve ${poly_tex([a, b, c])} = 0$\n\nGive each solution to {accw}, showing clear working.", 3, prefix="")],
             rows=[R("", f"$\\frac{{-({b}) \\pm \\sqrt{{({b})^2 - 4 \\times {a} \\times ({c})}}}}{{2 \\times {a}}}$", "M1", "for correct substitution into the formula; condone one sign error"),
                   R("", f"$\\frac{{{-b} \\pm \\sqrt{{{disc}}}}}{{{2 * a}}}$", "M1", "for correct simplification of the discriminant"),
                   R("", f"{fmt(lo)}, {fmt(hi)}", "A1", "dep on M1, awrt")],
             values={"roots": [round(lo, 6), round(hi, 6)]}, diff="4-6", cw="Solve", refs=["H2.7B"])


@tpl("algebra.quadratics", "algebra", n=7)
def quad_factorise_solve(r):
    a = r.choice([2, 3, 4, 5, 6])
    p, q = nz(r, -7, 7), nz(r, -7, 7)
    c = r.choice([1, 2, 3])
    if math.gcd(a, p) != 1:
        return None
    e = sp.expand((a * x + p) * (c * x + q))
    rhs = r.randint(-10, 10)
    lhs = e + rhs
    roots = sorted(sp.solve(e, x))
    return Q(parts=[P("", f"Solve $${lx(lhs)} = {rhs}$$\n\nShow clear algebraic working.", 3, prefix="")],
             rows=[R("", f"${lx(e)} = 0$", "M1", "for rearranging to a 3-term quadratic = 0" if rhs else "for a correct method to start"),
                   R("", f"$({lin_tex(a, p)})({lin_tex(c, q)}) = 0$", "M1", "for correct factorisation or correct use of the formula"),
                   R("", f"$x = {lx(roots[0])}$, $x = {lx(roots[1])}$", "A1", "dep on M1")],
             values={"roots": [str(t) for t in roots]}, diff="4-6" if c == 1 else "7-9", cw="Solve", refs=["H2.7A"])


@tpl("algebra.quadratics", "problem", n=14)
def quad_context(r):
    kind = r.choice(["rect", "tri", "path", "consec"])
    for _ in range(80):
        if kind == "rect":
            a, b = r.randint(1, 5), r.randint(-3, 6)
            w = r.randint(3, 15)
            l = w + a if r.random() < 0.5 else 2 * w + b
            if l <= w:
                continue
            lexp = f"x + {a}" if l == w + a else lin_tex(2, b)
            A = w * l
            e = x * (x + a) - A if l == w + a else x * (2 * x + b) - A
            sols = [s for s in sp.solve(e, x) if s > 0]
            if len(sols) != 1 or sols[0] != w:
                continue
            intro = f"A rectangle has width $x$ cm and length $({lexp})$ cm. The area of the rectangle is {A} cm²."
            ask = "Work out the perimeter of the rectangle.\n\nShow clear algebraic working."
            ans = 2 * (w + l)
            rows = [R("", f"$x({lexp}) = {A}$", "M1", "for a correct equation"),
                    R("", f"${lx(sp.expand(e))} = 0$", "M1", "for a correct quadratic = 0"),
                    R("", f"$x = {w}$", "A1", "may also see the negative root rejected"),
                    R("", str(ans), "A1", "cao")]
            break
        elif kind == "tri":
            a = r.randint(1, 6)
            h = r.randint(4, 16)
            base = h + a
            A = F(h * base, 2)
            if A.denominator != 1:
                continue
            e = sp.expand(x * (x + a) / 2 - int(A))
            intro = f"A right-angled triangle has height $x$ cm and base $(x + {a})$ cm. The area of the triangle is {A} cm²."
            ask = "Work out the length of the hypotenuse of the triangle.\n\nGive your answer correct to 3 significant figures."
            hyp = math.hypot(h, base)
            ans = sf(hyp, 3)
            rows = [R("", f"$\\frac{{1}}{{2}}x(x + {a}) = {A}$", "M1", ""), R("", f"${lx(sp.expand(2 * e))} = 0$", "M1", ""),
                    R("", f"$x = {h}$", "A1", ""), R("", f"$\\sqrt{{{h}^2 + {base}^2}}$", "M1", "ft their positive $x$"),
                    R("", ans, "A1", "awrt " + ans)]
            break
        elif kind == "path":
            L_, W_ = r.randint(8, 20), r.randint(5, 12)
            wd = r.choice([1, 2, 3])
            tot = (L_ + 2 * wd) * (W_ + 2 * wd)
            path = tot - L_ * W_
            intro = f"A rectangular garden is {L_} m long and {W_} m wide. A path of width $x$ metres is put around the outside of the garden. The area of the path is {path} m²."
            ask = "Work out the value of $x$.\n\nShow clear algebraic working."
            e = sp.expand((L_ + 2 * x) * (W_ + 2 * x) - L_ * W_ - path)
            ans = str(wd)
            rows = [R("", f"$({L_} + 2x)({W_} + 2x) - {L_ * W_} = {path}$", "M1", "for a correct equation for the area of the path"),
                    R("", f"${lx(e)} = 0$", "M1", "for a correct simplified quadratic"),
                    R("", "correct factorisation or use of the formula", "M1", ""),
                    R("", ans, "A1", "reject the negative root")]
            break
        else:
            k = r.randint(3, 15)
            prod = k * (k + 2)
            intro = f"The product of two consecutive odd numbers is {prod}."
            ask = "Use algebra to find the two numbers. Both numbers are positive."
            rows = [R("", f"$n(n + 2) = {prod}$", "M1", "or $(2m - 1)(2m + 1) = " + str(prod) + "$"),
                    R("", f"$n^2 + 2n - {prod} = 0$", "M1", ""), R("", f"$(n - {k})(n + {k + 2}) = 0$", "M1", ""),
                    R("", f"{k} and {k + 2}", "A1", "")]
            ans = f"{k}, {k + 2}"
            if k % 2 == 0:
                continue
            break
    else:
        return None
    return Q(intro=intro, parts=[P("", ask, sum(int(rw["marks"][1:]) for rw in rows), prefix="")], rows=rows,
             values={"answer": ans}, diff="7-9", cw="Work out", refs=["H2.7C", "H2.7A"])


@tpl("algebra.quadratics", "proof", n=14)
def quad_show(r):
    for _ in range(60):
        kind = r.choice(["rect", "lshape", "trap"])
        if kind == "rect":
            a, b, c = r.randint(1, 4), nz(r, -3, 5), r.randint(1, 5)
            A = r.randint(20, 90)
            # (a x + b)(x + c) = A
            e = sp.expand((a * x + b) * (x + c) - A)
            co = sp.Poly(e, x).all_coeffs()
            g = math.gcd(*[int(t) for t in co])
            e2 = sp.expand(e / g)
            intro = f"The diagram shows a rectangle. The length is $({lin_tex(a, b)})$ cm and the width is $({lin_tex(1, c)})$ cm. The area of the rectangle is {A} cm²."
            stmt = f"Show that ${lx(e2)} = 0$"
            rows = [R("", f"$({lin_tex(a, b)})({lin_tex(1, c)}) = {A}$", "M1", "for a correct expression for the area set equal to " + str(A)),
                    R("", f"${lx(sp.expand((a * x + b) * (x + c)))} = {A}$", "M1", "for correct expansion"),
                    R("", f"${lx(e2)} = 0$", "A1", "dep on M2, correctly rearranged")]
            from maths_util import polygon_fig
            w0, l0 = 2.0, 3.4
            figs = [fig(polygon_fig([(0, 0), (l0, 0), (l0, w0), (0, w0)], sides={(0, 1): f"{lin_tex(a, b)}", (1, 2): f"{lin_tex(1, c)}"}, right=[0, 1, 2, 3], w=260, h=170), 60)]
            figs[0]["svg"] = figs[0]["svg"].replace("^", "")
        elif kind == "trap":
            a = r.randint(1, 5)
            h_ = r.randint(2, 6)
            A = r.randint(20, 80)
            # parallel sides x and x + a, height x + h  area = 1/2 (2x + a)(x + h) = A
            e = sp.expand((2 * x + a) * (x + h_) - 2 * A)
            g = math.gcd(*[int(t) for t in sp.Poly(e, x).all_coeffs()])
            e2 = sp.expand(e / g)
            intro = f"A trapezium has parallel sides of length $x$ cm and $(x + {a})$ cm. The perpendicular distance between the parallel sides is $(x + {h_})$ cm. The area of the trapezium is {A} cm²."
            stmt = f"Show that ${lx(e2)} = 0$"
            rows = [R("", f"$\\frac{{1}}{{2}}(x + x + {a})(x + {h_}) = {A}$", "M1", ""),
                    R("", f"${lx(sp.expand((2 * x + a) * (x + h_)))} = {2 * A}$", "M1", "for correct expansion and removal of the fraction"),
                    R("", f"${lx(e2)} = 0$", "A1", "dep on M2")]
            figs = None
        else:
            a, b = r.randint(4, 9), r.randint(3, 7)
            A = r.randint(25, 60)
            # L-shape: big square side x+a minus square side x? area = (x+a)^2 - x^2 linear. use rect (x+a) by (x+b) minus x by 2
            e = sp.expand((x + a) * (x + b) - 2 * x - A)
            intro = f"A rectangle measures $(x + {a})$ cm by $(x + {b})$ cm. A rectangle measuring $x$ cm by 2 cm is cut from one corner. The area of the shape that is left is {A} cm²."
            stmt = f"Show that ${lx(e)} = 0$"
            rows = [R("", f"$(x + {a})(x + {b}) - 2x = {A}$", "M1", ""),
                    R("", f"$x^2 + {a + b}x + {a * b} - 2x = {A}$", "M1", ""),
                    R("", f"${lx(e)} = 0$", "A1", "dep on M2")]
            figs = None
        disc = sp.discriminant(e, x)
        if disc <= 0:
            continue
        break
    else:
        return None
    return Q(intro=intro, figs=figs, parts=[P("", stmt, 3, space="working")], rows=rows,
             values={"equation": str(e)}, diff="7-9", cw="Show that", refs=["H2.7C"])


# ---------------------------------------------------------------- 2.7D nonlinear simultaneous
@tpl("algebra.simultaneous-nonlinear", "algebra", n=16)
def nonlinear(r):
    kind = r.choice(["circle", "parab", "parab"])
    for _ in range(100):
        if kind == "circle":
            pts = [(3, 4), (4, 3), (5, 0), (0, 5), (-3, 4), (-4, 3), (3, -4), (4, -3), (-3, -4), (-4, -3), (1, 7), (7, 1), (5, 5), (-1, 7), (7, -1), (5, -5), (6, 8), (8, 6), (0, 10), (10, 0), (6, -8), (8, -6)]
            p1, p2 = r.sample(pts, 2)
            R2 = p1[0] ** 2 + p1[1] ** 2
            if p2[0] ** 2 + p2[1] ** 2 != R2 or p1[0] == p2[0]:
                continue
            m = F(p2[1] - p1[1], p2[0] - p1[0])
            if m.denominator != 1:
                continue
            m = int(m)
            c = p1[1] - m * p1[0]
            eq2 = f"x^2 + y^2 = {R2}"
            eq1 = f"y = {lin_tex(m, c)}" if m != 0 else f"y = {c}"
            sols = sp.solve([y - (m * x + c), x ** 2 + y ** 2 - R2], [x, y])
            sub = f"x^2 + ({lin_tex(m, c)})^2 = {R2}"
            quad = sp.expand(x ** 2 + (m * x + c) ** 2 - R2)
        else:
            a = r.choice([1, 2, 3])
            x1, x2 = nz(r, -5, 5), nz(r, -5, 5)
            if x1 == x2:
                continue
            m, c = nz(r, -6, 6), r.randint(-6, 6)
            # y = a x^2 + b x + d ; intersections with y = m x + c at x1,x2: a(x-x1)(x-x2) = ax^2+bx+d - m x - c
            b = -a * (x1 + x2) + m
            d = a * x1 * x2 + c
            eq2 = f"y = {poly_tex([a, b, d])}"
            eq1 = f"y = {lin_tex(m, c)}" if m else f"y = {c}"
            sols = sp.solve([y - (m * x + c), y - (a * x ** 2 + b * x + d)], [x, y])
            sub = f"{poly_tex([a, b, d])} = {lin_tex(m, c)}"
            quad = sp.expand(a * x ** 2 + b * x + d - m * x - c)
            g = math.gcd(*[int(t) for t in sp.Poly(quad, x).all_coeffs()])
            quad = sp.expand(quad / g)
        if len(sols) != 2:
            continue
        sols = sorted(sols)
        break
    else:
        return None
    st = "; ".join(f"$x = {s[0]}, y = {s[1]}$" for s in sols)
    return Q(parts=[P("", f"Solve the simultaneous equations\n\n$${eq1}$$\n$${eq2}$$\n\nShow clear algebraic working.", 5, prefix="")],
             rows=[R("", f"${sub}$", "M1", "for substituting the linear equation into the other equation"),
                   R("", f"${lx(quad)} = 0$", "A1", "for a correct 3-term quadratic = 0 (may be in $y$)"),
                   R("", "correct factorisation or formula for their quadratic", "M1", "dep on first M1"),
                   R("", f"$x = {sols[0][0]}$ and $x = {sols[1][0]}$", "M1", "for both values of one variable and substituting to find the other"),
                   R("", st, "A1", "dep on first M1; must be correctly paired")],
             values={"solutions": [[int(s[0]), int(s[1])] for s in sols]}, diff="7-9", cw="Solve", refs=["H2.7D"])


# ---------------------------------------------------------------- 2.8 inequalities
@tpl("algebra.inequalities", "algebra", n=8)
def ineq_linear(r):
    a, b, c, d = r.randint(2, 9), nz(r, -12, 12), r.randint(1, 6), nz(r, -12, 12)
    if a == c:
        return None
    sym_ = r.choice(["<", ">", "\\leqslant", "\\geqslant"])
    bound = F(d - b, a - c)
    flip = (a - c) < 0
    rev = {"<": ">", ">": "<", "\\leqslant": "\\geqslant", "\\geqslant": "\\leqslant"}
    fs = rev[sym_] if flip else sym_
    if r.random() < 0.5:
        return Q(parts=[P("", f"Solve $${lin_tex(a, b)} {sym_} {lin_tex(c, d)}$$", 2, prefix="")],
                 rows=[R("", f"${a - c}x {sym_} {d - b}$" if not flip else f"${a - c}x {sym_} {d - b}$ or ${c - a}x {rev[sym_]} {b - d}$", "M1", "for collecting terms; condone an incorrect inequality sign or $=$"),
                       R("", f"$x {fs} {ftex(bound)}$", "A1", "oe")],
                 values={"bound": bound, "sign": fs}, diff="4-6", cw="Solve", refs=["F2.8C"])
    lo, hi = r.randint(-8, 2), r.randint(4, 15)
    m, k = r.randint(2, 5), nz(r, -6, 6)
    lo_v, hi_v = F(lo - k, m), F(hi - k, m)
    ints = [i for i in range(-30, 31) if lo_v < i <= hi_v]
    if not ints or len(ints) > 9:
        return None
    return Q(parts=[P("", f"$n$ is an integer.\n\nList all the values of $n$ such that $${lo} < {lin_tex(m, k, 'n')} \\leqslant {hi}$$", 3, prefix="")],
             rows=[R("", f"${lo - k} < {m}n \\leqslant {hi - k}$", "M1", "for a correct first step"),
                   R("", f"${ftex(lo_v)} < n \\leqslant {ftex(hi_v)}$", "M1", "for a fully correct inequality or a list with at most one error or omission"),
                   R("", ", ".join(map(str, ints)), "A1", "cao")],
             values={"values": ints}, diff="4-6", cw="List", refs=["F2.8C", "F2.8A"])


@tpl("algebra.inequalities", "algebra", n=8)
def ineq_quadratic(r):
    kind = r.choice(["fact", "sq"])
    if kind == "sq":
        k = r.choice([4, 9, 16, 25, 36, 49, 64, 81, 100])
        a = r.choice([1, 4, 9]) if k in (4, 16, 36, 64, 100) else 1
        s = r.choice([">", "<", "\\leqslant", "\\geqslant"])
        rt = F(math.isqrt(k), math.isqrt(a))
        e = f"{'' if a == 1 else a}x^2 {s} {k}"
        crit = f"$x = \\pm {ftex(rt)}$"
        ans = f"$-{ftex(rt)} {s} x {s} {ftex(rt)}$" if s in ("<", "\\leqslant") else f"$x {'<' if s == '>' else '\\leqslant'} -{ftex(rt)}$ or $x {s} {ftex(rt)}$"
        vals = {"critical": [str(-rt), str(rt)], "type": "inside" if s in ("<", "\\leqslant") else "outside"}
    else:
        p, q = sorted(r.sample(range(-8, 9), 2))
        e2 = sp.expand((x - p) * (x - q))
        s = r.choice([">", "<", "\\leqslant", "\\geqslant"])
        e = f"{lx(e2)} {s} 0"
        crit = f"$x = {p}$, $x = {q}$"
        if s in ("<", "\\leqslant"):
            ans = f"${p} {s} x {s} {q}$"
        else:
            o = "<" if s == ">" else "\\leqslant"
            ans = f"$x {o} {p}$ or $x {s} {q}$"
        vals = {"critical": [p, q], "type": "inside" if s in ("<", "\\leqslant") else "outside"}
    return Q(parts=[P("", f"Solve the inequality $${e}$$", 3, prefix="")],
             rows=[R("", crit, "M1", "for finding the critical values"),
                   R("", "a sketch or test showing the correct region", "M1", "for identifying the correct region, eg inside or outside the critical values"),
                   R("", ans, "A1", "oe, eg set notation")],
             values=vals, diff="7-9", cw="Solve", refs=["H2.8A"])


def _region_items(lines, shade_pts=None):
    def f(M):
        out = ""
        for (a, b, c, dash) in lines:  # a x + b y = c
            if b:
                cand = [(X, (c - a * X) / b) for X in (-1, 9)]
                if a:
                    cand += [((c - b * Y) / a, Y) for Y in (-1, 9)]
            else:
                cand = [(c / a, -1), (c / a, 9)]
            pts = sorted({(round(X, 9), round(Y, 9)) for X, Y in cand if -1 - 1e-9 <= X <= 9 + 1e-9 and -1 - 1e-9 <= Y <= 9 + 1e-9})
            if len(pts) < 2:
                continue
            P1, P2 = M(pts[0]), M(pts[-1])
            out += L(*P1, *P2, w=1.6, dash="6,4" if dash else None)
        if shade_pts:
            out += PL([M(p) for p in shade_pts], close=True, w=0.8, fill="currentColor").replace('fill="currentColor"', 'fill="currentColor" fill-opacity="0.18"')
        return out
    return f


@tpl("algebra.inequalities", "graph", n=8)
def region_describe(r):
    for _ in range(80):
        k = r.randint(1, 3)
        m = r.choice([1, 2, -1, -2])
        c = r.randint(1, 4) if m > 0 else r.randint(5, 8)
        xk = r.randint(1, 4)
        # region: y >= k, y <= m x + c, x <= xk  (or x+y<=s)
        s_ = r.randint(5, 8)
        verts = []
        lines = [(0, 1, k), (-m, 1, c), (1, 1, s_)]
        import itertools
        for (a1, b1, c1), (a2, b2, c2) in itertools.combinations(lines, 2):
            det = a1 * b2 - a2 * b1
            if det == 0:
                continue
            X = F(c1 * b2 - c2 * b1, det)
            Y = F(a1 * c2 - a2 * c1, det)
            verts.append((X, Y))
        ok = [(X, Y) for X, Y in verts if Y >= k and Y <= m * X + c and X + Y <= s_]
        if len(ok) != 3 or any(not (0 <= v[0] <= 8 and 0 <= v[1] <= 8) for v in ok):
            continue
        if len({(float(a), float(b)) for a, b in ok}) < 3:
            continue
        break
    else:
        return None
    svgs = grid_fig(-1, 9, -1, 9, items=_region_items([(0, 1, k, False), (-m, 1, c, False), (1, 1, s_, False)],
                                                      [(float(X), float(Y)) for X, Y in ok]), w=320, h=300)
    ans = [f"y \\geqslant {k}", f"y \\leqslant {lin_tex(m, c)}", f"x + y \\leqslant {s_}"]
    return Q(intro="Three straight lines form the edges of the shaded region **R**.",
             figs=[fig(svgs, 85, note=None)],
             parts=[P("", "Find the three inequalities satisfied by the points of **R** and by no other points.", 4, space="lines", lines=3)],
             rows=[R("", f"$y = {k}$, $y = {lin_tex(m, c)}$ and $x + y = {s_}$", "B2", "B1 for any two of the three line equations; may be seen as inequalities with incorrect signs"),
                   R("", f"${ans[0]}$, ${ans[1]}$, ${ans[2]}$", "B2", "B1 for two correct inequalities; accept strict inequalities")],
             values={"inequalities": ans}, diff="7-9", cw="Write down", refs=["H2.8B", "F2.8E"])


@tpl("algebra.inequalities", "graph", n=8)
def region_shade(r):
    a = r.randint(1, 3)
    b = r.randint(3, 6)
    m = r.choice([1, 2])
    c = r.randint(-1, 2)
    xk = r.randint(1, 3)
    # y < b, y > m x + c, x > -? region with x >= xk? choose x >= 0
    ver = [(0, max(c, 0) if c >= 0 else 0)]
    svgs = grid_fig(-2, 7, -2, 8, items="", w=320, h=300)
    lines = [f"y \\leqslant {b}", f"y \\geqslant {lin_tex(m, c)}", "x \\geqslant 0" if r.random() < 0.5 else f"x \\geqslant {-a + 1 if a > 1 else 0}"]
    if lines[2] == "x \\geqslant 0":
        xmin = 0
    else:
        xmin = -a + 1 if a > 1 else 0
    # vertices
    v1 = (xmin, b)
    v2 = (xmin, m * xmin + c)
    v3 = (F(b - c, m), b)
    if v3[0] < xmin + 1.5 or m * xmin + c > b - 2:
        return None
    return Q(figs=[fig(svgs, 85, note=None)],
             parts=[P("", "On the grid, show by shading the region that satisfies all three of the inequalities\n\n$$" +
                      ",\\quad ".join(lines) + "$$\n\nLabel the region **R**.", 4, space="graph")],
             rows=[R("", f"line $y = {b}$ drawn", "B1", ""), R("", f"line $y = {lin_tex(m, c)}$ drawn", "B1", ""),
                   R("", f"line $x = {xmin}$ drawn" if xmin else "the $y$-axis used as the boundary $x = 0$", "B1", "lines may be solid or dashed"),
                   R("", f"correct region shaded or labelled R: the triangle with vertices $({xmin}, {b})$, $({xmin}, {m * xmin + c})$ and $({num(float(v3[0]))}, {b})$", "B1", "")],
             values={"vertices": [[xmin, b], [xmin, m * xmin + c], [float(v3[0]), b]]}, diff="4-6", cw="Show",
             refs=["F2.8E", "H2.8B"])
