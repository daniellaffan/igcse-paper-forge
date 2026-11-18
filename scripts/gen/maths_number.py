"""Number templates (spec section 1)."""
import math
from fractions import Fraction as F

import sympy as sp

from maths_util import (tpl, P, R, Q, sf, dp, money, num, big, ftex, mixed_tex, name, cur, fig, table,
                        venn_fig, NOT_ACC)


def pf_tex(n):
    fs = sp.factorint(n)
    return " \\times ".join(f"{p}^{{{e}}}" if e > 1 else str(p) for p, e in sorted(fs.items()))


def rand_composite(r, primes=(2, 3, 5, 7, 11), lo=60, hi=2000, k=3):
    while True:
        n = 1
        for p in r.sample(primes, k):
            n *= p ** r.randint(1, 3)
        if lo <= n <= hi:
            return n


# ---------------------------------------------------------------- 1.1 factors
@tpl("number.factors", "short", n=8)
def prime_factors(r):
    n = rand_composite(r, lo=120, hi=3000, k=r.choice([2, 3, 3]))
    return Q(parts=[P("", f"Write ${big(n)}$ as a product of its prime factors.\n\nShow your working clearly.", 2,
                      prefix="")],
             rows=[R("", "eg a complete factor tree or repeated division, at least two correct steps", "M1",
                     "may be seen as a list of prime factors"),
                   R("", f"${pf_tex(n)}$", "A1", "oe, eg in expanded form with × signs; accept index form")],
             values={"n": n, "factorisation": pf_tex(n)}, diff="4-6", cw="Write", refs=["F1.4D", "F1.1H"])


@tpl("number.factors", "short", n=8)
def hcf_lcm_index(r):
    ps = r.sample([2, 3, 5, 7], 3)
    ea = [r.randint(1, 4) for _ in ps]
    eb = [r.randint(0, 3) for _ in ps]
    if eb == ea or sum(eb) == 0:
        return None
    A = math.prod(p ** e for p, e in zip(ps, ea))
    B = math.prod(p ** e for p, e in zip(ps, eb))
    h, l = math.gcd(A, B), A * B // math.gcd(A, B)
    lA, lB = r.sample(["A", "P", "M"], 1)[0], r.choice(["B", "Q", "N"])

    def ix(es):
        return " \\times ".join(f"{p}^{{{e}}}" if e > 1 else str(p) for p, e in sorted(zip(ps, es)) if e > 0)
    hb = [min(x, y) for x, y in zip(ea, eb)]
    lb = [max(x, y) for x, y in zip(ea, eb)]
    intro = f"${lA} = {ix(ea)}$\n\n${lB} = {ix(eb)}$"
    return Q(intro=intro,
             parts=[P("a", f"Write down the HCF of ${lA}$ and ${lB}$, leaving it as a product of prime powers.", 1, prefix=""),
                    P("b", f"Work out the LCM of ${lA}$ and ${lB}$.", 2, prefix="")],
             rows=[R("a", f"${ix(hb)}$", "B1", f"accept {h}"),
                   R("b", f"${ix(lb)}$ or a list of multiples showing a common multiple", "M1",
                     "for a correct product of prime powers with at most one error, or the value of any common multiple"),
                   R("b", f"${big(l)}$", "A1", f"oe, accept ${ix(lb)}$")],
             values={"hcf": h, "lcm": l}, diff=r.choice(["4-6", "4-6", "7-9"]), cw="Find",
             refs=["F1.4E", "F1.4D"])


@tpl("number.factors", "problem", n=8)
def lcm_context(r):
    a, b = r.sample([12, 15, 18, 20, 24, 25, 30, 35, 36, 40, 42, 45], 2)
    l = a * b // math.gcd(a, b)
    if l > 600 or l in (a, b):
        return None
    ctx = r.choice([
        ("Two lighthouses flash their lights at regular intervals. One flashes every {a} seconds and the other flashes every {b} seconds. Both lights flash together at exactly 9 pm.",
         "Work out the next time both lights flash together.", "seconds"),
        ("Bus route A leaves the station every {a} minutes. Bus route B leaves the same station every {b} minutes. A bus from each route leaves the station at 6 am.",
         "Work out the next time that buses from both routes leave the station at the same time.", "minutes"),
        ("Two runners start a lap of a track at the same time and from the same place. One runner takes {a} seconds for each lap and the other takes {b} seconds for each lap. They keep running at these speeds.",
         "After how many seconds will they next be at the starting place at the same time?", "seconds"),
    ])
    intro = ctx[0].format(a=a, b=b)
    unit = ctx[2]
    if "9 pm" in intro:
        mins, secs = divmod(l, 60)
        final = f"{l} seconds after 9 pm, ie at 9:{mins:02d}:{secs:02d} pm"
    elif "6 am" in intro:
        h, m = divmod(l, 60)
        final = f"{6 + h}:{m:02d} am" if 6 + h < 12 else (f"12:{m:02d} pm" if 6 + h == 12 else f"{6 + h - 12}:{m:02d} pm")
    else:
        final = f"{l} seconds"
    return Q(intro=intro, parts=[P("", ctx[1], 3, prefix="")],
             rows=[R("", f"eg multiples of {a}: {a}, {2 * a}, {3 * a}, … and multiples of {b}: {b}, {2 * b}, … or ${pf_tex(a)}$ and ${pf_tex(b)}$", "M1",
                     "for listing at least 3 multiples of each, or prime factors of both numbers"),
                   R("", f"{l} ({unit})", "M1", "for identifying the LCM"),
                   R("", final, "A1", "oe")],
             values={"lcm": l, "answer": final}, diff="4-6", cw="Work out", refs=["F1.4E", "F1.1H"])


@tpl("number.factors", "problem", n=8)
def hcf_context(r):
    g = r.choice([6, 8, 9, 12, 14, 15, 16, 18, 24])
    k = r.sample(range(3, 12), 3)
    if math.gcd(*k) != 1:
        return None
    lens = [g * x for x in k]
    item, unit = r.choice([("ribbons", "cm"), ("planks of wood", "cm"), ("rolls of cable", "m"), ("strips of fabric", "cm")])
    n = name(r)
    total = sum(k)
    return Q(intro=f"{n} has three {item} of lengths {lens[0]} {unit}, {lens[1]} {unit} and {lens[2]} {unit}.\n\n"
                   f"{n} cuts all three {item} into pieces that are all the same length, with nothing left over. Each piece is as long as possible.",
             parts=[P("", f"Work out the total number of pieces {n} gets.\n\nShow your working clearly.", 4, prefix="")],
             rows=[R("", f"eg ${pf_tex(lens[0])}$, ${pf_tex(lens[1])}$, ${pf_tex(lens[2])}$ or lists of factors", "M1",
                     "for prime factors of at least two of the lengths or a list of factors of each"),
                   R("", f"HCF = {g}", "M1", "for identifying the HCF"),
                   R("", f"{lens[0]} ÷ {g} + {lens[1]} ÷ {g} + {lens[2]} ÷ {g} or {k[0]} + {k[1]} + {k[2]}", "M1", "dep on previous M1"),
                   R("", str(total), "A1", "cao")],
             values={"hcf": g, "pieces": total}, diff="4-6", cw="Work out", refs=["F1.4E", "F1.1H"])


# ---------------------------------------------------------------- 1.2/1.3 fractions
def _mixed(r):
    d = r.choice([3, 4, 5, 6, 7, 8, 9])
    w = r.randint(1, 4)
    n = r.randint(1, d - 1)
    if math.gcd(n, d) != 1:
        return None
    return F(w * d + n, d)


@tpl("number.fractions", "short", n=8)
def mixed_calc(r):
    a, b = _mixed(r), _mixed(r)
    if a is None or b is None or a == b:
        return None
    op = r.choice(["+", "-", "\\times", "\\div"])
    if op == "-" and a < b:
        a, b = b, a
    res = {"+": a + b, "-": a - b, "\\times": a * b, "\\div": a / b}[op]
    if res.denominator == 1 or res.denominator > 60:
        return None
    return _fraction_short(a, b, op, res, r)


def _fraction_short(a, b, op, res, r):
    """Short version: work out and give as mixed number."""
    ia, ib = ftex(a), ftex(b)
    if op in "+-":
        lcd = a.denominator * b.denominator // math.gcd(a.denominator, b.denominator)
        mrow = f"$\\frac{{{a.numerator * (lcd // a.denominator)}}}{{{lcd}}} {op} \\frac{{{b.numerator * (lcd // b.denominator)}}}{{{lcd}}}$"
        m1 = "for both as improper fractions with a common denominator (or whole numbers and fractions dealt with separately)"
    elif op == "\\times":
        mrow = f"${ia} \\times {ib}$"
        m1 = "for both written as improper fractions"
    else:
        mrow = f"${ia} \\times \\frac{{{b.denominator}}}{{{b.numerator}}}$"
        m1 = "for improper fractions and multiplying by the reciprocal"
    return Q(parts=[P("", f"Work out $${mixed_tex(a)} {op} {mixed_tex(b)}$$\n\nGive your answer as a mixed number in its simplest form.", 2, prefix="")],
             rows=[R("", mrow, "M1", m1),
                   R("", f"${mixed_tex(res)}$", "A1", "cao")],
             values={"result": res}, diff="4-6" if op in "+-" else r.choice(["4-6", "1-3"]), cw="Work out",
             refs=["F1.2F" if op in "+-" else "F1.2I", "F1.2B"])


@tpl("number.fractions", "short", n=6)
def fraction_of_amount(r):
    d1, d2 = r.sample([3, 4, 5, 6, 8, 10], 2)
    n1 = r.randint(1, d1 - 1)
    n2 = r.randint(1, d2 - 1)
    f1, f2 = F(n1, d1), F(n2, d2)
    if f1.denominator != d1 or f2.denominator != d2:
        return None
    tot = d1 * d2 * r.randint(4, 15)
    first = f1 * tot
    rest = tot - first
    second = f2 * rest
    left = rest - second
    if left.denominator != 1 or second.denominator != 1:
        return None
    thing, verb = r.choice([("people at a concert", "are children"), ("books in a library", "are fiction"),
                            ("seats on a train", "are in first class")])
    n = name(r)
    if r.random() < 0.5:
        return Q(intro=f"There are {tot} {thing}. ${ftex(f1)}$ of them {verb}. ${ftex(f2)}$ of the rest are reserved.",
                 parts=[P("", "Work out how many are neither of these.", 3, prefix="")],
                 rows=[R("", f"${ftex(f1)} \\times {tot} = {first}$ or ${tot} - {first} = {rest}$", "M1", ""),
                       R("", f"${ftex(f2)} \\times {rest} = {second}$", "M1", "for a correct method for the second fraction, or $1 - " + ftex(f1) + " - " + ftex(f2) + "\\times(1-" + ftex(f1) + ")$ oe"),
                       R("", str(left), "A1", "cao")],
                 values={"answer": int(left)}, diff="1-3", cw="Work out", refs=["F1.2D", "F1.2E"])
    return Q(intro=f"{n} has {tot} {cur(r)}. {n} spends ${ftex(f1)}$ of the money on rent and ${ftex(f2)}$ of the remaining money on food.",
             parts=[P("", f"What fraction of the original amount does {n} have left?\n\nGive your answer in its simplest form.", 3, prefix="")],
             rows=[R("", f"${ftex(1 - f1)}$ left after rent, or {first} and {rest}", "M1", ""),
                   R("", f"${ftex(1 - f2)} \\times {ftex(1 - f1)}$ or ${left} \\div {tot}$", "M1", ""),
                   R("", f"${ftex(left / tot)}$", "A1", "cao")],
             values={"fraction": left / tot}, diff="4-6", cw="Work out", refs=["F1.2D", "F1.2E", "F1.2I"])


def recurring(r):
    """returns (latex, fraction, kind) with dot notation"""
    kind = r.choice(["one", "two", "mixed1", "mixed2"])
    if kind == "one":
        a = r.randint(1, 8)
        b = r.randint(0, 9)
        if a == b:
            return None
        # 0.a b-dot  (one non-recurring then one recurring)
        fr = F(a, 10) + F(b, 90)
        texs = f"0.{a}\\dot{{{b}}}"
        x = f"0.{a}{b}{b}{b}\\ldots"
        k = (10, 100)
    elif kind == "two":
        a, b = r.randint(0, 9), r.randint(1, 9)
        if a == b:
            return None
        fr = F(10 * a + b, 99)
        texs = f"0.\\dot{{{a}}}\\dot{{{b}}}"
        x = f"0.{a}{b}{a}{b}\\ldots"
        k = (1, 100)
    elif kind == "mixed1":
        a, b, c = r.randint(1, 9), r.randint(0, 9), r.randint(1, 9)
        if b == c:
            return None
        fr = F(a * 10 + b, 100) + F(c, 900)
        texs = f"0.{a}{b}\\dot{{{c}}}"
        x = f"0.{a}{b}{c}{c}{c}\\ldots"
        k = (100, 1000)
    else:
        a, b, c = r.randint(1, 9), r.randint(0, 9), r.randint(1, 9)
        if b == c:
            return None
        fr = F(a, 10) + F(10 * b + c, 990)
        texs = f"0.{a}\\dot{{{b}}}\\dot{{{c}}}"
        x = f"0.{a}{b}{c}{b}{c}\\ldots"
        k = (10, 1000)
    return texs, fr, x, k


@tpl("number.fractions", "proof", n=8)
def recurring_proof(r):
    rr = recurring(r)
    if rr is None:
        return None
    texs, fr, x, (k1, k2) = rr
    # numeric strings
    def shift(k):
        v = float(fr) * k
        return v
    num_d = fr * (k2 - k1)
    lhs = f"{k2 - k1}x" if k1 != 1 else f"{k2 - 1}x"
    ival = fr * (k2 - k1)
    return Q(parts=[P("", f"Prove algebraically that the recurring decimal ${texs}$ can be written as $${ftex(fr)}$$", 2, space="working")],
             rows=[R("", f"eg $x = {x}$ and ${k2 if k1 == 1 else k2}x = {sf(float(fr) * k2, 9)}\\ldots$" +
                     ("" if k1 == 1 else f" and ${k1}x = {sf(float(fr) * k1, 9)}\\ldots$"), "M1",
                     "for two recurring decimals that, when subtracted, leave a whole number or terminating decimal, eg "
                     f"${k2}x - {k1}x = {num(float(ival))}$" if k1 != 1 else
                     f"for two recurring decimals that, when subtracted, leave a whole number, eg ${k2}x - x = {num(float(ival))}$"),
                   R("", f"${k2 - k1}x = {num(float(ival))}$ so $x = {ftex(fr)}$", "A1",
                     "for completing the proof to the given fraction; must show the subtraction and the resulting fraction before simplifying")],
             values={"fraction": fr, "decimal": texs}, diff="7-9", cw="Prove", refs=["H1.3A"])


@tpl("number.fractions", "proof", n=7)
def fraction_show(r):
    a, b = _mixed(r), _mixed(r)
    if a is None or b is None or a == b:
        return None
    op = r.choice(["+", "-", "\\times", "\\div"])
    if op == "-" and a < b:
        a, b = b, a
    res = {"+": a + b, "-": a - b, "\\times": a * b, "\\div": a / b}[op]
    if res.denominator == 1 or res.denominator > 40:
        return None
    ia, ib = ftex(a), ftex(b)
    if op in "+-":
        lcd = a.denominator * b.denominator // math.gcd(a.denominator, b.denominator)
        m = f"$\\frac{{{a.numerator * (lcd // a.denominator)}}}{{{lcd}}} {op} \\frac{{{b.numerator * (lcd // b.denominator)}}}{{{lcd}}}$"
        m1 = "for both as improper fractions with a common denominator, or whole numbers and fractions treated separately with a common denominator"
        raw = (a + b) if op == "+" else (a - b)
        m2 = f"$\\frac{{{raw.numerator * (lcd // raw.denominator)}}}{{{lcd}}}$ oe"
    elif op == "\\times":
        m = f"${ia} \\times {ib}$"
        m1 = "for both written as correct improper fractions"
        m2 = f"$\\frac{{{a.numerator * b.numerator}}}{{{a.denominator * b.denominator}}}$ oe"
    else:
        m = f"${ia} \\times \\frac{{{b.denominator}}}{{{b.numerator}}}$"
        m1 = "for improper fractions and multiplying by the reciprocal of the second"
        m2 = f"$\\frac{{{a.numerator * b.denominator}}}{{{a.denominator * b.numerator}}}$ oe"
    return Q(parts=[P("", f"Show that $${mixed_tex(a)} {op} {mixed_tex(b)} = {mixed_tex(res)}$$", 3, space="working")],
             rows=[R("", m, "M1", m1),
                   R("", m2, "M1", "for a correct unsimplified result"),
                   R("", f"shown to equal ${mixed_tex(res)}$", "A1", "dep on M2; all working must be shown, a calculator answer alone scores 0")],
             values={"result": res}, diff="4-6", cw="Show that", refs=["F1.2F" if op in "+-" else "F1.2I", "F1.2B"])


# ---------------------------------------------------------------- 1.4 powers & surds
@tpl("number.powers", "short", n=8)
def eval_powers(r):
    base, root = r.choice([(8, 3), (27, 3), (64, 3), (125, 3), (16, 2), (25, 2), (36, 2), (49, 2), (81, 2), (16, 4), (81, 4), (32, 5)])
    b = round(base ** (1 / root))
    p = r.choice([1, 2, 3]) if root <= 3 else r.choice([1, 3])
    neg = r.random() < 0.6
    fr = r.random() < 0.4
    if fr:
        num_, den = r.choice([(1, 8), (4, 9), (9, 16), (27, 64), (1, 27), (16, 81), (8, 125)])
        rt = 2 if math.isqrt(num_) ** 2 == num_ and math.isqrt(den) ** 2 == den else 3
        rn, rd = round(num_ ** (1 / rt)), round(den ** (1 / rt))
        if rn ** rt != num_ or rd ** rt != den:
            return None
        val = F(rn, rd) ** p
        if neg:
            val = 1 / val
        e = f"-\\frac{{{p}}}{{{rt}}}" if neg else f"\\frac{{{p}}}{{{rt}}}"
        expr = f"\\left(\\frac{{{num_}}}{{{den}}}\\right)^{{{e}}}"
    else:
        val = F(b) ** p
        if neg:
            val = 1 / val
        e = f"-\\frac{{{p}}}{{{root}}}" if neg else f"\\frac{{{p}}}{{{root}}}"
        if p == 1 and not neg:
            return None
        expr = f"{base}^{{{e}}}"
    return Q(parts=[P("", f"Find the value of $${expr}$$\n\nGive your answer as an exact value.", 2, prefix="")],
             rows=[R("", "eg evidence of the root taken first, or the power applied first, or the reciprocal", "M1",
                     "for one correct stage, eg the root found, or $\\frac{1}{\\ldots}$ for the negative index"),
                   R("", f"${ftex(val)}$", "A1", "oe")],
             values={"value": val}, diff="7-9" if neg else "4-6", cw="Find", refs=["H1.4C"])


@tpl("number.powers", "short", n=7)
def find_n_index(r):
    b = r.choice([2, 3, 5])
    a, c = r.randint(2, 6), r.randint(2, 6)
    d = r.randint(1, 4)
    n = a + c - d
    form = r.choice(["mul", "root"])
    if form == "mul":
        txt = f"${b}^{{{a}}} \\times {b}^{{{c}}} \\div {b}^{{{d}}} = {b}^n$\n\nFind the value of $n$."
        ans = n
        m = f"${b}^{{{a + c}}} \\div {b}^{{{d}}}$ or ${a} + {c} - {d}$"
    else:
        k = r.choice([2, 4])
        p = r.choice([3, 5, 7, 9])
        # sqrt(b^p)= b^(p/2); base^? form
        ans = F(p, 2)
        txt = f"$\\sqrt{{{b}^{{{p}}}}} = {b}^n$\n\nFind the value of $n$."
        m = f"$({b}^{{{p}}})^{{\\frac{{1}}{{2}}}}$"
    return Q(parts=[P("", txt, 2, prefix="$n =$ ")],
             rows=[R("", m, "M1", ""), R("", f"${ftex(ans)}$", "A1", "oe")],
             values={"n": ans}, diff="4-6", cw="Find", refs=["F1.4C", "H1.4C"])


def cs(k, s):
    """signed coefficient times root s, eg '- 3\\sqrt{2}', '+ \\sqrt{5}'"""
    return f"{'+' if k >= 0 else '-'} {'' if abs(k) == 1 else abs(k)}\\sqrt{{{s}}}"


def surd_simplify(n):
    """n -> (a, b) with sqrt(n) = a sqrt(b)"""
    a = 1
    for k in range(int(math.isqrt(n)), 1, -1):
        if n % (k * k) == 0:
            a = k
            break
    return a, n // (a * a)


@tpl("number.powers", "algebra", n=8)
def surd_expand(r):
    s = r.choice([2, 3, 5, 7])
    a, b, c, d = r.randint(1, 6), r.choice([-3, -2, -1, 1, 2, 3]), r.randint(1, 6), r.choice([-3, -2, -1, 1, 2, 3])
    x = sp.sqrt(s)
    e = sp.expand((a + b * x) * (c + d * x))
    const = a * c + b * d * s
    coef = a * d + b * c
    if coef == 0:
        return None

    def t(k, l):
        return f"{k} {'+' if l > 0 else '-'} {'' if abs(l) == 1 else abs(l)}\\sqrt{{{s}}}"
    return Q(parts=[P("", f"Expand and simplify $$({t(a, b)})({t(c, d)})$$\n\nGive your answer in the form $p + q\\sqrt{{{s}}}$ where $p$ and $q$ are integers.", 3, prefix="")],
             rows=[R("", f"${a * c} {cs(a * d, s)} {cs(b * c, s)} {cs(b * d, s)}\\sqrt{{{s}}}$", "M1",
                     "for at least 3 of the 4 terms correct"),
                   R("", f"${a * c} {'+' if b * d * s >= 0 else '-'} {abs(b * d * s)}$ or $\\sqrt{{{s}}} \\times \\sqrt{{{s}}} = {s}$", "M1", ""),
                   R("", f"${const} {'+' if coef > 0 else '-'} {abs(coef)}\\sqrt{{{s}}}$", "A1", "cao")],
             values={"p": const, "q": coef}, diff="7-9", cw="Expand and simplify", refs=["H1.4B"])


@tpl("number.powers", "algebra", n=8)
def rationalise(r):
    kind = r.choice(["simple", "conj"])
    if kind == "simple":
        s = r.choice([2, 3, 5, 6, 7, 10])
        k = r.choice([2, 3, 4, 5, 6]) * r.choice([1, s])
        a = r.randint(1, 4)
        e = sp.nsimplify(k) / (a * sp.sqrt(s))
        e = sp.radsimp(e)
        txt = f"$$\\frac{{{k}}}{{{'' if a == 1 else a}\\sqrt{{{s}}}}}$$"
        res = sp.latex(sp.simplify(e))
        rows = [R("", f"$\\frac{{{k}}}{{{'' if a == 1 else a}\\sqrt{{{s}}}}} \\times \\frac{{\\sqrt{{{s}}}}}{{\\sqrt{{{s}}}}}$", "M1", ""),
                R("", f"${res}$", "A1", "cao, fully simplified")]
        marks_d = "4-6"
        form = "Give your answer in its simplest form."
    else:
        s = r.choice([2, 3, 5, 7])
        a, b = r.randint(2, 6), r.choice([-1, 1])
        if a * a == s:
            return None
        k = r.randint(1, 9)
        e = sp.radsimp(k / (a + b * sp.sqrt(s)))
        den = a * a - s
        if abs(den) == 1:
            return None
        txt = f"$$\\frac{{{k}}}{{{a} {'+' if b > 0 else '-'} \\sqrt{{{s}}}}}$$"
        res = sp.latex(sp.simplify(e))
        rows = [R("", f"$\\times \\frac{{{a} {'-' if b > 0 else '+'} \\sqrt{{{s}}}}}{{{a} {'-' if b > 0 else '+'} \\sqrt{{{s}}}}}$", "M1", ""),
                R("", f"denominator ${a * a} - {s} = {den}$", "M1", "for the rationalised denominator"),
                R("", f"${res}$", "A1", "oe, eg separate fractions")]
        marks_d = "7-9"
        form = "Give your answer in the form $\\frac{a + b\\sqrt{c}}{d}$ where $a$, $b$, $c$ and $d$ are integers."
    return Q(parts=[P("", f"Rationalise the denominator and simplify {txt}\n\n{form}", sum(int(x.strip('MA')) for x in [rw['marks'] for rw in rows]), prefix="")],
             rows=rows, values={"value": str(e)}, diff=marks_d, cw="Rationalise", refs=["H1.4B", "H1.4A"])


@tpl("number.powers", "proof", n=13)
def surd_show(r):
    kind = r.choice(["sum", "frac"])
    if kind == "sum":
        s = r.choice([2, 3, 5, 6, 7])
        ks = r.sample([2, 3, 4, 5], 2)
        sgn = r.choice([1, -1])
        n1, n2 = ks[0] ** 2 * s, ks[1] ** 2 * s
        tot = ks[0] + sgn * ks[1]
        if tot <= 0:
            return None
        txt = f"Show that $\\sqrt{{{n1}}} {'+' if sgn > 0 else '-'} \\sqrt{{{n2}}}$ can be written as ${'' if tot == 1 else tot}\\sqrt{{{s}}}$"
        rows = [R("", f"$\\sqrt{{{n1}}} = {ks[0]}\\sqrt{{{s}}}$ or $\\sqrt{{{n2}}} = {ks[1]}\\sqrt{{{s}}}$", "M1", "for one surd correctly simplified"),
                R("", f"${ks[0]}\\sqrt{{{s}}} {'+' if sgn > 0 else '-'} {ks[1]}\\sqrt{{{s}}} = {tot}\\sqrt{{{s}}}$", "A1", "dep on M1; full working shown")]
        val = f"{tot}sqrt({s})"
    else:
        s = r.choice([2, 3, 5])
        a = r.randint(2, 5)
        if a * a == s:
            return None
        # (a+sqrt s)^2 = a^2 + s + 2a sqrt s
        p, q = a * a + s, 2 * a
        txt = f"Show that $({a} + \\sqrt{{{s}}})^2 = {p} + {q}\\sqrt{{{s}}}$"
        rows = [R("", f"${a * a} + {a}\\sqrt{{{s}}} + {a}\\sqrt{{{s}}} + {s}$", "M1", "for 4 correct terms, or 3 correct terms with $\\sqrt{" + str(s) + "}\\times\\sqrt{" + str(s) + "} = " + str(s) + "$"),
                R("", f"${p} + {q}\\sqrt{{{s}}}$", "A1", "dep on M1, with working shown")]
        val = f"{p}+{q}sqrt({s})"
    return Q(parts=[P("", txt + "\n\nShow each stage of your working clearly.", 2, space="working")],
             rows=rows, values={"result": val}, diff="7-9", cw="Show that", refs=["H1.4A", "H1.4B"])


# ---------------------------------------------------------------- 1.5 sets
def _ints(lo, hi):
    return list(range(lo, hi + 1))


SET_RULES = [
    ("even numbers", lambda x: x % 2 == 0), ("odd numbers", lambda x: x % 2 == 1),
    ("prime numbers", lambda x: sp.isprime(x)), ("multiples of 3", lambda x: x % 3 == 0),
    ("multiples of 4", lambda x: x % 4 == 0), ("square numbers", lambda x: math.isqrt(x) ** 2 == x),
    ("factors of 24", lambda x: 24 % x == 0), ("factors of 36", lambda x: 36 % x == 0),
    ("multiples of 5", lambda x: x % 5 == 0), ("factors of 30", lambda x: 30 % x == 0),
]


def setstr(s):
    return "\\{" + ", ".join(str(x) for x in sorted(s)) + "\\}" if s else "\\varnothing"


@tpl("number.sets", "short", n=14)
def set_list(r):
    hi = r.choice([12, 15, 16, 18, 20])
    E = _ints(1, hi)
    (na, fa), (nb, fb) = r.sample(SET_RULES, 2)
    A = {x for x in E if fa(x)}
    B = {x for x in E if fb(x)}
    if not A or not B or A == B:
        return None
    ops = r.sample(["cap", "cup", "Acomp_cap", "Bcomp"], 2)

    def ev(o):
        return {"cap": (A & B, "A \\cap B"), "cup": (A | B, "A \\cup B"), "Acomp_cap": ((set(E) - A) & B, "A' \\cap B"),
                "Bcomp": (set(E) - B, "B'")}[o]
    (s1, t1), (s2, t2) = ev(ops[0]), ev(ops[1])
    intro = (f"$\\mathscr{{E}} = \\{{\\text{{whole numbers from 1 to {hi}}}\\}}$\n\n$A = \\{{\\text{{{na}}}\\}}$\n\n"
             f"$B = \\{{\\text{{{nb}}}\\}}$")
    return Q(intro=intro,
             parts=[P("a", f"List the members of the set $${t1}$$", 1, space="lines", lines=1),
                    P("b", f"List the members of the set $${t2}$$", 1, space="lines", lines=1),
                    P("c", "Find $n(A)$.", 1, space="lines", lines=1)],
             rows=[R("a", f"${setstr(s1)}$", "B1", "any order; no extras"),
                   R("b", f"${setstr(s2)}$", "B1", "any order; no extras"),
                   R("c", str(len(A)), "B1", "cao")],
             values={"s1": sorted(s1), "s2": sorted(s2), "nA": len(A)}, diff=r.choice(["1-3", "4-6"]), cw="List",
             refs=["F1.5B", "F1.5D", "H1.5C"])


@tpl("number.sets", "problem", n=7)
def venn_unknown(r):
    total = r.randint(40, 120)
    x = r.randint(3, 15)
    a_only = r.randint(5, 25)
    b_only = r.randint(5, 25)
    neither = total - a_only - b_only - x
    if neither < 2:
        return None
    nA, nB = a_only + x, b_only + x
    ctxs = [("students", "study History", "study Geography"), ("guests at a hotel", "use the pool", "use the gym"),
            ("members of a club", "play tennis", "play golf"), ("people in a survey", "own a cat", "own a dog")]
    who, p, q = r.choice(ctxs)
    return Q(intro=f"There are {total} {who}.\n\n{nA} of them {p}.\n{nB} of them {q}.\n{neither} of them do neither.",
             parts=[P("", f"One of these {who} is chosen at random.\n\nWork out the probability that this person does both.", 4, prefix="")],
             rows=[R("", f"${nA} + {nB} + {neither} - {total} = {x}$ or a Venn diagram with $x$ in the intersection, ${nA} - x$ and ${nB} - x$", "M1",
                     "for a correct start, eg a correct equation in $x$"),
                   R("", f"$({nA} - x) + x + ({nB} - x) + {neither} = {total}$", "M1", "for a complete equation or a fully correct Venn diagram"),
                   R("", f"$x = {x}$", "A1", ""),
                   R("", f"$\\frac{{{x}}}{{{total}}}$", "A1", f"oe, eg ${ftex(F(x, total))}$ or {sf(x / total, 3)}")],
             values={"both": x, "prob": F(x, total)}, diff="4-6", cw="Work out", refs=["H1.5B", "H1.5D", "F6.3D"])


@tpl("number.sets", "problem", n=7)
def venn_algebra(r):
    x = r.randint(2, 9)
    a, b, c = r.randint(1, 4), r.randint(1, 4), r.randint(1, 6)
    ka, kb = r.randint(0, 6), r.randint(0, 6)
    # regions: A only = a x + ka? keep: A only = 2x, both = x, B only = x + kb, neither = c
    A_only, both, B_only = a * x + ka, x, b * x - (kb if b * x > kb + 1 else 0)
    if B_only <= 0:
        return None
    kb_eff = b * x - B_only
    neither = c
    total = A_only + both + B_only + neither
    labels = [f"{'' if a == 1 else a}x" + (f" + {ka}" if ka else ""), "x", f"{'' if b == 1 else b}x" + (f" - {kb_eff}" if kb_eff else "")]
    svgs = venn_fig(["A", "B"], labels, outside=str(neither))
    return Q(intro=f"The Venn diagram shows the number of elements in each region of sets $A$ and $B$.\n\n$n(\\mathscr{{E}}) = {total}$",
             figs=[fig(svgs, 80, note=None)],
             parts=[P("a", "Find the value of $x$.", 3, prefix="$x =$ "),
                    P("b", "Find $n(A' \\cup B)$.", 1, prefix="")],
             rows=[R("a", f"$({labels[0]}) + x + ({labels[2]}) + {neither} = {total}$", "M1", "for a correct equation"),
                   R("a", f"${a + 1 + b}x = {total - neither - ka + kb_eff}$", "M1", "for correctly collecting terms"),
                   R("a", str(x), "A1", "cao"),
                   R("b", str(both + B_only + neither), "B1", "ft their $x$")],
             values={"x": x, "n": both + B_only + neither}, diff="7-9", cw="Find", refs=["H1.5B", "H1.5C", "H1.5D"])


@tpl("number.sets", "structured", n=14)
def venn_three(r):
    vals = [r.randint(1, 12) for _ in range(7)]
    outside = r.randint(0, 10)
    A, B, Cc, AB, AC, BC, ABC = vals
    labs = r.choice([("F", "G", "H"), ("P", "Q", "R"), ("A", "B", "C")])
    ctx = r.choice(["students and the sports they play", "people and the fruits they bought", "members of a club and the activities they did"])
    s = venn_fig(list(labs), [str(v) for v in vals], outside=str(outside), three=True)
    tot = sum(vals) + outside
    nA = A + AB + AC + ABC
    in_ab_not_c = AB
    p1 = labs[0]
    p2 = labs[1]
    p3 = labs[2]
    q_union = A + B + AB + AC + BC + ABC
    notC = A + B + AB + outside
    bc_given = F(BC + ABC, B + BC + AB + ABC)
    return Q(intro=f"The Venn diagram shows information about {ctx}. The numbers are the numbers of elements in each region.",
             figs=[fig(s, 90, note=None)],
             parts=[P("a", f"Find $n({p1})$.", 1, prefix=""),
                    P("b", f"Find $n({p1} \\cap {p2} \\cap {p3}')$.", 1, prefix=""),
                    P("c", f"Find $n({p3}')$.", 1, prefix=""),
                    P("d", f"Find $n(({p1} \\cup {p2}) \\cap {p3})$.", 1, prefix=""),
                    P("e", f"An element is chosen at random from ${p2}$.\n\nFind the probability that it is also in ${p3}$.", 2, prefix="")],
             rows=[R("a", str(nA), "B1", "cao"), R("b", str(AB), "B1", "cao"), R("c", str(notC), "B1", "cao"),
                   R("d", str(AC + BC + ABC), "B1", "cao"),
                   R("e", f"denominator {B + AB + BC + ABC} or numerator {BC + ABC}", "M1", "for a correct numerator or denominator in a fraction"),
                   R("e", f"$\\frac{{{BC + ABC}}}{{{B + AB + BC + ABC}}}$", "A1", "oe")],
             values={"nA": nA, "AB_notC": AB, "notC": notC, "union_cap_C": AC + BC + ABC, "prob": bc_given},
             diff=r.choice(["4-6", "4-6", "7-9"]), cw="Find", refs=["H1.5B", "H1.5C", "F1.5D", "F6.3D"])


# ---------------------------------------------------------------- 1.6 percentages
@tpl("number.percentages", "short", n=8)
def percent_change(r):
    old = r.randint(30, 900) * r.choice([1, 10])
    pct = r.choice([4, 6, 8, 12, 15, 18, 22, 25, 35, 40])
    up = r.random() < 0.5
    new = old * (100 + pct) // 100 if up else old * (100 - pct) // 100
    if new * 100 != old * (100 + (pct if up else -pct)):
        return None
    item, unit = r.choice([("The price of a bicycle", cur(r)), ("The population of a village", "people"),
                           ("The mass of a parcel", "grams"), ("The rent for a flat", cur(r) + " per month")])
    return Q(parts=[P("", f"{item} changed from {big(old)} {unit} to {big(new)} {unit}.\n\nWork out the percentage {'increase' if up else 'decrease'}.", 3, prefix="", )],
             rows=[R("", f"${big(abs(new - old))}$ or $\\frac{{{new}}}{{{old}}} = {num(new / old)}$", "M1", ""),
                   R("", f"$\\frac{{{abs(new - old)}}}{{{old}}} \\times 100$ or ${num(new / old)} \\times 100 - 100$", "M1", "for a complete method"),
                   R("", str(pct), "A1", "cao")],
             values={"percent": pct}, diff="4-6", cw="Work out", refs=["F1.6E"])


@tpl("number.percentages", "short", n=8)
def compound_short(r):
    P0 = r.randint(20, 90) * 100
    rate = r.choice([1.5, 2, 2.5, 3, 3.2, 3.5, 4, 4.5, 5, 6])
    yrs = r.randint(2, 6)
    dep = r.random() < 0.4
    m = 1 + rate / 100 * (-1 if dep else 1)
    val = P0 * m ** yrs
    if dep:
        txt = f"A machine was bought for {big(P0)} {cur(r)}. Its value depreciates by {num(rate)}% each year.\n\nWork out the value of the machine at the end of {yrs} years.\n\nGive your answer correct to the nearest whole number."
        refs = ["F1.6G"]
    else:
        txt = f"{name(r)} invests {big(P0)} {cur(r)} for {yrs} years at {num(rate)}% per year compound interest.\n\nCalculate how much the investment is worth after {yrs} years.\n\nGive your answer correct to 2 decimal places."
        refs = ["F1.6G", "H1.6B"]
    ans = f"{round(val)}" if dep else money(val)
    return Q(parts=[P("", txt, 3, prefix="")],
             rows=[R("", f"${num(m)}$ seen or ${big(P0)} \\times {num(m)}$ (= {money(P0 * m)})", "M1", "for the multiplier or the first year's value"),
                   R("", f"${big(P0)} \\times {num(m)}^{{{yrs}}}$", "M1", "for a complete method; year-by-year calculation acceptable"),
                   R("", ans, "A1", "awrt " + (str(round(val)) if dep else money(val)))],
             values={"value": round(val, 2)}, diff="4-6", cw="Work out", refs=refs)


@tpl("number.percentages", "problem", n=8)
def reverse_percent(r):
    pct = r.choice([5, 8, 12, 15, 20, 24, 30, 35, 40, 12.5, 17.5])
    up = r.random() < 0.5
    orig = r.randint(12, 400) * (2 if pct in (12.5, 17.5) else 1)
    new = orig * (1 + pct / 100) if up else orig * (1 - pct / 100)
    if abs(new * 100 - round(new * 100)) > 1e-6:
        return None
    m = (100 + pct) / 100 if up else (100 - pct) / 100
    c = cur(r)
    ctx = r.choice([
        (f"In a sale, all prices are reduced by {num(pct)}%. The sale price of a jacket is {money(new)} {c}.", "Work out the price of the jacket before the sale.", False),
        (f"The number of visitors to a museum in 2025 was {num(pct)}% more than in 2024. There were {big(round(new * 100))} visitors in 2025.", "Work out the number of visitors in 2024.", True),
        (f"After a pay rise of {num(pct)}%, {name(r)} earns {money(new)} {c} per week.", "Work out the weekly pay before the pay rise.", True),
        (f"A car is worth {money(new)} {c}. This is {num(pct)}% less than its value one year ago.", "Work out the value of the car one year ago.", False),
    ])
    if ctx[2] != up:
        return None
    if "visitors" in ctx[0]:
        newv, origv = round(new * 100), round(orig * 100)
    else:
        newv, origv = new, orig
    ans = big(origv) if "visitors" in ctx[0] else money(origv)
    return Q(intro=ctx[0], parts=[P("", ctx[1], 3, prefix="")],
             rows=[R("", f"${num(m)}$ or ${num(100 + (pct if up else -pct))}\\% = {money(newv) if 'visitors' not in ctx[0] else big(newv)}$", "M1",
                     "for the correct multiplier or the correct percentage linked to the value"),
                   R("", f"${money(newv) if 'visitors' not in ctx[0] else newv} \\div {num(m)}$", "M1", "for a complete method"),
                   R("", ans, "A1", "cao")],
             values={"original": origv}, diff="4-6", cw="Work out", refs=["F1.6F"])


@tpl("number.percentages", "problem", n=8)
def compound_years(r):
    P0 = r.randint(10, 60) * 500
    rate = r.choice([2, 2.5, 3, 3.5, 4, 4.5, 5, 6, 8])
    target_mult = r.choice([1.2, 1.25, 1.3, 1.4, 1.5])
    m = 1 + rate / 100
    n = math.ceil(math.log(target_mult) / math.log(m))
    target = P0 * target_mult
    c = cur(r)
    nm = name(r)
    v_n1 = P0 * m ** (n - 1)
    v_n = P0 * m ** n
    return Q(intro=f"{nm} invests {big(P0)} {c} in a savings account paying {num(rate)}% per year compound interest.",
             parts=[P("", f"Work out the least number of whole years it takes for the value of the investment to be more than {big(round(target))} {c}.", 3, prefix="")],
             rows=[R("", f"${big(P0)} \\times {num(m)}^n$ for at least one value of $n$, or year-by-year values", "M1", ""),
                   R("", f"${big(P0)} \\times {num(m)}^{{{n - 1}}} = {money(v_n1)}$ and ${big(P0)} \\times {num(m)}^{{{n}}} = {money(v_n)}$", "M1",
                     "for values for both $n - 1$ and $n$ years, either side of the target"),
                   R("", str(n), "A1", "cao")],
             values={"years": n}, diff="7-9", cw="Work out", refs=["H1.6B", "F1.6G"])


@tpl("number.percentages", "structured", n=8)
def repeated_change(r):
    p1, p2 = r.choice([10, 20, 25, 30, 40]), r.choice([10, 15, 20, 25, 30])
    up1 = r.random() < 0.5
    m1 = 1 + p1 / 100 if up1 else 1 - p1 / 100
    m2 = 1 - p2 / 100 if up1 else 1 + p2 / 100
    overall = m1 * m2
    pct = abs(overall - 1) * 100
    word = "increase" if overall > 1 else "decrease"
    price = r.randint(20, 300) * 10
    c = cur(r)
    final = price * overall
    tax = r.choice([5, 10, 15, 20])
    return Q(intro=f"A shop changes the price of a television. In January the price is {'increased' if up1 else 'decreased'} by {p1}%. In February the new price is {'decreased' if up1 else 'increased'} by {p2}%.",
             parts=[P("a", f"Work out the overall percentage change in the price. State whether it is an increase or a decrease.", 3, prefix=""),
                    P("b", f"The original price of the television was {big(price)} {c}.\n\nWork out the price at the end of February.", 1, prefix=""),
                    P("c", f"A customer pays the price at the end of February plus {tax}% tax.\n\nWork out how much tax the customer pays.", 2, prefix="")],
             rows=[R("a", f"${num(m1)} \\times {num(m2)}$", "M1", "or use of an example price, eg $100 \\to " + num(100 * m1) + "$"),
                   R("a", f"${num(round(overall, 6))}$", "M1", ""),
                   R("a", f"{num(round(pct, 6))}% {word}", "A1", "must state increase or decrease"),
                   R("b", money(final), "B1", "ft their multiplier"),
                   R("c", f"${money(final)} \\times {num(tax / 100)}$", "M1", ""),
                   R("c", money(final * tax / 100), "A1", "ft their (b)")],
             values={"percent": round(pct, 6), "final": round(final, 2), "tax": round(final * tax / 100, 2)},
             diff="4-6", cw="Work out", refs=["H1.6A", "F1.6E", "F1.6D"])


@tpl("number.percentages", "structured", n=8)
def depreciation_structured(r):
    P0 = r.randint(8, 40) * 1000
    rate = r.choice([8, 10, 12, 15, 18, 20])
    m = 1 - rate / 100
    y = r.randint(3, 5)
    v = P0 * m ** y
    c = cur(r)
    p2 = r.choice([2, 3, 4])
    v2 = P0 * m ** p2
    lost = (1 - m ** y) * 100
    return Q(intro=f"A van was bought for {big(P0)} {c}. Its value depreciates by {rate}% per year.",
             parts=[P("a", f"Work out the value of the van after {p2} years.", 2, prefix=""),
                    P("b", f"Work out the value of the van after {y} years as a percentage of its original value.", 2, prefix=""),
                    P("c", f"After {y} years the van is sold. The money received is {money(v)} {c}.\n\nWhat percentage of the original value has been lost?", 2, prefix="")],
             rows=[R("a", f"${big(P0)} \\times {num(m)}^{{{p2}}}$", "M1", ""),
                   R("a", money(v2), "A1", "awrt " + money(v2)),
                   R("b", f"${num(m)}^{{{y}}} \\times 100$", "M1", ""),
                   R("b", sf(m ** y * 100, 3), "A1", "awrt " + sf(m ** y * 100, 3)),
                   R("c", f"$100 - {sf(m ** y * 100, 3)}$ or $\\frac{{{big(P0)} - {money(v)}}}{{{big(P0)}}} \\times 100$", "M1", ""),
                   R("c", sf(lost, 3), "A1", "awrt " + sf(lost, 3))],
             values={"a": round(v2, 2), "b": round(m ** y * 100, 4), "c": round(lost, 4)}, diff="4-6", cw="Work out",
             refs=["F1.6G", "F1.6B"])


# ---------------------------------------------------------------- 1.7 ratio
@tpl("number.ratio", "short", n=7)
def share_ratio(r):
    parts = r.sample(range(1, 10), r.choice([2, 3]))
    if math.gcd(*parts) != 1:
        return None
    k = r.randint(5, 60)
    tot = sum(parts) * k
    ns = name(r, len(parts))
    c = cur(r)
    shares = [p * k for p in parts]
    rs = " : ".join(str(p) for p in parts)
    who = ", ".join(ns[:-1]) + " and " + ns[-1]
    return Q(parts=[P("", f"{who} share {big(tot)} {c} in the ratio {rs}.\n\nWork out how much {ns[-1]} gets.", 2, prefix="")],
             rows=[R("", f"${big(tot)} \\div {sum(parts)}$ (= {k})", "M1", ""), R("", str(shares[-1]), "A1", "cao")],
             values={"share": shares[-1]}, diff="1-3", cw="Work out", refs=["F1.7B"])


@tpl("number.ratio", "short", n=7)
def ratio_1n(r):
    a = r.choice([2, 4, 5, 8, 10, 16, 20, 25])
    b = r.randint(3, 90)
    u1, u2, f_ = r.choice([("cm", "m", 100), ("g", "kg", 1000), ("mm", "cm", 10), ("ml", "litres", 1000)])
    n = F(b * f_, a)
    if n.denominator not in (1, 2, 4, 5, 10, 8):
        return None
    return Q(parts=[P("", f"Write the ratio {a} {u1} : {b} {u2} in the form $1 : n$", 2, prefix="")],
             rows=[R("", f"{a} : {b * f_} oe (same units)", "M1", ""), R("", f"1 : {num(float(n))}", "A1", "oe")],
             values={"n": float(n)}, diff="4-6", cw="Write", refs=["F1.7A", "F1.10B"])


@tpl("number.ratio", "problem", n=7)
def ratio_difference(r):
    a, b, c = r.sample(range(1, 12), 3)
    if len({a, b, c}) < 3 or math.gcd(math.gcd(a, b), c) != 1:
        return None
    k = r.randint(2, 15)
    d = abs(b - a) * k
    if d == 0:
        return None
    ns = name(r, 3)
    thing = r.choice(["stickers", "marbles", "stamps", "cards"])
    return Q(intro=f"{ns[0]}, {ns[1]} and {ns[2]} share some {thing} in the ratio {a} : {b} : {c}.\n\n{ns[1] if b > a else ns[0]} gets {d} more {thing} than {ns[0] if b > a else ns[1]}.",
             parts=[P("", f"Work out the total number of {thing}.", 3, prefix="")],
             rows=[R("", f"${d} \\div {abs(b - a)}$ (= {k})", "M1", "for finding the value of one share"),
                   R("", f"${k} \\times {a + b + c}$", "M1", ""), R("", str(k * (a + b + c)), "A1", "cao")],
             values={"total": k * (a + b + c)}, diff="4-6", cw="Work out", refs=["F1.7B", "F1.7E"])


@tpl("number.ratio", "problem", n=7)
def ratio_combine(r):
    a, b = r.sample(range(1, 8), 2)
    c, d = r.sample(range(1, 8), 2)
    if math.gcd(a, b) != 1 or math.gcd(c, d) != 1:
        return None
    # x:y = a:b, y:z = c:d
    l = b * c // math.gcd(b, c)
    x, y, z = a * l // b, l, d * l // c
    g = math.gcd(math.gcd(x, y), z)
    x, y, z = x // g, y // g, z // g
    tot = (x + y + z) * r.randint(2, 9)
    k = tot // (x + y + z)
    animal = r.choice([("red", "blue", "green", "counters in a bag"), ("cars", "vans", "lorries", "vehicles in a car park"),
                       ("roses", "tulips", "lilies", "flowers in a garden")])
    return Q(intro=f"The {animal[3]} are {animal[0]}, {animal[1]} or {animal[2]}.\n\nnumber of {animal[0]} : number of {animal[1]} = {a} : {b}\n\nnumber of {animal[1]} : number of {animal[2]} = {c} : {d}\n\nThere are {tot} {animal[3]} in total.",
             parts=[P("", f"Work out the number of {animal[2]}.", 4, prefix="")],
             rows=[R("", f"{a * l // b} : {l} and {l} : {d * l // c} oe", "M1", "for scaling both ratios to a common middle term"),
                   R("", f"{x} : {y} : {z}", "A1", "oe"),
                   R("", f"${tot} \\div {x + y + z} \\times {z}$", "M1", "ft their three-part ratio"),
                   R("", str(k * z), "A1", "cao")],
             values={"answer": k * z, "ratio": [x, y, z]}, diff="7-9", cw="Work out", refs=["F1.7A", "F1.7E"])


# ---------------------------------------------------------------- 1.8 accuracy
@tpl("number.accuracy", "short", n=7)
def bounds_write(r):
    kind = r.choice(["nearest", "dp", "sf"])
    if kind == "nearest":
        acc = r.choice([1, 5, 10, 100])
        v = r.randint(3, 90) * acc
        lb, ub = v - acc / 2, v + acc / 2
        desc = f"correct to the nearest {acc if acc != 1 else 'whole number'}"
    elif kind == "dp":
        v = r.randint(11, 999) / 10
        lb, ub = v - 0.05, v + 0.05
        desc = "correct to 1 decimal place"
    else:
        v = r.randint(10, 99) * r.choice([10, 100])
        e = 10 ** (len(str(v)) - 2)
        lb, ub = v - e / 2, v + e / 2
        desc = "correct to 2 significant figures"
    q, unit = r.choice([("The length of a rope", "m"), ("The mass of a bag of flour", "g"), ("The time taken", "s"),
                        ("The height of a wall", "cm")])
    return Q(parts=[P("a", f"{q} is {num(v)} {unit}, {desc}.\n\nWrite down the lower bound of the {q.split(' of ')[0].lower().replace('the ', '')}.", 1, prefix=""),
                    P("b", "Write down the upper bound.", 1, prefix="")],
             rows=[R("a", num(round(lb, 6)), "B1", ""), R("b", num(round(ub, 6)), "B1", f"accept {num(round(ub, 6))}$\\dot{{}}$ eg {num(round(ub - (0.001 if kind == 'dp' else 0.1), 6))}99…")],
             values={"lb": round(lb, 6), "ub": round(ub, 6)}, diff="4-6", cw="Write down", refs=["F1.8C"])


@tpl("number.accuracy", "short", n=7)
def estimate_sf(r):
    a = r.randint(11, 99) * 10 ** r.randint(-1, 1) + r.randint(1, 9) / 10
    b = r.randint(11, 69) / 10 + r.random() * 0.05
    c = r.randint(2, 9) / 10 + r.randint(1, 9) / 100
    a, b, c = round(a, 2), round(b, 2), round(c, 2)
    ra, rb, rc = float(sf(a, 1)), float(sf(b, 1)), float(sf(c, 1))
    est = ra * rb / rc
    if est != round(est, 3):
        return None
    return Q(parts=[P("a", f"Work out the value of $$\\frac{{{num(a)} \\times {num(b)}}}{{{num(c)}}}$$\n\nWrite down all the figures on your calculator display.", 1, prefix=""),
                    P("b", "Give your answer to part (a) correct to 3 significant figures.", 1, prefix=""),
                    P("c", "By rounding each number to 1 significant figure, find an estimate for the value of the calculation. Show your working.", 2, prefix="")],
             rows=[R("a", num(round(a * b / c, 8)), "B1", "accept at least 6 significant figures"),
                   R("b", sf(a * b / c, 3), "B1", "ft their (a)"),
                   R("c", f"$\\frac{{{num(ra)} \\times {num(rb)}}}{{{num(rc)}}}$", "M1", "for all three numbers rounded to 1 sf"),
                   R("c", num(est), "A1", "cao")],
             values={"value": round(a * b / c, 8), "sf3": sf(a * b / c, 3), "estimate": est}, diff="1-3",
             cw="Work out", refs=["F1.8B", "F1.8D", "F1.11A"])


@tpl("number.accuracy", "problem", n=7)
def bounds_calc(r):
    kind = r.choice(["speed", "area", "density", "rect_pct"])
    if kind == "speed":
        d = r.randint(100, 900)
        t = r.randint(12, 60)
        dl, du, tl, tu = d - 0.5, d + 0.5, t - 0.5, t + 0.5
        ub = du / tl
        intro = f"A cyclist travels {d} m, correct to the nearest metre, in {t} seconds, correct to the nearest second."
        ask = "Work out the upper bound for the average speed of the cyclist.\n\nGive your answer correct to 3 significant figures."
        rows = [R("", f"{du} or {tl} seen", "B1", "for one correct bound"),
                R("", f"$\\frac{{{du}}}{{{tl}}}$", "M1", "for UB distance ÷ LB time"),
                R("", sf(ub, 3), "A1", "awrt " + sf(ub, 3))]
        val = ub
        diffb = "7-9"
    elif kind == "area":
        a, b = r.randint(5, 30), r.randint(5, 30)
        lb = (a - 0.5) * (b - 0.5)
        intro = f"A rectangle has length {a} cm and width {b} cm, both correct to the nearest centimetre."
        ask = "Work out the lower bound for the area of the rectangle."
        rows = [R("", f"{a - 0.5} or {b - 0.5} seen", "B1", ""), R("", f"${a - 0.5} \\times {b - 0.5}$", "M1", ""),
                R("", num(lb), "A1", "cao")]
        val = lb
        diffb = "4-6"
    elif kind == "density":
        m = r.randint(200, 900)
        v = r.randint(20, 90)
        lbd = (m - 5) / (v + 0.5)
        intro = f"A metal block has mass {m} g, correct to the nearest 10 g, and volume {v} cm³, correct to the nearest cm³."
        ask = "Work out the lower bound for the density of the metal.\n\nGive your answer correct to 3 significant figures. Show your working clearly."
        rows = [R("", f"{m - 5} or {v + 0.5} seen", "B1", ""), R("", f"$\\frac{{{m - 5}}}{{{v + 0.5}}}$", "M1", "for LB mass ÷ UB volume"),
                R("", sf(lbd, 3), "A1", "awrt " + sf(lbd, 3))]
        val = lbd
        diffb = "7-9"
    else:
        a, b = r.randint(6, 25), r.randint(4, 20)
        small = (a - 0.5) * (b - 0.5)
        large = (a + 0.5) * (b + 0.5)
        pc = small / large * 100
        intro = f"The length and width of a rectangle are {a} cm and {b} cm, each correct to the nearest cm."
        ask = "Find the least possible area of the rectangle as a percentage of its greatest possible area. Give your answer to 3 significant figures."
        rows = [R("", f"{a - 0.5}, {b - 0.5}, {a + 0.5}, {b + 0.5}", "B1", "for at least two correct bounds"),
                R("", f"$\\frac{{{a - 0.5} \\times {b - 0.5}}}{{{a + 0.5} \\times {b + 0.5}}} \\times 100$", "M1", ""),
                R("", sf(pc, 3), "A1", "awrt " + sf(pc, 3))]
        val = pc
        diffb = "7-9"
    return Q(intro=intro, parts=[P("", ask, 3, prefix="")], rows=rows, values={"answer": round(val, 6)}, diff=diffb,
             cw="Work out", refs=["H1.8A", "F1.8C"])


@tpl("number.accuracy", "problem", n=7)
def bounds_how_many(r):
    tank = r.randint(15, 60)
    jug = r.choice([0.4, 0.5, 0.6, 0.75, 0.8])
    lbt, ubj = tank - 0.5, jug + 0.05 if jug in (0.4, 0.5, 0.6, 0.8) else jug + 0.005
    jacc = "1 decimal place" if jug in (0.4, 0.5, 0.6, 0.8) else "2 decimal places"
    ubj = round(ubj, 3)
    k = math.floor(lbt / ubj)
    return Q(intro=f"A tank holds {tank} litres of water, correct to the nearest litre. A jug holds {num(jug)} litres, correct to {jacc}.",
             parts=[P("", "Work out the greatest number of full jugs of water that can definitely be filled from the tank.\n\nShow your working clearly.", 4, prefix="")],
             rows=[R("", f"{lbt} or {num(ubj)} seen", "B1", "for a correct bound"),
                   R("", f"{lbt} and {num(ubj)}", "B1", "for the two bounds needed"),
                   R("", f"$\\frac{{{lbt}}}{{{num(ubj)}}}$ (= {sf(lbt / ubj, 5)})", "M1", "for LB tank ÷ UB jug"),
                   R("", str(k), "A1", "cao")],
             values={"answer": k}, diff="7-9", cw="Work out", refs=["H1.8A", "F1.8C"])


# ---------------------------------------------------------------- 1.9 standard form
def stdf(m, e):
    return f"{num(m)} \\times 10^{{{e}}}"


@tpl("number.standard-form", "short", n=7)
def sf_convert(r):
    m = r.randint(11, 99) / 10
    e = r.choice([-6, -5, -4, -3, 4, 5, 6, 7])
    v = m * 10 ** e
    ordinary = f"{v:.10f}".rstrip("0").rstrip(".") if e < 0 else big(round(v))
    m2 = r.randint(101, 999) / 100
    e2 = r.choice([3, 4, 5, -2, -3])
    v2 = m2 * 10 ** e2
    ord2 = f"{v2:.10f}".rstrip("0").rstrip(".") if e2 < 0 else big(round(v2))
    return Q(parts=[P("a", f"Write ${stdf(m, e)}$ as an ordinary number.", 1, prefix=""),
                    P("b", f"Write ${ord2.replace(' ', '\\,')}$ in standard form.", 1, prefix="")],
             rows=[R("a", ordinary, "B1", "cao"), R("b", f"${stdf(m2, e2)}$", "B1", "cao")],
             values={"a": ordinary, "b": f"{m2}e{e2}"}, diff="1-3", cw="Write", refs=["F1.9A"])


@tpl("number.standard-form", "short", n=7)
def sf_calc(r):
    a, ea = r.randint(12, 95) / 10, r.randint(3, 9)
    b, eb = r.randint(12, 95) / 10, r.randint(-4, 6)
    op = r.choice(["\\times", "\\div", "+"])
    if op == "+":
        eb = ea - r.randint(1, 2)
    va, vb = sp.Rational(str(a)) * 10 ** ea, sp.Rational(str(b)) * sp.Integer(10) ** eb
    res = {"\\times": va * vb, "\\div": va / vb, "+": va + vb}[op]
    e = int(math.floor(math.log10(float(res))))
    mant = float(res) / 10 ** e
    ans = f"{sf(mant, 3)} \\times 10^{{{e}}}"
    return Q(parts=[P("", f"Work out $$({stdf(a, ea)}) {op} ({stdf(b, eb)})$$\n\nGive your answer in standard form correct to 3 significant figures.", 2, prefix="")],
             rows=[R("", f"{sf(float(res), 6)} or {sf(mant, 6)} × 10^{e} oe", "M1", "for a correct value in any form"),
                   R("", f"${ans}$", "A1", "cao")],
             values={"value": float(res)}, diff="4-6", cw="Work out", refs=["F1.9A"])


@tpl("number.standard-form", "problem", n=7)
def sf_context(r):
    kind = r.choice(["planet", "cells", "grains", "light"])
    if kind == "planet":
        pop = r.randint(12, 95) / 10
        ep = r.randint(6, 8)
        area = r.randint(12, 95) / 10
        ea = r.randint(4, 6)
        res = pop * 10 ** ep / (area * 10 ** ea)
        intro = f"The population of a country is ${stdf(pop, ep)}$. The area of the country is ${stdf(area, ea)}$ km²."
        ask = "Work out the population density of the country, in people per km².\n\nGive your answer correct to 3 significant figures."
        m = f"$\\frac{{{stdf(pop, ep)}}}{{{stdf(area, ea)}}}$"
    elif kind == "cells":
        d = r.randint(12, 95) / 10
        e = -r.randint(5, 7)
        L_ = r.randint(2, 9)
        res = L_ * 10 ** -2 / (d * 10 ** e)
        intro = f"The diameter of a type of cell is ${stdf(d, e)}$ metres."
        ask = f"How many of these cells, placed in a straight line touching each other, would fit along a line of length {L_} cm?\n\nGive your answer in standard form correct to 3 significant figures."
        m = f"$\\frac{{{L_} \\times 10^{{-2}}}}{{{stdf(d, e)}}}$"
    elif kind == "grains":
        mass = r.randint(12, 95) / 10
        e = -r.randint(3, 5)
        tot = r.randint(2, 9)
        res = tot / (mass * 10 ** e)
        intro = f"The mass of one grain of rice is ${stdf(mass, e)}$ grams."
        ask = f"Work out the number of grains in {tot} grams of rice.\n\nGive your answer in standard form correct to 3 significant figures."
        m = f"$\\frac{{{tot}}}{{{stdf(mass, e)}}}$"
    else:
        spd = 3
        dist = r.randint(12, 95) / 10
        e = r.randint(9, 12)
        res = dist * 10 ** e / (3 * 10 ** 5)
        intro = f"Light travels at $3 \\times 10^5$ km per second. The distance from a planet to a star is ${stdf(dist, e)}$ km."
        ask = "Work out the time, in seconds, that light takes to travel from the star to the planet.\n\nGive your answer in standard form correct to 3 significant figures."
        m = f"$\\frac{{{stdf(dist, e)}}}{{3 \\times 10^5}}$"
    ee = int(math.floor(math.log10(res)))
    ans = f"{sf(res / 10 ** ee, 3)} \\times 10^{{{ee}}}"
    if kind == "planet":
        ans_txt = sf(res, 3)
    else:
        ans_txt = f"${ans}$"
    return Q(intro=intro, parts=[P("", ask, 3, prefix="")],
             rows=[R("", m, "M1", "for a correct method"),
                   R("", sf(res, 6), "A1", "for a correct value in any form"),
                   R("", ans_txt, "A1", "for answer in the required form")],
             values={"answer": res}, diff="4-6", cw="Work out", refs=["H1.9A", "F1.9A"])


@tpl("number.standard-form", "problem", n=7)
def sf_compare(r):
    a, ea = r.randint(12, 95) / 10, r.randint(20, 27)
    b, eb = r.randint(12, 95) / 10, ea - r.randint(1, 3)
    ratio = a * 10 ** ea / (b * 10 ** eb)
    names_ = r.choice([("Jupiter", "Earth"), ("planet P", "planet Q"), ("star X", "star Y")])
    return Q(intro=f"The mass of {names_[0]} is ${stdf(a, ea)}$ kg.\n\nThe mass of {names_[1]} is ${stdf(b, eb)}$ kg.",
             parts=[P("a", f"Work out the difference between these masses. Give your answer in standard form.", 2, prefix="kg"),
                    P("b", f"How many times heavier is {names_[0]} than {names_[1]}? Give your answer correct to 3 significant figures.", 2, prefix="")],
             rows=[R("a", f"${stdf(a, ea)} - {stdf(b, eb)}$ with powers dealt with, eg ${num(a * 10 ** (ea - eb))} \\times 10^{{{eb}}} - {stdf(b, eb)}$", "M1", ""),
                   R("a", f"${_sfmt(a * 10 ** ea - b * 10 ** eb)}$", "A1", "oe in standard form"),
                   R("b", f"$\\frac{{{stdf(a, ea)}}}{{{stdf(b, eb)}}}$", "M1", ""),
                   R("b", sf(ratio, 3), "A1", "awrt " + sf(ratio, 3))],
             values={"difference": a * 10 ** ea - b * 10 ** eb, "ratio": ratio}, diff="4-6", cw="Work out",
             refs=["H1.9A", "F1.9A"])


def _sfmt(v):
    e = int(math.floor(math.log10(abs(v))))
    m = v / 10 ** e
    return f"{fmt_strip(m)} \\times 10^{{{e}}}"


def fmt_strip(m):
    s = f"{m:.6f}".rstrip("0").rstrip(".")
    return s


# ---------------------------------------------------------------- 1.10 applying number
@tpl("number.applying", "short", n=7)
def currency_convert(r):
    pairs = [("pounds", "euros", 1.15, 1.2), ("dollars", "rupees", 82, 84), ("euros", "dollars", 1.07, 1.12),
             ("dirhams", "rupees", 22.3, 23.1), ("yuan", "dollars", 0.137, 0.142)]
    a, b, lo, hi = r.choice(pairs)
    rate = round(r.uniform(lo, hi), 3 if lo < 1 else 2)
    amt = r.randint(40, 900)
    if r.random() < 0.5:
        res = amt * rate
        txt = f"The exchange rate is 1 {a[:-1] if a.endswith('s') else a} = {num(rate)} {b}.\n\nChange {amt} {a} into {b}."
        m = f"${amt} \\times {num(rate)}$"
        ans = money(res)
    else:
        res = amt / rate
        txt = f"The exchange rate is 1 {a[:-1] if a.endswith('s') else a} = {num(rate)} {b}.\n\nChange {amt} {b} into {a}. Give your answer correct to 2 decimal places."
        m = f"${amt} \\div {num(rate)}$"
        ans = money(res)
    return Q(parts=[P("", txt, 2, prefix="")], rows=[R("", m, "M1", ""), R("", ans, "A1", "awrt " + ans)],
             values={"answer": round(res, 4)}, diff="1-3", cw="Change", refs=["F1.10C"])


@tpl("number.applying", "short", n=7)
def unit_convert(r):
    kind = r.choice(["area", "vol", "speed"])
    if kind == "area":
        v = r.randint(2, 95) / 10 * r.choice([1, 10])
        res = v * 10000
        txt = f"Change {num(v)} m² into cm²."
        m = f"${num(v)} \\times 100 \\times 100$ or $\\times 10\\,000$"
        ans = big(round(res))
    elif kind == "vol":
        v = r.randint(2, 95) * 1000
        res = v / 1e6
        txt = f"Change {big(v)} cm³ into m³."
        m = f"${big(v)} \\div 1\\,000\\,000$"
        ans = num(res)
    else:
        v = r.choice([36, 54, 72, 90, 108, 18, 45, 63])
        res = v * 1000 / 3600
        txt = f"Change a speed of {v} km/h into m/s."
        m = f"${v} \\times 1000 \\div 3600$"
        ans = num(round(res, 6))
    return Q(parts=[P("", txt, 2, prefix="")], rows=[R("", m, "M1", "for a correct conversion factor used"),
                                                       R("", ans, "A1", "cao")],
             values={"answer": res}, diff="4-6", cw="Change", refs=["F1.10B", "F4.9A"])


@tpl("number.applying", "problem", n=8)
def best_buy_currency(r):
    c1, c2, rate = r.choice([("pounds", "euros", round(r.uniform(1.12, 1.2), 2)),
                             ("dollars", "pesos", round(r.uniform(17, 19), 1)),
                             ("euros", "francs", round(r.uniform(0.93, 0.98), 2))])
    p1 = r.randint(200, 900)
    p2 = round(p1 * rate * r.uniform(0.9, 1.1))
    item = r.choice(["laptop", "camera", "bicycle", "watch"])
    conv = p1 * rate
    cheaper = "the first shop" if conv < p2 else "the second shop"
    diff_ = abs(conv - p2)
    if diff_ < 1:
        return None
    return Q(intro=f"A {item} costs {p1} {c1} in a shop in one country. The same {item} costs {p2} {c2} in a shop in another country.\n\nThe exchange rate is 1 {c1[:-1] if c1.endswith('s') else c1} = {num(rate)} {c2}.",
             parts=[P("", f"In which shop is the {item} cheaper, and by how much? Give your answer in {c2}.\n\nYou must show your working.", 3, prefix="")],
             rows=[R("", f"${p1} \\times {num(rate)} = {money(conv)}$ or ${p2} \\div {num(rate)} = {money(p2 / rate)}$", "M1", ""),
                   R("", f"${money(max(conv, p2))} - {money(min(conv, p2))}$", "M1", "for a difference in the same currency"),
                   R("", f"{cheaper} by {money(diff_)} {c2}", "A1", "both the shop and the amount needed")],
             values={"difference": round(diff_, 2)}, diff="4-6", cw="Work out", refs=["F1.10C", "F1.10A"])


@tpl("number.applying", "problem", n=8)
def time_rate_problem(r):
    start_h, start_m = r.randint(7, 15), r.choice([0, 10, 15, 20, 30, 40, 45, 50])
    dist = r.randint(60, 400)
    speed = r.choice([40, 48, 50, 60, 64, 72, 75, 80, 90])
    t = F(dist, speed)
    mins = t * 60
    if mins.denominator != 1:
        return None
    mins = int(mins)
    stop = r.choice([0, 15, 20, 25, 30])
    total = mins + stop
    eh, em = divmod(start_h * 60 + start_m + total, 60)
    nm = name(r)
    return Q(intro=f"{nm} leaves home at {start_h:02d}:{start_m:02d} and drives {dist} km to a meeting at an average speed of {speed} km/h." +
                   (f" On the way {nm} stops for {stop} minutes." if stop else ""),
             parts=[P("", f"Work out the time at which {nm} arrives at the meeting. Give your answer using the 24-hour clock.", 3, prefix="")],
             rows=[R("", f"${dist} \\div {speed}$ (= {num(float(t))} hours)", "M1", ""),
                   R("", f"{mins} minutes" + (f" + {stop} minutes" if stop else ""), "M1", "for converting to minutes or hours and minutes" + (" and adding the stop" if stop else "")),
                   R("", f"{eh:02d}:{em:02d}", "A1", "cao")],
             values={"arrival": f"{eh:02d}:{em:02d}"}, diff="4-6", cw="Work out", refs=["F1.10C", "F4.4F"])
