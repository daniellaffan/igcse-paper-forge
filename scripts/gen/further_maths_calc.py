"""4PM1 templates: 9 calculus."""
import math

import sympy as sp

from further_maths_util import tpl, P, R, Q, tex, sf, dp, fr, nz, fig, Axes, x, t, name_ctx, xpow

E = sp.E


def d_(e):
    return sp.diff(e, x)


def nice(e):
    return tex(sp.simplify(e))


def dydx(e):
    return f"\\dfrac{{\\mathrm{{d}}y}}{{\\mathrm{{d}}x}}"


DY = "\\dfrac{\\mathrm{d}y}{\\mathrm{d}x}"
D2Y = "\\dfrac{\\mathrm{d}^2y}{\\mathrm{d}x^2}"


def _powers(r, k=3, neg=True):
    pool = [4, 3, 2, 1, sp.Rational(1, 2), sp.Rational(3, 2)] + ([-1, -2, sp.Rational(-1, 2)] if neg else [])
    ps = r.sample(pool, k)
    cs = [nz(r, -6, 6) for _ in ps]
    return sum(sp.Rational(c) * x ** sp.Rational(p_) for c, p_ in zip(cs, ps)), ps


def ytex(e):
    """y = ... display with sqrt and 1/x forms kept readable."""
    return tex(e)


def curve_fig(f, xr, yr, shade=None, pts=(), lines=()):
    ax = Axes(xr, yr, 330, 240)
    ax.axes()
    if shade:
        ax.shade(*shade)
    ax.curve(f)
    for m, c in lines:
        ax.line(m, c)
    for px, py, lab in pts:
        ax.point(px, py, lab)
    return fig(ax.svg(), 70)


# =============================================================== 9A differentiation of powers


@tpl("calc.diff", "short", 22)
def cd_short(r):
    v = r.choice(["deriv", "grad", "second"])
    e, ps = _powers(r, 3)
    de = d_(e)
    if v == "deriv":
        parts = [P("", f"Given that $y = {ytex(e)}$, find ${DY}$", 3)]
        rows = [R("", "At least one power reduced by 1", "M1"), R("", "Two terms correct", "A1"),
                R("", f"${DY} = {tex(de)}$", "A1", "all correct, any equivalent form")]
        return dict(Q(parts=parts, rows=rows, values={"dydx": str(de)}, diff="1-3", cw="Find", refs=["9A"]), variant=v)
    x0 = r.choice([1, 4, 9, 2]) if any(sp.Rational(p_).q == 2 for p_ in ps) else r.choice([1, 2, -1, 3, -2])
    g = de.subs(x, x0)
    if not g.is_rational:
        return None
    if sp.Rational(g).q > 32 or abs(g) > 2000:
        return None
    if v == "grad":
        parts = [P("", f"The curve $C$ has equation $y = {ytex(e)}$, $x > 0$\n\nFind the gradient of $C$ at the point where $x = {x0}$", 4)]
        if x0 <= 0:
            return None
        rows = [R("", "At least one power reduced by 1", "M1"), R("", f"${DY} = {tex(de)}$", "A1"),
                R("", f"Substitutes $x = {x0}$", "M1", "dM1"), R("", f"${fr(g)}$", "A1")]
        return dict(Q(parts=parts, rows=rows, values={"gradient": g}, diff="4-6", cw="Find", refs=["9A"]), variant=v)
    d2 = d_(de)
    if x0 <= 0:
        return None
    parts = [P("", f"Given that $y = {ytex(e)}$, find the value of ${D2Y}$ when $x = {x0}$", 4)]
    rows = [R("", f"${DY} = {tex(de)}$", "M1 A1"), R("", f"${D2Y} = {tex(d2)}$", "M1", "differentiates their first derivative"),
            R("", f"${fr(d2.subs(x, x0))}$", "A1")]
    if not d2.subs(x, x0).is_rational or sp.Rational(d2.subs(x, x0)).q > 32 or abs(d2.subs(x, x0)) > 2000:
        return None
    return dict(Q(parts=parts, rows=rows, values={"d2y": d2.subs(x, x0)}, diff="4-6", cw="Find", refs=["9A"]), variant=v)


@tpl("calc.diff", "show-that", 22)
def cd_show(r):
    v = r.choice(["exp", "trig", "poly"])
    k = r.choice([2, 3, 4, 5, sp.Rational(1, 2)])
    A, B = nz(r, -5, 5), nz(r, -5, 5)
    if v == "exp":
        e = A * sp.exp(k * x) + B * sp.exp(-k * x)
        parts = [P("a", f"Given that $y = {tex(e)}$, find ${DY}$", 2),
                 P("b", f"Show that ${D2Y} = {fr(k ** 2)}y$", 2)]
        rows = [R("a", f"${tex(d_(e))}$", "M1 A1", "M1 for $\\mathrm{e}^{ax} \\to a\\mathrm{e}^{ax}$"),
                R("b", f"${D2Y} = {tex(d_(d_(e)))}$", "M1"), R("b", f"$= {fr(k ** 2)}({tex(e)}) = {fr(k ** 2)}y$", "A1", "cso")]
        assert sp.simplify(d_(d_(e)) - k ** 2 * e) == 0
        return dict(Q(parts=parts, rows=rows, values={"dydx": str(d_(e))}, diff="4-6", cw="Show that", refs=["9A", "9B"]), variant=v)
    if v == "trig":
        e = A * sp.sin(k * x) + B * sp.cos(k * x)
        parts = [P("a", f"Given that $y = {tex(e)}$, find ${DY}$", 2),
                 P("b", f"Show that ${D2Y} + {fr(k ** 2)}y = 0$", 2)]
        rows = [R("a", f"${tex(d_(e))}$", "M1 A1"), R("b", f"${D2Y} = {tex(d_(d_(e)))}$", "M1"),
                R("b", f"$= -{fr(k ** 2)}y$ so ${D2Y} + {fr(k ** 2)}y = 0$", "A1", "cso")]
        assert sp.simplify(d_(d_(e)) + k ** 2 * e) == 0
        return dict(Q(parts=parts, rows=rows, values={"dydx": str(d_(e))}, diff="4-6", cw="Show that", refs=["9A", "9B"]), variant=v)
    a_, b_ = nz(r, -4, 4), r.randint(-9, 9)
    c_ = sp.Rational(r.choice([4, 8, 12, 16, 2, 6]))
    e = a_ * x ** 3 + b_ * x ** 2 + c_ / x
    x0 = r.choice([1, 2, -1, -2])
    g = d_(e).subs(x, x0)
    y0 = e.subs(x, x0)
    parts = [P("a", f"The curve $C$ has equation $y = {tex(e)}$, $x \\neq 0$. The point $P$ with $x$-coordinate ${x0}$ lies on $C$\n\nShow that the gradient of $C$ at $P$ is ${fr(g)}$", 3),
             P("b", "Find an equation of the tangent to $C$ at $P$, giving your answer in the form $y = mx + c$", 3)]
    cc = y0 - g * x0
    rows = [R("a", "Powers reduced by 1, including the $x^{-1}$ term", "M1"), R("a", f"${DY} = {tex(d_(e))}$", "A1"),
            R("a", f"Substitutes $x = {x0}$ to obtain ${fr(g)}$", "A1", "cso"),
            R("b", f"$y = {fr(y0)}$ at $P$", "B1"), R("b", f"$y - ({fr(y0)}) = {fr(g)}(x - ({x0}))$", "M1"),
            R("b", f"$y = {tex(g * x + cc)}$", "A1")]
    return dict(Q(parts=parts, rows=rows, values={"gradient": g, "tangent": str(g * x + cc)}, diff="4-6", cw="Show that",
                  refs=["9A", "9F"]), variant=v)


# =============================================================== 9B product / quotient / chain


def _rule_expr(r, kind):
    a, b = nz(r, 1, 5), nz(r, -6, 6)
    n_ = r.choice([2, 3, 4])
    k = nz(r, -3, 4)
    if kind == "product":
        return r.choice([x ** n_ * sp.exp(k * x), x ** n_ * sp.sin(k * x), x ** n_ * sp.log(x), (a * x + b) * sp.cos(k * x),
                         x * sp.sqrt(a * x + abs(b) + 1)])
    if kind == "quotient":
        c, d = nz(r, 1, 4), nz(r, -6, 6)
        if a * d - b * c == 0:
            d += 1
        return r.choice([(a * x + b) / (c * x + d), sp.exp(k * x) / x ** n_, sp.sin(abs(k) * x) / x, x ** 2 / (c * x + d),
                         sp.log(x) / x ** n_])
    return r.choice([(a * x + b) ** (n_ + 2), sp.sqrt(a * x ** 2 + abs(b) + 1), sp.exp(k * x ** 2), sp.log(a * x ** 2 + abs(b) + 1),
                     sp.sin(k * x + b) ** 2 if False else sp.cos(a * x + b) ** 3, 1 / (a * x + b) ** n_])


@tpl("calc.rules", "short", 22)
def cr_short(r):
    v = r.choice(["product", "quotient", "chain"])
    e = _rule_expr(r, v)
    de = sp.simplify(d_(e))
    if v == "chain":
        de = sp.factor(d_(e))
    rule = {"product": "$u'v + uv'$ with $u$ and $v$ identified", "quotient": "$\\dfrac{vu' - uv'}{v^2}$ correctly structured",
            "chain": "Chain rule: derivative of the outer function times derivative of the inner function"}[v]
    parts = [P("", f"Differentiate with respect to $x$\n\n$$y = {tex(e)}$$", 3 if v != "chain" else 2)]
    rows = [R("", rule, "M1"), R("", "One term (or factor) correct", "A1")] if v != "chain" else [R("", rule, "M1")]
    rows.append(R("", f"${DY} = {tex(de)}$", "A1", "any correct equivalent form; isw"))
    return dict(Q(parts=parts, rows=rows, values={"dydx": str(de)}, diff="4-6", cw="Differentiate", refs=["9B"]), variant=v)


@tpl("calc.rules", "show-that", 22)
def cr_show(r):
    v = r.choice(["quot", "prodexp", "rootprod"])
    if v == "quot":
        a, b, c, d = nz(r, 1, 6), nz(r, -7, 7), nz(r, 1, 5), nz(r, -7, 7)
        K = a * d - b * c
        if K == 0:
            return None
        e = (a * x + b) / (c * x + d)
        x0 = r.choice([0, 1, 2, -1])
        if c * x0 + d == 0:
            return None
        g = d_(e).subs(x, x0)
        parts = [P("a", f"Given that $y = \\dfrac{{{tex(a * x + b)}}}{{{tex(c * x + d)}}}$, show that ${DY} = \\dfrac{{{K}}}{{({tex(c * x + d)})^2}}$", 3),
                 P("b", f"Find the gradient of the curve at the point where $x = {x0}$", 1),
                 P("c", f"Explain why the curve has no stationary points.", 1)]
        rows = [R("a", "Quotient rule with correct structure", "M1"),
                R("a", f"$\\dfrac{{{a}({tex(c * x + d)}) - {c}({tex(a * x + b)})}}{{({tex(c * x + d)})^2}}$", "A1"),
                R("a", f"$= \\dfrac{{{K}}}{{({tex(c * x + d)})^2}}$", "A1", "cso"),
                R("b", f"${fr(g)}$", "B1"),
                R("c", f"Numerator is ${K} \\neq 0$, so ${DY}$ is never zero", "B1")]
        return dict(Q(parts=parts, rows=rows, values={"K": K, "gradient": g}, diff="4-6", cw="Show that", refs=["9B", "9D"]), variant=v)
    if v == "prodexp":
        n_, k = r.choice([2, 3]), nz(r, -3, 3)
        e = x ** n_ * sp.exp(k * x)
        fac = sp.factor(d_(e))
        xs = sorted(sp.solve(sp.simplify(d_(e) / sp.exp(k * x)), x))
        parts = [P("a", f"Given that $y = {tex(e)}$, show that ${DY} = {xpow(n_ - 1)}\\mathrm{{e}}^{{{tex(k * x)}}}({tex(n_ + k * x)})$", 3),
                 P("b", "Hence find the exact coordinates of the stationary points of the curve.", 3)]
        pts = [(xx, e.subs(x, xx)) for xx in xs]
        rows = [R("a", "Product rule", "M1"), R("a", f"${tex(n_ * x ** (n_ - 1))}\\mathrm{{e}}^{{{tex(k * x)}}} + {tex(k * x ** n_)}\\mathrm{{e}}^{{{tex(k * x)}}}$".replace("+ -", "- "), "A1"),
                R("a", "Factorises to the given answer", "A1", "cso"),
                R("b", f"Sets ${DY} = 0$ and uses $\\mathrm{{e}}^{{{tex(k * x)}}} > 0$", "M1"),
                R("b", f"$x = {', '.join(fr(xx) for xx in xs)}$", "A1"),
                R("b", "; ".join(f"$({fr(px)}, {tex(py)})$" for px, py in pts), "A1")]
        assert sp.simplify(fac - x ** (n_ - 1) * sp.exp(k * x) * (n_ + k * x)) == 0
        return dict(Q(parts=parts, rows=rows, values={"x": xs, "points": [[px, py] for px, py in pts]}, diff="7-9", cw="Show that",
                      refs=["9B", "9D"]), variant=v)
    a, b = nz(r, 1, 6), r.randint(1, 9)
    e = x * sp.sqrt(a * x + b)
    target = (3 * a * x + 2 * b) / (2 * sp.sqrt(a * x + b))
    assert sp.simplify(d_(e) - target) == 0
    x0 = sp.Rational(-2 * b, 3 * a)
    parts = [P("a", f"Given that $y = x\\sqrt{{{tex(a * x + b)}}}$, show that ${DY} = \\dfrac{{{tex(3 * a * x + 2 * b)}}}{{2\\sqrt{{{tex(a * x + b)}}}}}$", 4),
             P("b", "Find the $x$-coordinate of the point where the gradient of the curve is zero.", 1)]
    rows = [R("a", "Product rule", "M1"), R("a", f"Chain rule for $\\sqrt{{{tex(a * x + b)}}}$: $\\dfrac{{{a}}}{{2\\sqrt{{{tex(a * x + b)}}}}}$", "M1"),
            R("a", f"$\\sqrt{{{tex(a * x + b)}}} + \\dfrac{{{a}x}}{{2\\sqrt{{{tex(a * x + b)}}}}}$", "A1"),
            R("a", "Combines over a common denominator to the given answer", "A1", "cso"),
            R("b", f"$x = {fr(x0)}$", "B1")]
    return dict(Q(parts=parts, rows=rows, values={"x": x0}, diff="7-9", cw="Show that", refs=["9B"]), variant=v)


# =============================================================== integration


@tpl("calc.integration", "short", 22)
def ci_short(r):
    v = r.choice(["definite", "exp", "curve", "trig"])
    if v == "definite":
        e, ps = _powers(r, 3, neg=True)
        if any(p_ == -1 for p_ in ps):
            return None
        a, b = sorted(r.sample([1, 2, 3, 4], 2))
        I = sp.integrate(e, (x, a, b))
        if not I.is_rational or I.q > 60:
            return None
        F_ = sp.integrate(e, x)
        parts = [P("", f"Use algebraic integration to find the exact value of $$\\int_{{{a}}}^{{{b}}} \\left({tex(e)}\\right) \\mathrm{{d}}x$$", 4)]
        rows = [R("", "At least one power increased by 1", "M1"), R("", f"$\\left[{tex(F_)}\\right]$", "A1"),
                R("", "Substitutes both limits and subtracts", "M1", "dM1"), R("", f"${fr(I)}$", "A1")]
        return dict(Q(parts=parts, rows=rows, values={"integral": I}, diff="4-6", cw="Find", refs=["9A"]), variant=v)
    if v == "exp":
        k = r.choice([2, 3, sp.Rational(1, 2), -1, -2])
        A = r.choice([2, 4, 6, 3])
        c = r.randint(1, 5)
        e = A * sp.exp(k * x) + c
        b = r.choice([1, 2])
        I = sp.integrate(e, (x, 0, b))
        parts = [P("", f"Find the exact value of $$\\int_{{0}}^{{{b}}} \\left({tex(e)}\\right) \\mathrm{{d}}x$$", 3)]
        rows = [R("", f"$\\int \\mathrm{{e}}^{{ax}} \\, \\mathrm{{d}}x = \\dfrac{{1}}{{a}}\\mathrm{{e}}^{{ax}}$ used", "M1"),
                R("", f"$\\left[{tex(sp.integrate(e, x))}\\right]_0^{{{b}}}$", "A1"), R("", f"${tex(sp.expand(I))}$", "A1", "oe exact")]
        return dict(Q(parts=parts, rows=rows, values={"integral": sp.expand(I), "numeric": float(I)}, diff="4-6", cw="Find", refs=["9A"]), variant=v)
    if v == "trig":
        k = r.choice([2, 3, sp.Rational(1, 2)])
        A, B = nz(r, -4, 4), nz(r, -4, 4)
        e = A * sp.sin(k * x) + B * sp.cos(k * x)
        b = r.choice([sp.pi / 2, sp.pi / 4, sp.pi / 6, sp.pi / 3]) / k
        I = sp.nsimplify(sp.integrate(e, (x, 0, b)))
        parts = [P("", f"Find the exact value of $$\\int_{{0}}^{{{tex(b)}}} \\left({tex(e)}\\right) \\mathrm{{d}}x$$", 3)]
        rows = [R("", "Integrates $\\sin$ to $-\\cos$ and $\\cos$ to $\\sin$ with the factor $\\dfrac{1}{k}$", "M1"),
                R("", f"$\\left[{tex(sp.integrate(e, x))}\\right]$", "A1"), R("", f"${tex(sp.radsimp(I))}$", "A1")]
        return dict(Q(parts=parts, rows=rows, values={"integral": sp.radsimp(I)}, diff="4-6", cw="Find", refs=["9A", "10A"]), variant=v)
    e, ps = _powers(r, 2, neg=True)
    if -1 in ps:
        return None
    x0 = r.choice([1, 4]) if any(sp.Rational(p_).q == 2 for p_ in ps) else r.choice([1, 2, -1])
    yv = r.randint(-10, 10)
    F_ = sp.integrate(e, x)
    C = yv - F_.subs(x, x0)
    if not C.is_rational:
        return None
    parts = [P("", f"The curve $C$ passes through the point $({x0}, {yv})$ and has gradient function $${DY} = {tex(e)}$$\n\nFind an equation of $C$", 4, prefix="y = ")]
    rows = [R("", "Integrates, at least one power increased by 1", "M1"), R("", f"$y = {tex(F_)} + c$", "A1"),
            R("", f"Substitutes $({x0}, {yv})$ to find $c$", "M1", "dM1; constant of integration must appear"),
            R("", f"$y = {tex(F_ + C)}$", "A1")]
    return dict(Q(parts=parts, rows=rows, values={"y": str(F_ + C)}, diff="4-6", cw="Find", refs=["9A"]), variant=v)


# =============================================================== 9C area


@tpl("calc.area", "short", 22)
def ca_short(r):
    p_, q_ = sorted(r.sample(range(-4, 6), 2))
    k = r.choice([1, 2, 3])
    e = sp.expand(-k * (x - p_) * (x - q_))
    A = sp.integrate(e, (x, p_, q_))
    top = float(e.subs(x, sp.Rational(p_ + q_, 2)))
    f = sp.lambdify(x, e)
    fg = curve_fig(f, (min(p_, 0) - 1.2, max(q_, 0) + 1.2), (min(-1, -0.4 * top), top * 1.25), shade=(f, p_, q_))
    parts = [P("", f"The diagram shows part of the curve with equation $y = {tex(e)}$\n\nThe shaded region is bounded by the curve and the $x$-axis.\n\nUse algebraic integration to find the exact area of the shaded region.", 5)]
    rows = [R("", f"Solves ${tex(e)} = 0$: $x = {p_}$, $x = {q_}$", "M1 A1"),
            R("", "Integrates, at least one power increased by 1", "M1"),
            R("", f"$\\left[{tex(sp.integrate(e, x))}\\right]_{{{p_}}}^{{{q_}}}$", "M1", "dM1 uses their limits"),
            R("", f"${fr(A)}$", "A1")]
    return dict(Q(figs=[fg], parts=parts, rows=rows, values={"area": A}, diff="4-6", cw="Find", refs=["9C"]), variant="xaxis")


@tpl("calc.area", "multi-part", 22)
def ca_multi(r):
    p_, q_ = sorted(r.sample(range(-3, 6), 2))
    k = r.choice([1, 1, 2])
    m, c = nz(r, -3, 3), r.randint(-2, 6)
    line = m * x + c
    curve = sp.expand(line - k * (x - p_) * (x - q_))  # curve above line between p, q
    Ar = sp.integrate(curve - line, (x, p_, q_))
    f, g = sp.lambdify(x, curve), sp.lambdify(x, line)
    ys = [float(curve.subs(x, v_)) for v_ in (p_, q_, sp.Rational(p_ + q_, 2))] + [float(line.subs(x, p_)), float(line.subs(x, q_)), 0]
    fg = curve_fig(f, (min(p_, 0) - 1.5, max(q_, 0) + 1.5), (min(ys) - 2, max(ys) + 2), shade=(f, p_, q_, g), lines=[(m, c)],
                   pts=[(p_, float(line.subs(x, p_)), "A"), (q_, float(line.subs(x, q_)), "B")])
    intro = (f"The diagram shows the curve $C$ with equation $y = {tex(curve)}$ and the line $l$ with equation $y = {tex(line)}$\n\n"
             "The line $l$ meets $C$ at the points $A$ and $B$. The shaded region is bounded by $C$ and $l$")
    A_, B_ = (p_, line.subs(x, p_)), (q_, line.subs(x, q_))
    parts = [P("a", "Find the coordinates of $A$ and the coordinates of $B$", 4),
             P("b", "Use algebraic integration to find the exact area of the shaded region.", 5)]
    rows = [R("a", f"${tex(curve)} = {tex(line)}$", "M1"), R("a", f"${tex(sp.expand(curve - line))} = 0$", "A1"),
            R("a", "Solves their quadratic", "M1"), R("a", f"$A({p_}, {tex(A_[1])})$, $B({q_}, {tex(B_[1])})$", "A1"),
            R("b", "$\\int (\\text{curve} - \\text{line}) \\, \\mathrm{d}x$ or area under curve minus trapezium", "M1"),
            R("b", "Integrates, at least one power increased by 1", "M1"),
            R("b", f"$\\left[{tex(sp.integrate(curve - line, x))}\\right]_{{{p_}}}^{{{q_}}}$", "A1"),
            R("b", "Substitutes their limits", "M1", "dM1"), R("b", f"${fr(Ar)}$", "A1")]
    return dict(Q(intro=intro, figs=[fg], parts=parts, rows=rows, values={"A": list(A_), "B": list(B_), "area": Ar}, diff="7-9",
                  cw="Find", refs=["9C", "8E"]), variant="curve_line")


# =============================================================== 9C volume


@tpl("calc.volume", "short", 22)
def cv_short(r):
    v = r.choice(["poly", "root", "recip"])
    if v == "poly":
        a, b = r.randint(1, 3), r.randint(0, 4)
        e = a * x ** 2 + b if r.random() < 0.5 else a * x + b + 1
        lo, hi = sorted(r.sample([0, 1, 2, 3], 2))
    elif v == "root":
        a, b = r.randint(1, 4), r.randint(1, 6)
        e = sp.sqrt(a * x + b)
        lo, hi = 0, r.randint(1, 5)
    else:
        a = r.randint(1, 4)
        e = a / x
        lo, hi = r.choice([(1, 2), (1, 3), (2, 4), (1, 4)])
    V = sp.pi * sp.integrate(sp.expand(e ** 2), (x, lo, hi))
    parts = [P("", f"The region $R$ is bounded by the curve with equation $y = {tex(e)}$, the $x$-axis and the lines $x = {lo}$ and $x = {hi}$\n\nWhen $R$ makes one complete turn about the $x$-axis it sweeps out a solid of volume $V$\n\nUsing algebraic integration, find $V$ in terms of $\\pi$", 4)]
    rows = [R("", f"$\\pi \\int_{{{lo}}}^{{{hi}}} \\left({tex(e)}\\right)^2 \\mathrm{{d}}x$", "M1", "$\\pi$ may appear later"),
            R("", f"$\\pi \\int_{{{lo}}}^{{{hi}}} \\left({tex(sp.expand(e ** 2))}\\right) \\mathrm{{d}}x$", "A1"),
            R("", f"$\\pi\\left[{tex(sp.integrate(sp.expand(e ** 2), x))}\\right]_{{{lo}}}^{{{hi}}}$", "M1"),
            R("", f"${tex(V)}$", "A1", "exact")]
    return dict(Q(parts=parts, rows=rows, values={"volume": V, "numeric": float(V)}, diff="4-6", cw="Find", refs=["9C"]), variant=v)


@tpl("calc.volume", "multi-part", 22)
def cv_multi(r):
    p_ = r.randint(2, 7)
    k = r.choice([1, 2, 3, sp.Rational(1, 2), sp.Rational(1, 3)])
    e = sp.expand(k * x * (p_ - x))
    V = sp.pi * sp.integrate(sp.expand(e ** 2), (x, 0, p_))
    A = sp.integrate(e, (x, 0, p_))
    f = sp.lambdify(x, e)
    top = float(e.subs(x, sp.Rational(p_, 2)))
    fg = curve_fig(f, (-1, p_ + 1), (-0.4 * top, top * 1.3), shade=(f, 0, p_), pts=[(p_, 0, "A")])
    intro = f"The diagram shows part of the curve with equation $y = {tex(e)}$, which meets the $x$-axis at $O$ and at the point $A$. The shaded region $R$ is bounded by the curve and the $x$-axis."
    parts = [P("a", "Find the coordinates of $A$", 1),
             P("b", "Find the exact area of $R$", 3),
             P("c", f"Turning $R$ through one full revolution about the $x$-axis forms a solid. Prove that its volume is ${tex(V)}$", 5)]
    rows = [R("a", f"$({p_}, 0)$", "B1"),
            R("b", "Integrates their expression", "M1"), R("b", f"$\\left[{tex(sp.integrate(e, x))}\\right]_0^{{{p_}}}$", "M1"), R("b", f"${fr(A)}$", "A1"),
            R("c", f"$\\pi \\int_0^{{{p_}}} \\left({tex(e)}\\right)^2 \\mathrm{{d}}x$", "M1"),
            R("c", f"Expands: $\\pi \\int_0^{{{p_}}} \\left({tex(sp.expand(e ** 2))}\\right) \\mathrm{{d}}x$", "A1"),
            R("c", "Integrates their expansion", "M1"),
            R("c", f"$\\pi\\left[{tex(sp.integrate(sp.expand(e ** 2), x))}\\right]_0^{{{p_}}}$", "A1"),
            R("c", f"$= {tex(V)}$", "A1", "cso")]
    return dict(Q(intro=intro, figs=[fg], parts=parts, rows=rows, values={"A": [p_, 0], "area": A, "volume": V}, diff="7-9",
                  cw="Show that", refs=["9C"]), variant="xaxis")


# =============================================================== 9C kinematics


def _kin(r):
    t1, t2 = sorted(r.sample(range(1, 7), 2))
    k = r.choice([1, 2, 3])
    v = sp.expand(k * (t - t1) * (t - t2))
    return v, t1, t2, k


@tpl("calc.kinematics", "applied", 22)
def ck_applied(r):
    v, t1, t2, k = _kin(r)
    T = t2 + r.randint(1, 3)
    s = sp.integrate(v, t)
    dist = sp.integrate(v, (t, 0, t1)) - sp.integrate(v, (t, t1, t2)) + sp.integrate(v, (t, t2, T))
    disp = sp.integrate(v, (t, 0, T))
    ta = r.randint(0, T)
    acc = sp.diff(v, t).subs(t, ta)
    intro = (f"A particle $P$ moves along a straight line. At time $t$ seconds, $t \\geqslant 0$, the velocity of $P$ is $v$ m/s, where $$v = {tex(v).replace('x', 't')}$$")
    parts = [P("a", f"Find the acceleration of $P$ when $t = {ta}$", 2),
             P("b", "Find the values of $t$ when $P$ is instantaneously at rest.", 2),
             P("c", f"Find the total distance travelled by $P$ in the interval $0 \\leqslant t \\leqslant {T}$", 5)]
    rows = [R("a", f"$a = \\dfrac{{\\mathrm{{d}}v}}{{\\mathrm{{d}}t}} = {tex(sp.diff(v, t))}$", "M1"), R("a", f"${acc}$ m/s$^2$", "A1"),
            R("b", f"${tex(v)} = 0$", "M1"), R("b", f"$t = {t1}$, $t = {t2}$", "A1"),
            R("c", f"$s = \\int v \\, \\mathrm{{d}}t = {tex(s)}$", "M1 A1"),
            R("c", f"Splits the interval at $t = {t1}$ and $t = {t2}$", "M1"),
            R("c", f"$|s({t1}) - s(0)| + |s({t2}) - s({t1})| + |s({T}) - s({t2})|$", "M1", "dM1"),
            R("c", f"${fr(dist)}$ m", "A1", f"the displacement ${fr(disp)}$ scores M1 A1 M0 M0 A0")]
    return dict(Q(intro=intro, parts=parts, rows=rows, values={"a": acc, "rest": [t1, t2], "distance": dist}, diff="7-9",
                  cw="Find", refs=["9C"]), variant="velocity")


@tpl("calc.kinematics", "multi-part", 22)
def ck_multi(r):
    a1, a0 = nz(r, -4, 4), r.randint(-8, 8)
    acc = a1 * t + a0
    u = r.randint(-5, 10)
    v = sp.integrate(acc, t) + u
    s0 = 0
    T = r.randint(2, 6)
    s = sp.integrate(v, (t, 0, t))
    sT = s.subs(t, T)
    nm = r.choice(["particle", "small ball", "bead"])
    intro = (f"A {nm} moves along a straight line. At time $t$ seconds the acceleration is $a$ m/s$^2$, where $a = {tex(acc).replace('x', 't')}$\n\n"
             f"When $t = 0$, the {nm} is at the point $O$ and is moving with velocity ${u}$ m/s.")
    parts = [P("a", "Find an expression for the velocity, $v$ m/s, at time $t$ seconds.", 3, prefix="v = "),
             P("b", f"Find the displacement of the {nm} from $O$ when $t = {T}$", 3)]
    rows = [R("a", "Integrates $a$ with respect to $t$", "M1"), R("a", f"$v = {tex(sp.integrate(acc, t))} + c$", "A1"),
            R("a", f"$v = {tex(v)}$", "A1", "uses $v = " + str(u) + "$ at $t = 0$"),
            R("b", "Integrates their $v$", "M1"), R("b", f"$s = {tex(s)}$", "A1", "constant is 0 as $s = 0$ at $t = 0$"),
            R("b", f"${fr(sT)}$ m", "A1")]
    vals = {"v": str(v), "s": sT}
    rts = [z for z in sp.solve(v, t) if z.is_real and z > 0]
    if rts:
        tr_ = min(rts)
        parts.append(P("c", f"Find the value of $t$ when the {nm} first comes to instantaneous rest, giving your answer to 3 significant figures where appropriate.", 2))
        rows += [R("c", f"${tex(v)} = 0$", "M1"), R("c", f"$t = {tex(tr_) if tr_.is_rational else sf(tr_)}$", "A1")]
        vals["rest"] = float(tr_)
    else:
        parts.append(P("c", f"Show that the {nm} is never at rest.", 2))
        rows += [R("c", f"${tex(v)} = 0$ has discriminant ${sp.discriminant(v, t)} < 0$", "M1"), R("c", "So $v \\neq 0$ for all $t$", "A1", "cso")]
        if sp.Poly(v, t).degree() < 2 or sp.discriminant(v, t) >= 0:
            return None
    return dict(Q(intro=intro, parts=parts, rows=rows, values=vals, diff="4-6", cw="Find", refs=["9C"]), variant="accel")


# =============================================================== 9D/9E stationary points


def _cubic(r):
    p_, q_ = sorted(r.sample(range(-4, 5), 2))
    a = r.choice([1, 2, -1, 2, -2])
    if (p_ + q_) % 2 and a % 2:
        a *= 2
    c = r.randint(-8, 8)
    e = sp.expand(sp.integrate(3 * a * (x - p_) * (x - q_), x) + c)
    return e, p_, q_, a


@tpl("calc.stationary", "short", 22)
def cs_short(r):
    e, p_, q_, a = _cubic(r)
    pts = [(xx, e.subs(x, xx)) for xx in (p_, q_)]
    d2 = d_(d_(e))
    nat = ["minimum" if d2.subs(x, xx) > 0 else "maximum" for xx in (p_, q_)]
    parts = [P("", f"Find the coordinates of the stationary points on the curve with equation $y = {tex(e)}$ and determine the nature of each.", 6)]
    rows = [R("", f"${DY} = {tex(d_(e))}$", "M1 A1"), R("", "Sets their derivative to 0 and solves", "M1"),
            R("", "; ".join(f"$({px}, {fr(py)})$" for px, py in pts), "A1"),
            R("", f"${D2Y} = {tex(d2)}$ or examines gradient either side", "M1"),
            R("", f"$({p_}, {fr(pts[0][1])})$ is a {nat[0]} and $({q_}, {fr(pts[1][1])})$ is a {nat[1]}", "A1")]
    return dict(Q(parts=parts, rows=rows, values={"points": [[px, py] for px, py in pts], "nature": nat}, diff="4-6", cw="Find",
                  refs=["9D", "9E"]), variant="cubic")


@tpl("calc.stationary", "multi-part", 22)
def cs_multi(r):
    e, p_, q_, a = _cubic(r)
    ys = sorted([e.subs(x, p_), e.subs(x, q_)])
    d2 = d_(d_(e))
    pts = [(xx, e.subs(x, xx)) for xx in (p_, q_)]
    nat = ["minimum" if d2.subs(x, xx) > 0 else "maximum" for xx in (p_, q_)]
    parts = [P("a", f"Find ${DY}$", 2),
             P("b", "Find the coordinates of the stationary points of $C$", 3),
             P("c", "Use the second derivative to determine the nature of each stationary point.", 2),
             P("d", "Determine every value of $k$ such that $" + tex(e) + " = k$ has exactly three different real solutions.", 2)]
    rows = [R("a", f"${tex(d_(e))}$", "M1 A1"), R("b", "Sets $= 0$ and solves", "M1"),
            R("b", f"$x = {p_}$ and $x = {q_}$", "A1"), R("b", "; ".join(f"$({px}, {fr(py)})$" for px, py in pts), "A1"),
            R("c", f"${D2Y} = {tex(d2)}$ evaluated at both points", "M1"),
            R("c", f"{nat[0]} at $x = {p_}$, {nat[1]} at $x = {q_}$", "A1"),
            R("d", "Uses the $y$-coordinates of the turning points as boundaries", "M1"),
            R("d", f"${fr(ys[0])} < k < {fr(ys[1])}$", "A1", "strict inequalities")]
    return dict(Q(intro=f"The curve $C$ has equation $y = {tex(e)}$", parts=parts, rows=rows,
                  values={"points": [[px, py] for px, py in pts], "k_range": ys}, diff="7-9", cw="Find", refs=["9D", "9E", "4B"]),
                variant="cubic")


@tpl("calc.stationary", "applied", 22)
def cs_applied(r):
    v = r.choice(["box", "cyl", "pen"])
    if v == "box":
        L_ = r.choice([12, 18, 24, 30, 36, 15, 20])
        V = sp.expand(x * (L_ - 2 * x) ** 2)
        xs = [z for z in sp.solve(d_(V), x) if 0 < z < sp.Rational(L_, 2)]
        x0 = xs[0]
        Vm = V.subs(x, x0)
        intro = f"A square sheet of card has sides of length {L_} cm. A square of side $x$ cm is cut from each corner and the sides are folded up to make an open box."
        parts = [P("a", f"Show that the volume, $V$ cm$^3$, of the box is given by $V = {tex(V)}$", 2),
                 P("b", "Using calculus, find the value of $x$ that makes $V$ as large as possible, and confirm that this gives a maximum.", 5),
                 P("c", "Find the maximum volume.", 1)]
        rows = [R("a", f"$V = x({L_} - 2x)^2$", "M1"), R("a", f"$= {tex(V)}$", "A1", "cso"),
                R("b", f"$\\dfrac{{\\mathrm{{d}}V}}{{\\mathrm{{d}}x}} = {tex(d_(V))}$", "M1 A1"),
                R("b", "Sets $= 0$ and solves", "M1"), R("b", f"$x = {fr(x0)}$ (reject $x = {fr(sp.Rational(L_, 2))}$)", "A1"),
                R("b", f"$\\dfrac{{\\mathrm{{d}}^2V}}{{\\mathrm{{d}}x^2}} = {tex(d_(d_(V)).subs(x, x0))} < 0$ so maximum", "B1"),
                R("c", f"${fr(Vm)}$ cm$^3$", "B1")]
        return dict(Q(intro=intro, parts=parts, rows=rows, values={"x": x0, "Vmax": Vm}, diff="7-9", cw="Show that", refs=["9D", "9E"]), variant=v)
    if v == "cyl":
        Vc = r.choice([250, 500, 1000, 400, 800, 600])
        A = 2 * sp.pi * x ** 2 + 2 * Vc / x
        x0 = sp.cbrt(sp.Rational(Vc) / (2 * sp.pi))
        Am = A.subs(x, x0)
        intro = f"A closed cylindrical can has radius $r$ cm and height $h$ cm. The volume of the can is {Vc} cm$^3$"
        parts = [P("a", f"Show that the total surface area, $A$ cm$^2$, of the can is given by $A = 2\\pi r^2 + \\dfrac{{{2 * Vc}}}{{r}}$", 3),
                 P("b", "Using calculus, find the value of $r$ that makes $A$ as small as possible. Give $r$ to 3 significant figures.", 4),
                 P("c", "Justify that this value of $r$ gives a minimum.", 2),
                 P("d", "Find the minimum surface area, to 3 significant figures.", 1)]
        rows = [R("a", f"$\\pi r^2 h = {Vc}$", "B1"), R("a", "$A = 2\\pi r^2 + 2\\pi r h$ and substitutes for $h$", "M1"),
                R("a", "Given answer", "A1", "cso"),
                R("b", f"$\\dfrac{{\\mathrm{{d}}A}}{{\\mathrm{{d}}r}} = 4\\pi r - \\dfrac{{{2 * Vc}}}{{r^2}}$", "M1 A1"),
                R("b", f"$r^3 = \\dfrac{{{Vc}}}{{2\\pi}}$", "M1"), R("b", f"$r = {sf(x0)}$", "A1"),
                R("c", f"$\\dfrac{{\\mathrm{{d}}^2A}}{{\\mathrm{{d}}r^2}} = 4\\pi + \\dfrac{{{4 * Vc}}}{{r^3}}$", "M1"),
                R("c", "$> 0$ for $r > 0$ so minimum", "A1"),
                R("d", f"${sf(Am)}$ cm$^2$", "B1")]
        return dict(Q(intro=intro, parts=parts, rows=rows, values={"r": float(x0), "Amin": float(Am)}, diff="7-9", cw="Show that",
                      refs=["9D", "9E"]), variant=v)
    Lw = r.choice([60, 80, 100, 120, 150, 200])
    nm = name_ctx(r)
    # rectangle against a wall: 2x + y = Lw, area = x y
    Ar = sp.expand(x * (Lw - 2 * x))
    x0 = sp.Rational(Lw, 4)
    intro = f"{nm} uses {Lw} m of fencing to make three sides of a rectangular pen. The fourth side of the pen is a straight wall. The two sides of the pen perpendicular to the wall each have length $x$ m."
    parts = [P("a", f"Show that the area, $A$ m$^2$, of the pen is given by $A = {tex(Ar)}$", 2),
             P("b", "Using calculus, find the largest possible area of the pen, and confirm that your value is a maximum.", 4)]
    rows = [R("a", f"Side parallel to the wall $= {Lw} - 2x$", "M1"), R("a", f"$A = {tex(Ar)}$", "A1", "cso"),
            R("b", f"$\\dfrac{{\\mathrm{{d}}A}}{{\\mathrm{{d}}x}} = {tex(d_(Ar))} = 0$", "M1"), R("b", f"$x = {fr(x0)}$", "A1"),
            R("b", "$\\dfrac{\\mathrm{d}^2A}{\\mathrm{d}x^2} = -4 < 0$ so maximum", "B1"), R("b", f"$A = {fr(Ar.subs(x, x0))}$ m$^2$", "A1")]
    return dict(Q(intro=intro, parts=parts, rows=rows, values={"x": x0, "Amax": Ar.subs(x, x0)}, diff="4-6", cw="Show that",
                  refs=["9D", "9E"]), variant=v)


# =============================================================== 9F tangents and normals


def _tan_curve(r):
    e, ps = _powers(r, 2, neg=True)
    e = e + r.randint(-6, 6)
    x0 = r.choice([1, 4]) if any(sp.Rational(p_).q == 2 for p_ in ps) else r.choice([1, 2, -1, -2])
    if any(sp.Rational(p_).q == 2 for p_ in ps) and x0 < 0:
        return None
    y0, g = e.subs(x, x0), d_(e).subs(x, x0)
    if not (y0.is_rational and g.is_rational) or g == 0:
        return None
    return e, x0, y0, g


@tpl("calc.tangents", "short", 22)
def ct_short(r):
    got = _tan_curve(r)
    if not got:
        return None
    e, x0, y0, g = got
    v = r.choice(["tangent", "normal"])
    m = g if v == "tangent" else -1 / g
    ln = sp.expand(m * (x - x0) + y0)
    parts = [P("", f"The point $P$ with $x$-coordinate ${x0}$ lies on the curve with equation $y = {tex(e)}$\n\nFind an equation of the {v} to the curve at $P$, giving your answer in the form $y = mx + c$", 5)]
    rows = [R("", f"$y = {fr(y0)}$ at $P$", "B1"), R("", f"${DY} = {tex(d_(e))}$", "M1"),
            R("", f"Gradient {'of tangent' if v == 'tangent' else 'of normal'} $= {fr(m)}$", "A1" if v == "tangent" else "M1", None if v == "tangent" else "uses $-1/m$"),
            R("", f"$y - ({fr(y0)}) = {fr(m)}(x - ({x0}))$", "M1"), R("", f"$y = {tex(ln)}$", "A1")]
    return dict(Q(parts=parts, rows=rows, values={"line": str(ln)}, diff="4-6", cw="Find", refs=["9F"]), variant=v)


@tpl("calc.tangents", "multi-part", 22)
def ct_multi(r):
    got = _tan_curve(r)
    if not got:
        return None
    e, x0, y0, g = got
    tan = sp.expand(g * (x - x0) + y0)
    nor = sp.expand(-1 / g * (x - x0) + y0)
    xt, xn = sp.solve(tan, x)[0], sp.solve(nor, x)[0]
    ar = sp.Rational(abs(xt - xn) * abs(y0), 2)
    if ar == 0 or ar.q > 40:
        return None
    intro = f"The curve $C$ has equation $y = {tex(e)}$. The point $P$ on $C$ has $x$-coordinate ${x0}$"
    parts = [P("a", "Find an equation of the tangent to $C$ at $P$", 4),
             P("b", "Find an equation of the normal to $C$ at $P$", 2),
             P("c", "The tangent meets the $x$-axis at $A$ and the normal meets the $x$-axis at $B$. Find the area of triangle $APB$", 4)]
    rows = [R("a", f"${DY} = {tex(d_(e))}$", "M1"), R("a", f"Gradient ${fr(g)}$ and $y = {fr(y0)}$", "A1"),
            R("a", "Straight-line equation with their gradient through $P$", "M1"), R("a", f"$y = {tex(tan)}$", "A1"),
            R("b", f"Gradient $= {fr(-1 / g)}$", "M1"), R("b", f"$y = {tex(nor)}$", "A1"),
            R("c", f"$A = ({fr(xt)}, 0)$", "B1"), R("c", f"$B = ({fr(xn)}, 0)$", "B1"),
            R("c", "$\\dfrac{1}{2} \\times AB \\times |y_P|$", "M1"), R("c", f"${fr(ar)}$", "A1")]
    return dict(Q(intro=intro, parts=parts, rows=rows, values={"tangent": str(tan), "normal": str(nor), "area": ar}, diff="7-9",
                  cw="Find", refs=["9F", "8C", "8D"]), variant="area")


# =============================================================== 9G rates


@tpl("calc.rates", "applied", 22)
def crr_applied(r):
    v = r.choice(["sphere", "cone", "cube", "circle"])
    K = r.choice([2, 3, 5, 8, 10, 12, 20, 50])
    if v == "sphere":
        R0 = r.randint(2, 12)
        ans = sp.Rational(K) / (4 * sp.pi * R0 ** 2)
        intro = f"A spherical balloon is being inflated. Its volume is increasing at a constant rate of {K} cm$^3$ per second."
        parts = [P("", f"Find the rate at which the radius of the balloon is increasing at the instant when the radius is {R0} cm. Give your answer to 3 significant figures.", 4)]
        rows = [R("", "$\\dfrac{\\mathrm{d}V}{\\mathrm{d}r} = 4\\pi r^2$", "B1"),
                R("", "$\\dfrac{\\mathrm{d}r}{\\mathrm{d}t} = \\dfrac{\\mathrm{d}V}{\\mathrm{d}t} \\div \\dfrac{\\mathrm{d}V}{\\mathrm{d}r}$", "M1"),
                R("", f"$\\dfrac{{{K}}}{{4\\pi \\times {R0}^2}}$", "M1"), R("", f"${sf(ans)}$ cm/s", "A1", "awrt")]
        return dict(Q(intro=intro, parts=parts, rows=rows, values={"drdt": float(ans)}, diff="4-6", cw="Find", refs=["9G"]), variant=v)
    if v == "cone":
        c = r.choice([sp.Rational(1, 2), sp.Rational(1, 3), sp.Rational(2, 3), 1, sp.Rational(3, 4)])
        H = r.randint(3, 15)
        ans = sp.Rational(K) / (sp.pi * c ** 2 * H ** 2)
        intro = (f"Water is poured into an empty container in the shape of an inverted right circular cone at a rate of {K} cm$^3$/s. "
                 f"When the depth of water is $h$ cm, the radius of the water surface is ${tex(c * sp.Symbol('h'))}$ cm.")
        parts = [P("a", f"Show that the volume of water, $V$ cm$^3$, is given by $V = {tex(sp.pi * c ** 2 / 3 * sp.Symbol('h') ** 3)}$", 1),
                 P("b", f"Find the rate at which the depth of water is increasing when $h = {H}$, giving your answer to 3 significant figures.", 4)]
        rows = [R("a", f"$V = \\dfrac{{1}}{{3}}\\pi ({tex(c * sp.Symbol('h'))})^2 h$ leading to the given answer", "B1", "cso"),
                R("b", f"$\\dfrac{{\\mathrm{{d}}V}}{{\\mathrm{{d}}h}} = {tex(sp.pi * c ** 2 * sp.Symbol('h') ** 2)}$", "B1"),
                R("b", "Chain rule: $\\dfrac{\\mathrm{d}h}{\\mathrm{d}t} = \\dfrac{\\mathrm{d}V}{\\mathrm{d}t} \\div \\dfrac{\\mathrm{d}V}{\\mathrm{d}h}$", "M1"),
                R("b", f"Substitutes $h = {H}$", "M1", "dM1"), R("b", f"${sf(ans)}$ cm/s", "A1")]
        return dict(Q(intro=intro, parts=parts, rows=rows, values={"dhdt": float(ans)}, diff="7-9", cw="Find", refs=["9G"]), variant=v)
    if v == "cube":
        k = r.choice([sp.Rational(1, 10), sp.Rational(1, 5), sp.Rational(1, 2), 2, sp.Rational(3, 10)])
        A0 = r.choice([24, 54, 96, 150, 216, 294, 384])
        s0 = sp.sqrt(sp.Rational(A0, 6))
        dV = 3 * s0 ** 2 * k
        intro = f"The length of each edge of a cube is increasing at a rate of {fmtk(k)} cm/s."
        parts = [P("", f"Find the rate of increase of the volume of the cube at the instant when its total surface area is {A0} cm$^2$", 4)]
        rows = [R("", f"$6x^2 = {A0}$ so $x = {tex(s0)}$", "B1"), R("", "$\\dfrac{\\mathrm{d}V}{\\mathrm{d}x} = 3x^2$", "B1"),
                R("", f"$\\dfrac{{\\mathrm{{d}}V}}{{\\mathrm{{d}}t}} = 3x^2 \\times {fmtk(k)}$", "M1"), R("", f"${fmtk(dV)}$ cm$^3$/s", "A1")]
        return dict(Q(intro=intro, parts=parts, rows=rows, values={"dVdt": dV}, diff="4-6", cw="Find", refs=["9G"]), variant=v)
    R0 = r.randint(3, 20)
    ans = sp.Rational(K) / (2 * sp.pi * R0)
    intro = f"Oil spills onto a flat surface and spreads out as a circle. The area of the circle increases at a constant rate of {K} cm$^2$/s."
    parts = [P("", f"Find the rate of increase of the radius when the radius is {R0} cm, giving your answer to 3 significant figures.", 4)]
    rows = [R("", "$\\dfrac{\\mathrm{d}A}{\\mathrm{d}r} = 2\\pi r$", "B1"), R("", "Chain rule", "M1"),
            R("", f"$\\dfrac{{{K}}}{{2\\pi \\times {R0}}}$", "M1"), R("", f"${sf(ans)}$ cm/s", "A1")]
    return dict(Q(intro=intro, parts=parts, rows=rows, values={"drdt": float(ans)}, diff="4-6", cw="Find", refs=["9G"]), variant=v)


def fmtk(v):
    v = sp.Rational(v)
    return str(v.p) if v.q == 1 else dp(v, 2 if v.q in (5, 10, 2, 4, 20, 50) else 4).rstrip("0").rstrip(".")


@tpl("calc.rates", "short", 22)
def crr_short(r):
    v = r.choice(["small", "chain"])
    if v == "small":
        e, ps = _powers(r, 2, neg=True)
        x0 = r.choice([1, 4]) if any(sp.Rational(p_).q == 2 for p_ in ps) else r.choice([1, 2, 3])
        h = r.choice([sp.Rational(1, 100), sp.Rational(1, 50), sp.Rational(1, 10), sp.Rational(1, 20)])
        g = d_(e).subs(x, x0)
        if not g.is_rational or g == 0:
            return None
        parts = [P("", f"Given that $y = {tex(e)}$, use calculus to find the approximate change in $y$ when $x$ increases from ${x0}$ to ${fmtk(x0 + h)}$", 3)]
        rows = [R("", f"${DY} = {tex(d_(e))}$", "M1"), R("", f"$\\delta y \\approx {DY} \\times \\delta x = {fr(g)} \\times {fmtk(h)}$", "M1"),
                R("", f"${fmtk(g * h)}$", "A1", "a decrease if negative")]
        return dict(Q(parts=parts, rows=rows, values={"dy": g * h}, diff="4-6", cw="Find", refs=["9G"]), variant=v)
    e, ps = _powers(r, 2, neg=False)
    x0 = r.choice([1, 4]) if any(sp.Rational(p_).q == 2 for p_ in ps) else r.choice([1, 2, 3])
    K = r.choice([2, 3, sp.Rational(1, 2), 5, sp.Rational(1, 4)])
    g = d_(e).subs(x, x0)
    if not g.is_rational:
        return None
    parts = [P("", f"The variables $x$ and $y$ are connected by $y = {tex(e)}$. The variable $x$ is increasing at a rate of {fmtk(K)} units per second.\n\nFind the rate of change of $y$ when $x = {x0}$", 3)]
    rows = [R("", f"${DY} = {tex(d_(e))}$", "M1"), R("", "$\\dfrac{\\mathrm{d}y}{\\mathrm{d}t} = \\dfrac{\\mathrm{d}y}{\\mathrm{d}x} \\times \\dfrac{\\mathrm{d}x}{\\mathrm{d}t}$", "M1"),
            R("", f"${fmtk(g * K)}$ units per second", "A1")]
    return dict(Q(parts=parts, rows=rows, values={"dydt": g * K}, diff="4-6", cw="Find", refs=["9G"]), variant=v)
