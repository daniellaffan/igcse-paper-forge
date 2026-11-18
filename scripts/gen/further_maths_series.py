"""4PM1 templates: 5 series (sigma, AP, GP) and 6 binomial series."""
import math
from fractions import Fraction as F

import sympy as sp

from further_maths_util import tpl, P, R, Q, tex, sf, dp, fr, sg, poly, lin, nz, pick, x, n, name_ctx, ordinal, xpow

rr = sp.Symbol("r")


def ap_sum(a, d, N):
    return sp.Integer(N) / 2 * (2 * a + (N - 1) * d) if isinstance(N, int) else N / 2 * (2 * a + (N - 1) * d)


def gp_sum(a, q, N):
    a, q = sp.nsimplify(a), sp.nsimplify(q)
    return a * (1 - q ** N) / (1 - q)


def asc(cs, start=0, var="x"):
    """Ascending-power string from a coefficient list (index = power - start offset)."""
    out = ""
    for j, c in enumerate(cs):
        c = sp.nsimplify(c)
        if c == 0:
            continue
        pw = j + start
        mon = "" if pw == 0 else var if pw == 1 else f"{var}^{{{pw}}}"
        mag = abs(c)
        ms = fr(mag)
        if mon and mag == 1:
            ms = ""
        body = f"{ms}{' ' if ms and mon and mag.q != 1 else ''}{mon}" if mon else ms
        if not out:
            out = ("-" if c < 0 else "") + body
        else:
            out += (" - " if c < 0 else " + ") + body
    return out or "0"


# =============================================================== 5A sigma


@tpl("series.sigma", "short", 22)
def ss_short(r):
    v = r.choice(["ap", "gp", "range", "inf"])
    if v == "ap":
        a, b = nz(r, -5, 7), r.randint(-9, 9)
        N = r.randint(12, 40)
        val = sum(a * j + b for j in range(1, N + 1))
        parts = [P("", f"Evaluate $$\\sum_{{r=1}}^{{{N}}} ({lin(a, b, 'r')})$$", 3)]
        rows = [R("", f"Identifies an arithmetic series with $a = {a + b}$, $d = {a}$, $n = {N}$", "M1"),
                R("", f"$\\dfrac{{{N}}}{{2}}[2({a + b}) + {N - 1}({a})]$", "M1"),
                R("", f"${val}$", "A1", "cao")]
        return dict(Q(parts=parts, rows=rows, values={"sum": val}, diff="4-6", cw="Evaluate", refs=["5A", "5B"]), variant=v)
    if v == "range":
        a, b = nz(r, 1, 6), r.randint(-9, 9)
        m = r.randint(5, 20)
        N = m + r.randint(10, 30)
        val = sum(a * j + b for j in range(m, N + 1))
        parts = [P("", f"Find the value of $$\\sum_{{r={m}}}^{{{N}}} ({lin(a, b, 'r')})$$", 4)]
        rows = [R("", f"First term ${a * m + b}$, last term ${a * N + b}$", "B1"),
                R("", f"Number of terms $= {N - m + 1}$", "B1"),
                R("", f"$\\dfrac{{{N - m + 1}}}{{2}}({a * m + b} + {a * N + b})$ or $S_{{{N}}} - S_{{{m - 1}}}$", "M1"),
                R("", f"${val}$", "A1", "cao")]
        return dict(Q(parts=parts, rows=rows, values={"sum": val}, diff="4-6", cw="Find", refs=["5A", "5B"]), variant=v)
    if v == "gp":
        c = r.randint(1, 6)
        q = r.choice([2, 3, -2])
        N = r.randint(6, 12)
        val = sum(c * q ** (j - 1) for j in range(1, N + 1))
        parts = [P("", f"Evaluate $$\\sum_{{r=1}}^{{{N}}} {c if c > 1 else ''}({q})^{{r - 1}}$$", 3)]
        rows = [R("", f"Geometric with $a = {c}$, $r = {q}$", "M1"),
                R("", f"$\\dfrac{{{c}(1 - ({q})^{{{N}}})}}{{1 - ({q})}}$", "M1"),
                R("", f"${val}$", "A1")]
        return dict(Q(parts=parts, rows=rows, values={"sum": val}, diff="4-6", cw="Evaluate", refs=["5A", "5B"]), variant=v)
    c = r.randint(2, 30)
    q = sp.Rational(r.choice([1, 2, 1, 3]), r.choice([2, 3, 4, 5]))
    if q >= 1:
        return None
    sign = r.choice([1, -1])
    q = q * sign
    val = c * q / (1 - q)
    parts = [P("", f"Find the exact value of $$\\sum_{{r=1}}^{{\\infty}} {c}\\left({fr(q)}\\right)^{{r}}$$", 3)]
    rows = [R("", f"First term $a = {fr(c * q)}$, common ratio ${fr(q)}$", "B1"),
            R("", f"$\\dfrac{{{fr(c * q)}}}{{1 - ({fr(q)})}}$", "M1"),
            R("", f"${fr(val)}$", "A1")]
    return dict(Q(parts=parts, rows=rows, values={"sum": val}, diff="4-6", cw="Find", refs=["5A", "5B"]), variant=v)


@tpl("series.sigma", "show-that", 22)
def ss_show(r):
    a, b = r.randint(2, 9), r.randint(-9, 9)
    S = sp.expand(sp.summation(a * rr + b, (rr, 1, n)))
    # show S = n/2 (a n + a + 2b)
    form = f"\\dfrac{{n}}{{2}}({lin(a, a + 2 * b, 'n')})"
    assert sp.simplify(S - n / 2 * (a * n + a + 2 * b)) == 0
    v = r.choice(["find_n", "range"])
    parts = [P("a", f"Show that $$\\sum_{{r=1}}^{{n}} ({lin(a, b, 'r')}) = {form}$$", 3)]
    rows = [R("a", f"$a = {a + b}$, $d = {a}$", "B1"),
            R("a", f"$\\dfrac{{n}}{{2}}[2({a + b}) + (n - 1)({a})]$", "M1"),
            R("a", f"$= {form}$", "A1", "cso")]
    if v == "find_n":
        N = r.randint(15, 60)
        T_ = int(S.subs(n, N))
        parts.append(P("b", f"Given that $\\sum_{{r=1}}^{{n}} ({lin(a, b, 'r')}) = {T_}$, find the value of $n$", 3, prefix="n = "))
        other = [s_ for s_ in sp.solve(S - T_, n) if s_ != N]
        rows += [R("b", f"${tex(sp.expand(2 * S))} = {2 * T_}$", "M1", "forms a 3-term quadratic in $n$"),
                 R("b", "Solves their quadratic", "M1"),
                 R("b", f"$n = {N}$", "A1", f"rejects $n = {tex(other[0])}$" if other else None)]
        vals = {"n": N}
    else:
        m = r.randint(10, 30)
        N = m + r.randint(15, 40)
        val = int(S.subs(n, N) - S.subs(n, m - 1))
        parts.append(P("b", f"Hence, or otherwise, find the value of $\\sum_{{r={m}}}^{{{N}}} ({lin(a, b, 'r')})$", 3))
        rows += [R("b", f"$S_{{{N}}} - S_{{{m - 1}}}$", "M1", "allow $S_{" + str(N) + "} - S_{" + str(m) + "}$ for M1"),
                 R("b", f"${int(S.subs(n, N))} - {int(S.subs(n, m - 1))}$", "M1"),
                 R("b", f"${val}$", "A1")]
        vals = {"sum": val}
    return dict(Q(parts=parts, rows=rows, values=vals, diff="4-6", cw="Show that", refs=["5A", "5B"]), variant=v)


# =============================================================== 5B arithmetic


@tpl("series.ap", "short", 22)
def sa_short(r):
    v = r.choice(["two_terms", "sum_n", "last"])
    a, d = r.randint(-10, 20), nz(r, -5, 8)
    if v == "two_terms":
        p_, q_ = sorted(r.sample(range(3, 16), 2))
        N = r.randint(20, 50)
        up, uq = a + (p_ - 1) * d, a + (q_ - 1) * d
        S = ap_sum(a, d, N)
        parts = [P("", f"The {ordinal(p_)} term of an arithmetic series is ${up}$ and the {ordinal(q_)} term is ${uq}$\n\nFind the sum of the first {N} terms of the series.", 5)]
        rows = [R("", f"$a + {p_ - 1}d = {up}$, $a + {q_ - 1}d = {uq}$", "M1"),
                R("", f"$d = {d}$", "A1"), R("", f"$a = {a}$", "A1"),
                R("", f"$\\dfrac{{{N}}}{{2}}[2({a}) + {N - 1}({d})]$", "M1"),
                R("", f"$S_{{{N}}} = {S}$", "A1")]
        return dict(Q(parts=parts, rows=rows, values={"a": a, "d": d, "S": S}, diff="4-6", cw="Find", refs=["5B"]), variant=v)
    if v == "sum_n":
        if d <= 0 or a <= 0:
            return None
        N = r.randint(10, 40)
        S = ap_sum(a, d, N)
        other = [s_ for s_ in sp.solve(ap_sum(a, d, n) - S, n) if s_ != N]
        parts = [P("", f"An arithmetic series has first term ${a}$ and common difference ${d}$\n\nThe sum of the first $n$ terms is ${S}$\n\nFind the value of $n$", 4, prefix="n = ")]
        rows = [R("", f"$\\dfrac{{n}}{{2}}[{2 * a} + (n - 1)({d})] = {S}$", "M1"),
                R("", f"${tex(sp.expand(2 * ap_sum(a, d, n)))} = {2 * S}$", "A1", "3-term quadratic"),
                R("", "Solves their quadratic", "M1"),
                R("", f"$n = {N}$", "A1", "negative root rejected")]
        return dict(Q(parts=parts, rows=rows, values={"n": N, "other": other}, diff="4-6", cw="Find", refs=["5B"]), variant=v)
    N = r.randint(12, 45)
    L_ = a + (N - 1) * d
    S = ap_sum(a, d, N)
    parts = [P("a", f"An arithmetic series has first term ${a}$ and last term ${L_}$. The common difference is ${d}$\n\nFind the number of terms in the series.", 2, prefix="n = "),
             P("b", "Find the sum of the series.", 2)]
    rows = [R("a", f"${a} + (n - 1)({d}) = {L_}$", "M1"), R("a", f"$n = {N}$", "A1"),
            R("b", f"$\\dfrac{{{N}}}{{2}}({a} + {L_})$", "M1"), R("b", f"${S}$", "A1")]
    return dict(Q(parts=parts, rows=rows, values={"n": N, "S": S}, diff="1-3", cw="Find", refs=["5B"]), variant=v)


@tpl("series.ap", "multi-part", 22)
def sa_multi(r):
    a, d = r.randint(2, 15), r.randint(2, 7)
    p_ = r.randint(3, 8)
    q_ = r.randint(10, 20)
    # u_p and S_q give dependent equations when S_q = q * u_p, i.e. 2p = q + 1 (determinant q + 1 - 2p = 0)
    if 2 * p_ == q_ + 1:
        return None
    S_q = ap_sum(a, d, q_)
    up = a + (p_ - 1) * d
    Sn = sp.expand(ap_sum(a, d, n))
    K = r.choice([1000, 1500, 2000, 2500, 3000, 5000])
    sol = max(float(s_) for s_ in sp.solve(Sn - K, n))
    least = math.floor(sol) + 1
    if Sn.subs(n, least - 1) > K:
        return None
    parts = [P("a", f"Find the value of $a$ and the value of $d$", 5),
             P("b", f"Show that the sum of the first $n$ terms of the series is ${tex(Sn)}$", 2),
             P("c", f"Find the least value of $n$ for which the sum of the first $n$ terms exceeds {K}", 4, prefix="n = ")]
    intro = (f"The {ordinal(p_)} term of an arithmetic series is {up} and the sum of the first {q_} terms of the series is {S_q}\n\n"
             "The first term of the series is $a$ and the common difference is $d$")
    rows = [R("a", f"$a + {p_ - 1}d = {up}$", "B1"),
            R("a", f"$\\dfrac{{{q_}}}{{2}}[2a + {q_ - 1}d] = {S_q}$", "M1 A1"),
            R("a", "Solves simultaneously", "M1"),
            R("a", f"$a = {a}$, $d = {d}$", "A1"),
            R("b", f"$\\dfrac{{n}}{{2}}[{2 * a} + (n - 1){d}]$", "M1"),
            R("b", f"$= {tex(Sn)}$", "A1", "cso"),
            R("c", f"${tex(Sn)} > {K}$", "M1"),
            R("c", "Solves the quadratic equation or inequality", "M1"),
            R("c", f"$n = {sf(sol, 4)}$", "A1"),
            R("c", f"$n = {least}$", "A1", "cao")]
    return dict(Q(intro=intro, parts=parts, rows=rows, values={"a": a, "d": d, "Sn": str(Sn), "least_n": least},
                  diff="7-9", cw="Find", refs=["5B"]), variant="ap")


AP_CTX = [
    ("saves", "In month 1, {nm} saves \\${a}. Each month after that, {nm} saves \\${d} more than in the previous month.", "\\$"),
    ("run", "{nm} is training for a race. On day 1 {nm} runs {a} km. On each following day, {nm} runs {d} km further than on the previous day.", "km"),
    ("seats", "A theatre has rows of seats. The front row has {a} seats and each row after the first has {d} more seats than the row in front of it.", "seats"),
    ("bricks", "A builder stacks bricks in layers. The bottom layer has {a} bricks and each layer above has {d} fewer bricks than the layer below.", "bricks"),
]


@tpl("series.ap", "applied", 22)
def sa_applied(r):
    key, txt, unit = r.choice(AP_CTX)
    nm = name_ctx(r)
    if key == "bricks":
        d0 = r.randint(2, 4)
        layers = r.randint(10, 25)
        a = d0 * layers + r.randint(1, d0)
        d = -d0
    elif key == "run":
        a, d = r.choice([F(3, 2), 2, F(5, 2), 3]), r.choice([F(1, 2), F(1, 4), F(3, 4)])
    else:
        a, d = r.randint(10, 60), r.randint(2, 15)
    a_, d_ = sp.Rational(a), sp.Rational(d)
    intro = txt.format(nm=nm, a=fr(a_).replace("\\frac", "\\tfrac") if a_.q != 1 else a_, d=fr(abs(d_)) if d_.q != 1 else abs(d_))
    intro = intro.replace("\\tfrac{3}{2}", "1.5").replace("\\tfrac{5}{2}", "2.5").replace("\\frac{1}{2}", "0.5").replace("\\frac{1}{4}", "0.25").replace("\\frac{3}{4}", "0.75")
    N1 = r.randint(8, 20)
    uN = a_ + (N1 - 1) * d_
    N2 = r.randint(N1 + 2, N1 + 15)
    SN = ap_sum(a_, d_, N2)
    word = {"saves": ("month", "save", "saved"), "run": ("day", "run", "run"), "seats": ("row", "have", "in the first"),
            "bricks": ("layer", "contain", "used in the first")}[key]
    if key == "bricks":
        top = a_ + (N2 - 1) * d_
        if top <= 0:
            return None
    T = sp.Rational(r.randint(int(SN * 1.3), int(SN * 1.8))) if key != "bricks" else None
    parts = [P("a", f"Find the amount {nm} saves in month {N1}." if key == "saves" else f"Find the number of {unit} in {word[0]} {N1}." if key != "run" else f"Find the distance {nm} runs on day {N1}.", 2),
             P("b", {"saves": f"Find the total amount {nm} saves in the first {N2} months.", "run": f"Find the total distance {nm} runs in the first {N2} days.",
                   "seats": f"Find the total number of seats in the first {N2} rows.", "bricks": f"Find the total number of bricks in the first {N2} layers."}[key], 2)]
    rows = [R("a", f"${fr(a_)} + {N1 - 1} \\times {'(' + fr(d_) + ')' if d_ < 0 else fr(d_)}$", "M1"),
            R("a", f"${dp(uN, 2) if uN.q != 1 else uN}$ {unit if key != 'saves' else ''}".replace("$ \\$", "$"), "A1"),
            R("b", f"$\\dfrac{{{N2}}}{{2}}[2({fr(a_)}) + {N2 - 1}({fr(d_)})]$", "M1"),
            R("b", f"${dp(SN, 2) if SN.q != 1 else SN}$", "A1")]
    vals = {"term": uN, "sum": SN}
    if T is not None:
        sols = [s_ for s_ in sp.solve(ap_sum(a_, d_, n) - T, n) if s_.is_real and s_ > 0]
        M = math.floor(float(sols[0])) + 1
        parts.append(P("c", f"Find the number of {word[0]}s needed for the total to first exceed {T}{' ' + unit if key != 'saves' else ''}".replace(f"{T}", f"\\${T}" if key == "saves" else f"{T}"), 4))
        rows += [R("c", f"$\\dfrac{{n}}{{2}}[2({fr(a_)}) + (n - 1)({fr(d_)})] > {T}$", "M1"),
                 R("c", f"${tex(sp.expand(2 * ap_sum(a_, d_, n) * (4 if d_.q > 1 or a_.q > 1 else 1)))} > {2 * T * (4 if d_.q > 1 or a_.q > 1 else 1)}$", "A1", "oe 3-term quadratic"),
                 R("c", f"Solves to get $n = {sf(sols[0], 4)}$", "M1"),
                 R("c", f"${M}$ {word[0]}s", "A1", "cao")]
        vals["n"] = M
    else:
        top = a_ + (N2 - 1) * d_
        last = math.floor((a_ - 1) / (-d_)) + 1
        parts.append(P("c", "The builder keeps adding layers, following the same pattern, for as long as possible. Find the number of bricks in the top layer.", 2))
        rows += [R("c", f"${a_} - {-d_}(n - 1) > 0$ so $n = {last}$", "M1"), R("c", f"${a_ + (last - 1) * d_}$", "A1")]
        vals["top"] = a_ + (last - 1) * d_
    return dict(Q(intro=intro, parts=parts, rows=rows, values=vals, diff="4-6", cw="Find", refs=["5B"]), variant=key)


# =============================================================== 5B geometric


@tpl("series.gp", "short", 22)
def sg_short(r):
    v = r.choice(["terms", "inf", "inf_r"])
    if v == "terms":
        a = r.randint(1, 9) * r.choice([1, 2, 4])
        q = r.choice([2, 3, -2, sp.Rational(1, 2), sp.Rational(-1, 2), sp.Rational(3, 2)])
        p_, s_ = r.choice([(2, 5), (3, 6), (2, 4), (1, 4)])
        up, us = a * q ** (p_ - 1), a * q ** (s_ - 1)
        N = r.randint(6, 12)
        S = gp_sum(a, q, N)
        parts = [P("", f"The {['', 'first', 'second', 'third'][p_]} term of a geometric series is ${fr(up)}$ and the {['', '', '', '', 'fourth', 'fifth', 'sixth'][s_]} term is ${fr(us)}$\n\nFind\n\n(i) the common ratio\n\n(ii) the sum of the first {N} terms, giving your answer to 3 significant figures if it is not exact.", 5)]
        rows = [R("", f"(i) $r^{{{s_ - p_}}} = \\dfrac{{{fr(us)}}}{{{fr(up)}}}$", "M1"),
                R("", f"(i) $r = {fr(q)}$", "A1", "must consider sign if the power is even"),
                R("", f"(ii) $a = {fr(a)}$", "B1"),
                R("", f"(ii) $\\dfrac{{{fr(a)}(1 - ({fr(q)})^{{{N}}})}}{{1 - ({fr(q)})}}$", "M1"),
                R("", f"(ii) ${fr(S) if S.q == 1 else sf(S, 3)}$", "A1")]
        if (s_ - p_) % 2 == 0:
            return None
        return dict(Q(parts=parts, rows=rows, values={"r": q, "S": S}, diff="4-6", cw="Find", refs=["5B"]), variant=v)
    if v == "inf":
        a = r.randint(2, 40)
        q = sp.Rational(r.randint(1, 4), r.randint(5, 6)) * r.choice([1, -1])
        Sinf = a / (1 - q)
        N = r.randint(4, 9)
        parts = [P("a", f"A geometric series has first term ${a}$ and common ratio ${fr(q)}$\n\nFind the sum to infinity of the series.", 2),
                 P("b", f"Find the difference between the sum to infinity and the sum of the first {N} terms. Give your answer to 3 significant figures.", 3)]
        diff_ = Sinf - gp_sum(a, q, N)
        rows = [R("a", f"$\\dfrac{{{a}}}{{1 - ({fr(q)})}}$", "M1"), R("a", f"${fr(Sinf)}$", "A1"),
                R("b", f"$S_{{{N}}} = \\dfrac{{{a}(1 - ({fr(q)})^{{{N}}})}}{{1 - ({fr(q)})}}$", "M1"),
                R("b", f"$S_\\infty - S_{{{N}}}$", "M1", "dM1"),
                R("b", f"${sf(diff_)}$", "A1", "awrt; allow negative of this value if the sum is negative")]
        return dict(Q(parts=parts, rows=rows, values={"Sinf": Sinf, "difference": diff_}, diff="4-6", cw="Find", refs=["5B"]), variant=v)
    a = r.randint(2, 30)
    q = sp.Rational(r.randint(1, 4), 5) * r.choice([1, -1])
    Sinf = a / (1 - q)
    if Sinf.q > 6:
        return None
    parts = [P("", f"The first term of a convergent geometric series is ${a}$ and its sum to infinity is ${fr(Sinf)}$\n\nFind the common ratio and the third term of the series.", 4)]
    rows = [R("", f"$\\dfrac{{{a}}}{{1 - r}} = {fr(Sinf)}$", "M1"), R("", f"$r = {fr(q)}$", "A1"),
            R("", f"$u_3 = {a}({fr(q)})^2$", "M1"), R("", f"${fr(a * q ** 2)}$", "A1")]
    return dict(Q(parts=parts, rows=rows, values={"r": q, "u3": a * q ** 2}, diff="4-6", cw="Find", refs=["5B"]), variant=v)


@tpl("series.gp", "multi-part", 22)
def sg_multi(r):
    # u2 = A, Sinf = B -> a r = A, a/(1-r) = B  -> B r (1 - r) = A
    q = sp.Rational(r.randint(1, 4), r.choice([5, 4, 3])) * r.choice([1, 1, -1])
    if abs(q) >= 1:
        return None
    a = sp.Rational(r.choice([12, 18, 24, 30, 36, 40, 45, 48, 60, 72, 80, 96]))
    A, B = a * q, a / (1 - q)
    if A.q != 1 or B.q > 3:
        return None
    others = [s_ for s_ in sp.solve(B * rr * (1 - rr) - A, rr) if s_ != q]
    eps = r.choice([sp.Rational(1, 10), sp.Rational(1, 100), sp.Rational(1, 2)])
    # Sinf - Sn = B q^n < eps -> n > log(eps/B)/log|q|
    nmin = math.floor(math.log(float(eps / B)) / math.log(abs(float(q)))) + 1
    if q < 0:
        nmin = next(N for N in range(1, 200) if abs(B * q ** N) < eps)
    else:
        assert B * q ** nmin < eps and B * q ** (nmin - 1) >= eps
    C = sp.expand(B * rr * (1 - rr) - A)
    lc = sp.ilcm(*[sp.Rational(c_).q for c_ in sp.Poly(C, rr).coeffs()])
    Ce = sp.expand(-C * lc)
    if not others:
        btxt = "Find the value of $r$"  # repeated root: nothing to reject
    elif abs(others[0]) < 1:
        btxt = "Given that the series is convergent and that more than one value of $r$ is possible, find the possible values of $r$"
    else:
        btxt = "Find the value of $r$, explaining why any other value is rejected."
    parts = [P("a", f"Show that ${tex(Ce)} = 0$", 3),
             P("b", btxt, 2),
             P("c", f"For the value of $r$ equal to ${fr(q)}$, find the smallest value of $n$ for which $S_\\infty - S_n < {fr(eps)}$", 4, prefix="n = ")]
    intro = f"The second term of a geometric series is ${fr(A)}$ and the sum to infinity of the series is ${fr(B)}$\n\nThe common ratio of the series is $r$ and the sum of the first $n$ terms is $S_n$"
    rows = [R("a", f"$ar = {fr(A)}$ and $\\dfrac{{a}}{{1 - r}} = {fr(B)}$", "B1"),
            R("a", "Eliminates $a$", "M1"),
            R("a", f"${tex(Ce)} = 0$", "A1", "cso"),
            R("b", "Solves the quadratic", "M1"),
            R("b", f"$r = {', '.join(fr(z) for z in sorted([q] + others))}$" + (" (reject any with $|r| \\geqslant 1$)" if others and abs(others[0]) >= 1 else "") + (" (repeated root)" if not others else ""), "A1"),
            R("c", f"$S_\\infty - S_n = \\dfrac{{a r^n}}{{1 - r}} = {fr(B)}({fr(q)})^n$", "M1"),
            R("c", f"${fr(B)}{'|' if q < 0 else ''}({fr(q)})^n{'|' if q < 0 else ''} < {fr(eps)}$", "M1", "uses logs or trial"),
            R("c", f"$n > {sf(math.log(float(eps / B)) / math.log(abs(float(q))), 4)}$", "A1"),
            R("c", f"$n = {nmin}$", "A1", "cao")]
    return dict(Q(intro=intro, parts=parts, rows=rows, values={"r": [q] + others, "a": a, "n": nmin}, diff="7-9",
                  cw="Show that", refs=["5B", "1B"]), variant="sinf")


@tpl("series.gp", "applied", 22)
def sg_applied(r):
    v = r.choice(["salary", "ball", "value"])
    nm = name_ctx(r)
    if v == "ball":
        h = r.choice([2, 3, 4, 5, 6, 8, 10])
        q = sp.Rational(r.choice([3, 2, 4, 3]), r.choice([4, 5, 5, 5]))
        if q >= 1:
            return None
        tot = h + 2 * h * q / (1 - q)
        kb = r.randint(3, 6)
        hk = h * q ** kb
        intro = f"A ball is dropped from a height of {h} m onto horizontal ground. After each bounce it rises to ${fr(q)}$ of the height from which it last fell."
        parts = [P("a", f"Find the height the ball reaches after the {['', '', '', 'third', 'fourth', 'fifth', 'sixth'][kb]} bounce, in metres to 3 significant figures.", 2),
                 P("b", "Find the total distance the ball travels before coming to rest, assuming it keeps bouncing indefinitely.", 4)]
        rows = [R("a", f"${h} \\times ({fr(q)})^{{{kb}}}$", "M1"), R("a", f"${sf(hk)}$ m", "A1"),
                R("b", f"Recognises the upward distances form a geometric series with first term ${fr(h * q)}$", "M1"),
                R("b", f"$S_\\infty = \\dfrac{{{fr(h * q)}}}{{1 - {fr(q)}}} = {fr(h * q / (1 - q))}$", "M1 A1"),
                R("b", f"Total $= {h} + 2 \\times {fr(h * q / (1 - q))} = {fr(tot)}$ m", "A1")]
        return dict(Q(intro=intro, parts=parts, rows=rows, values={"height": hk, "total": tot}, diff="7-9", cw="Find", refs=["5B"]), variant=v)
    if v == "salary":
        S0 = r.choice([18000, 22000, 25000, 28000, 30000, 32000])
        pc = r.choice([2, 2.5, 3, 4, 5])
        q = 1 + pc / 100
        N = r.randint(8, 15)
        tot = S0 * (q ** N - 1) / (q - 1)
        T = r.choice([40000, 45000, 50000])
        yr = math.floor(math.log(T / S0) / math.log(q)) + 2
        if yr <= 2:
            return None
        intro = f"{nm} starts a job with an annual salary of \\${S0}. Each year the salary increases by {fmt(pc)}% of the previous year's salary."
        parts = [P("a", f"Find, to the nearest dollar, the total {nm} earns in the first {N} years.", 3),
                 P("b", f"Find the first year in which {nm}'s salary exceeds \\${T}", 3)]
        rows = [R("a", f"$r = {fmt(q)}$", "B1"), R("a", f"$\\dfrac{{{S0}({fmt(q)}^{{{N}}} - 1)}}{{{fmt(q)} - 1}}$", "M1"),
                R("a", f"\\${round(tot)}", "A1", "awrt"),
                R("b", f"${S0} \\times {fmt(q)}^{{n - 1}} > {T}$", "M1"),
                R("b", f"$n - 1 > \\dfrac{{\\log({T}/{S0})}}{{\\log {fmt(q)}}} = {sf(math.log(T / S0) / math.log(q), 4)}$", "M1"),
                R("b", f"Year {yr}", "A1")]
        return dict(Q(intro=intro, parts=parts, rows=rows, values={"total": tot, "year": yr}, diff="7-9", cw="Find", refs=["5B", "1B"]), variant=v)
    V0 = r.choice([12000, 15000, 18000, 24000, 30000])
    pc = r.choice([10, 12, 15, 18, 20])
    q = 1 - pc / 100
    N = r.randint(3, 8)
    VN = V0 * q ** N
    T = r.choice([2000, 3000, 4000, 5000])
    yrs = math.floor(math.log(T / V0) / math.log(q)) + 1
    item = r.choice(["car", "machine", "motorbike", "boat"])
    intro = f"A {item} is bought for \\${V0}. Its value falls by {pc}% each year."
    parts = [P("a", f"Find the value of the {item} after {N} years, to the nearest dollar.", 2),
             P("b", f"Find the number of complete years after which the value of the {item} first falls below \\${T}", 3)]
    rows = [R("a", f"${V0} \\times {fmt(q)}^{{{N}}}$", "M1"), R("a", f"\\${round(VN)}", "A1"),
            R("b", f"${V0} \\times {fmt(q)}^{{n}} < {T}$", "M1"),
            R("b", f"$n > \\dfrac{{\\log({T}/{V0})}}{{\\log {fmt(q)}}} = {sf(math.log(T / V0) / math.log(q), 4)}$", "M1", "note inequality reverses as $\\log " + fmt(q) + " < 0$"),
            R("b", f"${yrs}$ years", "A1")]
    return dict(Q(intro=intro, parts=parts, rows=rows, values={"value": VN, "years": yrs}, diff="4-6", cw="Find", refs=["5B", "1B"]), variant=v)


def fmt(v):
    from common import fmt_num
    return fmt_num(v)


# =============================================================== 6A(i) positive integer


def coeff_series(expr, N):
    s = sp.series(expr, x, 0, N + 1).removeO()
    return [sp.nsimplify(s.coeff(x, j)) for j in range(N + 1)]


@tpl("binom.posint", "short", 22)
def bp_short(r):
    v = r.choice(["first4", "coef", "const"])
    a, b = r.choice([1, 2, 3]), r.choice([1, 2, 3, -1, -2, sp.Rational(1, 2), sp.Rational(-1, 3)])
    N = r.randint(5, 9)
    e = (a + b * x) ** N
    if v == "first4":
        cs = coeff_series(e, 3)
        parts = [P("", f"Find the first four terms, in ascending powers of $x$, of the binomial expansion of $({asc([a, b])})^{{{N}}}$\n\nGive each term in its simplest form.", 4)]
        rows = [R("", f"${fr(cs[0])}$", "B1"),
                R("", f"Correct structure, e.g. $\\binom{{{N}}}{{2}}{a}^{{{N - 2}}}({tex(b * x)})^2$", "M1"),
                R("", f"${asc([0, cs[1], cs[2]])}$", "A1"),
                R("", f"${asc([cs[3]], 3)}$", "A1")]
        return dict(Q(parts=parts, rows=rows, values={"coeffs": cs}, diff="4-6", cw="Find", refs=["6A(i)"]), variant=v)
    if v == "coef":
        j = r.randint(2, min(5, N - 1))
        c = sp.expand(e).coeff(x, j)
        parts = [P("", f"Find the coefficient of $x^{{{j}}}$ in the binomial expansion of $({asc([a, b])})^{{{N}}}$", 3)]
        rows = [R("", f"$\\binom{{{N}}}{{{j}}}$ or ${sp.binomial(N, j)}$ seen", "B1"),
                R("", f"$\\binom{{{N}}}{{{j}}}({a})^{{{N - j}}}({fr(b)})^{{{j}}}$", "M1"),
                R("", f"${fr(c)}$", "A1")]
        return dict(Q(parts=parts, rows=rows, values={"coeff": c}, diff="4-6", cw="Find", refs=["6A(i)"]), variant=v)
    p_ = r.choice([1, 2])
    N = r.choice([4, 6, 8]) if p_ == 1 else r.choice([3, 6, 9])
    c1 = r.choice([1, 2, 3])
    c2 = r.choice([1, 2, 3, -1, -2])
    e = (c1 * x + c2 / x ** p_) ** N
    term = sp.expand(e).coeff(x, 0)
    if term == 0:
        return None
    jj = sp.Rational(N, p_ + 1)
    if jj.q != 1:
        return None
    parts = [P("", f"Find the term independent of $x$ in the expansion of $\\left({tex(c1 * x)} {'+' if c2 > 0 else '-'} \\dfrac{{{abs(c2)}}}{{x{'^' + str(p_) if p_ > 1 else ''}}}\\right)^{{{N}}}$", 4)]
    rows = [R("", f"General term $\\binom{{{N}}}{{r}}({tex(c1 * x)})^{{{N} - r}}\\left(\\dfrac{{{c2}}}{{{xpow(p_)}}}\\right)^r$", "M1"),
            R("", f"Power of $x$: ${N} - r - {p_ if p_ > 1 else ''}r = 0 \\Rightarrow r = {N - jj * p_ if False else int(jj * p_ // p_ * 1) if False else int(N // (p_ + 1))}$", "M1"),
            R("", f"$\\binom{{{N}}}{{{int(jj)}}}({c1})^{{{N - int(jj)}}}({c2})^{{{int(jj)}}}$", "M1"),
            R("", f"${term}$", "A1")]
    return dict(Q(parts=parts, rows=rows, values={"term": term}, diff="7-9", cw="Find", refs=["6A(i)"]), variant=v)


@tpl("binom.posint", "multi-part", 22)
def bp_multi(r):
    N = r.randint(5, 9)
    kk = r.choice([2, 3, -2, sp.Rational(1, 2), -3, sp.Rational(3, 2)])
    K = sp.Symbol("k")
    c1, c2 = N * kk, sp.binomial(N, 2) * kk ** 2
    c1s, c2s = tex(N * K), tex(sp.binomial(N, 2) * K ** 2)
    v = r.choice(["ratio", "value"])
    p_, q_ = r.choice([1, 2, 3]), nz(r, -4, 4)
    pc = sp.expand((p_ + q_ * x) * (1 + kk * x) ** N).coeff(x, 2)
    approx = 1 + kk * sp.Rational(1, 100)
    est = 1 + c1 / 100 + c2 / 10000 + sp.binomial(N, 3) * kk ** 3 / 10 ** 6
    parts = [P("a", f"Find the first four terms, in ascending powers of $x$, of the expansion of $(1 + kx)^{{{N}}}$, where $k$ is a non-zero constant. Give each coefficient in terms of $k$", 3)]
    rows = [R("a", f"$1 + {c1s}x$", "B1"),
            R("a", f"${c2s}x^2$", "B1"),
            R("a", f"${tex(sp.binomial(N, 3) * K ** 3)}x^3$", "B1")]
    if v == "ratio":
        ratio = c2 / c1
        parts.append(P("b", f"Given that the coefficient of $x^2$ is ${fr(ratio)}$ times the coefficient of $x$, find the value of $k$", 3, prefix="k = "))
        rows += [R("b", f"${c2s} = {fr(ratio)} \\times {c1s}$", "M1"),
                 R("b", "Solves for $k$, dividing by $k \\neq 0$", "M1"), R("b", f"$k = {fr(kk)}$", "A1")]
    else:
        parts.append(P("b", f"Given that the coefficient of $x^2$ is ${fr(c2)}$ and $k {'>' if kk > 0 else '<'} 0$, find the value of $k$", 3, prefix="k = "))
        rows += [R("b", f"${c2s} = {fr(c2)}$", "M1"), R("b", f"$k^2 = {fr(kk ** 2)}$", "M1"), R("b", f"$k = {fr(kk)}$", "A1")]
    parts.append(P("c", f"Using your value of $k$, find the coefficient of $x^2$ in the expansion of $({lin(q_, p_)})(1 + kx)^{{{N}}}$", 3))
    rows += [R("c", f"${p_} \\times {fr(c2)} + ({q_}) \\times {fr(c1)}$", "M1 A1", "M1 two products"),
             R("c", f"${fr(pc)}$", "A1")]
    parts.append(P("d", f"Use your expansion from part (a), with a suitable value of $x$, to find an estimate for ${fmt(float(approx))}^{{{N}}}$, giving your answer to 4 decimal places.", 2))
    rows += [R("d", "Uses $x = 0.01$ in their expansion", "M1"), R("d", f"${dp(est, 4)}$", "A1", f"true value ${dp(float(approx) ** N, 4)}$")]
    return dict(Q(parts=parts, rows=rows, values={"k": kk, "coeff_c": pc, "estimate": est}, diff="7-9", cw="Find",
                  refs=["6A(i)"]), variant=v)


# =============================================================== 6A(ii) rational index

RAT = [sp.Rational(1, 2), sp.Rational(-1, 2), sp.Rational(1, 3), sp.Rational(-1, 3), sp.Integer(-1), sp.Integer(-2), sp.Integer(-3), sp.Rational(3, 2), sp.Rational(-3, 2), sp.Rational(2, 3)]


def _rat_expr(r):
    m = sp.Rational(r.choice(RAT))
    c = r.choice([2, 3, 4, -2, -3, -4, sp.Rational(1, 2), sp.Rational(-1, 3)])
    a0 = r.choice([1, 1, 4, 9, 8]) if m in (sp.Rational(1, 2), sp.Rational(-1, 2)) else r.choice([1, 1, 2])
    if a0 == 8 and m.q != 3:
        a0 = 1
    if a0 in (4, 9) and m.q != 2:
        a0 = 1
    if a0 == 2 and m.q != 1:
        a0 = 1
    return m, c, a0


def _pow_tex(base_tex, m):
    m = sp.Rational(m)
    if m == sp.Rational(1, 2):
        return f"\\sqrt{{{base_tex}}}"
    if m == sp.Rational(1, 3):
        return f"\\sqrt[3]{{{base_tex}}}"
    if m < 0 and m.q == 1:
        return f"\\dfrac{{1}}{{{base_tex}}}" if m == -1 else f"\\dfrac{{1}}{{({base_tex})^{{{-m}}}}}"
    if m == sp.Rational(-1, 2):
        return f"\\dfrac{{1}}{{\\sqrt{{{base_tex}}}}}"
    return f"({base_tex})^{{{fr(m)}}}"


@tpl("binom.rational", "short", 22)
def br_short(r):
    m, c, a0 = _rat_expr(r)
    cx = c if a0 == 1 else c * a0
    e = (a0 + cx * x) ** m
    cs = coeff_series(e, 3)
    valid = sp.Rational(abs(a0), abs(sp.Rational(cx)))
    bt = asc([a0, cx])
    parts = [P("a", f"Expand ${_pow_tex(bt, m)}$ in ascending powers of $x$ up to and including the term in $x^3$, simplifying each coefficient.", 4),
             P("b", "For which values of $x$ is this expansion valid?", 1)]
    rows = [R("a", (f"Takes out ${a0}^{{{fr(m)}}}$: ${tex(sp.Rational(a0) ** m)}({asc([1, sp.Rational(cx, a0)])})^{{{fr(m)}}}$; " if a0 != 1 else "") + f"$1 + ({fr(m)})({asc([0, sp.Rational(cx, a0)])}) + \\dfrac{{({fr(m)})({fr(m - 1)})}}{{2!}}({asc([0, sp.Rational(cx, a0)])})^2 + \\ldots$", "M1", "correct structure for at least two terms"),
            R("a", f"${asc(cs[:2])}$", "A1"),
            R("a", f"${asc([cs[2]], 2)}$", "A1"),
            R("a", f"${asc([cs[3]], 3)}$", "A1"),
            R("b", f"$|x| < {fr(valid)}$", "B1", f"or $-{fr(valid)} < x < {fr(valid)}$")]
    return dict(Q(parts=parts, rows=rows, values={"coeffs": cs, "valid": valid}, diff="7-9" if a0 != 1 else "4-6",
                  cw="Expand", refs=["6A(ii)"]), variant="a0" if a0 != 1 else "basic")


@tpl("binom.rational", "multi-part", 22)
def br_multi(r):
    m = sp.Rational(r.choice([sp.Rational(1, 2), sp.Rational(-1, 2), sp.Rational(1, 3), -1, -2, sp.Rational(-1, 3)]))
    c = r.choice([2, 4, -2, -4, 3, -3, 6, -6])
    e = (1 + c * x) ** m
    cs = coeff_series(e, 3)
    p_, q_ = nz(r, 1, 4), nz(r, -5, 5)
    prod = coeff_series((p_ + q_ * x) * e, 2)
    # approximation: choose x0 small so that 1 + c x0 is nice
    x0 = sp.Rational(r.choice([1, -1]), r.choice([100, 50, 200]))
    val = 1 + c * x0
    est = cs[0] + cs[1] * x0 + cs[2] * x0 ** 2 + cs[3] * x0 ** 3
    true = float(val) ** float(m)
    bt = asc([1, c])
    parts = [P("a", f"Expand ${_pow_tex(bt, m)}$ in ascending powers of $x$ up to and including the term in $x^3$", 4),
             P("b", "Give the interval of $x$ over which your series converges.", 1),
             P("c", f"Hence find the first three terms in the expansion of $({lin(q_, p_)}){_pow_tex(bt, m)}$", 3),
             P("d", f"Use your answer to (a) with $x = {fr(x0)}$ to find an estimate for ${fmt(float(val))}^{{{fr(m)}}}$, giving your answer to 6 decimal places.", 2)]
    rows = [R("a", "Correct binomial structure for at least two terms", "M1"),
            R("a", f"${asc(cs[:2])}$", "A1"), R("a", f"${asc([cs[2]], 2)}$", "A1"), R("a", f"${asc([cs[3]], 3)}$", "A1"),
            R("b", f"$|x| < {fr(sp.Rational(1, abs(c)))}$", "B1"),
            R("c", "Multiplies their expansion by the linear factor, at least two correct products", "M1"),
            R("c", f"${asc(prod[:2])}$", "A1", "ft"), R("c", f"${asc([prod[2]], 2)}$", "A1"),
            R("d", f"Substitutes $x = {fr(x0)}$ into their expansion", "M1"),
            R("d", f"${dp(est, 6)}$", "A1", f"calculator value {dp(true, 6)}")]
    return dict(Q(parts=parts, rows=rows, values={"coeffs": cs, "product": prod, "estimate": est}, diff="7-9", cw="Expand",
                  refs=["6A(ii)"]), variant="approx")


@tpl("binom.rational", "show-that", 22)
def br_show(r):
    v = r.choice(["coef", "approx"])
    m = sp.Rational(r.choice([sp.Rational(1, 2), sp.Rational(-1, 2), -1, -2, sp.Rational(1, 3), sp.Rational(-1, 3), sp.Rational(3, 2)]))
    c = r.choice([2, 3, 4, 6, -2, -3, -4, -6])
    e = (1 + c * x) ** m
    cs = coeff_series(e, 3)
    bt = asc([1, c])
    if v == "coef":
        parts = [P("a", f"Show that the coefficient of $x^2$ in the binomial expansion of ${_pow_tex(bt, m)}$ is ${fr(cs[2])}$", 2),
                 P("b", f"Find the coefficient of $x^3$", 2),
                 P("c", "Write down the condition on $x$ needed for the expansion to be valid.", 1)]
        rows = [R("a", f"$\\dfrac{{({fr(m)})({fr(m - 1)})}}{{2}}({c})^2$", "M1"),
                R("a", f"$= {fr(cs[2])}$", "A1", "cso"),
                R("b", f"$\\dfrac{{({fr(m)})({fr(m - 1)})({fr(m - 2)})}}{{3!}}({c})^3$", "M1"),
                R("b", f"${fr(cs[3])}$", "A1"),
                R("c", f"$-{fr(sp.Rational(1, abs(c)))} < x < {fr(sp.Rational(1, abs(c)))}$", "B1")]
        return dict(Q(parts=parts, rows=rows, values={"c2": cs[2], "c3": cs[3]}, diff="4-6", cw="Show that",
                      refs=["6A(ii)"]), variant=v)
    # approximation of a root: (1 + c x)^m with x = 1/N such that ...
    m = r.choice([sp.Rational(1, 2), sp.Rational(1, 3)])
    c = r.choice([-1, 1])
    Nn = r.choice([10, 20, 25, 50, 100])
    e = (1 + c * x) ** m
    cs = coeff_series(e, 2)
    x0 = sp.Rational(1, Nn)
    inner = 1 + c * x0
    est = cs[0] + cs[1] * x0 + cs[2] * x0 ** 2
    parts = [P("a", f"Find the first three terms, in ascending powers of $x$, of the expansion of ${_pow_tex(asc([1, c]), m)}$", 3),
             P("b", f"By substituting $x = {fr(x0)}$, show that ${_pow_tex(fr(inner), m)} \\approx {fr(est)}$", 2)]
    rows = [R("a", "Correct structure", "M1"), R("a", f"${asc(cs[:2])}$", "A1"), R("a", f"${asc([cs[2]], 2)}$", "A1"),
            R("b", f"$1 {'+' if c > 0 else '-'} {fr(abs(cs[1]) * x0)} - {fr(abs(cs[2]) * x0 ** 2)}$", "M1"),
            R("b", f"$= {fr(est)}$", "A1", "cso")]
    assert sp.simplify(est - (cs[0] + cs[1] * x0 + cs[2] * x0 ** 2)) == 0
    return dict(Q(parts=parts, rows=rows, values={"coeffs": cs, "estimate": est, "true": float(inner) ** float(m)}, diff="7-9",
                  cw="Show that", refs=["6A(ii)"]), variant=v)
