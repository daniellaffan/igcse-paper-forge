"""4PM1 templates: 7 vectors and 8 rectangular Cartesian coordinates."""
import math

import sympy as sp

from further_maths_util import (tpl, P, R, Q, tex, sf, fr, nz, fig, Axes, points_fig, x, y)

lam, mu = sp.symbols("lambda mu")


# ------------------------------------------------------------------ helpers

def ij(p, q):
    """p i + q j in bold unit-vector form."""
    e = sp.nsimplify(p) * sp.Symbol("I") + sp.nsimplify(q) * sp.Symbol("J")
    return tex(e).replace("I", "\\mathbf{i}").replace("J", "\\mathbf{j}")


def col(p, q):
    return f"\\begin{{pmatrix}} {tex(p)} \\\\ {tex(q)} \\end{{pmatrix}}"


def vab(ca, cb):
    """Combination of bold a and b, coefficients written in front: 2/3 a - b."""
    out = ""
    for c, v in ((sp.nsimplify(ca), "\\mathbf{a}"), (sp.nsimplify(cb), "\\mathbf{b}")):
        if c == 0:
            continue
        mag = "" if abs(c) == 1 else fr(abs(c))
        if not out:
            out = ("-" if c < 0 else "") + mag + v
        else:
            out += (" - " if c < 0 else " + ") + mag + v
    return out or "\\mathbf{0}"


def pt(px, py):
    return f"({fr(px)}, {fr(py)})"


def surd(v):
    return tex(sp.sqrt(sp.nsimplify(v)))


def line_eq(a, b, c):
    """Integer form a x + b y + c = 0 with a > 0."""
    a, b, c = (sp.nsimplify(t) for t in (a, b, c))
    L_ = sp.ilcm(*[sp.Rational(t).q for t in (a, b, c)])
    a, b, c = a * L_, b * L_, c * L_
    g = sp.igcd(*[int(t) for t in (a, b, c) if t != 0])
    a, b, c = a / g, b / g, c / g
    if a < 0 or (a == 0 and b < 0):
        a, b, c = -a, -b, -c
    return (a, b, c), tex(a * x + b * y + c) + " = 0"


def thru(m, px, py):
    """Line with gradient m through (px, py) as (a, b, c) for a x + b y + c = 0."""
    m = sp.nsimplify(m)
    return line_eq(m, -1, py - m * px)


def tri_fig(pts, names, extra=None, arrows=(), sides=None):
    segs = [(names[i], names[(i + 1) % len(names)]) for i in range(len(names))]
    return points_fig(dict(zip(names, pts)), segs + list(extra or []), arrows=arrows, sides=sides)


# =============================================================== 7A-7E vector basics


@tpl("vec.basic", "short", 22)
def vb_short(r):
    v = r.choice(["unit", "parallel", "ratio", "mag"])
    if v == "unit":
        p, q = nz(r, -9, 9), nz(r, -9, 9)
        m = sp.sqrt(p * p + q * q)
        parts = [P("", f"Given that $\\mathbf{{a}} = {ij(p, q)}$, find\n\n(i) $|\\mathbf{{a}}|$, giving your answer as a simplified surd or an integer\n\n(ii) a unit vector in the direction of $\\mathbf{{a}}$", 3)]
        rows = [R("", f"(i) $\\sqrt{{({p})^2 + ({q})^2}} = {tex(m)}$", "M1 A1"),
                R("", f"(ii) $\\dfrac{{1}}{{{tex(m)}}}({ij(p, q)})$", "B1", "ft their magnitude; oe")]
        return dict(Q(parts=parts, rows=rows, values={"magnitude": m, "unit": [p / m, q / m]}, diff="1-3", cw="Find",
                      refs=["7A", "7B", "7D"]), variant=v)
    if v == "parallel":
        p, q = nz(r, -6, 6), nz(r, -6, 6)
        lm = r.choice([2, 3, -2, 4, sp.Rational(1, 2), -3])
        c = r.randint(-5, 5)
        kv = lm * p - c
        parts = [P("", f"The vectors $\\mathbf{{u}} = {ij(p, q)}$ and $\\mathbf{{v}} = (k{' + ' + str(c) if c > 0 else ' - ' + str(-c) if c < 0 else ''})\\mathbf{{i}} {'+' if lm * q > 0 else '-'} {fr(abs(lm * q))}\\mathbf{{j}}$ are parallel.\n\nFind the value of $k$", 3, prefix="k = ")]
        rows = [R("", f"$\\mathbf{{v}} = \\lambda \\mathbf{{u}}$ with $\\lambda = {fr(lm)}$ from the $\\mathbf{{j}}$ components", "M1"),
                R("", f"$k{' + ' + str(c) if c > 0 else ' - ' + str(-c) if c < 0 else ''} = {fr(lm)} \\times {p if p > 0 else '(' + str(p) + ')'}$", "M1"),
                R("", f"$k = {fr(kv)}$", "A1")]
        if lm * p - c == 0 or abs(lm * q) == 1:
            return None
        return dict(Q(parts=parts, rows=rows, values={"k": kv}, diff="4-6", cw="Find", refs=["7A", "7C"]), variant=v)
    if v == "ratio":
        A = (r.randint(-8, 8), r.randint(-8, 8))
        m_, n_ = r.choice([(1, 2), (2, 1), (1, 3), (3, 1), (2, 3), (3, 2), (1, 4), (3, 4)])
        B = (A[0] + (m_ + n_) * nz(r, -3, 3), A[1] + (m_ + n_) * nz(r, -3, 3))
        Pp = [sp.Rational(n_ * A[i] + m_ * B[i], m_ + n_) for i in range(2)]
        parts = [P("", f"Relative to a fixed origin $O$, the points $A$ and $B$ have position vectors ${ij(*A)}$ and ${ij(*B)}$ respectively.\n\n$P$ is the point on $AB$ with $AP : PB = {m_} : {n_}$\n\nFind the position vector of $P$", 3)]
        rows = [R("", f"$\\overrightarrow{{AB}} = {ij(B[0] - A[0], B[1] - A[1])}$", "B1"),
                R("", f"$\\overrightarrow{{OP}} = \\overrightarrow{{OA}} + \\dfrac{{{m_}}}{{{m_ + n_}}}\\overrightarrow{{AB}}$", "M1"),
                R("", f"${ij(*Pp)}$", "A1")]
        return dict(Q(parts=parts, rows=rows, values={"OP": Pp}, diff="4-6", cw="Find", refs=["7C", "7E"]), variant=v)
    trip = r.choice([(3, 4, 5), (5, 12, 13), (6, 8, 10), (8, 15, 17), (9, 12, 15), (7, 24, 25)])
    a_, b_, h = trip if r.random() < 0.5 else (trip[1], trip[0], trip[2])
    c = r.randint(-6, 6)
    ks = sorted([b_ - c, -b_ - c])
    parts = [P("", f"Given that $|{a_}\\mathbf{{i}} + (k{' + ' + str(c) if c > 0 else ' - ' + str(-c) if c < 0 else ''})\\mathbf{{j}}| = {h}$, find the possible values of $k$", 3)]
    rows = [R("", f"${a_}^2 + (k{' + ' + str(c) if c > 0 else ' - ' + str(-c) if c < 0 else ''})^2 = {h}^2$", "M1"),
            R("", f"$k{' + ' + str(c) if c > 0 else ' - ' + str(-c) if c < 0 else ''} = \\pm {b_}$", "M1"),
            R("", f"$k = {ks[0]}$ or $k = {ks[1]}$", "A1")]
    return dict(Q(parts=parts, rows=rows, values={"k": ks}, diff="4-6", cw="Find", refs=["7B"]), variant=v)


@tpl("vec.basic", "multi-part", 22)
def vb_multi(r):
    A = (r.randint(-6, 6), r.randint(-6, 6))
    B = (r.randint(-6, 6), r.randint(-6, 6))
    C = (r.randint(-6, 6), r.randint(-6, 6))
    AB = (B[0] - A[0], B[1] - A[1])
    BC = (C[0] - B[0], C[1] - B[1])
    if AB == (0, 0) or BC == (0, 0) or AB[0] * BC[1] - AB[1] * BC[0] == 0:
        return None
    D = (A[0] + C[0] - B[0], A[1] + C[1] - B[1])
    mag = sp.sqrt(AB[0] ** 2 + AB[1] ** 2)
    v = r.choice(["col", "ij"])
    show = col if v == "col" else ij
    sp_ = 3 * mag  # speed scaling question: vector of magnitude K parallel to AB
    K = r.choice([2, 3, 5, 10])
    W = [K * AB[0] / mag, K * AB[1] / mag]
    intro = (f"Relative to a fixed origin $O$, the points $A$, $B$ and $C$ have position vectors "
             f"$\\overrightarrow{{OA}} = {show(*A)}$, $\\overrightarrow{{OB}} = {show(*B)}$ and $\\overrightarrow{{OC}} = {show(*C)}$")
    parts = [P("a", "Find $\\overrightarrow{AB}$", 1),
             P("b", "Find the exact value of $|\\overrightarrow{AB}|$", 2),
             P("c", f"Find a vector of magnitude {K} in the direction of $\\overrightarrow{{AB}}$", 2),
             P("d", "The point $D$ is such that $ABCD$ is a parallelogram. Find the position vector of $D$", 2)]
    rows = [R("a", f"${show(*AB)}$", "B1"),
            R("b", f"$\\sqrt{{({AB[0]})^2 + ({AB[1]})^2}}$", "M1"), R("b", f"${tex(mag)}$", "A1"),
            R("c", f"$\\dfrac{{{K}}}{{{tex(mag)}}}{show(*AB) if v == 'col' else '(' + show(*AB) + ')'}$", "M1"), R("c", f"${show(*[sp.radsimp(w) for w in W])}$", "A1", "oe"),
            R("d", "$\\overrightarrow{OD} = \\overrightarrow{OA} + \\overrightarrow{BC}$", "M1"),
            R("d", f"${show(*D)}$", "A1")]
    del sp_
    return dict(Q(intro=intro, parts=parts, rows=rows, values={"AB": list(AB), "magAB": mag, "D": list(D)}, diff="4-6",
                  cw="Find", refs=["7A", "7B", "7C", "7D", "7E"]), variant=v)


# =============================================================== 7F vector geometry


def _ratio(r):
    return r.choice([(1, 2), (2, 1), (1, 3), (3, 1), (2, 3), (3, 2), (1, 4), (3, 4), (2, 5), (3, 5)])


@tpl("vec.geometry", "show-that", 22)
def vg_show(r):
    m_, n_ = _ratio(r)
    u = sp.Rational(r.randint(2, 4), r.randint(1, 4)) if r.random() < 0.3 else sp.Rational(r.choice([2, 3, 3, 4, 5]), r.choice([4, 5, 6]))
    base = sp.Rational(n_, m_ + n_)
    if u <= base:
        return None
    t = 1 - base / u
    s = sp.Rational(m_, m_ + n_) / t
    if s.q > 6 or u.q > 6 or s == 1 or u == 1:
        return None
    OP = (base, sp.Rational(m_, m_ + n_))
    Qv, Rv = (u, 0), (0, s)
    QP = (OP[0] - u, OP[1])
    PR = (-OP[0], s - OP[1])
    ratio = t / (1 - t)
    rq = sp.Rational(ratio)
    intro = (f"$OAB$ is a triangle with $\\overrightarrow{{OA}} = \\mathbf{{a}}$ and $\\overrightarrow{{OB}} = \\mathbf{{b}}$\n\n"
             f"$P$ is the point on $AB$ with $AP : PB = {m_} : {n_}$\n\n"
             f"The point $Q$ lies on {'$OA$' if u < 1 else '$OA$ extended'} such that $\\overrightarrow{{OQ}} = {vab(u, 0)}$ and the point $R$ lies on {'$OB$' if s < 1 else '$OB$ extended'} such that $\\overrightarrow{{OR}} = {vab(0, s)}$")
    # diagram: O origin, A along x, B up-right
    Oc, Ac, Bc = (0, 0), (6, 0), (2, 4.5)
    def at(ca, cb):
        return (ca * Ac[0] + cb * Bc[0], ca * Ac[1] + cb * Bc[1])
    pts = {"O": Oc, "A": Ac, "B": Bc, "P": at(*OP), "Q": at(u, 0), "R": at(0, s)}
    segs = [("O", "A"), ("A", "B"), ("O", "B"), ("Q", "R")]
    if u > 1:
        segs.append(("A", "Q"))
    if s > 1:
        segs.append(("B", "R"))
    fg = fig(points_fig({k_: (float(v_[0]), float(v_[1])) for k_, v_ in pts.items()}, segs), 70)
    parts = [P("a", "Find, in terms of $\\mathbf{a}$ and $\\mathbf{b}$, $\\overrightarrow{AB}$", 1),
             P("b", f"Show that $\\overrightarrow{{OP}} = {vab(*OP)}$", 2),
             P("c", "Find, in terms of $\\mathbf{a}$ and $\\mathbf{b}$, simplifying your answers, (i) $\\overrightarrow{QP}$ (ii) $\\overrightarrow{PR}$", 2),
             P("d", "Hence show that $Q$, $P$ and $R$ lie on a straight line.", 2),
             P("e", "Find the ratio $QP : PR$", 1)]
    rows = [R("a", "$\\mathbf{b} - \\mathbf{a}$", "B1"),
            R("b", f"$\\overrightarrow{{OP}} = \\mathbf{{a}} + \\dfrac{{{m_}}}{{{m_ + n_}}}(\\mathbf{{b}} - \\mathbf{{a}})$", "M1"),
            R("b", f"$= {vab(*OP)}$", "A1", "cso"),
            R("c", f"(i) ${vab(*QP)}$", "B1"), R("c", f"(ii) ${vab(*PR)}$", "B1"),
            R("d", f"$\\overrightarrow{{QP}} = {fr(rq)}\\overrightarrow{{PR}}$ oe", "M1", "shows one is a multiple of the other"),
            R("d", "Parallel with common point $P$, so $Q$, $P$, $R$ are collinear", "A1", "cso; must mention common point"),
            R("e", f"${rq.p} : {rq.q}$", "B1")]
    assert sp.simplify(QP[0] - rq * PR[0]) == 0 and sp.simplify(QP[1] - rq * PR[1]) == 0
    return dict(Q(intro=intro, figs=[fg], parts=parts, rows=rows, values={"OP": list(OP), "QP": list(QP), "PR": list(PR), "ratio": [rq.p, rq.q]},
                  diff="7-9", cw="Show that", refs=["7F"]), variant="collinear")


@tpl("vec.geometry", "multi-part", 22)
def vg_multi(r):
    p_, q_ = _ratio(r)
    s_, t_ = _ratio(r)
    m = sp.Rational(p_, p_ + q_)   # OM = m a
    nn = sp.Rational(s_, s_ + t_)  # ON = nn b
    sol = sp.solve([sp.Eq(1 - lam, mu * m), sp.Eq(lam * nn, 1 - mu)], [lam, mu], dict=True)[0]
    L_, M_ = sol[lam], sol[mu]
    OX = (1 - L_, L_ * nn)
    if max(sp.Rational(L_).q, sp.Rational(M_).q) > 30:
        return None
    intro = (f"In triangle $OAB$, $\\overrightarrow{{OA}} = \\mathbf{{a}}$ and $\\overrightarrow{{OB}} = \\mathbf{{b}}$\n\n"
             f"$M$ is on $OA$ with $OM : MA = {p_} : {q_}$, and $N$ is on $OB$ with $ON : NB = {s_} : {t_}$\n\n"
             "The point $X$ is where the line segments $AN$ and $BM$ cross.")
    Oc, Ac, Bc = (0, 0), (6.5, 0), (1.8, 4.6)
    def at(ca, cb):
        return (float(ca * Ac[0] + cb * Bc[0]), float(ca * Ac[1] + cb * Bc[1]))
    pts = {"O": Oc, "A": Ac, "B": Bc, "M": at(m, 0), "N": at(0, nn), "X": at(*OX)}
    fg = fig(points_fig(pts, [("O", "A"), ("O", "B"), ("A", "N"), ("B", "M")]), 70)
    AN = (-1, nn)
    BM = (m, -1)
    parts = [P("a", "Find, in terms of $\\mathbf{a}$ and $\\mathbf{b}$, (i) $\\overrightarrow{AN}$ (ii) $\\overrightarrow{BM}$", 2),
             P("b", "Given that $\\overrightarrow{AX} = \\lambda \\overrightarrow{AN}$, find $\\overrightarrow{OX}$ in terms of $\\lambda$, $\\mathbf{a}$ and $\\mathbf{b}$", 1),
             P("c", "Given also that $\\overrightarrow{BX} = \\mu \\overrightarrow{BM}$, find $\\overrightarrow{OX}$ in terms of $\\mu$, $\\mathbf{a}$ and $\\mathbf{b}$", 1),
             P("d", "Hence find the value of $\\lambda$ and the value of $\\mu$", 4),
             P("e", "Find $\\overrightarrow{OX}$ in terms of $\\mathbf{a}$ and $\\mathbf{b}$", 1),
             P("f", "Find the ratio $AX : XN$", 1)]
    lamt = f"(1 - \\lambda)\\mathbf{{a}} + {fr(nn)}\\lambda\\mathbf{{b}}"
    mut = f"{fr(m)}\\mu\\mathbf{{a}} + (1 - \\mu)\\mathbf{{b}}"
    ratio = sp.Rational(L_) / (1 - L_)
    rows = [R("a", f"(i) ${vab(*AN)}$", "B1"), R("a", f"(ii) ${vab(*BM)}$", "B1"),
            R("b", f"$\\overrightarrow{{OX}} = {lamt}$", "B1", "oe"),
            R("c", f"$\\overrightarrow{{OX}} = {mut}$", "B1", "oe"),
            R("d", f"Equates coefficients: $1 - \\lambda = {fr(m)}\\mu$ and ${fr(nn)}\\lambda = 1 - \\mu$", "M1 A1"),
            R("d", "Solves simultaneously", "M1", "dM1"),
            R("d", f"$\\lambda = {fr(L_)}$, $\\mu = {fr(M_)}$", "A1"),
            R("e", f"${vab(*OX)}$", "B1", "ft their $\\lambda$ or $\\mu$"),
            R("f", f"${ratio.p} : {ratio.q}$", "B1")]
    return dict(Q(intro=intro, figs=[fg], parts=parts, rows=rows,
                  values={"lambda": L_, "mu": M_, "OX": list(OX), "AX_XN": [ratio.p, ratio.q]}, diff="7-9", cw="Find",
                  refs=["7F"]), variant="intersect")


# =============================================================== 8A/8B points


@tpl("coord.points", "short", 22)
def cp_short(r):
    v = r.choice(["ratio", "find_end", "dist", "area"])
    if v in ("ratio", "find_end"):
        m_, n_ = _ratio(r)
        A = (r.randint(-9, 9), r.randint(-9, 9))
        B = (A[0] + (m_ + n_) * nz(r, -3, 3), A[1] + (m_ + n_) * nz(r, -3, 3))
        Pp = tuple(sp.Rational(n_ * A[i] + m_ * B[i], m_ + n_) for i in range(2))
        if v == "ratio":
            parts = [P("", f"$A$ is the point ${pt(*A)}$ and $B$ is the point ${pt(*B)}$\n\n$P$ is the point on $AB$ with $AP : PB = {m_} : {n_}$\n\nFind the coordinates of $P$", 3)]
            rows = [R("", f"$x = \\dfrac{{{n_}({A[0]}) + {m_}({B[0]})}}{{{m_ + n_}}}$ or $y = \\dfrac{{{n_}({A[1]}) + {m_}({B[1]})}}{{{m_ + n_}}}$", "M1"),
                    R("", f"$x = {fr(Pp[0])}$", "A1"), R("", f"$y = {fr(Pp[1])}$", "A1")]
            return dict(Q(parts=parts, rows=rows, values={"P": list(Pp)}, diff="1-3", cw="Find", refs=["8B"]), variant=v)
        parts = [P("", f"$A$ is the point ${pt(*A)}$. The point $P$ ${pt(*Pp)}$ lies on the line segment $AB$ such that $AP : PB = {m_} : {n_}$\n\nFind the coordinates of $B$", 3)]
        rows = [R("", f"$\\dfrac{{{n_}({A[0]}) + {m_}x_B}}{{{m_ + n_}}} = {fr(Pp[0])}$ oe", "M1"),
                R("", f"$x_B = {B[0]}$", "A1"), R("", f"$y_B = {B[1]}$", "A1")]
        return dict(Q(parts=parts, rows=rows, values={"B": list(B)}, diff="4-6", cw="Find", refs=["8B"]), variant=v)
    if v == "dist":
        A = (r.randint(-9, 9), r.randint(-9, 9))
        B = (r.randint(-9, 9), r.randint(-9, 9))
        d2 = (A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2
        if d2 == 0 or sp.sqrt(d2).is_Integer or tex(sp.sqrt(d2)) == f"\\sqrt{{{d2}}}":
            return None
        M = (sp.Rational(A[0] + B[0], 2), sp.Rational(A[1] + B[1], 2))
        parts = [P("", f"The points $A$ and $B$ have coordinates ${pt(*A)}$ and ${pt(*B)}$ respectively.\n\nFind\n\n(i) the coordinates of the midpoint of $AB$\n\n(ii) the exact length of $AB$, giving your answer as a simplified surd.", 4)]
        rows = [R("", f"(i) ${pt(*M)}$", "B1"),
                R("", f"(ii) $\\sqrt{{({B[0] - A[0]})^2 + ({B[1] - A[1]})^2}}$", "M1"),
                R("", f"$\\sqrt{{{d2}}}$", "A1"), R("", f"${surd(d2)}$", "A1", "cao")]
        return dict(Q(parts=parts, rows=rows, values={"M": list(M), "AB": sp.sqrt(d2)}, diff="1-3", cw="Find", refs=["8A"]), variant=v)
    V = [(r.randint(-8, 8), r.randint(-8, 8)) for _ in range(3)]
    ar = sp.Rational(abs(V[0][0] * (V[1][1] - V[2][1]) + V[1][0] * (V[2][1] - V[0][1]) + V[2][0] * (V[0][1] - V[1][1])), 2)
    if ar < 4:
        return None
    parts = [P("", f"The vertices of triangle $ABC$ are $A{pt(*V[0])}$, $B{pt(*V[1])}$ and $C{pt(*V[2])}$\n\nFind the area of triangle $ABC$", 3)]
    rows = [R("", "$\\dfrac{1}{2}|x_A(y_B - y_C) + x_B(y_C - y_A) + x_C(y_A - y_B)|$ or encloses in a rectangle and subtracts", "M1"),
            R("", "Correct substitution", "M1"), R("", f"${fr(ar)}$", "A1")]
    return dict(Q(parts=parts, rows=rows, values={"area": ar}, diff="4-6", cw="Find", refs=["8A"]), variant=v)


@tpl("coord.points", "multi-part", 22)
def cp_multi(r):
    m_, n_ = _ratio(r)
    A = (r.randint(-8, 4), r.randint(-8, 8))
    B = (A[0] + (m_ + n_) * r.randint(1, 3), A[1] + (m_ + n_) * nz(r, -3, 3))
    C = (r.randint(-8, 10), r.randint(-8, 10))
    D = tuple(sp.Rational(n_ * A[i] + m_ * B[i], m_ + n_) for i in range(2))
    cd2 = (C[0] - D[0]) ** 2 + (C[1] - D[1]) ** 2
    ar = sp.Rational(abs(A[0] * (B[1] - C[1]) + B[0] * (C[1] - A[1]) + C[0] * (A[1] - B[1])), 2)
    if ar < 6 or cd2 == 0:
        return None
    E = (A[0] + C[0] - B[0], A[1] + C[1] - B[1])
    parts = [P("a", f"Find the coordinates of the point $D$ on $AB$ such that $AD : DB = {m_} : {n_}$", 2),
             P("b", "Find the exact length of $CD$", 2),
             P("c", "Find the area of triangle $ABC$", 3),
             P("d", "The point $E$ is such that $ABCE$ is a parallelogram. Find the coordinates of $E$", 2)]
    intro = f"The points $A$, $B$ and $C$ have coordinates ${pt(*A)}$, ${pt(*B)}$ and ${pt(*C)}$ respectively."
    rows = [R("a", "Uses the ratio formula for either coordinate", "M1"), R("a", f"$D{pt(*D)}$", "A1"),
            R("b", f"$\\sqrt{{({fr(C[0] - D[0])})^2 + ({fr(C[1] - D[1])})^2}}$", "M1"), R("b", f"${tex(sp.sqrt(cd2))}$", "A1"),
            R("c", "Determinant or rectangle method", "M1"), R("c", "Correct substitution", "M1"), R("c", f"${fr(ar)}$", "A1"),
            R("d", "Uses $\\overrightarrow{AE} = \\overrightarrow{BC}$ or midpoints of diagonals", "M1"), R("d", f"$E{pt(*E)}$", "A1")]
    return dict(Q(intro=intro, parts=parts, rows=rows, values={"D": list(D), "CD": sp.sqrt(cd2), "area": ar, "E": list(E)},
                  diff="4-6", cw="Find", refs=["8A", "8B"]), variant="ratio")


# =============================================================== 8C-8E lines


@tpl("coord.lines", "short", 22)
def cl_short(r):
    v = r.choice(["two_pts", "perp", "bisector", "meet"])
    A = (r.randint(-8, 8), r.randint(-8, 8))
    B = (r.randint(-8, 8), r.randint(-8, 8))
    if A[0] == B[0] or A[1] == B[1]:
        return None
    m = sp.Rational(B[1] - A[1], B[0] - A[0])
    if v == "two_pts":
        (a, b, c), eq = thru(m, *A)
        parts = [P("", f"Find an equation of the line through $A{pt(*A)}$ and $B{pt(*B)}$\n\nGive your answer in the form $ax + by + c = 0$, where $a$, $b$ and $c$ are integers.", 3)]
        rows = [R("", f"Gradient $= {fr(m)}$", "B1"), R("", f"$y {'-' if A[1] >= 0 else '+'} {abs(A[1])} = {fr(m)}(x {'-' if A[0] >= 0 else '+'} {abs(A[0])})$", "M1"),
                R("", f"${eq}$", "A1", "or any integer multiple")]
        return dict(Q(parts=parts, rows=rows, values={"abc": [a, b, c]}, diff="1-3", cw="Find", refs=["8C"]), variant=v)
    if v == "perp":
        Cp = (r.randint(-8, 8), r.randint(-8, 8))
        (a, b, c), eq = thru(-1 / m, *Cp)
        (a0, b0, c0), eq0 = thru(m, *A)
        parts = [P("", f"The line $l_1$ has equation ${eq0}$\n\nThe line $l_2$ is perpendicular to $l_1$ and passes through the point ${pt(*Cp)}$\n\nWrite an equation of $l_2$ as $ax + by + c = 0$, where $a$, $b$ and $c$ are integers.", 4)]
        rows = [R("", f"Gradient of $l_1 = {fr(m)}$", "B1"), R("", f"Gradient of $l_2 = {fr(-1 / m)}$", "M1", "uses $m_1 m_2 = -1$"),
                R("", "Uses their perpendicular gradient with the given point", "M1"), R("", f"${eq}$", "A1")]
        return dict(Q(parts=parts, rows=rows, values={"abc": [a, b, c]}, diff="4-6", cw="Find", refs=["8C", "8D"]), variant=v)
    if v == "bisector":
        M = (sp.Rational(A[0] + B[0], 2), sp.Rational(A[1] + B[1], 2))
        (a, b, c), eq = thru(-1 / m, *M)
        parts = [P("", f"The points $A$ and $B$ have coordinates ${pt(*A)}$ and ${pt(*B)}$\n\nFind an equation of the perpendicular bisector of $AB$, giving your answer in the form $ax + by + c = 0$ where $a$, $b$ and $c$ are integers.", 5)]
        rows = [R("", f"Midpoint ${pt(*M)}$", "B1"), R("", f"Gradient $AB = {fr(m)}$", "B1"),
                R("", f"Perpendicular gradient ${fr(-1 / m)}$", "M1"), R("", "Line through their midpoint with their perpendicular gradient", "M1"),
                R("", f"${eq}$", "A1")]
        return dict(Q(parts=parts, rows=rows, values={"abc": [a, b, c]}, diff="4-6", cw="Find", refs=["8A", "8C", "8D"]), variant=v)
    X = (r.randint(-6, 6), r.randint(-6, 6))
    m1, m2 = sp.Rational(nz(r, -5, 5), r.choice([1, 1, 2, 3])), sp.Rational(nz(r, -5, 5), r.choice([1, 2]))
    if m1 == m2:
        return None
    (a1, b1, c1), e1 = thru(m1, *X)
    (a2, b2, c2), e2 = thru(m2, *X)
    parts = [P("", f"Find the coordinates of the point of intersection of the lines with equations ${e1}$ and ${e2}$", 3)]
    rows = [R("", "Eliminates one variable", "M1"), R("", f"$x = {X[0]}$", "A1"), R("", f"$y = {X[1]}$", "A1")]
    return dict(Q(parts=parts, rows=rows, values={"point": list(X)}, diff="1-3", cw="Find", refs=["8C", "8E"]), variant=v)


@tpl("coord.lines", "multi-part", 22)
def cl_multi(r):
    # A on y-axis side, B; line through B perpendicular to AB meets x-axis at C
    A = (r.randint(-6, 2), r.randint(-6, 8))
    B = (A[0] + r.randint(2, 7), A[1] + nz(r, -6, 6))
    m = sp.Rational(B[1] - A[1], B[0] - A[0])
    mp = -1 / m
    (a, b, c), eq = thru(mp, *B)
    # intersection with x-axis: y = 0
    Cx = sp.solve(a * x + c, x)[0]
    C = (Cx, 0)
    if Cx.q > 4 or abs(Cx) > 40:
        return None
    ar = sp.Rational(abs(A[0] * (B[1] - C[1]) + B[0] * (C[1] - A[1]) + C[0] * (A[1] - B[1])), 2)
    if ar == 0:
        return None
    (aa, bb, cc), eqAB = thru(m, *A)
    xs = [A[0], B[0], float(Cx), 0]
    ys = [A[1], B[1], 0, 0]
    ax_ = Axes((min(xs) - 2, max(xs) + 2), (min(ys) - 2, max(ys) + 2), 320, 240)
    ax_.axes()
    ax_.items.append(f'<line x1="{ax_.X(A[0]):.1f}" y1="{ax_.Y(A[1]):.1f}" x2="{ax_.X(B[0]):.1f}" y2="{ax_.Y(B[1]):.1f}" stroke-width="1.4"/>')
    ax_.items.append(f'<line x1="{ax_.X(B[0]):.1f}" y1="{ax_.Y(B[1]):.1f}" x2="{ax_.X(float(Cx)):.1f}" y2="{ax_.Y(0):.1f}" stroke-width="1.4"/>')
    ax_.point(A[0], A[1], "A")
    ax_.point(B[0], B[1], "B")
    ax_.point(float(Cx), 0, "C", dy=14)
    fg = fig(ax_.svg(), 70)
    intro = (f"$A$ is the point ${pt(*A)}$ and $B$ is the point ${pt(*B)}$\n\n"
             "The line $l$ passes through $B$ and is perpendicular to $AB$. The line $l$ meets the $x$-axis at the point $C$")
    parts = [P("a", "Find the gradient of $AB$", 1),
             P("b", "Write an equation of $l$ as $ax + by + c = 0$, with $a$, $b$ and $c$ integers.", 3),
             P("c", "Find the coordinates of $C$", 1),
             P("d", "Find the area of triangle $ABC$", 3)]
    AB2 = (B[0] - A[0]) ** 2 + (B[1] - A[1]) ** 2
    BC2 = (B[0] - Cx) ** 2 + B[1] ** 2
    rows = [R("a", f"${fr(m)}$", "B1"),
            R("b", f"Gradient of $l = {fr(mp)}$", "M1"), R("b", "Uses $B$ with their perpendicular gradient", "M1"), R("b", f"${eq}$", "A1"),
            R("c", f"${pt(*C)}$", "B1", "ft their $l$"),
            R("d", f"$AB = {tex(sp.sqrt(AB2))}$ and $BC = {tex(sp.sqrt(BC2))}$, or the determinant method", "M1"),
            R("d", "$\\dfrac{1}{2} \\times AB \\times BC$ (right angle at $B$)", "M1"),
            R("d", f"${fr(ar)}$", "A1")]
    assert sp.simplify(sp.sqrt(AB2) * sp.sqrt(BC2) / 2 - ar) == 0
    return dict(Q(intro=intro, figs=[fg], parts=parts, rows=rows, values={"m": m, "abc": [a, b, c], "C": list(C), "area": ar},
                  diff="4-6", cw="Find", refs=["8C", "8D"]), variant="perp")


@tpl("coord.lines", "show-that", 22)
def cl_show(r):
    v = r.choice(["right", "on_line", "equation"])
    if v == "right":
        B = (r.randint(-5, 5), r.randint(-5, 5))
        d1 = (nz(r, -4, 4), nz(r, -4, 4))
        kk = r.choice([1, 2, -1, -2, sp.Rational(1, 2)])
        d2 = (-d1[1] * kk, d1[0] * kk)
        if any(sp.Rational(t).q != 1 for t in d2):
            return None
        A = (B[0] + d1[0], B[1] + d1[1])
        C = (B[0] + d2[0], B[1] + d2[1])
        if A[0] == B[0] or C[0] == B[0]:
            return None
        mAB = sp.Rational(A[1] - B[1], A[0] - B[0])
        mBC = sp.Rational(C[1] - B[1], C[0] - B[0])
        ar = sp.Rational(abs(A[0] * (B[1] - C[1]) + B[0] * (C[1] - A[1]) + C[0] * (A[1] - B[1])), 2)
        parts = [P("a", f"The points $A{pt(*A)}$, $B{pt(*B)}$ and $C{pt(*C)}$ are the vertices of a triangle.\n\nShow that angle $ABC = 90^\\circ$", 3),
                 P("b", "Find the area of triangle $ABC$", 2)]
        rows = [R("a", f"Gradient $AB = {fr(mAB)}$", "B1"), R("a", f"Gradient $BC = {fr(mBC)}$", "B1"),
                R("a", f"${fr(mAB)} \\times {fr(mBC) if mBC > 0 else '(' + fr(mBC) + ')'} = -1$ so $AB$ is perpendicular to $BC$", "A1", "cso; conclusion required"),
                R("b", "$\\dfrac{1}{2} \\times AB \\times BC$", "M1"), R("b", f"${fr(ar)}$", "A1")]
        assert mAB * mBC == -1
        return dict(Q(parts=parts, rows=rows, values={"mAB": mAB, "mBC": mBC, "area": ar}, diff="4-6", cw="Show that",
                      refs=["8C", "8D"]), variant=v)
    A = (r.randint(-8, 8), r.randint(-8, 8))
    B = (r.randint(-8, 8), r.randint(-8, 8))
    if A[0] == B[0] or A[1] == B[1]:
        return None
    M = (sp.Rational(A[0] + B[0], 2), sp.Rational(A[1] + B[1], 2))
    m = sp.Rational(B[1] - A[1], B[0] - A[0])
    (a, b, c), eq = thru(-1 / m, *M)
    if v == "equation":
        ty = sp.solve(a * x + b * y + c, y)
        yint = [t.subs(x, 0) for t in ty][0]
        parts = [P("a", f"The points $A$ and $B$ have coordinates ${pt(*A)}$ and ${pt(*B)}$\n\nShow that the perpendicular bisector of $AB$ has equation ${eq}$", 4),
                 P("b", "The perpendicular bisector meets the $y$-axis at $D$. Find the coordinates of $D$", 1)]
        rows = [R("a", f"Midpoint ${pt(*M)}$", "B1"), R("a", f"Perpendicular gradient ${fr(-1 / m)}$", "M1"),
                R("a", f"$y - {fr(M[1])} = {fr(-1 / m)}(x - {fr(M[0])})$".replace("- -", "+ "), "M1"),
                R("a", f"${eq}$", "A1", "cso"),
                R("b", f"$(0, {fr(yint)})$", "B1")]
        return dict(Q(parts=parts, rows=rows, values={"abc": [a, b, c], "D": [0, yint]}, diff="4-6", cw="Show that",
                      refs=["8C", "8D"]), variant=v)
    # on_line: show point C equidistant from A and B lies on bisector; find point on bisector with given x
    t0 = nz(r, -3, 3)
    Cp = (M[0] - b * t0, M[1] + a * t0)
    dA = (Cp[0] - A[0]) ** 2 + (Cp[1] - A[1]) ** 2
    parts = [P("a", f"The points $A$ and $B$ have coordinates ${pt(*A)}$ and ${pt(*B)}$. The point $C$ has coordinates ${pt(*Cp)}$\n\nShow that $CA = CB$", 3),
             P("b", f"Hence show that $C$ lies on the line with equation ${eq}$", 2)]
    rows = [R("a", "Uses the distance formula for $CA$ or $CB$", "M1"),
            R("a", f"$CA^2 = {fr(dA)}$", "A1"), R("a", f"$CB^2 = {fr(dA)}$ so $CA = CB$", "A1", "cso"),
            R("b", "$C$ is equidistant from $A$ and $B$ so lies on the perpendicular bisector, or substitutes into the equation", "M1"),
            R("b", f"${tex(a * Cp[0])} {'+' if b * Cp[1] >= 0 else '-'} {tex(abs(b * Cp[1]))} {'+' if c >= 0 else '-'} {abs(c)} = 0$", "A1", "cso")]
    assert a * Cp[0] + b * Cp[1] + c == 0 and dA == (Cp[0] - B[0]) ** 2 + (Cp[1] - B[1]) ** 2
    return dict(Q(parts=parts, rows=rows, values={"CA2": dA}, diff="4-6", cw="Show that", refs=["8A", "8C", "8D"]), variant=v)
