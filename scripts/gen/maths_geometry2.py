"""Geometry templates, part 2: mensuration, volume and surface area, similarity,
vectors and transformations.  Spec sections 4.9-4.11 and 5."""
import math
from fractions import Fraction as F

import sympy as sp

from maths_util import (tpl, P, R, Q, sf, dp, num, ftex, name, fig, table, polygon_fig, Frame, svg, PL, L, T, DOT,
                        ARC, ARROW, C, grid_fig, cone_fig, sphere_fig, sector_fig, angle_mark, right_mark, NOT_ACC, big)
from maths_geometry import LET, tick, par_arrow, DEG

PI = math.pi


def pi_tex(c):
    """c*pi with c a Fraction."""
    c = F(c)
    if c == 1:
        return "\\pi"
    if c.denominator == 1:
        return f"{c.numerator}\\pi"
    return f"\\frac{{{c.numerator}\\pi}}{{{c.denominator}}}"


# ================================================================ 4.9 mensuration
@tpl("geometry.mensuration", "short", n=16)
def sector_measure(r):
    rad = r.choice([F(k, 2) for k in range(8, 40)])
    ang = r.choice([k for k in range(30, 330, 5) if k not in (90, 180, 270)])
    want = r.choice(["arc", "area", "perim"])
    arc = ang / 360 * 2 * PI * float(rad)
    area = ang / 360 * PI * float(rad) ** 2
    s = sector_fig(f"{num(float(rad))} cm", ang, f"{ang}°")
    if want == "arc":
        return Q(intro="$OAB$ is a sector of a circle with centre $O$.", figs=[fig(s, 55)],
                 parts=[P("", "Calculate the length of the arc $AB$.\n\nGive your answer to 3 significant figures.", 2, prefix="cm")],
                 rows=[R("", f"$\\dfrac{{{ang}}}{{360}} \\times 2 \\times \\pi \\times {num(float(rad))}$", "M1", ""),
                       R("", sf(arc, 3), "A1", f"awrt {sf(arc, 3)}")],
                 values={"arc": arc}, diff="4-6", cw="Calculate", refs=["H4.9A"])
    if want == "area":
        return Q(intro="$OAB$ is a sector of a circle with centre $O$.", figs=[fig(s, 55)],
                 parts=[P("", "Calculate the area of the sector.\n\nGive your answer to 3 significant figures.", 2, prefix="cm²")],
                 rows=[R("", f"$\\dfrac{{{ang}}}{{360}} \\times \\pi \\times {num(float(rad))}^2$", "M1", ""),
                       R("", sf(area, 3), "A1", f"awrt {sf(area, 3)}")],
                 values={"area": area}, diff="4-6", cw="Calculate", refs=["H4.9A"])
    per = arc + 2 * float(rad)
    return Q(intro="$OAB$ is a sector of a circle with centre $O$.", figs=[fig(s, 55)],
             parts=[P("", "Calculate the perimeter of the sector.\n\nGive your answer to 3 significant figures.", 3, prefix="cm")],
             rows=[R("", f"$\\dfrac{{{ang}}}{{360}} \\times 2 \\times \\pi \\times {num(float(rad))}$ $(= {sf(arc, 4)})$", "M1", ""),
                   R("", f"${sf(arc, 4)} + 2 \\times {num(float(rad))}$", "M1", "for adding two radii to their arc length"),
                   R("", sf(per, 3), "A1", f"awrt {sf(per, 3)}")],
             values={"perimeter": per}, diff="4-6", cw="Calculate", refs=["H4.9A"])


@tpl("geometry.mensuration", "short", n=16)
def trapezium_area(r):
    a, b = sorted(r.sample(range(3, 25), 2))
    h = r.randint(3, 15)
    area = F(a + b, 2) * h
    off = r.uniform(-0.3, 0.6) * (b - a)
    pts = [(0, 0), (b, 0), (off + a, h), (off, h)]
    if r.random() < 0.5:
        s = polygon_fig(pts, sides={(0, 1): f"{b} cm", (2, 3): f"{a} cm"},
                        extra={"body": lambda fr: L(*fr((off, h)), *fr((off, 0)), dash="4,3") + T(fr((off, h / 2))[0] - 18, fr((off, h / 2))[1], f"{h} cm")
                               + par_arrow(fr((0, 0)), fr((b, 0))) + par_arrow(fr((off + a, h)), fr((off, h)))}, w=300, h=190)
        return Q(intro="The diagram shows a trapezium.", figs=[fig(s, 60)],
                 parts=[P("", "Work out the area of the trapezium.", 2, prefix="cm²")],
                 rows=[R("", f"$\\frac{{1}}{{2}}({a} + {b}) \\times {h}$", "M1", ""), R("", num(area), "A1", "cao")],
                 values={"area": area}, diff="1-3", cw="Work out", refs=["F4.9D"])
    s = polygon_fig(pts, sides={(0, 1): f"{b} cm", (2, 3): f"{a} cm"},
                    extra={"body": lambda fr: L(*fr((off, h)), *fr((off, 0)), dash="4,3") + T(fr((off, h / 2))[0] - 14, fr((off, h / 2))[1], "h")
                           + par_arrow(fr((0, 0)), fr((b, 0))) + par_arrow(fr((off + a, h)), fr((off, h)))}, w=300, h=190)
    return Q(intro=f"The diagram shows a trapezium.\n\nThe area of the trapezium is {num(area)} cm².", figs=[fig(s, 60)],
             parts=[P("", "Work out the value of $h$, the perpendicular height of the trapezium.", 3, prefix="$h =$")],
             rows=[R("", f"$\\frac{{1}}{{2}}({a} + {b}) \\times h = {num(area)}$", "M1", ""),
                   R("", f"$h = {num(area)} \\div {num(F(a + b, 2))}$", "M1", f"or $2 \\times {num(area)} \\div {a + b}$"),
                   R("", str(h), "A1", "cao")],
             values={"h": h}, diff="4-6", cw="Work out", refs=["F4.9D"])


@tpl("geometry.mensuration", "short", n=16)
def area_units(r):
    kind = r.choice(["m2cm2", "cm2mm2", "cm2m2", "circle", "semi"])
    if kind == "m2cm2":
        v = r.choice([F(k, 100) for k in range(15, 900, 7)])
        return Q(parts=[P("", f"Change {num(float(v))} m² into cm².", 2, prefix="cm²")],
                 rows=[R("", f"${num(float(v))} \\times 100^2$", "M1", "or $\\times 10\\,000$"), R("", big(v * 10000), "A1", "cao")],
                 values={"cm2": v * 10000}, diff="4-6", cw="Change", refs=["F4.9A"])
    if kind == "cm2mm2":
        v = r.choice([F(k, 10) for k in range(12, 900, 7)])
        return Q(parts=[P("", f"Change {num(float(v))} cm² into mm².", 2, prefix="mm²")],
                 rows=[R("", f"${num(float(v))} \\times 10^2$", "M1", ""), R("", num(float(v * 100)), "A1", "cao")],
                 values={"mm2": v * 100}, diff="4-6", cw="Change", refs=["F4.9A"])
    if kind == "cm2m2":
        v = r.randrange(1500, 95000, 50)
        return Q(parts=[P("", f"Change {big(v)} cm² into m².", 2, prefix="m²")],
                 rows=[R("", f"${big(v)} \\div 100^2$", "M1", ""), R("", num(float(F(v, 10000))), "A1", "cao")],
                 values={"m2": F(v, 10000)}, diff="4-6", cw="Change", refs=["F4.9A"])
    d = r.randint(4, 40)
    if kind == "circle":
        area = PI * d * d / 4
        return Q(parts=[P("", f"A circle has a diameter of {d} cm.\n\nWork out the area of the circle.\n\nGive your answer to 3 significant figures.", 2, prefix="cm²")],
                 rows=[R("", f"$\\pi \\times {num(F(d, 2))}^2$", "M1", ""), R("", sf(area, 3), "A1", f"awrt {sf(area, 3)}")],
                 values={"area": area}, diff="1-3", cw="Work out", refs=["F4.9E"])
    per = PI * d / 2 + d
    return Q(parts=[P("", f"A semicircle has a diameter of {d} cm.\n\nFind the perimeter of this semicircle.\n\nGive your answer to 3 significant figures.", 3, prefix="cm")],
             rows=[R("", f"$\\pi \\times {d} \\div 2$", "M1", "for the curved part"), R("", f"$\\ldots + {d}$", "M1", "for adding the diameter"),
                   R("", sf(per, 3), "A1", f"awrt {sf(per, 3)}")],
             values={"perimeter": per}, diff="4-6", cw="Work out", refs=["F4.9E"])


@tpl("geometry.mensuration", "problem", n=17)
def segment_area(r):
    rad = r.randint(5, 20)
    ang = r.randint(40, 150)
    sector = ang / 360 * PI * rad * rad
    tri = 0.5 * rad * rad * math.sin(math.radians(ang))
    seg = sector - tri
    s = sector_fig(f"{rad} cm", ang, f"{ang}°")
    return Q(intro=f"The diagram shows a sector $OAB$ of a circle, centre $O$, radius {rad} cm.\n\nThe chord $AB$ divides the sector into a triangle and a segment.",
             figs=[fig(_with_chord(s), 55)],
             parts=[P("", "Calculate the area of the segment between the chord $AB$ and the arc $AB$.\n\nGive your answer to 3 significant figures.", 4, prefix="cm²")],
             rows=[R("", f"$\\dfrac{{{ang}}}{{360}} \\times \\pi \\times {rad}^2$ $(= {sf(sector, 4)})$", "M1", "for the sector area"),
                   R("", f"$\\frac{{1}}{{2}} \\times {rad} \\times {rad} \\times \\sin {ang}$ $(= {sf(tri, 4)})$", "M1", "for the triangle area"),
                   R("", f"${sf(sector, 4)} - {sf(tri, 4)}$", "M1", "dep on both previous M marks"),
                   R("", sf(seg, 3), "A1", f"awrt {sf(seg, 3)}")],
             values={"segment": seg}, diff="7-9", cw="Calculate", refs=["H4.9A", "H4.8E"])


def _with_chord(s):
    """Add chord between the two line ends of a sector_fig (first two <line> elements share O)."""
    import re
    ls = re.findall(r'<line x1="([\d.]+)" y1="([\d.]+)" x2="([\d.]+)" y2="([\d.]+)"/>', s)
    if len(ls) >= 2:
        (_, _, ax, ay), (_, _, bx, by) = ls[0], ls[1]
        s = s.replace("</svg>", f'<line x1="{ax}" y1="{ay}" x2="{bx}" y2="{by}"/></svg>')
    return s


@tpl("geometry.mensuration", "problem", n=17)
def sector_reverse(r):
    kind = r.choice(["area_to_arc", "arc_to_area", "angle"])
    rad = r.randint(4, 25)
    ang = r.choice(range(20, 340, 5))
    arc = ang / 360 * 2 * PI * rad
    area = ang / 360 * PI * rad * rad
    if kind == "area_to_arc":
        A_ = round(area, 1)
        a_ = A_ / (PI * rad * rad) * 360
        arc_ = a_ / 360 * 2 * PI * rad
        return Q(intro=f"A sector of a circle has radius {rad} cm and area {num(A_)} cm².",
                 parts=[P("", "Calculate the perimeter of the sector.\n\nGive your answer to 3 significant figures.", 4, prefix="cm")],
                 rows=[R("", f"$\\dfrac{{\\theta}}{{360}} \\times \\pi \\times {rad}^2 = {num(A_)}$", "M1", ""),
                       R("", f"$\\theta = {sf(a_, 4)}$", "A1", "or arc $= 2 \\times " + num(A_) + " \\div " + str(rad) + "$"),
                       R("", f"$\\dfrac{{{sf(a_, 4)}}}{{360}} \\times 2\\pi \\times {rad} + 2 \\times {rad}$", "M1", "ft their angle"),
                       R("", sf(arc_ + 2 * rad, 3), "A1", f"awrt {sf(arc_ + 2 * rad, 3)}")],
                 values={"angle": a_, "perimeter": arc_ + 2 * rad}, diff="7-9", cw="Calculate", refs=["H4.9A"])
    if kind == "arc_to_area":
        L_ = round(arc, 1)
        a_ = L_ / (2 * PI * rad) * 360
        ar = a_ / 360 * PI * rad * rad
        return Q(intro=f"A sector of a circle has radius {rad} cm.\n\nThe length of the arc of the sector is {num(L_)} cm.",
                 parts=[P("", "Calculate the area of the sector.\n\nGive your answer to 3 significant figures.", 4, prefix="cm²")],
                 rows=[R("", f"$\\dfrac{{\\theta}}{{360}} \\times 2\\pi \\times {rad} = {num(L_)}$", "M1", ""),
                       R("", f"$\\theta = {sf(a_, 4)}$", "A1", ""),
                       R("", f"$\\dfrac{{{sf(a_, 4)}}}{{360}} \\times \\pi \\times {rad}^2$", "M1", "ft their angle; or $\\frac{1}{2} \\times " + num(L_) + " \\times " + str(rad) + "$"),
                       R("", sf(ar, 3), "A1", f"awrt {sf(ar, 3)}")],
                 values={"angle": a_, "area": ar}, diff="7-9", cw="Calculate", refs=["H4.9A"])
    A_ = round(area, 1)
    rr = math.sqrt(A_ * 360 / (ang * PI))
    return Q(intro=f"A sector of a circle has an angle of ${ang}{DEG}$ at the centre.\n\nThe area of the sector is {num(A_)} cm².",
             parts=[P("", "Calculate the radius of the circle.\n\nGive your answer to 3 significant figures.", 3, prefix="cm")],
             rows=[R("", f"$\\dfrac{{{ang}}}{{360}} \\times \\pi r^2 = {num(A_)}$", "M1", ""),
                   R("", f"$r = \\sqrt{{\\dfrac{{{num(A_)} \\times 360}}{{{ang}\\pi}}}}$", "M1", ""),
                   R("", sf(rr, 3), "A1", f"awrt {sf(rr, 3)}")],
             values={"radius": rr}, diff="7-9", cw="Calculate", refs=["H4.9A"])


@tpl("geometry.mensuration", "problem", n=17)
def composite_semicircle(r):
    w_ = r.randint(6, 24)
    l = r.randint(w_ + 2, 40)
    kind = r.choice(["area", "perim", "cutout"])
    pts = [(0, 0), (l, 0), (l, w_), (0, w_)]

    def body(fr):
        cx, cy = fr((l, w_ / 2))
        rr = fr.k * w_ / 2
        if kind == "cutout":
            return ARC(cx, cy, rr, 90, 270)
        return ARC(cx, cy, rr, 270, 450)
    s = polygon_fig([(l, 0), (0, 0), (0, w_), (l, w_)], sides={(0, 1): f"{l} cm", (1, 2): f"{w_} cm"}, extra={"body": body,
                    "pts": [(l + w_ / 2, 0)]}, closed=False, w=320, h=200)
    if kind == "cutout":
        area = l * w_ - PI * (w_ / 2) ** 2 / 2
        per = 2 * l + w_ + PI * w_ / 2
        return Q(intro=f"The diagram shows a metal plate. It is a rectangle, {l} cm by {w_} cm, with a semicircle of diameter {w_} cm cut out of one end.",
                 figs=[fig(s, 70)],
                 parts=[P("a", "Calculate the area of the plate.\n\nGive your answer to 3 significant figures.", 3, prefix="cm²"),
                        P("b", "Calculate the perimeter of the plate.\n\nGive your answer to 3 significant figures.", 3, prefix="cm")],
                 rows=[R("a", f"${l} \\times {w_} = {l * w_}$", "M1", ""), R("a", f"$\\frac{{1}}{{2}} \\times \\pi \\times {num(F(w_, 2))}^2$ subtracted", "M1", ""),
                       R("a", sf(area, 3), "A1", f"awrt {sf(area, 3)}"),
                       R("b", f"$\\frac{{1}}{{2}} \\times \\pi \\times {w_}$", "M1", "for the curved edge"),
                       R("b", f"$2 \\times {l} + {w_} + {sf(PI * w_ / 2, 4)}$", "M1", "for all the straight edges with their curved edge"),
                       R("b", sf(per, 3), "A1", f"awrt {sf(per, 3)}")],
                 values={"area": area, "perimeter": per}, diff="7-9", cw="Calculate", refs=["F4.9E"])
    area = l * w_ + PI * (w_ / 2) ** 2 / 2
    per = 2 * l + w_ + PI * w_ / 2
    if kind == "area":
        return Q(intro=f"The diagram shows a shape made from a rectangle, {l} cm by {w_} cm, and a semicircle.", figs=[fig(s, 70)],
                 parts=[P("", "Calculate the area of the shape.\n\nGive your answer to 3 significant figures.", 3, prefix="cm²")],
                 rows=[R("", f"${l} \\times {w_}$", "M1", ""), R("", f"$\\frac{{1}}{{2}} \\times \\pi \\times {num(F(w_, 2))}^2$", "M1", ""),
                       R("", sf(area, 3), "A1", f"awrt {sf(area, 3)}")],
                 values={"area": area}, diff="4-6", cw="Calculate", refs=["F4.9E"])
    return Q(intro=f"The diagram shows a shape made from a rectangle, {l} cm by {w_} cm, and a semicircle.", figs=[fig(s, 70)],
             parts=[P("", "Calculate the perimeter of the shape.\n\nGive your answer to 3 significant figures.", 3, prefix="cm")],
             rows=[R("", f"$\\frac{{1}}{{2}} \\times \\pi \\times {w_}$", "M1", ""), R("", f"$2 \\times {l} + {w_} + {sf(PI * w_ / 2, 4)}$", "M1", ""),
                   R("", sf(per, 3), "A1", f"awrt {sf(per, 3)}")],
             values={"perimeter": per}, diff="4-6", cw="Calculate", refs=["F4.9E"])


# ================================================================ 4.10 volume
@tpl("geometry.volume", "short", n=7)
def volume_solid(r):
    kind = r.choice(["cyl", "cone", "sphere", "hemi", "prism"])
    rad = r.choice([F(k, 2) for k in range(4, 30)])
    h = r.randint(4, 30)
    if kind == "cyl":
        v = PI * float(rad) ** 2 * h
        s = cone_fig(f"{num(float(rad))} cm", f"{h} cm", kind="cylinder")
        txt, m = "a cylinder", f"$\\pi \\times {num(float(rad))}^2 \\times {h}$"
    elif kind == "cone":
        v = PI * float(rad) ** 2 * h / 3
        s = cone_fig(f"{num(float(rad))} cm", f"{h} cm")
        txt, m = "a solid cone", f"$\\frac{{1}}{{3}} \\times \\pi \\times {num(float(rad))}^2 \\times {h}$"
    elif kind == "sphere":
        v = 4 / 3 * PI * float(rad) ** 3
        s = sphere_fig(f"{num(float(rad))} cm")
        txt, m = "a solid sphere", f"$\\frac{{4}}{{3}} \\times \\pi \\times {num(float(rad))}^3$"
    elif kind == "hemi":
        v = 2 / 3 * PI * float(rad) ** 3
        s = sphere_fig(f"{num(float(rad))} cm", hemi=True)
        txt, m = "a solid hemisphere", f"$\\frac{{1}}{{2}} \\times \\frac{{4}}{{3}} \\times \\pi \\times {num(float(rad))}^3$"
    else:
        b, hh, l = r.randint(3, 14), r.randint(3, 14), r.randint(5, 25)
        v = F(1, 2) * b * hh * l
        pts = [(0, 0), (b, 0), (0, hh)]
        s = svg(300, 200, _prism_body(b, hh, l))
        return Q(intro=f"The diagram shows a prism. The cross section of the prism is a right-angled triangle with base {b} cm and height {hh} cm.\n\nThe length of the prism is {l} cm.",
                 figs=[fig(s, 60)], parts=[P("", "Work out the volume of the prism.", 2, prefix="cm³")],
                 rows=[R("", f"$\\frac{{1}}{{2}} \\times {b} \\times {hh} \\times {l}$", "M1", ""), R("", num(v), "A1", "cao")],
                 values={"volume": v}, diff="4-6", cw="Work out", refs=["F4.10E"])
    dims = f"radius {num(float(rad))} cm" + (f" and height {h} cm" if kind in ("cyl", "cone") else "")
    return Q(intro=f"The diagram shows {txt} with {dims}.", figs=[fig(s, 50)],
             parts=[P("", f"Work out the volume of the {txt.split()[-1]}.\n\nGive your answer to 3 significant figures.", 2, prefix="cm³")],
             rows=[R("", m, "M1", ""), R("", sf(v, 3), "A1", f"awrt {sf(v, 3)}")],
             values={"volume": v}, diff="4-6", cw="Work out", refs=["H4.10A", "F4.10E"])


def _prism_body(b, hh, l):
    k = min(110 / max(b, hh), 12)
    ox, oy = 30, 185
    A, B, Cc = (ox, oy), (ox + b * k, oy), (ox, oy - hh * k)
    dx, dy = min(130, l * 6), -min(60, l * 3)
    A2, B2, C2 = (A[0] + dx, A[1] + dy), (B[0] + dx, B[1] + dy), (Cc[0] + dx, Cc[1] + dy)
    return (PL([A, B, Cc], close=True) + L(*B, *B2) + L(*Cc, *C2) + L(*A, *A2, dash="4,3") + L(*B2, *C2)
            + L(*A2, *B2, dash="4,3") + L(*A2, *C2, dash="4,3") + right_mark(A, B, Cc))


@tpl("geometry.volume", "short", n=7)
def surface_area(r):
    kind = r.choice(["cyl", "cone", "sphere", "hemi"])
    rad = r.randint(2, 20)
    h = r.randint(3, 30)
    if kind == "cyl":
        sa = 2 * PI * rad * h + 2 * PI * rad * rad
        return Q(intro=f"A solid cylinder has radius {rad} cm and height {h} cm.",
                 parts=[P("", "Work out the total surface area of the cylinder.\n\nGive your answer to 3 significant figures.", 3, prefix="cm²")],
                 rows=[R("", f"$2 \\times \\pi \\times {rad} \\times {h}$", "M1", "for the curved surface"),
                       R("", f"$2 \\times \\pi \\times {rad}^2$", "M1", "for the two circular ends"),
                       R("", sf(sa, 3), "A1", f"awrt {sf(sa, 3)}")],
                 values={"sa": sa}, diff="4-6", cw="Work out", refs=["F4.10D"])
    if kind == "cone":
        l = math.sqrt(rad * rad + h * h)
        sa = PI * rad * l + PI * rad * rad
        return Q(intro=f"A solid cone has base radius {rad} cm and perpendicular height {h} cm.", figs=[fig(cone_fig(f"{rad} cm", f"{h} cm"), 45)],
                 parts=[P("", "Work out the total surface area of the cone.\n\nGive your answer to 3 significant figures.", 4, prefix="cm²")],
                 rows=[R("", f"$l = \\sqrt{{{rad}^2 + {h}^2}}$", "M1", "for the slant height"),
                       R("", f"$\\pi \\times {rad} \\times {sf(l, 4)}$", "M1", "for the curved surface area"),
                       R("", f"$\\ldots + \\pi \\times {rad}^2$", "M1", "for adding the base"),
                       R("", sf(sa, 3), "A1", f"awrt {sf(sa, 3)}")],
                 values={"sa": sa}, diff="7-9", cw="Work out", refs=["H4.10A", "F4.8A"])
    if kind == "sphere":
        sa = 4 * PI * rad * rad
        return Q(intro=f"A sphere has a diameter of {2 * rad} cm.",
                 parts=[P("", "Work out the surface area of the sphere.\n\nGive your answer to 3 significant figures.", 2, prefix="cm²")],
                 rows=[R("", f"$4 \\times \\pi \\times {rad}^2$", "M1", "radius must be halved"), R("", sf(sa, 3), "A1", f"awrt {sf(sa, 3)}")],
                 values={"sa": sa}, diff="4-6", cw="Work out", refs=["H4.10A"])
    sa = 3 * PI * rad * rad
    return Q(intro=f"A solid hemisphere has radius {rad} cm.", figs=[fig(sphere_fig(f"{rad} cm", hemi=True), 45)],
             parts=[P("", "Work out the total surface area of the hemisphere.\n\nGive your answer to 3 significant figures.", 3, prefix="cm²")],
             rows=[R("", f"$\\frac{{1}}{{2}} \\times 4 \\times \\pi \\times {rad}^2$", "M1", "for the curved surface"),
                   R("", f"$\\ldots + \\pi \\times {rad}^2$", "M1", "for the flat face"),
                   R("", sf(sa, 3), "A1", f"awrt {sf(sa, 3)}")],
             values={"sa": sa}, diff="7-9", cw="Work out", refs=["H4.10A"])


@tpl("geometry.volume", "problem", n=6)
def melt_recast(r):
    R_ = r.randint(3, 15)
    kind = r.choice(["cones", "cylinder", "spheres"])
    vs = 4 / 3 * PI * R_ ** 3
    if kind == "cones":
        cr, ch = r.randint(1, 4), r.randint(2, 9)
        vc = PI * cr * cr * ch / 3
        ratio = F(4 * R_ ** 3, cr * cr * ch)  # exact V_sphere / V_cone (pi cancels)
        n = math.floor(ratio)  # whole cones: floor of the exact value
        if n < 3:
            return None
        return Q(intro=f"A solid metal sphere has radius {R_} cm.\n\nThe sphere is melted down and the metal is used to make solid cones. Each cone has base radius {cr} cm and height {ch} cm.",
                 parts=[P("", "Work out the greatest number of cones that can be made.", 4, prefix="")],
                 rows=[R("", f"$\\frac{{4}}{{3}} \\pi \\times {R_}^3$ $(= {sf(vs, 5)})$", "M1", "for the volume of the sphere"),
                       R("", f"$\\frac{{1}}{{3}} \\pi \\times {cr}^2 \\times {ch}$ $(= {sf(vc, 5)})$", "M1", "for the volume of one cone"),
                       R("", f"${sf(vs, 5)} \\div {sf(vc, 5)} = {num(ratio) if ratio.denominator == 1 else sf(float(ratio), 5)}$", "M1", ""),
                       R("", str(n), "A1", "cao; must be a whole number")],
                 values={"n": n}, diff="7-9", cw="Work out", refs=["H4.10A"])
    if kind == "cylinder":
        cr = r.randint(2, 12)
        h = vs / (PI * cr * cr)
        return Q(intro=f"A solid metal sphere has radius {R_} cm.\n\nThe sphere is melted down and all the metal is made into a solid cylinder of radius {cr} cm.",
                 parts=[P("", "Calculate the height of the cylinder.\n\nGive your answer to 3 significant figures.", 3, prefix="cm")],
                 rows=[R("", f"$\\frac{{4}}{{3}} \\pi \\times {R_}^3$", "M1", ""),
                       R("", f"$\\pi \\times {cr}^2 \\times h = \\frac{{4}}{{3}} \\pi \\times {R_}^3$", "M1", ""),
                       R("", sf(h, 3), "A1", f"awrt {sf(h, 3)}; exact value ${ftex(F(4 * R_ ** 3, 3 * cr * cr))}$")],
                 values={"height": h}, diff="7-9", cw="Calculate", refs=["H4.10A", "F4.10E"])
    k = r.choice([8, 27, 64, 125, 1000])
    rr = R_ / round(k ** (1 / 3))
    return Q(intro=f"A solid metal sphere has radius {R_} cm.\n\nThe sphere is melted down and all the metal is made into {k} identical smaller spheres.",
             parts=[P("", "Work out the radius of each small sphere.", 3, prefix="cm")],
             rows=[R("", f"$\\frac{{4}}{{3}} \\pi \\times {R_}^3 \\div {k}$", "M1", ""),
                   R("", f"$\\frac{{4}}{{3}} \\pi r^3 = \\ldots$ and $r^3 = {num(F(R_ ** 3, k))}$", "M1", ""),
                   R("", num(rr), "A1", "oe")],
             values={"radius": rr}, diff="7-9", cw="Work out", refs=["H4.10A"])


@tpl("geometry.volume", "problem", n=6)
def fill_container(r):
    kind = r.choice(["rate", "pour"])
    if kind == "rate":
        rad = r.randint(10, 60)
        h = r.randint(20, 120)
        rate = r.choice([F(k, 2) for k in range(2, 30)])
        vol = PI * rad * rad * h / 1000
        t = vol / float(rate)
        return Q(intro=f"A water tank is a cylinder with radius {rad} cm and height {h} cm.\n\nThe tank is empty. Water flows into the tank at a rate of {num(float(rate))} litres per minute.\n\n1 litre $= 1000$ cm³",
                 parts=[P("", "Work out how long it takes to fill the tank. Give your answer in minutes, correct to the nearest minute.", 4, prefix="minutes")],
                 rows=[R("", f"$\\pi \\times {rad}^2 \\times {h}$ $(= {sf(vol * 1000, 5)})$", "M1", ""),
                       R("", f"$\\div 1000$ $(= {sf(vol, 5)}$ litres$)$", "M1", "for converting to litres"),
                       R("", f"$\\div {num(float(rate))}$", "M1", ""),
                       R("", str(round(t)), "A1", f"accept {sf(t, 3)}")],
                 values={"minutes": t}, diff="7-9", cw="Work out", refs=["F4.10E", "F4.10F"])
    cr, ch = r.randint(3, 12), r.randint(6, 25)
    vr = r.randint(4, 15)
    vc = PI * cr * cr * ch / 3
    h = vc / (PI * vr * vr)
    return Q(intro=f"A container in the shape of a cone, with base radius {cr} cm and height {ch} cm, is full of water.\n\nAll the water is poured into an empty cylinder of radius {vr} cm.",
             parts=[P("", "Calculate the depth of water in the cylinder, in cm.\n\nGive your answer to 3 significant figures.", 3, prefix="cm")],
             rows=[R("", f"$\\frac{{1}}{{3}} \\pi \\times {cr}^2 \\times {ch}$", "M1", ""),
                   R("", f"$\\pi \\times {vr}^2 \\times d = \\ldots$", "M1", ""),
                   R("", sf(h, 3), "A1", f"awrt {sf(h, 3)}")],
             values={"depth": h}, diff="7-9", cw="Calculate", refs=["H4.10A", "F4.10E"])


@tpl("geometry.volume", "problem", n=6)
def frustum(r):
    R_ = r.randint(6, 20)
    H = r.randint(10, 40)
    k = r.choice([F(1, 2), F(1, 3), F(2, 3), F(1, 4), F(3, 4), F(2, 5), F(3, 5)])
    rs, hs = R_ * k, H * k
    if F(rs).denominator > 2 or F(hs).denominator > 2:
        return None
    vbig = PI * R_ * R_ * H / 3
    vs = PI * float(rs) ** 2 * float(hs) / 3
    v = vbig - vs
    return Q(intro=f"A solid cone has base radius {R_} cm and height {H} cm.\n\nA small cone of height {num(float(hs))} cm is removed from the top of the cone to leave a frustum. The base of the small cone is parallel to the base of the large cone.",
             figs=[fig(cone_fig(f"{R_} cm", f"{H} cm"), 45)],
             parts=[P("", "Calculate the volume of the frustum.\n\nGive your answer to 3 significant figures.", 5, prefix="cm³")],
             rows=[R("", f"radius of small cone $= {R_} \\times \\dfrac{{{num(float(hs))}}}{{{H}}} = {num(float(rs))}$", "M1", "for using similar triangles"),
                   R("", f"$\\frac{{1}}{{3}} \\pi \\times {R_}^2 \\times {H}$", "M1", "for the volume of the large cone"),
                   R("", f"$\\frac{{1}}{{3}} \\pi \\times {num(float(rs))}^2 \\times {num(float(hs))}$", "M1", "for the volume of the small cone"),
                   R("", f"${sf(vbig, 5)} - {sf(vs, 5)}$", "M1", "dep on M2; or volume of large cone $\\times (1 - (" + ftex(k) + ")^3)$"),
                   R("", sf(v, 3), "A1", f"awrt {sf(v, 3)}")],
             values={"volume": v}, diff="7-9", cw="Calculate", refs=["H4.10A", "H4.11B"])


@tpl("geometry.volume", "proof", n=7)
def show_surface(r):
    k = r.randint(2, 6)
    kind = r.choice(["cyl_hemi", "cone_hemi"])
    if kind == "cyl_hemi":
        tot = 2 * k + 2 + 1  # 2*pi*r*kr + 2 pi r^2 + pi r^2
        return Q(intro=f"A solid is made from a cylinder and a hemisphere.\n\nThe cylinder has radius $r$ cm and height ${k}r$ cm. The flat face of the hemisphere is joined to one end of the cylinder, and the radius of the hemisphere is $r$ cm.",
                 parts=[P("", f"Show that the total surface area of the solid is ${tot}\\pi r^2$ cm².", 3, space="working")],
                 rows=[R("", f"curved surface of cylinder $= 2\\pi r \\times {k}r = {2 * k}\\pi r^2$", "M1", ""),
                       R("", "curved surface of hemisphere $= 2\\pi r^2$ and base of cylinder $= \\pi r^2$", "M1", ""),
                       R("", f"${2 * k}\\pi r^2 + 2\\pi r^2 + \\pi r^2 = {tot}\\pi r^2$", "A1", "dep on M2; correct total shown with no incorrect working")],
                 values={"k": tot}, diff="7-9", cw="Show that", refs=["H4.10A", "F4.10D"])
    trip = r.choice([(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (6, 8, 10)])
    a, b, c = trip
    # cone radius a*t, height b*t, slant c*t: use radius = a x, height = b x
    tot = F(a * c) + 2 * a * a  # pi r l + 2 pi r^2
    return Q(intro=f"A solid is made from a cone and a hemisphere.\n\nThe cone has base radius ${a}x$ cm and perpendicular height ${b}x$ cm. The hemisphere has radius ${a}x$ cm and its flat face is joined to the base of the cone.",
             parts=[P("", f"Show that the total surface area of the solid is ${num(tot)}\\pi x^2$ cm².", 4, space="working")],
             rows=[R("", f"slant height $= \\sqrt{{({a}x)^2 + ({b}x)^2}} = {c}x$", "M1", ""),
                   R("", f"curved surface of cone $= \\pi \\times {a}x \\times {c}x = {a * c}\\pi x^2$", "M1", ""),
                   R("", f"curved surface of hemisphere $= 2\\pi({a}x)^2 = {2 * a * a}\\pi x^2$", "M1", ""),
                   R("", f"${a * c}\\pi x^2 + {2 * a * a}\\pi x^2 = {num(tot)}\\pi x^2$", "A1", "dep on M3; with no incorrect working")],
             values={"k": tot}, diff="7-9", cw="Show that", refs=["H4.10A", "F4.8A"])


@tpl("geometry.volume", "proof", n=7)
def show_volume_relation(r):
    kind = r.choice(["cone_sphere", "cyl_sphere", "cone_cyl"])
    m = r.randint(2, 5)
    if kind == "cone_sphere":
        # cone radius m r, height h equal volume sphere radius r: (1/3) pi m^2 r^2 h = 4/3 pi r^3 -> h = 4r/m^2
        hk = F(4, m * m)
        return Q(intro=f"A solid cone has base radius ${m}r$ cm and height $h$ cm.\n\nA solid sphere has radius $r$ cm.\n\nThe volume of the cone is equal to the volume of the sphere.",
                 parts=[P("", f"Show that $h = {ftex(hk) if hk.denominator != 1 else hk.numerator}r$" + ("" if hk.denominator == 1 else "") + ".", 3, space="working")],
                 rows=[R("", f"$\\frac{{1}}{{3}}\\pi({m}r)^2 h$ or $\\frac{{4}}{{3}}\\pi r^3$", "M1", ""),
                       R("", f"$\\frac{{{m * m}}}{{3}}\\pi r^2 h = \\frac{{4}}{{3}}\\pi r^3$", "M1", "for equating correct expressions"),
                       R("", f"$h = {ftex(hk)}r$ with correct cancelling shown", "A1", "dep on M2")],
                 values={"h_over_r": hk}, diff="7-9", cw="Show that", refs=["H4.10A"])
    if kind == "cyl_sphere":
        hk = F(4, 3 * m * m)
        return Q(intro=f"A solid cylinder has radius ${m}r$ cm and height $h$ cm.\n\nA solid sphere has radius $r$ cm.\n\nThe volume of the cylinder is equal to the volume of the sphere.",
                 parts=[P("", f"Show that $h = {ftex(hk)}r$.", 3, space="working")],
                 rows=[R("", f"$\\pi({m}r)^2 h$ or $\\frac{{4}}{{3}}\\pi r^3$", "M1", ""),
                       R("", f"${m * m}\\pi r^2 h = \\frac{{4}}{{3}}\\pi r^3$", "M1", ""),
                       R("", f"$h = {ftex(hk)}r$ with correct working", "A1", "dep on M2")],
                 values={"h_over_r": hk}, diff="7-9", cw="Show that", refs=["H4.10A", "F4.10E"])
    hk = F(3, m * m)
    return Q(intro=f"A solid cylinder has radius $r$ cm and height $h$ cm.\n\nA solid cone has radius ${m}r$ cm and height $H$ cm.\n\nThe volume of the cone is equal to the volume of the cylinder.",
             parts=[P("", f"Show that $H = {ftex(hk)}h$.", 3, space="working")],
             rows=[R("", f"$\\pi r^2 h$ or $\\frac{{1}}{{3}}\\pi({m}r)^2 H$", "M1", ""),
                   R("", f"$\\pi r^2 h = \\frac{{{m * m}}}{{3}}\\pi r^2 H$", "M1", ""),
                   R("", f"$H = {ftex(hk)}h$ with correct working", "A1", "dep on M2")],
             values={"H_over_h": hk}, diff="7-9", cw="Show that", refs=["H4.10A", "F4.10E"])


# ================================================================ 4.11 similarity
def two_tri_fig(p1, p2, n1, n2, s1, s2, gap=0.6):
    """two triangles drawn side by side; s1/s2 side labels {(i,j):lab}."""
    w1 = max(p[0] for p in p1) - min(p[0] for p in p1)
    shift = w1 + gap * max(1, w1)
    p2s = [(x + shift, y) for x, y in p2]
    fr = Frame(p1 + p2s, 360, 200, m=30)
    out = ""
    for pts, nms, sides in ((p1, n1, s1), (p2s, n2, s2)):
        S = [fr(p) for p in pts]
        out += PL(S, close=True)
        cx, cy = sum(p[0] for p in S) / 3, sum(p[1] for p in S) / 3
        for (x, y), nm in zip(S, nms):
            d = math.hypot(x - cx, y - cy) or 1
            out += T(x + 12 * (x - cx) / d, y + 12 * (y - cy) / d, nm)
        for (i, j), lab in sides.items():
            mx, my = (S[i][0] + S[j][0]) / 2, (S[i][1] + S[j][1]) / 2
            d = math.hypot(mx - cx, my - cy) or 1
            out += T(mx + (12 + 2.5 * len(lab)) * (mx - cx) / d, my + 14 * (my - cy) / d, lab, size=12)
    return svg(fr.w, fr.h, out)


@tpl("geometry.similarity", "short", n=7)
def similar_lengths(r):
    a, b, c = sorted(r.sample(range(4, 16), 3))
    if a + b <= c:
        return None
    k = r.choice([F(3, 2), F(5, 2), F(2), F(3), F(4, 3), F(5, 4), F(7, 4), F(5, 3)])
    p1 = [(0, 0), (c, 0), ((b * b + c * c - a * a) / (2 * c), math.sqrt(max(0.1, b * b - ((b * b + c * c - a * a) / (2 * c)) ** 2)))]
    p2 = [(x * float(k), y * float(k)) for x, y in p1]
    n1, n2 = r.sample(LET, 2)
    s1 = {(0, 1): f"{c} cm", (1, 2): f"{a} cm", (2, 0): "x cm"}
    s2 = {(0, 1): f"{num(float(c * k))} cm", (2, 0): f"{num(float(b * k))} cm", (1, 2): "y cm"}
    s = two_tri_fig(p1, p2, n1, n2, s1, s2)
    return Q(intro=f"Triangle ${n1}$ is similar to triangle ${n2}$.\n\nAngle ${n1[0]}$ = angle ${n2[0]}$, angle ${n1[1]}$ = angle ${n2[1]}$ and angle ${n1[2]}$ = angle ${n2[2]}$.",
             figs=[fig(s, 85)],
             parts=[P("a", "Work out the value of $x$.", 2, prefix="$x =$"), P("b", "Work out the value of $y$.", 2, prefix="$y =$")],
             rows=[R("a", f"scale factor $= {num(float(c * k))} \\div {c} = {num(float(k))}$", "M1", f"or ${num(float(b * k))} \\div {num(float(k))}$"),
                   R("a", num(float(b)), "A1", "cao"),
                   R("b", f"${a} \\times {num(float(k))}$", "M1", "ft their scale factor"),
                   R("b", num(float(a * k)), "A1", "cao")],
             values={"x": b, "y": float(a * k)}, diff="4-6", cw="Work out", refs=["F4.11A"])


@tpl("geometry.similarity", "short", n=7)
def similar_area_short(r):
    k = r.choice([F(3, 2), F(2), F(3), F(5, 2), F(4, 3), F(5, 3), F(4), F(5, 4)])
    a1 = r.randint(3, 40)
    l1 = r.randint(2, 15)
    shape = r.choice(["triangles", "rectangles", "pentagons", "hexagons", "kites"])
    kind = r.choice(["area", "length"])
    if kind == "area":
        a2 = a1 * k * k
        return Q(intro=f"Two {shape}, $A$ and $B$, are mathematically similar.\n\nA side of shape $A$ is {l1} cm. The corresponding side of shape $B$ is {num(float(l1 * k))} cm.\n\nThe area of shape $A$ is {a1} cm².",
                 parts=[P("", "Work out the area of shape $B$.", 2, prefix="cm²")],
                 rows=[R("", f"$\\left(\\dfrac{{{num(float(l1 * k))}}}{{{l1}}}\\right)^2 = {num(float(k * k))}$", "M1", "for the area scale factor"),
                       R("", num(float(a2)), "A1", "oe")],
                 values={"area": float(a2)}, diff="7-9", cw="Work out", refs=["H4.11A"])
    a2 = a1 * k * k
    return Q(intro=f"Two {shape}, $A$ and $B$, are mathematically similar.\n\nThe area of shape $A$ is {a1} cm². The area of shape $B$ is {num(float(a2))} cm².\n\nA side of shape $A$ is {l1} cm.",
             parts=[P("", "Work out the length of the corresponding side of shape $B$.", 2, prefix="cm")],
             rows=[R("", f"$\\sqrt{{{num(float(a2))} \\div {a1}}} = {num(float(k))}$", "M1", "for the length scale factor"),
                   R("", num(float(l1 * k)), "A1", "oe")],
             values={"length": float(l1 * k)}, diff="7-9", cw="Work out", refs=["H4.11A"])


@tpl("geometry.similarity", "problem", n=7)
def similar_volume(r):
    k = r.choice([F(3, 2), F(2), F(3), F(5, 2), F(4, 3), F(5, 3), F(5, 4), F(6, 5)])
    obj = r.choice(["bottles", "jugs", "statues", "vases", "containers", "candles"])
    s1 = r.randint(20, 400)
    v1 = r.randint(50, 2000)
    kind = r.choice(["sa_to_v", "v_to_sa", "h"])
    if kind == "sa_to_v":
        s2 = s1 * k * k
        v2 = v1 * k ** 3
        return Q(intro=f"Two {obj}, $P$ and $Q$, are mathematically similar.\n\nThe surface area of $P$ is {s1} cm². The surface area of $Q$ is {num(float(s2))} cm².\n\nThe volume of $P$ is {v1} cm³.",
                 parts=[P("", "Work out the volume of $Q$.", 4, prefix="cm³")],
                 rows=[R("", f"$\\dfrac{{{num(float(s2))}}}{{{s1}}} = {num(float(k * k))}$", "M1", "for the area scale factor"),
                       R("", f"$\\sqrt{{{num(float(k * k))}}} = {num(float(k))}$", "M1", "for the length scale factor"),
                       R("", f"${v1} \\times {num(float(k))}^3$", "M1", "for using the volume scale factor"),
                       R("", num(float(v2)), "A1", "oe")],
                 values={"volume": float(v2)}, diff="7-9", cw="Work out", refs=["H4.11C", "H4.11B"])
    if kind == "v_to_sa":
        v2 = v1 * k ** 3
        s2 = s1 * k * k
        return Q(intro=f"Two {obj}, $P$ and $Q$, are mathematically similar.\n\nThe volume of $P$ is {v1} cm³. The volume of $Q$ is {num(float(v2))} cm³.\n\nThe surface area of $P$ is {s1} cm².",
                 parts=[P("", "Work out the surface area of $Q$.", 4, prefix="cm²")],
                 rows=[R("", f"$\\dfrac{{{num(float(v2))}}}{{{v1}}} = {num(float(k ** 3))}$", "M1", "for the volume scale factor"),
                       R("", f"$\\sqrt[3]{{{num(float(k ** 3))}}} = {num(float(k))}$", "M1", ""),
                       R("", f"${s1} \\times {num(float(k))}^2$", "M1", ""),
                       R("", num(float(s2)), "A1", "oe")],
                 values={"sa": float(s2)}, diff="7-9", cw="Work out", refs=["H4.11C", "H4.11B"])
    h1 = r.randint(5, 30)
    v2 = v1 * k ** 3
    return Q(intro=f"Two {obj}, $P$ and $Q$, are mathematically similar.\n\nThe volume of $P$ is {v1} cm³ and the volume of $Q$ is {num(float(v2))} cm³.\n\nThe height of $P$ is {h1} cm.",
             parts=[P("", "Work out the height of $Q$.", 3, prefix="cm")],
             rows=[R("", f"$\\dfrac{{{num(float(v2))}}}{{{v1}}}$", "M1", ""), R("", f"$\\sqrt[3]{{{num(float(k ** 3))}}} = {num(float(k))}$", "M1", ""),
                   R("", num(float(h1 * k)), "A1", "oe")],
             values={"height": float(h1 * k)}, diff="7-9", cw="Work out", refs=["H4.11C", "H4.11B"])


@tpl("geometry.similarity", "problem", n=7)
def similar_parallel(r):
    ad = r.randint(3, 12)
    db = r.randint(2, 12)
    de = r.randint(3, 14)
    ab = ad + db
    bc = F(de * ab, ad)
    if bc.denominator > 4:
        return None
    kind = r.choice(["length", "area"])
    pts = [(0, 3.2), (-2.2, 0), (2.6, 0)]
    t = ad / ab
    D = (pts[0][0] + t * (pts[1][0] - pts[0][0]), pts[0][1] + t * (pts[1][1] - pts[0][1]))
    E = (pts[0][0] + t * (pts[2][0] - pts[0][0]), pts[0][1] + t * (pts[2][1] - pts[0][1]))

    def body(fr):
        a, b = fr(D), fr(E)
        return (L(*a, *b) + T(a[0] - 12, a[1], "D") + T(b[0] + 12, b[1], "E") + par_arrow(a, b)
                + par_arrow(fr(pts[1]), fr(pts[2])))
    s = polygon_fig(pts, names=["A", "B", "C"], extra={"body": body}, w=300, h=220)
    if kind == "length":
        return Q(intro=f"$ADB$ and $AEC$ are straight lines. $DE$ is parallel to $BC$.\n\n$AD = {ad}$ cm, $DB = {db}$ cm and $DE = {de}$ cm.",
                 figs=[fig(s, 60)], parts=[P("", "Work out the length of $BC$.", 3, prefix="cm")],
                 rows=[R("", "triangles $ADE$ and $ABC$ are similar", "M1", f"may be implied by working; scale factor $\\dfrac{{{ab}}}{{{ad}}}$"),
                       R("", f"${de} \\times \\dfrac{{{ab}}}{{{ad}}}$", "M1", ""), R("", num(float(bc)), "A1", "oe")],
                 values={"BC": float(bc)}, diff="7-9", cw="Work out", refs=["F4.11A"])
    A1 = r.randint(6, 60)
    A2 = A1 * F(ab, ad) ** 2
    trap = A2 - A1
    return Q(intro=f"$ADB$ and $AEC$ are straight lines. $DE$ is parallel to $BC$.\n\n$AD = {ad}$ cm and $DB = {db}$ cm.\n\nThe area of triangle $ADE$ is {A1} cm².",
             figs=[fig(s, 60)], parts=[P("", "Work out the area of the trapezium $DBCE$.", 4, prefix="cm²")],
             rows=[R("", f"length scale factor $= \\dfrac{{{ab}}}{{{ad}}}$", "M1", ""),
                   R("", f"area scale factor $= \\left(\\dfrac{{{ab}}}{{{ad}}}\\right)^2$", "M1", ""),
                   R("", f"${A1} \\times {ftex(F(ab, ad) ** 2)} - {A1}$", "M1", "for the area of $ABC$ minus the area of $ADE$"),
                   R("", sf(trap, 3) if F(trap).denominator > 8 else num(float(trap)), "A1", "oe")],
             values={"trapezium": float(trap)}, diff="7-9", cw="Work out", refs=["H4.11A", "H4.11C"])


# ================================================================ 5.1 vectors
def col(v):
    return f"\\begin{{pmatrix}} {num(v[0])} \\\\ {num(v[1])} \\end{{pmatrix}}"


def vtex(ca, cb, a="a", b="b"):
    """latex for ca*a + cb*b (Fractions), bold vectors."""
    out = ""
    for c, s in ((F(ca), a), (F(cb), b)):
        if c == 0:
            continue
        sign = "-" if c < 0 else "+"
        m = abs(c)
        body = ("" if m == 1 else ftex(m)) + f"\\mathbf{{{s}}}"
        out += (("-" if c < 0 else "") + body) if not out else f" {sign} {body}"
    return out or "\\mathbf{0}"


@tpl("vectors.vectors", "short", n=7)
def column_vectors(r):
    a = (r.randint(-6, 6), r.randint(-6, 6))
    b = (r.randint(-6, 6), r.randint(-6, 6))
    if 0 in a and 0 in b:
        return None
    p, q = r.choice([2, 3, 4]), r.choice([-1, -2, -3, 2, 3])
    res = (p * a[0] + q * b[0], p * a[1] + q * b[1])
    s_ = (a[0] + b[0], a[1] + b[1])
    mag = math.hypot(*s_)
    expr = f"{p}\\mathbf{{a}} {'+' if q > 0 else '-'} {abs(q) if abs(q) != 1 else ''}\\mathbf{{b}}"
    return Q(intro=f"$\\mathbf{{a}} = {col(a)}$ and $\\mathbf{{b}} = {col(b)}$",
             parts=[P("a", f"Find ${expr}$ as a column vector.", 2, prefix=""),
                    P("b", "Find $|\\mathbf{a} + \\mathbf{b}|$.\n\nGive your answer to 3 significant figures.", 2, prefix="")],
             rows=[R("a", f"$\\begin{{pmatrix}} {res[0]} \\\\ \\ldots \\end{{pmatrix}}$ or $\\begin{{pmatrix}} \\ldots \\\\ {res[1]} \\end{{pmatrix}}$", "M1", "for one correct component"),
                   R("a", f"${col(res)}$", "A1", "cao"),
                   R("b", f"$\\sqrt{{({s_[0]})^2 + ({s_[1]})^2}}$", "M1", f"for $\\mathbf{{a}} + \\mathbf{{b}} = {col(s_)}$ and Pythagoras"),
                   R("b", sf(mag, 3) if abs(mag - round(mag)) > 1e-9 else str(round(mag)), "A1", f"awrt {sf(mag, 3)}")],
             values={"res": list(res), "mag": mag}, diff="4-6", cw="Find", refs=["H5.1B", "H5.1C", "H5.1D", "H5.1E"])


@tpl("vectors.vectors", "short", n=7)
def vector_midpoint(r):
    m, n = r.choice([(1, 1), (1, 2), (2, 1), (1, 3), (3, 1), (2, 3), (3, 2), (1, 4), (3, 4)])
    pa, pb = r.choice([("a", "b"), ("p", "q"), ("a", "c"), ("u", "v")])
    ca, cb = F(n, m + n), F(m, m + n)
    desc = "is the midpoint of $AB$" if m == n else f"is the point on $AB$ such that $AM : MB = {m} : {n}$"
    return Q(intro=f"$OAB$ is a triangle.\n\n$\\overrightarrow{{OA}} = \\mathbf{{{pa}}}$ and $\\overrightarrow{{OB}} = \\mathbf{{{pb}}}$\n\n$M$ {desc}.",
             parts=[P("a", f"Find $\\overrightarrow{{AB}}$ in terms of $\\mathbf{{{pa}}}$ and $\\mathbf{{{pb}}}$.", 1, prefix="$\\overrightarrow{AB} =$"),
                    P("b", f"Find $\\overrightarrow{{OM}}$ in terms of $\\mathbf{{{pa}}}$ and $\\mathbf{{{pb}}}$. Give your answer in its simplest form.", 2, prefix="$\\overrightarrow{OM} =$")],
             rows=[R("a", f"$-\\mathbf{{{pa}}} + \\mathbf{{{pb}}}$", "B1", "oe"),
                   R("b", f"$\\mathbf{{{pa}}} + {ftex(F(m, m + n))}(-\\mathbf{{{pa}}} + \\mathbf{{{pb}}})$", "M1", "for a correct vector path"),
                   R("b", f"${vtex(ca, cb, pa, pb)}$", "A1", "oe, simplified")],
             values={"OM_a": ca, "OM_b": cb}, diff="4-6", cw="Find", refs=["H5.1F", "H5.1D"])


@tpl("vectors.vectors", "proof", n=7)
def vector_collinear(r):
    p, q = r.choice([(1, 2), (2, 1), (1, 3), (3, 1), (2, 3), (3, 2), (1, 1)])
    k = r.choice([F(1, 2), F(1, 3), F(2, 3), F(1, 4), F(3, 4), F(2, 5), F(3, 5)])
    s_ = F(q, p + q)  # coefficient of a in OM
    if k == s_:
        return None
    sc = k / (k - s_)
    t = sc * F(p, p + q)
    if t <= 0 or t.denominator > 4 or t == 1:
        return None
    # N on OA with ON = k a; M on AB, AM:MB = p:q; X on OB (extended) with OX = t b
    NM = (s_ - k, F(p, p + q))
    MX = (-s_, t - F(p, p + q))
    lam = MX[1] / NM[1]
    where = "the line $OB$ extended" if t > 1 else "$OB$"
    return Q(intro=(f"$OAB$ is a triangle.\n\n$\\overrightarrow{{OA}} = \\mathbf{{a}}$ and $\\overrightarrow{{OB}} = \\mathbf{{b}}$\n\n"
                    f"$N$ is the point on $OA$ such that $ON = {ftex(k)}OA$.\n\n$M$ is the point on $AB$ such that $AM : MB = {p} : {q}$.\n\n"
                    f"$X$ is the point on {where} such that $\\overrightarrow{{OX}} = {vtex(0, t)}$."),
             parts=[P("", "Use a vector method to prove that $N$, $M$ and $X$ lie on a straight line.", 4, space="working")],
             rows=[R("", f"$\\overrightarrow{{OM}} = {vtex(s_, F(p, p + q))}$", "M1", "for a correct vector for $\\overrightarrow{OM}$ or $\\overrightarrow{AM}$"),
                   R("", f"$\\overrightarrow{{NM}} = {vtex(*NM)}$", "M1", "for a correct vector for $\\overrightarrow{NM}$, $\\overrightarrow{MX}$ or $\\overrightarrow{NX}$"),
                   R("", f"$\\overrightarrow{{MX}} = {vtex(*MX)} = {ftex(lam)}\\left({vtex(*NM)}\\right)$", "M1", "for two vectors shown to be multiples of each other"),
                   R("", "$\\overrightarrow{MX}$ is a multiple of $\\overrightarrow{NM}$ and $M$ is a common point, so $N$, $M$ and $X$ are collinear", "A1",
                     "dep on M3; must mention the common point (or shared vector) and parallel")],
             values={"lambda": lam, "t": t}, diff="7-9", cw="Prove", refs=["H5.1G", "H5.1F"])


@tpl("vectors.vectors", "proof", n=7)
def vector_parallel(r):
    m, n = r.choice([(1, 2), (2, 1), (1, 3), (3, 1), (2, 3), (3, 2), (1, 4), (3, 5), (2, 5)])
    pa, pb = r.choice([("a", "b"), ("p", "q"), ("u", "v")])
    k = r.randint(2, 4)
    # OAB triangle, OA = k a ... P on OA with OP:PA = m:n, Q on OB with OQ:QB = m:n
    f_ = F(m, m + n)
    ca = k
    return Q(intro=(f"$OAB$ is a triangle.\n\n$\\overrightarrow{{OA}} = {k}\\mathbf{{{pa}}}$ and $\\overrightarrow{{OB}} = {k}\\mathbf{{{pb}}}$\n\n"
                    f"$P$ is the point on $OA$ such that $OP : PA = {m} : {n}$.\n\n$Q$ is the point on $OB$ such that $OQ : QB = {m} : {n}$."),
             parts=[P("a", "Show that $PQ$ is parallel to $AB$.", 3, space="working"),
                    P("b", "Write down the ratio $PQ : AB$.", 1, prefix="")],
             rows=[R("a", f"$\\overrightarrow{{AB}} = -{k}\\mathbf{{{pa}}} + {k}\\mathbf{{{pb}}}$", "M1", ""),
                   R("a", f"$\\overrightarrow{{PQ}} = {vtex(-k * f_, k * f_, pa, pb)}$", "M1", ""),
                   R("a", f"$\\overrightarrow{{PQ}} = {ftex(f_)}\\overrightarrow{{AB}}$ so $PQ$ is parallel to $AB$", "A1", "dep on M2; conclusion required"),
                   R("b", f"${m} : {m + n}$", "B1", "oe")],
             values={"ratio": f"{m}:{m + n}"}, diff="7-9", cw="Show that", refs=["H5.1G", "H5.1C"])


@tpl("vectors.vectors", "structured", n=14)
def vector_struct(r):
    m, n = r.choice([(1, 2), (2, 1), (1, 3), (3, 1), (2, 3), (3, 2), (1, 1)])
    k = r.choice([2, 3, F(3, 2), F(1, 2)])
    # OABC trapezium: OA = a, OC = c, CB = k a.  M on AB with AM:MB = m:n
    fA = F(m, m + n)
    # AB = -a + c + k a = (k-1) a + c
    AB = (F(k) - 1, F(1))
    OM = (1 + fA * AB[0], fA * AB[1])
    # X on OM extended meets CB extended?  ask CM
    CM = (OM[0], OM[1] - 1)
    shape = "parallelogram" if k == 1 else "trapezium"
    return Q(intro=(f"$OABC$ is a {shape}.\n\n$\\overrightarrow{{OA}} = \\mathbf{{a}}$, $\\overrightarrow{{OC}} = \\mathbf{{c}}$ and "
                    f"$\\overrightarrow{{CB}} = {vtex(k, 0)}$\n\n$M$ is the point on $AB$ such that $AM : MB = {m} : {n}$."),
             parts=[P("a", "Find, in terms of $\\mathbf{a}$ and $\\mathbf{c}$, the vector $\\overrightarrow{OB}$.", 1, prefix=""),
                    P("b", "Find, in terms of $\\mathbf{a}$ and $\\mathbf{c}$, the vector $\\overrightarrow{AB}$.", 1, prefix=""),
                    P("c", "Find, in terms of $\\mathbf{a}$ and $\\mathbf{c}$, the vector $\\overrightarrow{OM}$. Give your answer in its simplest form.", 2, prefix=""),
                    P("d", "Find, in terms of $\\mathbf{a}$ and $\\mathbf{c}$, the vector $\\overrightarrow{CM}$. Give your answer in its simplest form.", 2, prefix="")],
             rows=[R("a", f"${vtex(k, 1, 'a', 'c')}$", "B1", "oe"),
                   R("b", f"${vtex(*AB, 'a', 'c')}$", "B1", "oe"),
                   R("c", f"$\\mathbf{{a}} + {ftex(fA)}\\left({vtex(*AB, 'a', 'c')}\\right)$", "M1", "ft their (b)"),
                   R("c", f"${vtex(*OM, 'a', 'c')}$", "A1", "oe, simplified"),
                   R("d", f"$-\\mathbf{{c}} + \\overrightarrow{{OM}}$", "M1", "ft their (c)"),
                   R("d", f"${vtex(*CM, 'a', 'c')}$", "A1", "oe")],
             values={"OM": [OM[0], OM[1]], "CM": [CM[0], CM[1]]}, diff="7-9", cw="Find", refs=["H5.1D", "H5.1F", "H5.1C"])


# ================================================================ 5.2 transformations
SHAPES = [[(0, 0), (2, 0), (0, 3)], [(0, 0), (3, 0), (3, 1), (1, 2)], [(0, 0), (2, 0), (2, 1), (1, 1), (1, 3), (0, 3)],
          [(0, 0), (3, 0), (1, 2)], [(0, 0), (1, 0), (1, 2), (3, 2), (3, 3), (0, 3)], [(0, 0), (2, 1), (1, 3)]]


def apply(kind, pts, prm):
    out = []
    for x, y in pts:
        if kind == "trans":
            out.append((x + prm[0], y + prm[1]))
        elif kind == "refl":
            ln = prm
            if ln[0] == "x":
                out.append((2 * ln[1] - x, y))
            elif ln[0] == "y":
                out.append((x, 2 * ln[1] - y))
            elif ln[0] == "y=x":
                out.append((y, x))
            else:
                out.append((-y, -x))
        elif kind == "rot":
            (a, b), ang = prm
            dx, dy = x - a, y - b
            if ang == 90:
                out.append((a - dy, b + dx))
            elif ang == -90:
                out.append((a + dy, b - dx))
            else:
                out.append((a - dx, b - dy))
        else:
            (a, b), k = prm
            out.append((a + k * (x - a), b + k * (y - b)))
    return out


def line_text(ln):
    if ln[0] == "x":
        return f"x = {ln[1]}"
    if ln[0] == "y":
        return f"y = {ln[1]}"
    return "y = x" if ln[0] == "y=x" else "y = -x"


def describe(kind, prm):
    if kind == "trans":
        return f"translation by the vector ${col(prm)}$", ["translation", f"vector ${col(prm)}$"]
    if kind == "refl":
        return f"reflection in the line ${line_text(prm)}$", ["reflection", f"in the line ${line_text(prm)}$"]
    if kind == "rot":
        (a, b), ang = prm
        dirn = {90: "$90^\\circ$ anticlockwise", -90: "$90^\\circ$ clockwise", 180: "$180^\\circ$"}[ang]
        return f"rotation {dirn} about $({a}, {b})$", ["rotation", f"{dirn} and centre $({a}, {b})$"]
    (a, b), k = prm
    return f"enlargement, scale factor ${ftex(k)}$, centre $({a}, {b})$", ["enlargement", f"scale factor ${ftex(k)}$ and centre $({a}, {b})$"]


def in_box(pts, lo=-6, hi=6):
    return all(lo <= x <= hi and lo <= y <= hi for x, y in pts)


def shapes_grid(polys, labels, lo=-6, hi=6):
    def items(M):
        out = ""
        for pts, lab in zip(polys, labels):
            if not pts:
                continue
            S = [M(p) for p in pts]
            out += PL(S, close=True, w=2)
            cx = sum(p[0] for p in pts) / len(pts)
            cy = sum(p[1] for p in pts) / len(pts)
            X, Y = M((cx, cy))
            out += T(X, Y, lab, size=13, weight="bold")
        return out
    return grid_fig(lo, hi, lo, hi, items=items, w=330, h=330)


def rand_transform(r, allow=("trans", "refl", "rot", "enl")):
    kind = r.choice(allow)
    if kind == "trans":
        prm = (r.randint(-7, 7), r.randint(-7, 7))
        if prm[0] == 0 or prm[1] == 0:
            return None
    elif kind == "refl":
        prm = r.choice([("x", r.randint(-2, 2)), ("y", r.randint(-2, 2)), ("y=x", 0), ("y=-x", 0)])
    elif kind == "rot":
        prm = ((r.randint(-2, 2), r.randint(-2, 2)), r.choice([90, -90, 180]))
    else:
        prm = ((r.randint(-5, 2), r.randint(-5, 2)), r.choice([2, 3, F(1, 2), F(1, 3)]))
    return kind, prm


@tpl("vectors.transformations", "graph", n=7)
def describe_transform(r):
    t = rand_transform(r)
    if t is None:
        return None
    kind, prm = t
    base = r.choice(SHAPES)
    if kind == "enl" and F(prm[1]) < 1:
        base = [(x * 3, y * 3) for x, y in base[:4]] if len(base) <= 4 else None
        if base is None:
            return None
    ox, oy = r.randint(-5, 4), r.randint(-5, 4)
    A = [(x + ox, y + oy) for x, y in base]
    B = apply(kind, A, prm)
    if not (in_box(A) and in_box(B)) or set(A) == set(B):
        return None
    if any(F(c).denominator != 1 for p in B for c in p):
        return None
    s = shapes_grid([A, B], ["A", "B"])
    full, bits = describe(kind, prm)
    marks = 2 if kind in ("trans", "refl") else 3
    rows = [R("", bits[0], "B1", "")]
    if marks == 2:
        rows.append(R("", bits[1], "B1", "a single transformation must be given; B0 for a combination"))
    else:
        rows.append(R("", bits[1].split(" and ")[0], "B1", ""))
        rows.append(R("", bits[1].split(" and ")[1], "B1", "a combination of transformations scores B0"))
    return Q(intro="Shape $A$ and shape $B$ are drawn on the grid.", figs=[fig(s, 75, note=None)],
             parts=[P("", "Give a full description of the single transformation that takes shape $A$ to shape $B$.", marks, space="lines", lines=2)],
             rows=rows, values={"transformation": full}, diff="4-6" if marks == 2 else "7-9", cw="Describe", refs=["F5.2M"],
             method="coordinates transformed exactly")


@tpl("vectors.transformations", "graph", n=7)
def draw_transform(r):
    t = rand_transform(r, ("rot", "refl", "enl", "enl"))
    if t is None:
        return None
    kind, prm = t
    base = r.choice(SHAPES[:4])
    if kind == "enl" and F(prm[1]) < 1:
        base = [(x * 2 if F(prm[1]) == F(1, 2) else x * 3, y * 2 if F(prm[1]) == F(1, 2) else y * 3) for x, y in base]
    ox, oy = r.randint(-5, 4), r.randint(-5, 4)
    A = [(x + ox, y + oy) for x, y in base]
    B = apply(kind, A, prm)
    if not (in_box(A) and in_box(B)) or set(A) == set(B):
        return None
    if any(F(c).denominator != 1 for p in B for c in p):
        return None
    s = shapes_grid([A], ["P"])
    full, _ = describe(kind, prm)
    if kind == "rot":
        instr = f"Rotate shape $P$ {full.split('rotation ')[1]}."
    elif kind == "refl":
        instr = f"Reflect shape $P$ in the line ${line_text(prm)}$."
    else:
        instr = f"Enlarge shape $P$ with scale factor ${ftex(prm[1])}$ and centre $({prm[0][0]}, {prm[0][1]})$."
    verts = ", ".join(f"$({int(x)}, {int(y)})$" for x, y in B)
    return Q(intro="Shape $P$ is drawn on the grid.", figs=[fig(s, 75, note=None)],
             parts=[P("", instr + "\n\nLabel the new shape $Q$.", 2, space="none")],
             rows=[R("", f"shape with vertices {verts}", "B2", "B1 for a shape of the correct size and orientation in the wrong position, or for "
                     + ("an enlargement with the correct scale factor but wrong centre" if kind == "enl" else "a correct transformation with one error"))],
             values={"vertices": [[int(x), int(y)] for x, y in B]}, diff="4-6", cw="Draw",
             refs={"rot": ["F5.2B"], "refl": ["F5.2E"], "enl": ["F5.2L"]}[kind], method="coordinates transformed exactly")


@tpl("vectors.transformations", "short", n=7)
def transform_point(r):
    t = rand_transform(r)
    if t is None:
        return None
    kind, prm = t
    p = (r.randint(-6, 6), r.randint(-6, 6))
    img = apply(kind, [p], prm)[0]
    if img == p or any(F(c).denominator != 1 for c in img):
        return None
    full, _ = describe(kind, prm)
    return Q(parts=[P("", f"The point $A$ has coordinates $({p[0]}, {p[1]})$.\n\n$A$ is mapped to the point $B$ by a {full.replace('enlargement, ', 'enlargement with ').replace(', centre', ' and centre')}.\n\nWrite down the coordinates of $B$.", 2, prefix="")],
             rows=[R("", f"$({num(F(img[0]))}, {num(F(img[1]))})$", "B2", "B1 for one correct coordinate")],
             values={"B": [num(F(img[0])), num(F(img[1]))]}, diff="4-6", cw="Write down",
             refs={"trans": ["F5.2H"], "refl": ["F5.2E"], "rot": ["F5.2B"], "enl": ["F5.2L"]}[kind])


@tpl("vectors.transformations", "short", n=7)
def combined_transform(r):
    t1 = rand_transform(r, ("refl", "rot"))
    t2 = rand_transform(r, ("refl", "rot", "trans"))
    if t1 is None or t2 is None:
        return None
    test = [(1, 0), (0, 1), (2, 3), (0, 0)]
    out = apply(t2[0], apply(t1[0], test, t1[1]), t2[1])
    # identify a single transformation matching the composite
    found = None
    cands = [("trans", (a, b)) for a in range(-12, 13) for b in range(-12, 13) if (a, b) != (0, 0)]
    cands += [("refl", ln) for ln in [("x", k / 2) for k in range(-12, 13)] + [("y", k / 2) for k in range(-12, 13)] + [("y=x", 0), ("y=-x", 0)]]
    cands += [("rot", ((F(a, 2), F(b, 2)), ang)) for a in range(-12, 13) for b in range(-12, 13) for ang in (90, -90, 180)]
    for kind, prm in cands:
        if apply(kind, test, prm) == out:
            found = (kind, prm)
            break
    if found is None:
        return None
    kind, prm = found
    if kind == "rot" and any(F(c).denominator != 1 for c in prm[0]):
        return None
    if kind == "refl" and F(prm[1]).denominator != 1:
        return None
    if kind == "refl":
        prm = (prm[0], int(prm[1]))
    if kind == "rot":
        prm = ((int(prm[0][0]), int(prm[0][1])), prm[1])
    d1, _ = describe(*t1)
    d2, _ = describe(*t2)
    full, bits = describe(kind, prm)
    marks = 3 if kind == "rot" else 2
    rows = [R("", bits[0], "B1", "")]
    if marks == 2:
        rows.append(R("", bits[1], "B1", ""))
    else:
        rows += [R("", bits[1].split(" and ")[0], "B1", ""), R("", bits[1].split(" and ")[1], "B1", "")]
    return Q(intro=f"Shape $S$ is mapped onto shape $T$ by a {d1}.\n\nShape $T$ is mapped onto shape $U$ by a {d2}.",
             parts=[P("", "Give a full description of the single transformation that takes shape $S$ to shape $U$.", marks, space="lines", lines=2)],
             rows=rows, values={"transformation": full}, diff="7-9", cw="Describe", refs=["F5.2M", "F5.2B", "F5.2E"],
             method="composition checked on test points")
