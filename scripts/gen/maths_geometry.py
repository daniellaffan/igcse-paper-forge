"""Geometry templates, part 1: angles, measures, constructions, circle theorems,
trigonometry (right-angled, sine/cosine rules, 3D).  Spec sections 4.1-4.8."""
import math
from fractions import Fraction as F

from maths_util import (tpl, P, R, Q, sf, dp, num, ftex, name, fig, table, polygon_fig, circle_fig, angle_mark,
                        right_mark, Frame, svg, PL, L, T, DOT, ARC, ARROW, C, cuboid_fig, NOT_ACC, big)

LET = ["ABC", "PQR", "XYZ", "DEF", "LMN", "KLM", "RST", "EFG", "UVW"]
POLY = {3: "triangle", 4: "quadrilateral", 5: "pentagon", 6: "hexagon", 7: "heptagon", 8: "octagon", 9: "nonagon",
        10: "decagon", 12: "dodecagon"}
DEG = "^\\circ"


def deg(x):
    """angle value as text, integer if whole."""
    return num(F(x)) if isinstance(x, (int, F)) else dp(x, 1)


def tick(p, q, k=1):
    """equal-length tick marks on screen segment p-q."""
    mx, my = (p[0] + q[0]) / 2, (p[1] + q[1]) / 2
    dx, dy = q[0] - p[0], q[1] - p[1]
    d = math.hypot(dx, dy) or 1
    ux, uy = dx / d, dy / d
    nx, ny = -uy, ux
    out = ""
    for i in range(k):
        o = (i - (k - 1) / 2) * 4
        cx, cy = mx + o * ux, my + o * uy
        out += L(cx - 5 * nx, cy - 5 * ny, cx + 5 * nx, cy + 5 * ny, w=1)
    return out


def par_arrow(p, q, k=1):
    mx, my = (p[0] + q[0]) / 2, (p[1] + q[1]) / 2
    dx, dy = q[0] - p[0], q[1] - p[1]
    d = math.hypot(dx, dy) or 1
    ux, uy = dx / d, dy / d
    out = ""
    for i in range(k):
        cx, cy = mx + i * 6 * ux, my + i * 6 * uy
        out += PL([(cx - 6 * ux - 4 * uy, cy - 6 * uy + 4 * ux), (cx, cy), (cx - 6 * ux + 4 * uy, cy - 6 * uy - 4 * ux)], w=1.2)
    return out


def tri_from_sides(a, b, c):
    """A=(0,0), B=(c,0), C above AB.  a=BC, b=CA, c=AB."""
    cosA = (b * b + c * c - a * a) / (2 * b * c)
    cosA = max(-1, min(1, cosA))
    A_ = math.acos(cosA)
    return [(0, 0), (c, 0), (b * math.cos(A_), b * math.sin(A_))]


def lab_len(v, unit="cm"):
    return f"{num(v) if not isinstance(v, float) else sf(v, 3)} {unit}"


# ================================================================ 4.1 angles
REG_N = [5, 6, 8, 9, 10, 12, 15, 18, 20, 24, 30, 36, 40, 45, 60, 72]


@tpl("geometry.angles", "short", n=10)
def polygon_angles(r):
    n = r.choice(REG_N)
    ext = F(360, n)
    I = 180 - ext
    kind = r.choice(["int", "sides_ext", "sides_int", "sum"])
    if kind == "int":
        return Q(parts=[P("", f"Work out the size of each interior angle of a regular polygon with {n} sides.", 2, prefix="")],
                 rows=[R("", f"$360 \\div {n} = {deg(ext)}$ or $({n} - 2) \\times 180 = {(n - 2) * 180}$", "M1", ""),
                       R("", f"${deg(I)}{DEG}$", "A1", "cao")],
                 values={"interior": I}, diff="4-6", cw="Work out", refs=["F4.2D"])
    if kind == "sides_ext":
        return Q(parts=[P("", f"Each exterior angle of a regular polygon is ${deg(ext)}{DEG}$.\n\nWork out the number of sides of the polygon.", 2, prefix="")],
                 rows=[R("", f"$360 \\div {deg(ext)}$", "M1", ""), R("", str(n), "A1", "cao")],
                 values={"n": n}, diff="4-6", cw="Work out", refs=["F4.2D"])
    if kind == "sides_int":
        return Q(parts=[P("", f"Each interior angle of a regular polygon is ${deg(I)}{DEG}$.\n\nWork out the number of sides of the polygon.", 3, prefix="")],
                 rows=[R("", f"$180 - {deg(I)} = {deg(ext)}$", "M1", "for the exterior angle, or for $180(n - 2) = " + deg(I) + "n$"),
                       R("", f"$360 \\div {deg(ext)}$", "M1", "or for a correct rearrangement of their equation"),
                       R("", str(n), "A1", "cao")],
                 values={"n": n}, diff="4-6", cw="Work out", refs=["F4.2D"])
    m = r.choice([5, 6, 7, 8, 9, 10, 12])
    ang = [r.randint(95, 170) for _ in range(m - 1)]
    last = (m - 2) * 180 - sum(ang)
    if not 60 <= last <= 175:
        return None
    return Q(intro=f"A {POLY[m]} has {m} interior angles.\n\n{m - 1} of the angles are ${', '.join(map(str, ang))}{DEG}$.",
             parts=[P("", "Work out the size of the other interior angle.", 2, prefix="")],
             rows=[R("", f"$({m} - 2) \\times 180 = {(m - 2) * 180}$", "M1", "for the angle sum"),
                   R("", f"${last}{DEG}$", "A1", "cao")],
             values={"angle": last}, diff="4-6", cw="Work out", refs=["F4.2E"])


@tpl("geometry.angles", "short", n=10)
def isos_exterior(r):
    a = r.randrange(24, 140, 2)
    base = F(180 - a, 2)
    nm = r.choice(LET)
    A, B, C_ = nm
    h = math.tan(math.radians(float(base))) * 1.0
    pts = [(0, h), (-1, 0), (1, 0)]
    extD = (1.9, 0)
    ask = r.choice(["ext", "base"])
    D = "D" if "D" not in nm else "W"

    def extra(fr):
        S = [fr(p) for p in pts]
        Ds = fr(extD)
        out = L(*S[2], *Ds) + tick(S[0], S[1]) + tick(S[0], S[2]) + T(Ds[0] + 10, Ds[1] + 4, D)
        out += angle_mark(S[2], S[0], Ds, "x", r=18)
        return out
    svgs = polygon_fig(pts, names=[A, B, C_], angles={0: f"{a}°"}, extra={"pts": [extD], "body": extra}, w=300, h=200)
    if ask == "ext":
        ans = 180 - base
        rows = [R("", f"$(180 - {a}) \\div 2 = {deg(base)}$", "M1", f"for angle ${A}{C_}{B} = {deg(base)}$ or angle ${A}{B}{C_} = {deg(base)}$"),
                R("", f"${deg(ans)}$", "A1", "cao")]
    else:
        ans = 180 - base
        rows = [R("", f"angle ${A}{C_}{B} = (180 - {a}) \\div 2$", "M1", "or $x = " + f"{a} + " + "$ base angle (exterior angle of a triangle)"),
                R("", f"${deg(ans)}$", "A1", "cao")]
    return Q(intro=f"${A}{B}{C_}$ is an isosceles triangle with ${A}{B} = {A}{C_}$.\n\n${B}{C_}{D}$ is a straight line.",
             figs=[fig(svgs, 70)],
             parts=[P("", "Find the size of angle $x$.", 2, prefix="$x =$")],
             rows=rows, values={"x": ans}, diff="4-6", cw="Work out", refs=["F4.1C", "F4.1D"])


def poly_from_angles(r, ints, tries=200):
    n = len(ints)
    for _ in range(tries):
        th = [0.0]
        for i in range(1, n):
            th.append(th[-1] + math.radians(180 - float(ints[i])))
        ls = [r.uniform(0.8, 1.6) for _ in range(n - 2)]
        sx = sum(l * math.cos(t) for l, t in zip(ls, th))
        sy = sum(l * math.sin(t) for l, t in zip(ls, th))
        a1, a2 = th[n - 2], th[n - 1]
        c1, s1, c2, s2 = math.cos(a1), math.sin(a1), math.cos(a2), math.sin(a2)
        det = c1 * s2 - c2 * s1
        if abs(det) < 1e-6:
            continue
        l1 = (-sx * s2 + sy * c2) / det
        l2 = (-c1 * sy + s1 * sx) / det
        if 0.6 < l1 < 2.0 and 0.6 < l2 < 2.0:
            ls += [l1, l2]
            pts = [(0.0, 0.0)]
            for l, t in zip(ls[:-1], th[:-1]):
                pts.append((pts[-1][0] + l * math.cos(t), pts[-1][1] + l * math.sin(t)))
            # vertex order: edge i goes V_i -> V_{i+1}; interior angle i at V_i requires shift
            return pts
    return None


@tpl("geometry.angles", "problem", n=10)
def polygon_algebra(r):
    n = r.choice([4, 5, 5, 6])
    S = (n - 2) * 180
    xv = r.randint(12, 40)
    for _ in range(50):
        cs = [r.choice([1, 2, 3, 4]) for _ in range(n)]
        ks = [r.randrange(-30, 60, 5) for _ in range(n - 1)]
        kl = S - sum(c * xv for c in cs) - sum(ks)
        ks.append(kl)
        angs = [c * xv + k for c, k in zip(cs, ks)]
        if all(70 <= a <= 170 for a in angs) and -60 <= kl <= 90 and kl % 5 == 0:
            break
    else:
        return None
    if len(set(angs)) < n:
        return None
    # angle i is at vertex i: interior angle at V_i is between edges (i-1) and i, so rotate
    pts = poly_from_angles(r, angs[1:] + angs[:1])
    if pts is None:
        return None
    pts = pts[-1:] + pts[:-1]

    def lab(c, k):
        s = ("" if c == 1 else str(c)) + "x"
        return s + (f" + {k}" if k > 0 else (f" − {-k}" if k < 0 else "")) + "°"
    labels = {i: lab(c, k) for i, (c, k) in enumerate(zip(cs, ks))}
    names = list("ABCDEF"[:n])
    svgs = polygon_fig(pts, names=names, angles=labels, w=320, h=240)
    big_ = max(angs)
    expr = " + ".join(f"({lab(c, k)[:-1].replace('−', '-')})" for c, k in zip(cs, ks))
    return Q(intro=f"The diagram shows a {POLY[n]}.\n\nAll the angles are measured in degrees.", figs=[fig(svgs, 75)],
             parts=[P("", f"Work out the size of the largest angle of the {POLY[n]}.", 4, prefix="")],
             rows=[R("", f"$({n} - 2) \\times 180 = {S}$", "M1", "for the sum of the interior angles"),
                   R("", f"${expr} = {S}$", "M1", f"for a correct equation, eg ${sum(cs)}x + {sum(ks)} = {S}$".replace("+ -", "- ")),
                   R("", f"$x = {xv}$", "A1", ""),
                   R("", f"${big_}{DEG}$", "A1", "cao")],
             values={"x": xv, "largest": big_}, diff="7-9", cw="Work out", refs=["F4.2E", "F4.2B"])


TILINGS = [(3, 7, 42), (3, 8, 24), (3, 9, 18), (3, 10, 15), (3, 12, 12), (4, 5, 20), (4, 6, 12), (4, 8, 8),
           (5, 5, 10), (6, 6, 6), (3, 3, 6)]


def int_ang(n):
    return 180 - F(360, n)


@tpl("geometry.angles", "problem", n=10)
def regular_meet(r):
    kind = r.choice(["meet", "ratio", "ratio"])
    if kind == "meet":
        t = list(r.choice(TILINGS))
        r.shuffle(t)
        a, b, c = t
        nm = lambda k: f"a regular {POLY[k]}" if k in POLY else f"a regular polygon with {k} sides"
        if a == b:
            return None
        rest = 360 - int_ang(a) - int_ang(b)
        return Q(intro=f"Three regular polygons fit together at a point, with no gaps and no overlaps.\n\nOne of the polygons is {nm(a)}. Another is {nm(b)}.",
                 parts=[P("", "Work out the number of sides of the third polygon.", 4, prefix="")],
                 rows=[R("", f"interior angle ${deg(int_ang(a))}$ or ${deg(int_ang(b))}$", "M1", "for one correct interior angle"),
                       R("", f"$360 - {deg(int_ang(a))} - {deg(int_ang(b))} = {deg(rest)}$", "M1", "for the third interior angle"),
                       R("", f"$360 \\div (180 - {deg(rest)})$", "M1", "or $180(n-2) = " + deg(rest) + "n$"),
                       R("", str(c), "A1", "cao")],
                 values={"n": c}, diff="7-9", cw="Work out", refs=["F4.2D", "F4.1B"])
    k = r.choice([2, 3, 4, 5, 7, 8, 9, 11, 14, F(1, 2), F(3, 2), F(5, 2), F(7, 2)])
    n = 2 * (k + 1)
    if F(n).denominator != 1:
        return None
    word = {F(1, 2): "half", F(3, 2): "one and a half times", F(5, 2): "two and a half times",
            F(7, 2): "three and a half times"}.get(F(k), f"{k} times")
    phr = f"is {word}" if word != "half" else "is half"
    return Q(parts=[P("", f"The size of each interior angle of a regular polygon {phr} the size of each exterior angle.\n\nWork out the number of sides of the polygon.", 3, prefix="")],
             rows=[R("", f"$e + {ftex(k)}e = 180$", "M1", "for a correct equation in the exterior (or interior) angle"),
                   R("", f"$e = {deg(F(180) / (1 + F(k)))}$ and $360 \\div {deg(F(180) / (1 + F(k)))}$", "M1", ""),
                   R("", str(int(n)), "A1", "cao")],
             values={"n": int(n)}, diff="7-9", cw="Work out", refs=["F4.2D"])


REASONS = {"alt": "alternate angles are equal", "line": "angles on a straight line sum to $180^\\circ$",
           "tri": "angles in a triangle sum to $180^\\circ$", "co": "co-interior angles sum to $180^\\circ$",
           "corr": "corresponding angles are equal", "vert": "vertically opposite angles are equal",
           "iso": "base angles of an isosceles triangle are equal", "ext": "exterior angles of a polygon sum to $360^\\circ$",
           "poly": "interior angles of a polygon with $n$ sides add up to $(n-2) \\times 180^\\circ$"}


@tpl("geometry.angles", "proof", n=10)
def parallel_triangle(r):
    p = r.randint(28, 78)
    q = r.randint(max(100, p + 35), 160)
    xv = q - p
    h = 1.0
    ex = 0.0
    fx = ex - h / math.tan(math.radians(p))
    gx = ex + h / math.tan(math.radians(180 - q))
    E, Fp, G = (ex, h), (fx, 0), (gx, 0)
    Al, Br = (fx - 0.6, h), (gx + 0.8, h)
    Cl, Dr = (fx - 0.6, 0), (gx + 0.8, 0)
    pts = [Al, Br, Cl, Dr]
    fr = Frame(pts + [(fx, -0.2), (ex, h + 0.2)], 330, 200)
    s = {k: fr(v) for k, v in dict(E=E, F=Fp, G=G, A=Al, B=Br, C=Cl, D=Dr).items()}
    b = L(*s["A"], *s["B"]) + L(*s["C"], *s["D"]) + L(*s["E"], *s["F"]) + L(*s["E"], *s["G"])
    b += par_arrow(s["A"], s["B"]) + par_arrow(s["C"], s["D"])
    for k, off in dict(A=(-10, 0), B=(10, 0), C=(-10, 0), D=(10, 0), E=(0, -11), F=(0, 13), G=(0, 13)).items():
        b += T(s[k][0] + off[0], s[k][1] + off[1], k)
    b += angle_mark(s["E"], s["A"], s["F"], f"{p}°", r=20)
    b += angle_mark(s["G"], s["E"], s["D"], f"{q}°", r=18)
    b += angle_mark(s["E"], s["F"], s["G"], "x", r=26)
    return Q(intro="$AB$ is parallel to $CD$.\n\n$EFG$ is a triangle with $E$ on $AB$ and $F$ and $G$ on $CD$.",
             figs=[fig(svg(fr.w, fr.h, b), 80)],
             parts=[P("", "Find the size of angle $x$.\n\nGive reasons for each step of your working.", 4, prefix="$x =$")],
             rows=[R("", f"angle $EFG = {p}$ or angle $EGF = 180 - {q} = {180 - q}$", "M1", "may be marked on the diagram"),
                   R("", f"${xv}$", "A1", f"for $x = {xv}$; alternative: angle $BEG = {180 - q}$ (co-interior) then $180 - {p} - {180 - q}$"),
                   R("", f"one correct reason, eg {REASONS['alt']}", "B1", "dep on M1"),
                   R("", f"all reasons correct for their method, eg {REASONS['alt']}, {REASONS['line']}, {REASONS['tri']}", "B1",
                     "dep on M1; reasons must be given in full, not abbreviated")],
             values={"x": xv}, diff="7-9", cw="Work out", refs=["F4.1B", "F4.1C", "H4.7A"])


@tpl("geometry.angles", "proof", n=10)
def polygon_diag_reasons(r):
    n = r.choice([5, 6, 8, 9, 10, 12, 15, 18, 20])
    I = int_ang(n)
    small = F(180, n)
    ask = r.choice(["ACD", "BAC", "ACD"])
    vs = [(math.cos(math.radians(-90 - 180 / n + 360 * k / n)), math.sin(math.radians(-90 - 180 / n + 360 * k / n))) for k in range(n)]
    pts = vs[:min(n, 6)] if n > 6 else vs
    names = list("ABCDEF"[:len(pts)])
    closed = n <= 6

    def extra(fr):
        S = [fr(p) for p in pts]
        out = L(*S[0], *S[2])
        if ask == "ACD":
            out += angle_mark(S[2], S[0], S[3], "x", r=22)
        else:
            out += angle_mark(S[0], S[1], S[2], "x", r=26)
        return out
    svgs = polygon_fig(pts, names=names, extra={"body": extra}, closed=closed, w=300, h=230)
    ans = I - small if ask == "ACD" else small
    shape = f"a regular {POLY[n]}" if n in POLY else f"part of a regular polygon with {n} sides"
    intro = (f"The diagram shows {shape}" + (f" $ABCDE{'F' if n == 6 else ''}$." if n <= 6 else ".")
             + ("" if n <= 6 else f"\n\n$A$, $B$, $C$ and $D$ are consecutive vertices of the polygon."))
    return Q(intro=intro, figs=[fig(svgs, 70)],
             parts=[P("", f"Find the size of angle $x$.\n\nGive reasons for each step of your working.", 4, prefix="$x =$")],
             rows=[R("", f"interior angle $= {deg(I)}$ (or exterior angle $= {deg(F(360, n))}$)", "M1", ""),
                   R("", f"angle $BAC$ = angle $BCA = (180 - {deg(I)}) \\div 2 = {deg(small)}$", "M1", ""),
                   R("", f"${deg(ans)}$", "A1", "cao"),
                   R("", f"reasons, eg {REASONS['ext']} (or {REASONS['poly']}), {REASONS['iso']}, {REASONS['tri']}", "B1",
                     "dep on M2; for all reasons appropriate to their method")],
             values={"x": ans}, diff="7-9", cw="Work out", refs=["F4.2D", "F4.1D", "H4.7A"])


# ================================================================ 4.4 measures
def b3(t):
    return f"{int(round(t)) % 360:03d}"


@tpl("geometry.measures", "short", n=10)
def bearing_back(r):
    th = r.choice([k for k in range(5, 356) if k % 90])
    back = (th + 180) % 360
    A, B = r.choice([("A", "B"), ("P", "Q"), ("X", "Y"), ("H", "K")])
    th2 = r.choice([k for k in range(5, 356) if k % 90 and abs(k - th) > 30 and abs(k - back) > 30])
    pa = (0, 0)
    pb = (math.sin(math.radians(th)), math.cos(math.radians(th)))
    fr = Frame([pa, pb, (pa[0], pa[1] + 0.5), (pb[0], pb[1] + 0.5), (pa[0] - .3, pa[1]), (pb[0] + .3, pb[1])], 260, 220)
    sa, sb = fr(pa), fr(pb)
    bb = L(*sa, *sb) + ARROW(sa[0], sa[1], sa[0], sa[1] - 45) + ARROW(sb[0], sb[1], sb[0], sb[1] - 45)
    bb += T(sa[0], sa[1] - 55, "N", size=11) + T(sb[0], sb[1] - 55, "N", size=11)
    bb += DOT(*sa) + DOT(*sb) + T(sa[0] - 12, sa[1] + 8, A) + T(sb[0] + 12, sb[1] + 8, B)
    return Q(intro=f"The bearing of {B} from {A} is ${b3(th)}{DEG}$.", figs=[fig(svg(fr.w, fr.h, bb), 55)],
             parts=[P("", f"Work out the bearing of {A} from {B}.", 2, prefix="")],
             rows=[R("", f"${th} {'+' if th < 180 else '-'} 180$", "M1", "or a correct angle shown on a diagram, eg alternate angles with the north lines"),
                   R("", f"${b3(back)}{DEG}$", "A1", "must be given as three figures")],
             values={"bearing": b3(back)}, diff="4-6", cw="Work out", refs=["F4.4D"])


@tpl("geometry.measures", "short", n=12)
def compound_short(r):
    kind = r.choice(["speed", "pressure", "density", "density_kg"])
    if kind == "speed":
        v = r.choice([18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108, 117, 126, 135, 144])
        if r.random() < 0.5:
            return Q(parts=[P("", f"A train travels at an average speed of {v} km/h.\n\nChange {v} km/h into metres per second.", 2, prefix="m/s")],
                     rows=[R("", f"${v} \\times 1000 \\div 3600$", "M1", "or $" + f"{v} \\times 1000 = {v * 1000}$ or " + f"$3600 \\div 1000$"),
                           R("", num(F(v * 1000, 3600)), "A1", "cao")],
                     values={"ms": F(v * 1000, 3600)}, diff="4-6", cw="Change", refs=["F4.4F", "F4.4G"])
        ms = F(v * 1000, 3600)
        return Q(parts=[P("", f"A cyclist has an average speed of {num(ms)} metres per second.\n\nWork out this speed in kilometres per hour.", 2, prefix="km/h")],
                 rows=[R("", f"${num(ms)} \\times 3600 \\div 1000$", "M1", ""), R("", str(v), "A1", "cao")],
                 values={"kmh": v}, diff="4-6", cw="Work out", refs=["F4.4F", "F4.4G"])
    if kind == "pressure":
        a, b = r.randint(12, 60), r.randint(10, 50)
        f_ = r.randrange(60, 900, 5)
        area = F(a * b, 10000)
        p = F(f_) / area
        return Q(intro=f"A box rests on horizontal ground. The face in contact with the ground is a rectangle {a} cm by {b} cm.\n\nThe box exerts a force of {f_} newtons on the ground.\n\npressure $= \\dfrac{{\\text{{force}}}}{{\\text{{area}}}}$",
                 parts=[P("", "Work out the pressure, in newtons per square metre, exerted by the box on the ground.\n\nGive your answer to 3 significant figures.", 3, prefix="N/m²")],
                 rows=[R("", f"${a} \\times {b} = {a * b}$ cm² or $0.{a:02d} \\times 0.{b:02d}$" if a < 100 and b < 100 else "area", "M1", "for the area"),
                       R("", f"${f_} \\div {num(area)}$", "M1", "for converting to m² and dividing; or $" + f"{f_} \\div {a * b} \\times 10000" + "$"),
                       R("", sf(p, 3), "A1", f"awrt {sf(p, 3)}")],
                 values={"pressure": float(p)}, diff="4-6", cw="Work out", refs=["F4.4G"])
    l, w_, h_ = r.randint(3, 15), r.randint(2, 12), r.randint(2, 10)
    d = r.choice([F(27, 10), F(79, 10), F(89, 10), F(113, 10), F(193, 10), F(105, 10), F(73, 10), F(86, 10)])
    V = l * w_ * h_
    m = d * V
    if kind == "density":
        return Q(intro=f"A solid metal block is a cuboid measuring {l} cm by {w_} cm by {h_} cm.\n\nThe metal has a density of {num(float(d))} g/cm³.",
                 parts=[P("", "Work out the mass of the block.", 3, prefix="g")],
                 rows=[R("", f"${l} \\times {w_} \\times {h_} = {V}$", "M1", "for the volume"),
                       R("", f"${num(float(d))} \\times {V}$", "M1", ""),
                       R("", num(float(m)), "A1", "oe")],
                 values={"mass": float(m)}, diff="4-6", cw="Work out", refs=["F4.4G", "F4.10E"])
    mk = m / 1000
    return Q(intro=f"A solid metal block is a cuboid measuring {l} cm by {w_} cm by {h_} cm.\n\nThe block has a mass of {num(float(mk))} kg.",
             parts=[P("", "Work out the density of the metal in g/cm³.", 3, prefix="g/cm³")],
             rows=[R("", f"${l} \\times {w_} \\times {h_} = {V}$", "M1", "for the volume"),
                   R("", f"${num(float(m))} \\div {V}$", "M1", "for converting the mass to grams and dividing"),
                   R("", num(float(d)), "A1", "oe")],
             values={"density": float(d)}, diff="4-6", cw="Work out", refs=["F4.4G", "F4.10E"])


@tpl("geometry.measures", "problem", n=8)
def alloy_density(r):
    mats = r.sample([("copper", F(89, 10)), ("zinc", F(71, 10)), ("tin", F(73, 10)), ("nickel", F(89, 10)),
                     ("aluminium", F(27, 10)), ("silver", F(105, 10)), ("lead", F(113, 10)), ("iron", F(79, 10))], 2)
    (n1, d1), (n2, d2) = mats
    if d1 == d2:
        return None
    m1 = r.randrange(200, 2000, 10)
    v2 = r.randrange(20, 250, 5)
    v1 = F(m1) / d1
    m2 = d2 * v2
    dens = (m1 + m2) / (v1 + v2)
    return Q(intro=f"An alloy is made by mixing {n1} and {n2}.\n\n{m1} g of {n1} is mixed with {v2} cm³ of {n2}.\n\nThe density of {n1} is {num(float(d1))} g/cm³. The density of {n2} is {num(float(d2))} g/cm³.",
             parts=[P("", "Work out the density of the alloy.\n\nGive your answer to 3 significant figures.", 4, prefix="g/cm³")],
             rows=[R("", f"volume of {n1} $= {m1} \\div {num(float(d1))}$ $(= {sf(v1, 4)})$", "M1", ""),
                   R("", f"mass of {n2} $= {num(float(d2))} \\times {v2}$ $(= {num(float(m2))})$", "M1", ""),
                   R("", f"$({m1} + {num(float(m2))}) \\div ({sf(v1, 4)} + {v2})$", "M1", "dep on at least M1; total mass $\\div$ total volume"),
                   R("", sf(dens, 3), "A1", f"awrt {sf(dens, 3)}")],
             values={"density": float(dens)}, diff="7-9", cw="Work out", refs=["F4.4G"])


@tpl("geometry.measures", "problem", n=7)
def speed_journey(r):
    nm = name(r)
    d1 = r.randint(20, 150)
    s1 = r.choice([40, 45, 48, 50, 60, 64, 72, 75, 80, 90])
    t2 = r.choice([15, 20, 24, 25, 35, 40, 45, 50, 75, 84, 90])
    s2 = r.choice([30, 36, 42, 54, 66, 70, 84, 96, 100])
    tt = F(d1, s1) + F(t2, 60)
    dist = d1 + s2 * F(t2, 60)
    avg = dist / tt
    veh = r.choice(["drives", "drives", "cycles"]) if s1 > 30 else "cycles"
    return Q(intro=f"{nm} {veh} {d1} km at an average speed of {s1} km/h.\n\n{nm} then {veh} for {t2} minutes at an average speed of {s2} km/h.",
             parts=[P("", f"Work out {nm}'s average speed for the whole journey.\n\nGive your answer to 3 significant figures.", 4, prefix="km/h")],
             rows=[R("", f"${d1} \\div {s1}$ $(= {sf(F(d1, s1), 4)}$ hours$)$", "M1", "for the time of the first part"),
                   R("", f"${s2} \\times \\frac{{{t2}}}{{60}}$ $(= {num(float(s2 * F(t2, 60)))}$ km$)$", "M1", "for the distance of the second part"),
                   R("", f"$({d1} + {num(float(s2 * F(t2, 60)))}) \\div ({sf(F(d1, s1), 4)} + {num(float(F(t2, 60)))})$", "M1", "for total distance $\\div$ total time, with consistent units"),
                   R("", sf(avg, 3), "A1", f"awrt {sf(avg, 3)}")],
             values={"speed": float(avg)}, diff="7-9", cw="Work out", refs=["F4.4F", "F4.4G"])


@tpl("geometry.measures", "problem", n=7)
def pressure_faces(r):
    dims = sorted(r.sample(range(10, 80, 5), 3))
    a, b, c = dims
    P1 = r.randrange(200, 3000, 50)
    face = r.choice([(a, b), (a, c), (b, c)])
    other = r.choice([f for f in [(a, b), (a, c), (b, c)] if f != face])
    force = F(P1) * F(face[0] * face[1], 10000)
    P2 = force / F(other[0] * other[1], 10000)
    kind = r.choice(["other", "max"])
    if kind == "max":
        other = (a, b)
        P2 = force / F(a * b, 10000)
        ask = "Work out the greatest possible pressure the box can exert on the floor."
    else:
        ask = f"The box is turned so that a face measuring {other[0]} cm by {other[1]} cm is on the floor.\n\nWork out the pressure the box now exerts on the floor."
    if face == other:
        return None
    return Q(intro=f"A box in the shape of a cuboid measures {a} cm by {b} cm by {c} cm.\n\nWhen the face measuring {face[0]} cm by {face[1]} cm is on a horizontal floor, the box exerts a pressure of {big(P1)} N/m².\n\npressure $= \\dfrac{{\\text{{force}}}}{{\\text{{area}}}}$",
             parts=[P("", ask + "\n\nGive your answer to 3 significant figures.", 4, prefix="N/m²")],
             rows=[R("", f"${face[0] / 100:g} \\times {face[1] / 100:g} = {num(float(F(face[0] * face[1], 10000)))}$", "M1", "for the area of the first face in m² (or cm²)"),
                   R("", f"force $= {big(P1)} \\times {num(float(F(face[0] * face[1], 10000)))} = {num(float(force))}$", "M1", ""),
                   R("", f"${num(float(force))} \\div {num(float(F(other[0] * other[1], 10000)))}$", "M1", "for dividing by the area of the " + ("smallest face" if kind == "max" else "new face")),
                   R("", sf(P2, 3), "A1", f"awrt {sf(P2, 3)}")],
             values={"pressure": float(P2)}, diff="7-9", cw="Work out", refs=["F4.4G"])


# ================================================================ 4.5 constructions
SCALE_PX = 22  # px per cm in accurate drawings


@tpl("geometry.construction", "graph", n=10)
def construct_bisect(r):
    a, b, c = r.randint(10, 18) / 2, r.randint(10, 18) / 2, r.randint(12, 20) / 2
    if not (a + b > c + 1 and a + c > b + 1 and b + c > a + 1):
        return None
    pts = tri_from_sides(a, b, c)
    nm = r.choice(["ABC", "PQR", "DEF", "LMN"])
    A, B, C_ = nm
    rad = r.randint(3, int(min(a, b)) - 1) if min(a, b) > 4 else None
    if rad is None:
        return None
    first = r.choice(["perp", "angle"])
    W = c * SCALE_PX + 60
    H = max(p[1] for p in pts) * SCALE_PX + 60
    S = [(30 + p[0] * SCALE_PX, H - 30 - p[1] * SCALE_PX) for p in pts]
    bb = PL(S, close=True) + T(S[0][0] - 10, S[0][1] + 8, A) + T(S[1][0] + 10, S[1][1] + 8, B) + T(S[2][0], S[2][1] - 10, C_)
    if first == "perp":
        pa = P("a", f"Construct the perpendicular bisector of ${A}{B}$ using only a ruler and compasses.\n\nLeave in all your construction arcs.", 2, space="none")
        ra = [R("a", f"correct perpendicular bisector of ${A}{B}$ with two pairs of intersecting arcs", "B2",
                "B1 for two pairs of correct intersecting arcs with no line, or a correct line within guidelines with one pair of arcs")]
        pb = P("b", f"Shade the region of points inside the triangle that are closer to ${B}$ than to ${A}$ and less than {rad} cm from ${C_}$.", 2, space="none")
        rb = [R("b", f"region on the ${B}$ side of the perpendicular bisector and inside an arc of radius {rad} cm centre ${C_}$", "B2",
                f"B1 for an arc of radius {rad} cm, centre ${C_}$ (within 2 mm), or a fully correct region for one condition")]
    else:
        pa = P("a", f"Construct the bisector of angle ${B}{A}{C_}$ using only a ruler and compasses.\n\nLeave in all your construction arcs.", 2, space="none")
        ra = [R("a", f"correct angle bisector with all construction arcs", "B2",
                "B1 for correct arcs on both arms and intersecting arcs with no line, or a line within guidelines with no arcs")]
        pb = P("b", f"Shade the region of points inside the triangle that are closer to ${A}{B}$ than to ${A}{C_}$ and more than {rad} cm from ${C_}$.", 2, space="none")
        rb = [R("b", f"region between ${A}{B}$ and the angle bisector, outside an arc of radius {rad} cm centre ${C_}$", "B2",
                f"B1 for an arc of radius {rad} cm, centre ${C_}$ (within 2 mm), or a fully correct region for one condition")]
    return Q(intro=f"The diagram shows triangle ${nm}$, accurately drawn.\n\n${A}{B} = {num(c)}$ cm, ${B}{C_} = {num(a)}$ cm and ${A}{C_} = {num(b)}$ cm.",
             figs=[fig(svg(W, H, bb), min(95, int(W / 3.6)), note=None)], parts=[pa, pb], rows=ra + rb,
             values={"AB": c, "BC": a, "AC": b, "r": rad}, diff="4-6", cw="Construct", refs=["F4.5D", "F4.5C"],
             method="construction (geometry given exactly)")


@tpl("geometry.construction", "graph", n=10)
def construct_triangle(r):
    a, b, c = r.randint(8, 18) / 2, r.randint(8, 18) / 2, r.randint(12, 20) / 2
    if not (a + b > c + 1.5 and a + c > b + 1.5 and b + c > a + 1.5):
        return None
    nm = r.choice(["PQR", "ABC", "XYZ", "KLM"])
    A, B, C_ = nm
    angA = math.degrees(math.acos((b * b + c * c - a * a) / (2 * b * c)))
    W = c * SCALE_PX + 70
    H = 90
    bb = L(35, H - 30, 35 + c * SCALE_PX, H - 30) + T(25, H - 30, A) + T(45 + c * SCALE_PX, H - 30, B)
    return Q(intro=f"Triangle ${nm}$ has ${A}{B} = {num(c)}$ cm, ${A}{C_} = {num(b)}$ cm and ${B}{C_} = {num(a)}$ cm.\n\nThe side ${A}{B}$ has been drawn accurately below.",
             figs=[fig(svg(W, H, bb), min(95, int(W / 3.6)), note=None)],
             parts=[P("a", f"Use ruler and compasses to construct triangle ${nm}$.\n\nYou must show all your construction lines.", 2, space="none"),
                    P("b", f"Measure the size of angle ${B}{A}{C_}$ in your triangle.", 1, prefix="°")],
             rows=[R("a", f"arcs of radius {num(b)} cm from ${A}$ and {num(a)} cm from ${B}$", "M1", "for one correct arc (within 2 mm)"),
                   R("a", "triangle completed with both arcs shown", "A1", ""),
                   R("b", f"{round(angA) - 2} to {round(angA) + 2}", "B1", f"exact value {dp(angA, 1)}°; ft their triangle")],
             values={"angle": round(angA, 1)}, diff="4-6", cw="Construct", refs=["F4.5B"], method="cosine rule for the measured angle")


@tpl("geometry.construction", "problem", n=10)
def map_scale(r):
    sc = r.choice([20000, 25000, 40000, 50000, 75000, 80000, 100000, 125000, 200000, 250000])
    d = r.choice([F(k, 10) for k in range(15, 160, 3)])
    real_km = d * sc / 100000
    A = r.choice([F(k, 2) for k in range(3, 40)])
    real_area = A * F(sc, 100000) ** 2
    place = r.choice(["a lake", "a forest", "a park", "a farm", "an island"])
    t1, t2 = r.sample(["Ashby", "Brenton", "Carrow", "Dunmore", "Elmstead", "Fenwick", "Garford", "Holbeck"], 2)
    return Q(intro=f"A map has a scale of 1 : {big(sc)}",
             parts=[P("a", f"On the map, the distance between {t1} and {t2} is {num(float(d))} cm.\n\nWork out the real distance between {t1} and {t2}. Give your answer in kilometres.", 2, prefix="km"),
                    P("b", f"On the map, {place} has an area of {num(float(A))} cm².\n\nWork out the real area of {place}. Give your answer in km².", 2, prefix="km²")],
             rows=[R("a", f"${num(float(d))} \\times {big(sc)} = {num(float(d * sc))}$ cm", "M1", "or $1$ cm represents " + num(float(F(sc, 100000))) + " km"),
                   R("a", num(float(real_km)), "A1", "oe"),
                   R("b", f"${num(float(A))} \\times {num(float(F(sc, 100000)))}^2$", "M1", "for using the area scale factor"),
                   R("b", num(float(real_area)), "A1", "oe")],
             values={"distance_km": float(real_km), "area_km2": float(real_area)}, diff="7-9", cw="Work out",
             refs=["F4.11B", "F4.5C", "H4.11A"])


@tpl("geometry.construction", "problem", n=10)
def scale_speed(r):
    nm = name(r)
    sc = r.choice([50000, 100000, 200000, 250000, 400000, 500000])
    d = r.choice([F(k, 10) for k in range(25, 200, 5)])
    real = d * sc / 100000
    sp_ = r.choice([30, 40, 45, 48, 50, 60, 64, 72, 75, 80, 90])
    t = real / sp_
    mins = t * 60
    if mins.denominator != 1 or mins < 20:
        return None
    hh, mm = divmod(int(mins), 60)
    start_h = r.randint(7, 15)
    start_m = r.choice([0, 10, 15, 20, 30, 40, 45, 50])
    end = start_h * 60 + start_m + int(mins)
    eh, em = divmod(end, 60)
    return Q(intro=f"{nm} uses a map with a scale of 1 : {big(sc)} to plan a journey.\n\nOn the map, the route is {num(float(d))} cm long.\n\n{nm} leaves at {start_h:02d}:{start_m:02d} and travels at an average speed of {sp_} km/h.",
             parts=[P("", f"Work out the time at which {nm} arrives.", 4, prefix="")],
             rows=[R("", f"${num(float(d))} \\times {big(sc)} \\div 100\\,000$", "M1", "for converting the map distance to a real distance"),
                   R("", f"${num(float(real))}$ km", "A1", ""),
                   R("", f"${num(float(real))} \\div {sp_} = {num(float(t))}$ hours", "M1", f"or {hh} h {mm} min"),
                   R("", f"{eh:02d}:{em:02d}", "A1", "accept any unambiguous time format")],
             values={"distance_km": float(real), "arrive": f"{eh:02d}:{em:02d}"}, diff="4-6", cw="Work out",
             refs=["F4.11B", "F4.5C", "F4.4F"])


# ================================================================ 4.6 circles
@tpl("geometry.circles", "short", n=12)
def circle_theorem(r):
    kind = r.choice(["centre", "segment", "cyclic", "semi", "tangent", "alt"])
    xv = r.randint(24, 72)
    pts = None
    if kind == "centre":
        pts = {"A": -90 - xv, "B": -90 + xv, "C": 90 + r.randint(-30, 30)}
        s, pos = circle_fig(pts, chords=[("A", "C"), ("B", "C")], centre="O", extra_lines=[("O", "A"), ("O", "B")],
                            angles={("C", "A", "B"): f"{xv}°", ("O", "A", "B"): "x"})
        given = "$A$, $B$ and $C$ are points on a circle, centre $O$."
        ans, reason = 2 * xv, "the angle at the centre is twice the angle at the circumference"
    elif kind == "segment":
        pts = {"A": -90 - xv, "B": -90 + xv, "C": 90 + r.randint(20, 50), "D": 90 - r.randint(20, 50)}
        s, pos = circle_fig(pts, chords=[("A", "C"), ("B", "C"), ("A", "D"), ("B", "D")],
                            angles={("C", "A", "B"): f"{xv}°", ("D", "A", "B"): "x"})
        given = "$A$, $B$, $C$ and $D$ are points on a circle."
        ans, reason = xv, "angles in the same segment are equal"
    elif kind == "cyclic":
        xv = r.randint(50, 80)
        pts = {"A": -90 - xv, "B": 90 + r.randint(-25, 25), "C": -90 + xv, "D": -90 + r.randint(-xv + 20, xv - 20)}
        s, pos = circle_fig(pts, chords=[("A", "B"), ("B", "C"), ("C", "D"), ("D", "A")],
                            angles={("B", "A", "C"): f"{xv}°", ("D", "A", "C"): "x"})
        given = "$ABCD$ is a cyclic quadrilateral."
        ans, reason = 180 - xv, "opposite angles of a cyclic quadrilateral sum to $180^\\circ$"
    elif kind == "semi":
        pts = {"A": 180, "B": 0, "C": 2 * xv}
        s, pos = circle_fig(pts, chords=[("A", "B"), ("A", "C"), ("C", "B")], centre="O",
                            angles={("A", "C", "B"): f"{xv}°", ("B", "C", "A"): "x"})
        given = "$A$, $B$ and $C$ are points on a circle, centre $O$.\n\n$AB$ is a diameter of the circle."
        ans, reason = 90 - xv, "the angle in a semicircle is $90^\\circ$, and angles in a triangle sum to $180^\\circ$"
    elif kind == "tangent":
        xv = r.randint(28, 62)
        k = 1 / math.tan(math.radians(xv))
        pts = {"T": 90, "P": (k, 1.0)}
        s, pos = circle_fig(pts, centre="O", extra_lines=[("O", "T"), ("T", "P"), ("O", "P")], R=min(85, 200 / (k + 1.3)),
                            angles={("P", "T", "O"): f"{xv}°", ("O", "T", "P"): "x"})
        given = "$T$ is a point on a circle, centre $O$.\n\n$PT$ is the tangent to the circle at $T$."
        ans, reason = 90 - xv, "the tangent is perpendicular to the radius, and angles in a triangle sum to $180^\\circ$"
    else:
        pts = {"A": -90, "B": -90 + 2 * xv, "C": 90 + r.randint(-30, 30)}
        s, pos = circle_fig(pts, chords=[("A", "B"), ("A", "C"), ("B", "C")], tangents=[("A", 95, 95, ("S", "T"))],
                            angles={("A", "T", "B"): f"{xv}°", ("C", "A", "B"): "x"})
        given = "$A$, $B$ and $C$ are points on a circle.\n\n$SAT$ is the tangent to the circle at $A$."
        ans, reason = xv, "the angle between a tangent and a chord is equal to the angle in the alternate segment"
    return Q(intro=given, figs=[fig(s, 60)],
             parts=[P("a", "Write down the size of the angle marked $x$." if kind in ("centre", "segment", "alt", "cyclic") else "Find the size of angle $x$.", 1, prefix="$x =$"),
                    P("b", "Give a reason for your answer.", 1, space="lines", lines=2)],
             rows=[R("a", f"${ans}$", "B1", "cao"), R("b", reason, "B1", "dep on B1 in (a); the reason must be stated in full")],
             values={"x": ans}, diff="4-6", cw="Write down", refs=["H4.6C", "F4.6B", "H4.6B", "H4.7A"],
             method="exact circle theorem; diagram angles computed from the same values")


@tpl("geometry.circles", "short", n=10)
def intersecting_chords(r):
    kind = r.choice(["in", "in", "out"])
    if kind == "in":
        a, b, c = r.randint(3, 15), r.randint(3, 15), r.randint(3, 15)
        d = F(a * b, c)
        if a == c or d.denominator not in (1, 2, 4, 5):
            return None
        P0 = (r.uniform(-0.25, 0.25), r.uniform(-0.2, 0.2))
        t1, t2 = math.radians(r.randint(10, 50)), math.radians(r.randint(110, 160))
        pts = {}
        for (n1, n2), th in ((("A", "B"), t1), (("C", "D"), t2)):
            ux, uy = math.cos(th), math.sin(th)
            bq = P0[0] * ux + P0[1] * uy
            cq = P0[0] ** 2 + P0[1] ** 2 - 1
            s1 = -bq + math.sqrt(bq * bq - cq)
            s2 = -bq - math.sqrt(bq * bq - cq)
            pts[n1] = math.degrees(math.atan2(P0[1] + s1 * uy, P0[0] + s1 * ux))
            pts[n2] = math.degrees(math.atan2(P0[1] + s2 * uy, P0[0] + s2 * ux))
        pts["P"] = P0
        s, pos = circle_fig(pts, chords=[("A", "B"), ("C", "D")])
        return Q(intro=f"$A$, $B$, $C$ and $D$ are points on a circle.\n\nThe chords $AB$ and $CD$ intersect at the point $P$.\n\n$AP = {a}$ cm, $PB = {b}$ cm and $CP = {c}$ cm.",
                 figs=[fig(s, 55)], parts=[P("", "Work out the length of $PD$.", 2, prefix="cm")],
                 rows=[R("", f"${a} \\times {b} = {c} \\times PD$", "M1", ""), R("", num(float(d)), "A1", "oe")],
                 values={"PD": float(d)}, diff="7-9", cw="Work out", refs=["H4.6A"])
    pa, ab, pc = r.randint(3, 12), r.randint(4, 15), r.randint(3, 14)
    pd = F(pa * (pa + ab), pc)
    cd = pd - pc
    if pc >= pa + ab or cd <= 1 or pc == pa or cd.denominator not in (1, 2, 4, 5):
        return None
    P0 = (-1.9, 0.0)
    pts = {}
    for (n1, n2), th in ((("A", "B"), math.radians(r.randint(8, 18))), (("C", "D"), -math.radians(r.randint(8, 18)))):
        ux, uy = math.cos(th), math.sin(th)
        bq = P0[0] * ux + P0[1] * uy
        cq = P0[0] ** 2 + P0[1] ** 2 - 1
        s1 = -bq - math.sqrt(bq * bq - cq)
        s2 = -bq + math.sqrt(bq * bq - cq)
        pts[n1] = math.degrees(math.atan2(P0[1] + s1 * uy, P0[0] + s1 * ux))
        pts[n2] = math.degrees(math.atan2(P0[1] + s2 * uy, P0[0] + s2 * ux))
    pts["P"] = P0
    s, pos = circle_fig(pts, extra_lines=[("P", "B"), ("P", "D")], w=330, R=70)
    return Q(intro=f"$A$, $B$, $C$ and $D$ are points on a circle.\n\n$PAB$ and $PCD$ are straight lines.\n\n$PA = {pa}$ cm, $AB = {ab}$ cm and $PC = {pc}$ cm.",
             figs=[fig(s, 60)], parts=[P("", "Work out the length of $CD$.", 3, prefix="cm")],
             rows=[R("", f"${pa} \\times {pa + ab} = {pc} \\times PD$", "M1", f"or ${pa} \\times {pa + ab} = {pc}({pc} + CD)$"),
                   R("", f"$PD = {num(float(pd))}$", "M1", ""),
                   R("", num(float(cd)), "A1", "oe")],
             values={"CD": float(cd)}, diff="7-9", cw="Work out", refs=["H4.6A"])


@tpl("geometry.circles", "proof", n=10)
def alt_segment_reasons(r):
    xv = r.randint(28, 70)
    pts = {"A": -90, "B": -90 + 2 * xv, "C": 90 + r.randint(-30, 30)}
    s, pos = circle_fig(pts, chords=[("A", "B"), ("A", "C"), ("B", "C")], centre="O",
                        extra_lines=[("O", "A"), ("O", "B")], tangents=[("A", 95, 95, ("S", "T"))],
                        angles={("A", "T", "B"): f"{xv}°"})
    ask = r.choice(["OBA", "ACB"])
    if ask == "OBA":
        ans = 90 - xv
        rows = [R("", f"angle $OAT = 90$ or angle $ACB = {xv}$ or angle $AOB = {2 * xv}$", "M1", ""),
                R("", f"${ans}$", "A1", "cao"),
                R("", "reason, eg the tangent is perpendicular to the radius / alternate segment theorem / the angle at the centre is twice the angle at the circumference", "B1", ""),
                R("", "full reasons appropriate to their method, including base angles of an isosceles triangle are equal", "B1", "dep on M1")]
    else:
        ans = xv
        rows = [R("", f"angle $OAT = 90$ and angle $OAB = {90 - xv}$, or angle $AOB = {2 * xv}$", "M1", "or direct use of the alternate segment theorem"),
                R("", f"${ans}$", "A1", "cao"),
                R("", "reason, eg the tangent is perpendicular to the radius / the angle at the centre is twice the angle at the circumference", "B1", ""),
                R("", "full reasons for their method, eg the alternate segment theorem", "B1", "dep on M1")]
    return Q(intro="$A$, $B$ and $C$ are points on a circle, centre $O$.\n\n$SAT$ is the tangent to the circle at $A$.",
             figs=[fig(s, 60)],
             parts=[P("", f"Find the size of angle ${ask}$.\n\nGive reasons for each step of your working.", 4, prefix="°")],
             rows=rows, values={ask: ans}, diff="7-9", cw="Work out", refs=["H4.6C", "F4.6B", "H4.7A"])


@tpl("geometry.circles", "proof", n=10)
def cyclic_reasons(r):
    a = r.randint(40, 85)
    pts = {"A": 90 + r.randint(-20, 20), "B": -90 - a + r.randint(-10, 10)}
    # B and D symmetric about the point opposite so that angle BAD = a
    pts["B"] = -90 - a
    pts["D"] = -90 + a
    pts["C"] = -90 + r.randint(-a + 15, a - 15)
    s, pos = circle_fig(pts, chords=[("A", "B"), ("B", "C"), ("C", "D"), ("D", "A")], centre="O",
                        extra_lines=[("O", "B"), ("O", "D")], angles={("A", "B", "D"): f"{a}°"})
    ask = r.choice(["BCD", "OBD", "both"])
    if ask == "BCD":
        return Q(intro="$A$, $B$, $C$ and $D$ are points on a circle, centre $O$.",
                 figs=[fig(s, 60)],
                 parts=[P("a", "Find the size of angle $BOD$.\n\nGive a reason for your answer.", 2, prefix="°"),
                        P("b", "Find the size of angle $BCD$.\n\nGive a reason for your answer.", 2, prefix="°")],
                 rows=[R("a", f"${2 * a}$", "B1", ""), R("a", "the angle at the centre is twice the angle at the circumference", "B1", ""),
                       R("b", f"${180 - a}$", "B1", ""), R("b", "opposite angles of a cyclic quadrilateral sum to $180^\\circ$", "B1", "")],
                 values={"BOD": 2 * a, "BCD": 180 - a}, diff="7-9", cw="Work out", refs=["H4.6C", "H4.6B", "H4.7A"])
    ans = 90 - a
    return Q(intro="$A$, $B$, $C$ and $D$ are points on a circle, centre $O$.",
             figs=[fig(s, 60)],
             parts=[P("", "Find the size of angle $OBD$.\n\nGive reasons for each step of your working.", 4, prefix="°")],
             rows=[R("", f"angle $BOD = {2 * a}$", "M1", ""),
                   R("", f"$(180 - {2 * a}) \\div 2 = {ans}$", "A1", "cao"),
                   R("", "the angle at the centre is twice the angle at the circumference", "B1", ""),
                   R("", "base angles of an isosceles triangle are equal (and angles in a triangle sum to $180^\\circ$)", "B1", "dep on M1")],
             values={"OBD": ans}, diff="7-9", cw="Work out", refs=["H4.6C", "H4.7A"])


# ================================================================ 4.8 right-angled trig
def rt_fig(r, adj, opp, nm, labs, ang_lab=None):
    pts = [(0, 0), (adj, 0), (adj, opp)]
    if r.random() < 0.5:
        pts = [(0, 0), (-adj, 0), (-adj, opp)]
        pts = [(x + adj, y) for x, y in pts]
    angles = {0: ang_lab} if ang_lab else {}
    return polygon_fig(pts, names=list(nm), sides=labs, angles=angles, right=[1], w=300, h=200)


@tpl("geometry.trigonometry", "short", n=17)
def trig_side(r):
    th = r.randint(18, 72)
    known = r.choice(["adj", "opp", "hyp"])
    want = r.choice([s for s in ["adj", "opp", "hyp"] if s != known])
    L_ = r.choice([F(k, 10) for k in range(45, 250, 3)])
    t = math.radians(th)
    sides = {"adj": math.cos(t), "opp": math.sin(t), "hyp": 1.0}
    k = float(L_) / sides[known]
    val = sides[want] * k
    nm = r.choice(LET)
    A, B, C_ = nm
    seg = {"adj": (0, 1), "opp": (1, 2), "hyp": (2, 0)}
    nmseg = {"adj": A + B, "opp": B + C_, "hyp": A + C_}
    labs = {seg[known]: f"{num(float(L_))} cm", seg[want]: "x cm"}
    s = rt_fig(r, sides["adj"] * 3, sides["opp"] * 3, nm, labs, f"{th}°")
    ratio = {("opp", "hyp"): "sin", ("hyp", "opp"): "sin", ("adj", "hyp"): "cos", ("hyp", "adj"): "cos",
             ("opp", "adj"): "tan", ("adj", "opp"): "tan"}[(known, want)]
    if want == "hyp":
        m2 = f"$x = {num(float(L_))} \\div \\{ratio} {th}$"
    elif known == "hyp":
        m2 = f"$x = {num(float(L_))} \\times \\{ratio} {th}$"
    elif want == "opp":
        m2 = f"$x = {num(float(L_))} \\times \\tan {th}$"
    else:
        m2 = f"$x = {num(float(L_))} \\div \\tan {th}$"
    return Q(intro=f"${nm}$ is a right-angled triangle.", figs=[fig(s, 65)],
             parts=[P("", "Calculate the value of $x$.\n\nGive your answer to 3 significant figures.", 3, prefix="$x =$")],
             rows=[R("", f"$\\{ratio} {th} = \\dfrac{{\\ldots}}{{\\ldots}}$ with the correct sides", "M1", "for a correct trigonometric statement"),
                   R("", m2, "M1", "for a correct rearrangement"),
                   R("", sf(val, 3), "A1", f"awrt {sf(val, 3)}")],
             values={"x": val}, diff="4-6", cw="Calculate", refs=["F4.8B"])


@tpl("geometry.trigonometry", "short", n=17)
def trig_angle(r):
    s1, s2 = r.sample([F(k, 10) for k in range(30, 200, 7)], 2)
    combo = r.choice([("opp", "adj"), ("opp", "hyp"), ("adj", "hyp")])
    vals = dict(zip(combo, (s1, s2)))
    if "hyp" in vals and vals["hyp"] <= max(v for k, v in vals.items() if k != "hyp") * F(11, 10):
        return None
    if combo == ("opp", "adj"):
        th = math.degrees(math.atan(float(s1 / s2))); fn = "tan"
        adj, opp = float(s2), float(s1)
    elif combo == ("opp", "hyp"):
        th = math.degrees(math.asin(float(s1 / s2))); fn = "sin"
        opp = float(s1); adj = math.sqrt(float(s2) ** 2 - opp ** 2)
    else:
        th = math.degrees(math.acos(float(s1 / s2))); fn = "cos"
        adj = float(s1); opp = math.sqrt(float(s2) ** 2 - adj ** 2)
    if not 12 < th < 78:
        return None
    nm = r.choice(LET)
    seg = {"adj": (0, 1), "opp": (1, 2), "hyp": (2, 0)}
    labs = {seg[k]: f"{num(float(v))} cm" for k, v in vals.items()}
    sc = 3 / max(adj, opp)
    s = rt_fig(r, adj * sc, opp * sc, nm, labs, "y")
    return Q(intro=f"${nm}$ is a right-angled triangle.", figs=[fig(s, 65)],
             parts=[P("", "Calculate the size of the angle marked $y$.\n\nGive your answer to 1 decimal place.", 3, prefix="$y =$")],
             rows=[R("", f"$\\{fn} y = \\dfrac{{{num(float(s1))}}}{{{num(float(s2))}}}$", "M1", ""),
                   R("", f"$y = \\{fn}^{{-1}}\\left(\\dfrac{{{num(float(s1))}}}{{{num(float(s2))}}}\\right)$", "M1", ""),
                   R("", dp(th, 1), "A1", f"awrt {dp(th, 1)}")],
             values={"y": th}, diff="4-6", cw="Calculate", refs=["F4.8B"])


@tpl("geometry.trigonometry", "short", n=17)
def pythagoras(r):
    a, b = r.sample([F(k, 10) for k in range(25, 180, 3)], 2)
    want = r.choice(["hyp", "leg"])
    nm = r.choice(LET)
    A, B, C_ = nm
    if want == "hyp":
        val = math.sqrt(float(a * a + b * b))
        labs = {(0, 1): f"{num(float(a))} cm", (1, 2): f"{num(float(b))} cm"}
        adj, opp = float(a), float(b)
        m1 = f"${num(float(a))}^2 + {num(float(b))}^2$"
        m2 = f"$\\sqrt{{{num(float(a * a + b * b))}}}$"
        ask = A + C_
    else:
        hyp, leg = max(a, b), min(a, b)
        if hyp < leg * F(6, 5):
            return None
        val = math.sqrt(float(hyp * hyp - leg * leg))
        labs = {(2, 0): f"{num(float(hyp))} cm", (0, 1): f"{num(float(leg))} cm"}
        adj, opp = float(leg), val
        m1 = f"${num(float(hyp))}^2 - {num(float(leg))}^2$"
        m2 = f"$\\sqrt{{{num(float(hyp * hyp - leg * leg))}}}$"
        ask = B + C_
    sc = 3 / max(adj, opp)
    s = rt_fig(r, adj * sc, opp * sc, nm, labs)
    return Q(intro=f"${nm}$ is a right-angled triangle.", figs=[fig(s, 65)],
             parts=[P("", f"Calculate the length of ${ask}$.\n\nGive your answer to 3 significant figures.", 3, prefix="cm")],
             rows=[R("", m1, "M1", ""), R("", m2, "M1", ""), R("", sf(val, 3), "A1", f"awrt {sf(val, 3)}")],
             values={ask: val}, diff="4-6", cw="Calculate", refs=["F4.8A"])


@tpl("geometry.trigonometry", "problem", n=17)
def elevation_two(r):
    al = r.randint(35, 65)
    be = r.randint(15, al - 8)
    d = r.randint(15, 120)
    ta, tb = math.tan(math.radians(al)), math.tan(math.radians(be))
    xa = d * tb / (ta - tb)
    h = xa * ta
    obj = r.choice(["tower", "tree", "building", "flagpole", "lighthouse"])
    fr = Frame([(0, 0), (xa + d, 0), (0, h)], 330, 180)
    T0, Bs, Ap, Bp = fr((0, h)), fr((0, 0)), fr((xa, 0)), fr((xa + d, 0))
    bb = L(*Bs, *T0, w=2) + L(Bs[0] - 10, Bs[1], Bp[0] + 15, Bp[1]) + L(*Ap, *T0) + L(*Bp, *T0)
    bb += right_mark(Bs, T0, Ap) + T(Ap[0], Ap[1] + 12, "A") + T(Bp[0], Bp[1] + 12, "B") + T(Bs[0] - 4, Bs[1] + 12, "F") + T(T0[0] - 10, T0[1], "T")
    bb += ARC(Ap[0], Ap[1], 20, 180 - al, 180, w=1) + T(Ap[0] - 30, Ap[1] - 10, f"{al}°", size=11)
    bb += ARC(Bp[0], Bp[1], 28, 180 - be, 180, w=1) + T(Bp[0] - 42, Bp[1] - 8, f"{be}°", size=11)
    bb += T((Ap[0] + Bp[0]) / 2, Ap[1] + 12, f"{d} m", size=11)
    return Q(intro=f"The diagram shows a vertical {obj} $FT$ on horizontal ground.\n\n$F$, $A$ and $B$ are points in a straight line on the ground, with $AB = {d}$ m.\n\nThe angle of elevation of $T$ from $A$ is ${al}{DEG}$. The angle of elevation of $T$ from $B$ is ${be}{DEG}$.",
             figs=[fig(svg(fr.w, fr.h, bb), 80)],
             parts=[P("", f"Calculate the height of the {obj}.\n\nGive your answer to 3 significant figures.", 5, prefix="m")],
             rows=[R("", f"$h = FA \\tan {al}$ or $h = (FA + {d}) \\tan {be}$", "M1", "or angle $ATB = " + str(al - be) + "$"),
                   R("", f"$FA \\tan {al} = (FA + {d}) \\tan {be}$", "M1", f"or $AT = \\dfrac{{{d} \\sin {be}}}{{\\sin {al - be}}}$ (sine rule)"),
                   R("", f"$FA = {sf(xa, 4)}$ or $AT = {sf(h / math.sin(math.radians(al)), 4)}$", "A1", ""),
                   R("", f"$h = {sf(xa, 4)} \\times \\tan {al}$", "M1", "dep on previous M1"),
                   R("", sf(h, 3), "A1", f"awrt {sf(h, 3)}")],
             values={"height": h}, diff="7-9", cw="Calculate", refs=["H4.8B", "F4.8C"])


@tpl("geometry.trigonometry", "problem", n=17)
def bearing_trig(r):
    th = r.randint(15, 75)
    a, b = r.randint(8, 60), r.randint(8, 60)
    d = math.hypot(a, b)
    phi = math.degrees(math.atan(b / a))
    br = th + phi
    pts = [(0, 0), (a * math.sin(math.radians(th)), a * math.cos(math.radians(th)))]
    q = pts[1]
    t2 = math.radians(th + 90)
    pts.append((q[0] + b * math.sin(t2), q[1] + b * math.cos(t2)))
    fr = Frame(pts + [(0, a * 0.5)], 300, 240, m=62)
    S = [fr(p) for p in pts]
    bb = PL(S) + ARROW(S[0][0], S[0][1], S[0][0], S[0][1] - 50) + T(S[0][0], S[0][1] - 58, "N", size=11)
    bb += ARROW(S[1][0], S[1][1], S[1][0], S[1][1] - 40) + T(S[1][0], S[1][1] - 48, "N", size=11)
    bb += T(S[0][0] - 10, S[0][1] + 8, "P") + T(S[1][0] + 4, S[1][1] - 10, "Q") + T(S[2][0] + 10, S[2][1] + 8, "R")
    bb += right_mark(S[1], S[0], S[2])
    return Q(intro=f"A ship sails {a} km from a port $P$ on a bearing of ${b3(th)}{DEG}$ to a point $Q$.\n\nThe ship then sails {b} km on a bearing of ${b3(th + 90)}{DEG}$ to a point $R$.",
             figs=[fig(svg(fr.w, fr.h, bb), 65)],
             parts=[P("a", "Calculate the distance $PR$.\n\nGive your answer to 3 significant figures.", 2, prefix="km"),
                    P("b", "Calculate the bearing of $R$ from $P$.\n\nGive your answer correct to the nearest degree.", 3, prefix="°")],
             rows=[R("a", f"$\\sqrt{{{a}^2 + {b}^2}}$", "M1", ""), R("a", sf(d, 3), "A1", f"awrt {sf(d, 3)}"),
                   R("b", f"$\\tan QPR = \\dfrac{{{b}}}{{{a}}}$", "M1", "or another correct trigonometric statement for angle $QPR$"),
                   R("b", f"${th} + {dp(phi, 1)}$", "M1", "for adding their angle to the first bearing"),
                   R("b", f"${b3(br)}$", "A1", f"accept {b3(br - 0.5)} to {b3(br + 0.5)}")],
             values={"PR": d, "bearing": round(br)}, diff="7-9", cw="Calculate", refs=["F4.8A", "F4.8C", "F4.4D"])


@tpl("geometry.trigonometry", "problem", n=17)
def two_triangles(r):
    p = r.randint(6, 25)
    al = r.randint(30, 70)
    q = r.randint(5, 30)
    ad = p * math.sin(math.radians(al))
    bd = p * math.cos(math.radians(al))
    angC = math.degrees(math.atan(ad / q))
    pts = [(bd, ad), (0, 0), (bd, 0), (bd + q, 0)]
    fr = Frame(pts, 320, 200)
    S = [fr(x) for x in pts]
    bb = PL([S[0], S[1], S[3]], close=True) + L(*S[0], *S[2]) + right_mark(S[2], S[0], S[3])
    bb += T(S[0][0], S[0][1] - 12, "A") + T(S[1][0] - 10, S[1][1] + 6, "B") + T(S[2][0], S[2][1] + 13, "D") + T(S[3][0] + 10, S[3][1] + 6, "C")
    bb += angle_mark(S[1], S[2], S[0], f"{al}°") + angle_mark(S[3], S[0], S[1], "y", r=24)
    bb += T((S[0][0] + S[1][0]) / 2 - 22, (S[0][1] + S[1][1]) / 2, f"{p} cm") + T((S[2][0] + S[3][0]) / 2, S[2][1] + 13, f"{q} cm")
    return Q(intro="$BDC$ is a straight line. $AD$ is perpendicular to $BC$.", figs=[fig(svg(fr.w, fr.h, bb), 75)],
             parts=[P("", "Calculate the size of the angle marked $y$.\n\nGive your answer to 1 decimal place.", 4, prefix="$y =$")],
             rows=[R("", f"$AD = {p} \\sin {al}$", "M1", ""),
                   R("", f"$AD = {sf(ad, 4)}$", "A1", ""),
                   R("", f"$\\tan y = \\dfrac{{{sf(ad, 4)}}}{{{q}}}$", "M1", "ft their $AD$"),
                   R("", dp(angC, 1), "A1", f"awrt {dp(angC, 1)}")],
             values={"y": angC}, diff="7-9", cw="Calculate", refs=["F4.8B", "F4.8C"])


# ================================================================ sine / cosine rules
def tri_fig(pts, nm, sides, angles, w=300, h=210):
    return polygon_fig(pts, names=list(nm), sides=sides, angles=angles, w=w, h=h)


def rand_tri(r):
    """random triangle with sides a, b, c (opposite A, B, C) and angles in degrees."""
    for _ in range(100):
        A_ = r.randint(25, 120)
        B_ = r.randint(25, 120)
        C_ = 180 - A_ - B_
        if C_ >= 25:
            return A_, B_, C_
    return 60, 60, 60


@tpl("geometry.sine-cosine", "short", n=15)
def sine_rule_side(r):
    A_, B_, C_ = rand_tri(r)
    a = r.choice([F(k, 10) for k in range(40, 200, 3)])
    k = float(a) / math.sin(math.radians(A_))
    b = k * math.sin(math.radians(B_))
    c = k * math.sin(math.radians(C_))
    nm = r.choice(LET)
    pts = tri_from_sides(float(a), b, c)
    s = tri_fig(pts, nm, {(1, 2): f"{num(float(a))} cm", (2, 0): "x cm"}, {0: f"{A_}°", 1: f"{B_}°"})
    return Q(intro=f"${nm}$ is a triangle.", figs=[fig(s, 65)],
             parts=[P("", "Calculate the value of $x$.\n\nGive your answer to 3 significant figures.", 3, prefix="$x =$")],
             rows=[R("", f"$\\dfrac{{x}}{{\\sin {B_}}} = \\dfrac{{{num(float(a))}}}{{\\sin {A_}}}$", "M1", "for a correct sine rule statement"),
                   R("", f"$x = \\dfrac{{{num(float(a))} \\sin {B_}}}{{\\sin {A_}}}$", "M1", ""),
                   R("", sf(b, 3), "A1", f"awrt {sf(b, 3)}")],
             values={"x": b}, diff="7-9", cw="Calculate", refs=["H4.8C"])


@tpl("geometry.sine-cosine", "short", n=15)
def cosine_rule_side(r):
    b, c = r.sample([F(k, 10) for k in range(40, 180, 3)], 2)
    A_ = r.randint(25, 140)
    a2 = float(b * b + c * c) - 2 * float(b * c) * math.cos(math.radians(A_))
    a = math.sqrt(a2)
    nm = r.choice(LET)
    pts = tri_from_sides(a, float(b), float(c))
    s = tri_fig(pts, nm, {(0, 1): f"{num(float(c))} cm", (2, 0): f"{num(float(b))} cm", (1, 2): "x cm"}, {0: f"{A_}°"})
    return Q(intro=f"${nm}$ is a triangle.", figs=[fig(s, 65)],
             parts=[P("", "Calculate the value of $x$.\n\nGive your answer to 3 significant figures.", 3, prefix="$x =$")],
             rows=[R("", f"$x^2 = {num(float(b))}^2 + {num(float(c))}^2 - 2 \\times {num(float(b))} \\times {num(float(c))} \\times \\cos {A_}$", "M1", ""),
                   R("", f"$x = \\sqrt{{{sf(a2, 5)}}}$", "M1", ""),
                   R("", sf(a, 3), "A1", f"awrt {sf(a, 3)}")],
             values={"x": a}, diff="7-9", cw="Calculate", refs=["H4.8C", "H4.8A"])


@tpl("geometry.sine-cosine", "short", n=15)
def cosine_rule_angle(r):
    a, b, c = sorted(r.sample(range(4, 25), 3))
    if a + b <= c + 1:
        return None
    sides = [a, b, c]
    r.shuffle(sides)
    a, b, c = sides
    cosA = F(b * b + c * c - a * a, 2 * b * c)
    A_ = math.degrees(math.acos(float(cosA)))
    nm = r.choice(LET)
    pts = tri_from_sides(a, b, c)
    s = tri_fig(pts, nm, {(0, 1): f"{c} cm", (2, 0): f"{b} cm", (1, 2): f"{a} cm"}, {0: "y"})
    return Q(intro=f"${nm}$ is a triangle.", figs=[fig(s, 65)],
             parts=[P("", "Calculate the size of the angle marked $y$.\n\nGive your answer to 1 decimal place.", 3, prefix="$y =$")],
             rows=[R("", f"$\\cos y = \\dfrac{{{b}^2 + {c}^2 - {a}^2}}{{2 \\times {b} \\times {c}}}$", "M1", f"or ${a}^2 = {b}^2 + {c}^2 - 2 \\times {b} \\times {c} \\cos y$"),
                   R("", f"$y = \\cos^{{-1}}\\left({ftex(cosA)}\\right)$", "M1", ""),
                   R("", dp(A_, 1), "A1", f"awrt {dp(A_, 1)}")],
             values={"y": A_}, diff="7-9", cw="Calculate", refs=["H4.8C", "H4.8A"])


@tpl("geometry.sine-cosine", "short", n=15)
def area_half_absinC(r):
    b, c = r.sample([F(k, 10) for k in range(40, 180, 3)], 2)
    A_ = r.randint(20, 150)
    area = 0.5 * float(b * c) * math.sin(math.radians(A_))
    a = math.sqrt(float(b * b + c * c) - 2 * float(b * c) * math.cos(math.radians(A_)))
    nm = r.choice(LET)
    pts = tri_from_sides(a, float(b), float(c))
    s = tri_fig(pts, nm, {(0, 1): f"{num(float(c))} cm", (2, 0): f"{num(float(b))} cm"}, {0: f"{A_}°"})
    return Q(intro=f"${nm}$ is a triangle.", figs=[fig(s, 65)],
             parts=[P("", "Calculate the area of the triangle.\n\nGive your answer to 3 significant figures.", 2, prefix="cm²")],
             rows=[R("", f"$\\frac{{1}}{{2}} \\times {num(float(b))} \\times {num(float(c))} \\times \\sin {A_}$", "M1", ""),
                   R("", sf(area, 3), "A1", f"awrt {sf(area, 3)}")],
             values={"area": area}, diff="7-9", cw="Calculate", refs=["H4.8E", "H4.8A"])


@tpl("geometry.sine-cosine", "problem", n=17)
def area_given_find_side(r):
    c = r.randint(5, 18)
    A_ = r.randint(25, 140)
    b = r.choice([F(k, 2) for k in range(8, 36)])
    area = F(1, 2) * c * b * F(round(math.sin(math.radians(A_)) * 10000), 10000)
    area = round(0.5 * c * float(b) * math.sin(math.radians(A_)), 1)
    bb_ = 2 * area / (c * math.sin(math.radians(A_)))
    a = math.sqrt(bb_ ** 2 + c * c - 2 * bb_ * c * math.cos(math.radians(A_)))
    nm = r.choice(LET)
    A, B, C_ = nm
    pts = tri_from_sides(a, bb_, c)
    s = tri_fig(pts, nm, {(0, 1): f"{c} cm"}, {0: f"{A_}°"})
    return Q(intro=f"The area of triangle ${nm}$ is {num(area)} cm².\n\n${A}{B} = {c}$ cm and angle ${B}{A}{C_} = {A_}{DEG}$.",
             figs=[fig(s, 65)],
             parts=[P("", f"Calculate the length of ${B}{C_}$.\n\nGive your answer to 3 significant figures.", 5, prefix="cm")],
             rows=[R("", f"$\\frac{{1}}{{2}} \\times {c} \\times {A}{C_} \\times \\sin {A_} = {num(area)}$", "M1", ""),
                   R("", f"${A}{C_} = {sf(bb_, 4)}$", "A1", ""),
                   R("", f"${B}{C_}^2 = {c}^2 + {sf(bb_, 4)}^2 - 2 \\times {c} \\times {sf(bb_, 4)} \\cos {A_}$", "M1", "ft their $" + A + C_ + "$"),
                   R("", f"${B}{C_} = \\sqrt{{{sf(a * a, 5)}}}$", "M1", "dep on previous M1"),
                   R("", sf(a, 3), "A1", f"awrt {sf(a, 3)}")],
             values={"AC": bb_, "BC": a}, diff="7-9", cw="Calculate", refs=["H4.8E", "H4.8C"])


@tpl("geometry.sine-cosine", "problem", n=17)
def quad_two_triangles(r):
    ab, ad = r.randint(5, 14), r.randint(5, 14)
    A_ = r.randint(50, 120)
    bd = math.sqrt(ab * ab + ad * ad - 2 * ab * ad * math.cos(math.radians(A_)))
    Cang = r.randint(40, 80)
    dbc = r.randint(30, 150 - Cang)
    cd = bd * math.sin(math.radians(dbc)) / math.sin(math.radians(Cang))
    # coordinates: B=(0,0), D on x-axis at (bd,0); A below, C above
    angABD = math.degrees(math.asin(ad * math.sin(math.radians(A_)) / bd))
    if ab * ab + bd * bd < ad * ad:
        angABD = 180 - angABD
    Apt = (ab * math.cos(math.radians(angABD)), -ab * math.sin(math.radians(angABD)))
    bc = bd * math.sin(math.radians(180 - Cang - dbc)) / math.sin(math.radians(Cang))
    Cpt = (bc * math.cos(math.radians(dbc)), bc * math.sin(math.radians(dbc)))
    pts = [Apt, (0, 0), Cpt, (bd, 0)]
    fr = Frame(pts, 320, 240)
    S = [fr(p) for p in pts]
    body = PL(S, close=True) + L(*S[1], *S[3])
    for nmv, p, off in zip("ABCD", S, [(0, 13), (-12, 0), (0, -12), (12, 0)]):
        body += T(p[0] + off[0], p[1] + off[1], nmv)
    body += angle_mark(S[0], S[1], S[3], f"{A_}°") + angle_mark(S[2], S[1], S[3], f"{Cang}°") + angle_mark(S[1], S[3], S[2], f"{dbc}°", r=24)
    mid = lambda i, j, dx, dy, t: T((S[i][0] + S[j][0]) / 2 + dx, (S[i][1] + S[j][1]) / 2 + dy, t)
    body += mid(0, 1, -18, 8, f"{ab} cm") + mid(0, 3, 18, 8, f"{ad} cm")
    return Q(intro="$ABCD$ is a quadrilateral.", figs=[fig(svg(fr.w, fr.h, body), 75)],
             parts=[P("", "Calculate the length of $CD$.\n\nGive your answer to 3 significant figures.", 5, prefix="cm")],
             rows=[R("", f"$BD^2 = {ab}^2 + {ad}^2 - 2 \\times {ab} \\times {ad} \\cos {A_}$", "M1", ""),
                   R("", f"$BD = {sf(bd, 4)}$", "A1", ""),
                   R("", f"$\\dfrac{{CD}}{{\\sin {dbc}}} = \\dfrac{{{sf(bd, 4)}}}{{\\sin {Cang}}}$", "M1", "ft their $BD$"),
                   R("", f"$CD = \\dfrac{{{sf(bd, 4)} \\sin {dbc}}}{{\\sin {Cang}}}$", "M1", ""),
                   R("", sf(cd, 3), "A1", f"awrt {sf(cd, 3)}")],
             values={"BD": bd, "CD": cd}, diff="7-9", cw="Calculate", refs=["H4.8C", "H4.8A"])


@tpl("geometry.sine-cosine", "problem", n=17)
def bearing_cosine(r):
    t1 = r.randint(20, 80)
    t2 = t1 + r.randint(40, 130)
    a, b = r.randint(10, 80), r.randint(10, 80)
    P0 = (0, 0)
    Q0 = (a * math.sin(math.radians(t1)), a * math.cos(math.radians(t1)))
    R0 = (Q0[0] + b * math.sin(math.radians(t2)), Q0[1] + b * math.cos(math.radians(t2)))
    ang = 180 - (t2 - t1)
    d = math.hypot(*R0)
    fr = Frame([P0, Q0, R0, (0, max(a, b) * 0.4)], 300, 240, m=62)
    S = [fr(p) for p in (P0, Q0, R0)]
    bb = PL(S) + L(*S[0], *S[2], dash="4,3") + ARROW(S[0][0], S[0][1], S[0][0], S[0][1] - 45) + T(S[0][0], S[0][1] - 53, "N", size=11)
    bb += ARROW(S[1][0], S[1][1], S[1][0], S[1][1] - 40) + T(S[1][0], S[1][1] - 48, "N", size=11)
    bb += T(S[0][0] - 10, S[0][1] + 8, "A") + T(S[1][0] + 4, S[1][1] - 12, "B") + T(S[2][0] + 10, S[2][1] + 8, "C")
    return Q(intro=f"A boat sails {a} km from $A$ on a bearing of ${b3(t1)}{DEG}$ to $B$.\n\nIt then sails {b} km from $B$ on a bearing of ${b3(t2)}{DEG}$ to $C$.",
             figs=[fig(svg(fr.w, fr.h, bb), 65)],
             parts=[P("", "Calculate the distance $AC$.\n\nGive your answer to 3 significant figures.", 4, prefix="km")],
             rows=[R("", f"angle $ABC = 180 - ({t2} - {t1}) = {ang}$", "M1", "for a correct method to find angle $ABC$"),
                   R("", f"$AC^2 = {a}^2 + {b}^2 - 2 \\times {a} \\times {b} \\cos {ang}$", "M1", "ft their angle $ABC$"),
                   R("", f"$AC = \\sqrt{{{sf(d * d, 5)}}}$", "M1", ""),
                   R("", sf(d, 3), "A1", f"awrt {sf(d, 3)}")],
             values={"AC": d}, diff="7-9", cw="Calculate", refs=["H4.8C", "F4.4D"])


@tpl("geometry.sine-cosine", "structured", n=14)
def sine_cosine_struct(r):
    ab, ac = r.randint(5, 16), r.randint(5, 16)
    A_ = r.randint(30, 130)
    bc = math.sqrt(ab * ab + ac * ac - 2 * ab * ac * math.cos(math.radians(A_)))
    sB = ac * math.sin(math.radians(A_)) / bc
    B_ = math.degrees(math.asin(min(1, sB)))
    if ac * ac > ab * ab + bc * bc:
        B_ = 180 - B_
    area = 0.5 * ab * ac * math.sin(math.radians(A_))
    nm = r.choice(LET)
    A, B, C_ = nm
    pts = tri_from_sides(bc, ac, ab)
    s = tri_fig(pts, nm, {(0, 1): f"{ab} cm", (2, 0): f"{ac} cm"}, {0: f"{A_}°"})
    h = 2 * area / bc
    return Q(intro=f"${nm}$ is a triangle with ${A}{B} = {ab}$ cm, ${A}{C_} = {ac}$ cm and angle ${B}{A}{C_} = {A_}{DEG}$.", figs=[fig(s, 65)],
             parts=[P("a", f"Calculate the length of ${B}{C_}$.\n\nGive your answer to 3 significant figures.", 3, prefix="cm"),
                    P("b", f"Calculate the size of angle ${A}{B}{C_}$.\n\nGive your answer to 1 decimal place.", 3, prefix="°"),
                    P("c", f"Calculate the shortest distance from ${A}$ to the line ${B}{C_}$.\n\nGive your answer to 3 significant figures.", 3, prefix="cm")],
             rows=[R("a", f"${B}{C_}^2 = {ab}^2 + {ac}^2 - 2 \\times {ab} \\times {ac} \\cos {A_}$", "M1", ""),
                   R("a", f"$\\sqrt{{{sf(bc * bc, 5)}}}$", "M1", ""), R("a", sf(bc, 3), "A1", f"awrt {sf(bc, 3)}"),
                   R("b", f"$\\dfrac{{\\sin {A}{B}{C_}}}{{{ac}}} = \\dfrac{{\\sin {A_}}}{{{sf(bc, 4)}}}$", "M1", "ft their (a); or cosine rule"),
                   R("b", f"$\\sin^{{-1}}\\left(\\dfrac{{{ac} \\sin {A_}}}{{{sf(bc, 4)}}}\\right)$", "M1", ""),
                   R("b", dp(B_, 1), "A1", f"awrt {dp(B_, 1)}"),
                   R("c", f"area $= \\frac{{1}}{{2}} \\times {ab} \\times {ac} \\sin {A_} = {sf(area, 4)}$", "M1", f"or ${ab} \\sin({dp(B_, 1)})$ directly"),
                   R("c", f"$2 \\times {sf(area, 4)} \\div {sf(bc, 4)}$", "M1", "for area $= \\frac{1}{2} \\times " + f"{B}{C_}" + " \\times h$ rearranged"),
                   R("c", sf(h, 3), "A1", f"awrt {sf(h, 3)}")],
             values={"BC": bc, "ABC": B_, "distance": h}, diff="7-9", cw="Calculate", refs=["H4.8C", "H4.8E", "H4.8A"])


# ================================================================ 3D
@tpl("geometry.3d", "problem", n=10)
def cuboid_angle(r):
    l, w_, h_ = r.randint(4, 20), r.randint(3, 15), r.randint(3, 15)
    d2 = l * l + w_ * w_
    diag = math.sqrt(d2 + h_ * h_)
    ang = math.degrees(math.atan(h_ / math.sqrt(d2)))
    s, P_ = cuboid_fig(l, w_, h_, dims=(f"{l} cm", f"{w_} cm", f"{h_} cm"), diag=[("A", "G"), ("A", "C")])
    ask = r.choice(["both", "angle"])
    if ask == "both":
        return Q(intro="The diagram shows a cuboid $ABCDEFGH$.", figs=[fig(s, 70)],
                 parts=[P("a", "Calculate the length of $AG$.\n\nGive your answer to 3 significant figures.", 3, prefix="cm"),
                        P("b", "Calculate the size of the angle between $AG$ and the plane $ABCD$.\n\nGive your answer to 1 decimal place.", 3, prefix="°")],
                 rows=[R("a", f"$AC^2 = {l}^2 + {w_}^2 = {d2}$", "M1", ""), R("a", f"$\\sqrt{{{d2} + {h_}^2}}$", "M1", ""),
                       R("a", sf(diag, 3), "A1", f"awrt {sf(diag, 3)}"),
                       R("b", "angle $GAC$ identified", "M1", "may be implied by a correct trigonometric statement"),
                       R("b", f"$\\tan GAC = \\dfrac{{{h_}}}{{\\sqrt{{{d2}}}}}$ or $\\sin GAC = \\dfrac{{{h_}}}{{{sf(diag, 4)}}}$", "M1", ""),
                       R("b", dp(ang, 1), "A1", f"awrt {dp(ang, 1)}")],
                 values={"AG": diag, "angle": ang}, diff="7-9", cw="Calculate", refs=["H4.8D", "H4.8F"])
    return Q(intro="The diagram shows a cuboid $ABCDEFGH$.", figs=[fig(s, 70)],
             parts=[P("", "Calculate the size of the angle between $AG$ and the plane $ABCD$.\n\nGive your answer to 1 decimal place.", 4, prefix="°")],
             rows=[R("", f"$AC^2 = {l}^2 + {w_}^2$", "M1", ""), R("", f"$AC = {sf(math.sqrt(d2), 4)}$", "A1", ""),
                   R("", f"$\\tan GAC = \\dfrac{{{h_}}}{{{sf(math.sqrt(d2), 4)}}}$", "M1", "ft their $AC$"),
                   R("", dp(ang, 1), "A1", f"awrt {dp(ang, 1)}")],
             values={"angle": ang}, diff="7-9", cw="Calculate", refs=["H4.8D", "H4.8F"])


def pyramid_fig(base_lab, edge_lab, W=300, H=240):
    A, B, Cc, D = (40, 190), (200, 190), (260, 135), (100, 135)
    M = ((A[0] + Cc[0]) / 2, (A[1] + Cc[1]) / 2)
    V = (M[0], 30)
    b = PL([A, B, Cc]) + L(*A, *D, dash="4,3") + L(*D, *Cc, dash="4,3")
    b += L(*V, *A) + L(*V, *B) + L(*V, *Cc) + L(*V, *D, dash="4,3") + L(*V, *M, dash="2,3") + L(*A, *Cc, dash="2,3")
    for nm, p, o in (("A", A, (-10, 6)), ("B", B, (8, 10)), ("C", Cc, (10, 2)), ("D", D, (-10, -4)), ("V", V, (0, -10)), ("M", M, (10, 8))):
        b += T(p[0] + o[0], p[1] + o[1], nm)
    b += T((A[0] + B[0]) / 2, A[1] + 14, base_lab) + T((V[0] + B[0]) / 2 + 22, (V[1] + B[1]) / 2, edge_lab)
    return svg(W, H, b)


@tpl("geometry.3d", "problem", n=10)
def pyramid(r):
    s_ = r.randint(4, 16)
    e = r.randint(s_ - 1, 2 * s_ + 4)
    half_d = s_ * math.sqrt(2) / 2
    if e <= half_d + 1:
        return None
    hgt = math.sqrt(e * e - half_d * half_d)
    ang = math.degrees(math.acos(half_d / e))
    ask = r.choice(["height", "angle"])
    s = pyramid_fig(f"{s_} cm", f"{e} cm")
    intro = (f"The diagram shows a pyramid with a square base $ABCD$.\n\n$AB = {s_}$ cm. Each sloping edge of the pyramid has length {e} cm.\n\n"
             "The vertex $V$ is vertically above $M$, the centre of the base.")
    if ask == "height":
        vol = s_ * s_ * hgt / 3
        return Q(intro=intro, figs=[fig(s, 70)],
                 parts=[P("", "Calculate the volume of the pyramid.\n\nGive your answer to 3 significant figures.", 5, prefix="cm³")],
                 rows=[R("", f"$AC = \\sqrt{{{s_}^2 + {s_}^2}}$ and $AM = {sf(half_d, 4)}$", "M1", ""),
                       R("", f"$VM = \\sqrt{{{e}^2 - {sf(half_d, 4)}^2}}$", "M1", ""),
                       R("", f"$VM = {sf(hgt, 4)}$", "A1", ""),
                       R("", f"$\\frac{{1}}{{3}} \\times {s_}^2 \\times {sf(hgt, 4)}$", "M1", "ft their height"),
                       R("", sf(vol, 3), "A1", f"awrt {sf(vol, 3)}")],
                 values={"height": hgt, "volume": vol}, diff="7-9", cw="Calculate", refs=["H4.8D", "H4.10A"])
    return Q(intro=intro, figs=[fig(s, 70)],
             parts=[P("", "Calculate the size of the angle between $VA$ and the base $ABCD$.\n\nGive your answer to 1 decimal place.", 4, prefix="°")],
             rows=[R("", f"$AC = \\sqrt{{{s_}^2 + {s_}^2}} = {sf(2 * half_d, 4)}$", "M1", ""),
                   R("", f"$AM = {sf(half_d, 4)}$", "A1", ""),
                   R("", f"$\\cos VAM = \\dfrac{{{sf(half_d, 4)}}}{{{e}}}$", "M1", "or another correct trigonometric ratio"),
                   R("", dp(ang, 1), "A1", f"awrt {dp(ang, 1)}")],
             values={"angle": ang}, diff="7-9", cw="Calculate", refs=["H4.8D", "H4.8F"])
