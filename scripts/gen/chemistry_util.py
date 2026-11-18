"""Shared helpers for the 4CH1 chemistry generator.

* chemical text: F() turns plain formulae ("CuSO4.5H2O", "SO4^2-") into Unicode
  sub/superscripts; Mr() computes relative formula masses from the same strings;
  EQ() parses, *checks the balance of* (atoms and charge) and renders equations.
* question builders: mcq(), pts(), anyof(), lv6() and the @tpl registry.
* SVG helpers for apparatus, graphs, chromatograms, atom diagrams.
Every template returns a dict (parts, markscheme, spec_refs, difficulty, ...);
chemistry.py adds subject-wide fields and runs the checks.
"""
import math
import re
from fractions import Fraction

from common import fmt_num, row  # noqa: F401

TEMPLATES = []


def tpl(sub, qtype, n=12):
    def deco(f):
        TEMPLATES.append({"name": f.__name__, "sub": sub, "qtype": qtype, "n": n, "f": f})
        return f
    return deco


# --------------------------------------------------------------- atomic data
# symbol: (Z, Ar as printed on the paper's Periodic Table, name)
EL = {}
_PT = """H 1 1 hydrogen|He 2 4 helium|Li 3 7 lithium|Be 4 9 beryllium|B 5 11 boron|C 6 12 carbon|N 7 14 nitrogen|
O 8 16 oxygen|F 9 19 fluorine|Ne 10 20 neon|Na 11 23 sodium|Mg 12 24 magnesium|Al 13 27 aluminium|Si 14 28 silicon|
P 15 31 phosphorus|S 16 32 sulfur|Cl 17 35.5 chlorine|Ar 18 40 argon|K 19 39 potassium|Ca 20 40 calcium|
Sc 21 45 scandium|Ti 22 48 titanium|V 23 51 vanadium|Cr 24 52 chromium|Mn 25 55 manganese|Fe 26 56 iron|
Co 27 59 cobalt|Ni 28 59 nickel|Cu 29 63.5 copper|Zn 30 65 zinc|Ga 31 70 gallium|Ge 32 73 germanium|
As 33 75 arsenic|Se 34 79 selenium|Br 35 80 bromine|Kr 36 84 krypton|Rb 37 85 rubidium|Sr 38 88 strontium|
Y 39 89 yttrium|Zr 40 91 zirconium|Nb 41 93 niobium|Mo 42 96 molybdenum|Tc 43 [98] technetium|Ru 44 101 ruthenium|
Rh 45 103 rhodium|Pd 46 106 palladium|Ag 47 108 silver|Cd 48 112 cadmium|In 49 115 indium|Sn 50 119 tin|
Sb 51 122 antimony|Te 52 128 tellurium|I 53 127 iodine|Xe 54 131 xenon|Cs 55 133 caesium|Ba 56 137 barium|
La 57 139 lanthanum|Hf 72 178 hafnium|Ta 73 181 tantalum|W 74 184 tungsten|Re 75 186 rhenium|Os 76 190 osmium|
Ir 77 192 iridium|Pt 78 195 platinum|Au 79 197 gold|Hg 80 201 mercury|Tl 81 204 thallium|Pb 82 207 lead|
Bi 83 209 bismuth|Po 84 [209] polonium|At 85 [210] astatine|Rn 86 [222] radon|Fr 87 [223] francium|
Ra 88 [226] radium|Ac 89 [227] actinium|Rf 104 [261] rutherfordium|Db 105 [262] dubnium|Sg 106 [266] seaborgium|
Bh 107 [264] bohrium|Hs 108 [277] hassium|Mt 109 [268] meitnerium|Ds 110 [271] darmstadtium|Rg 111 [272] roentgenium"""
for _e in _PT.replace("\n", "").split("|"):
    s, z, a, nm = _e.split()
    EL[s] = (int(z), a, nm)


def AR(sym):
    a = EL[sym][1].strip("[]")
    return Fraction(a) if "." not in a else Fraction(str(a))


def config(z):
    """Electronic configuration of the first 20 elements, e.g. '2.8.1'."""
    shells, left = [], z
    for cap in (2, 8, 8, 2):
        take = min(cap, left)
        if take:
            shells.append(take)
        left -= take
    return ".".join(map(str, shells))


GROUP = {}
for _s, (_z, _a, _n) in EL.items():
    if _z <= 20:
        last = int(config(_z).split(".")[-1])
        GROUP[_s] = 0 if (_s in ("He", "Ne", "Ar")) else last
PERIOD = {s: len(config(EL[s][0]).split(".")) for s in GROUP}

# --------------------------------------------------------------- formulae
SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
SUP = str.maketrans("0123456789+-", "⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻")


def F(s):
    """Plain formula/equation text -> Unicode. 'SO4^2-' -> SO₄²⁻, 'CuSO4·5H2O' -> CuSO₄·5H₂O.
    Digits directly after a letter or ')' become subscripts. '^..' is a charge.
    Spaces and other text are left alone, so whole equations can be passed."""
    out = []
    i = 0
    while i < len(s):
        c = s[i]
        if c == "^":
            j = i + 1
            while j < len(s) and (s[j].isdigit() or s[j] in "+-"):
                j += 1
            out.append(s[i + 1:j].translate(SUP))
            i = j
            continue
        if c.isdigit() and i > 0 and ((s[i - 1].isalpha() or s[i - 1] in ")]") and not _in_word(s, i)
                                      or (s[i - 1].isdigit() and out and out[-1] in "₀₁₂₃₄₅₆₇₈₉")):
            out.append(c.translate(SUB))
        else:
            out.append(c)
        i += 1
    return "".join(out)


def _in_word(s, i):
    # digit inside a normal word such as 'Q1' or 'but-1-ene' should not be subscripted
    j = i - 1
    while j >= 0 and s[j].isalpha():
        j -= 1
    word = s[j + 1:i]
    if not word:
        return False
    if word[0].isupper():
        # every capital-led chunk must be an element symbol, e.g. 'CuSO' 'NaOH'
        return not re.fullmatch(r"(?:[A-Z][a-z]?)+", word) or not all(
            t in EL for t in re.findall(r"[A-Z][a-z]?", word))
    return True


_TOK = re.compile(r"([A-Z][a-z]?)(\d*)|(\()|(\))(\d*)")


def atoms(formula):
    """Count atoms in a plain formula, e.g. 'Ca(OH)2', 'CuSO4.5H2O', 'SO4^2-'."""
    f = formula.split("^")[0]
    total = {}
    for chunk in re.split(r"[.·]", f):
        m = re.match(r"^(\d+)(.*)$", chunk)
        mult = 1
        if m and not chunk[0].isalpha():
            mult, chunk = int(m.group(1)), m.group(2)
        stack = [{}]
        for sym, n, op, cl, cn in _TOK.findall(chunk):
            if op:
                stack.append({})
            elif cl:
                top = stack.pop()
                k = int(cn) if cn else 1
                for e, v in top.items():
                    stack[-1][e] = stack[-1].get(e, 0) + v * k
            else:
                assert sym in EL, (formula, sym)
                stack[-1][sym] = stack[-1].get(sym, 0) + (int(n) if n else 1)
        for e, v in stack[0].items():
            total[e] = total.get(e, 0) + v * mult
    return total


def charge(formula):
    if "^" not in formula:
        return 0
    c = formula.split("^")[1]
    n = int(c[:-1]) if c[:-1] else 1
    return n if c[-1] == "+" else -n


def Mr(formula):
    return sum(AR(e) * n for e, n in atoms(formula).items())


def num(x, sf=None, dp=None):
    """Format a Fraction/float cleanly."""
    x = float(x)
    if sf is None and dp is None:
        if abs(x - round(x)) < 1e-9:
            return str(int(round(x)))
        return fmt_num(round(x, 6))
    return fmt_num(x, sf=sf, dp=dp)


def mr_str(formula):
    return num(Mr(formula))


# --------------------------------------------------------------- equations
_STATE = re.compile(r"\((s|l|g|aq)\)$")


def _split_side(side):
    terms = []
    for t in side.split(" + "):
        t = t.strip()
        st = _STATE.search(t)
        state = st.group(1) if st else None
        if st:
            t = t[:st.start()]
        m = re.match(r"^(\d+(?:/\d+)?)(?=[A-Ze(])", t)
        coef = Fraction(m.group(1)) if m else Fraction(1)
        if m:
            t = t[m.end():]
        terms.append((coef, t, state))
    return terms


def balanced(eq):
    arrow = "<=>" if "<=>" in eq else "->"
    lhs, rhs = eq.split(f" {arrow} ")
    tot = []
    for side in (lhs, rhs):
        a, q = {}, Fraction(0)
        for coef, f, _ in _split_side(side):
            if f.startswith("e^-"):
                q += -coef
                continue
            for e, n in atoms(f).items():
                a[e] = a.get(e, 0) + coef * n
            q += coef * charge(f)
        tot.append((a, q))
    return tot[0] == tot[1]


def EQ(eq, states=True):
    """Check balance and render. '->' becomes →, '<=>' becomes ⇌.
    states=False strips state symbols from the rendered text."""
    assert balanced(eq), f"unbalanced: {eq}"
    s = eq if states else re.sub(r"\((s|l|g|aq)\)", "", eq)
    s = s.replace("<=>", "⇌").replace("->", "→")
    s = re.sub(r"e\^-", "e⁻", s)
    return F(s)


def eq_terms(eq):
    arrow = "<=>" if "<=>" in eq else "->"
    lhs, rhs = eq.split(f" {arrow} ")
    return _split_side(lhs), _split_side(rhs)


def unbalanced_skeleton(eq):
    """Return the equation with all coefficients removed (formulae only)."""
    L, R = eq_terms(eq)
    arrow = " ⇌ " if "<=>" in eq else " → "
    f = lambda side: " + ".join(F(t) + (f"({s})" if s else "") for _, t, s in side)
    return f(L) + arrow + f(R)


# --------------------------------------------------------------- mark scheme helpers
LET = "ABCD"


def mcq(r, stem, correct, wrong, notes=None, intro=None, label=""):
    """One-mark multiple choice. `wrong` = list of >= 3 distractors (3 are sampled)."""
    w = list(wrong)
    r.shuffle(w)
    ch = [correct] + w[:3]
    # deterministic ordering: numbers ascending, otherwise random
    try:
        vals = [float(re.sub(r"[^0-9.\-]", "", c.split()[0])) for c in ch]
        if all(re.match(r"^-?[0-9.]+", c) for c in ch):
            ch = [c for _, c in sorted(zip(vals, ch))]
        else:
            r.shuffle(ch)
    except (ValueError, IndexError):
        r.shuffle(ch)
    k = ch.index(correct)
    part = {"label": label, "text": stem, "marks": 1, "space": "mcq", "choices": ch}
    others = ", ".join(LET[i] for i in range(4) if i != k)
    rw = row(label, f"{LET[k]} ({correct})", 1, notes or f"{others} incorrect", "AO1")
    return part, rw


def pts(part, points, notes=None, lead=None, ao=None):
    """One row per marking point M1, M2 ... each worth 1."""
    rows = []
    notes = notes or {}
    for i, p in enumerate(points):
        ans = f"M{i + 1} {p}"
        if i == 0 and lead:
            ans = f"{lead}\n{ans}"
        rows.append(row(part, ans, 1, notes.get(i), ao))
    return rows


def anyof(part, n, points, notes=None, lead=None, ao=None):
    """A single row: 'any n from' a list of creditworthy points."""
    if len(points) == n and n > 1 and lead is None:
        lead = f"All {WORD[n]} points needed, one mark each"
    head = lead or (f"Any {WORD[n]} from:" if len(points) > n else "")
    body = "\n".join(f"• {p}" for p in points) if len(points) > 1 else points[0]
    return [row(part, (head + "\n" + body).strip(), n, notes, ao)]


WORD = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six"}

GRID6 = [
    ("0", "0", "No rewardable material."),
    ("1", "1–2", "A few relevant points (e.g. a reagent, an observation or a single idea) that are largely "
                 "isolated; the method or explanation could not be followed or is mostly incomplete."),
    ("2", "3–4", "Several relevant, mostly accurate points with some linkage; a workable outline is given "
                 "but there are gaps, such as a missing step, condition, observation or reason."),
    ("3", "5–6", "A detailed, accurate and logically ordered answer that covers all the main stages or ideas, "
                 "using correct chemical terms, reagents, conditions and observations."),
]


def lv6(part, indicative, title=None, ao_split="AO1 3, AO2 3"):
    from common import levels
    return levels(part, GRID6, indicative, title=title, ao_split=ao_split,
                  credit_note="Indicative content is not exhaustive: credit any other valid chemistry.")


LV_GENERAL = ("Award a level first, then a mark within it. Live papers mark these 6-mark answers as six "
              "separate marking points, so the indicative content doubles as a checklist: an answer that "
              "makes about n of these points securely is usually worth about n marks.")


def lines_for(marks):
    return {1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 14}.get(marks, marks * 2 + 2)


FIXED_UNIT = {"percentage = ": "%", "percentage yield = ": "%", "mean titre = ": "cm³", "ΔH = ": "kJ/mol", "amount = ": "mol",
              "temperature = ": "°C", "loss in mass = ": "g", "abundance = ": "%"}
UNIT_RX = re.compile(r"(?:\bin|answer in|units of)\s+(g per 100 g of water|kJ/mol|mol/dm³|g/dm³|cm³/s|cm³/min|g/s|g/min|mol/s|kJ|J|cm³|dm³|tonnes|kg|g|mol|°C|%)(?![\w/³])")


def suffix_for(prefix, text):
    """Unit printed after the answer dots, when the question fixes it."""
    if prefix in FIXED_UNIT:
        return FIXED_UNIT[prefix]
    m = UNIT_RX.findall(F(text)) if prefix else []
    if m:
        return m[-1]
    return {"mass = ": "g", "volume = ": "cm³", "solubility = ": "g per 100 g of water"}.get(prefix)


def P(label, text, marks, **kw):
    if kw.get("answer_prefix") and "answer_suffix" not in kw:
        u = suffix_for(kw["answer_prefix"], text)
        if u:
            kw["answer_suffix"] = u
    p = {"label": label, "text": text, "marks": marks}
    if "space" not in kw and "lines" not in kw:
        kw["lines"] = lines_for(marks)
    p.update(kw)
    return p


def band_of(*xs):
    """Pick the hardest band among items."""
    order = ["1-3", "4-6", "7-9"]
    return max(xs, key=order.index)


# --------------------------------------------------------------- SVG
def svg(w, h, body, fs=12):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" font-family="sans-serif" '
            f'font-size="{fs}" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round" '
            f'stroke-linecap="round">{body}</svg>')


def L(x1, y1, x2, y2, w=None, dash=None):
    e = f' stroke-width="{w}"' if w else ""
    e += f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}"{e}/>'


def T(x, y, s, anchor="middle", size=None, it=False, bold=False):
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    e = f' font-size="{size}"' if size else ""
    e += ' font-style="italic"' if it else ""
    e += ' font-weight="bold"' if bold else ""
    return (f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" dominant-baseline="middle" '
            f'fill="currentColor" stroke="none"{e}>{s}</text>')


def R(x, y, w, h, fill=None, rx=0, dash=None):
    f = f' fill="{fill}"' if fill else ""
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}"{f}{d}/>'


def C(x, y, r, fill=None, w=None):
    f = f' fill="{fill}"' if fill else ""
    ww = f' stroke-width="{w}"' if w else ""
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}"{f}{ww}/>'


def PATH(d, fill=None, dash=None, w=None):
    f = f' fill="{fill}"' if fill else ""
    f += f' stroke-dasharray="{dash}"' if dash else ""
    f += f' stroke-width="{w}"' if w else ""
    return f'<path d="{d}"{f}/>'


def PL(pts_, close=False, fill=None, w=None):
    p = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts_)
    f = f' fill="{fill}"' if fill else ""
    f += f' stroke-width="{w}"' if w else ""
    return f'<polygon points="{p}"{f}/>' if close else f'<polyline points="{p}"{f}/>'


def ARROW(x1, y1, x2, y2, head=6, w=None):
    a = math.atan2(y2 - y1, x2 - x1)
    p1 = (x2 - head * math.cos(a - 0.4), y2 - head * math.sin(a - 0.4))
    p2 = (x2 - head * math.cos(a + 0.4), y2 - head * math.sin(a + 0.4))
    return L(x1, y1, x2, y2, w) + PL([p1, (x2, y2), p2], close=True, fill="currentColor")


def LABEL(x, y, tx, ty, s, anchor="start"):
    """Label line from (x,y) on the object to text at (tx,ty)."""
    return L(x, y, tx - (3 if anchor == "start" else -3), ty, w=0.8) + T(tx, ty, s, anchor=anchor, size=11)


def nice_ticks(vmax, n=5):
    raw = vmax / n
    mag = 10 ** math.floor(math.log10(raw))
    for m in (1, 2, 2.5, 5, 10):
        if raw <= m * mag:
            step = m * mag
            break
    top = math.ceil(vmax / step - 1e-9) * step
    return step, top


def graph(xlabel, ylabel, series, xmax=None, ymax=None, xstep=None, ystep=None, grid=True, markers=True,
          smooth=True, labels=None, ymin=0, xmin=0, W=420, H=300, legend=None):
    """Line graph.  series = list of point lists.  Returns svg string.
    Points are plotted as small crosses; a curve is drawn through them if smooth/lines requested."""
    allx = [p[0] for s in series for p in s] or [1]
    ally = [p[1] for s in series for p in s] or [1]
    if xmax is None:
        xstep, xmax = nice_ticks(max(allx))
    if ymax is None:
        ystep, ymax = nice_ticks(max(ally))
    xstep = xstep or nice_ticks(xmax)[0]
    ystep = ystep or nice_ticks(ymax - ymin)[0]
    ox, oy, pw, ph = 60, H - 45, W - 80, H - 70
    X = lambda v: ox + (v - xmin) / (xmax - xmin) * pw
    Y = lambda v: oy - (v - ymin) / (ymax - ymin) * ph
    b = ""
    if grid:
        nx = round((xmax - xmin) / xstep * 5)
        ny = round((ymax - ymin) / ystep * 5)
        for i in range(nx + 1):
            x = ox + pw * i / nx
            b += L(x, oy, x, oy - ph, w=(0.6 if i % 5 == 0 else 0.25))
        for j in range(ny + 1):
            y = oy - ph * j / ny
            b += L(ox, y, ox + pw, y, w=(0.6 if j % 5 == 0 else 0.25))
    b += L(ox, oy, ox + pw, oy, w=1.4) + L(ox, oy, ox, oy - ph, w=1.4)
    v = xmin
    while v <= xmax + 1e-9:
        b += L(X(v), oy, X(v), oy + 4) + T(X(v), oy + 14, num(round(v, 6)), size=11)
        v += xstep
    v = ymin
    while v <= ymax + 1e-9:
        b += L(ox - 4, Y(v), ox, Y(v)) + T(ox - 8, Y(v), num(round(v, 6)), anchor="end", size=11)
        v += ystep
    b += T(ox + pw / 2, H - 10, xlabel, size=12)
    b += (f'<text x="14" y="{oy - ph / 2:.1f}" transform="rotate(-90 14 {oy - ph / 2:.1f})" text-anchor="middle" '
          f'fill="currentColor" stroke="none" font-size="12">{ylabel}</text>')
    for si, s in enumerate(series):
        pts_ = [(X(x), Y(y)) for x, y in s]
        if smooth and len(pts_) > 2:
            b += PATH(_catmull(pts_), w=1.6)
        elif len(pts_) > 1:
            b += PL(pts_, w=1.6)
        if markers:
            for x, y in pts_:
                b += L(x - 3, y - 3, x + 3, y + 3, w=1.2) + L(x - 3, y + 3, x + 3, y - 3, w=1.2)
        if labels and si < len(labels) and labels[si]:
            lx, ly = pts_[-1]
            b += T(min(lx + 4, W - 4), ly - 8, labels[si], anchor="end", size=11)
    return svg(W, H, b)


def _catmull(p):
    d = f"M{p[0][0]:.1f},{p[0][1]:.1f}"
    for i in range(len(p) - 1):
        p0 = p[i - 1] if i else p[i]
        p1, p2 = p[i], p[i + 1]
        p3 = p[i + 2] if i + 2 < len(p) else p2
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d += f" C{c1[0]:.1f},{c1[1]:.1f} {c2[0]:.1f},{c2[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}"
    return d


def fig(s, width=110, caption=None, note=None):
    f = {"type": "svg", "svg": s, "width": width}
    if caption:
        f["caption"] = caption
    if note:
        f["note"] = note
    return f


def table(headers, rows, caption=None):
    t = {"type": "table", "headers": headers, "rows": [[str(c) for c in r] for r in rows]}
    if caption:
        t["caption"] = caption
    return t


def Q(cw, d, parts, rows, refs, intro=None, figs=None, ans=None, ao=None, style="points", levels_=None, general=None):
    q = {"command_word": cw, "difficulty": d, "parts": parts,
         "markscheme": {"style": style, "rows": rows}, "spec_refs": list(refs), "ao": ao or ["AO2"]}
    if levels_:
        q["markscheme"]["levels"] = levels_
    if general:
        q["markscheme"]["general"] = general
    if intro:
        q["intro"] = intro
    if figs:
        q["figures"] = figs
    if ans:
        q["answer"] = {"method": ans[0], "values": ans[1], "checked": True}
    return q


def pick(r, seq, k=None):
    return r.choice(seq) if k is None else r.sample(seq, k)
