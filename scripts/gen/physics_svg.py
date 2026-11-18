"""SVG drawing helpers for the physics bank (circuits, rays, waves, graphs, fields, apparatus).

All drawings use currentColor strokes on a transparent background, a viewBox and the
generic sans-serif font family only.
"""
import math


def f(x):
    s = f"{x:.1f}"
    return s[:-2] if s.endswith(".0") else s


def svg(w, h, body, fs=12):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {f(w)} {f(h)}" font-family="sans-serif" '
            f'font-size="{fs}" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" '
            f'stroke-linejoin="round">{body}</svg>')


def line(x1, y1, x2, y2, extra=""):
    return f'<line x1="{f(x1)}" y1="{f(y1)}" x2="{f(x2)}" y2="{f(y2)}"{extra}/>'


def dashed(x1, y1, x2, y2):
    return line(x1, y1, x2, y2, ' stroke-dasharray="5,4" stroke-width="1"')


def poly(pts, close=False, extra=""):
    p = " ".join(f"{f(x)},{f(y)}" for x, y in pts)
    tag = "polygon" if close else "polyline"
    return f'<{tag} points="{p}"{extra}/>'


def circle(x, y, r, filled=False, extra=""):
    fill = ' fill="currentColor"' if filled else ""
    return f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r)}"{fill}{extra}/>'


def rect(x, y, w, h, extra=""):
    return f'<rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}"{extra}/>'


def text(x, y, s, anchor="middle", size=None, italic=False, bold=False):
    a = f' font-size="{size}"' if size else ""
    if italic:
        a += ' font-style="italic"'
    if bold:
        a += ' font-weight="bold"'
    s = str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return (f'<text x="{f(x)}" y="{f(y)}" text-anchor="{anchor}" dominant-baseline="middle" '
            f'fill="currentColor" stroke="none"{a}>{s}</text>')


def arrowhead(x1, y1, x2, y2, size=7):
    """Filled arrowhead at (x2, y2) pointing from (x1, y1)."""
    ang = math.atan2(y2 - y1, x2 - x1)
    a1, a2 = ang + math.radians(155), ang - math.radians(155)
    p = [(x2, y2), (x2 + size * math.cos(a1), y2 + size * math.sin(a1)), (x2 + size * math.cos(a2), y2 + size * math.sin(a2))]
    return poly(p, True, ' fill="currentColor" stroke-width="1"')


def arrow(x1, y1, x2, y2, size=7, width=1.5):
    return line(x1, y1, x2, y2, f' stroke-width="{width}"') + arrowhead(x1, y1, x2, y2, size)


def mid_arrow(x1, y1, x2, y2, size=6):
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    return line(x1, y1, x2, y2) + arrowhead(x1, y1, mx + (x2 - x1) * 0.03, my + (y2 - y1) * 0.03, size)


def dbl_arrow(x1, y1, x2, y2, size=6):
    return line(x1, y1, x2, y2, ' stroke-width="1"') + arrowhead(x1, y1, x2, y2, size) + arrowhead(x2, y2, x1, y1, size)


def g(body, tx=0, ty=0, rot=0):
    t = f"translate({f(tx)},{f(ty)})"
    if rot:
        t += f" rotate({rot})"
    return f'<g transform="{t}">{body}</g>'


# ------------------------------------------------------------------ circuit symbols
# Each symbol is drawn horizontally, centred on the origin, with terminals at x = -20 and x = +20.

def _sym(kind):
    L = 20
    if kind == "cell":
        return line(-L, 0, -3, 0) + line(-3, -13, -3, 13) + line(3, -7, 3, 7, ' stroke-width="3"') + line(3, 0, L, 0)
    if kind == "battery":
        return (line(-L, 0, -9, 0) + line(-9, -13, -9, 13) + line(-4, -7, -4, 7, ' stroke-width="3"') +
                dashed(-3, 0, 3, 0) + line(4, -13, 4, 13) + line(9, -7, 9, 7, ' stroke-width="3"') + line(9, 0, L, 0))
    if kind == "dc":  # power supply drawn as cell with terminals
        return _sym("cell")
    if kind == "ac":
        return (line(-L, 0, -10, 0) + circle(-10, 0, 1.8, True) + circle(10, 0, 1.8, True) + line(10, 0, L, 0) +
                '<path d="M -7 0 q 3.5 -7 7 0 t 7 0"/>')
    if kind == "resistor" or kind == "heater":
        return line(-L, 0, -13, 0) + rect(-13, -6, 26, 12) + line(13, 0, L, 0)
    if kind == "varres":
        return _sym("resistor") + arrow(-12, 11, 12, -11, 5, 1.2)
    if kind == "lamp":
        d = 10 / math.sqrt(2)
        return line(-L, 0, -10, 0) + circle(0, 0, 10) + line(-d, -d, d, d) + line(-d, d, d, -d) + line(10, 0, L, 0)
    if kind in ("ammeter", "voltmeter", "motor", "generator"):
        return line(-L, 0, -10, 0) + circle(0, 0, 10) + line(10, 0, L, 0)
    if kind == "switch_open":
        return line(-L, 0, -9, 0) + circle(-9, 0, 2) + line(-8, -1, 9, -10) + circle(9, 0, 2) + line(9, 0, L, 0)
    if kind == "switch_closed":
        return line(-L, 0, -9, 0) + circle(-9, 0, 2) + line(-8, 0, 9, 0) + circle(9, 0, 2) + line(9, 0, L, 0)
    if kind == "fuse":
        return line(-L, 0, -12, 0) + rect(-12, -4, 24, 8) + line(-12, 0, 12, 0, ' stroke-width="1"') + line(12, 0, L, 0)
    if kind in ("diode", "led"):
        s = line(-L, 0, -6, 0) + poly([(-6, -7), (-6, 7), (6, 0)], True) + line(6, -7, 6, 7) + line(6, 0, L, 0) + line(-6, 0, 6, 0)
        if kind == "led":
            s += arrow(0, -9, 7, -17, 4, 1) + arrow(5, -7, 12, -15, 4, 1)
        return s
    if kind == "ldr":
        return _sym("resistor") + circle(0, 0, 15, extra=' stroke-width="1"') + arrow(-18, -20, -9, -11, 4, 1) + arrow(-11, -24, -2, -15, 4, 1)
    if kind == "thermistor":
        return _sym("resistor") + poly([(-16, 11), (-11, 11), (12, -10)], extra=' stroke-width="1.2"')
    raise ValueError(kind)


SYM_LETTER = {"ammeter": "A", "voltmeter": "V", "motor": "M", "generator": "G"}


def symbol(kind, x, y, vertical=False, label=None, label_side=1):
    body = g(_sym(kind), x, y, 90 if vertical else 0)
    if kind in SYM_LETTER:
        body += text(x, y + 0.5, SYM_LETTER[kind], size=11)
    if label:
        if vertical:
            body += text(x + 24 * label_side, y, label, anchor="start" if label_side > 0 else "end", size=11)
        else:
            body += text(x, y - 20 * label_side, label, size=11)
    return body


def dot(x, y):
    return circle(x, y, 2.6, True)


def ladder(top, rungs, width=300, rung_gap=70, voltmeters=(), labels=None, top_y=30):
    """Circuit drawn as a ladder.

    top    : list of component kinds on the top wire (usually the supply)
    rungs  : list of lists of component kinds; one rung = series circuit, several = parallel branches
    voltmeters: list of (rung_index, item_index) — a voltmeter is drawn across that component
    labels : dict {(row, idx): text} where row -1 = top wire
    Returns (svg_body, height).
    """
    labels = labels or {}
    xl, xr = 30, width - 30
    body = ""
    ys = [top_y + rung_gap * (i + 1) for i in range(len(rungs))]
    if len(rungs) == 1 and top_y + rung_gap > top_y:
        pass

    def place(items, y, row):
        out = ""
        n = len(items)
        xs = [xl + (xr - xl) * (i + 1) / (n + 1) for i in range(n)]
        prev = xl
        for i, (kind, x) in enumerate(zip(items, xs)):
            out += line(prev, y, x - 20, y)
            out += symbol(kind, x, y, label=labels.get((row, i)))
            prev = x + 20
        out += line(prev, y, xr, y)
        return out, xs

    b, _ = place(top, top_y, -1)
    body += b
    last = ys[-1]
    body += line(xl, top_y, xl, last) + line(xr, top_y, xr, last)
    pos = {}
    for r, items in enumerate(rungs):
        b, xs = place(items, ys[r], r)
        body += b
        for i, x in enumerate(xs):
            pos[(r, i)] = (x, ys[r])
        if len(rungs) > 1 and r < len(rungs) - 1:
            body += dot(xl, ys[r]) + dot(xr, ys[r])
    for (r, i) in voltmeters:
        x, y = pos[(r, i)]
        vy = y + 34 if r == len(rungs) - 1 else y - 30
        body += dot(x - 26, y) + dot(x + 26, y)
        body += line(x - 26, y, x - 26, vy) + line(x + 26, y, x + 26, vy)
        body += line(x - 26, vy, x - 10, vy) + line(x + 10, vy, x + 26, vy) + symbol("voltmeter", x, vy)[0:0]
        body += g(_sym("voltmeter"), x, vy) + text(x, vy + 0.5, "V", size=11)
    h = last + (55 if any(r == len(rungs) - 1 for r, _ in voltmeters) else 25)
    return body, h


def circuit(top, rungs, width=300, **kw):
    body, h = ladder(top, rungs, width=width, **kw)
    return svg(width, h, body)


# ------------------------------------------------------------------ graphs

def nice_ticks(lo, hi, n=5):
    span = hi - lo
    raw = span / n
    mag = 10 ** math.floor(math.log10(raw))
    for m in (1, 2, 2.5, 5, 10):
        if raw <= m * mag:
            step = m * mag
            break
    t0 = math.ceil(lo / step - 1e-9) * step
    out = []
    t = t0
    while t <= hi + 1e-9:
        out.append(round(t, 10))
        t += step
    return out, step


def tick_label(v):
    if abs(v - round(v)) < 1e-9:
        return str(int(round(v)))
    s = f"{v:.3f}".rstrip("0").rstrip(".")
    return s


def graph(xmax, ymax, xlabel, ylabel, series=(), curves=(), xmin=0, ymin=0, w=360, h=260, grid=True,
          xticks=None, yticks=None, marks=(), hlines=(), vlines=(), minor=5):
    """Plot axes with a fine grid.

    series: list of dicts {pts:[(x,y)], marker:'x'|'o'|None, join:bool}
    curves: list of lists of (x,y) drawn as smooth polylines
    marks : list of (x, y, label) annotations
    """
    L, R, T, B = 55, 15, 15, 45
    pw, ph = w - L - R, h - T - B
    X = lambda x: L + (x - xmin) / (xmax - xmin) * pw  # noqa: E731
    Y = lambda y: T + ph - (y - ymin) / (ymax - ymin) * ph  # noqa: E731
    xt, xs = (xticks, None) if xticks else nice_ticks(xmin, xmax)
    yt, ys = (yticks, None) if yticks else nice_ticks(ymin, ymax)
    if xticks:
        xs = xticks[1] - xticks[0]
    if yticks:
        ys = yticks[1] - yticks[0]
    body = ""
    if grid:
        for i in range(int(round((xmax - xmin) / xs * minor)) + 1):
            x = xmin + i * xs / minor
            if x > xmax + 1e-9:
                break
            wdt = "0.8" if i % minor == 0 else "0.3"
            body += line(X(x), T, X(x), T + ph, f' stroke-width="{wdt}"')
        for i in range(int(round((ymax - ymin) / ys * minor)) + 1):
            y = ymin + i * ys / minor
            if y > ymax + 1e-9:
                break
            wdt = "0.8" if i % minor == 0 else "0.3"
            body += line(L, Y(y), L + pw, Y(y), f' stroke-width="{wdt}"')
    body += line(L, T + ph, L + pw, T + ph) + line(L, T, L, T + ph)
    for t in xt:
        body += line(X(t), T + ph, X(t), T + ph + 4) + text(X(t), T + ph + 13, tick_label(t), size=10)
    for t in yt:
        body += line(L - 4, Y(t), L, Y(t)) + text(L - 7, Y(t), tick_label(t), anchor="end", size=10)
    body += text(L + pw / 2, h - 10, xlabel, size=11)
    body += (f'<text x="14" y="{f(T + ph / 2)}" text-anchor="middle" dominant-baseline="middle" fill="currentColor" '
             f'stroke="none" font-size="11" transform="rotate(-90 14 {f(T + ph / 2)})">{ylabel}</text>')
    for c in curves:
        body += poly([(X(x), Y(y)) for x, y in c], extra=' stroke-width="1.6"')
    for s in series:
        pts = s["pts"]
        if s.get("join"):
            body += poly([(X(x), Y(y)) for x, y in pts], extra=' stroke-width="1.6"')
        mk = s.get("marker", "x")
        for x, y in pts:
            if mk == "x":
                body += line(X(x) - 3.5, Y(y) - 3.5, X(x) + 3.5, Y(y) + 3.5, ' stroke-width="1.2"') + \
                    line(X(x) - 3.5, Y(y) + 3.5, X(x) + 3.5, Y(y) - 3.5, ' stroke-width="1.2"')
            elif mk == "o":
                body += circle(X(x), Y(y), 2.5, True)
    for y in hlines:
        body += dashed(L, Y(y), L + pw, Y(y))
    for x in vlines:
        body += dashed(X(x), T, X(x), T + ph)
    for x, y, lab in marks:
        body += circle(X(x), Y(y), 2.5, True) + text(X(x) + 6, Y(y) - 9, lab, anchor="start", size=11)
    return svg(w, h, body)


# ------------------------------------------------------------------ waves

def transverse_wave(cycles=2.5, amp=40, wl=120, label_amp=False, label_wl=False, w=None, axis=True, labels=None):
    w = w or int(cycles * wl + 60)
    h = 2 * amp + 60
    y0 = h / 2
    pts = [(30 + x, y0 - amp * math.sin(2 * math.pi * x / wl)) for x in range(0, int(cycles * wl) + 1, 2)]
    body = poly(pts, extra=' stroke-width="1.8"')
    if axis:
        body += dashed(20, y0, w - 10, y0)
    if label_amp:
        x = 30 + wl * 0.25
        body += dbl_arrow(x, y0, x, y0 - amp) + text(x + 8, y0 - amp / 2, label_amp, anchor="start", size=11)
    if label_wl:
        x1 = 30 + wl * 0.25
        yy = y0 - amp - 12
        body += dbl_arrow(x1, yy, x1 + wl, yy) + text(x1 + wl / 2, yy - 9, label_wl, size=11)
    for (x, y, s) in (labels or []):
        body += text(x, y, s, size=11)
    return svg(w, h, body)


def longitudinal_wave(n=60, w=420, h=70, comp=4, label=True):
    body = ""
    k = 2 * math.pi * comp / w
    xs = []
    for i in range(n):
        x0 = 10 + i * (w - 20) / n
        xs.append(x0 - 6 * math.sin(k * x0))
    for x in xs:
        body += line(x, 15, x, h - 25, ' stroke-width="1"')
    if label:
        # compression where lines are closest: sin(kx) phase where derivative of displacement max
        c = 10 + (w - 20) / comp * 0.0 + (w - 20) / comp * 0.0
        body += text(w * 0.5, h - 10, "direction of energy transfer →", size=11)
    return svg(w, h, body)


def oscilloscope(cycles, amp_div, divs_x=10, divs_y=8, cell=30, phase=0.0):
    w, h = divs_x * cell + 20, divs_y * cell + 20
    body = rect(10, 10, divs_x * cell, divs_y * cell)
    for i in range(1, divs_x):
        body += line(10 + i * cell, 10, 10 + i * cell, 10 + divs_y * cell, ' stroke-width="0.4"')
    for j in range(1, divs_y):
        body += line(10, 10 + j * cell, 10 + divs_x * cell, 10 + j * cell, ' stroke-width="0.4"')
    y0 = 10 + divs_y * cell / 2
    W = divs_x * cell
    pts = [(10 + x, y0 - amp_div * cell * math.sin(2 * math.pi * (cycles * x / W) + phase)) for x in range(0, W + 1, 2)]
    body += poly(pts, extra=' stroke-width="1.8"')
    return svg(w, h, body)


# ------------------------------------------------------------------ rays and optics

def _ray(x1, y1, x2, y2, arrow_mid=True):
    return mid_arrow(x1, y1, x2, y2) if arrow_mid else line(x1, y1, x2, y2)


def block_refraction(i_deg, n, show_refracted=True, show_emergent=True, labels=True, w=360, h=300):
    """Ray entering the top face of a rectangular glass block."""
    bx, by, bw, bh = 90, 110, 200, 110
    xi, yi = 160, by
    r = math.degrees(math.asin(math.sin(math.radians(i_deg)) / n))
    L = 95
    xa = xi - L * math.sin(math.radians(i_deg))
    ya = yi - L * math.cos(math.radians(i_deg))
    body = rect(bx, by, bw, bh) + dashed(xi, by - 70, xi, by + bh * 0.55)
    body += _ray(xa, ya, xi, yi)
    if labels:
        body += text(bx + bw - 30, by + bh - 15, "glass", size=11) + text(bx + bw - 30, by - 15, "air", size=11)
        body += text(xi + 8, by - 62, "normal", anchor="start", size=10)
    xo = xi + bh * math.tan(math.radians(r))
    if show_refracted:
        body += _ray(xi, yi, xo, by + bh)
        if show_emergent:
            body += dashed(xo, by + bh - 30, xo, by + bh + 55)
            body += _ray(xo, by + bh, xo + 70 * math.sin(math.radians(i_deg)), by + bh + 70 * math.cos(math.radians(i_deg)))
    return svg(w, h, body), r


def semicircle_block(theta, n, mode="incident", w=360, h=260):
    """Ray entering the curved side of a semicircular block towards the centre, meeting the flat face at theta."""
    cx, cy, R = 180, 150, 110
    body = f'<path d="M {cx - R} {cy} A {R} {R} 0 0 0 {cx + R} {cy} Z"/>'  # curved part below the flat face
    body += dashed(cx, cy - 90, cx, cy + R + 10)
    # incoming ray from below-left to centre
    a = math.radians(theta)
    sx, sy = cx - (R + 40) * math.sin(a), cy + (R + 40) * math.cos(a)
    body += _ray(sx, sy, cx, cy)
    body += text(cx - R + 25, cy + 20, "glass", size=11) + text(cx - R + 10, cy - 20, "air", size=11)
    c = math.degrees(math.asin(1 / n))
    if mode == "full":
        if theta < c:
            r = math.degrees(math.asin(n * math.sin(a)))
            ra = math.radians(r)
            body += _ray(cx, cy, cx + 100 * math.sin(ra), cy - 100 * math.cos(ra))
        else:
            body += _ray(cx, cy, cx + (R) * math.sin(a), cy + (R) * math.cos(a))
    return svg(w, h, body), c


def plane_mirror(i_deg, show_reflected=False, w=320, h=220):
    mx1, mx2, my = 40, 280, 180
    px = 160
    body = line(mx1, my, mx2, my, ' stroke-width="2.5"')
    for x in range(mx1, mx2, 12):
        body += line(x, my, x + 8, my + 8, ' stroke-width="1"')
    body += dashed(px, my, px, 40)
    a = math.radians(i_deg)
    L = 140
    body += _ray(px - L * math.sin(a), my - L * math.cos(a), px, my)
    if show_reflected:
        body += _ray(px, my, px + L * math.sin(a), my - L * math.cos(a))
    body += text(px + 6, 48, "normal", anchor="start", size=10) + text(mx2 - 25, my + 22, "mirror", size=11)
    return svg(w, h, body)


def prism(w=340, h=260, ray=True):
    A, B, C = (170, 30), (60, 220), (280, 220)
    body = poly([A, B, C], True)
    if ray:
        body += _ray(10, 175, 112, 130)
    return svg(w, h, body)


def optical_fibre(w=420, h=120):
    body = rect(20, 30, 380, 60) + rect(10, 20, 400, 80, ' stroke-width="0.8" stroke-dasharray="3,3"')
    pts = [(20, 75)]
    x, y, up = 20, 75, True
    while x < 395:
        x += 45
        y = 32 if up else 88
        pts.append((min(x, 400), y))
        up = not up
    body += poly(pts, extra=' stroke-width="1.4"')
    body += text(60, 110, "cladding", size=10) + text(210, 60, "core", size=10)
    return svg(w, h, body)


# ------------------------------------------------------------------ forces, objects

def force_diagram(obj="box", forces=(), w=300, h=260, label_obj=None):
    """forces: list of (direction, length, label) with direction in up/down/left/right."""
    cx, cy = w / 2, h / 2
    body = ""
    if obj == "box":
        body += rect(cx - 35, cy - 25, 70, 50)
    elif obj == "ball":
        body += circle(cx, cy, 28)
    elif obj == "car":
        body += poly([(cx - 60, cy + 15), (cx - 60, cy - 5), (cx - 30, cy - 8), (cx - 15, cy - 28), (cx + 30, cy - 28),
                      (cx + 45, cy - 8), (cx + 60, cy - 5), (cx + 60, cy + 15)], True)
        body += circle(cx - 35, cy + 17, 9) + circle(cx + 35, cy + 17, 9)
    elif obj == "parachutist":
        body += f'<path d="M {cx - 50} {cy - 40} Q {cx} {cy - 95} {cx + 50} {cy - 40} Z"/>'
        body += line(cx - 50, cy - 40, cx, cy) + line(cx + 50, cy - 40, cx, cy) + circle(cx, cy + 5, 6) + line(cx, cy + 11, cx, cy + 30)
    if label_obj:
        body += text(cx, cy, label_obj, size=11)
    off = {"up": (0, -1), "down": (0, 1), "left": (-1, 0), "right": (1, 0)}
    start = {"up": (cx, cy - 30), "down": (cx, cy + 30), "left": (cx - 40, cy), "right": (cx + 40, cy)}
    if obj == "car":
        start = {"up": (cx, cy - 30), "down": (cx, cy + 28), "left": (cx - 62, cy), "right": (cx + 62, cy)}
    if obj == "parachutist":
        start = {"up": (cx, cy - 70), "down": (cx, cy + 32), "left": (cx - 52, cy), "right": (cx + 52, cy)}
    for d, Ln, lab in forces:
        dx, dy = off[d]
        x0, y0 = start[d]
        x1, y1 = x0 + dx * Ln, y0 + dy * Ln
        body += arrow(x0, y0, x1, y1, 8, 2)
        if lab:
            tx, ty = x1 + dx * 14 + (10 if d in ("up", "down") else 0), y1 + dy * 12 + (0 if d in ("up", "down") else -12)
            body += text(tx, ty, lab, anchor="start" if d in ("up", "down") else "middle", size=11)
    return svg(w, h, body)


def beam(pivot_x, loads, length=10.0, w=420, h=170, support="pivot", labels_m=True, unit="m"):
    """Uniform beam (metre rule) on a pivot. loads: list of (pos, label, up_or_down)."""
    L, R = 30, w - 30
    X = lambda p: L + (R - L) * p / length  # noqa: E731
    y = 80
    body = rect(L, y - 6, R - L, 12)
    if support == "pivot":
        px = X(pivot_x)
        body += poly([(px, y + 6), (px - 14, y + 34), (px + 14, y + 34)], True)
        body += line(px - 26, y + 34, px + 26, y + 34, ' stroke-width="2"')
    elif support == "ends":
        for px in (L + 6, R - 6):
            body += poly([(px, y + 6), (px - 12, y + 30), (px + 12, y + 30)], True)
    for pos, lab, d in loads:
        x = X(pos)
        if d == "down":
            body += arrow(x, y + 6, x, y + 55, 8, 2) + text(x, y + 66, lab, size=11)
        else:
            body += arrow(x, y - 6, x, y - 55, 8, 2) + text(x, y - 64, lab, size=11)
    if labels_m:
        pass
    return svg(w, h, body)


def spring_apparatus(w=260, h=300, masses=2):
    body = line(30, 20, 150, 20, ' stroke-width="3"') + line(40, 20, 40, 280, ' stroke-width="2"')  # clamp stand
    body += rect(25, 275, 120, 10)
    # ruler
    body += rect(175, 30, 22, 240)
    for i in range(0, 25):
        y = 35 + i * 9.5
        body += line(175, y, 175 + (10 if i % 5 == 0 else 6), y, ' stroke-width="0.8"')
    # spring
    pts = [(130, 20), (130, 32)]
    for i in range(12):
        pts.append((120 if i % 2 == 0 else 140, 38 + i * 7))
    pts += [(130, 124), (130, 136)]
    body += poly(pts, extra=' stroke-width="1.3"')
    y = 136
    body += line(130, y, 130, y + 8)
    for k in range(masses):
        body += rect(112, y + 8 + k * 18, 36, 16)
    body += line(148, y + 4, 175, y + 4, ' stroke-dasharray="2,2" stroke-width="0.8"')
    body += text(186, 285, "ruler", size=10) + text(80, 140, "spring", anchor="end", size=10)
    body += text(80, y + 20, "masses", anchor="end", size=10)
    return svg(w, h, body)


def ramp_trolley(w=420, h=200, gates=True):
    body = poly([(20, 170), (400, 170), (20, 60)], True)
    body += rect(60, 65, 60, 22, ' transform="rotate(16.1 90 76)"')
    if gates:
        for x in (170, 300):
            yy = 60 + (x - 20) * (110 / 380) - 10
            body += rect(x - 4, yy - 40, 8, 40)
        body += text(235, 40, "light gates", size=11)
    body += text(80, 40, "trolley", size=11) + text(330, 188, "ramp", size=11)
    return svg(w, h, body)


def magnet(x, y, w=120, h=34, left="N", right="S"):
    return (rect(x, y, w, h) + line(x + w / 2, y, x + w / 2, y + h) + text(x + w / 4, y + h / 2, left, bold=True) +
            text(x + 3 * w / 4, y + h / 2, right, bold=True))


def bar_magnet_field(w=420, h=260, lines_drawn=True):
    cx, cy = w / 2, h / 2
    body = magnet(cx - 60, cy - 17)
    if lines_drawn:
        for k in (1, 2, 3):
            ry = 28 + 30 * k
            rx = 60 + 25 * k
            for s in (-1, 1):
                d = f"M {f(cx - 60)} {f(cy + s * 6)} C {f(cx - 60 - rx * 0.7)} {f(cy + s * ry * 1.2)}, {f(cx + 60 + rx * 0.7)} {f(cy + s * ry * 1.2)}, {f(cx + 60)} {f(cy + s * 6)}"
                body += f'<path d="{d}" stroke-width="1"/>'
                body += arrowhead(cx - 2, cy + s * ry * 0.9, cx + 2, cy + s * ry * 0.9, 6)
        body += line(cx - 60, cy, cx - 150, cy, ' stroke-width="1"') + arrowhead(cx - 60, cy, cx - 120, cy, 6)
        body += line(cx + 60, cy, cx + 150, cy, ' stroke-width="1"') + arrowhead(cx + 150, cy, cx + 90, cy, 6)
    return svg(w, h, body)


def two_magnets(w=420, h=160, facing=("S", "N"), field=False):
    opp = {"N": "S", "S": "N"}
    body = magnet(20, 60, left=opp.get(facing[0], " "), right=facing[0]) + magnet(280, 60, left=facing[1], right=opp.get(facing[1], " "))
    if field:
        for k in range(5):
            y = 66 + k * 5.5
            body += arrow(140, y, 280, y, 5, 1)
    return svg(w, h, body)


def wire_field_top(current_out=True, rings=3, w=240, h=240):
    cx, cy = w / 2, h / 2
    body = circle(cx, cy, 9)
    if current_out:
        body += circle(cx, cy, 2.5, True)
    else:
        body += line(cx - 5, cy - 5, cx + 5, cy + 5) + line(cx - 5, cy + 5, cx + 5, cy - 5)
    for k in range(1, rings + 1):
        r = 22 + 26 * k
        body += circle(cx, cy, r, extra=' stroke-width="1"')
        if current_out:  # anticlockwise seen from above
            body += arrowhead(cx + r, cy + 4, cx + r, cy - 4, 6)
        else:
            body += arrowhead(cx + r, cy - 4, cx + r, cy + 4, 6)
    return svg(w, h, body)


def magnet_and_bar(pole="N", side="right", w=420, h=140):
    """Bar magnet with one pole facing an unmagnetised bar."""
    opp = {"N": "S", "S": "N"}[pole]
    if side == "right":
        body = magnet(30, 55, left=opp, right=pole) + rect(220, 62, 150, 20) + text(295, 100, "bar", size=10)
    else:
        body = rect(30, 62, 150, 20) + text(105, 100, "bar", size=10) + magnet(260, 55, left=pole, right=opp)
    return svg(w, h, body)


def solenoid(w=400, h=180, turns=8, core=False, label=True):
    x0, x1, y0, y1 = 90, 310, 60, 120
    body = ""
    if core:
        body += rect(70, 75, 260, 30, ' stroke-width="1"')
    step = (x1 - x0) / turns
    for i in range(turns):
        x = x0 + i * step
        body += f'<path d="M {f(x)} {y1} Q {f(x + step * 0.25)} {y0 - 6} {f(x + step * 0.5)} {y0}" stroke-width="1.4"/>'
        body += f'<path d="M {f(x + step * 0.5)} {y0} Q {f(x + step * 0.75)} {y0 + 6} {f(x + step)} {y1}" stroke-width="0.8" stroke-dasharray="3,2"/>'
    body += line(x0, y1, x0, 160) + line(x1, y1, x1, 160) + line(x0, 160, 170, 160) + line(230, 160, x1, 160)
    body += symbol("cell", 200, 160)
    if core and label:
        body += text(360, 90, "iron core", size=10)
    return svg(w, h, body)


def motor_diagram(w=360, h=220):
    body = rect(20, 50, 50, 120) + text(45, 110, "N", bold=True) + rect(290, 50, 50, 120) + text(315, 110, "S", bold=True)
    body += poly([(110, 70), (250, 70), (250, 150), (110, 150), (110, 70)])
    body += line(170, 150, 170, 185) + line(190, 150, 190, 185)
    body += f'<path d="M 162 185 A 18 10 0 0 0 198 185" stroke-width="2"/>'
    body += rect(140, 190, 14, 18) + rect(206, 190, 14, 18)
    body += text(180, 30, "coil", size=11) + text(180, 215, "split-ring commutator and brushes", size=10)
    body += text(98, 68, "A", size=11) + text(262, 68, "B", size=11) + text(262, 156, "C", size=11) + text(98, 156, "D", size=11)
    return svg(w, h, body)


def transformer(np_, ns, w=380, h=200, labels=True):
    body = rect(110, 30, 160, 140) + rect(140, 60, 100, 80)
    for i in range(6):
        y = 45 + i * 20
        body += f'<path d="M 100 {y} Q 125 {y + 6} 150 {y + 4}" stroke-width="1.3"/>'
        body += f'<path d="M 230 {y + 4} Q 255 {y + 6} 280 {y}" stroke-width="1.3"/>'
    body += line(100, 45, 50, 45) + line(100, 145, 50, 145) + line(280, 45, 330, 45) + line(280, 145, 330, 145)
    if labels:
        body += text(60, 95, "primary", size=10) + text(60, 110, f"{np_} turns", size=10)
        body += text(320, 95, "secondary", size=10) + text(320, 110, f"{ns} turns", size=10)
        body += text(190, 20, "iron core", size=10)
    return svg(w, h, body)


# ------------------------------------------------------------------ radioactivity and astrophysics

def gm_absorber(w=420, h=150, absorber="absorber"):
    body = rect(20, 60, 40, 30) + text(40, 105, "source", size=10)
    body += rect(160, 40, 10, 70) + text(165, 125, absorber, size=10)
    body += rect(260, 62, 70, 26) + line(330, 75, 360, 75) + rect(360, 55, 50, 40) + text(385, 75, "counter", size=9)
    body += text(295, 105, "GM tube", size=10)
    body += arrow(62, 75, 150, 75, 6, 1)
    return svg(w, h, body)


def nz_chart(points, zr, nr, w=320, h=300, arrows=()):
    """Nuclear decay chart: N (neutron number) against Z (proton number)."""
    zmin, zmax = zr
    nmin, nmax = nr
    L, B, T, R = 50, 40, 15, 15
    pw, ph = w - L - R, h - B - T
    X = lambda z: L + (z - zmin + 0.5) / (zmax - zmin + 1) * pw  # noqa: E731
    Y = lambda n: T + ph - (n - nmin + 0.5) / (nmax - nmin + 1) * ph  # noqa: E731
    body = line(L, T, L, T + ph) + line(L, T + ph, L + pw, T + ph)
    for z in range(zmin, zmax + 1):
        body += line(X(z), T + ph, X(z), T + ph + 4) + text(X(z), T + ph + 13, str(z), size=10)
        body += line(X(z), T, X(z), T + ph, ' stroke-width="0.3"')
    for n in range(nmin, nmax + 1):
        body += line(L - 4, Y(n), L, Y(n)) + text(L - 7, Y(n), str(n), anchor="end", size=10)
        body += line(L, Y(n), L + pw, Y(n), ' stroke-width="0.3"')
    body += text(L + pw / 2, h - 8, "proton number Z", size=11)
    body += (f'<text x="12" y="{f(T + ph / 2)}" text-anchor="middle" dominant-baseline="middle" fill="currentColor" '
             f'stroke="none" font-size="11" transform="rotate(-90 12 {f(T + ph / 2)})">neutron number N</text>')
    for z, n, lab in points:
        body += circle(X(z), Y(n), 4, True) + text(X(z) + 7, Y(n) - 9, lab, anchor="start", size=10)
    for (z1, n1), (z2, n2) in arrows:
        body += arrow(X(z1), Y(n1), X(z2), Y(n2), 7, 1.4)
    return svg(w, h, body)


def hr_axes(w=380, h=300, regions=True, labels=None):
    L, B = 60, 45
    body = line(L, 15, L, h - B) + line(L, h - B, w - 15, h - B)
    body += text((L + w) / 2, h - 12, "surface temperature (hot ← → cool)", size=11)
    body += (f'<text x="16" y="{(h - B) / 2}" text-anchor="middle" dominant-baseline="middle" fill="currentColor" '
             f'stroke="none" font-size="11" transform="rotate(-90 16 {(h - B) / 2})">absolute magnitude (bright at top)</text>')
    if regions:
        body += f'<path d="M {L + 20} 40 Q {L + 140} 120 {w - 40} {h - B - 25}" stroke-width="12" stroke-opacity="0.35"/>'
        body += f'<ellipse cx="{w - 80}" cy="80" rx="45" ry="22" stroke-width="1"/>'
        body += f'<ellipse cx="{L + 70}" cy="{h - B - 30}" rx="35" ry="14" stroke-width="1"/>'
    for (x, y, s) in labels or []:
        body += text(x, y, s, size=11)
    return svg(w, h, body)


def sankey(inp, outs, w=380, h=220):
    """Simple Sankey diagram: inp = (label, value); outs = [(label, value)], first output continues straight."""
    tot = inp[1]
    scale = 110 / tot
    y0 = 40
    hw = tot * scale
    body = poly([(20, y0), (200, y0), (200, y0 + hw), (20, y0 + hw)])
    body += text(30, y0 - 12, f"{inp[0]} {inp[1]} J", anchor="start", size=11)
    y = y0
    first = True
    for lab, val in outs:
        t = val * scale
        if first:
            body += poly([(200, y), (330, y)]) + poly([(200, y + t), (330, y + t)]) + poly([(330, y - 5), (350, y + t / 2), (330, y + t + 5)])
            body += text(345, y - 14, f"{lab}", anchor="end", size=11)
            first = False
        else:
            x = 200 - (y - y0) * 0.0
            body += f'<path d="M 200 {f(y + t)} Q {f(200 + 40)} {f(y + t)} {f(200 + 40 + t)} {f(y + t + 60)}" />'
            body += f'<path d="M 200 {f(y)} Q {f(200 + 40 + t)} {f(y)} {f(200 + 40 + 2 * t)} {f(y + 60)}" />'
            body += text(240 + t, y + t + 78, lab, size=11)
        y += t
    return svg(w, h, body)


def orbit(w=320, h=220, ecc=0.0, body_label="Sun", obj="planet"):
    cx, cy = w / 2, h / 2
    a = 120
    b = a * math.sqrt(1 - ecc ** 2)
    c = a * ecc
    s = f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(a)}" ry="{f(b)}" stroke-width="1.2"/>'
    s += circle(cx - c, cy, 12, True) + text(cx - c, cy + 24, body_label, size=11)
    s += circle(cx + a, cy, 5, True) + text(cx + a - 6, cy - 14, obj, size=11)
    return svg(w, h, s)


def table_apparatus_heater(w=360, h=240):
    """Metal block with immersion heater and thermometer, joulemeter."""
    body = rect(110, 110, 120, 100) + text(170, 225, "metal block", size=10)
    body += rect(140, 60, 14, 110) + text(120, 50, "heater", size=10)
    body += line(200, 40, 200, 160) + circle(200, 165, 5) + text(220, 40, "thermometer", anchor="start", size=10)
    body += line(147, 60, 147, 30) + line(147, 30, 40, 30) + rect(10, 30, 50, 34) + text(35, 47, "joulemeter", size=8)
    body += rect(100, 100, 140, 120, ' stroke-dasharray="4,3" stroke-width="1"') + text(300, 115, "insulation", size=10)
    return svg(w, h, body)


def ldr_graph_axes(*a, **k):
    return graph(*a, **k)
