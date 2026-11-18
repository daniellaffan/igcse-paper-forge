"""Topic 5: Solids, liquids and gases."""
import physics_svg as S
from physics_util import (K, M, X, T, kb, calc_q, line_part, work_part, row, num, sf, clean, pick, nice, alts)

DE, ST, GA = ("physics.matter.density", "physics.matter.state", "physics.matter.gases")

kb(DE, ["density of materials", "floating and sinking", "pressure under water", "pressure on surfaces", "measuring density"],
   mcq=[
       M("What is the unit of density?", ["kg/m³", "kg/m²", "N/m²", "kg m³"], "5.1 5.3"),
       M("What is the unit of pressure?", ["pascal", "newton", "joule", "watt"], "5.1 5.5"),
       M("A block has a mass of 6 kg and a volume of 0.002 m³. What is its density?", ["3000 kg/m³", "0.012 kg/m³", "333 kg/m³", "12 kg/m³"], "5.3", ao="AO2", d="4-6"),
       M("A force of 50 N acts on an area of 0.5 m². What is the pressure?", ["100 Pa", "25 Pa", "50.5 Pa", "0.01 Pa"], "5.5", ao="AO2"),
       M("Pressure at a point in a liquid at rest", ["acts equally in all directions", "acts only downwards", "acts only upwards", "is zero at the bottom"], "5.6"),
       M("Why do snowshoes stop a person sinking into snow?", ["they spread the weight over a larger area, reducing pressure", "they reduce the person's weight", "they increase the pressure", "they reduce friction"], "5.5", d="4-6"),
       M("The pressure in a liquid increases with", ["depth and density", "volume only", "surface area", "the shape of the container"], "5.7", d="4-6"),
       M("Which piece of apparatus is used to find the volume of an irregular stone?", ["a displacement (eureka) can and measuring cylinder", "a metre rule", "a balance", "a newtonmeter"], "5.4"),
   ],
   recall=[
       K("State the equation linking density, mass and volume.", 1, ["density = mass ÷ volume | allow ρ = m ÷ V"], "5.3", cmd="State"),
       K("State the equation linking pressure, force and area.", 1, ["pressure = force ÷ area | allow p = F ÷ A"], "5.5", cmd="State"),
       K("State the equation linking pressure difference, height, density and g.", 1, ["pressure difference = height × density × g | allow p = h × ρ × g"], "5.7", cmd="State"),
       K("Name the apparatus used to measure the mass of a stone.", 1, ["(top-pan / electronic) balance"], "5.4", cmd="Name"),
       K("State the unit of pressure in terms of newtons and metres.", 1, ["N/m² | allow N m⁻²"], "5.1", cmd="State"),
       K("State how the pressure on a diver changes as she swims deeper.", 1, ["it increases"], "5.7", cmd="State"),
   ],
   explain=[
       K("Explain why a sharp knife cuts more easily than a blunt one.", 2, ["sharp edge has a smaller area", "so the same force gives a greater pressure"], "5.5", cmd="Explain"),
       K("Explain why a dam is built thicker at the bottom than at the top.", 2, ["pressure increases with depth", "so the force on the bottom of the dam is greatest"], "5.7", cmd="Explain"),
       K("Explain why tractors have wide tyres.", 2, ["larger area in contact with the ground", "reduces pressure so the tractor does not sink into soft ground"], "5.5", cmd="Explain"),
       K("Explain why water spurts furthest from the lowest hole in the side of a tall can.", 2, ["pressure is greatest at the greatest depth", "so the force pushing water out is largest there"], "5.7", cmd="Explain", d="4-6"),
       K("Explain why a block of wood floats on water but a block of iron sinks.", 2, ["wood is less dense than water", "iron is denser than water"], "5.3", cmd="Explain", d="4-6"),
       K("Explain why a submarine needs a strong hull to dive deep.", 2, ["water pressure increases with depth (p = hρg)", "large pressure difference across the hull"], "5.7", cmd="Explain", d="7-9"),
   ])

kb(ST, ["melting and boiling", "particles in solids, liquids and gases", "heating water", "cooling curves", "specific heat capacity"],
   mcq=[
       M("In which state are particles close together and vibrate about fixed positions?", ["solid", "liquid", "gas", "plasma"], "5.10P"),
       M("While ice is melting at 0 °C, its temperature", ["stays the same", "rises steadily", "falls", "rises then falls"], "5.8P 5.9P"),
       M("What is the unit of specific heat capacity?", ["J/kg °C", "J/kg", "J °C", "kg/J °C"], "5.2P"),
       M("How much energy is needed to raise the temperature of 2 kg of water by 5 °C? (c = 4200 J/kg °C)", ["42 000 J", "8400 J", "21 000 J", "4200 J"], "5.13P", ao="AO2", d="4-6"),
       M("Evaporation cools a liquid because", ["the fastest particles escape from the surface", "the slowest particles escape", "all particles slow down", "particles gain energy"], "5.9P", d="7-9"),
       M("When a substance boils, the energy supplied", ["breaks bonds between particles", "increases the average speed of particles", "is destroyed", "lowers the internal energy"], "5.8P 5.9P", d="7-9"),
       M("In which state are particles far apart and moving randomly at high speed?", ["gas", "liquid", "solid", "all states"], "5.10P"),
   ],
   recall=[
       K("State what is meant by *specific heat capacity*.", 2, ["energy needed to raise the temperature of 1 kg", "by 1 °C"], "5.12P", cmd="State"),
       K("State the equation linking change in thermal energy, mass, specific heat capacity and temperature change.", 1, ["ΔQ = m × c × ΔT"], "5.13P", cmd="State"),
       K("Describe the arrangement of particles in a liquid.", 2, ["close together", "randomly arranged / can move past each other"], "5.10P", cmd="Describe"),
       K("Name the change of state from liquid to gas.", 1, ["evaporation / boiling"], "5.9P", cmd="Name"),
       K("State what happens to the internal energy of a substance when it is heated.", 1, ["it increases"], "5.8P", cmd="State"),
       K("State **two** differences between evaporation and boiling.", 2, ["evaporation happens at any temperature; boiling only at boiling point", "evaporation only at the surface; boiling throughout the liquid", "boiling forms bubbles"], "5.9P", cmd="State", d="4-6"),
   ],
   describe=[
       K("Compare how the particles move in each of the three states of matter.", 3, ["solid: vibrate about fixed positions", "liquid: move around each other / slide past", "gas: move quickly in random directions"], "5.10P", cmd="Describe"),
       K("Describe what happens to the particles when a solid melts.", 2, ["particles gain energy and vibrate more", "break free from fixed positions / bonds weaken"], "5.9P", cmd="Describe"),
       K("Describe how a temperature-time graph for cooling stearic acid shows the change of state.", 2, ["temperature falls, then stays constant (flat section) at the melting point", "then falls again once solid"], "5.11P", cmd="Describe", d="4-6"),
       K("Describe how the particles in a gas change when it condenses.", 2, ["particles lose energy / move more slowly", "come closer together and form a liquid"], "5.9P 5.10P", cmd="Describe"),
   ],
   explain=[
       K("Explain why the temperature of boiling water stays at 100 °C even though it is still being heated.", 2, ["energy is used to overcome forces between particles / change state", "not to increase the kinetic energy of the particles"], "5.8P 5.9P", cmd="Explain", d="7-9"),
       K("Explain why sweating helps to cool the body.", 2, ["sweat evaporates", "fastest particles escape, lowering average kinetic energy/temperature of what remains"], "5.9P", cmd="Explain", d="7-9"),
       K("Explain why gases can be compressed but solids cannot.", 2, ["gas particles are far apart with large spaces", "solid particles are already touching"], "5.10P", cmd="Explain"),
       K("Explain why water is used in central heating systems.", 2, ["water has a high specific heat capacity", "stores a lot of energy for each degree of temperature"], "5.12P", cmd="Explain", d="4-6"),
       K("Explain why a metal block heats up faster than the same mass of water with the same heater.", 2, ["metal has a lower specific heat capacity", "less energy needed per °C so temperature rises faster"], "5.12P 5.13P", cmd="Explain", d="7-9"),
   ],
   extended=[
       X("Describe an experiment to measure the specific heat capacity of a metal block. Include how you would calculate the result and how to improve accuracy.",
         ["use a metal block of known mass (balance)", "insert an electric heater and thermometer in the holes", "measure starting temperature", "switch on heater for a measured time",
          "measure energy supplied with a joulemeter or from V × I × t", "record the final/highest temperature", "c = ΔQ ÷ (m × ΔT)", "wrap the block in insulation", "add oil to thermometer hole for good contact",
          "repeat and average"], "5.14P 5.13P"),
       X("Explain, in terms of particles, what happens as a block of ice at -10 °C is heated until it becomes steam at 110 °C.",
         ["ice: particles vibrate in fixed positions; heating makes them vibrate more and temperature rises", "at 0 °C energy breaks bonds; temperature constant while melting",
          "liquid: particles move around each other; temperature rises", "average kinetic energy increases with temperature", "some evaporation from surface",
          "at 100 °C energy separates particles completely; temperature constant during boiling", "steam: particles far apart, moving fast and randomly", "internal energy increases throughout",
          "flat sections on a temperature-time graph"], "5.8P 5.9P 5.10P"),
   ])

kb(GA, ["gas in a container", "pumping a tyre", "absolute zero", "gas syringes", "weather balloons"],
   mcq=[
       M("What is absolute zero on the Celsius scale?", ["-273 °C", "0 °C", "-100 °C", "273 °C"], "5.16"),
       M("A temperature of 27 °C is equal to", ["300 K", "246 K", "27 K", "-246 K"], "5.17", ao="AO2"),
       M("Gas pressure is caused by", ["molecules colliding with the container walls", "molecules sticking to the walls", "gravity pulling the gas down", "molecules colliding only with each other"], "5.15"),
       M("When a gas is heated in a sealed container, its molecules", ["move faster on average", "become larger", "move more slowly", "stop colliding"], "5.18"),
       M("The volume of a gas is halved at constant temperature. Its pressure", ["doubles", "halves", "stays the same", "quadruples"], "5.20 5.22", d="4-6"),
       M("The Kelvin temperature of a gas is proportional to", ["the average kinetic energy of its molecules", "its volume only", "the number of molecules", "the size of the molecules"], "5.19", d="4-6"),
       M("A gas at constant volume is heated from 200 K to 400 K. Its pressure", ["doubles", "halves", "increases by 200 Pa", "stays the same"], "5.21", d="7-9", ao="AO2"),
   ],
   recall=[
       K("State what is meant by *absolute zero*.", 1, ["temperature at which particles have the least (no) kinetic energy / stop moving | allow -273 °C or 0 K"], "5.16", cmd="State"),
       K("Convert 50 °C to kelvin.", 1, ["323 K"], "5.17", cmd="Convert", ao="AO2"),
       K("Convert 200 K to degrees Celsius.", 1, ["-73 °C"], "5.17", cmd="Convert", ao="AO2"),
       K("State the equation linking pressure and volume for a fixed mass of gas at constant temperature.", 1, ["p₁V₁ = p₂V₂"], "5.22", cmd="State"),
       K("State the equation linking pressure and Kelvin temperature for a fixed mass of gas at constant volume.", 1, ["p₁ ÷ T₁ = p₂ ÷ T₂"], "5.21", cmd="State"),
       K("Describe the motion of molecules in a gas.", 2, ["random", "constant/high speed in straight lines between collisions"], "5.15", cmd="Describe"),
   ],
   explain=[
       K("Explain, in terms of molecules, why the pressure of a gas increases when it is heated in a sealed container.", 3, ["molecules move faster / gain kinetic energy", "collide with walls more often", "and with greater force, so pressure increases"], "5.18 5.20", cmd="Explain", d="4-6"),
       K("Explain, in terms of molecules, why squashing a gas into a smaller volume at constant temperature increases its pressure.", 2, ["molecules hit the walls more often (more collisions per second per unit area)", "average speed unchanged, so force per collision is the same"], "5.20", cmd="Explain", d="7-9"),
       K("Explain why there is a lowest possible temperature.", 2, ["temperature depends on kinetic energy of particles", "at absolute zero particles cannot lose any more kinetic energy"], "5.16", cmd="Explain", d="7-9"),
       K("Explain why a car tyre's pressure is higher after a long journey.", 2, ["air in the tyre is warmer", "molecules move faster and hit the walls harder and more often"], "5.18 5.20", cmd="Explain"),
       K("Explain why a balloon expands when taken from a cold room into a warm room.", 2, ["molecules move faster in warmer air", "push harder on the inside of the balloon, which stretches until pressures balance"], "5.18", cmd="Explain", d="4-6"),
   ])


# ====================================================================== density & pressure calcs

MAT = [("aluminium", 2700), ("copper", 8900), ("iron", 7900), ("oak", 700), ("glass", 2500), ("lead", 11300), ("brass", 8500), ("ice", 920), ("concrete", 2400)]


@T(DE, "calc", 5, "de-rho")
def de_rho(r):
    mat, rho = pick(r, MAT)
    a, b, c = nice(r, 2, 12, 0.5), nice(r, 2, 10, 0.5), nice(r, 1, 6, 0.5)
    Vcm = a * b * c
    m_g = rho * Vcm / 1000
    if r.random() < 0.5:
        return calc_q(intro=f"A block of {mat} measures {clean(a)} cm × {clean(b)} cm × {clean(c)} cm. Its mass is {sf(m_g, 3)} g.", text="Calculate the density of the block in g/cm³.",
                      eq="ρ = m ÷ V", working=[f"V = {clean(a)} × {clean(b)} × {clean(c)} = {clean(Vcm)} cm³", f"ρ = {sf(m_g, 3)} ÷ {clean(Vcm)}"],
                      ans=sf(float(sf(m_g, 3)) / Vcm, 3), unit="g/cm³", prefix="density (g/cm³) = ", refs=["5.3"], d="4-6", rearr=False,
                      values={"V": Vcm, "rho": rho / 1000}, notes="first mark for volume; " + alts(rho / 1000),
                      state=("density, mass and volume", "density = mass ÷ volume", None) if r.random() < 0.5 else None)
    V = nice(r, 0.001, 0.5, 0.001)
    m = rho * V
    return calc_q(intro=f"The density of {mat} is {rho} kg/m³.", text=f"Calculate the mass of a piece of {mat} with a volume of {clean(V)} m³.",
                  eq="ρ = m ÷ V", working=[f"{rho} = m ÷ {clean(V)}", f"m = {rho} × {clean(V)}"], ans=num(m, 3), unit="kg", prefix="mass (kg) = ",
                  refs=["5.3"], d="4-6", values={"m": m}, notes=alts(m))


@T(DE, "calc", 5, "de-p")
def de_p(r):
    obj = pick(r, ["a box resting on its base", "a person standing on one foot", "an elephant standing on four feet", "a crate on the floor", "a tank tread on soft ground", "a stiletto heel"])
    F = nice(r, 50, 60000, 50)
    A = nice(r, 0.0005, 2.0, 0.0005)
    p = F / A
    if r.random() < 0.5:
        return calc_q(intro=f"The weight of {obj} is {clean(F)} N. The area of contact is {clean(A)} m².", text="Calculate the pressure exerted on the ground.",
                      eq="p = F ÷ A", working=[f"p = {clean(F)} ÷ {clean(A)}"], ans=num(p, 3), unit="Pa", prefix="pressure (Pa) = ", refs=["5.5"], d="1-3",
                      rearr=False, values={"p": p}, notes=alts(p), state=("pressure, force and area", "pressure = force ÷ area", None))
    return calc_q(intro=f"{obj.capitalize()} exerts a pressure of {num(p, 3)} Pa over an area of {clean(A)} m².", text="Calculate the force exerted.", eq="p = F ÷ A",
                  working=[f"{num(p, 3)} = F ÷ {clean(A)}", f"F = {num(p, 3)} × {clean(A)}"], ans=num(F, 3), unit="N", prefix="force (N) = ", refs=["5.5"],
                  d="4-6", values={"F": F}, notes=alts(F))


@T(DE, "calc", 5, "de-hrg")
def de_hrg(r):
    liq, rho = pick(r, [("sea water", 1030), ("fresh water", 1000), ("oil", 850), ("mercury", 13600), ("a salt solution", 1200)])
    h = nice(r, 0.2, 200, 0.1) if rho < 13000 else nice(r, 0.05, 0.8, 0.01)
    p = h * rho * 10
    who = pick(r, ["a diver", "a sensor", "a submarine window", "the base of a tank", "a fish"])
    if r.random() < 0.6:
        return calc_q(intro=f"{who.capitalize()} is {clean(h)} m below the surface of {liq}. The density of {liq} is {rho} kg/m³. (g = 10 N/kg)",
                      text="Calculate the pressure due to the liquid at this depth.", eq="p = h × ρ × g", working=[f"p = {clean(h)} × {rho} × 10"],
                      ans=num(p, 3), unit="Pa", prefix="pressure (Pa) = ", refs=["5.7"], d="4-6", rearr=False, values={"p": p}, notes=alts(p) + "; allow answer in kPa with unit")
    pk = p / 1000
    return calc_q(intro=f"The pressure due to {liq} on {who} is {num(pk, 3)} kPa. The density of {liq} is {rho} kg/m³. (g = 10 N/kg)",
                  text="Calculate the depth.", eq="p = h × ρ × g", working=[f"p = {num(p, 3)} Pa", f"h = {num(p, 3)} ÷ ({rho} × 10)"], ans=num(h, 3), unit="m",
                  prefix="depth (m) = ", refs=["5.7", "5.1"], d="7-9", values={"h": h}, notes=alts(h) + "; kPa must be converted to Pa")


@T(DE, "practical", 7, "de-prac-irreg")
def de_prac(r):
    obj, rho = pick(r, [("small stone", 2600), ("metal key", 8500), ("lump of plasticine", 1700), ("glass marble", 2500), ("brass weight", 8500), ("piece of rock", 3000)])
    v1 = nice(r, 30, 60, 1)
    dv = nice(r, 5, 25, 1)
    m = rho * dv / 1000
    rr = float(sf(m, 3)) / dv
    tab = {"type": "table", "headers": ["measurement", "value"], "rows": [["mass of object in g", sf(m, 3)], ["water level before in cm³", clean(v1)], ["water level after in cm³", clean(v1 + dv)]], "caption": "Results"}
    parts = [line_part("a", f"Describe how the student could find the volume of the {obj}.", 3, 4),
             work_part("b", "Use the results to calculate the density of the object in g/cm³.", 3, "density (g/cm³) = "),
             line_part("c", "State **one** source of error and how to reduce it.", 2, 2)]
    rows = [row("(a)", "any three from:\nMP1. part fill a measuring cylinder with water and read the volume;\nMP2. lower the object in on a thread so it is fully submerged;\nMP3. read the new volume at eye level / bottom of meniscus;\nMP4. volume = difference between readings;\nMP5. alternatively use a displacement (eureka) can and collect the overflow;", 3, None, "AO3"),
            row("(b)", f"volume = {clean(dv)} cm³;", 1, None, "AO2"), row("(b)", f"ρ = {sf(m, 3)} ÷ {clean(dv)};", 1, None, "AO2"), row("(b)", f"{sf(rr, 3)} (g/cm³);", 1, alts(rr), "AO2"),
            row("(c)", "air bubbles on the object / parallax reading the meniscus / water splashing out;", 1, None, "AO3"),
            row("(c)", "matching improvement e.g. tap to remove bubbles / read at eye level / lower gently;", 1, None, "AO3")]
    return dict(parts=parts, rows=rows, refs=["5.4", "5.3"], cmd="Describe", d="4-6", ao=["AO2", "AO3"], figures=[tab],
                intro=f"A student wants to find the density of a {obj}. Her measurements are shown.", answer={"method": "python", "values": {"rho": rr}, "checked": True})


@T(DE, "practical", 6, "de-prac-reg")
def de_prac_reg(r):
    mat, rho = pick(r, MAT[:7])
    a, b, c = nice(r, 2, 6, 0.1), nice(r, 2, 6, 0.1), nice(r, 1, 4, 0.1)
    V = a * b * c
    m = rho * V / 1000
    parts = [line_part("a", "Name the measuring instruments needed to find the volume and the mass of the block.", 2, 2),
             work_part("b", f"The block measures {clean(a)} cm × {clean(b)} cm × {clean(c)} cm and has a mass of {sf(m, 3)} g. Calculate its density in kg/m³.", 4, "density (kg/m³) = "),
             line_part("c", "Explain why the student measures each side several times.", 1, 2)]
    rr = float(sf(m, 3)) / V * 1000
    rows = [row("(a)", "ruler / vernier calipers for the lengths;", 1, None, "AO3"), row("(a)", "balance for mass;", 1, None, "AO3"),
            row("(b)", f"V = {sf(V, 3)} cm³;", 1, None, "AO2"), row("(b)", f"ρ = {sf(m, 3)} ÷ {sf(V, 3)} = {sf(rr / 1000, 3)} g/cm³;", 1, None, "AO2"),
            row("(b)", "conversion × 1000;", 1, "allow conversion of m and V first", "AO2"), row("(b)", f"{num(rr, 3)} (kg/m³);", 1, alts(rr), "AO2"),
            row("(c)", "the block may not be perfectly regular, so a mean reduces the effect of random error;", 1, None, "AO3")]
    return dict(parts=parts, rows=rows, refs=["5.4", "5.3", "5.1"], cmd="Calculate", d="7-9", ao=["AO2", "AO3"],
                intro=f"A student finds the density of a rectangular block of {mat}.", answer={"method": "python", "values": {"rho": rr}, "checked": True})


# ====================================================================== state: SHC calc / practical / cooling data

SUB = [("water", 4200), ("aluminium", 900), ("copper", 390), ("oil", 2000), ("iron", 450), ("concrete", 880), ("ethanol", 2400)]


@T(ST, "calc", 14, "st-mct")
def st_mct(r):
    s, c = pick(r, SUB)
    m = nice(r, 0.1, 5, 0.1)
    dT = nice(r, 2, 80, 1)
    Q = m * c * dT
    mode = r.choice(["Q", "dT", "c"])
    if mode == "Q":
        t1 = nice(r, 10, 25, 1)
        return calc_q(intro=f"A {clean(m)} kg sample of {s} is heated from {clean(t1)} °C to {clean(t1 + dT)} °C. The specific heat capacity of {s} is {c} J/kg °C.",
                      text="Calculate the energy transferred to the sample.", eq="ΔQ = m × c × ΔT", working=[f"ΔT = {clean(dT)} °C", f"ΔQ = {clean(m)} × {c} × {clean(dT)}"],
                      ans=num(Q, 3), unit="J", prefix="energy (J) = ", refs=["5.13P"], d="4-6", rearr=False, values={"Q": Q}, notes=alts(Q),
                      state=("change in thermal energy, mass, specific heat capacity and change in temperature", "ΔQ = m × c × ΔT", None) if r.random() < 0.5 else None)
    if mode == "dT":
        return calc_q(intro=f"{num(Q, 3)} J of energy is supplied to {clean(m)} kg of {s} (specific heat capacity {c} J/kg °C).", text="Calculate the rise in temperature.",
                      eq="ΔQ = m × c × ΔT", working=[f"{num(Q, 3)} = {clean(m)} × {c} × ΔT", f"ΔT = {num(Q, 3)} ÷ ({clean(m)} × {c})"], ans=num(dT, 3), unit="°C",
                      prefix="temperature rise (°C) = ", refs=["5.13P"], d="4-6", values={"dT": dT}, notes=alts(dT))
    P = pick(r, [50, 100, 500, 1000, 2000])
    t = Q / P
    return calc_q(intro=f"A {P} W heater warms {clean(m)} kg of a liquid by {clean(dT)} °C in {sf(t, 3)} s. Assume all the energy goes into the liquid.",
                  text="Calculate the specific heat capacity of the liquid.", eq="ΔQ = m × c × ΔT",
                  working=[f"ΔQ = {P} × {sf(t, 3)} = {num(P * float(sf(t, 3)), 3)} J", f"c = {num(P * float(sf(t, 3)), 3)} ÷ ({clean(m)} × {clean(dT)})"],
                  ans=num(P * float(sf(t, 3)) / (m * dT), 3), unit="J/kg °C", prefix="specific heat capacity (J/kg °C) = ", refs=["5.13P", "4.17"], d="7-9",
                  values={"c": P * float(sf(t, 3)) / (m * dT)}, notes=alts(P * float(sf(t, 3)) / (m * dT)) + "; energy from E = P × t")


@T(ST, "practical", 7, "st-prac-shc")
def st_prac(r):
    mat, c = pick(r, SUB[1:3] + SUB[4:5] + [("brass", 380)])
    m = pick(r, [0.5, 1.0, 1.0, 2.0])
    E = nice(r, 8000, 40000, 500)
    dT_true = E / (m * c)
    dT = round(dT_true * r.uniform(0.80, 0.92), 1)
    cm = E / (m * dT)
    fig = {"type": "svg", "svg": S.table_apparatus_heater(), "width": 80, "caption": "Apparatus"}
    parts = [work_part("a", f"The joulemeter reading increases by {clean(E)} J and the temperature rises by {clean(dT)} °C. The block has a mass of {clean(m)} kg. Calculate the specific heat capacity.", 3, "c (J/kg °C) = "),
             line_part("b", f"The accepted value for {mat} is {c} J/kg °C. Explain why the student's value is higher.", 2, 3),
             line_part("c", "State **two** ways the student could improve the experiment.", 2, 2)]
    rows = [row("(a)", f"substitution: {clean(E)} = {clean(m)} × c × {clean(dT)};", 1, None, "AO2"), row("(a)", "rearrangement;", 1, None, "AO2"),
            row("(a)", f"{num(cm, 3)} (J/kg °C);", 1, alts(cm), "AO2"),
            row("(b)", "energy is lost to the surroundings;", 1, None, "AO3"), row("(b)", "so the temperature rise is smaller than it should be, giving a larger value of c;", 1, None, "AO3"),
            row("(c)", "any two from:\nadd (more) insulation / lid;\nput oil in the thermometer hole;\nuse a digital thermometer / temperature probe;\nrecord the highest temperature after switching off;\nrepeat and average;", 2, None, "AO3")]
    return dict(parts=parts, rows=rows, refs=["5.14P", "5.13P"], cmd="Calculate", d="7-9", ao=["AO2", "AO3"], figures=[fig],
                intro=f"A student uses the apparatus shown to measure the specific heat capacity of {mat}.", answer={"method": "python", "values": {"c": cm}, "checked": True})


@T(ST, "practical", 6, "st-prac-water")
def st_prac_water(r):
    m = nice(r, 0.2, 0.8, 0.05)
    P = pick(r, [24, 36, 48, 60, 100])
    t = pick(r, [300, 360, 420, 480, 600])
    E = P * t
    dT = round(E / (m * 4200) * r.uniform(0.85, 0.95), 1)
    c = E / (m * dT)
    parts = [line_part("a", "Describe how the student should carry out the experiment.", 4, 6),
             work_part("b", f"The heater has a power of {P} W and is on for {t} s. The temperature rises by {clean(dT)} °C. Calculate the specific heat capacity of water.", 3, "c (J/kg °C) = ")]
    rows = [row("(a)", "any four from:\nMP1. measure the mass of water using a balance;\nMP2. place the water in an insulated beaker with an immersion heater and thermometer;\nMP3. measure the starting temperature;\n"
                       "MP4. switch on the heater and start the stopwatch;\nMP5. stir the water;\nMP6. record final temperature after a measured time;\nMP7. calculate energy from P × t (or joulemeter);", 4, None, "AO3"),
            row("(b)", f"E = {P} × {t} = {E} J;", 1, None, "AO2"), row("(b)", f"c = {E} ÷ ({clean(m)} × {clean(dT)});", 1, None, "AO2"), row("(b)", f"{num(c, 3)} (J/kg °C);", 1, alts(c), "AO2")]
    return dict(parts=parts, rows=rows, refs=["5.14P", "5.13P"], cmd="Describe", d="4-6", ao=["AO2", "AO3"],
                intro=f"A student wants to measure the specific heat capacity of water using {clean(m)} kg of water and an electric immersion heater.",
                answer={"method": "python", "values": {"c": c}, "checked": True})


@T(ST, "data", 14, "st-cooling")
def st_cooling(r):
    sub, mp = pick(r, [("stearic acid", 69), ("salol", 43), ("paraffin wax", 56), ("lauric acid", 44), ("a wax", 62), ("an unknown solid", 52)])
    start = mp + nice(r, 12, 20, 1)
    times = list(range(0, 13))
    temps = []
    T_ = start
    plateau_start = r.randint(3, 4)
    plateau_len = r.randint(4, 5)
    for k in times:
        if k < plateau_start:
            T_ = start - (start - mp) * k / plateau_start
        elif k < plateau_start + plateau_len:
            T_ = mp
        else:
            T_ = mp - 4 * (k - plateau_start - plateau_len + 1)
        temps.append(round(T_))
    tab = {"type": "table", "headers": ["time in min"] + [str(t) for t in times], "rows": [["temperature in °C"] + [str(t) for t in temps]], "caption": "Results"}
    parts = [{"label": "a", "text": "Plot a graph of temperature against time and draw a suitable line.", "marks": 4, "space": "graph"},
             line_part("b", f"Use your graph to find the melting point of {sub}.", 1, 1, prefix="melting point (°C) = "),
             line_part("c", "Explain why the temperature stays constant for several minutes.", 2, 3)]
    rows = [row("(a)", "suitable scales (more than half the grid);", 1, None, "AO3"), row("(a)", "axes labelled with units;", 1, None, "AO3"),
            row("(a)", "points plotted to nearest half square;", 1, None, "AO3"), row("(a)", "smooth curve/lines including a flat section;", 1, None, "AO3"),
            row("(b)", f"{mp};", 1, "allow ±1", "AO3"),
            row("(c)", "substance is changing state (liquid to solid);", 1, None, "AO1"), row("(c)", "energy released as bonds form balances the energy lost, so kinetic energy of particles is unchanged;", 1, None, "AO1")]
    return dict(parts=parts, rows=rows, refs=["5.11P", "5.8P", "5.9P"], cmd="Plot", d="4-6", ao=["AO1", "AO3"], figures=[tab],
                intro=f"A student heats a tube of {sub} until it melts, then records its temperature every minute as it cools.",
                answer={"method": "python", "values": {"mp": mp}, "checked": True})


# ====================================================================== gases

@T(GA, "calc", 7, "ga-boyle")
def ga_boyle(r):
    p1 = nice(r, 80, 300, 5)
    V1 = nice(r, 20, 400, 5)
    k = pick(r, [0.25, 0.4, 0.5, 0.6, 0.75, 1.5, 2, 2.5, 3])
    V2 = V1 * k
    p2 = p1 * V1 / V2
    ctx = pick(r, ["a gas syringe", "a bicycle pump", "a sealed cylinder", "a weather balloon", "a diver's air bubble"])
    return calc_q(intro=f"Air in {ctx} has a pressure of {clean(p1)} kPa and a volume of {clean(V1)} cm³. The volume changes to {sf(V2, 3)} cm³ at constant temperature.",
                  text="Calculate the new pressure.", eq="p₁V₁ = p₂V₂", working=[f"{clean(p1)} × {clean(V1)} = p₂ × {sf(V2, 3)}", f"p₂ = {clean(p1 * V1)} ÷ {sf(V2, 3)}"],
                  ans=num(p2, 3), unit="kPa", prefix="pressure (kPa) = ", refs=["5.22"], d="4-6", values={"p2": p2}, notes=alts(p2))


@T(GA, "calc", 7, "ga-pt")
def ga_pt(r):
    p1 = nice(r, 90, 300, 5)
    t1 = nice(r, -20, 40, 1)
    t2 = t1 + nice(r, 10, 120, 5)
    T1, T2 = t1 + 273, t2 + 273
    p2 = p1 * T2 / T1
    ctx = pick(r, ["a car tyre", "a sealed can", "a gas cylinder", "a pressure cooker", "a football"])
    return calc_q(intro=f"The gas in {ctx} is at {clean(p1)} kPa and {clean(t1)} °C. It is heated to {clean(t2)} °C at constant volume.",
                  text="Calculate the new pressure.", eq="p₁ ÷ T₁ = p₂ ÷ T₂", working=[f"T₁ = {T1} K, T₂ = {T2} K", f"p₂ = {clean(p1)} × {T2} ÷ {T1}"],
                  ans=num(p2, 3), unit="kPa", prefix="pressure (kPa) = ", refs=["5.21", "5.17"], d="7-9", values={"T1": T1, "T2": T2, "p2": p2},
                  notes=alts(p2) + "; using °C scores substitution only if it is consistent; temperatures must be in kelvin for evaluation")


@T(GA, "data", 7, "ga-data-pt")
def ga_data_pt(r):
    k = nice(r, 0.30, 0.40, 0.01)
    temps = [0, 20, 40, 60, 80, 100]
    ps = [round(k * (t + 273) + r.choice([-1, 0, 0, 1])) for t in temps]
    tab = {"type": "table", "headers": ["temperature in °C"] + [str(t) for t in temps], "rows": [["pressure in kPa"] + [str(p) for p in ps]], "caption": "Results"}
    parts = [{"label": "a", "text": "Plot a graph of pressure against temperature in °C and draw a line of best fit.", "marks": 4, "space": "graph"},
             line_part("b", "The line is extended to the left until the pressure would be zero. State the temperature at which this happens.", 1, 1, prefix="temperature (°C) = "),
             line_part("c", "Explain, in terms of molecules, why the pressure increases with temperature.", 2, 3)]
    rows = [row("(a)", "suitable scales;", 1, None, "AO3"), row("(a)", "axes labelled with units;", 1, None, "AO3"), row("(a)", "points plotted correctly;", 1, None, "AO3"),
            row("(a)", "straight line of best fit;", 1, None, "AO3"),
            row("(b)", "-273 °C;", 1, "allow -260 to -290", "AO3"),
            row("(c)", "molecules move faster;", 1, None, "AO1"), row("(c)", "more frequent / harder collisions with the walls;", 1, None, "AO1")]
    return dict(parts=parts, rows=rows, refs=["5.16", "5.20", "5.18"], cmd="Plot", d="7-9", ao=["AO1", "AO3"], figures=[tab],
                intro=f"A student heats a fixed mass of {pick(r, ['air', 'nitrogen', 'gas'])} in a sealed flask and records its pressure at different temperatures.",
                answer={"method": "python", "values": {"p": ps}, "checked": True})


@T(GA, "data", 7, "ga-data-pv")
def ga_data_pv(r):
    pV = nice(r, 2000, 6000, 100)
    Vs = [10, 15, 20, 25, 30, 40]
    ps = [round(pV / V) for V in Vs]
    tab = {"type": "table", "headers": ["volume in cm³"] + [str(v) for v in Vs], "rows": [["pressure in kPa"] + [str(p) for p in ps]], "caption": "Results"}
    Vq = pick(r, [12, 18, 35])
    parts = [line_part("a", "Show that pressure × volume is approximately constant. Use **three** results.", 2, 3),
             work_part("b", f"Use the relationship to calculate the pressure when the volume is {Vq} cm³.", 2, "pressure (kPa) = "),
             line_part("c", "State **two** variables that must be kept constant.", 2, 2)]
    pq = pV / Vq
    rows = [row("(a)", "three products of p × V calculated;", 1, None, "AO3"), row("(a)", f"all close to {clean(pV)};", 1, None, "AO3"),
            row("(b)", f"p = {clean(pV)} ÷ {Vq};", 1, "allow ecf", "AO2"), row("(b)", f"{num(pq, 3)} (kPa);", 1, alts(pq), "AO2"),
            row("(c)", "temperature;", 1, None, "AO3"), row("(c)", "mass (amount) of gas;", 1, None, "AO3")]
    return dict(parts=parts, rows=rows, refs=["5.22", "5.20"], cmd="Show", d="4-6", ao=["AO2", "AO3"], figures=[tab],
                intro=f"A student traps air in a {pick(r, ['syringe', 'sealed tube', 'cylinder with a piston'])} and measures its pressure as the volume is changed slowly.",
                answer={"method": "python", "values": {"pV": pV, "p": pq}, "checked": True})
