"""Original inline-SVG figures for economics questions (black on transparent, generic fonts)."""
import math

OX, OY, XM, YT = 62, 205, 300, 22   # origin, x max, y top
FONT = 'font-family="sans-serif" font-size="11" fill="currentColor"'


def _t(x, y, s, anchor="middle", size=11, italic=False):
    st = ' font-style="italic"' if italic else ""
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-family="sans-serif" font-size="{size}" fill="currentColor"{st}>{s}</text>'


def _l(x1, y1, x2, y2, dash=False, w=1.6):
    d = ' stroke-dasharray="4 3"' if dash else ""
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="currentColor" stroke-width="{w}"{d}/>'


def _wrap(s, n=12):
    words, lines, cur = s.split(), [], ""
    for w in words:
        if len(cur) + len(w) + 1 > n and cur:
            lines.append(cur)
            cur = w
        else:
            cur = (cur + " " + w).strip()
    lines.append(cur)
    return lines


def _axes(xlabel, ylabel):
    out = [_l(OX, OY, OX, YT - 4, w=1.4), _l(OX, OY, XM + 8, OY, w=1.4),
           f'<path d="M{OX-4},{YT+2} L{OX},{YT-6} L{OX+4},{YT+2}" fill="none" stroke="currentColor" stroke-width="1.4"/>',
           f'<path d="M{XM+2},{OY-4} L{XM+10},{OY} L{XM+2},{OY+4}" fill="none" stroke="currentColor" stroke-width="1.4"/>',
           _t((OX + XM) / 2, OY + 30, xlabel)]
    for i, ln in enumerate(_wrap(ylabel, 11)):
        out.append(_t(OX - 6, 40 + 13 * i, ln, anchor="end"))
    out.append(_t(OX - 6, OY + 13, "O", anchor="end"))
    return out


def _svg(elems, w=340, h=245):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">' + "".join(elems) + "</svg>"


# straight-line demand and supply, sharing the same slope magnitude
D0 = ((92, 45), (272, 185))
S0 = ((92, 185), (272, 45))


def _shift(seg, dx):
    (a, b), (c, d) = seg
    return ((a + dx, b), (c + dx, d))


def _inter(s1, s2):
    (x1, y1), (x2, y2) = s1
    (x3, y3), (x4, y4) = s2
    den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / den
    py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / den
    return px, py


def _curve(seg, lab, both=True):
    (a, b), (c, d) = seg
    out = [_l(a, b, c, d, w=1.8), _t(c + 9, d + 4, lab, anchor="start")]
    if both:
        out.append(_t(a - 4, b + (-4 if b < d else 12), lab, anchor="end"))
    return out


def _eq(p, plab, qlab):
    x, y = p
    return [_l(OX, y, x, y, dash=True, w=1), _l(x, y, x, OY, dash=True, w=1),
            _t(OX - 5, y + 4, plab, anchor="end"), _t(x, OY + 14, qlab)]


def sd_base(xlabel, ylabel, slab="S", dlab="D", plab="Pe", qlab="Qe"):
    """Supply and demand at equilibrium, for 'draw the effect of ...' questions."""
    e = _axes(xlabel, ylabel) + _curve(S0, slab) + _curve(D0, dlab) + _eq(_inter(S0, D0), plab, qlab)
    return _svg(e)


def sd_shift(xlabel, ylabel, curve, direction, slab="S", dlab="D"):
    """Original equilibrium plus one shifted curve (curve 'S' or 'D', direction +1 right / -1 left)."""
    dx = 48 * direction
    S1 = _shift(S0, dx) if curve == "S" else S0
    D1 = _shift(D0, dx) if curve == "D" else D0
    e = _axes(xlabel, ylabel) + _curve(S0, slab) + _curve(D0, dlab) + _eq(_inter(S0, D0), "Pe", "Qe")
    e += _curve(S1 if curve == "S" else D1, (slab if curve == "S" else dlab) + "1")
    e += _eq(_inter(S1, D1), "P1", "Q1")
    return _svg(e)


def sd_price_line(xlabel, ylabel, above):
    """Equilibrium diagram with a horizontal price line above or below equilibrium (for MCQ / labelling)."""
    pe = _inter(S0, D0)
    y = pe[1] - 40 if above else pe[1] + 40
    e = _axes(xlabel, ylabel) + _curve(S0, "S") + _curve(D0, "D") + _eq(pe, "Pe", "Qe")
    e += [_l(OX, y, 290, y, w=1.2), _t(OX - 5, y + 4, "P1", anchor="end")]
    return _svg(e)


def blank_axes(xlabel, ylabel):
    return _svg(_axes(xlabel, ylabel))


def single_curve(xlabel, ylabel, kind, lab):
    """One demand or supply curve: kind in elastic/inelastic/unitary... used for MCQs."""
    segs = {"elastic-d": ((80, 95), (290, 150)), "inelastic-d": ((150, 30), (200, 195)),
            "elastic-s": ((80, 160), (290, 95)), "inelastic-s": ((150, 195), (200, 30)),
            "perfectly-elastic": ((70, 110), (290, 110)), "perfectly-inelastic": ((180, 30), (180, 200))}
    a, b = segs[kind]
    return _svg(_axes(xlabel, ylabel) + [_l(*a, *b, w=1.8), _t(b[0] + 6, b[1] + 4, lab, anchor="start")])


def _bez(p0, p1, p2, t):
    return ((1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0],
            (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1])


PPC = ((OX, 48), (262, 48), (262, OY))


def ppc_base(xgood, ygood, points=None, label="PPC", extra=None):
    """Concave PPC. points: list of (name, where) with where in 'on:t', 'in', 'out'."""
    p0, p1, p2 = PPC
    e = _axes(xgood, ygood)
    e.append(f'<path d="M{p0[0]},{p0[1]} Q{p1[0]},{p1[1]} {p2[0]},{p2[1]}" fill="none" stroke="currentColor" stroke-width="1.8"/>')
    e.append(_t(p2[0] + 4, p2[1] - 8, label, anchor="start"))
    if extra == "out":
        q0, q1, q2 = (OX, 28), (290, 28), (290, OY)
        e.append(f'<path d="M{q0[0]},{q0[1]} Q{q1[0]},{q1[1]} {q2[0]},{q2[1]}" fill="none" stroke="currentColor" stroke-width="1.8"/>')
        e.append(_t(q2[0] + 4, q2[1] - 22, label + "1", anchor="start"))
    for name, where in points or []:
        if where.startswith("on"):
            x, y = _bez(p0, p1, p2, float(where.split(":")[1]))
        elif where == "in":
            x, y = 150, 150
        else:
            x, y = 262, 40
        e.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3" fill="currentColor"/>')
        e.append(_t(x + 7, y - 5, name, anchor="start"))
        if where.startswith("on"):
            e += [_l(OX, y, x, y, dash=True, w=0.9), _l(x, y, x, OY, dash=True, w=0.9)]
    return _svg(e)


CYCLE = ["Boom", "Downturn", "Recession", "Recovery"]


def cycle_base(given):
    """Economic cycle around a rising trend line with four boxes; the stage `given` is printed, others empty."""
    e = _axes("Time", "Real GDP")
    pts = []
    for i in range(0, 241):
        x = OX + 8 + i
        trend = 170 - 0.42 * i
        y = trend - 30 * math.sin((i - 20) / 240 * 2 * math.pi * 1.25)
        pts.append(f"{x:.1f},{y:.1f}")
    e.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="currentColor" stroke-width="1.8"/>')
    e.append(_l(OX + 8, 170, OX + 248, 170 - 0.42 * 240, dash=True, w=1))
    e.append(_t(OX + 252, 170 - 0.42 * 240 + 16, "trend", anchor="start", size=10))

    def at(i):
        trend = 170 - 0.42 * i
        return OX + 8 + i, trend - 30 * math.sin((i - 20) / 240 * 2 * math.pi * 1.25)
    spots = {"Boom": (at(68), -30), "Downturn": (at(116), -26), "Recession": (at(164), 22), "Recovery": (at(206), 26)}
    for st, ((x, y), dy) in spots.items():
        bx, by = x - 30, y + dy - 10
        e.append(f'<rect x="{bx:.1f}" y="{by:.1f}" width="60" height="17" fill="none" stroke="currentColor" stroke-width="1"/>')
        if st == given:
            e.append(_t(x, by + 12.5, st, size=10))
    return _svg(e)


def lrac_base(labelled=False):
    e = _axes("Output", "Average cost")
    e.append(f'<path d="M80,60 Q180,250 285,60" fill="none" stroke="currentColor" stroke-width="1.8"/>')
    e.append(_t(288, 56, "LRAC", anchor="start"))
    if labelled:
        e += [_l(182, 155, 182, OY, dash=True, w=1), _t(182, OY + 14, "Q1")]
    return _svg(e, w=350)


def bar_table_svg():
    return None
