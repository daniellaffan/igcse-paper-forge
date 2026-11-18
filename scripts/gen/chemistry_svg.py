"""SVG drawings for the chemistry bank: apparatus, atoms, chromatograms,
displayed formulae, energy diagrams.  All drawn in our own simple style with
currentColor strokes and generic sans-serif text."""
import math

from chemistry_util import svg, L, T, R, C, PATH, PL, ARROW, LABEL, F


# ------------------------------------------------------------------ atoms
def atom(z, centre="", show_nucleus=True, W=200):
    from chemistry_util import config
    shells = [int(x) for x in config(z).split(".")]
    cx = cy = W / 2
    b = C(cx, cy, 16) + T(cx, cy, centre, size=12) if show_nucleus else ""
    for i, n in enumerate(shells):
        rr = 30 + i * 20
        b += C(cx, cy, rr, w=1)
        for j in range(n):
            # pairs on the first shell, then spread evenly
            a = -math.pi / 2 + 2 * math.pi * j / n + (0.25 if i % 2 else 0)
            x, y = cx + rr * math.cos(a), cy + rr * math.sin(a)
            b += L(x - 3, y - 3, x + 3, y + 3, w=1.3) + L(x - 3, y + 3, x + 3, y - 3, w=1.3)
    return svg(W, W, b)


# ------------------------------------------------------------------ chromatogram
def chromatogram(columns, labels, front_mm=80, base_mm=10, scale=3.0, ruler=False):
    """columns: list of lists of spot heights in mm above the baseline.  Returns svg."""
    n = len(columns)
    W = 60 + n * 50
    H = (front_mm + base_mm + 20) * scale / 2.4 + 40
    s = scale / 2.4
    top, bot = 20, 20 + (front_mm + base_mm + 15) * s
    b = R(30, top, W - 60, bot - top)
    yb = bot - base_mm * s
    yf = yb - front_mm * s
    b += L(30, yb, W - 30, yb, w=0.8, dash="5,3") + L(30, yf, W - 30, yf, w=0.8, dash="2,2")
    b += T(W - 28, yb, "baseline", anchor="start", size=10) + T(W - 28, yf, "solvent front", anchor="start", size=10)
    for i, col in enumerate(columns):
        x = 30 + 25 + i * 50
        for h in col:
            y = yb - h * s
            b += f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="6" ry="4.5" fill="currentColor" stroke="none"/>'
        b += T(x, bot + 12, labels[i], size=12)
    return svg(W + 60, bot + 24, b)


# ------------------------------------------------------------------ apparatus
def _flask(x, y, w=60, h=70):
    """Round-bottomed flask outline with neck; (x,y) is the top of the neck."""
    r = w / 2
    return PATH(f"M{x - 7},{y} L{x - 7},{y + h - 2 * r} A{r},{r} 0 1 0 {x + 7},{y + h - 2 * r} L{x + 7},{y}")


def _bunsen(x, y):
    return (R(x - 6, y, 12, 36) + R(x - 18, y + 36, 36, 6) +
            PATH(f"M{x - 5},{y - 2} Q{x},{y - 26} {x + 5},{y - 2}", w=1))


def simple_distillation(liquid="mixture", collect="distillate", label_x=False):
    b = _flask(70, 70, 70, 90) + _bunsen(70, 175)
    b += PATH("M63,140 Q70,150 77,140", w=0.6)
    b += R(64, 52, 12, 18) + L(70, 30, 70, 110, w=1) + C(70, 112, 3, fill="currentColor")   # thermometer
    b += L(77, 76, 120, 92) + L(77, 84, 120, 100)  # side arm
    # condenser
    b += PL([(120, 86), (250, 134), (244, 150), (114, 102)], close=True)
    b += L(120, 92, 250, 140, w=0.8) + L(114, 98, 244, 146, w=0.8)
    b += L(150, 112, 150, 124) + L(220, 128, 220, 116)
    b += T(150, 132, "water in", size=10) + T(220, 108, "water out", size=10)
    b += L(250, 140, 268, 156) + PATH("M258,160 L258,205 L292,205 L292,160")
    b += PATH("M259,190 L291,190", w=0.6)
    b += LABEL(50, 140, 8, 140, liquid, anchor="start") if False else T(70, 132, liquid, size=10)
    b += T(275, 218, collect, size=10) + T(70, 230, "heat", size=10)
    if label_x:
        b += T(185, 100, "X", size=13, bold=True)
    b += T(40, 34, "thermometer", size=10)
    return svg(320, 240, b)


def fractional_column(fractions=None):
    fractions = fractions or ["refinery gases", "gasoline", "kerosene", "diesel", "fuel oil", "bitumen"]
    n = len(fractions)
    b = R(110, 20, 60, 40 + 30 * n)
    for i, f in enumerate(fractions):
        y = 30 + i * 30 + (20 if i else 0)
        b += ARROW(170, y, 205, y, 5) + T(210, y, f, anchor="start", size=11)
        if 0 < i < n - 1:
            b += L(110, y + 12, 170, y + 12, w=0.6, dash="3,2")
    y_in = 40 + 30 * n - 25
    b += ARROW(40, y_in, 108, y_in, 6) + T(40, y_in - 12, "crude oil vapour", anchor="start", size=11)
    b += T(80, 26, "cool", size=11) + T(80, 40 + 30 * n, "hot", size=11)
    b += ARROW(80, 40 + 30 * n - 10, 80, 36, 5, w=0.8)
    return svg(330, 70 + 30 * n, b)


def filtration(mixture="mixture", residue="residue", filtrate="filtrate"):
    b = PATH("M60,40 L140,40 L106,95 L106,125 L94,125 L94,95 Z")
    b += PATH("M66,44 L134,44 L100,92 Z", w=0.7, dash="3,2")
    b += PATH("M70,170 L70,230 L130,230 L130,170") + L(70, 210, 130, 210, w=0.6)
    b += LABEL(100, 70, 170, 60, f"{residue}", anchor="start")
    b += LABEL(110, 220, 170, 220, filtrate, anchor="start")
    b += T(100, 28, mixture, size=11) + LABEL(130, 44, 170, 40, "filter paper", anchor="start")
    return svg(280, 245, b)


def titration(burette_label="acid", flask_label="alkali + indicator"):
    b = R(92, 15, 16, 170) + PATH("M92,185 L100,205 L108,185") + L(100, 205, 100, 215)
    b += R(84, 160, 32, 6) + L(97, 205, 103, 205, w=3)
    for i in range(8):
        b += L(92, 30 + i * 18, 100, 30 + i * 18, w=0.6)
    b += PATH("M80,225 L72,280 L128,280 L120,225 L112,225 L112,215 L88,215 L88,225 Z")
    b += PATH("M76,262 L124,262", w=0.6)
    b += LABEL(108, 60, 160, 60, "burette", anchor="start") + LABEL(108, 90, 160, 90, burette_label, anchor="start")
    b += LABEL(120, 255, 160, 255, "conical flask", anchor="start") + LABEL(115, 270, 160, 275, flask_label, anchor="start")
    b += R(60, 280, 80, 6) + T(100, 296, "white tile", size=10)
    return svg(300, 305, b)


def electrolysis(electrolyte="electrolyte", molten=False, tubes=False):
    b = PATH("M40,90 L40,200 L220,200 L220,90")
    b += L(40, 120, 220, 120, w=0.6, dash="4,3")
    b += R(80, 70, 12, 110) + R(168, 70, 12, 110)
    if tubes:
        b += PATH("M72,180 L72,50 Q86,38 100,50 L100,180", w=1) + PATH("M160,180 L160,50 Q174,38 188,50 L188,180", w=1)
    b += L(86, 70, 86, 30) + L(174, 70, 174, 30) + L(86, 30, 115, 30) + L(145, 30, 174, 30)
    b += L(115, 18, 115, 42, w=1.4) + L(123, 24, 123, 36, w=2.4)  # cell
    b += L(123, 30, 145, 30)
    b += T(110, 12, "+", size=12) + T(130, 12, "−", size=13)
    b += T(86, 214, "anode (+)", size=11) + T(174, 214, "cathode (−)", size=11)
    b += T(130, 160, electrolyte, size=11)
    if molten:
        b += _bunsen(130, 222)
        return svg(260, 280, b)
    return svg(260, 225, b)


def gas_syringe(reactants="reaction mixture", gas_label="gas syringe"):
    b = PATH("M40,150 L40,110 Q40,90 58,86 L58,70 L72,70 L72,86 Q90,90 90,110 L90,150 Z")
    b += L(44, 132, 86, 132, w=0.6)
    b += L(65, 70, 65, 50) + L(65, 50, 130, 50)
    b += R(130, 40, 140, 20) + R(160, 43, 110, 14, dash="2,2") + L(270, 50, 300, 50)
    for i in range(7):
        b += L(140 + i * 18, 40, 140 + i * 18, 34, w=0.6)
    b += T(200, 26, gas_label, size=11) + T(65, 168, reactants, size=11)
    return svg(320, 180, b)


def gas_over_water(reactants="reactants"):
    b = PATH("M30,150 L30,110 Q30,90 48,86 L48,70 L62,70 L62,86 Q80,90 80,110 L80,150 Z")
    b += L(34, 132, 76, 132, w=0.6)
    b += L(55, 70, 55, 50) + L(55, 50, 190, 50) + L(190, 50, 190, 145)
    b += PATH("M140,110 L140,190 L290,190 L290,110") + L(140, 130, 290, 130, w=0.6)
    b += PATH("M175,175 L175,40 L205,40 L205,175") if False else PATH("M178,170 L178,30 L208,30 L208,170")
    for i in range(6):
        b += L(208, 45 + i * 20, 200, 45 + i * 20, w=0.6)
    b += T(55, 168, reactants, size=11) + LABEL(208, 60, 230, 70, "measuring cylinder", anchor="start")
    b += T(250, 178, "water", size=10)
    return svg(330, 200, b)


def calorimeter(contents="solution"):
    b = PATH("M60,60 L70,170 L130,170 L140,60") + L(60, 60, 140, 60)
    b += PATH("M66,90 L134,90", w=0.6)
    b += R(95, 15, 10, 140, rx=4) + C(100, 150, 5, fill="currentColor")
    b += R(55, 52, 90, 8)
    b += PATH("M40,160 L40,195 L160,195 L160,160", w=0.8)
    b += LABEL(105, 30, 160, 30, "thermometer", anchor="start") + LABEL(145, 56, 160, 50, "lid", anchor="start")
    b += LABEL(136, 110, 165, 110, "polystyrene cup", anchor="start") + LABEL(120, 130, 165, 140, contents, anchor="start")
    b += LABEL(156, 180, 175, 180, "beaker", anchor="start")
    return svg(290, 205, b)


def spirit_burner(fuel="fuel"):
    b = R(70, 30, 60, 70) + L(70, 45, 130, 45, w=0.6) + T(100, 70, "water", size=11)
    b += R(96, 5, 8, 80, rx=3) + C(100, 85, 4, fill="currentColor")
    b += PATH("M85,150 L85,175 L115,175 L115,150 Z") + L(100, 150, 100, 140)
    b += PATH("M94,140 Q100,110 106,140", w=1)
    b += LABEL(130, 60, 160, 60, "copper can", anchor="start") + LABEL(115, 165, 160, 165, f"spirit burner ({fuel})", anchor="start")
    b += LABEL(104, 15, 160, 15, "thermometer", anchor="start")
    return svg(330, 185, b)


def mass_loss():
    b = R(40, 160, 160, 26) + R(90, 166, 60, 14) + T(120, 173, "g", size=11)
    b += PATH("M90,160 L80,110 Q80,90 108,80 L108,55 L132,55 L132,80 Q160,90 160,110 L150,160 Z")
    b += PATH("M106,58 Q120,46 134,58", w=0.8) + T(120, 40, "cotton wool", size=10)
    b += L(86, 135, 154, 135, w=0.6)
    for x, y in ((105, 150), (120, 152), (135, 149)):
        b += R(x - 5, y - 4, 10, 7)
    b += LABEL(150, 125, 205, 120, "dilute acid", anchor="start") + LABEL(136, 150, 205, 152, "marble chips", anchor="start")
    b += T(120, 198, "balance", size=10)
    return svg(290, 205, b)


def iron_wool_syringes():
    b = R(20, 70, 90, 20) + R(40, 73, 70, 14, dash="2,2") + L(110, 80, 130, 80)
    b += R(130, 72, 110, 16) + T(185, 100, "iron wool", size=10)
    for x in range(140, 235, 9):
        b += PATH(f"M{x},76 q4,4 0,8", w=0.6)
    b += L(240, 80, 260, 80) + R(260, 70, 90, 20) + R(260, 73, 50, 14, dash="2,2")
    b += T(65, 60, "syringe A", size=10) + T(305, 60, "syringe B", size=10)
    return svg(370, 110, b)


def heat_tube(solid="solid", delivery=True, liquid="limewater"):
    b = PATH("M40,60 L170,60 Q180,70 170,80 L40,80") + L(40, 60, 40, 80, w=2.2)
    b += PATH("M120,80 q15,3 40,0", fill="currentColor", w=0.5) if False else R(120, 72, 40, 7, fill="currentColor")
    b += _bunsen(140, 110)
    if delivery:
        b += L(40, 70, 20, 70) + L(20, 70, 20, 120) + L(20, 120, 240, 120) if False else (
            L(40, 70, 15, 70) + L(15, 70, 15, 30) + L(15, 30, 250, 30) + L(250, 30, 250, 140))
        b += PATH("M225,100 L225,175 L275,175 L275,100") + L(225, 130, 275, 130, w=0.6)
        b += T(250, 188, liquid, size=11)
    b += T(140, 50, solid, size=11)
    return svg(300, 195, b)


# ------------------------------------------------------------------ energy diagrams
def energy_level(exo=True, react="reactants", prod="products", dh_label="ΔH"):
    y1, y2 = (70, 150) if exo else (150, 70)
    b = ARROW(40, 190, 40, 20, 6) + L(40, 190, 300, 190)
    b += T(18, 105, "energy", size=11) if False else (
        '<text x="22" y="105" transform="rotate(-90 22 105)" text-anchor="middle" fill="currentColor" '
        'stroke="none" font-size="11">energy</text>')
    b += L(70, y1, 150, y1, w=2) + L(190, y2, 270, y2, w=2)
    b += T(110, y1 - 12, react, size=11) + T(230, y2 - 12, prod, size=11)
    b += ARROW(170, y1, 170, y2, 6) + T(178, (y1 + y2) / 2, dh_label, anchor="start", size=11)
    b += T(170, 205, "progress of reaction", size=11)
    return svg(320, 215, b)


def profile(exo=True, react="reactants", prod="products", labels=True, cat=False):
    y1, y2 = (130, 170) if exo else (170, 120)
    if exo:
        y1, y2 = 120, 170
    peak = 50
    b = ARROW(40, 200, 40, 20, 6) + L(40, 200, 310, 200)
    b += ('<text x="22" y="110" transform="rotate(-90 22 110)" text-anchor="middle" fill="currentColor" '
          'stroke="none" font-size="11">energy</text>')
    b += PATH(f"M55,{y1} L95,{y1} C140,{y1} 140,{peak} 170,{peak} C200,{peak} 200,{y2} 245,{y2} L290,{y2}", w=1.8)
    if cat:
        p2 = peak + (min(y1, y2) - peak) * 0.55
        b += PATH(f"M95,{y1} C140,{y1} 140,{p2} 170,{p2} C200,{p2} 200,{y2} 245,{y2}", dash="5,3", w=1.3)
    b += T(72, y1 - 10, react, size=11) + T(272, y2 - 10, prod, size=11)
    if labels:
        b += ARROW(110, y1, 110, peak + 2, 5, w=1) + T(104, (y1 + peak) / 2, "A", anchor="end", size=12, bold=True)
        b += ARROW(265, y1, 265, y2, 5, w=1) + L(245, y1, 290, y1, w=0.6, dash="3,2")
        b += T(272, (y1 + y2) / 2, "B", anchor="start", size=12, bold=True)
    b += T(175, 214, "progress of reaction", size=11)
    return svg(320, 222, b)


# ------------------------------------------------------------------ lattices
def metallic_lattice(charge="+", rows=3, cols=5):
    b = ""
    for i in range(rows):
        for j in range(cols):
            x, y = 40 + j * 46, 35 + i * 46
            b += C(x, y, 16) + T(x, y, charge, size=12)
    import random as _r
    rr = _r.Random(7)
    for _ in range(rows * cols + 4):
        x, y = 20 + rr.random() * (cols * 46), 15 + rr.random() * (rows * 46)
        b += T(x, y, "e⁻", size=9)
    return svg(cols * 46 + 30, rows * 46 + 20, b)


def ionic_lattice(cat="Na⁺", an="Cl⁻", n=4):
    b = ""
    for i in range(n):
        for j in range(n):
            x, y = 35 + j * 44, 30 + i * 44
            big = (i + j) % 2
            b += C(x, y, 18 if big else 11) + T(x, y, an if big else cat, size=10 if big else 9)
    return svg(n * 44 + 30, n * 44 + 20, b)


# ------------------------------------------------------------------ displayed formulae
def displayed(atoms_, bonds=None, bracket=False, W=None):
    """atoms_: list of dicts for a straight backbone {el, up, down, left, right}.
    Substituent values: 'H', 'Cl', 'Br', 'OH', '=O', 'CH3' or None. bonds: list of '1'/'2'
    between backbone atoms. bracket=True draws a polymer repeat unit with extension bonds and n."""
    n = len(atoms_)
    bonds = bonds or ["1"] * (n - 1)
    dx = 56
    x0 = 70 if not bracket else 80
    y0 = 90
    b = ""

    def bond(x1, y1, x2, y2, order="1"):
        if order == "2":
            if abs(y1 - y2) < 1:
                return L(x1, y1 - 3, x2, y2 - 3) + L(x1, y1 + 3, x2, y2 + 3)
            return L(x1 - 3, y1, x2 - 3, y2) + L(x1 + 3, y1, x2 + 3, y2)
        return L(x1, y1, x2, y2)

    def sub(x, y, s, d):
        # d = (dx, dy) unit direction
        if s is None:
            return ""
        ux, uy = d
        if s == "=O":
            return bond(x + ux * 9, y + uy * 9, x + ux * 32, y + uy * 32, "2") + T(x + ux * 40, y + uy * 40, "O", size=13)
        if s == "OH":
            ex = bond(x + ux * 9, y + uy * 9, x + ux * 32, y + uy * 32) + T(x + ux * 40, y + uy * 40, "O", size=13)
            ex += L(x + ux * 48, y + uy * 48, x + ux * 68, y + uy * 68) + T(x + ux * 76, y + uy * 76, "H", size=13)
            return ex
        return bond(x + ux * 9, y + uy * 9, x + ux * 32, y + uy * 32) + T(x + ux * 40, y + uy * 40, s, size=13)

    for i, a in enumerate(atoms_):
        x = x0 + i * dx
        b += T(x, y0, a.get("el", "C"), size=13)
        b += sub(x, y0, a.get("up"), (0, -1)) + sub(x, y0, a.get("down"), (0, 1))
        if i == 0:
            b += sub(x, y0, a.get("left"), (-1, 0))
        if i == n - 1:
            b += sub(x, y0, a.get("right"), (1, 0))
        if i < n - 1:
            b += bond(x + 9, y0, x + dx - 9, y0, bonds[i])
    xl, xr = x0, x0 + (n - 1) * dx
    if bracket:
        b += L(xl - 9, y0, xl - 40, y0) + L(xr + 9, y0, xr + 40, y0)
        b += PATH(f"M{xl - 24},{y0 - 50} q-8,50 0,100") + PATH(f"M{xr + 24},{y0 - 50} q8,50 0,100")
        b += T(xr + 34, y0 + 52, "n", size=13, it=True)
    right_extra = 0
    if not bracket and atoms_[-1].get("right") == "OH":
        right_extra = 80
    elif not bracket and atoms_[-1].get("right"):
        right_extra = 45
    w = W or (xr + (60 if bracket else 30) + right_extra)
    top_extra = 0
    return svg(max(w, 160), 180 + top_extra, f'<g transform="translate(0,0)">{b}</g>')


def chain(nc, double_at=None, subs=None, end="H"):
    """Backbone for a straight-chain hydrocarbon derivative with nc carbons.
    double_at = index of first carbon of the C=C (0-based).  subs = {(i,'up'|'down'|'left'|'right'): group}."""
    subs = subs or {}
    at, bonds = [], []
    for i in range(nc):
        a = {"el": "C", "up": "H", "down": "H"}
        if i == 0:
            a["left"] = "H"
        if i == nc - 1:
            a["right"] = end
        at.append(a)
    for i in range(nc - 1):
        bonds.append("2" if double_at == i else "1")
    if double_at is not None:
        at[double_at]["down"] = None
        at[double_at + 1]["down"] = None
    for (i, pos), g in subs.items():
        at[i][pos] = g
    return at, bonds
