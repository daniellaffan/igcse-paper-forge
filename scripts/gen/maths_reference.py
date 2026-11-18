"""Writes data/reference/maths-formulae-higher.json: our own layout of the
formulae that the Higher-tier papers print on page 2."""
import json
import math
from pathlib import Path

from maths_util import svg, PL, L, T, C, ARC, right_mark

ROOT = Path(__file__).resolve().parents[2]


def _trap():
    b = PL([(40, 100), (200, 100), (160, 30), (75, 30)], close=True)
    b += L(110, 30, 110, 100, dash="4,3") + right_mark((110, 100), (110, 30), (200, 100), s=7)
    b += T(118, 34, "a", it=True) + T(120, 112, "b", it=True) + T(102, 66, "h", it=True)
    return svg(240, 125, b)


def _tri():
    A, B, Cc = (30, 110), (210, 110), (150, 25)
    b = PL([A, B, Cc], close=True) + T(20, 116, "A") + T(220, 116, "B") + T(152, 14, "C")
    b += T(120, 124, "c", it=True) + T(188, 64, "a", it=True) + T(80, 62, "b", it=True)
    return svg(240, 132, b)


def _cone():
    b = '<ellipse cx="80" cy="120" rx="50" ry="13"/>' + L(30, 120, 80, 20) + L(130, 120, 80, 20)
    b += L(80, 20, 80, 120, dash="4,3") + L(80, 120, 130, 120, dash="4,3")
    b += T(72, 72, "h", it=True) + T(105, 130, "r", it=True) + T(112, 66, "l", it=True)
    return svg(170, 145, b)


def _sphere():
    b = C(70, 70, 50) + '<path d="M20,70 A50,12 0 0 0 120,70"/>' + L(70, 70, 120, 70) + T(95, 62, "r", it=True)
    return svg(140, 135, b)


def _cyl():
    b = '<ellipse cx="70" cy="25" rx="45" ry="11"/><ellipse cx="70" cy="115" rx="45" ry="11"/>'
    b += L(25, 25, 25, 115) + L(115, 25, 115, 115) + L(70, 25, 115, 25, dash="4,3")
    b += T(92, 16, "r", it=True) + T(125, 70, "h", it=True)
    return svg(150, 135, b)


def _prism():
    f = [(20, 125), (90, 125), (90, 75), (55, 50), (20, 75)]
    dx, dy = 75, -35
    b = PL(f, close=True)
    for p in f[1:]:
        b += L(p[0], p[1], p[0] + dx, p[1] + dy)
    b += PL([(p[0] + dx, p[1] + dy) for p in f[1:]])
    b += T(55, 95, "cross", size=10) + T(55, 107, "section", size=10) + T(150, 108, "length", size=11)
    return svg(200, 135, b)


def build():
    blocks = [
        {"type": "source", "label": "Arithmetic series",
         "text": "Sum to $n$ terms: $S_n = \\dfrac{n}{2}\\left[2a + (n-1)d\\right]$"},
        {"type": "source", "label": "The quadratic equation",
         "text": "If $ax^2 + bx + c = 0$ with $a \\ne 0$, then $x = \\dfrac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}$"},
        {"type": "svg", "svg": _trap(), "width": 45, "caption": "Area of trapezium $= \\frac{1}{2}(a + b)h$"},
        {"type": "svg", "svg": _tri(), "width": 45,
         "caption": "In any triangle $ABC$: sine rule $\\dfrac{a}{\\sin A} = \\dfrac{b}{\\sin B} = \\dfrac{c}{\\sin C}$; "
                    "cosine rule $a^2 = b^2 + c^2 - 2bc\\cos A$; area of triangle $= \\frac{1}{2}ab\\sin C$"},
        {"type": "svg", "svg": _prism(), "width": 40, "caption": "Volume of prism $=$ area of cross section $\\times$ length"},
        {"type": "svg", "svg": _cyl(), "width": 32,
         "caption": "Volume of cylinder $= \\pi r^2 h$; curved surface area of cylinder $= 2\\pi r h$"},
        {"type": "svg", "svg": _cone(), "width": 34,
         "caption": "Volume of cone $= \\frac{1}{3}\\pi r^2 h$; curved surface area of cone $= \\pi r l$"},
        {"type": "svg", "svg": _sphere(), "width": 30,
         "caption": "Volume of sphere $= \\frac{4}{3}\\pi r^3$; surface area of sphere $= 4\\pi r^2$"},
    ]
    ref = {"id": "maths-formulae-higher", "title": "Formulae sheet – Higher Tier", "blocks": blocks}
    out = ROOT / "data" / "reference" / "maths-formulae-higher.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(ref, ensure_ascii=False, indent=1))
