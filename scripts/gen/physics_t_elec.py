"""Topic 2: Electricity."""
import math

import physics_svg as S
from physics_util import (K, M, X, T, kb, calc_q, line_part, work_part, row, num, sf, clean, pick, nice, alts)

MA, CI, CH, ST = ("physics.electricity.mains", "physics.electricity.circuits", "physics.electricity.charge", "physics.electricity.static")

kb(MA, ["electrical safety in the home", "domestic appliances", "using mains electricity", "fuses and circuit breakers", "heating effects of current"],
   mcq=[
       M("Which wire in a mains plug is connected to the metal case of an appliance?", ["earth", "live", "neutral", "fuse"], "2.2"),
       M("What type of current is supplied by a battery?", ["direct current", "alternating current", "mains current", "induced current"], "2.6"),
       M("A kettle is labelled 230 V, 2300 W. What is the current when it is working normally?", ["10 A", "0.10 A", "100 A", "529 000 A"], "2.4", ao="AO2", d="4-6"),
       M("Which device protects a circuit by switching off automatically and can be reset?", ["circuit breaker", "fuse", "earth wire", "switch"], "2.2"),
       M("An appliance is double insulated. This means it", ["has a plastic case and does not need an earth wire", "has two fuses", "has a metal case connected to earth", "works on direct current only"], "2.2", d="4-6"),
       M("Which unit is used for energy transferred?", ["joule", "watt", "volt", "ampere"], "2.1 2.5"),
       M("A fuse melts when", ["the current is larger than the fuse rating", "the voltage falls", "the appliance is switched off", "the earth wire is connected"], "2.2"),
       M("Which household device uses the heating effect of a current?", ["toaster", "radio", "doorbell magnet", "phone charger"], "2.3"),
   ],
   recall=[
       K("State the equation linking power, current and voltage.", 1, ["power = current × voltage | allow P = I × V"], "2.4", cmd="State"),
       K("State what is meant by *alternating current*.", 1, ["current that keeps changing direction | allow flows one way then the other"], "2.6", cmd="State"),
       K("Give **two** devices in the home that make use of the heating effect of an electric current.", 2, ["kettle", "toaster", "electric heater", "hair dryer", "iron", "immersion heater/oven"], "2.3", cmd="Give"),
       K("Name **two** safety features that protect a user from electric shock if a live wire touches the metal case of an appliance.", 2, ["earth wire / earthing", "fuse", "circuit breaker"], "2.2", cmd="Name"),
       K("State **one** difference between a fuse and a circuit breaker.", 1, ["a circuit breaker can be reset but a fuse must be replaced | allow circuit breaker acts faster"], "2.2", cmd="State"),
       K("Give the unit of electrical power.", 1, ["watt / W | allow J/s"], "2.1", cmd="Give"),
   ],
   describe=[
       K("Describe how a fuse protects an appliance.", 3, ["fuse is in series with the live wire", "if the current is too large the fuse wire heats up and melts", "which breaks the circuit / stops the current"], "2.2", cmd="Describe"),
       K("Describe the difference between the current from a cell and the current from the mains supply.", 2, ["cell gives direct current that flows in one direction only", "mains gives alternating current that changes direction (many times a second)"], "2.6", cmd="Describe"),
       K("Describe how double insulation protects the user of a hair dryer.", 2, ["the casing is made of an insulator / plastic", "so the user cannot touch a live conducting part even if a wire comes loose"], "2.2", cmd="Describe"),
       K("Describe how the heating effect of a current is used in an electric kettle.", 2, ["current passes through a (high resistance) heating element", "element gets hot and transfers energy to the water by heating"], "2.3", cmd="Describe"),
   ],
   explain=[
       K("Explain why a current in a resistor causes the resistor to get hot.", 2, ["electrons collide with ions/atoms in the resistor", "transferring energy which increases the thermal energy store"], "2.3", cmd="Explain", d="4-6"),
       K("Explain how the earth wire and fuse together protect a person who touches a faulty appliance with a metal case.", 3,
         ["the live wire touches the case and a large current flows to earth (low resistance path)", "the large current melts the fuse", "the circuit is broken so the case is no longer live"], "2.2", cmd="Explain", d="4-6"),
       K("Explain why the fuse is always placed in the live wire.", 2, ["so that when it melts the appliance is disconnected from the high voltage", "if it were in the neutral the appliance would still be live"], "2.2", cmd="Explain", d="7-9"),
       K("Explain why a 13 A fuse would not be suitable for a lamp that draws 0.25 A.", 2, ["the fuse rating is much higher than the normal current", "a fault current could flow without melting the fuse, so the lamp/wire could overheat"], "2.4", cmd="Explain", d="4-6", ao="AO2"),
       K("Explain why an appliance with a plastic case does not need an earth wire.", 2, ["plastic is an insulator", "so the case cannot become live / current cannot flow through the user"], "2.2", cmd="Explain"),
   ],
   extended=[
       X("A hair dryer has a metal case. Explain how the earth wire, the fuse and the insulation work together to protect the user and the appliance.",
         ["plastic insulation around wires prevents contact with live parts", "earth wire is connected to the metal case", "if a fault lets the live wire touch the case, the case would become live",
          "earth wire provides a low-resistance path to earth", "a very large current flows", "fuse is in the live wire and is rated just above the normal current",
          "the large current heats and melts the fuse", "circuit is broken so the case is no longer at a high voltage", "the user does not receive a shock and wiring does not overheat",
          "a circuit breaker could be used instead and reset"], "2.2"),
       X("Explain how you would choose a suitable fuse for an electric heater rated 2.0 kW, 230 V, and why using the wrong fuse could be dangerous. Fuses of 3 A, 5 A and 13 A are available.",
         ["use P = I × V", "current = 2000 ÷ 230 = 8.7 A", "fuse must have a rating just above the normal current", "choose the 13 A fuse", "3 A or 5 A fuse would melt in normal use",
          "a fuse with a much larger rating would not melt during a fault", "large fault current could overheat wires and cause a fire", "fuse goes in the live wire"], "2.4 2.2"),
       X("Compare the use of fuses and circuit breakers to protect domestic circuits.",
         ["both are placed in the live wire", "both break the circuit if the current is too large", "fuse contains a thin wire that heats and melts", "circuit breaker uses an electromagnet/switch that trips",
          "circuit breaker can be reset; fuse must be replaced", "circuit breaker acts faster", "fuses are cheaper", "circuit breakers are more convenient and reliable",
          "a fuse with the wrong rating may be fitted by mistake"], "2.2"),
   ])

kb(CI, ["series and parallel circuits", "electrical components", "sensors in circuits", "resistance", "lighting circuits"],
   mcq=[
       M("Which component's resistance decreases as the temperature increases?", ["thermistor", "LDR", "diode", "filament lamp"], "2.11"),
       M("Which component's resistance decreases as the light intensity increases?", ["LDR", "thermistor", "fixed resistor", "fuse"], "2.11"),
       M("Which component allows current to flow in one direction only?", ["diode", "resistor", "lamp", "thermistor"], "2.9"),
       M("Lamps in a house are connected in parallel. Which is a reason for this?", ["each lamp can be switched on and off independently", "the current in each lamp is the same", "fewer wires are needed", "the lamps share the voltage"], "2.7"),
       M("A 6.0 V supply is connected across a 3.0 Ω resistor. What is the current?", ["2.0 A", "0.50 A", "18 A", "9.0 A"], "2.13", ao="AO2"),
       M("The resistance in a series circuit is increased. What happens to the current?", ["it decreases", "it increases", "it stays the same", "it reverses"], "2.10"),
       M("What is the shape of the current-voltage graph for a fixed resistor at constant temperature?", ["a straight line through the origin", "a curve that gets less steep", "zero current until about 0.6 V", "a horizontal line"], "2.9"),
       M("Why does the resistance of a filament lamp increase as the current increases?", ["the filament gets hotter", "the filament gets longer", "the voltage falls", "the electrons move more slowly"], "2.9", d="7-9"),
       M("An LED is used in a circuit mainly to", ["show that a current is flowing", "increase the current", "store charge", "measure the voltage"], "2.12"),
   ],
   recall=[
       K("State the equation linking voltage, current and resistance.", 1, ["voltage = current × resistance | allow V = I × R"], "2.13", cmd="State"),
       K("State how the resistance of a thermistor changes as its temperature rises.", 1, ["it decreases"], "2.11", cmd="State"),
       K("State how the resistance of an LDR changes when the light falling on it gets brighter.", 1, ["it decreases"], "2.11", cmd="State"),
       K("Give **two** components that could be used to show that there is a current in a circuit.", 2, ["lamp", "LED", "ammeter | allow buzzer"], "2.12", cmd="Give"),
       K("State how an ammeter and a voltmeter should be connected to measure the current in and voltage across a lamp.", 2, ["ammeter in series (with the lamp)", "voltmeter in parallel (across the lamp)"], "2.9", cmd="State"),
       K("Give **one** advantage of connecting lamps in parallel rather than in series.", 1, ["each lamp can be controlled by its own switch | allow if one breaks the others stay on; allow each gets the full supply voltage"], "2.7", cmd="Give"),
       K("State what happens to the current in a series circuit when an extra lamp is added.", 1, ["current decreases | allow lamps become dimmer"], "2.8", cmd="State"),
   ],
   describe=[
       K("Describe how the current through a filament lamp changes as the voltage across it increases.", 2, ["current increases", "but by less and less / graph curves (because resistance increases)"], "2.9", cmd="Describe", d="4-6"),
       K("Describe the current-voltage characteristic of a diode.", 3, ["no current when voltage is in the reverse direction", "very little current at small forward voltages", "current rises steeply above a small forward voltage (about 0.6 V)"], "2.9", cmd="Describe", d="4-6"),
       K("Describe how the current-voltage graph of a fixed resistor shows that its resistance is constant.", 2, ["straight line through the origin", "so V/I (or gradient) is constant"], "2.9", cmd="Describe"),
       K("Describe how a variable resistor is used to change the current in a circuit.", 2, ["increasing its resistance reduces the current", "decreasing its resistance increases the current"], "2.10", cmd="Describe"),
   ],
   explain=[
       K("Explain why the lamps in a series circuit get dimmer when another lamp is added.", 2, ["total resistance increases", "so the current decreases | allow voltage shared between more lamps"], "2.8 2.10", cmd="Explain"),
       K("A thermistor is used in a circuit to switch on a fan when a room gets hot. Explain how the thermistor's resistance makes this possible.", 2,
         ["as temperature rises the resistance of the thermistor falls", "so the current (or voltage across another component) increases and switches on the fan"], "2.11", cmd="Explain", d="4-6", ao="AO2"),
       K("Explain why street lights could use an LDR to switch them on automatically.", 2, ["when it gets dark the resistance of the LDR increases", "the change in voltage/current is used to switch the lights on"], "2.11", cmd="Explain", d="4-6", ao="AO2"),
       K("Explain why lights in a house are connected in parallel rather than in series.", 3, ["each light gets the full mains voltage", "each can be switched independently", "if one bulb fails the others still work"], "2.7", cmd="Explain"),
       K("Explain why the resistance of a metal filament lamp increases as the current through it increases.", 3, ["larger current makes the filament hotter", "ions vibrate more", "so electrons collide more often / flow is opposed more"], "2.9", cmd="Explain", d="7-9"),
   ],
   extended=[
       X("Describe how a student could investigate how the current in a filament lamp varies with the potential difference across it. Include a circuit diagram and describe how the results should be analysed.",
         ["circuit: supply, lamp, ammeter in series", "voltmeter in parallel across the lamp", "variable resistor (or variable supply) to change the voltage",
          "record current and voltage for a range of settings", "reverse the connections to obtain negative values", "repeat readings and take means",
          "switch off between readings so the lamp does not overheat", "plot a graph of current against voltage", "the graph is a curve: resistance increases as the lamp heats up",
          "calculate R = V/I at several points"], "2.9 2.13", title="I-V investigation"),
       X("Explain how a light-dependent resistor and a thermistor could be used in a greenhouse control circuit to switch on lamps when it is dark and a heater when it is cold.",
         ["LDR resistance increases as light level falls", "thermistor resistance increases as temperature falls", "each sensor in series with a fixed resistor (potential divider idea)",
          "the change in resistance changes the current or voltage", "this change can operate a switch / relay", "lamps switched on in the dark",
          "heater switched on when cold", "lamp or LED could indicate the heater is on", "separate circuits/parallel so each works independently"], "2.11 2.10 2.12"),
       X("Compare series and parallel circuits, using lamps connected to a battery as an example.",
         ["series: one path for the current", "series: same current through every lamp", "series: voltage shared between lamps", "series: lamps dimmer as more are added (resistance increases)",
          "series: if one lamp breaks all go out", "parallel: separate branches", "parallel: each lamp has the full battery voltage", "parallel: total current is the sum of branch currents",
          "parallel: lamps stay bright and can be switched separately", "parallel: battery runs down faster because more current flows"], "2.7 2.8 2.18"),
   ])

kb(CH, ["electric charge and current", "energy in circuits", "currents at junctions", "electrons in wires"],
   mcq=[
       M("What is electric current?", ["the rate of flow of charge", "the energy per unit charge", "the resistance per metre", "the force on a charge"], "2.14"),
       M("Which particles carry the current in a metal wire?", ["electrons", "protons", "neutrons", "positive ions"], "2.16"),
       M("One volt is equal to one", ["joule per coulomb", "coulomb per second", "watt per ampere squared", "ohm per ampere"], "2.20"),
       M("A current of 2.0 A flows for 30 s. How much charge flows?", ["60 C", "15 C", "0.067 C", "32 C"], "2.15", ao="AO2"),
       M("Two resistors are connected in parallel to a 9.0 V battery. What is the voltage across each resistor?", ["9.0 V", "4.5 V", "18 V", "3.0 V"], "2.18", d="4-6"),
       M("A current of 3.0 A enters a junction and splits into two branches. One branch carries 1.2 A. What is the current in the other branch?", ["1.8 A", "4.2 A", "1.2 A", "3.0 A"], "2.17", ao="AO2"),
       M("How much energy is transferred when 5.0 C of charge passes through a voltage of 12 V?", ["60 J", "2.4 J", "0.42 J", "17 J"], "2.21", ao="AO2", d="4-6"),
   ],
   recall=[
       K("State the equation linking charge, current and time.", 1, ["charge = current × time | allow Q = I × t"], "2.15", cmd="State"),
       K("State the equation linking energy transferred, charge and voltage.", 1, ["energy transferred = charge × voltage | allow E = Q × V"], "2.21", cmd="State"),
       K("State what is meant by an electric current.", 1, ["rate of flow of charge | allow flow of electrons; allow charge per second"], "2.14", cmd="State"),
       K("Give the unit of charge.", 1, ["coulomb / C | allow A s"], "2.1", cmd="Give"),
       K("State what is meant by the *voltage* across a component.", 1, ["energy transferred per unit charge (passing through it) | allow joules per coulomb"], "2.20", cmd="State"),
       K("Name the particles that flow in a copper wire when there is a current.", 1, ["(free) electrons | reject protons, ions"], "2.16", cmd="Name"),
   ],
   explain=[
       K("Explain why the current entering a junction is equal to the total current leaving it.", 2, ["charge is conserved / not used up", "so charge flowing in per second equals charge flowing out per second"], "2.17", cmd="Explain", d="4-6"),
       K("Explain why two lamps connected in parallel to a battery each have the same voltage across them.", 2, ["each lamp is connected directly across the battery terminals", "so each unit of charge transfers the same energy through either branch"], "2.18 2.20", cmd="Explain", d="7-9"),
       K("Explain, in terms of electrons, why an ammeter reads the same at any point in a series circuit.", 2, ["there is only one path for the electrons", "electrons are not used up so the same number pass each point per second"], "2.16 2.17", cmd="Explain", d="4-6"),
       K("Explain what is meant by saying that a cell has a voltage of 1.5 V.", 2, ["each coulomb of charge", "is given 1.5 J of energy (by the cell)"], "2.20", cmd="Explain", d="4-6"),
   ])

kb(ST, ["static electricity", "charging by friction", "dangers of static charge", "uses of electrostatics", "conductors and insulators"],
   mcq=[
       M("A polythene rod becomes negatively charged when rubbed with a cloth. This is because", ["electrons move from the cloth to the rod", "protons move from the rod to the cloth", "electrons move from the rod to the cloth", "protons move from the cloth to the rod"], "2.24P", d="4-6"),
       M("Two negatively charged balloons are held close together. What happens?", ["they repel", "they attract", "nothing happens", "they become neutral"], "2.25P"),
       M("Which of these materials is an electrical conductor?", ["copper", "polythene", "glass", "rubber"], "2.22P"),
       M("Why can a metal rod held in the hand not be charged by rubbing it?", ["charge flows through the metal and the person to earth", "metals have no electrons", "metals only gain protons", "the rod becomes too hot"], "2.22P 2.26P", d="7-9"),
       M("Which is a use of electrostatic charge?", ["inkjet printer", "electric kettle", "transformer", "fuse"], "2.28P"),
       M("A tanker is earthed before fuel is pumped out of it. This is to", ["prevent a spark from discharged static", "make the fuel flow faster", "charge the fuel", "cool the pipe"], "2.27P"),
       M("A charged rod attracts small pieces of uncharged paper. Which statement explains this?", ["charges in the paper are separated so unlike charges are closer", "the paper has the same charge as the rod", "the paper is a conductor", "gravity pulls the paper up"], "2.26P", d="7-9"),
   ],
   recall=[
       K("State what happens when two objects with unlike charges are brought close together.", 1, ["they attract"], "2.25P", cmd="State"),
       K("Name **two** materials that are good electrical insulators.", 2, ["plastic / polythene", "rubber", "glass", "wood (dry)", "acetate / perspex"], "2.22P", cmd="Name"),
       K("Name the particles that are transferred when an insulator is charged by rubbing.", 1, ["electrons | reject protons"], "2.24P", cmd="Name"),
       K("Give **one** use of electrostatic charge.", 1, ["photocopier", "inkjet printer", "paint spraying", "electrostatic precipitator/dust removal"], "2.28P", cmd="Give"),
       K("Give **one** situation where static charge can be dangerous.", 1, ["refuelling aircraft", "filling fuel tankers", "flour/grain dust in silos", "lightning | allow electronic component damage"], "2.27P", cmd="Give"),
   ],
   explain=[
       K("A balloon is rubbed on a woollen jumper and becomes negatively charged. Explain why.", 2, ["electrons are transferred", "from the jumper to the balloon (balloon gains electrons)"], "2.24P", cmd="Explain"),
       K("Explain why a charged balloon sticks to an uncharged wall.", 3, ["charged balloon repels electrons in the wall surface", "surface of wall nearest the balloon becomes positively charged (induced charge)", "unlike charges attract"], "2.26P", cmd="Explain", d="7-9"),
       K("Explain why an aircraft must be connected to earth before it is refuelled.", 3, ["friction between fuel and pipe causes a build-up of charge", "a spark could jump and ignite the fuel vapour", "earthing lets charge flow away safely"], "2.27P", cmd="Explain", d="4-6"),
       K("Explain how electrostatic charge is used in an inkjet printer.", 3, ["ink droplets are given a charge", "they pass between charged deflecting plates", "the size/sign of charge on the plates controls where droplets land on the paper"], "2.28P", cmd="Explain", d="7-9"),
       K("Explain why a person can get a small electric shock after walking across a nylon carpet and touching a metal door handle.", 3, ["friction transfers electrons between shoes and carpet", "charge builds up on the person", "charge flows (electrons move) to the earthed handle as a spark"], "2.24P 2.26P", cmd="Explain", d="4-6"),
       K("Explain why a photocopier drum attracts toner powder only where the image is dark.", 3, ["the drum is charged all over", "light from bright parts of the image discharges those areas", "toner (oppositely charged) is attracted only to the areas that remain charged"], "2.28P", cmd="Explain", d="7-9"),
   ],
   extended=[
       X("Explain how charging by friction happens and how it can be dangerous when fuel is transferred from a tanker. Suggest how the danger can be reduced.",
         ["materials rubbing together transfer electrons", "the object gaining electrons becomes negative, the other positive", "fuel flowing through a pipe rubs against it",
          "charge builds up on the tanker/pipe (insulated from earth by tyres)", "large voltage between tanker and ground", "a spark could jump", "spark ignites fuel vapour causing an explosion",
          "connect the tanker to earth with a conducting cable", "charge flows away safely", "use conducting pipes/hoses"], "2.24P 2.27P"),
       X("Describe an experiment to show that there are two kinds of electric charge. Explain the results in terms of electrons.",
         ["rub a polythene rod with a cloth and hang it from a thread (in a stirrup)", "rub a second polythene rod and bring it near: they repel", "rub an acetate rod and bring it near the polythene: they attract",
          "two identical rods must carry the same charge, so like charges repel", "different materials gain different charges, so unlike charges attract", "polythene gains electrons and is negative",
          "acetate loses electrons and is positive", "use a dry environment for best results", "no charge forms on a metal rod held in the hand because it conducts"], "2.23P 2.24P 2.25P"),
   ])


# ====================================================================== mains calculations

APPLIANCES = [("kettle", 1800, 3000, 100), ("toaster", 700, 1500, 50), ("hair dryer", 900, 2200, 100), ("lamp", 40, 150, 10), ("television", 60, 250, 10),
              ("microwave oven", 700, 1200, 50), ("electric heater", 1000, 3000, 250), ("food mixer", 200, 700, 50), ("vacuum cleaner", 600, 1600, 100)]


@T(MA, "calc", 7, "ma-fuse")
def ma_fuse(r):
    name, lo, hi, st = pick(r, APPLIANCES)
    P = nice(r, lo, hi, st)
    V = pick(r, [230, 230, 240, 120])
    I = P / V
    fuses = [3, 5, 13]
    choice = min(f for f in fuses if f > I) if I < 13 else None
    if choice is None:
        return None
    q = calc_q(intro=f"A {name} is rated at {clean(P)} W when connected to the {V} V mains supply.", text=f"Calculate the current in the {name}.",
               eq="P = I × V", working=[f"{clean(P)} = I × {V}", f"I = {clean(P)} ÷ {V}"], ans=num(I, 2), unit="A", prefix="current (A) = ",
               refs=["2.4"], d="4-6", values={"P": P, "V": V, "I": I, "fuse": choice}, notes=alts(I),
               state=("power, current and voltage", "power = current × voltage", None))
    q["parts"].append(line_part("c", "Fuses rated at 3 A, 5 A and 13 A are available. State which fuse should be fitted and give a reason.", 2, 2))
    q["rows"] += [row("(c)", f"{choice} A;", 1, "allow ecf from (b)"), row("(c)", "the smallest rating that is above the normal current;", 1)]
    return q


@T(MA, "calc", 7, "ma-energy")
def ma_energy(r):
    name, lo, hi, st = pick(r, APPLIANCES)
    V = pick(r, [230, 240, 12])
    if V == 12:
        name = pick(r, ["car headlamp", "camping heater", "electric fan in a car", "phone charger circuit"])
        I = nice(r, 0.5, 8, 0.5)
    else:
        I = nice(r, 0.2, 12, 0.2)
    tmin = r.choice([2, 5, 10, 15, 20, 30, 45])
    t = tmin * 60
    E = I * V * t
    mode = r.choice(["E", "t"])
    if mode == "E":
        q = calc_q(intro=f"A {name} is connected to a {V} V supply. The current is {clean(I)} A. It is switched on for {tmin} minutes.",
                   text="Calculate the energy transferred.", eq="E = I × V × t", working=[f"t = {tmin} × 60 = {t} s", f"E = {clean(I)} × {V} × {t}"],
                   ans=num(E, 3), unit="J", prefix="energy (J) = ", refs=["2.5"], d="4-6", rearr=False, values={"I": I, "V": V, "t": t, "E": E},
                   notes=alts(E) + "; time must be converted to seconds")
        q["parts"][-1]["marks"] = 3
        q["rows"].insert(1, row("", "conversion of minutes to seconds;", 1))
        return q
    return calc_q(intro=f"A {name} connected to a {V} V supply takes a current of {clean(I)} A. It transfers {num(E, 3)} J of energy.",
                  text="Calculate the time it was switched on for, in minutes.", eq="E = I × V × t",
                  working=[f"{num(E, 3)} = {clean(I)} × {V} × t", f"t = {num(E, 3)} ÷ ({clean(I)} × {V}) = {clean(t)} s", f"t = {tmin} minutes"],
                  ans=str(tmin), unit="minutes", prefix="time (minutes) = ", refs=["2.5"], d="7-9", values={"t_s": t, "t_min": tmin},
                  notes="award evaluation only if converted to minutes; allow 1 mark max for answer in seconds")


# ====================================================================== circuits

@T(CI, "calc", 9, "ci-vir")
def ci_vir(r):
    comp = pick(r, ["resistor", "heating element", "lamp", "wire", "motor coil"])
    R = nice(r, 2, 470, 1) if comp != "wire" else nice(r, 0.5, 8, 0.5)
    I = nice(r, 0.05, 3.0, 0.05)
    V = I * R
    mode = r.choice(["V", "I", "R", "mA"])
    if mode == "V":
        return calc_q(intro=f"A current of {clean(I)} A passes through a {comp} of resistance {clean(R)} Ω.", text=f"Calculate the voltage across the {comp}.",
                      eq="V = I × R", working=[f"V = {clean(I)} × {clean(R)}"], ans=num(V, 3), unit="V", prefix="voltage (V) = ", refs=["2.13"], d="1-3",
                      rearr=False, values={"I": I, "R": R, "V": V}, notes=alts(V),
                      state=("voltage, current and resistance", "voltage = current × resistance", None))
    if mode == "I":
        return calc_q(intro=f"There is a voltage of {num(V, 3)} V across a {comp} of resistance {clean(R)} Ω.", text=f"Calculate the current in the {comp}.",
                      eq="V = I × R", working=[f"{num(V, 3)} = I × {clean(R)}", f"I = {num(V, 3)} ÷ {clean(R)}"], ans=num(I, 2), unit="A",
                      prefix="current (A) = ", refs=["2.13"], d="4-6", values={"I": I, "R": R, "V": V}, notes=alts(I))
    if mode == "R":
        return calc_q(intro=f"The voltage across a {comp} is {num(V, 3)} V and the current is {clean(I)} A.", text=f"Calculate the resistance of the {comp}.",
                      eq="V = I × R", working=[f"{num(V, 3)} = {clean(I)} × R", f"R = {num(V, 3)} ÷ {clean(I)}"], ans=num(R, 3), unit="Ω",
                      prefix="resistance (Ω) = ", refs=["2.13"], d="4-6", values={"I": I, "R": R, "V": V}, notes=alts(R))
    ImA = I * 1000
    return calc_q(intro=f"An ammeter shows that the current in a {comp} is {clean(ImA)} mA when the voltage across it is {num(V, 3)} V.",
                  text=f"Calculate the resistance of the {comp}.", eq="V = I × R",
                  working=[f"I = {clean(ImA)} mA = {clean(I)} A", f"R = {num(V, 3)} ÷ {clean(I)}"], ans=num(R, 3), unit="Ω", prefix="resistance (Ω) = ",
                  refs=["2.13", "2.1"], d="7-9", values={"I": I, "R": R, "V": V}, notes=alts(R) + "; current must be converted to amperes")


@T(CI, "calc", 4, "ci-ldr")
def ci_ldr(r):
    sensor = pick(r, ["LDR", "thermistor"])
    Vs = pick(r, [6.0, 9.0, 12.0])
    Rf = pick(r, [100, 220, 470, 1000])
    Rs = pick(r, [150, 330, 680, 1500, 2200])
    I = Vs / (Rf + Rs)
    Vf = I * Rf
    cond = "in bright light" if sensor == "LDR" else "at room temperature"
    fig = {"type": "svg", "svg": S.circuit(["battery"], [["resistor", sensor.lower()]], labels={(0, 0): f"{Rf} Ω", (0, 1): sensor}), "width": 90,
           "caption": "Sensor circuit"}
    q = calc_q(intro=f"A {sensor} is connected in series with a {Rf} Ω resistor and a {clean(Vs)} V battery. {cond.capitalize()} the resistance of the {sensor} is {Rs} Ω.",
               text="Calculate the current in the circuit.", eq="V = I × R", working=[f"total R = {Rf} + {Rs} = {Rf + Rs} Ω", f"I = {clean(Vs)} ÷ {Rf + Rs}"],
               ans=num(I, 2), unit="A", prefix="current (A) = ", refs=["2.13", "2.19", "2.11"], d="7-9", values={"I": I, "Vf": Vf},
               notes=alts(I) + "; rearrangement mark for adding resistances", figs=[fig])
    change = "it gets darker" if sensor == "LDR" else "the temperature falls"
    q["parts"][0]["label"] = "a"
    for rw in q["rows"]:
        rw["part"] = "(a)"
    q["parts"].append(line_part("b", f"State and explain what happens to the current when {change}.", 2, 2))
    q["rows"] += [row("(b)", "current decreases;", 1), row("(b)", f"because the resistance of the {sensor} increases;", 1)]
    return q


@T(CI, "practical", 7, "ci-prac-iv")
def ci_prac_iv(r):
    comp = pick(r, ["filament lamp", "fixed resistor", "diode", "length of nichrome wire"])
    sym = {"filament lamp": "lamp", "fixed resistor": "resistor", "diode": "diode", "length of nichrome wire": "resistor"}[comp]
    fig = {"type": "svg", "svg": S.circuit(["battery"], [["varres", sym, "ammeter"]], voltmeters=[(0, 1)]), "width": 95, "caption": "Circuit used"}
    parts = [line_part("a", "Name the component that the student uses to change the current in the circuit.", 1, 1),
             line_part("b", "State **two** readings the student must record each time.", 2, 2),
             line_part("c", "Explain why the student should switch off the circuit between readings.", 2, 2),
             line_part("d", f"Describe how the student should use the results to show how the resistance of the {comp} varies with current.", 2, 3)]
    rows = [row("(a)", "variable resistor / rheostat;", 1, None, "AO3"),
            row("(b)", "current (from ammeter);", 1, None, "AO3"), row("(b)", "voltage/potential difference (from voltmeter);", 1, None, "AO3"),
            row("(c)", "to stop the component/wires heating up;", 1, None, "AO3"), row("(c)", "because temperature changes the resistance (not a fair test);", 1, "allow battery runs down", "AO3"),
            row("(d)", "calculate R = V ÷ I for each pair of readings | allow plot I against V and compare gradients;", 1, None, "AO3"),
            row("(d)", "compare values of R / plot R against I;", 1, None, "AO3")]
    return dict(parts=parts, rows=rows, refs=["2.9", "2.13"], cmd="State", d="4-6", ao=["AO3"], figures=[fig],
                intro=f"A student uses the circuit shown to find out how the current through a {comp} depends on the voltage applied to it. She plans to take {pick(r, ['six', 'eight', 'ten'])} pairs of readings using a {pick(r, ['6 V battery', '12 V low-voltage supply', '4.5 V battery pack'])}.",
                answer={"method": "none", "values": {}, "checked": True})


@T(CI, "practical", 8, "ci-prac-ldr")
def ci_prac_ldr(r):
    sensor = pick(r, ["LDR", "thermistor"])
    ivar = "the distance of a lamp from the LDR" if sensor == "LDR" else "the temperature of the water"
    parts = [line_part("a", f"Describe how the student could investigate how the resistance of a {sensor} changes with {ivar.replace('the distance of a lamp from the LDR', 'light intensity').replace('the temperature of the water', 'temperature')}.", 4, 6),
             line_part("b", "Identify **one** control variable.", 1, 1),
             line_part("c", "Suggest **one** source of error and how to reduce it.", 2, 2)]
    if sensor == "LDR":
        mps = ("MP1. connect LDR to an ohmmeter / to a supply with ammeter and voltmeter;\nMP2. place a lamp at a measured distance from the LDR;\nMP3. change the distance in equal steps;\n"
               "MP4. measure the resistance (or V and I) each time;\nMP5. calculate R = V ÷ I;\nMP6. darken the room / shield from other light;\nMP7. repeat and find means;")
        ctrl = "same lamp/power of lamp / background light level / same LDR;"
        err = ("background light changes the readings;", "use a darkened room or a tube around the LDR;")
    else:
        mps = ("MP1. connect thermistor to an ohmmeter / to a supply with ammeter and voltmeter;\nMP2. place thermistor in a beaker of water with a thermometer;\nMP3. heat the water (or add hot water) to change temperature;\n"
               "MP4. measure resistance (or V and I) at regular temperature intervals;\nMP5. stir the water before each reading;\nMP6. calculate R = V ÷ I;\nMP7. repeat and find means;")
        ctrl = "same thermistor / same supply voltage / thermistor fully immersed;"
        err = ("thermistor and thermometer not at the same temperature;", "stir and wait before reading / place them close together;")
    rows = [row("(a)", "any four from:\n" + mps, 4, "marks can be awarded from a diagram", "AO3"),
            row("(b)", ctrl, 1, None, "AO3"), row("(c)", err[0], 1, None, "AO3"), row("(c)", err[1], 1, "improvement must match the error", "AO3")]
    ctx = pick(r, ["for a school science fair", "to design an automatic sensor", "as part of a project on sensors", "to calibrate a sensor for a weather station",
                   "to check a component from a kit"])
    return dict(parts=parts, rows=rows, refs=["2.11", "2.13"], cmd="Describe", d="4-6", ao=["AO3"],
                intro=f"A student investigates a {sensor} {ctx}.", answer={"method": "none", "values": {}, "checked": True})


@T(CI, "data", 7, "ci-data-iv")
def ci_data_iv(r):
    comp = pick(r, ["fixed resistor", "filament lamp"])
    Vs = [0, 1, 2, 3, 4, 5, 6]
    if comp == "fixed resistor":
        R = nice(r, 10, 50, 5)
        Is = [round(v / R + r.uniform(-0.004, 0.004), 3) for v in Vs]
    else:
        k = nice(r, 0.10, 0.25, 0.01)
        Is = [round(k * math.sqrt(v) + r.uniform(-0.003, 0.003), 3) for v in Vs]
    Is[0] = 0.0
    tab = {"type": "table", "headers": ["voltage in V"] + [str(v) for v in Vs], "rows": [["current in A"] + [f"{i:.3f}" for i in Is]],
           "caption": f"Results for a {comp}"}
    vq = pick(r, [2, 4, 5])
    iq = Is[vq]
    Rq = vq / iq
    parts = [{"label": "a", "text": "Plot a graph of current against voltage and draw the line or curve of best fit.", "marks": 4, "space": "graph"},
             work_part("b", f"Use the results to calculate the resistance of the {comp} at {vq} V.", 2, "resistance (Ω) = "),
             line_part("c", f"Describe what the graph shows about the resistance of the {comp} as the voltage increases.", 2, 2)]
    rows = [row("(a)", "suitable linear scales (points occupy more than half the grid);", 1, None, "AO3"),
            row("(a)", "axes labelled with quantities and units;", 1, None, "AO3"),
            row("(a)", "all points plotted to nearest half square;", 1, None, "AO3"),
            row("(a)", "straight line through origin;" if comp == "fixed resistor" else "smooth curve getting less steep;", 1, None, "AO3"),
            row("(b)", f"R = V ÷ I, e.g. {vq} ÷ {iq:.3f};", 1, None, "AO2"), row("(b)", f"{num(Rq, 3)} (Ω);", 1, alts(Rq), "AO2")]
    if comp == "fixed resistor":
        rows += [row("(c)", "resistance stays constant;", 1, None, "AO3"), row("(c)", "because the graph is a straight line through the origin / current proportional to voltage;", 1, None, "AO3")]
    else:
        rows += [row("(c)", "resistance increases;", 1, None, "AO3"), row("(c)", "because the gradient decreases / current increases less for each volt;", 1, None, "AO3")]
    return dict(parts=parts, rows=rows, refs=["2.9", "2.13"], cmd="Plot", d="4-6", ao=["AO2", "AO3"], figures=[tab],
                intro=f"A student measures the current in a {comp} for different voltages.", answer={"method": "python", "values": {"R": Rq, "I": Is}, "checked": True})


@T(CI, "data", 6, "ci-data-ldr")
def ci_data_ldr(r):
    ds = [10, 20, 30, 40, 50, 60]
    a = nice(r, 0.8, 2.0, 0.1)
    b = nice(r, 0.2, 0.8, 0.1)
    Rs = [round(b + a * (d / 10) ** 1.5 * 0.4, 2) for d in ds]
    tab = {"type": "table", "headers": ["distance of lamp in cm"] + [str(d) for d in ds], "rows": [["resistance of LDR in kΩ"] + [f"{x:.2f}" for x in Rs]],
           "caption": "Results"}
    dq = pick(r, [25, 35, 45])
    Rq = b + a * (dq / 10) ** 1.5 * 0.4
    parts = [{"label": "a", "text": "Plot a graph of resistance against distance and draw a curve of best fit.", "marks": 4, "space": "graph"},
             line_part("b", f"Use your graph to estimate the resistance when the lamp is {dq} cm from the LDR.", 1, 1, prefix="resistance = "),
             line_part("c", "Write a conclusion for this investigation.", 2, 2)]
    rows = [row("(a)", "suitable linear scales (points occupy more than half the grid);", 1, None, "AO3"),
            row("(a)", "axes labelled with quantities and units;", 1, None, "AO3"),
            row("(a)", "all points plotted to nearest half square;", 1, None, "AO3"),
            row("(a)", "smooth curve of best fit;", 1, None, "AO3"),
            row("(b)", f"{sf(Rq * 0.93, 2)} to {sf(Rq * 1.07, 2)} (kΩ);", 1, "allow ecf from curve", "AO3"),
            row("(c)", "as the lamp moves further away (light gets dimmer) the resistance increases;", 1, None, "AO3"),
            row("(c)", "the increase is not proportional / gets larger at greater distances;", 1, None, "AO3")]
    return dict(parts=parts, rows=rows, refs=["2.11"], cmd="Plot", d="4-6", ao=["AO3"], figures=[tab],
                intro="A student measures the resistance of an LDR as a lamp is moved further away from it in a dark room.",
                answer={"method": "python", "values": {"R_at": Rq}, "checked": True})


DIAG_TASKS = [
    ("lamp", "measure the current in and the voltage across a lamp, and change the current using a variable resistor",
     ["cell/battery and lamp in series", "ammeter in series", "voltmeter in parallel with the lamp", "variable resistor in series"]),
    ("resistor", "find the resistance of a resistor",
     ["cell/battery and resistor in series", "ammeter in series", "voltmeter in parallel with the resistor"]),
    ("lamp", "light two lamps that can be switched on and off independently from one battery",
     ["battery with two lamps in parallel", "a switch in each branch", "correct symbols used"]),
    ("diode", "show that a diode lets current pass in one direction only, using a lamp as an indicator",
     ["cell, diode and lamp in series", "diode symbol correct", "lamp used as indicator"]),
    ("ldr", "make a lamp brighter when it gets darker, using an LDR",
     ["battery, LDR and resistor in series (potential divider)", "lamp connected in parallel with the LDR", "correct LDR symbol"]),
    ("thermistor", "measure the resistance of a thermistor at different temperatures",
     ["thermistor in series with an ammeter and battery", "voltmeter across the thermistor", "correct thermistor symbol"]),
]


@T(CI, "diagram", 7, "ci-draw")
def ci_draw(r):
    comp, task, pts = pick(r, DIAG_TASKS)
    m = len(pts)
    who = pick(r, ["A student", "A technician", "An engineer", "A pupil"])
    parts = [{"label": "", "text": f"{who} wants to {task}.\n\nDraw a circuit diagram that could be used. Use the correct circuit symbols.", "marks": m, "space": "box", "lines": 8}]
    rows = [row("", p + ";", 1, "ignore extra components that do not stop the circuit working" if i == 0 else None) for i, p in enumerate(pts)]
    return dict(parts=parts, rows=rows, refs=["2.9", "2.7", "2.12"] if comp != "ldr" else ["2.11", "2.12"], cmd="Draw", d="4-6", ao=["AO1", "AO3"],
                answer={"method": "none", "values": {}, "checked": True})


@T(CI, "diagram", 6, "ci-read")
def ci_read(r):
    n = pick(r, [2, 3])
    kind = pick(r, ["series", "parallel"])
    V = pick(r, [3.0, 4.5, 6.0, 9.0, 12.0])
    Rs = [pick(r, [2, 3, 4, 5, 6, 8, 10, 12]) for _ in range(n)]
    if kind == "series":
        fig = {"type": "svg", "svg": S.circuit(["battery"], [["resistor"] * n + ["ammeter"]], labels={(0, i): f"{x} Ω" for i, x in enumerate(Rs)}),
               "width": 100, "caption": "Circuit"}
        I = V / sum(Rs)
        ans = f"{num(I, 2)} A"
        rows = [row("(a)", "total resistance = sum of resistances;", 1), row("(a)", f"{sum(Rs)} Ω used and I = {num(I, 2)} (A);", 1, alts(I))]
        vals = {"I": I}
        txt = "Calculate the reading on the ammeter."
    else:
        fig = {"type": "svg", "svg": S.circuit(["battery", "ammeter"], [["resistor"] for _ in range(n)], labels={(i, 0): f"{x} Ω" for i, x in enumerate(Rs)}),
               "width": 100, "caption": "Circuit"}
        Is = [V / x for x in Rs]
        I = sum(Is)
        rows = [row("(a)", f"current in each branch found using I = V/R with V = {clean(V)} V;", 1), row("(a)", f"total = {num(I, 3)} (A);", 1, alts(I))]
        vals = {"I": I, "branches": Is}
        txt = "Calculate the reading on the ammeter."
    parts = [work_part("a", txt, 2, "current (A) = "),
             line_part("b", f"State the voltage across the first resistor{' if the voltage is shared in proportion to resistance' if kind == 'series' else ''}.", 1, 1, prefix="voltage = "),
             {"label": "c", "text": "On the diagram, draw a voltmeter connected to measure the voltage across the first resistor.", "marks": 1, "space": "none"}]
    if kind == "series":
        v1 = V * Rs[0] / sum(Rs)
        rows.append(row("(b)", f"{num(v1, 3)} (V);", 1, "allow ecf: answer (a) × first resistance"))
    else:
        v1 = V
        rows.append(row("(b)", f"{clean(V)} (V);", 1, "voltage is the same across parallel branches"))
    rows.append(row("(c)", "voltmeter symbol drawn in parallel across the first resistor only;", 1))
    vals["V1"] = v1
    return dict(parts=parts, rows=rows, refs=["2.19", "2.18", "2.13"], cmd="Calculate", d="7-9" if kind == "parallel" else "4-6", ao=["AO2"],
                intro=f"The diagram shows {n} resistors connected in {kind} to a {clean(V)} V battery.", figures=[fig],
                answer={"method": "python", "values": vals, "checked": True})


# ====================================================================== charge

@T(CH, "calc", 5, "ch-qit")
def ch_qit(r):
    ctx = pick(r, ["a phone charger", "a torch bulb", "an electric motor", "a heating element", "a car starter motor", "an LED"])
    I = nice(r, 0.02, 4.0, 0.02) if ctx != "a car starter motor" else nice(r, 80, 200, 10)
    unit_t = pick(r, ["s", "minutes", "hours"])
    t = {"s": r.randint(5, 120), "minutes": r.randint(2, 30), "hours": r.randint(1, 6)}[unit_t]
    ts = t * {"s": 1, "minutes": 60, "hours": 3600}[unit_t]
    Q = I * ts
    mode = r.choice(["Q", "I"])
    if mode == "Q":
        q = calc_q(intro=f"There is a current of {clean(I)} A in {ctx} for {t} {unit_t}.", text="Calculate the charge that flows.", eq="Q = I × t",
                   working=([f"t = {ts} s"] if unit_t != "s" else []) + [f"Q = {clean(I)} × {ts}"], ans=num(Q, 3), unit="C", prefix="charge (C) = ",
                   refs=["2.15", "2.1"], d="4-6" if unit_t != "s" else "1-3", rearr=False, values={"I": I, "t": ts, "Q": Q}, notes=alts(Q),
                   state=("charge, current and time", "charge = current × time", None))
        return q
    return calc_q(intro=f"A charge of {num(Q, 3)} C flows through {ctx} in {t} {unit_t}.", text="Calculate the current.", eq="Q = I × t",
                  working=([f"t = {ts} s"] if unit_t != "s" else []) + [f"{num(Q, 3)} = I × {ts}", f"I = {num(Q, 3)} ÷ {ts}"], ans=num(I, 2), unit="A",
                  prefix="current (A) = ", refs=["2.15"], d="7-9" if unit_t != "s" else "4-6", values={"Q": Q, "t": ts, "I": I}, notes=alts(I))


@T(CH, "calc", 4, "ch-eqv")
def ch_eqv(r):
    V = pick(r, [1.5, 3.0, 4.5, 6.0, 9.0, 12, 230])
    Q = nice(r, 2, 600, 2)
    E = Q * V
    mode = r.choice(["E", "V", "Q"])
    dev = pick(r, ["a lamp", "a battery-powered fan", "a heater", "a buzzer", "an electric drill"])
    if mode == "E":
        return calc_q(intro=f"{dev.capitalize()} is connected to a {clean(V)} V supply. {clean(Q)} C of charge passes through it.", text="Calculate the energy transferred.",
                      eq="E = Q × V", working=[f"E = {clean(Q)} × {clean(V)}"], ans=num(E, 3), unit="J", prefix="energy (J) = ", refs=["2.21"], d="1-3",
                      rearr=False, values={"Q": Q, "V": V, "E": E}, notes=alts(E),
                      state=("energy transferred, charge and voltage", "energy transferred = charge × voltage", None))
    if mode == "V":
        return calc_q(intro=f"When {clean(Q)} C of charge passes through {dev}, {num(E, 3)} J of energy is transferred.", text="Calculate the voltage across it.",
                      eq="E = Q × V", working=[f"{num(E, 3)} = {clean(Q)} × V", f"V = {num(E, 3)} ÷ {clean(Q)}"], ans=num(V, 3), unit="V", prefix="voltage (V) = ",
                      refs=["2.21", "2.20"], d="4-6", values={"Q": Q, "V": V, "E": E}, notes=alts(V))
    I = nice(r, 0.1, 3.0, 0.1)
    t = Q / I
    return calc_q(intro=f"{dev.capitalize()} works from a {clean(V)} V supply and transfers {num(E, 3)} J of energy. The current is {clean(I)} A.",
                  text="Calculate the time for which it was switched on.", eq="E = Q × V and Q = I × t",
                  working=[f"Q = {num(E, 3)} ÷ {clean(V)} = {clean(Q)} C", f"t = {clean(Q)} ÷ {clean(I)}"], ans=num(t, 3), unit="s", prefix="time (s) = ",
                  refs=["2.21", "2.15"], d="7-9", values={"Q": Q, "t": t}, notes=alts(t) + "; allow use of E = IVt")


@T(CH, "calc", 4, "ch-series")
def ch_series(r):
    V = pick(r, [6.0, 9.0, 12.0, 4.5])
    R1, R2 = pick(r, [(2, 4), (3, 6), (5, 10), (4, 8), (10, 20), (6, 12), (3, 9), (15, 30), (20, 40), (2, 10)])
    if r.random() < 0.5:
        R1, R2 = R2, R1
    I = V / (R1 + R2)
    V2 = I * R2
    fig = {"type": "svg", "svg": S.circuit(["battery"], [["resistor", "resistor", "ammeter"]], labels={(0, 0): f"{R1} Ω", (0, 1): f"{R2} Ω"}),
           "width": 100, "caption": "Series circuit"}
    q = calc_q(intro=f"A {R1} Ω resistor and a {R2} Ω resistor are connected in series with a {clean(V)} V battery.", text="Calculate the current in the circuit.",
               eq="V = I × R", working=[f"R = {R1} + {R2} = {R1 + R2} Ω", f"I = {clean(V)} ÷ {R1 + R2}"], ans=num(I, 3), unit="A", prefix="current (A) = ",
               refs=["2.19", "2.13"], d="4-6", values={"I": I, "V2": V2}, notes=alts(I), figs=[fig])
    q["parts"][0]["label"] = "a"
    for rw in q["rows"]:
        rw["part"] = "(a)"
    q["parts"].append(work_part("b", f"Calculate the voltage across the {R2} Ω resistor.", 2, "voltage (V) = "))
    q["rows"] += [row("(b)", f"substitution: V = {num(I, 3)} × {R2};", 1, "allow ecf from (a)"), row("(b)", f"{num(V2, 3)} (V);", 1)]
    return q


# ====================================================================== static practical

@T(ST, "practical", 13, "st-prac")
def st_prac(r):
    rods = r.sample([("polythene", "-"), ("acetate", "+"), ("perspex", "+"), ("glass", "+"), ("ebonite", "-"), ("PVC", "-")], 3)
    first = rods[0]
    tab = {"type": "table", "headers": ["rod brought near the suspended " + first[0] + " rod", "observation"],
           "rows": [[name, "repels" if s == first[1] else "attracts"] for name, s in rods[1:]] + [[first[0] + " (second rod)", "repels"]],
           "caption": "Results"}
    parts = [line_part("a", f"Describe how the student should charge the {first[0]} rod and suspend it so that it is free to move.", 2, 3),
             line_part("b", "Explain the observations in the table.", 3, 5),
             line_part("c", "Suggest why the experiment works less well on a humid day.", 1, 2),
             line_part("d", "State why a metal rod held in the hand cannot be charged in this way.", 1, 2)]
    rows = [row("(a)", "rub the rod with a (dry) cloth;", 1, None, "AO3"), row("(a)", "hang it from a thread/in a paper stirrup;", 1, None, "AO3"),
            row("(b)", "like charges repel / identical rods have the same charge;", 1, None, "AO1"),
            row("(b)", "unlike charges attract;", 1, None, "AO1"),
            row("(b)", f"the {first[0]} rod has a {'negative' if first[1] == '-' else 'positive'} charge because it {'gained' if first[1] == '-' else 'lost'} electrons;", 1, "allow rods that attract it have the opposite charge", "AO2"),
            row("(c)", "moisture in the air lets charge leak away;", 1, None, "AO3"),
            row("(d)", "metal is a conductor so charge flows through the person to earth;", 1, None, "AO1")]
    return dict(parts=parts, rows=rows, refs=["2.23P", "2.24P", "2.25P", "2.22P"], cmd="Describe", d="4-6", ao=["AO1", "AO2", "AO3"], figures=[tab],
                intro=f"A student suspends a charged {first[0]} rod and brings other charged rods near it, one at a time.",
                answer={"method": "lookup", "values": {"rods": [x[0] for x in rods]}, "checked": True})
