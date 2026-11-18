"""Equation list printed with 4PH1 papers -> data/reference/physics-equations.json (own layout)."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

GROUPS = [
    ("1. Forces and motion", [
        "average speed = distance moved ÷ time taken",
        "acceleration = change in velocity ÷ time taken    $a = \\dfrac{(v - u)}{t}$",
        "(final speed)² = (initial speed)² + (2 × acceleration × distance moved)    $v^2 = u^2 + (2 \\times a \\times s)$",
        "force = mass × acceleration    $F = m \\times a$",
        "weight = mass × gravitational field strength    $W = m \\times g$"]),
    ("2. Electricity", [
        "power = current × voltage    $P = I \\times V$",
        "energy transferred = current × voltage × time    $E = I \\times V \\times t$",
        "voltage = current × resistance    $V = I \\times R$",
        "charge = current × time    $Q = I \\times t$",
        "energy transferred = charge × voltage    $E = Q \\times V$"]),
    ("3. Waves", [
        "wave speed = frequency × wavelength    $v = f \\times \\lambda$",
        "frequency = 1 ÷ time period    $f = \\dfrac{1}{T}$",
        "refractive index = sin(angle of incidence) ÷ sin(angle of refraction)    $n = \\dfrac{\\sin i}{\\sin r}$",
        "sin(critical angle) = 1 ÷ refractive index    $\\sin c = \\dfrac{1}{n}$"]),
    ("4. Energy resources and energy transfers", [
        "efficiency = (useful energy output ÷ total energy output) × 100%",
        "work done = force × distance moved    $W = F \\times d$",
        "gravitational potential energy = mass × gravitational field strength × height    $GPE = m \\times g \\times h$",
        "kinetic energy = ½ × mass × speed²    $KE = \\frac{1}{2} \\times m \\times v^2$",
        "power = work done ÷ time taken    $P = \\dfrac{W}{t}$"]),
    ("5. Solids, liquids and gases", [
        "density = mass ÷ volume    $\\rho = \\dfrac{m}{V}$",
        "pressure = force ÷ area    $p = \\dfrac{F}{A}$",
        "pressure difference = height × density × gravitational field strength    $p = h \\times \\rho \\times g$",
        "pressure ÷ temperature = constant    $\\dfrac{p_1}{T_1} = \\dfrac{p_2}{T_2}$",
        "pressure × volume = constant    $p_1 \\times V_1 = p_2 \\times V_2$"]),
    ("8. Astrophysics", [
        "orbital speed = (2 × π × orbital radius) ÷ time period    $v = \\dfrac{2 \\times \\pi \\times r}{T}$"]),
    ("Paper 2 only: additional equations", [
        "momentum = mass × velocity    $p = m \\times v$",
        "force = change in momentum ÷ time taken    $F = \\dfrac{(mv - mu)}{t}$",
        "moment = force × perpendicular distance from the pivot",
        "change in thermal energy = mass × specific heat capacity × change in temperature    $\\Delta Q = m \\times c \\times \\Delta T$",
        "input (primary) voltage ÷ output (secondary) voltage = primary turns ÷ secondary turns    $\\dfrac{V_p}{V_s} = \\dfrac{n_p}{n_s}$",
        "input power = output power (for 100% efficiency)    $V_p I_p = V_s I_s$",
        "change in wavelength ÷ reference wavelength = velocity of a galaxy ÷ speed of light    $\\dfrac{\\lambda - \\lambda_0}{\\lambda_0} = \\dfrac{\\Delta\\lambda}{\\lambda_0} = \\dfrac{v}{c}$"]),
]


def build():
    blocks = [{"type": "source", "label": "Equation list",
               "text": "You may find these equations useful. Where necessary, take g = 10 N/kg (10 m/s²)."}]
    for title, eqs in GROUPS:
        blocks.append({"type": "source", "label": title, "text": "\n".join(eqs)})
    return {"id": "physics-equations", "title": "Physics equation list", "blocks": blocks}


def write():
    d = ROOT / "data" / "reference"
    d.mkdir(parents=True, exist_ok=True)
    (d / "physics-equations.json").write_text(json.dumps(build(), ensure_ascii=False, indent=1))


if __name__ == "__main__":
    write()
