"""4PM1 templates: 10 trigonometry."""
import math

import sympy as sp

from further_maths_util import (tpl, P, R, Q, tex, sf, dp, fr, nz, fig, Axes, triangle_fig, sector_fig, solid_fig, x)

TRIPLES = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (20, 21, 29), (9, 40, 41)]


def d1(v):
    return dp(v, 1)


def sols(fn, k, b, c, lo, hi):
    """Solutions x (degrees) of fn(b x + c) = k with lo <= x <= hi (fn in sin/cos/tan)."""
    out = []
    if fn == "tan":
        base = math.degrees(math.atan(k))
        cands = [base + 180 * n for n in range(-12, 13)]
    else:
        if abs(k) > 1:
            return []
        base = math.degrees(math.asin(k) if fn == "sin" else math.acos(k))
        sec = 180 - base if fn == "sin" else -base
        cands = [b0 + 360 * n for b0 in (base, sec) for n in range(-6, 7)]
    for a in cands:
        xv = (a - c) / b
        if lo - 1e-9 <= xv <= hi + 1e-9:
            out.append(round(xv, 6))
    return sorted(set(round(v, 6) for v in out))


def ans_list(vs, k=1):
    return ", ".join(f"{dp(v, k)}^\\circ" for v in vs)


def deg_sym(e):
    return tex(e).replace("x", "\\theta")


# =============================================================== 10A radians, arcs, sectors


@tpl("trig.radians", "short", 22)
def tr_short(r):
    v = r.choice(["arc_area", "find_theta", "perimeter"])
    rad = r.randint(3, 15)
    th = sp.Rational(r.randint(3, 25), 10)
    if th >= 2 * sp.pi:
        return None
    s, A = rad * th, sp.Rational(1, 2) * rad ** 2 * th
    fg = fig(sector_fig(float(th), f"{rad} cm", f"{fmt(th)} rad" if v != "find_theta" else "θ"), 50)
    if v == "arc_area":
        parts = [P("", f"In the diagram, $OAB$ is a sector of a circle, centre $O$, of radius {rad} cm, and angle $AOB = {fmt(th)}$ radians.\n\nFind (i) the length of the arc $AB$ (ii) the area of the sector.", 4)]
        rows = [R("", f"(i) ${rad} \\times {fmt(th)}$", "M1"), R("", f"(i) ${fmt(s)}$ cm", "A1"),
                R("", f"(ii) $\\dfrac{{1}}{{2}} \\times {rad}^2 \\times {fmt(th)}$", "M1"), R("", f"(ii) ${fmt(A)}$ cm$^2$", "A1")]
        return dict(Q(figs=[fg], parts=parts, rows=rows, values={"arc": s, "area": A}, diff="1-3", cw="Find", refs=["10A"]), variant=v)
    if v == "find_theta":
        parts = [P("", f"In the diagram, $OAB$ is a sector of a circle, centre $O$, of radius {rad} cm. The area of the sector is {fmt(A)} cm$^2$\n\nFind the length of the arc $AB$", 4)]
        rows = [R("", f"$\\dfrac{{1}}{{2}} \\times {rad}^2 \\theta = {fmt(A)}$", "M1"), R("", f"$\\theta = {fmt(th)}$", "A1"),
                R("", f"$s = {rad} \\times {fmt(th)}$", "M1", "ft their $\\theta$"), R("", f"${fmt(s)}$ cm", "A1")]
        return dict(Q(figs=[fg], parts=parts, rows=rows, values={"theta": th, "arc": s}, diff="4-6", cw="Find", refs=["10A"]), variant=v)
    per = 2 * rad + s
    parts = [P("", f"The perimeter of a sector of a circle of radius {rad} cm is {fmt(per)} cm.\n\nFind the area of the sector.", 4)]
    rows = [R("", f"${2 * rad} + {rad}\\theta = {fmt(per)}$", "M1"), R("", f"$\\theta = {fmt(th)}$", "A1"),
            R("", f"$\\dfrac{{1}}{{2}} \\times {rad}^2 \\times {fmt(th)}$", "M1"), R("", f"${fmt(A)}$ cm$^2$", "A1")]
    return dict(Q(parts=parts, rows=rows, values={"theta": th, "area": A}, diff="4-6", cw="Find", refs=["10A"]), variant=v)


def fmt(v):
    v = sp.Rational(v)
    return str(v.p) if v.q == 1 else dp(v, 2).rstrip("0").rstrip(".")


@tpl("trig.radians", "multi-part", 22)
def tr_multi(r):
    rad = r.randint(4, 20)
    th = sp.Rational(r.randint(6, 25), 10)
    s = rad * th
    chord = 2 * rad * math.sin(float(th) / 2)
    seg = 0.5 * rad ** 2 * (float(th) - math.sin(float(th)))
    perseg = float(s) + chord
    fg = fig(sector_fig(float(th), f"{rad} cm", f"{fmt(th)} rad", chord=True, shade="segment"), 50)
    intro = f"In the diagram, $OAB$ is a sector of a circle, centre $O$, of radius {rad} cm, and angle $AOB = {fmt(th)}$ radians. The shaded region is bounded by the arc $AB$ and the chord $AB$"
    parts = [P("a", "Find the length of the arc $AB$", 1),
             P("b", "Find the length of the chord $AB$, giving your answer to 3 significant figures.", 2),
             P("c", "Find the perimeter of the shaded region.", 1),
             P("d", "Find the area of the shaded region, giving your answer to 3 significant figures.", 3)]
    rows = [R("a", f"${fmt(s)}$ cm", "B1"),
            R("b", f"$2 \\times {rad}\\sin {fmt(th / 2)}$ or cosine rule", "M1"), R("b", f"${sf(chord)}$ cm", "A1"),
            R("c", f"${sf(perseg)}$ cm", "B1", "ft"),
            R("d", f"Sector $= \\dfrac{{1}}{{2}}({rad})^2({fmt(th)})$", "M1"), R("d", f"Triangle $= \\dfrac{{1}}{{2}}({rad})^2\\sin {fmt(th)}$", "M1"),
            R("d", f"${sf(seg)}$ cm$^2$", "A1", "awrt")]
    return dict(Q(intro=intro, figs=[fg], parts=parts, rows=rows, values={"arc": s, "chord": chord, "perimeter": perseg, "segment": seg},
                  diff="4-6", cw="Find", refs=["10A", "10D"]), variant="segment")


@tpl("trig.radians", "show-that", 22)
def tr_show(r):
    rad = r.randint(3, 15)
    th = sp.Rational(r.randint(4, 25), 10)
    A = sp.Rational(1, 2) * rad ** 2 * th
    v = r.choice(["area", "rel"])
    if v == "area":
        per = 2 * rad + rad * th
        parts = [P("a", f"A sector of a circle has radius {rad} cm and area {fmt(A)} cm$^2$. The angle of the sector is $\\theta$ radians.\n\nShow that $\\theta = {fmt(th)}$", 2),
                 P("b", "Find the perimeter of the sector.", 2),
                 P("c", "Find the area of the triangle formed by the two radii and the chord, giving your answer to 3 significant figures.", 2)]
        tri = 0.5 * rad ** 2 * math.sin(float(th))
        rows = [R("a", f"$\\dfrac{{1}}{{2}}({rad})^2\\theta = {fmt(A)}$", "M1"), R("a", f"$\\theta = {fmt(th)}$", "A1", "cso"),
                R("b", f"${2 * rad} + {rad} \\times {fmt(th)}$", "M1"), R("b", f"${fmt(per)}$ cm", "A1"),
                R("c", f"$\\dfrac{{1}}{{2}}({rad})^2\\sin {fmt(th)}$", "M1"), R("c", f"${sf(tri)}$ cm$^2$", "A1")]
        return dict(Q(parts=parts, rows=rows, values={"theta": th, "perimeter": per, "triangle": tri}, diff="4-6", cw="Show that",
                      refs=["10A"]), variant=v)
    # perimeter = k * arc -> 2r + r th = k r th  -> th = 2/(k-1)
    k = r.choice([2, 3, 5, sp.Rational(3, 2), sp.Rational(5, 2), 4])
    th = sp.Rational(2) / (k - 1)
    if th >= 2 * sp.pi:
        return None
    A = sp.Rational(1, 2) * rad ** 2 * th
    parts = [P("a", f"The perimeter of a sector $OAB$ of a circle, centre $O$ and radius $r$ cm, is {fmt(k)} times the length of its arc. The angle $AOB$ is $\\theta$ radians.\n\nShow that $\\theta = {fr(th)}$", 3),
             P("b", f"Given that $r = {rad}$, find the area of the sector.", 2)]
    rows = [R("a", f"$2r + r\\theta = {fmt(k)}r\\theta$", "M1"), R("a", "Divides by $r$ and rearranges", "M1"),
            R("a", f"$\\theta = {fr(th)}$", "A1", "cso"),
            R("b", f"$\\dfrac{{1}}{{2}}({rad})^2 \\times {fr(th)}$", "M1"), R("b", f"${fr(A)}$ cm$^2$", "A1")]
    return dict(Q(parts=parts, rows=rows, values={"theta": th, "area": A}, diff="7-9", cw="Show that", refs=["10A"]), variant=v)


# =============================================================== 10B ratios and graphs


@tpl("trig.ratios", "short", 22)
def tq_short(r):
    a, b, h = r.choice(TRIPLES)
    if r.random() < 0.5:
        a, b = b, a
    quad = r.choice(["obtuse", "reflex3", "reflex4"])
    fn = r.choice(["sin", "cos", "tan"])
    s0, c0 = sp.Rational(a, h), sp.Rational(b, h)
    sgn = {"obtuse": (1, -1), "reflex3": (-1, -1), "reflex4": (-1, 1)}[quad]
    S, C = sgn[0] * s0, sgn[1] * c0
    Tn = S / C
    rng = {"obtuse": "90^\\circ < \\theta < 180^\\circ", "reflex3": "180^\\circ < \\theta < 270^\\circ", "reflex4": "270^\\circ < \\theta < 360^\\circ"}[quad]
    given = {"sin": S, "cos": C, "tan": Tn}[fn]
    others = [g for g in ("sin", "cos", "tan") if g != fn]
    vals = {"sin": S, "cos": C, "tan": Tn}
    parts = [P("", f"Given that $\\{fn} \\theta = {fr(given)}$ and ${rng}$, find the exact value of\n\n(i) $\\{others[0]} \\theta$\n\n(ii) $\\{others[1]} \\theta$", 4)]
    rows = [R("", "Uses a right-angled triangle or $\\sin^2\\theta + \\cos^2\\theta = 1$", "M1"),
            R("", f"Correct magnitude ${fr(abs(vals[others[0]]))}$", "A1"),
            R("", f"(i) $\\{others[0]} \\theta = {fr(vals[others[0]])}$", "A1", "correct sign for the quadrant"),
            R("", f"(ii) $\\{others[1]} \\theta = {fr(vals[others[1]])}$", "B1", "ft")]
    return dict(Q(parts=parts, rows=rows, values={others[0]: vals[others[0]], others[1]: vals[others[1]]}, diff="4-6", cw="Find",
                  refs=["10B", "10E"]), variant=quad)


@tpl("trig.ratios", "graph", 22)
def tq_graph(r):
    fn = r.choice(["sin", "cos"])
    a = r.choice([1, 2, 3, 4])
    b = r.choice([1, 2, 3])
    c = r.choice([0, 1, -1, 2])
    f = (lambda v: a * math.sin(math.radians(b * v)) + c) if fn == "sin" else (lambda v: a * math.cos(math.radians(b * v)) + c)
    ax = Axes((0, 360), (c - a - 1, c + a + 1), 380, 230)
    ax.axes(xl="x°")
    ax.curve(f)
    for xv in range(90, 361, 90):
        ax.label(xv, c - a - 1 + 0.15 if c - a - 1 < 0 else 0, str(xv), size=10)
    xmax = 90 / b if fn == "sin" else 0
    ax.hline(c + a, label=str(c + a))
    ax.hline(c - a, label=str(c - a))
    fg = fig(ax.svg(), 80)
    k = r.choice([c + a / 2, c - a / 2, c, c + a * 0.8])
    nsol = len(sols(fn, (k - c) / a, b, 0, 0, 360))
    parts = [P("a", f"The diagram shows the graph of $y = p\\{fn}(qx)^\\circ + s$ for $0 \\leqslant x \\leqslant 360$, where $p$, $q$ and $s$ are positive integers{' or zero' if c == 0 else ''}. Write down the value of $p$, the value of $q$ and the value of $s$", 3),
             P("b", f"Write down the number of solutions of the equation $p\\{fn}(qx)^\\circ + s = {fmt(k)}$ in the interval $0 \\leqslant x \\leqslant 360$", 1),
             P("c", "Write down the period of the function.", 1)]
    if c < 0:
        parts[0]["text"] = parts[0]["text"].replace("are positive integers", "are integers, with $p > 0$ and $q > 0$")
    rows = [R("a", f"$p = {a}$", "B1"), R("a", f"$q = {b}$", "B1"), R("a", f"$s = {c}$", "B1"),
            R("b", f"${nsol}$", "B1"), R("c", f"${fmt(sp.Rational(360, b))}^\\circ$", "B1")]
    del xmax
    return dict(Q(figs=[fg], parts=parts, rows=rows, values={"p": a, "q": b, "s": c, "n_solutions": nsol, "period": sp.Rational(360, b)},
                  diff="4-6", cw="Write down", refs=["10B"]), variant=fn)


# =============================================================== 10C 3D problems


@tpl("trig.3d", "applied", 22)
def t3_applied(r):
    l_, w_, h_ = r.randint(4, 15), r.randint(3, 12), r.randint(2, 10)
    V = {"A": (0, 0, 0), "B": (l_, 0, 0), "C": (l_, w_, 0), "D": (0, w_, 0), "E": (0, 0, h_), "F": (l_, 0, h_), "G": (l_, w_, h_), "H": (0, w_, h_)}
    edges = [("A", "B"), ("B", "C"), ("C", "D"), ("D", "A"), ("E", "F"), ("F", "G"), ("G", "H"), ("H", "E"), ("A", "E"), ("B", "F"), ("C", "G"), ("D", "H")]
    hidden = [("C", "D"), ("D", "A"), ("D", "H")]
    fg = fig(solid_fig(V, edges, hidden=hidden, extra_lines=[("A", "G"), ("A", "C")], dims={("A", "B"): f"{l_} cm", ("B", "C"): f"{w_} cm", ("B", "F"): f"{h_} cm"}), 60)
    AC = math.hypot(l_, w_)
    AG = math.sqrt(l_ ** 2 + w_ ** 2 + h_ ** 2)
    ang = math.degrees(math.atan(h_ / AC))
    ang2 = math.degrees(math.atan(h_ / l_))
    item = r.choice(["box", "room", "block", "container"])
    intro = f"The diagram shows a cuboid $ABCDEFGH$ representing a {item}, with $AB = {l_}$ cm, $BC = {w_}$ cm and $BF = {h_}$ cm."
    parts = [P("a", "Find the length of $AG$, giving your answer to 3 significant figures.", 3),
             P("b", "Find the size of the angle between $AG$ and the plane $ABCD$, giving your answer to 1 decimal place.", 2),
             P("c", "Find the size of the angle between the plane $ABGH$ and the plane $ABCD$, giving your answer to 1 decimal place.", 2)]
    rows = [R("a", f"$AC = \\sqrt{{{l_}^2 + {w_}^2}}$", "M1"), R("a", f"$AG = \\sqrt{{{l_}^2 + {w_}^2 + {h_}^2}}$", "M1"), R("a", f"${sf(AG)}$ cm", "A1"),
            R("b", f"$\\tan \\theta = \\dfrac{{{h_}}}{{AC}}$ oe", "M1", "identifies angle $GAC$"), R("b", f"${d1(ang)}^\\circ$", "A1"),
            R("c", f"Identifies angle $GBC$: $\\tan \\phi = \\dfrac{{{h_}}}{{{w_}}}$", "M1"), R("c", f"${d1(math.degrees(math.atan(h_ / w_)))}^\\circ$", "A1")]
    del ang2
    return dict(Q(intro=intro, figs=[fg], parts=parts, rows=rows,
                  values={"AG": AG, "angle_AG_base": ang, "angle_planes": math.degrees(math.atan(h_ / w_))}, diff="7-9", cw="Find",
                  refs=["10C"]), variant="cuboid")


@tpl("trig.3d", "multi-part", 22)
def t3_multi(r):
    s = r.randint(4, 16)
    e = r.randint(s, 2 * s)
    half_d = s / math.sqrt(2)
    if e <= half_d + 0.5:
        return None
    h = math.sqrt(e ** 2 - half_d ** 2)
    a1 = math.degrees(math.atan(h / half_d))
    a2 = math.degrees(math.atan(h / (s / 2)))
    slant = math.sqrt(e ** 2 - (s / 2) ** 2)
    a3 = math.degrees(2 * math.asin((s / 2) / e))
    V = {"A": (0, 0, 0), "B": (s, 0, 0), "C": (s, s, 0), "D": (0, s, 0), "V": (s / 2, s / 2, h)}
    edges = [("A", "B"), ("B", "C"), ("C", "D"), ("D", "A"), ("V", "A"), ("V", "B"), ("V", "C"), ("V", "D")]
    fg = fig(solid_fig(V, edges, hidden=[("C", "D"), ("D", "A"), ("V", "D")], dims={("A", "B"): f"{s} cm", ("V", "B"): f"{e} cm"}), 55)
    intro = f"The diagram shows a right pyramid $VABCD$ with a square base $ABCD$ of side {s} cm. The vertex $V$ is directly above the centre of the base, and each sloping edge has length {e} cm."
    parts = [P("a", "Find the height of the pyramid, giving your answer to 3 significant figures.", 3),
             P("b", "Find the angle between $VA$ and the base $ABCD$, giving your answer to 1 decimal place.", 2),
             P("c", "Find the angle between the face $VAB$ and the base $ABCD$, giving your answer to 1 decimal place.", 3),
             P("d", "Find the size of angle $AVB$, giving your answer to 1 decimal place.", 2)]
    rows = [R("a", f"Half-diagonal $= \\dfrac{{\\sqrt{{{s}^2 + {s}^2}}}}{{2}} = {sf(half_d)}$", "M1"), R("a", f"$h = \\sqrt{{{e}^2 - {sf(half_d, 4)}^2}}$", "M1"),
            R("a", f"${sf(h)}$ cm", "A1"),
            R("b", "$\\cos \\alpha = \\dfrac{\\text{half-diagonal}}{" + str(e) + "}$ oe", "M1"), R("b", f"${d1(a1)}^\\circ$", "A1"),
            R("c", "Identifies the angle between the line from $V$ to the midpoint of $AB$ and the base", "M1"),
            R("c", f"$\\tan \\beta = \\dfrac{{h}}{{{fmt(sp.Rational(s, 2))}}}$", "M1"), R("c", f"${d1(a2)}^\\circ$", "A1"),
            R("d", f"$\\sin \\dfrac{{\\gamma}}{{2}} = \\dfrac{{{fmt(sp.Rational(s, 2))}}}{{{e}}}$ or cosine rule", "M1"), R("d", f"${d1(a3)}^\\circ$", "A1")]
    del slant
    return dict(Q(intro=intro, figs=[fg], parts=parts, rows=rows, values={"h": h, "edge_angle": a1, "face_angle": a2, "AVB": a3},
                  diff="7-9", cw="Find", refs=["10C"]), variant="pyramid")


# =============================================================== 10D triangles


def _tri_pts(a, b, C):
    """Triangle with CA = b, CB = a, angle C (deg): returns points A, B, C."""
    Cp = (0, 0)
    Bp = (a, 0)
    Ap = (b * math.cos(math.radians(C)), b * math.sin(math.radians(C)))
    return Ap, Bp, Cp


@tpl("trig.triangles", "short", 22)
def tt_short(r):
    v = r.choice(["cosrule", "sinrule", "area", "angle"])
    a, b = r.randint(4, 20), r.randint(4, 20)
    C = r.randint(25, 140)
    c = math.sqrt(a * a + b * b - 2 * a * b * math.cos(math.radians(C)))
    A = math.degrees(math.asin(a * math.sin(math.radians(C)) / c))
    if a * a > b * b + c * c:
        A = 180 - A
    Ap, Bp, Cp = _tri_pts(a, b, C)
    if v == "cosrule":
        fg = fig(triangle_fig(Ap, Bp, Cp, sides={(1, 2): f"{a} cm", (0, 2): f"{b} cm"}, angles={2: f"{C}°"}), 50)
        parts = [P("", f"In triangle $ABC$, $BC = {a}$ cm, $AC = {b}$ cm and angle $ACB = {C}^\\circ$\n\nFind the length of $AB$, giving your answer to 3 significant figures.", 3)]
        rows = [R("", f"$AB^2 = {a}^2 + {b}^2 - 2({a})({b})\\cos {C}^\\circ$", "M1"), R("", f"$AB^2 = {sf(c * c, 5)}$", "A1"), R("", f"${sf(c)}$ cm", "A1")]
        return dict(Q(figs=[fg], parts=parts, rows=rows, values={"AB": c}, diff="1-3", cw="Find", refs=["10D"]), variant=v)
    if v == "area":
        ar = 0.5 * a * b * math.sin(math.radians(C))
        parts = [P("", f"In triangle $PQR$, $PQ = {a}$ cm, $PR = {b}$ cm and angle $QPR = {C}^\\circ$\n\nFind the area of triangle $PQR$, giving your answer to 3 significant figures.", 2)]
        rows = [R("", f"$\\dfrac{{1}}{{2}}({a})({b})\\sin {C}^\\circ$", "M1"), R("", f"${sf(ar)}$ cm$^2$", "A1")]
        return dict(Q(parts=parts, rows=rows, values={"area": ar}, diff="1-3", cw="Find", refs=["10D"]), variant=v)
    if v == "sinrule":
        cc = r.randint(5, 20)
        Ai = r.randint(25, 110)
        C = r.randint(25, 120)
        if Ai + C >= 165:
            return None
        aa = cc * math.sin(math.radians(Ai)) / math.sin(math.radians(C))
        bb = cc * math.sin(math.radians(180 - Ai - C)) / math.sin(math.radians(C))
        Cp, Bp = (0, 0), (aa, 0)
        Ap = (bb * math.cos(math.radians(C)), bb * math.sin(math.radians(C)))
        fg = fig(triangle_fig(Ap, Bp, Cp, sides={(0, 1): f"{cc} cm"}, angles={2: f"{C}°", 0: f"{Ai}°"}), 50)
        parts = [P("", f"In triangle $ABC$, $AB = {cc}$ cm, angle $ACB = {C}^\\circ$ and angle $BAC = {Ai}^\\circ$\n\nFind the length of $BC$, giving your answer to 3 significant figures.", 3)]
        rows = [R("", f"$\\dfrac{{BC}}{{\\sin {Ai}^\\circ}} = \\dfrac{{{cc}}}{{\\sin {C}^\\circ}}$", "M1 A1"), R("", f"${sf(aa)}$ cm", "A1")]
        return dict(Q(figs=[fg], parts=parts, rows=rows, values={"BC": aa}, diff="1-3", cw="Find", refs=["10D"]), variant=v)
    p_, q_, s_ = r.randint(4, 15), r.randint(4, 15), r.randint(4, 15)
    if not (p_ + q_ > s_ and p_ + s_ > q_ and q_ + s_ > p_):
        return None
    ang = math.degrees(math.acos((p_ ** 2 + q_ ** 2 - s_ ** 2) / (2 * p_ * q_)))
    parts = [P("", f"The sides of a triangle have lengths {p_} cm, {q_} cm and {s_} cm.\n\nFind the size of the angle opposite the side of length {s_} cm, giving your answer to 1 decimal place.", 3)]
    rows = [R("", f"$\\cos \\theta = \\dfrac{{{p_}^2 + {q_}^2 - {s_}^2}}{{2({p_})({q_})}}$", "M1"), R("", f"$= {fr(sp.Rational(p_ ** 2 + q_ ** 2 - s_ ** 2, 2 * p_ * q_))}$", "A1"),
            R("", f"${d1(ang)}^\\circ$", "A1")]
    return dict(Q(parts=parts, rows=rows, values={"angle": ang}, diff="4-6", cw="Find", refs=["10D"]), variant=v)


@tpl("trig.triangles", "multi-part", 22)
def tt_multi(r):
    a, b = r.randint(5, 20), r.randint(5, 20)
    C = r.randint(30, 130)
    c = math.sqrt(a * a + b * b - 2 * a * b * math.cos(math.radians(C)))
    ar = 0.5 * a * b * math.sin(math.radians(C))
    sA = a * math.sin(math.radians(C)) / c
    A = math.degrees(math.asin(min(1, sA)))
    if a * a > b * b + c * c:
        A = 180 - A
    hgt = 2 * ar / c
    Ap, Bp, Cp = _tri_pts(a, b, C)
    fg = fig(triangle_fig(Ap, Bp, Cp, sides={(1, 2): f"{a} m", (0, 2): f"{b} m"}, angles={2: f"{C}°"}), 50)
    intro = f"The diagram shows a triangular field $ABC$ with $BC = {a}$ m, $AC = {b}$ m and angle $ACB = {C}^\\circ$"
    parts = [P("a", "Find the length of $AB$, giving your answer to 3 significant figures.", 2),
             P("b", "Find the area of the field, giving your answer to 3 significant figures.", 2),
             P("c", "Find the size of angle $BAC$, giving your answer to 1 decimal place.", 2),
             P("d", "Find the shortest distance from $C$ to $AB$, giving your answer to 3 significant figures.", 2)]
    rows = [R("a", f"$AB^2 = {a}^2 + {b}^2 - 2({a})({b})\\cos {C}^\\circ$", "M1"), R("a", f"${sf(c)}$ m", "A1"),
            R("b", f"$\\dfrac{{1}}{{2}}({a})({b})\\sin {C}^\\circ$", "M1"), R("b", f"${sf(ar)}$ m$^2$", "A1"),
            R("c", f"$\\dfrac{{\\sin A}}{{{a}}} = \\dfrac{{\\sin {C}^\\circ}}{{{sf(c, 4)}}}$ or cosine rule", "M1"), R("c", f"${d1(A)}^\\circ$", "A1", "check for obtuse angle"),
            R("d", "$\\dfrac{2 \\times \\text{area}}{AB}$ or $AC \\sin A$", "M1"), R("d", f"${sf(hgt)}$ m", "A1")]
    return dict(Q(intro=intro, figs=[fg], parts=parts, rows=rows, values={"AB": c, "area": ar, "BAC": A, "distance": hgt}, diff="4-6",
                  cw="Find", refs=["10D"]), variant="field")


# =============================================================== 10E-10G identities

th = sp.Symbol("theta")


def _ident(r):
    a, b = r.sample([2, 3, 4, 5, 6, 7], 2)
    opts = [
        ("lin", f"{a}\\sin^2\\theta + {b}\\cos^2\\theta \\equiv {b} {'+' if a > b else '-'} {abs(a - b) if abs(a - b) != 1 else ''}\\sin^2\\theta",
         a * sp.sin(th) ** 2 + b * sp.cos(th) ** 2, b + (a - b) * sp.sin(th) ** 2,
         ["Uses $\\cos^2\\theta = 1 - \\sin^2\\theta$", "Collects terms to reach the given result"]),
        ("tan", "\\tan\\theta + \\dfrac{1}{\\tan\\theta} \\equiv \\dfrac{1}{\\sin\\theta\\cos\\theta}",
         sp.tan(th) + 1 / sp.tan(th), 1 / (sp.sin(th) * sp.cos(th)),
         ["Writes $\\tan\\theta = \\dfrac{\\sin\\theta}{\\cos\\theta}$ and combines over a common denominator", "Uses $\\sin^2\\theta + \\cos^2\\theta = 1$"]),
        ("sq", "(\\sin\\theta + \\cos\\theta)^2 + (\\sin\\theta - \\cos\\theta)^2 \\equiv 2",
         (sp.sin(th) + sp.cos(th)) ** 2 + (sp.sin(th) - sp.cos(th)) ** 2, sp.Integer(2),
         ["Expands both brackets", "Cross terms cancel and uses $\\sin^2\\theta + \\cos^2\\theta = 1$"]),
        ("frac", "\\dfrac{1 - \\cos^2\\theta}{\\sin\\theta\\cos\\theta} \\equiv \\tan\\theta",
         (1 - sp.cos(th) ** 2) / (sp.sin(th) * sp.cos(th)), sp.tan(th),
         ["Replaces $1 - \\cos^2\\theta$ by $\\sin^2\\theta$", "Cancels and uses $\\dfrac{\\sin\\theta}{\\cos\\theta} = \\tan\\theta$"]),
        ("add", "\\sin(\\theta + 30^\\circ) + \\sin(\\theta - 30^\\circ) \\equiv \\sqrt{3}\\sin\\theta",
         sp.sin(th + sp.pi / 6) + sp.sin(th - sp.pi / 6), sp.sqrt(3) * sp.sin(th),
         ["Expands both using the addition formulae", "Uses $\\cos 30^\\circ = \\dfrac{\\sqrt{3}}{2}$ and the $\\cos\\theta\\sin 30^\\circ$ terms cancel"]),
        ("dbl", "\\dfrac{\\sin 2\\theta}{1 + \\cos 2\\theta} \\equiv \\tan\\theta",
         sp.sin(2 * th) / (1 + sp.cos(2 * th)), sp.tan(th),
         ["Uses $\\sin 2\\theta = 2\\sin\\theta\\cos\\theta$", "Uses $\\cos 2\\theta = 2\\cos^2\\theta - 1$ and cancels"]),
    ]
    return r.choice(opts)


@tpl("trig.identities", "show-that", 22)
def ti_show(r):
    key, stmt, lhs, rhs, steps = _ident(r)
    assert sp.simplify(sp.expand_trig(lhs - rhs)) == 0
    parts = [P("a", f"Show that $${stmt}$$", 3)]
    rows = [R("a", steps[0], "M1"), R("a", steps[1], "M1"), R("a", "Fully correct proof with no errors", "A1", "cso")]
    vals = {"identity": key}
    if key == "lin":
        a = int(lhs.coeff(sp.sin(th) ** 2)) if False else None
        b_ = rhs.subs(sp.sin(th), 0)
        coef = sp.expand(rhs - b_).coeff(sp.sin(th) ** 2)
        s2 = r.choice([sp.Rational(1, 4), sp.Rational(3, 4), sp.Rational(1, 2)])
        k = b_ + coef * s2
        xs = sols("sin", float(sp.sqrt(s2)), 1, 0, 0, 360) + sols("sin", -float(sp.sqrt(s2)), 1, 0, 0, 360)
        lhs_t = stmt.split("\\equiv")[0].replace("\\theta", "x")
        parts.append(P("b", f"Hence solve, for $0 \\leqslant x \\leqslant 360^\\circ$, the equation ${lhs_t}= {fmt(k)}$", 4))
        rows += [R("b", f"$\\sin^2 x = {fr(s2)}$", "M1 A1"), R("b", f"$\\sin x = \\pm {tex(sp.sqrt(s2))}$", "M1"),
                 R("b", f"$x = {ans_list(sorted(xs), 0)}$", "A1", "all four, no extras in range")]
        vals["x"] = sorted(xs)
        del a
    elif key in ("frac", "dbl", "tan"):
        k = r.choice([2, 3, sp.Rational(1, 2), -1, sp.Rational(-3, 4)])
        if key == "tan":
            # 1/(sin cos) = k -> sin 2x = 2/k
            if abs(2 / k) > 1:
                return None
            xs = sols("sin", float(2 / k), 2, 0, 0, 180)
            parts.append(P("b", f"Hence solve, for $0 < \\theta < 180^\\circ$, the equation $\\tan\\theta + \\dfrac{{1}}{{\\tan\\theta}} = {fr(k)}$, giving your answers to 1 decimal place.", 2 + len(xs)))
            rows += [R("b", f"$\\sin\\theta\\cos\\theta = {fr(1 / k)}$", "M1"), R("b", f"$\\sin 2\\theta = {fr(2 / k)}$", "M1"),
                     R("b", f"$\\theta = {ans_list(xs)}$", " ".join(["A1"] * len(xs)), "A1 for each" if len(xs) > 1 else None)]
        else:
            xs = sols("tan", float(k), 1, 0, 0, 360)
            xs = [v for v in xs if abs(v % 180 - 90) > 1e-6]
            parts.append(P("b", f"Hence solve, for $0 \\leqslant \\theta < 360^\\circ$, the equation ${stmt.split(chr(92) + 'equiv')[0]}= {fr(k)}$, giving your answers to 1 decimal place.", 3))
            rows += [R("b", f"$\\tan\\theta = {fr(k)}$", "M1"), R("b", f"$\\theta = {ans_list(xs)}$", "A1 A1", "A1 for each")]
        vals["theta"] = xs
    elif key == "add":
        k = r.choice([1, sp.Rational(1, 2), sp.Rational(3, 2), -1])
        sv = float(k / sp.sqrt(3))
        xs = sols("sin", sv, 1, 0, 0, 360)
        parts.append(P("b", f"Hence solve, for $0 \\leqslant \\theta < 360^\\circ$, $\\sin(\\theta + 30^\\circ) + \\sin(\\theta - 30^\\circ) = {fr(k)}$, giving your answers to 1 decimal place.", 3))
        rows += [R("b", f"$\\sin\\theta = \\dfrac{{{fr(k)}}}{{\\sqrt{{3}}}}$", "M1"), R("b", f"$\\theta = {ans_list(xs)}$", "A1 A1")]
        vals["theta"] = xs
    else:
        parts.append(P("b", "Hence, or otherwise, find the value of $(\\sin 15^\\circ + \\cos 15^\\circ)^2 + (\\sin 15^\\circ - \\cos 15^\\circ)^2$", 1))
        rows.append(R("b", "$2$", "B1"))
    return dict(Q(parts=parts, rows=rows, values=vals, diff="7-9", cw="Show that", refs=["10E", "10F", "10G", "10H"]), variant=key)


@tpl("trig.identities", "short", 22)
def ti_short(r):
    (a1, b1, h1), (a2, b2, h2) = r.sample(TRIPLES[:4], 2)
    sA, cA = sp.Rational(a1, h1), sp.Rational(b1, h1)
    sB, cB = sp.Rational(a2, h2), sp.Rational(b2, h2)
    v = r.choice(["sum", "diff", "tan", "double"])
    giv = f"Given that $\\sin A = {fr(sA)}$ and $\\cos B = {fr(cB)}$, where $A$ and $B$ are both acute angles,"
    if v == "sum":
        val, tgt = sA * cB + cA * sB, "\\sin(A + B)"
    elif v == "diff":
        val, tgt = cA * cB + sA * sB, "\\cos(A - B)"
    elif v == "tan":
        tA, tB = sA / cA, sB / cB
        val, tgt = (tA + tB) / (1 - tA * tB), "\\tan(A + B)"
        if tA * tB == 1:
            return None
    else:
        val, tgt = 2 * sA * cA, "\\sin 2A"
        giv = f"Given that $\\sin A = {fr(sA)}$, where $A$ is acute,"
    parts = [P("", f"{giv} find the exact value of ${tgt}$", 3 if v != "double" else 2)]
    rows = ([R("", f"$\\cos A = {fr(cA)}$" + ("" if v == "double" else f", $\\sin B = {fr(sB)}$"), "B1")] +
            ([R("", "Correct addition formula with their values", "M1")] if v != "double" else []) +
            [R("", f"${tgt} = {fr(val)}$", "A1" if v != "double" else "B1")])
    if v == "double":
        rows = [R("", f"$\\cos A = {fr(cA)}$ and uses $\\sin 2A = 2\\sin A\\cos A$", "M1"), R("", f"${fr(val)}$", "A1")]
    return dict(Q(parts=parts, rows=rows, values={"value": val}, diff="4-6", cw="Find", refs=["10F", "10G"]), variant=v)


# =============================================================== 10H equations


@tpl("trig.equations", "short", 22)
def te_short(r):
    fn = r.choice(["sin", "cos", "tan"])
    b = r.choice([1, 2, 3, 1])
    c = r.choice([0, 20, 30, 45, -40, 60, -15])
    k = sp.Rational(r.randint(-9, 9), 10) if fn != "tan" else sp.Rational(r.randint(-30, 30), 10)
    if k == 0:
        return None
    A = r.choice([1, 2, 3, 4, 5])
    kk = k * A
    xs = sols(fn, float(k), b, c, 0, 360)
    if not xs or len(xs) > 6:
        return None
    arg = tex(b * sp.Symbol("x") + c).replace("x", "x^\\circ") if False else (f"{b if b > 1 else ''}x" + (f" + {c}" if c > 0 else f" - {-c}" if c < 0 else ""))
    lhs = f"{A if A > 1 else ''}\\{fn}({arg})^\\circ" if (b > 1 or c) else f"{A if A > 1 else ''}\\{fn} x^\\circ"
    parts = [P("", f"Solve, for $0 \\leqslant x \\leqslant 360$, the equation $${lhs} = {fmt(kk)}$$\n\nGive your answers to 1 decimal place.", 3 + (1 if len(xs) > 2 else 0))]
    rows = [R("", f"$\\{fn}({arg}) = {fmt(k)}$ and finds a principal value", "M1"),
            R("", "Uses the symmetry of the graph" + (" and the extended range for the argument" if b > 1 or c else ""), "M1"),
            R("", f"$x = {ans_list(xs)}$", "A1" if len(xs) <= 2 else "A1 A1", "all values, no extras in range")]
    return dict(Q(parts=parts, rows=rows, values={"x": xs}, diff="4-6" if b > 1 or c else "1-3", cw="Solve", refs=["10H"]), variant=fn)


@tpl("trig.equations", "multi-part", 22)
def te_multi(r):
    fn = r.choice(["sin", "cos"])
    other = "cos" if fn == "sin" else "sin"
    s1 = r.choice([sp.Rational(1, 2), sp.Rational(-1, 2), sp.Rational(1, 3), sp.Rational(-1, 4), sp.Rational(3, 4), sp.Rational(2, 3), sp.Rational(-2, 5)])
    s2 = r.choice([2, -2, 3, -3, sp.Rational(3, 2), sp.Rational(-5, 3)])
    A = sp.lcm(s1.q, sp.Rational(s2).q) * r.choice([1, 2])
    S = sp.Symbol("s")
    poly = sp.expand(A * (S - s1) * (S - s2))
    a2, a1, a0 = [poly.coeff(S, j) for j in (2, 1, 0)]
    # present with other^2: a2 s^2 = a2 - a2 o^2
    pa2, pa1, pa0 = -a2, a1, a0 + a2
    def tq(c2, f2, c1, f1, c0):
        out = ""
        for c, mon in ((c2, f"\\{f2}^2 x"), (c1, f"\\{f1} x"), (c0, "")):
            c = sp.Rational(c)
            if c == 0:
                continue
            mag = fr(abs(c)) if (abs(c) != 1 or not mon) else ""
            term = f"{mag}{mon}"
            out += (("-" if c < 0 else "") + term) if not out else ((" - " if c < 0 else " + ") + term)
        return out
    shown = tq(pa2, other, pa1, fn, pa0)
    target = tq(a2, fn, a1, fn, a0)
    fac = f"({tq(0, fn, 1, fn, -s1 * 1) if s1.q == 1 else tq(0, fn, s1.q, fn, -s1.p)})({tq(0, fn, 1, fn, -sp.Rational(s2)) if sp.Rational(s2).q == 1 else tq(0, fn, sp.Rational(s2).q, fn, -sp.Rational(s2).p)})"
    xs = sols(fn, float(s1), 1, 0, 0, 360)
    parts = [P("a", f"Show that the equation $${shown} = 0$$ can be written as $${target} = 0$$", 2),
             P("b", "Hence solve, for $0 \\leqslant x < 360^\\circ$, the equation in part (a). Give your answers to 1 decimal place.", 4)]
    rows = [R("a", f"Uses $\\{other}^2 x = 1 - \\{fn}^2 x$", "M1"), R("a", "Correct rearrangement to the given equation", "A1", "cso"),
            R("b", f"Factorises or solves: ${fac} = 0$", "M1"),
            R("b", f"$\\{fn} x = {fr(s1)}$ (and $\\{fn} x = {fr(s2)}$ rejected as $|\\{fn} x| \\leqslant 1$)", "A1"),
            R("b", f"$x = {ans_list(xs)}$", "A1 A1", "A1 for each correct value; deduct for extras in range")]
    return dict(Q(parts=parts, rows=rows, values={"root": s1, "rejected": s2, "x": xs}, diff="7-9", cw="Show that",
                  refs=["10E", "10H", "2A"]), variant=fn)
