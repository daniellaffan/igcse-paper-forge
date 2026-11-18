"""4PM1 templates: 1 logs/indices/surds, 2 quadratics, 3 identities & inequalities, 4 graphs."""
import math
from fractions import Fraction as F

import sympy as sp

from further_maths_util import (tpl, P, R, Q, tex, sf, dp, fr, sg, poly, lin, nz, pick, fig, table, Axes,
                                grid_paper, x, y, k, name_ctx, lin2, kq, logx, xpow)

# =============================================================== 1A graphs of a^x, log x


@tpl("logs.graphs", "graph", 21)
def lg_sketch(r):
    v = r.choice(["exp", "exp", "log"])
    if v == "exp":
        a = r.choice([2, 3, 4, 5])
        c = nz(r, -6, 5)
        neg = r.random() < 0.35
        ex = f"{a}^{{-x}}" if neg else f"{a}^{{x}}"
        f = (lambda X: a ** (-X) + c) if neg else (lambda X: a ** X + c)
        yint = 1 + c
        parts_a = (f"On the axes, sketch the curve with equation $y = {ex}{sg(c)}$\n\n"
                   "Show clearly the coordinates of any points where the curve crosses the coordinate axes "
                   "and state the equation of the asymptote to the curve.")
        rows = [R("a", "Correct shape: " + ("decreasing" if neg else "increasing") + " exponential curve lying entirely above its asymptote", "B1"),
                R("a", f"Crosses the $y$-axis at $(0, {yint})$", "B1"),
                R("a", f"Asymptote $y = {c}$ stated or drawn and labelled", "B1")]
        marks_a = 3
        vals = {"y_intercept": yint, "asymptote": f"y = {c}"}
        if c < 0:
            xi = sp.log(-c, a) * (-1 if neg else 1)
            xi = sp.nsimplify(xi)
            rows.insert(2, R("a", f"Crosses the $x$-axis at $({sf(float(xi))}, 0)$ (accept exact form $x = {'-' if neg else ''}\\log_{{{a}}} {-c}$)", "B1", "awrt 3 s.f."))
            marks_a = 4
            vals["x_intercept"] = float(xi)
        # (b) line and number of solutions
        m = nz(r, -3, 3)
        d = r.randint(-3, 6)
        g = sp.lambdify(x, (a ** (-x) if neg else a ** x) + c - (m * x + d))
        xs = [i / 200 for i in range(-4000, 4001)]
        cnt = sum(1 for i in range(len(xs) - 1) if g(xs[i]) * g(xs[i + 1]) < 0)
        if cnt == 0 and r.random() < 0.6:
            return None
        sol_word = {0: "no real solutions", 1: "exactly one real solution", 2: "two real solutions"}[cnt]
        parts = [P("a", parts_a, marks_a, space="box"),
                 P("b", f"By drawing a suitable straight line on your sketch, state the number of real solutions of the equation\n\n$${ex}{sg(c)} = {lin(m, d)}$$\n\nGive a reason for your answer.", 2, space="lines", lines=3)]
        rows += [R("b", f"Line $y = {lin(m, d)}$ drawn with correct gradient sign and $y$-intercept", "B1"),
                 R("b", f"{cnt} ({sol_word}) with reason: the line and curve meet {cnt} time{'s' if cnt != 1 else ''}", "B1", "dep on a correct line")]
        vals["solutions"] = cnt
        return dict(Q(parts=parts, rows=rows, values=vals, diff=pick(r, "4-6", "4-6", "1-3"), cw="Sketch",
                      refs=["1A"]), variant="exp")
    b = r.choice([2, 3, 5, 10])
    h = r.choice([-3, -2, -1, 1, 2, 3, 4])
    c = r.choice([0, 0, 1, 2, -1])
    lab = f"\\log_{{{b}}}(x {'+' if h > 0 else '-'} {abs(h)})" + (sg(c) if c else "")
    rows = [R("a", "Correct shape: increasing logarithmic curve to the right of its asymptote", "B1"),
            R("a", f"Asymptote $x = {-h}$", "B1")]
    xi = sp.Rational(b) ** (-c) - h
    if xi == 0:
        return None
    rows.append(R("a", f"Crosses the $x$-axis at $({fr(xi)}, 0)$", "B1"))
    vals = {"asymptote": f"x = {-h}", "x_intercept": str(xi)}
    marks = 3
    if h > 0:
        yi = math.log(h, b) + c
        rows.append(R("a", f"Crosses the $y$-axis at $(0, {sf(yi)})$ (accept $\\log_{{{b}}} {h}{sg(c) if c else ''}$)", "B1"))
        vals["y_intercept"] = yi
        marks = 4
    kk = r.randint(2, 4) + c
    xk = sp.Rational(b) ** (kk - c) - h
    parts = [P("a", f"Sketch the curve with equation $y = {lab}$\n\nOn your sketch show the equation of the asymptote and the coordinates of any points where the curve meets the coordinate axes.", marks, space="box"),
             P("b", f"Find the exact value of $x$ for which $y = {kk}$", 2, prefix="x = ")]
    rows += [R("b", f"${b}^{{{kk - c}}} = x {'+' if h > 0 else '-'} {abs(h)}$", "M1", "removes the log correctly"),
             R("b", f"$x = {xk}$", "A1", "cao")]
    vals["x_at_k"] = int(xk)
    return dict(Q(parts=parts, rows=rows, values=vals, diff="4-6", cw="Sketch", refs=["1A"]), variant="log")


@tpl("logs.graphs", "graph", 12)
def lg_table(r):
    a = r.choice([2, 3])
    s = r.choice([F(1, 2), F(1), F(1, 3)]) if a == 3 else r.choice([F(1, 2), F(1)])
    c = nz(r, -4, 2)
    ex = f"{a}^{{{'x' if s == 1 else fr(s) + 'x'}}}"
    f = lambda X: a ** (float(s) * X) + c
    xs = [-2, -1, 0, 1, 2, 3, 4] if s < 1 else [-2, -1, -0.5, 0, 0.5, 1, 1.5, 2]
    yv = [round(f(X), 2) for X in xs]
    hide = sorted(r.sample(range(len(xs)), 3))
    rowvals = [("" if i in hide else dp(v, 2)) for i, v in enumerate(yv)]
    ymin = math.floor(min(yv)) - 1
    ymax = math.ceil(max(yv)) + 1
    ystep = 1 if ymax - ymin <= 12 else 2
    kk = round(r.uniform(min(yv) + 0.5, max(yv) - 0.5), 1)
    if abs(kk - c) < 0.3 or kk <= c:
        return None
    root = math.log(kk - c, a) / float(s)
    parts = [P("a", f"Complete the table of values for $y = {ex}{sg(c)}$, giving your values to 2 decimal places.", 2,
               space="table"),
             P("b", "On the grid, plot the points from your completed table and join them to form a smooth curve.", 2,
               space="graph", figs=[fig(grid_paper((xs[0], xs[-1]), (ymin, ymax), 1 if s < 1 else 0.5, ystep), 120, note=None)]),
             P("c", f"Use your graph to estimate, to 1 decimal place, the solution of the equation ${ex} = {dp(kk - c, 1)}$", 2, prefix="x = ")]
    rows = [R("a", ", ".join(f"$x = {X}$: ${dp(yv[i], 2)}$" for i, X in enumerate(xs) if i in hide), "B2",
              "B1 for two correct values"),
            R("b", "All points plotted correctly (within half a small square)", "B1", "ft their table"),
            R("b", "Smooth curve through all points", "B1"),
            R("c", f"Line $y = {dp(kk, 1)}$ drawn, or reading taken at $y = {dp(kk, 1)}$", "M1"),
            R("c", f"$x = {dp(root, 1)}$", "A1", f"accept answers in the range {dp(root - 0.1, 1)} to {dp(root + 0.1, 1)}")]
    figs = [table(["$x$"] + [str(X) for X in xs], [["$y$"] + rowvals])]
    return dict(Q(parts=parts, rows=rows, values={"table": yv, "root": root}, diff="4-6", cw="Complete",
                  refs=["1A"], figs=figs), variant="table")


@tpl("logs.graphs", "short", 11)
def lg_short_points(r):
    v = r.choice(["exp", "exp2"])
    p = nz(r, 2, 9)
    a = r.choice([2, 3, 4, 5, F(1, 2), F(1, 3)])
    x1, x2 = sorted(r.sample([-1, 1, 2, 3, 4], 2))
    y1, y2 = F(p) * F(a) ** x1, F(p) * F(a) ** x2
    if v == "exp":
        parts = [P("a", f"The curve with equation $y = pa^x$, where $p$ and $a$ are positive constants, passes through the points $({x1}, {fr(y1)})$ and $({x2}, {fr(y2)})$\n\nFind the value of $p$ and the value of $a$", 4),
                 P("b", f"Find, to 3 significant figures, the value of $x$ for which $y = {p * 7}$", 2, prefix="x = ")]
    else:
        parts = [P("a", f"A curve has equation $y = pa^x$, where $p > 0$ and $a > 0$\n\nWhen $x = {x1}$, $y = {fr(y1)}$ and when $x = {x2}$, $y = {fr(y2)}$\n\nFind the value of $p$ and the value of $a$", 4),
                 P("b", f"Hence find, to 3 significant figures, the value of $x$ when $y = {p * 7}$", 2, prefix="x = ")]
    xv = math.log(7, float(a))
    pax = lambda e_: "p" if e_ == 0 else "p" + xpow(e_, "a")
    rows = [R("a", f"${pax(x1)} = {fr(y1)}$ and ${pax(x2)} = {fr(y2)}$", "M1", "both equations formed"),
            R("a", f"${xpow(x2 - x1, 'a')} = {fr(y2 / y1)}$", "M1", "divides to eliminate $p$"),
            R("a", f"$a = {fr(a)}$", "A1"),
            R("a", f"$p = {p}$", "A1"),
            R("b", f"$x = \\dfrac{{\\log 7}}{{\\log {fr(a)}}}$", "M1", "takes logs of $a^x = 7$ correctly, ft their $a$"),
            R("b", f"$x = {sf(xv)}$", "A1", "awrt")]
    return dict(Q(parts=parts, rows=rows, values={"p": p, "a": a, "x": xv}, diff="4-6", cw="Find", refs=["1A", "1B"]),
                variant=v)


@tpl("logs.graphs", "short", 11)
def lg_short_meet(r):
    b = r.choice([2, 3, 5])
    p, q = r.sample([1, 2, 3], 2)
    c1, c2 = nz(r, -4, 4), nz(r, -4, 4)
    m1, m2 = r.randint(1, 3), r.randint(1, 3)
    # b^p^(m1 x + c1) = b^q^(m2 x + c2) -> p(m1x+c1) = q(m2x+c2)
    if p * m1 == q * m2:
        return None
    xs = sp.Rational(q * c2 - p * c1, p * m1 - q * m2)
    if abs(p * (m1 * xs + c1)) > 10:
        return None
    yv = sp.Rational(b) ** (p * (m1 * xs + c1))
    A, B = b ** p, b ** q
    parts = [P("", f"The curves with equations $y = {A}^{{{lin(m1, c1)}}}$ and $y = {B}^{{{lin(m2, c2)}}}$ meet at the point $P$\n\nFind the exact coordinates of $P$", 4)]
    rows = [R("", f"Writes both in base ${b}$: ${b}^{{{p}({lin(m1, c1)})}} = {b}^{{{q}({lin(m2, c2)})}}$", "M1", "or takes logs of both sides"),
            R("", f"${tex(sp.expand(p * (m1 * x + c1)))} = {tex(sp.expand(q * (m2 * x + c2)))}$", "M1", "equates indices"),
            R("", f"$x = {fr(xs)}$", "A1"),
            R("", f"$y = {tex(yv)}$", "A1", "exact value only")]
    return dict(Q(parts=parts, rows=rows, values={"x": xs, "y": yv}, diff="4-6", cw="Find", refs=["1A", "1B"]),
                variant="meet")


# =============================================================== 1B laws of logs


@tpl("logs.laws", "short", 22)
def ll_solve(r):
    v = r.choice(["lin", "both", "quad", "logeq", "base"])
    if v == "lin":
        p = r.choice([2, 3, 5, 6, 7])
        m, c = r.randint(2, 4), nz(r, -3, 3)
        qv = r.choice([20, 45, 80, 150, 200, 500, 1000])
        xv = (math.log(qv) / math.log(p) - c) / m
        parts = [P("", f"Solve the equation $${p}^{{{lin(m, c)}}} = {qv}$$\n\nGive your answer to 3 significant figures.", 3, prefix="x = ")]
        rows = [R("", f"$({lin(m, c)})\\log {p} = \\log {qv}$", "M1", "takes logs of both sides correctly"),
                R("", f"$x = \\dfrac{{1}}{{{m}}}\\left(\\dfrac{{\\log {qv}}}{{\\log {p}}}{sg(-c)}\\right)$", "M1", "rearranges for $x$"),
                R("", f"$x = {sf(xv)}$", "A1", "awrt")]
        return dict(Q(parts=parts, rows=rows, values={"x": xv}, diff="4-6", cw="Solve", refs=["1B"]), variant=v)
    if v == "both":
        p, q = r.sample([2, 3, 5, 7], 2)
        c1, c2 = nz(r, -2, 3), nz(r, -2, 3)
        # p^(x+c1) = q^(2x+c2)? keep x coefficient 1 and 2 options
        m2 = r.choice([1, 2])
        lp, lq = math.log(p), math.log(q)
        if abs(lp - m2 * lq) < 0.05:
            return None
        xv = (c2 * lq - c1 * lp) / (lp - m2 * lq)
        parts = [P("", f"Solve $${p}^{{{lin(1, c1)}}} = {q}^{{{lin(m2, c2)}}}$$\n\nGive your answer to 3 significant figures.", 4, prefix="x = ")]
        rhs = f"{c2}\\log {q} {'-' if c1 > 0 else '+'} {abs(c1)}\\log {p}".replace("1\\log", "\\log").replace("-1\\log", "-\\log")
        rows = [R("", f"$({lin(1, c1)})\\log {p} = ({lin(m2, c2)})\\log {q}$", "M1"),
                R("", f"$x(\\log {p} - {m2 if m2 > 1 else ''}\\log {q}) = {rhs}$", "M1", "collects terms in $x$"),
                R("", f"$x = \\dfrac{{{rhs}}}{{\\log {p} - {m2 if m2 > 1 else ''}\\log {q}}}$", "M1", "dM1 – dependent on both previous M marks"),
                R("", f"$x = {sf(xv)}$", "A1", "awrt")]
        return dict(Q(parts=parts, rows=rows, values={"x": xv}, diff="7-9", cw="Solve", refs=["1B"]), variant=v)
    if v == "quad":
        a = r.choice([2, 3, 5])
        u1 = a ** r.randint(1, 3)
        u2 = r.choice([z for z in range(2, 13) if z not in (a, a * a, a ** 3)])
        s, pr = u1 + u2, u1 * u2
        parts = [P("", f"Solve the equation $${a}^{{2x}} - {s}({a}^{{x}}) + {pr} = 0$$\n\nGive your answers to 3 significant figures where appropriate.", 5)]
        x1, x2 = round(math.log(u1, a)), math.log(u2, a)
        rows = [R("", f"Let $u = {a}^x$: $u^2 - {s}u + {pr} = 0$", "M1", "recognises the quadratic in $u$"),
                R("", f"$(u - {u1})(u - {u2}) = 0 \\Rightarrow u = {u1}$ or $u = {u2}$", "M1 A1", "M1 solves 3-term quadratic"),
                R("", f"$x = {x1}$ and $x = {sf(x2)}$", "M1 A1", f"M1 takes logs of ${a}^x = {u2}$; A1 both values")]
        return dict(Q(parts=parts, rows=rows, values={"x": [x1, x2]}, diff="7-9", cw="Solve", refs=["1B"]), variant=v)
    if v == "logeq":
        b = r.choice([2, 3, 6])
        kk = r.choice([1, 2, 3]) if b != 6 else r.choice([1, 2])
        T_ = b ** kk
        # (x+p)(x+q) = T with integer roots, one valid
        x1 = r.randint(1, 12)
        p = r.randint(-x1 + 1, 6)
        qn = sp.Rational(T_, x1 + p) - x1
        if qn.q != 1 or x1 + qn <= 0 or p == qn:
            return None
        qn = int(qn)
        sols = sp.solve((x + p) * (x + qn) - T_, x)
        valid = [s_ for s_ in sols if s_ + p > 0 and s_ + qn > 0]
        bad = [s_ for s_ in sols if s_ not in valid]
        if len(valid) != 1 or not bad:
            return None
        parts = [P("", f"Solve the equation $$\\log_{{{b}}}(x {'+' if p >= 0 else '-'} {abs(p)}) + \\log_{{{b}}}(x {'+' if qn >= 0 else '-'} {abs(qn)}) = {kk}$$", 5, prefix="x = ")]
        rows = [R("", f"$\\log_{{{b}}}[(x {sg(p)[1:]})(x {sg(qn)[1:]})] = {kk}$", "M1", "uses the addition law"),
                R("", f"$(x {sg(p)[1:]})(x {sg(qn)[1:]}) = {T_}$", "M1", "removes logs correctly"),
                R("", f"${tex(sp.expand((x + p) * (x + qn) - T_))} = 0$", "A1"),
                R("", f"$x = {valid[0]}$", "M1 A1", f"M1 solves their quadratic; A1 must reject $x = {bad[0]}$ with a reason or by omission")]
        return dict(Q(parts=parts, rows=rows, values={"x": valid[0], "rejected": bad[0]}, diff="4-6", cw="Solve",
                      refs=["1B"]), variant=v)
    b = r.choice([2, 3, 4, 5])
    m = r.choice([2, 3, 4, 6, 8])
    # log_b x - m log_x b = c  -> u^2 - c u - m = 0 integer roots
    roots = [(u1, -m // u1) for u1 in range(1, m + 1) if m % u1 == 0]
    u1, u2 = r.choice(roots)
    if r.random() < 0.5:
        u1, u2 = -u2, -u1
    c = u1 + u2
    if c == 0:
        return None
    pr = -u1 * u2
    xs = [sp.Rational(b) ** u1, sp.Rational(b) ** u2]
    parts = [P("", f"Using the substitution $u = \\log_{{{b}}} x$, or otherwise, solve $$\\log_{{{b}}} x - {pr}\\log_{{x}} {b} = {c}$$", 5)]
    rows = [R("", f"$\\log_x {b} = \\dfrac{{1}}{{\\log_{{{b}}} x}}$", "B1", "change of base"),
            R("", f"$u^2 {sg(-c)}u - {pr} = 0$", "M1", "forms a 3-term quadratic in $u$"),
            R("", f"$u = {u1}$ or $u = {u2}$", "A1"),
            R("", f"$x = {tex(xs[0])}$, $x = {tex(xs[1])}$", "M1 A1", "M1 uses $x = " + str(b) + "^u$")]
    return dict(Q(parts=parts, rows=rows, values={"x": xs}, diff="7-9", cw="Solve", refs=["1B"]), variant=v)


@tpl("logs.laws", "show-that", 22)
def ll_show(r):
    v = r.choice(["base", "linear", "pq"])
    if v == "base":
        b = r.choice([2, 3, 5])
        kk = r.choice([2, 3])
        L_ = r.choice([2, 3, 4, 6, 8, 9, 12])
        m = sp.Rational(L_ * (kk + 1), kk)
        if m.q != 1:
            return None
        parts = [P("a", f"Show that $\\log_{{{b ** kk}}} x = \\dfrac{{1}}{{{kk}}}\\log_{{{b}}} x$", 2, space="working"),
                 P("b", f"Hence solve the equation $\\log_{{{b}}} x + \\log_{{{b ** kk}}} x = {m}$", 3, prefix="x = ")]
        rows = [R("a", f"$\\log_{{{b ** kk}}} x = \\dfrac{{\\log_{{{b}}} x}}{{\\log_{{{b}}} {b ** kk}}}$", "M1", "change of base"),
                R("a", f"$\\log_{{{b}}} {b ** kk} = {kk}$ so $\\log_{{{b ** kk}}} x = \\dfrac{{1}}{{{kk}}}\\log_{{{b}}} x$", "A1", "cso"),
                R("b", f"$\\dfrac{{{kk + 1}}}{{{kk}}}\\log_{{{b}}} x = {m}$", "M1"),
                R("b", f"$\\log_{{{b}}} x = {L_}$", "A1"),
                R("b", f"$x = {b ** L_ if b ** L_ < 10 ** 6 else str(b) + '^{' + str(L_) + '}'}$", "A1", "cao; accept equivalent exact form")]
        return dict(Q(parts=parts, rows=rows, values={"x": b ** L_}, diff="4-6", cw="Show that", refs=["1B"]), variant=v)
    if v == "linear":
        a = r.choice([2, 3, 5])
        kk = r.choice([1, 2])
        A2 = a ** kk
        p = r.randint(1, 9)
        q = r.randint(1, 6)
        xv = sp.Rational(A2 * q + p, A2 - 1)
        parts = [P("a", f"Show that the equation $$\\log_{{{a}}}(x + {p}) = {kk} + \\log_{{{a}}}(x - {q})$$ has solution $x = {fr(xv)}$", 4),
                 P("b", f"Hence find the exact value of $\\log_{{{a}}}(x + {p}) - \\log_{{{a}}}{fr(xv + p)}$", 1)]
        rows = [R("a", f"$\\log_{{{a}}}\\dfrac{{x + {p}}}{{x - {q}}} = {kk}$", "M1", "uses the subtraction law"),
                R("a", f"$x + {p} = {A2}(x - {q})$", "M1", "removes logs"),
                R("a", f"${A2 - 1}x = {A2 * q + p}$", "A1"),
                R("a", f"$x = {fr(xv)}$", "A1", "cso – no errors seen"),
                R("b", "$0$", "B1")]
        return dict(Q(parts=parts, rows=rows, values={"x": xv}, diff="4-6", cw="Show that", refs=["1B"]), variant=v)
    a = r.choice(["a", "b", "c"])
    m, nn = r.choice([(2, 3), (3, 2), (2, 5), (4, 3), (3, 4), (5, 2)])
    i, j = r.randint(1, 3), r.randint(1, 2)
    num = m ** i * nn ** j
    hk = r.choice([2, 3])
    parts = [P("a", f"Given that $\\log_{{{a}}} {m} = p$ and $\\log_{{{a}}} {nn} = q$, show that $\\log_{{{a}}} {num} = {i if i > 1 else ''}p + {j if j > 1 else ''}q$", 2),
             P("b", f"Hence express $\\log_{{{a}}} \\left(\\dfrac{{{num}}}{{{a}^{hk}}}\\right)$ in terms of $p$ and $q$", 2)]
    rows = [R("a", f"${num} = {xpow(i, str(m))} \\times {xpow(j, str(nn))}$", "M1", "correct factorisation"),
            R("a", f"$\\log_{{{a}}} {num} = {i if i > 1 else ''}\\log_{{{a}}} {m} + {j if j > 1 else ''}\\log_{{{a}}} {nn} = {i if i > 1 else ''}p + {j if j > 1 else ''}q$", "A1", "cso"),
            R("b", f"$\\log_{{{a}}} {num} - {hk}\\log_{{{a}}} {a}$", "M1"),
            R("b", f"${i if i > 1 else ''}p + {j if j > 1 else ''}q - {hk}$", "A1", "oe")]
    return dict(Q(parts=parts, rows=rows, values={"expr": f"{i}*p + {j}*q - {hk}"}, diff="1-3", cw="Show that", refs=["1B"]),
                variant=v)


@tpl("logs.laws", "multi-part", 22)
def ll_multi(r):
    v = r.choice(["simul", "quadexp"])
    if v == "simul":
        b = r.choice([2, 3, 5, 7])
        c = r.randint(2, 6)
        m = r.randint(1, 4)
        x1 = c * m
        y1 = c * m * m
        d = x1 + y1
        x2 = -c - x1
        w = r.choice([8, 27, 125, 16, 81])
        wb = {8: 2, 27: 3, 125: 5, 16: 2, 81: 3}[w]
        wv = sp.log(w, wb)
        parts = [P("a", f"Find the value of $\\log_{{{wb}}} {w}$", 1),
                 P("b", f"Given that $2\\log_{{{b}}} x - \\log_{{{b}}} y = \\log_{{{b}}} {c}$, show that $y = \\dfrac{{x^2}}{{{c}}}$", 2),
                 P("c", f"Given also that $\\log_{{{b}}}(x + y) = \\log_{{{b}}} {d}$, solve the simultaneous equations to find the value of $x$ and the value of $y$", 5)]
        rows = [R("a", f"${int(wv)}$", "B1"),
                R("b", f"$\\log_{{{b}}} \\dfrac{{x^2}}{{y}} = \\log_{{{b}}} {c}$", "M1", "power and subtraction laws"),
                R("b", f"$\\dfrac{{x^2}}{{y}} = {c} \\Rightarrow y = \\dfrac{{x^2}}{{{c}}}$", "A1", "cso"),
                R("c", f"$x + \\dfrac{{x^2}}{{{c}}} = {d}$", "M1", "substitutes"),
                R("c", f"$x^2 + {c}x - {c * d} = 0$", "A1"),
                R("c", f"$(x - {x1})(x + {-x2}) = 0$", "M1", "solves their 3-term quadratic"),
                R("c", f"$x = {x1}$, $y = {y1}$", "A1", "both"),
                R("c", f"$x = {x2}$ rejected since $\\log_{{{b}}} x$ is undefined for $x < 0$", "B1")]
        return dict(Q(parts=parts, rows=rows, values={"x": x1, "y": y1}, diff="7-9", cw="Solve", refs=["1B"]), variant=v)
    a = r.choice([2, 3, 5])
    u1 = r.choice([1, 2, 3, 4, 6])
    u2 = r.choice([z for z in [F(1, 2), F(3, 2), 5, 7, 9, 10] if z != u1])
    # a u^2 - (a(u1+u2)) u + a u1 u2 = 0 -> a^(2x+1) - d a^x + e = 0
    d = a * (u1 + u2)
    e = a * u1 * u2
    if F(d).denominator != 1 or F(e).denominator != 1:
        return None
    d, e = int(d), int(e)
    xs = [math.log(float(u1), a), math.log(float(u2), a)]
    parts = [P("a", f"Show that, using the substitution $u = {a}^x$, the equation $${a}^{{2x + 1}} - {d}({a}^x) + {e} = 0$$ can be written as ${a}u^2 - {d}u + {e} = 0$", 2),
             P("b", "Hence solve the equation, giving your answers to 3 significant figures where appropriate.", 5),
             P("c", f"Show that the sum of the two solutions is $\\log_{{{a}}} {fr(F(e, a))}$", 2)]
    rows = [R("a", f"${a}^{{2x+1}} = {a} \\times ({a}^x)^2 = {a}u^2$", "M1"),
            R("a", f"${a}u^2 - {d}u + {e} = 0$", "A1", "cso"),
            R("b", f"$({a}u - {fr(a * F(u1))})(u - {fr(u2)}) = 0$ or formula", "M1"),
            R("b", f"$u = {fr(u1)}$ or $u = {fr(u2)}$", "A1"),
            R("b", f"${a}^x = {fr(u1)} \\Rightarrow x = \\dfrac{{\\log {fr(u1)}}}{{\\log {a}}}$", "M1", "takes logs of at least one"),
            R("b", f"$x = {sf(xs[0]) if xs[0] != 0 else '0'}$", "A1"),
            R("b", f"$x = {sf(xs[1])}$", "A1"),
            R("c", f"$x_1 + x_2 = \\log_{{{a}}} u_1 + \\log_{{{a}}} u_2 = \\log_{{{a}}}(u_1 u_2)$", "M1"),
            R("c", f"$u_1 u_2 = \\dfrac{{{e}}}{{{a}}}$ so sum $= \\log_{{{a}}} {fr(F(e, a))}$", "A1", "cso")]
    return dict(Q(parts=parts, rows=rows, values={"x": xs}, diff="7-9", cw="Solve", refs=["1B"]), variant=v)


# =============================================================== 1C/1D surds

def _surd(r):
    s = r.choice([2, 3, 5, 6, 7])
    return s, sp.sqrt(s)


@tpl("logs.surds", "short", 22)
def su_short(r):
    v = r.choice(["rat", "simplify", "solve"])
    s, rs = _surd(r)
    if v == "rat":
        p, q = r.randint(1, 9), nz(r, -5, 5)
        m = r.randint(1, 6)
        if m * m == s:
            return None
        e = sp.radsimp((p + q * rs) / (m - rs))
        ee = sp.expand(e)
        A_, B_ = ee.as_coefficients_dict().get(1, 0), ee.coeff(rs)
        parts = [P("", f"Express $\\dfrac{{{tex(p + q * rs)}}}{{{tex(m - rs)}}}$ in the form $a + b\\sqrt{{{s}}}$, where $a$ and $b$ are rational numbers.", 3)]
        rows = [R("", f"Multiplies numerator and denominator by ${tex(m + rs)}$", "M1"),
                R("", f"Denominator ${m * m - s}$ or numerator ${tex(sp.expand((p + q * rs) * (m + rs)))}$", "A1"),
                R("", f"${tex(ee)}$", "A1", "oe")]
        return dict(Q(parts=parts, rows=rows, values={"a": A_, "b": B_}, diff="4-6", cw="Express", refs=["1D"]), variant=v)
    if v == "simplify":
        sq = r.sample([4, 9, 16, 25], 3)
        cs = [nz(r, -4, 5) for _ in range(3)]
        terms = [c * sp.sqrt(a_ * s) for c, a_ in zip(cs, sq)]
        tot = sp.simplify(sum(terms))
        if tot == 0:
            return None
        def tt(c, a_):
            return f"{'' if c == 1 else ('-' if c == -1 else c)}\\sqrt{{{a_ * s}}}"
        ex = tt(cs[0], sq[0]) + "".join((" + " if c > 0 else " - ") + tt(abs(c), a_) for c, a_ in zip(cs[1:], sq[1:]))
        dn = r.choice([2, 3])
        parts = [P("a", f"Simplify fully $${ex}$$", 2),
                 P("b", f"Rationalise the denominator of $\\dfrac{{{dn * s}}}{{\\sqrt{{{s}}}}}$ and simplify your answer.", 2)]
        rows = [R("a", "At least two surds correctly simplified, e.g. $" + tex(terms[0]) + "$", "M1"),
                R("a", f"${tex(tot)}$", "A1"),
                R("b", f"$\\dfrac{{{dn * s}\\sqrt{{{s}}}}}{{{s}}}$", "M1"),
                R("b", f"${dn}\\sqrt{{{s}}}$", "A1")]
        return dict(Q(parts=parts, rows=rows, values={"a": tot, "b": dn * rs}, diff="1-3", cw="Simplify", refs=["1C", "1D"]),
                    variant=v)
    p, q = r.randint(2, 6), nz(r, -5, 5)
    m = r.randint(1, 4)
    # x * sqrt(s) + q = m x + p  -> x (sqrt s - m) = p - q
    if m * m == s or p == q:
        return None
    xv = sp.radsimp(sp.Rational(p - q) / (rs - m))
    xv = sp.expand(xv)
    parts = [P("", f"Solve the equation $$x\\sqrt{{{s}}} {sg(q)} = {m if m > 1 else ''}x + {p}$$ giving your answer in the form $a + b\\sqrt{{{s}}}$, where $a$ and $b$ are rational.", 4, prefix="x = ")]
    rows = [R("", f"$x(\\sqrt{{{s}}} - {m}) = {p - q}$", "M1", "collects terms in $x$"),
            R("", f"$x = \\dfrac{{{p - q}}}{{\\sqrt{{{s}}} - {m}}}$", "A1"),
            R("", f"Multiplies by $\\dfrac{{\\sqrt{{{s}}} + {m}}}{{\\sqrt{{{s}}} + {m}}}$", "M1"),
            R("", f"$x = {tex(xv)}$", "A1", "oe")]
    return dict(Q(parts=parts, rows=rows, values={"x": xv}, diff="4-6", cw="Solve", refs=["1C", "1D"]), variant=v)


@tpl("logs.surds", "show-that", 22)
def su_show(r):
    v = r.choice(["rect", "sum", "tri"])
    s, rs = _surd(r)
    if v == "rect":
        a, b = r.randint(2, 7), r.randint(1, 3)
        c, d = r.randint(2, 7), r.randint(1, 3)
        L1, L2 = a + b * rs, c - d * rs
        if float(L2) <= 0:
            return None
        A_ = sp.expand(L1 * L2)
        cont = r.choice(["rectangle", "parallelogram base"])
        parts = [P("a", f"A rectangle has length $({tex(L1)})$ cm and width $({tex(L2)})$ cm.\n\nShow that the area of the rectangle is $({tex(A_)})$ cm$^2$", 2),
                 P("b", f"Find the exact length of a diagonal of the rectangle. Give your answer in the form $\\sqrt{{p + q\\sqrt{{{s}}}}}$, where $p$ and $q$ are integers.", 3)]
        dsq = sp.expand(L1 ** 2 + L2 ** 2)
        rows = [R("a", f"$({tex(L1)})({tex(L2)}) = {tex(sp.expand(a * c))} {sg(-a * d)}\\sqrt{{{s}}} {sg(b * c)}\\sqrt{{{s}}} {sg(-b * d * s)}$", "M1", "expands with at least 3 terms correct"),
                R("a", f"$= {tex(A_)}$", "A1", "cso"),
                R("b", f"$d^2 = ({tex(L1)})^2 + ({tex(L2)})^2$", "M1", "Pythagoras"),
                R("b", f"$d^2 = {tex(dsq)}$", "A1"),
                R("b", f"$d = \\sqrt{{{tex(dsq)}}}$", "A1")]
        return dict(Q(parts=parts, rows=rows, values={"area": A_, "d2": dsq}, diff="4-6", cw="Show that",
                      refs=["1C"]), variant=v)
    if v == "sum":
        m = r.randint(2, 5)
        if m * m == s:
            return None
        c = r.randint(1, 6)
        e = sp.radsimp(c / (m + rs) + c / (m - rs))
        parts = [P("", f"Show that $$\\dfrac{{{c}}}{{{m} + \\sqrt{{{s}}}}} + \\dfrac{{{c}}}{{{m} - \\sqrt{{{s}}}}} = {fr(e)}$$", 3)]
        rows = [R("", f"Common denominator $({m} + \\sqrt{{{s}}})({m} - \\sqrt{{{s}}}) = {m * m - s}$", "M1"),
                R("", f"Numerator ${c}({m} - \\sqrt{{{s}}}) + {c}({m} + \\sqrt{{{s}}}) = {2 * c * m}$", "M1"),
                R("", f"$\\dfrac{{{2 * c * m}}}{{{m * m - s}}} = {fr(e)}$", "A1", "cso")]
        return dict(Q(parts=parts, rows=rows, values={"value": e}, diff="4-6", cw="Show that", refs=["1C", "1D"]), variant=v)
    a, b = r.randint(1, 5), r.randint(1, 4)
    L1 = a + b * rs
    L2 = sp.Rational(r.randint(2, 9))
    hyp2 = sp.expand(L1 ** 2 + L2 ** 2)
    ar = sp.expand(L1 * L2 / 2)
    parts = [P("a", f"In triangle $ABC$, angle $ABC = 90^\\circ$, $AB = ({tex(L1)})$ cm and $BC = {L2}$ cm.\n\nShow that $AC^2 = {tex(hyp2)}$", 2),
             P("b", f"Find the area of triangle $ABC$, giving your answer in the form $p + q\\sqrt{{{s}}}$", 2)]
    rows = [R("a", f"$({tex(L1)})^2 = {tex(sp.expand(L1 ** 2))}$", "M1"),
            R("a", f"$AC^2 = {tex(sp.expand(L1 ** 2))} + {L2 ** 2} = {tex(hyp2)}$", "A1", "cso"),
            R("b", f"$\\tfrac12 \\times {L2} \\times ({tex(L1)})$", "M1"),
            R("b", f"${tex(ar)}$", "A1", "oe")]
    return dict(Q(parts=parts, rows=rows, values={"AC2": hyp2, "area": ar}, diff="1-3", cw="Show that", refs=["1C"]),
                variant=v)


# =============================================================== 2A completing the square


def _cs(a, b, c):
    """a(x + p)^2 + q"""
    p = sp.Rational(b, 2 * a)
    q = sp.Rational(c) - a * p ** 2
    return p, q


def _cs_tex(a, p, q):
    inner = f"(x {'+' if p >= 0 else '-'} {fr(abs(p))})^2"
    return f"{'' if a == 1 else ('-' if a == -1 else a)}{inner}{sg(q)}"


@tpl("quad.manip", "short", 22)
def qm_short(r):
    v = r.choice(["cs", "csneg", "hidden"])
    if v in ("cs", "csneg"):
        a = r.choice([1, 2, 3]) if v == "cs" else -r.choice([1, 2, 3])
        b = nz(r, -12, 12)
        c = r.randint(-10, 15)
        p, q = _cs(a, b, c)
        ex = poly([a, b, c])
        if v == "cs":
            form = "a(x + b)^2 + c"
        else:
            form = "c - a(x + b)^2"
        parts = [P("a", f"Write ${ex}$ as ${form}$, stating the values of the constants $a$, $b$ and $c$", 3),
                 P("b", f"Hence state the {'minimum' if a > 0 else 'maximum'} value of ${ex}$ and the value of $x$ at which it occurs.", 2)]
        rows = [R("a", f"$a = {abs(a)}$", "B1"),
                R("a", f"Attempt to complete the square: ${a}\\left[(x {'+' if p >= 0 else '-'} {fr(abs(p))})^2 - {fr(p ** 2)}\\right] {sg(c)}$", "M1"),
                R("a", f"${_cs_tex(a, p, q)}$", "A1", "all values correct, oe"),
                R("b", f"{'Minimum' if a > 0 else 'Maximum'} value ${fr(q)}$", "B1", "ft their $c$"),
                R("b", f"when $x = {fr(-p)}$", "B1", "ft their $b$")]
        return dict(Q(parts=parts, rows=rows, values={"a": a, "b": p, "c": q, "turning_x": -p, "turning_y": q},
                      diff="4-6", cw="Write", refs=["2A"]), variant=v)
    # quadratic in disguise: a z^2 + b z + c with z = x^2 or z = 2^x
    r1, r2 = r.sample([F(1, 2), F(2, 3), F(3, 2), 2, 3, 4, F(5, 2), -2, -3, F(-1, 2), 5], 2)
    den = F(r1).denominator * F(r2).denominator
    cs = sp.Poly(sp.expand(den * (x - sp.Rational(str(r1))) * (x - sp.Rational(str(r2)))), x).all_coeffs()
    g = math.gcd(*[int(c_) for c_ in cs])
    cs = [int(c_) // g for c_ in cs]
    if cs[0] < 0:
        cs = [-c_ for c_ in cs]
    sub = r.choice(["x^2", "\\sqrt{x}", "2^x"])
    if sub == "x^2":
        eq = poly([cs[0], 0, cs[1], 0, cs[2]])
        sols = sorted({s_ for rt in (r1, r2) if rt > 0 for s_ in (sp.sqrt(sp.Rational(str(rt))), -sp.sqrt(sp.Rational(str(rt))))}, key=float)
    elif sub == "\\sqrt{x}":
        eq = f"{cs[0]}x {sg(cs[1])}\\sqrt{{x}} {sg(cs[2])}".replace(" + -", " - ")
        sols = [sp.Rational(str(rt)) ** 2 for rt in (r1, r2) if rt > 0]
    else:
        eq = f"{cs[0]}(2^{{2x}}) {sg(cs[1])}(2^x) {sg(cs[2])}"
        sols = [sp.Rational(str(rt)) for rt in (r1, r2) if rt > 0]
    if not sols:
        return None
    zq = poly(cs, "y")
    parts = [P("a", f"Factorise ${zq}$", 2),
             P("b", f"Hence, or otherwise, solve the equation ${eq} = 0$\n\nGive exact answers.", 3)]
    fac = sp.factor(sp.Poly(cs, sp.Symbol("y")).as_expr())
    rows = [R("a", f"Two brackets that expand to give two of the three terms", "M1"),
            R("a", f"${tex(fac)}$", "A1"),
            R("b", f"Recognises $y = {sub}$ and uses their roots", "M1"),
            R("b", f"Values of ${sub}$: ${', '.join(fr(sp.Rational(str(z))) for z in (r1, r2))}$ with any impossible value rejected", "A1"),
            R("b", f"$x = {', '.join((logx(2, s_) if sub == '2^x' else tex(s_)) for s_ in sols)}$", "A1", "all correct values and no extras" + ("; accept 3 s.f. decimals if exact form not required" if sub == "2^x" else ""))]
    if sub == "2^x":
        sols = [float(sp.log(s_, 2)) for s_ in sols]
    return dict(Q(parts=parts, rows=rows, values={"x": sols}, diff="7-9" if sub == "2^x" else "4-6", cw="Factorise",
                  refs=["2A"]), variant="hidden")


@tpl("quad.manip", "multi-part", 22)
def qm_multi(r):
    v = r.choice(["sketch", "points"])
    a = r.choice([1, 1, 2, -1])
    b = nz(r, -10, 10)
    if v == "sketch":
        c = r.randint(-9, 14)
    else:
        c = r.randint(-9, 14)
    p, q = _cs(a, b, c)
    ex = poly([a, b, c])
    if v == "sketch":
        kk_word = "two distinct real roots" if a > 0 else "two distinct real roots"
        parts = [P("a", f"Express $f(x) = {ex}$ as $A(x + B)^2 + C$, stating the values of the constants $A$, $B$ and $C$", 3),
                 P("b", "Write down the coordinates of the turning point of the curve $y = f(x)$", 2),
                 P("c", "Sketch the curve with equation $y = f(x)$, showing the coordinates of the turning point and of the point where the curve crosses the $y$-axis.", 3, space="box"),
                 P("d", "Determine every value of $k$ such that $f(x) = k$ has two different real solutions.", 2)]
        rel = ">" if a > 0 else "<"
        rows = [R("a", f"$A = {a}$", "B1"),
                R("a", "Attempt to complete the square", "M1"),
                R("a", f"${_cs_tex(a, p, q)}$", "A1"),
                R("b", f"$({fr(-p)}, {fr(q)})$", "B1 B1", "ft their $B$ and $C$; B1 each coordinate"),
                R("c", f"{'U' if a > 0 else '∩'}-shaped parabola", "B1"),
                R("c", f"Turning point at $({fr(-p)}, {fr(q)})$ shown", "B1", "ft"),
                R("c", f"$y$-intercept $(0, {c})$", "B1"),
                R("d", f"$k {rel} {fr(q)}$", "M1 A1", "M1 uses the turning point value")]
        return dict(Q(parts=parts, rows=rows, values={"A": a, "B": p, "C": q, "k": f"k {rel} {q}"}, diff="4-6",
                      cw="Express", refs=["2A", "2B"]), variant=v)
    x1, x2 = r.sample(range(-4, 5), 2)
    y1, y2 = a * x1 ** 2 + b * x1 + c, a * x2 ** 2 + b * x2 + c
    lim = r.randint(int(q) + 2, int(q) + 25) if a > 0 else r.randint(int(q) - 25, int(q) - 2)
    sol = sp.solve(a * x ** 2 + b * x + c - lim, x)
    if len(sol) != 2 or not all(s_.is_real for s_ in sol):
        return None
    s1, s2 = sorted(sol, key=float)
    lead = "" if a == 1 else ("-" if a == -1 else str(a))
    parts = [P("a", f"The curve with equation $y = {lead}x^2 + px + q$ passes through the points $({x1}, {y1})$ and $({x2}, {y2})$\n\nFind the value of $p$ and the value of $q$", 4),
             P("b", f"Write ${ex}$ in the form $A(x + B)^2 + C$", 3),
             P("c", f"Find the set of values of $x$ for which ${ex} < {lim}$", 3)]
    ineq = f"{tex(s1)} < x < {tex(s2)}" if a > 0 else f"x < {tex(s1)}, \\; x > {tex(s2)}"
    rows = [R("a", f"${tex(a * x1 * x1 + x1 * sp.Symbol('p') + sp.Symbol('q'))} = {y1}$ and ${tex(a * x2 * x2 + x2 * sp.Symbol('p') + sp.Symbol('q'))} = {y2}$", "M1"),
            R("a", "Solves simultaneously", "M1"),
            R("a", f"$p = {b}$", "A1"),
            R("a", f"$q = {c}$", "A1"),
            R("b", f"$A = {a}$", "B1"),
            R("b", "Completing the square method", "M1"),
            R("b", f"${_cs_tex(a, p, q)}$", "A1"),
            R("c", f"Critical values $x = {tex(s1)}$ and $x = {tex(s2)}$", "M1 A1", f"M1 solves ${ex} = {lim}$"),
            R("c", f"${ineq}$", "A1", "correct region chosen")]
    return dict(Q(parts=parts, rows=rows, values={"p": b, "q": c, "crit": [s1, s2]}, diff="7-9", cw="Find",
                  refs=["2A", "3D"]), variant=v)


# =============================================================== 2B discriminant


def _k_family(r):
    for _ in range(200):
        a1, a0 = r.randint(-1, 2), r.randint(-3, 4)
        b1, b0 = r.randint(-2, 2), r.randint(-6, 6)
        c1, c0 = r.randint(-1, 2), r.randint(-4, 5)
        A = a1 * k + a0
        B = b1 * k + b0
        C = c1 * k + c0
        D = sp.expand(B ** 2 - 4 * A * C)
        if sp.degree(D, k) != 2:
            continue
        sols = sp.solve(D, k)
        if len(sols) != 2 or not all(s_.is_rational for s_ in sols):
            continue
        if any(A.subs(k, s_) == 0 for s_ in sols):
            continue
        if any(abs(s_.q) > 4 or abs(s_) > 12 for s_ in sols):
            continue
        if a1 == 0 and b1 == 0:
            continue
        return A, B, C, D, sorted(sols)
    return None


@tpl("quad.discriminant", "short", 22)
def qd_short(r):
    fam = _k_family(r)
    if not fam:
        return None
    A, B, C, D, sols = fam
    eq = kq(A, B, C)
    v = r.choice(["equal", "none", "two"])
    lead = sp.Poly(D, k).LC()
    if v == "equal":
        parts = [P("", f"The equation $${eq} = 0$$ where $k$ is a constant, has equal roots.\n\nFind the possible values of $k$", 4)]
        rows = [R("", "Uses $b^2 - 4ac = 0$ with their $a$, $b$, $c$", "M1"),
                R("", f"${tex(D)} = 0$", "A1"),
                R("", "Solves their 3-term quadratic in $k$", "M1"),
                R("", f"$k = {fr(sols[0])}$, $k = {fr(sols[1])}$", "A1")]
        val = sols
    else:
        want_neg = v == "none"
        inside = (lead > 0) == want_neg
        reg = f"{fr(sols[0])} < k < {fr(sols[1])}" if inside else f"k < {fr(sols[0])} \\text{{ or }} k > {fr(sols[1])}"
        # exclude any k that makes the x^2 coefficient vanish (the equation is then not a quadratic)
        excl = None
        if A.has(k):
            k0 = sp.solve(A, k)[0]
            in_reg = (sols[0] < k0 < sols[1]) if inside else (k0 < sols[0] or k0 > sols[1])
            if in_reg:
                if want_neg and B.subs(k, k0) == 0:
                    return None
                excl = k0
                reg += f", \\; k \\neq {fr(k0)}"
        words = "has no real roots" if want_neg else "has two distinct real roots"
        parts = [P("", f"Given that the equation $${eq} = 0$$ {words}, find the set of possible values of $k$", 5)]
        rows = [R("", f"Uses $b^2 - 4ac {'<' if want_neg else '>'} 0$", "M1"),
                R("", f"${tex(D)} {'<' if want_neg else '>'} 0$", "A1", "oe"),
                R("", "Finds critical values", "M1"),
                R("", f"$k = {fr(sols[0])}$, $k = {fr(sols[1])}$", "A1"),
                R("", f"${reg}$", "A1", "correct region" + (f"; must exclude $k = {fr(excl)}$, which makes the coefficient of $x^2$ zero" if excl is not None else ""))]
        val = reg
    return dict(Q(parts=parts, rows=rows, values={"k": val}, diff="7-9" if v != "equal" else "4-6", cw="Find",
                  refs=["2B"]), variant=v)


@tpl("quad.discriminant", "show-that", 22)
def qd_show(r):
    v = r.choice(["allk", "tangent"])
    if v == "allk":
        a = r.choice([1, 2])
        b = r.randint(-4, 4)
        c = r.choice([-2, -1, 1, 2])
        d = r.randint(-4, 4)
        # a x^2 + (k + b) x + (c k + d)
        D = sp.expand((k + b) ** 2 - 4 * a * (c * k + d))
        m = sp.Rational(sp.Poly(D, k).coeffs()[1] if len(sp.Poly(D, k).coeffs()) > 2 else 0, 2)
        cd = sp.Poly(D, k).all_coeffs()
        m = sp.Rational(cd[1], 2)
        qq = cd[2] - m ** 2
        if qq <= 0:
            return None
        eq = kq(a, k + b, c * k + d)
        if m == 0:
            return None
        parts = [P("", f"Show that the equation $${eq} = 0$$ has two distinct real roots for all real values of $k$", 4)]
        rows = [R("", f"$b^2 - 4ac = ({tex(k + b)})^2 - {4 * a}({tex(c * k + d)})$", "M1"),
                R("", f"$= {tex(D)}$", "A1"),
                R("", f"$= (k {'+' if m >= 0 else '-'} {fr(abs(m))})^2 + {fr(qq)}$", "M1", "completes the square or other valid argument"),
                R("", f"$> 0$ for all $k$ since a square is non-negative, so two distinct real roots", "A1", "cso with conclusion")]
        return dict(Q(parts=parts, rows=rows, values={"disc": D}, diff="7-9", cw="Show that", refs=["2B"]), variant=v)
    a = r.choice([1, 2, -1])
    b = r.randint(-6, 6)
    d = r.randint(-5, 8)
    m = nz(r, -6, 6)
    # tangent: a x^2 + b x + d = m x + c has equal roots -> c chosen
    # (b - m)^2 = 4a(d - c)
    x0 = sp.Rational(m - b, 2 * a)
    c = a * x0 ** 2 + b * x0 + d - m * x0
    if c.q != 1 or x0.q > 2:
        return None
    y0 = m * x0 + c
    parts = [P("a", f"Show that the line with equation $y = {lin(m, c)}$ is a tangent to the curve with equation $y = {poly([a, b, d])}$", 4),
             P("b", "Find the coordinates of the point of contact.", 2)]
    rows = [R("a", f"${poly([a, b, d])} = {lin(m, c)}$", "M1", "equates"),
            R("a", f"${poly([a, b - m, d - c])} = 0$", "A1"),
            R("a", f"$b^2 - 4ac = ({b - m})^2 - 4({a})({d - c})$", "M1"),
            R("a", "$= 0$ so equal roots, hence the line is a tangent", "A1", "cso with conclusion"),
            R("b", f"$x = {fr(x0)}$", "M1", "solves their quadratic"),
            R("b", f"$({fr(x0)}, {fr(y0)})$", "A1")]
    return dict(Q(parts=parts, rows=rows, values={"x": x0, "y": y0}, diff="4-6", cw="Show that", refs=["2B", "3C"]),
                variant=v)


# =============================================================== 2C roots


al, be = sp.symbols("alpha beta")
S_, P_ = sp.symbols("S P")
EXPRS = [
    ("\\alpha^2 + \\beta^2", al ** 2 + be ** 2),
    ("\\alpha^3 + \\beta^3", al ** 3 + be ** 3),
    ("\\dfrac{1}{\\alpha} + \\dfrac{1}{\\beta}", 1 / al + 1 / be),
    ("(\\alpha - \\beta)^2", (al - be) ** 2),
    ("\\dfrac{\\alpha}{\\beta} + \\dfrac{\\beta}{\\alpha}", al / be + be / al),
    ("\\alpha^2\\beta + \\alpha\\beta^2", al ** 2 * be + al * be ** 2),
    ("\\dfrac{1}{\\alpha^2} + \\dfrac{1}{\\beta^2}", 1 / al ** 2 + 1 / be ** 2),
    ("(\\alpha + 2)(\\beta + 2)", (al + 2) * (be + 2)),
]
NEWROOTS = [
    ("\\alpha + 3", "\\beta + 3", al + 3, be + 3),
    ("\\alpha^2", "\\beta^2", al ** 2, be ** 2),
    ("\\dfrac{1}{\\alpha}", "\\dfrac{1}{\\beta}", 1 / al, 1 / be),
    ("\\dfrac{\\alpha}{\\beta}", "\\dfrac{\\beta}{\\alpha}", al / be, be / al),
    ("\\alpha + \\dfrac{1}{\\beta}", "\\beta + \\dfrac{1}{\\alpha}", al + 1 / be, be + 1 / al),
    ("2\\alpha - \\beta", "2\\beta - \\alpha", 2 * al - be, 2 * be - al),
    ("\\alpha^2\\beta", "\\alpha\\beta^2", al ** 2 * be, al * be ** 2),
    ("\\dfrac{\\alpha}{\\beta^2}", "\\dfrac{\\beta}{\\alpha^2}", al / be ** 2, be / al ** 2),
]


def sym_eval(expr, s, p):
    from sympy.polys.polyfuncs import symmetrize
    num, den = sp.fraction(sp.together(expr))
    def ev(e):
        sym, rem, defs = symmetrize(sp.expand(e), al, be, formal=True)
        assert rem == 0
        return sym.subs({d[0]: (s if d[1] == al + be else p) for d in defs})
    return sp.nsimplify(ev(num) / ev(den))


def _roots_eq(r):
    a = r.choice([1, 2, 3, 2, 3])
    b = nz(r, -9, 9)
    c = nz(r, -8, 8)
    s, p = sp.Rational(-b, a), sp.Rational(c, a)
    return a, b, c, s, p


@tpl("quad.roots", "short", 22)
def qr_short(r):
    a, b, c, s, p = _roots_eq(r)
    e1, e2 = r.sample(EXPRS, 2)
    v1, v2 = sym_eval(e1[1], s, p), sym_eval(e2[1], s, p)
    eq = poly([a, b, c])
    parts = [P("", f"The roots of the equation ${eq} = 0$ are $\\alpha$ and $\\beta$\n\nWithout solving the equation, find the exact value of\n\n(i) ${e1[0]}$\n\n(ii) ${e2[0]}$", 5)]
    rows = [R("", f"$\\alpha + \\beta = {fr(s)}$, $\\alpha\\beta = {fr(p)}$", "B1"),
            R("", f"(i) Writes ${e1[0]}$ in terms of $\\alpha + \\beta$ and $\\alpha\\beta$", "M1"),
            R("", f"(i) ${fr(v1)}$", "A1"),
            R("", f"(ii) Writes ${e2[0]}$ in terms of $\\alpha + \\beta$ and $\\alpha\\beta$", "M1"),
            R("", f"(ii) ${fr(v2)}$", "A1")]
    return dict(Q(parts=parts, rows=rows, values={"sum": s, "product": p, "i": v1, "ii": v2}, diff="4-6",
                  cw="Find", refs=["2C"]), variant="eval")


@tpl("quad.roots", "multi-part", 22)
def qr_multi(r):
    a, b, c, s, p = _roots_eq(r)
    e1 = r.choice(EXPRS[:4])
    nr = r.choice(NEWROOTS)
    v1 = sym_eval(e1[1], s, p)
    ns = sym_eval(nr[2] + nr[3], s, p)
    npd = sym_eval(nr[2] * nr[3], s, p)
    den = sp.ilcm(ns.q, npd.q)
    coeffs = [den, -ns * den, npd * den]
    g = sp.igcd(*[int(c_) for c_ in coeffs])
    coeffs = [int(c_ / g) for c_ in coeffs]
    neweq = poly(coeffs)
    eq = poly([a, b, c])
    parts = [P("a", f"Write down the value of $\\alpha + \\beta$ and the value of $\\alpha\\beta$", 2),
             P("b", f"Find the value of ${e1[0]}$", 2),
             P("c", f"Form a quadratic equation, with integer coefficients, which has roots ${nr[0]}$ and ${nr[1]}$", 5)]
    intro = f"The equation ${eq} = 0$ has roots $\\alpha$ and $\\beta$"
    rows = [R("a", f"$\\alpha + \\beta = {fr(s)}$", "B1"),
            R("a", f"$\\alpha\\beta = {fr(p)}$", "B1"),
            R("b", "Correct expression in terms of $\\alpha + \\beta$ and $\\alpha\\beta$", "M1"),
            R("b", f"${fr(v1)}$", "A1"),
            R("c", "Attempt at sum of new roots in terms of $\\alpha + \\beta$, $\\alpha\\beta$", "M1"),
            R("c", f"Sum $= {fr(ns)}$", "A1"),
            R("c", "Attempt at product of new roots", "M1"),
            R("c", f"Product $= {fr(npd)}$", "A1"),
            R("c", f"${neweq} = 0$", "A1", "oe with integer coefficients; '= 0' required")]
    return dict(Q(intro=intro, parts=parts, rows=rows, values={"sum": ns, "product": npd, "equation": neweq},
                  diff="7-9", cw="Form", refs=["2C"]), variant="form")


@tpl("quad.roots", "show-that", 22)
def qr_show(r):
    v = r.choice(["cube", "kroots"])
    if v == "cube":
        a, b, c, s, p = _roots_eq(r)
        v3 = sym_eval(al ** 3 + be ** 3, s, p)
        v2 = sym_eval(al ** 2 + be ** 2, s, p)
        eq = poly([a, b, c])
        parts = [P("a", f"Show that $\\alpha^3 + \\beta^3 = (\\alpha + \\beta)^3 - 3\\alpha\\beta(\\alpha + \\beta)$", 2),
                 P("b", f"Given that $\\alpha$ and $\\beta$ are the roots of ${eq} = 0$, show that $\\alpha^3 + \\beta^3 = {fr(v3)}$", 3),
                 P("c", f"Find the value of $\\alpha^2 + \\beta^2$", 2)]
        rows = [R("a", "$(\\alpha + \\beta)^3 = \\alpha^3 + 3\\alpha^2\\beta + 3\\alpha\\beta^2 + \\beta^3$", "M1"),
                R("a", "$= \\alpha^3 + \\beta^3 + 3\\alpha\\beta(\\alpha + \\beta)$, rearranged", "A1", "cso"),
                R("b", f"$\\alpha + \\beta = {fr(s)}$, $\\alpha\\beta = {fr(p)}$", "B1"),
                R("b", f"$({fr(s)})^3 - 3({fr(p)})({fr(s)})$", "M1"),
                R("b", f"$= {fr(v3)}$", "A1", "cso"),
                R("c", "$(\\alpha + \\beta)^2 - 2\\alpha\\beta$", "M1"),
                R("c", f"${fr(v2)}$", "A1")]
        return dict(Q(parts=parts, rows=rows, values={"cube_sum": v3, "square_sum": v2}, diff="4-6", cw="Show that",
                      refs=["2C"]), variant=v)
    # one root is m times the other
    m = r.choice([2, 3, 4])
    be0 = nz(r, -4, 4)
    a = r.choice([1, 2])
    # roots be0 and m be0: sum (m+1)be0 = -b/a, product m be0^2 = c/a
    b = -a * (m + 1) * be0
    c = a * m * be0 ** 2
    parts = [P("a", f"The equation $${a if a > 1 else ''}x^2 + px + {c} = 0$$ has roots $\\alpha$ and $\\beta$, where $\\alpha = {m}\\beta$ and $p$ is a constant.\n\nShow that $\\beta^2 = {fr(sp.Rational(c, a * m))}$", 3),
             P("b", "Hence find the possible values of $p$", 3)]
    pv = sorted({-a * (m + 1) * be0, a * (m + 1) * be0})
    rows = [R("a", f"$\\alpha\\beta = {fr(sp.Rational(c, a))}$", "B1"),
            R("a", f"${m}\\beta^2 = {fr(sp.Rational(c, a))}$", "M1"),
            R("a", f"$\\beta^2 = {fr(sp.Rational(c, a * m))}$", "A1", "cso"),
            R("b", f"$\\beta = \\pm {abs(be0)}$", "B1"),
            R("b", f"$\\alpha + \\beta = {m + 1}\\beta = -\\dfrac{{p}}{{{a}}}$", "M1"),
            R("b", f"$p = {pv[0]}$ or $p = {pv[1]}$", "A1")]
    return dict(Q(parts=parts, rows=rows, values={"p": pv}, diff="7-9", cw="Show that", refs=["2C"]), variant=v)


# =============================================================== 3A/3B factor & remainder


def _cubic(r, lead=None):
    a = lead or r.choice([1, 1, 2, 3])
    roots = [nz(r, -4, 4)]
    if a > 1:
        roots.append(sp.Rational(nz(r, -3, 3), a))
    else:
        roots.append(nz(r, -5, 5))
    roots.append(nz(r, -5, 5))
    f = sp.expand(a * sp.prod([(x - z) for z in roots]))
    return a, roots, f


@tpl("ident.factor", "short", 22)
def if_short(r):
    v = r.choice(["find_ab", "divide", "remainder"])
    if v == "find_ab":
        a, roots, f = _cubic(r)
        cs = sp.Poly(f, x).all_coeffs()
        p0 = roots[0]
        q0 = r.choice([z for z in [-3, -2, -1, 1, 2, 3, sp.Rational(1, 2), sp.Rational(-1, 2)] if z not in roots])
        rem = f.subs(x, q0)
        dv = f"(2x {'+' if q0 < 0 else '-'} 1)" if abs(q0) == sp.Rational(1, 2) else f"(x {'+' if q0 < 0 else '-'} {abs(q0)})"
        ex = f"{'' if a == 1 else a}x^3 + px^2 + qx {sg(cs[3])}"
        parts = [P("", f"$$\\mathrm{{f}}(x) = {ex}$$ and $p$, $q$ are constants.\n\nGiven that $(x {'+' if p0 < 0 else '-'} {abs(p0)})$ is a factor of $\\mathrm{{f}}(x)$ and that the remainder when $\\mathrm{{f}}(x)$ is divided by ${dv}$ is ${fr(rem)}$, find the value of $p$ and the value of $q$", 5)]
        rows = [R("", f"$\\mathrm{{f}}({p0}) = 0$ used", "M1"),
                R("", f"$\\mathrm{{f}}({fr(q0)}) = {fr(rem)}$ used", "M1"),
                R("", "Both equations correct and simplified", "A1"),
                R("", "Solves simultaneously", "M1", "dM1 – dependent on both previous M marks"),
                R("", f"$p = {cs[1]}$, $q = {cs[2]}$", "A1")]
        return dict(Q(parts=parts, rows=rows, values={"p": cs[1], "q": cs[2]}, diff="4-6", cw="Find", refs=["3B"]),
                    variant=v)
    if v == "divide":
        cs = [r.choice([1, 2, 3]), nz(r, -6, 6), r.randint(-9, 9), r.randint(-9, 9)]
        f = sp.Poly(cs, x).as_expr()
        dv = r.choice([x + nz(r, -4, 4), 2 * x + r.choice([-3, -1, 1, 3])])
        qt, rm = sp.div(f, dv, x)
        parts = [P("", f"Find the quotient and the remainder when $${poly(cs)}$$ is divided by $({tex(dv)})$", 4)]
        rows = [R("", "Long division (or equivalent) with first term of quotient correct", "M1"),
                R("", "Quotient with at least two terms correct", "A1"),
                R("", f"Quotient ${tex(sp.expand(qt))}$", "A1"),
                R("", f"Remainder ${fr(rm)}$", "B1", "remainder theorem may be used for this mark")]
        return dict(Q(parts=parts, rows=rows, values={"quotient": sp.expand(qt), "remainder": rm}, diff="4-6",
                      cw="Find", refs=["3A", "3B"]), variant=v)
    a, roots, f = _cubic(r)
    kk = nz(r, -4, 4)
    g = sp.expand(f + kk * x)
    q0 = sp.Rational(r.choice([F(1, 2), F(-3, 2), F(1, 3), -2, 3]))
    rem = g.subs(x, q0)
    dvt = f"({q0.q}x {'-' if q0 > 0 else '+'} {abs(q0.p)})" if q0.q > 1 else f"(x {'-' if q0 > 0 else '+'} {abs(q0)})"
    parts = [P("", f"Find the remainder when $\\mathrm{{f}}(x) = {tex(g)}$ is divided by ${dvt}$", 2)]
    if r.random() < 0.5:
        parts = [P("a", f"Find the remainder when $\\mathrm{{f}}(x) = {tex(g)}$ is divided by ${dvt}$", 2),
                 P("b", f"Find the value of the constant $c$ such that $(x {'-' if roots[0] > 0 else '+'} {abs(roots[0])})$ is a factor of $\\mathrm{{f}}(x) + cx$", 2)]
        cval = -kk
        rows = [R("a", f"$\\mathrm{{f}}({fr(q0)})$ attempted", "M1"),
                R("a", f"${fr(rem)}$", "A1"),
                R("b", f"$\\mathrm{{f}}({roots[0]}) + {roots[0]}c = 0$", "M1"),
                R("b", f"$c = {cval}$", "A1")]
        return dict(Q(parts=parts, rows=rows, values={"remainder": rem, "c": cval}, diff="4-6", cw="Find",
                      refs=["3B"]), variant="rem2")
    rows = [R("", f"$\\mathrm{{f}}({fr(q0)})$ attempted", "M1"), R("", f"${fr(rem)}$", "A1")]
    return dict(Q(parts=parts, rows=rows, values={"remainder": rem}, diff="1-3", cw="Find", refs=["3B"]), variant=v)


@tpl("ident.factor", "show-that", 22)
def if_show(r):
    a, roots, f = _cubic(r)
    p0 = roots[0]
    fac = sp.factor(f)
    other = sp.factor(sp.cancel(f / (x - p0)))
    parts = [P("a", f"Show that $(x {'-' if p0 > 0 else '+'} {abs(p0)})$ is a factor of $\\mathrm{{f}}(x) = {tex(f)}$", 2),
             P("b", "Hence factorise $\\mathrm{f}(x)$ completely.", 3),
             P("c", "Hence solve the equation $\\mathrm{f}(x) = 0$", 1)]
    sols = sorted(set(roots), key=float)
    rows = [R("a", f"$\\mathrm{{f}}({p0}) = {tex(f).replace('x', '(' + str(p0) + ')')}$", "M1", "substitutes"),
            R("a", f"$= 0$ so $(x {'-' if p0 > 0 else '+'} {abs(p0)})$ is a factor", "A1", "cso with conclusion"),
            R("b", "Divides by the factor or compares coefficients to obtain a quadratic", "M1"),
            R("b", f"$(x {'-' if p0 > 0 else '+'} {abs(p0)})({tex(sp.expand(other))})$", "A1"),
            R("b", f"${tex(fac)}$", "A1"),
            R("c", f"$x = {', '.join(fr(z) for z in sols)}$", "B1", "ft their factors")]
    return dict(Q(parts=parts, rows=rows, values={"roots": sols}, diff="4-6", cw="Show that", refs=["3B"]),
                variant="factor")


@tpl("ident.factor", "multi-part", 22)
def if_multi(r):
    # f(x) = a x^3 + p x^2 + q x + c with a linear factor and irrational quadratic factor
    a = r.choice([1, 2])
    p0 = nz(r, -3, 3)
    for _ in range(40):
        bq, cq = r.randint(-6, 6), r.randint(-6, 6)
        disc = bq * bq - 4 * a * cq
        if disc > 0 and sp.sqrt(disc).is_rational is False:
            break
    else:
        return None
    f = sp.expand((x - p0) * (a * x ** 2 + bq * x + cq))
    cs = sp.Poly(f, x).all_coeffs()
    q0 = r.choice([z for z in [-2, -1, 1, 2, 3] if z != p0])
    rem = f.subs(x, q0)
    ex = f"{'' if a == 1 else a}x^3 + px^2 + qx {sg(cs[3])}"
    sols = sp.solve(a * x ** 2 + bq * x + cq, x)
    parts = [P("a", f"Given that $(x {'-' if p0 > 0 else '+'} {abs(p0)})$ is a factor of $\\mathrm{{f}}(x)$, and that when $\\mathrm{{f}}(x)$ is divided by $(x {'-' if q0 > 0 else '+'} {abs(q0)})$ the remainder is ${rem}$, find the value of $p$ and the value of $q$", 5),
             P("b", "Hence write $\\mathrm{f}(x)$ as the product of a linear factor and a quadratic factor.", 2),
             P("c", "Find the exact solutions of the equation $\\mathrm{f}(x) = 0$", 3)]
    intro = f"$$\\mathrm{{f}}(x) = {ex}$$ and $p$, $q$ are constants."
    rows = [R("a", f"$\\mathrm{{f}}({p0}) = 0$", "M1"),
            R("a", f"$\\mathrm{{f}}({q0}) = {rem}$", "M1"),
            R("a", "Two correct simplified linear equations", "A1"),
            R("a", "Solves simultaneously", "M1", "dM1"),
            R("a", f"$p = {cs[1]}$, $q = {cs[2]}$", "A1"),
            R("b", "Division or comparison of coefficients", "M1"),
            R("b", f"$(x {'-' if p0 > 0 else '+'} {abs(p0)})({poly([a, bq, cq])})$", "A1"),
            R("c", f"$x = {p0}$", "B1"),
            R("c", "Correct use of the quadratic formula on their quadratic factor", "M1"),
            R("c", f"$x = {', '.join(tex(s_) for s_ in sols)}$", "A1", "exact form")]
    return dict(Q(intro=intro, parts=parts, rows=rows, values={"p": cs[1], "q": cs[2], "roots": [p0] + sols},
                  diff="7-9", cw="Find", refs=["3A", "3B", "3C"]), variant="factor-irr")


# =============================================================== 3C simultaneous / cubic


def _linquad(r):
    for _ in range(200):
        m, c0 = nz(r, -3, 3), r.randint(-5, 5)
        A, B, C, D, E = r.randint(1, 3), r.randint(-2, 2), r.randint(0, 2), r.randint(-4, 4), r.randint(-4, 4)
        x1 = r.randint(-4, 4)
        Qe = A * x ** 2 + B * x * y + C * y ** 2 + D * x + E * y
        sub = sp.expand(Qe.subs(y, m * x + c0))
        f0 = -sub.subs(x, x1)
        Qp = sp.Poly(sub + f0, x)
        if Qp.degree() != 2:
            continue
        sols = sp.solve(Qp.as_expr(), x)
        if len(sols) != 2 or not all(s_.is_rational and s_.q <= 3 for s_ in sols):
            continue
        rhs = -f0
        return m, c0, Qe, rhs, sols, Qp
    return None


@tpl("ident.simul", "short", 22)
def is_short(r):
    v = r.choice(["lq", "lq", "cubic"])
    if v == "lq":
        res = _linquad(r)
        if not res:
            return None
        m, c0, Qe, rhs, sols, Qp = res
        pts = [(s_, m * s_ + c0) for s_ in sorted(sols)]
        g = sp.gcd_list([int(c_) for c_ in Qp.all_coeffs()])
        lin_eq = f"{tex(y - m * x)} = {c0}" if r.random() < 0.5 else f"y = {lin(m, c0)}"
        parts = [P("", f"Solve the simultaneous equations\n\n$${lin_eq}$$\n$${tex(Qe)} = {rhs}$$\n\nShow clear algebraic working.", 6)]
        rows = [R("", f"Substitutes $y = {lin(m, c0)}$ into the second equation", "M1"),
                R("", f"${tex(sp.expand(Qp.as_expr() / g))} = 0$", "A1", "oe 3-term quadratic"),
                R("", "Solves their 3-term quadratic", "M1"),
                R("", f"$x = {fr(pts[0][0])}$, $x = {fr(pts[1][0])}$", "A1"),
                R("", "Substitutes at least one $x$ value to find $y$", "M1", "dM1"),
                R("", f"$y = {fr(pts[0][1])}$, $y = {fr(pts[1][1])}$ (correctly paired)", "A1")]
        return dict(Q(parts=parts, rows=rows, values={"solutions": [list(p_) for p_ in pts]}, diff="4-6", cw="Solve",
                      refs=["3C"]), variant=v)
    a, roots, f = _cubic(r, lead=r.choice([1, 2]))
    sols = sorted(set(roots), key=float)
    ints = [z for z in roots if sp.Rational(z).q == 1]
    parts = [P("", f"Solve the equation $${tex(f)} = 0$$", 5)]
    rows = [R("", f"Finds a root by the factor theorem, e.g. $\\mathrm{{f}}({ints[0]}) = 0$", "M1"),
            R("", f"$(x {'-' if ints[0] > 0 else '+'} {abs(ints[0])})$ is a factor", "A1"),
            R("", "Obtains the quadratic factor by division or comparing coefficients", "M1"),
            R("", f"${tex(sp.factor(f))}$", "A1"),
            R("", f"$x = {', '.join(fr(z) for z in sols)}$", "A1")]
    return dict(Q(parts=parts, rows=rows, values={"roots": sols}, diff="4-6", cw="Solve", refs=["3B", "3C"]),
                variant=v)


@tpl("ident.simul", "multi-part", 22)
def is_multi(r):
    res = _linquad(r)
    if not res:
        return None
    m, c0, Qe, rhs, sols, Qp = res
    pts = [(s_, m * s_ + c0) for s_ in sorted(sols)]
    (xa, ya), (xb, yb) = pts
    d2 = (xa - xb) ** 2 + (ya - yb) ** 2
    mid = ((xa + xb) / 2, (ya + yb) / 2)
    pm = sp.Rational(-1, m)
    cc = mid[1] - pm * mid[0]
    # integer form ax + by + c = 0
    A_, B_, C_ = pm.p * (1 if pm.q else 1), -pm.q, cc * pm.q
    den = sp.ilcm(1, cc.q)
    A_, B_, C_ = [sp.Rational(v_) * den for v_ in (pm * pm.q, -pm.q, cc * pm.q)]
    if A_ < 0:
        A_, B_, C_ = -A_, -B_, -C_
    perp = f"{tex(A_ * x + B_ * y + C_)} = 0"
    g = sp.gcd_list([int(c_) for c_ in Qp.all_coeffs()])
    parts = [P("a", "Find the coordinates of $A$ and the coordinates of $B$", 6),
             P("b", "Find the exact length of $AB$", 2),
             P("c", "Find an equation of the perpendicular bisector of $AB$. Give your answer in the form $ax + by + c = 0$, where $a$, $b$ and $c$ are integers.", 4)]
    intro = f"The line with equation $y = {lin(m, c0)}$ meets the curve with equation ${tex(Qe)} = {rhs}$ at the points $A$ and $B$, where the $x$-coordinate of $A$ is less than the $x$-coordinate of $B$."
    rows = [R("a", "Substitutes the linear equation into the curve", "M1"),
            R("a", f"${tex(sp.expand(Qp.as_expr() / g))} = 0$", "A1"),
            R("a", "Solves their quadratic", "M1"),
            R("a", f"$x = {fr(xa)}$, ${fr(xb)}$", "A1"),
            R("a", "Finds the corresponding $y$ values", "M1", "dM1"),
            R("a", f"$A({fr(xa)}, {fr(ya)})$, $B({fr(xb)}, {fr(yb)})$", "A1"),
            R("b", "Correct use of the distance formula with their points", "M1"),
            R("b", f"$AB = {tex(sp.sqrt(d2))}$", "A1", "exact"),
            R("c", f"Midpoint $({fr(mid[0])}, {fr(mid[1])})$", "B1", "ft"),
            R("c", f"Perpendicular gradient $= {fr(pm)}$", "B1", "ft"),
            R("c", f"${tex(y - mid[1])} = {fr(pm)}({tex(x - mid[0])})$", "M1"),
            R("c", f"${perp}$", "A1", "or any integer multiple")]
    return dict(Q(intro=intro, parts=parts, rows=rows, values={"A": list(pts[0]), "B": list(pts[1]), "AB2": d2, "perp": perp},
                  diff="7-9", cw="Find", refs=["3C", "8A", "8E"]), variant="lq-line")


# =============================================================== 3D inequalities


def _quad_ineq(r):
    a = r.choice([1, 1, 2, 3, -1, -2])
    r1, r2 = sorted(r.sample([-5, -4, -3, -2, -1, F(-1, 2), F(1, 2), F(3, 2), 1, 2, 3, 4, 5, F(-3, 2), F(2, 3)], 2))
    den = F(r1).denominator * F(r2).denominator
    cs = sp.Poly(sp.expand(a * den * (x - sp.Rational(str(r1))) * (x - sp.Rational(str(r2)))), x).all_coeffs()
    g = sp.igcd(*[int(c_) for c_ in cs])
    cs = [int(c_ / g) for c_ in cs]
    return cs, sp.Rational(str(r1)), sp.Rational(str(r2))


@tpl("ident.ineq", "short", 22)
def ii_short(r):
    cs, r1, r2 = _quad_ineq(r)
    op = r.choice(["<", ">", "\\leqslant", "\\geqslant"])
    a = cs[0]
    inside = (op in ("<", "\\leqslant")) == (a > 0)
    st = "\\leqslant" if op in ("\\leqslant", "\\geqslant") else "<"
    ans = f"{fr(r1)} {st} x {st} {fr(r2)}" if inside else f"x {st.replace('<', '<').replace('leqslant', 'leqslant')} {fr(r1)}".replace(
        st, "<" if st == "<" else "\\leqslant") + " \\text{ or } " + f"x {'>' if st == '<' else '\\geqslant'} {fr(r2)}"
    if r.random() < 0.5:
        # rearranged form
        shift = r.randint(-6, 6)
        lhs = poly([cs[0], cs[1], cs[2] + shift])
        q_text = f"${lhs} {op} {shift}$"
    else:
        q_text = f"${poly(cs)} {op} 0$"
    parts = [P("", f"Find the set of values of $x$ for which {q_text}", 4)]
    rows = [R("", "Rearranges to a 3-term quadratic $\\ldots 0$ and attempts to solve", "M1"),
            R("", f"Critical values $x = {fr(r1)}$ and $x = {fr(r2)}$", "A1"),
            R("", "Chooses the correct region for their critical values", "M1"),
            R("", f"${ans}$", "A1", "set notation or a correct number line diagram accepted")]
    return dict(Q(parts=parts, rows=rows, values={"critical": [r1, r2], "set": ans}, diff="4-6", cw="Find",
                  refs=["3D"]), variant="quad")


@tpl("ident.ineq", "multi-part", 22)
def ii_multi(r):
    cs, r1, r2 = _quad_ineq(r)
    if cs[0] < 0:
        cs = [-c_ for c_ in cs]
    a1, b1 = r.randint(2, 7), r.randint(-9, 9)
    a2, b2 = r.randint(-3, 1), r.randint(-9, 9)
    if a1 == a2:
        return None
    bound = sp.Rational(b2 - b1, a1 - a2)
    # a1 x + b1 < a2 x + b2 -> (a1 - a2) x < b2 - b1
    lin_sol = f"x < {fr(bound)}" if a1 > a2 else f"x > {fr(bound)}"
    # quadratic: > 0 -> outside
    quad_sol = f"x < {fr(r1)} \\text{{ or }} x > {fr(r2)}"
    # combined
    pieces = []
    lo, hi = (-sp.oo, bound) if a1 > a2 else (bound, sp.oo)
    for (u, w) in ((-sp.oo, r1), (r2, sp.oo)):
        L_, H_ = max(lo, u), min(hi, w)
        if L_ < H_:
            pieces.append((L_, H_))
    if not pieces:
        return None

    def show(p_):
        L_, H_ = p_
        if L_ == -sp.oo:
            return f"x < {fr(H_)}"
        if H_ == sp.oo:
            return f"x > {fr(L_)}"
        return f"{fr(L_)} < x < {fr(H_)}"
    comb = " \\text{ or } ".join(show(p_) for p_ in pieces)
    parts = [P("a", f"Solve the inequality ${lin(a1, b1)} < {lin(a2, b2)}$", 2),
             P("b", f"Solve the inequality ${poly(cs)} > 0$", 4),
             P("c", "Hence find the set of values of $x$ for which both inequalities are true.", 2)]
    rows = [R("a", f"${a1 - a2}x < {b2 - b1}$" if a1 > a2 else f"${a1 - a2}x < {b2 - b1}$, dividing by a negative", "M1"),
            R("a", f"${lin_sol}$", "A1"),
            R("b", "Attempts to find critical values", "M1"),
            R("b", f"$x = {fr(r1)}$, $x = {fr(r2)}$", "A1"),
            R("b", "Chooses outside region", "M1"),
            R("b", f"${quad_sol}$", "A1"),
            R("c", "Combines their answers to (a) and (b), e.g. a number line", "M1"),
            R("c", f"${comb}$", "A1", "cao")]
    return dict(Q(parts=parts, rows=rows, values={"a": lin_sol, "b": [r1, r2], "c": comb}, diff="4-6", cw="Solve",
                  refs=["3D"]), variant="combined")


# =============================================================== 3E regions & LP


def _region(r):
    """Three lines with integer intercepts bounding a triangle in the first quadrant region."""
    for _ in range(300):
        p, q = r.randint(3, 8), r.randint(3, 8)          # x/p + y/q <= 1  -> q x + p y <= pq
        m = r.choice([F(1, 2), 1, 2, F(1, 3), F(3, 2)])  # y >= m x - c? use y <= m x + c0
        c0 = r.randint(-2, 2)
        kx = r.randint(0, 2)                              # x >= kx
        # vertices of region: x >= kx, y >= m x + c0... choose y >= c1 (horizontal)
        c1 = r.randint(0, 2)
        lines = [("qx+py<=pq", q, p, p * q), ]
        # region R: x >= kx, y >= c1, q x + p y <= p q, y <= m x + c0  (m>0)
        X, Y = sp.symbols("X Y")
        cons = [(X >= kx), (Y >= c1), (q * X + p * Y <= p * q), (Y <= m * X + c0)]
        # find vertices by pairwise intersection
        eqs = [sp.Eq(X, kx), sp.Eq(Y, c1), sp.Eq(q * X + p * Y, p * q), sp.Eq(Y, sp.Rational(str(m)) * X + c0)]
        verts = []
        for i in range(4):
            for j in range(i + 1, 4):
                s_ = sp.solve([eqs[i], eqs[j]], [X, Y], dict=True)
                if not s_:
                    continue
                vx, vy = s_[0][X], s_[0][Y]
                if (vx >= kx and vy >= c1 and q * vx + p * vy <= p * q and vy <= sp.Rational(str(m)) * vx + c0):
                    if (vx, vy) not in verts:
                        verts.append((vx, vy))
        if len(verts) >= 3 and max(v_[0] for v_ in verts) <= 9 and max(v_[1] for v_ in verts) <= 9:
            area_ok = sp.Polygon(*[sp.Point(*v_) for v_ in verts]).area if len(verts) >= 3 else 0
            if area_ok and abs(area_ok) >= 2 and all(sp.Rational(c_).q == 1 for v_ in verts for c_ in v_):
                return p, q, sp.Rational(str(m)), c0, kx, c1, verts
    return None


@tpl("ident.regions", "graph", 22)
def ir_graph(r):
    res = _region(r)
    if not res:
        return None
    p, q, m, c0, kx, c1, verts = res
    X, Y = sp.symbols("x y")
    a, b = r.randint(1, 5), r.randint(1, 5)
    vals = [(a * v_[0] + b * v_[1], v_) for v_ in verts]
    best = max(vals, key=lambda t_: t_[0])
    worst = min(vals, key=lambda t_: t_[0])
    want = r.choice(["max", "min"])
    tgt = best if want == "max" else worst
    ineqs = [f"y \\geqslant {c1}", f"{lin2(q, p)} \\leqslant {p * q}", f"y \\leqslant {tex(m * X + c0)}"]
    if kx:
        ineqs.insert(0, f"x \\geqslant {kx}")
    r.shuffle(ineqs)
    grid = grid_paper((0, 10), (0, 10), 1, 1, W=380, H=380)
    parts = [P("a", "Show, by shading on the grid, the region $R$ defined by the inequalities\n\n$$" + " \\qquad ".join(ineqs) +
               "$$\n\nLabel the region $R$", 4, space="graph", figs=[fig(grid, 110, note=None)]),
             P("b", f"For all points in $R$, the {'greatest' if want == 'max' else 'least'} value of ${lin2(a, b)}$ occurs at the point $(x, y)$\n\nFind this {'greatest' if want == 'max' else 'least'} value.", 2)]
    rows = [R("a", f"Line ${lin2(q, p)} = {p * q}$ drawn correctly", "B1"),
            R("a", f"Line $y = {tex(m * X + c0)}$ drawn correctly", "B1"),
            R("a", f"Line $y = {c1}$" + (f" and $x = {kx}$" if kx else "") + " drawn correctly", "B1"),
            R("a", "Correct region identified and labelled $R$", "B1", "dep on at least two correct lines"),
            R("b", "Evaluates $" + lin2(a, b) + "$ at the vertices of their region or uses a search line", "M1"),
            R("b", f"{'Greatest' if want == 'max' else 'Least'} value ${fr(tgt[0])}$ at $({fr(tgt[1][0])}, {fr(tgt[1][1])})$", "A1")]
    return dict(Q(parts=parts, rows=rows, values={"vertices": [list(v_) for v_ in verts], "optimum": tgt[0]},
                  diff="4-6", cw="Show", refs=["3E"]), variant=want)


LP_CTX = [
    # (context, plural x, plural y, objective, currency, singular x, singular y, verb)
    ("A bakery makes $x$ trays of bread rolls and $y$ trays of pastries each morning.", "trays of bread rolls", "trays of pastries", "profit", "\\$", "tray of bread rolls", "tray of pastries", "made"),
    ("A workshop builds $x$ chairs and $y$ tables each week.", "chairs", "tables", "profit", "\\$", "chair", "table", "built"),
    ("A farmer plants $x$ hectares of maize and $y$ hectares of beans.", "hectares of maize", "hectares of beans", "income", "\\$", "hectare of maize", "hectare of beans", "planted"),
    ("A school hires $x$ small buses and $y$ large buses for a trip.", "small buses", "large buses", "number of seats", "", "small bus", "large bus", "hired"),
    ("A factory produces $x$ crates of juice and $y$ crates of water per hour.", "crates of juice", "crates of water", "profit", "\\$", "crate of juice", "crate of water", "produced"),
]


@tpl("ident.regions", "applied", 22)
def ir_lp(r):
    ctx, wx, wy, obj, cur, sx, sy, verb = r.choice(LP_CTX)
    for _ in range(200):
        a1, b1 = r.randint(1, 4), r.randint(1, 4)
        c1 = r.randint(8, 24)
        a2, b2 = r.randint(1, 4), r.randint(1, 4)
        c2 = r.randint(8, 24)
        if a1 * b2 == a2 * b1:
            continue
        mn = r.randint(1, 2)
        X, Y = sp.symbols("x y")
        cons = lambda X_, Y_: a1 * X_ + b1 * Y_ <= c1 and a2 * X_ + b2 * Y_ <= c2 and X_ >= mn and Y_ >= mn
        pts = [(i, j) for i in range(0, 25) for j in range(0, 25) if cons(i, j)]
        if len(pts) < 6:
            continue
        if max(p_[0] for p_ in pts) > 10 or max(p_[1] for p_ in pts) > 10:
            continue
        px, py = r.randint(2, 9), r.randint(2, 9)
        best = max(pts, key=lambda p_: (px * p_[0] + py * p_[1], p_[0]))
        ties = [p_ for p_ in pts if px * p_[0] + py * p_[1] == px * best[0] + py * best[1]]
        if len(ties) > 1:
            continue
        break
    else:
        return None
    val = px * best[0] + py * best[1]
    grid = grid_paper((0, 12), (0, 12), 1, 1, W=380, H=380)
    unit = lambda n: f"{n} unit{'s' if n > 1 else ''}"
    intro = (f"{ctx}\n\nThe constraints are\n\n- each {sx} uses {unit(a1)} of resource P and each {sy} uses {unit(b1)}; at most {c1} units of P are available\n"
             f"- each {sx} uses {unit(a2)} of resource Q and each {sy} uses {unit(b2)}; at most {c2} units of Q are available\n"
             f"- at least {mn} {wx if mn > 1 else sx} and at least {mn} {wy if mn > 1 else sy} must be {verb}\n\n"
             f"The {obj} is {cur}{px} for each {sx} and {cur}{py} for each {sy}.")
    parts = [P("a", "Write down the inequalities, other than those already given in terms of $x$ and $y$, that model the constraints on resources P and Q.", 2),
             P("b", "On the grid, draw straight lines and use shading to show the region $R$ that satisfies all the inequalities. Label the region $R$", 4, space="graph", figs=[fig(grid, 110, note=None)]),
             P("c", f"Given that $x$ and $y$ are integers, use your graph to find the values of $x$ and $y$ that give the greatest {obj}, and state this greatest {obj}.", 3)]
    rows = [R("a", f"${lin2(a1, b1)} \\leqslant {c1}$", "B1"),
            R("a", f"${lin2(a2, b2)} \\leqslant {c2}$", "B1"),
            R("b", f"Line ${lin2(a1, b1)} = {c1}$ drawn", "B1"),
            R("b", f"Line ${lin2(a2, b2)} = {c2}$ drawn", "B1"),
            R("b", f"Lines $x = {mn}$ and $y = {mn}$ drawn", "B1"),
            R("b", "Correct region labelled $R$", "B1"),
            R("c", f"Evaluates ${lin2(px, py)}$ at integer points near the vertices, or uses a search line", "M1"),
            R("c", f"$x = {best[0]}$, $y = {best[1]}$", "A1"),
            R("c", f"Greatest {obj} $= {cur}{val}$", "A1")]
    return dict(Q(intro=intro, parts=parts, rows=rows, values={"x": best[0], "y": best[1], "max": val}, diff="7-9",
                  cw="Find", refs=["3E"]), variant="lp")


# =============================================================== 4A sketching


def ivl(S):
    """Union of open intervals -> inequality text."""
    parts = S.args if isinstance(S, sp.Union) else [S]
    out = []
    for I in parts:
        a, b = I.start, I.end
        if a == -sp.oo:
            out.append(f"x < {fr(b)}")
        elif b == sp.oo:
            out.append(f"x > {fr(a)}")
        else:
            out.append(f"{fr(a)} < x < {fr(b)}")
    return " \\text{ or } ".join(out)


def _rational(r):
    a, b = nz(r, -4, 4), nz(r, -8, 8)
    c, d = r.choice([1, 1, 2]), nz(r, -6, 6)
    if a * d == b * c:
        return None
    return a, b, c, d


@tpl("graphs.sketch", "graph", 22)
def gs_graph(r):
    v = r.choice(["rational", "rational", "cubic"])
    if v == "rational":
        res = _rational(r)
        if not res:
            return None
        a, b, c, d = res
        va, ha = sp.Rational(-d, c), sp.Rational(a, c)
        xi, yi = sp.Rational(-b, a), sp.Rational(b, d)
        ax = Axes((float(min(va, xi, 0)) - 4, float(max(va, xi, 0)) + 4), (float(min(ha, yi, 0)) - 5, float(max(ha, yi, 0)) + 5))
        parts = [P("a", f"Sketch the curve $C$ with equation $$y = \\dfrac{{{lin(a, b)}}}{{{lin(c, d)}}}, \\quad x \\neq {fr(va)}$$\n\nShow clearly the equations of the asymptotes and the coordinates of the points where $C$ crosses the coordinate axes.", 5, space="box")]
        rows = [R("a", "Correct shape: two branches in opposite quadrants of the asymptotes", "B1"),
                R("a", f"Vertical asymptote $x = {fr(va)}$", "B1"),
                R("a", f"Horizontal asymptote $y = {fr(ha)}$", "B1"),
                R("a", f"Crosses $x$-axis at $({fr(xi)}, 0)$", "B1"),
                R("a", f"Crosses $y$-axis at $(0, {fr(yi)})$", "B1")]
        kv = r.choice([z for z in range(-4, 6) if z != ha])
        sols = sp.solve(sp.Eq((a * x + b), kv * (c * x + d)), x)
        parts.append(P("b", f"Use your sketch to explain why the equation $\\dfrac{{{lin(a, b)}}}{{{lin(c, d)}}} = {kv}$ has exactly one solution, and find it.", 2))
        rows += [R("b", f"The horizontal line $y = {kv}$ meets $C$ once (it is not the asymptote)", "B1"),
                 R("b", f"$x = {fr(sols[0])}$", "B1")]
        return dict(Q(parts=parts, rows=rows, values={"va": va, "ha": ha, "x_int": xi, "y_int": yi, "sol": sols[0]},
                      diff="4-6", cw="Sketch", refs=["4A"]), variant=v)
    rts = r.sample([-4, -3, -2, -1, 1, 2, 3, 4, 5], 2)
    rep = r.random() < 0.5
    sign = r.choice([1, -1])
    if rep:
        f = sign * (x - rts[0]) ** 2 * (x - rts[1])
        ftex = f"{'-' if sign < 0 else ''}(x {sg(-rts[0])[1:]})^2(x {sg(-rts[1])[1:]})"
    else:
        r3 = r.choice([z for z in [-3, -1, 0, 2, 6] if z not in rts])
        f = sign * (x - rts[0]) * (x - rts[1]) * (x - r3)
        ftex = f"{'-' if sign < 0 else ''}{'x' if r3 == 0 else ''}(x {sg(-rts[0])[1:]})(x {sg(-rts[1])[1:]})" + ("" if r3 == 0 else f"(x {sg(-r3)[1:]})")
    yi = f.subs(x, 0)
    parts = [P("a", f"Sketch the curve with equation $y = {ftex}$\n\nShow the coordinates of the points where the curve meets the coordinate axes.", 4, space="box"),
             P("b", f"Hence find the set of values of $x$ for which ${ftex} > 0$", 2)]
    roots = sorted(set(sp.solve(f, x)))
    sol = sp.solve_univariate_inequality(f > 0, x, relational=False)
    rows = [R("a", f"Correct cubic shape with {'positive' if sign > 0 else 'negative'} $x^3$ coefficient", "B1"),
            R("a", f"Meets $x$-axis at $x = {', '.join(fr(z) for z in roots)}$", "B1"),
            R("a", "Touches the $x$-axis at the repeated root" if rep else "Crosses the $x$-axis at three distinct points", "B1"),
            R("a", f"Meets $y$-axis at $(0, {yi})$", "B1"),
            R("b", "Uses their sketch to identify where the curve is above the $x$-axis", "M1"),
            R("b", f"${ivl(sol)}$", "A1", "accept equivalent set notation")]
    return dict(Q(parts=parts, rows=rows, values={"roots": roots, "y_int": yi, "positive": str(sol)}, diff="4-6",
                  cw="Sketch", refs=["4A", "3D"]), variant="cubic")


@tpl("graphs.sketch", "multi-part", 22)
def gs_multi(r):
    res = _rational(r)
    if not res:
        return None
    a, b, c, d = res
    va, ha = sp.Rational(-d, c), sp.Rational(a, c)
    xi, yi = sp.Rational(-b, a), sp.Rational(b, d)
    m = nz(r, -3, 3)
    for _ in range(30):
        cc = r.randint(-6, 6)
        sols = sp.solve(sp.Eq(a * x + b, (m * x + cc) * (c * x + d)), x)
        if len(sols) == 2 and all(s_.is_rational for s_ in sols):
            break
    else:
        return None
    pts = [(s_, m * s_ + cc) for s_ in sorted(sols)]
    parts = [P("a", "Write down an equation of each asymptote of $C$", 2),
             P("b", "Find the coordinates of the points where $C$ crosses the coordinate axes.", 2),
             P("c", "Sketch $C$, showing the asymptotes and the points found in part (b).", 3, space="box"),
             P("d", f"The line with equation $y = {lin(m, cc)}$ meets $C$ at two points. Find the coordinates of these points.", 5)]
    intro = f"The curve $C$ has equation $y = \\dfrac{{{lin(a, b)}}}{{{lin(c, d)}}}$, $x \\neq {fr(va)}$"
    rows = [R("a", f"$x = {fr(va)}$", "B1"), R("a", f"$y = {fr(ha)}$", "B1"),
            R("b", f"$({fr(xi)}, 0)$", "B1"), R("b", f"$(0, {fr(yi)})$", "B1"),
            R("c", "Correct shape with two branches", "B1"),
            R("c", "Asymptotes drawn and labelled", "B1", "ft their (a)"),
            R("c", "Intercepts marked", "B1", "ft their (b)"),
            R("d", f"${lin(m, cc)} = \\dfrac{{{lin(a, b)}}}{{{lin(c, d)}}}$", "M1"),
            R("d", f"${tex(sp.expand((m * x + cc) * (c * x + d) - (a * x + b)))} = 0$", "A1"),
            R("d", "Solves their quadratic", "M1"),
            R("d", f"$x = {fr(pts[0][0])}$, $x = {fr(pts[1][0])}$", "A1"),
            R("d", f"$({fr(pts[0][0])}, {fr(pts[0][1])})$ and $({fr(pts[1][0])}, {fr(pts[1][1])})$", "A1")]
    return dict(Q(intro=intro, parts=parts, rows=rows, values={"va": va, "ha": ha, "points": [list(p_) for p_ in pts]},
                  diff="7-9", cw="Sketch", refs=["4A", "3C"]), variant="rational-line")


# =============================================================== 4B graphical solution

GFUNCS = [
    ("x^2 - \\dfrac{3}{x}", lambda X: X ** 2 - 3 / X, x ** 2 - 3 / x, (0.5, 4), [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4]),
    ("2x^2 - 5x + \\dfrac{4}{x}", lambda X: 2 * X ** 2 - 5 * X + 4 / X, 2 * x ** 2 - 5 * x + 4 / x, (0.5, 4), [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4]),
    ("x^3 - 4x + 1", lambda X: X ** 3 - 4 * X + 1, x ** 3 - 4 * x + 1, (-2.5, 2.5), [-2.5, -2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2, 2.5]),
    ("2^x - 3", lambda X: 2 ** X - 3, 2 ** x - 3, (-2, 3), [-2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2, 2.5, 3]),
    ("3 - x^2 + \\dfrac{2}{x}", lambda X: 3 - X ** 2 + 2 / X, 3 - x ** 2 + 2 / x, (0.5, 3), [0.5, 0.75, 1, 1.5, 2, 2.5, 3]),
    ("x^3 - 3x^2 + 2", lambda X: X ** 3 - 3 * X ** 2 + 2, x ** 3 - 3 * x ** 2 + 2, (-1, 3), [-1, -0.5, 0, 0.5, 1, 1.5, 2, 2.5, 3]),
    ("\\mathrm{e}^{0.5x} - 2", lambda X: math.exp(0.5 * X) - 2, sp.exp(x / 2) - 2, (-2, 4), [-2, -1, 0, 1, 2, 3, 4]),
    ("x + \\dfrac{4}{x} - 3", lambda X: X + 4 / X - 3, x + 4 / x - 3, (0.5, 6), [0.5, 1, 1.5, 2, 3, 4, 5, 6]),
    ("4 - 2x^2 + \\dfrac{x^3}{2}", lambda X: 4 - 2 * X ** 2 + X ** 3 / 2, 4 - 2 * x ** 2 + x ** 3 / 2, (-1.5, 4), [-1.5, -1, 0, 1, 2, 3, 3.5, 4]),
]


def _roots_in(expr, lo, hi):
    f = sp.lambdify(x, expr, "math")
    out = []
    N = 2000
    prev = None
    for i in range(N + 1):
        X = lo + (hi - lo) * i / N
        try:
            v = f(X)
        except ZeroDivisionError:
            prev = None
            continue
        if prev is not None and prev[1] * v < 0:
            try:
                out.append(float(sp.nsolve(expr, x, (prev[0] + X) / 2)))
            except Exception:
                out.append((prev[0] + X) / 2)
        prev = (X, v)
    return out


@tpl("graphs.solve", "graph", 22)
def gsol_graph(r):
    label, f, fe, (lo, hi), xs = r.choice(GFUNCS)
    yv = [round(f(X), 1) for X in xs]
    hide = sorted(r.sample(range(len(xs)), 3))
    m = r.choice([-1, F(1, 2), 1, 2, -2])
    cc = r.randint(-2, 3)
    line = sp.Rational(str(m)) * x + cc
    g = sp.expand(fe - line)
    # multiply out denominators for the printed equation
    num, den = sp.fraction(sp.together(g))
    if den.has(x):
        mult = den
    else:
        mult = 1
    printed = sp.expand(num) if mult != 1 else g
    lcm = sp.ilcm(*[sp.Rational(c_).q for c_ in sp.Poly(printed, x).coeffs()]) if printed.is_polynomial(x) else 1
    printed = sp.expand(printed * lcm)
    rts = _roots_in(g, lo, hi)
    if not rts or len(rts) > 3:
        return None
    ymin = math.floor(min(yv + [float(line.subs(x, lo)), float(line.subs(x, hi))])) - 1
    ymax = math.ceil(max(yv + [float(line.subs(x, lo)), float(line.subs(x, hi))])) + 1
    ymin = max(ymin, math.floor(min(yv)) - 3)
    ymax = min(ymax, math.ceil(max(yv)) + 3)
    ystep = 1 if ymax - ymin <= 14 else 2
    xstep = 0.5 if hi - lo <= 4 else 1
    grid = grid_paper((math.floor(lo), math.ceil(hi)), (ymin, ymax), xstep if xstep >= 1 else 1, ystep, W=420, H=380)
    vals_txt = ["" if i in hide else dp(v, 1) for i, v in enumerate(yv)]
    parts = [P("a", f"Complete the table of values for $y = {label}$, giving your values to 1 decimal place.", 2, space="table"),
             P("b", "On the grid, plot the points from your completed table and join them to form a smooth curve.", 3,
               space="graph", figs=[fig(grid, 120, note=None)]),
             P("c", f"Add a suitable straight line to your graph and use it to estimate, to 1 decimal place, the solution{'s' if len(rts) > 1 else ''} of the equation $${tex(printed)} = 0$$ in the interval ${dp(lo, 1) if lo != int(lo) else int(lo)} \\leqslant x \\leqslant {dp(hi, 1) if hi != int(hi) else int(hi)}$", 4)]
    rows = [R("a", ", ".join(f"$x = {xs[i]}$: ${dp(yv[i], 1)}$" for i in hide), "B2", "B1 for two correct"),
            R("b", "At least 6 points plotted correctly", "B1", "ft their table"),
            R("b", "All points plotted correctly", "B1", "ft"),
            R("b", "Smooth curve through the points", "B1"),
            R("c", f"Rearranges to $y = {label}$ and $y = {tex(line)}$", "M1"),
            R("c", f"Line $y = {tex(line)}$ drawn", "A1"),
            R("c", "Reads $x$-coordinates of the intersections", "M1", "dM1"),
            R("c", ", ".join(f"$x = {dp(z, 1)}$" for z in rts), "A1", "accept $\\pm 0.1$ of each value")]
    figs = [table(["$x$"] + [str(X) for X in xs], [["$y$"] + vals_txt])]
    return dict(Q(parts=parts, rows=rows, values={"table": yv, "line": str(line), "roots": rts}, diff="7-9",
                  cw="Complete", refs=["4B"], figs=figs), variant="table-line")


@tpl("graphs.solve", "short", 22)
def gsol_short(r):
    label, f, fe, (lo, hi), xs = r.choice(GFUNCS)
    m = r.choice([-2, -1, F(1, 2), 1, 2, 3, F(3, 2)])
    cc = r.randint(-4, 4)
    line = sp.Rational(str(m)) * x + cc
    g = sp.expand(fe - line)
    num, den = sp.fraction(sp.together(g))
    printed = sp.expand(num)
    if printed.is_polynomial(x):
        lcm = sp.ilcm(*[sp.Rational(c_).q for c_ in sp.Poly(printed, x).coeffs()])
        printed = sp.expand(printed * lcm)
        sc = r.choice([1, 2, -1]) if not sp.Poly(printed, x).LC() < 0 else -1
        printed = sp.expand(printed * sc)
    # the line must actually meet the drawn curve: at least one root inside the drawn range
    if not _roots_in(g, lo, hi):
        return None
    pts = r.choice([2, 3])
    parts = [P("", f"The graph of $y = {label}$ has been drawn for ${lo} \\leqslant x \\leqslant {hi}$\n\nFind the equation of the straight line that should be drawn on the same axes in order to solve the equation $${tex(printed)} = 0$$", 3, prefix="y = ")]
    rows = [R("", f"Rearranges ${tex(printed)} = 0$ so that one side is ${label}$", "M1"),
            R("", f"${label} = {tex(line)}$", "A1", "oe"),
            R("", f"$y = {tex(line)}$", "A1", "cao")]
    return dict(Q(parts=parts, rows=rows, values={"line": str(line)}, diff="4-6", cw="Find", refs=["4B"]),
                variant="line")
