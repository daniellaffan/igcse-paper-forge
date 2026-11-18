"""Topic 4: Energy resources and energy transfers."""
import physics_svg as S
from physics_util import (K, M, X, T, kb, calc_q, line_part, work_part, row, num, sf, clean, pick, nice, alts)

TR, TH, WO, RE = ("physics.energy.transfers", "physics.energy.thermal", "physics.energy.work", "physics.energy.resources")

kb(TR, ["energy in the home", "energy in devices", "efficiency of machines", "energy stores", "wasted energy"],
   mcq=[
       M("Which of these is an energy store?", ["kinetic", "electrical", "light", "sound"], "4.2", why="electrical, light and sound are ways of transferring energy, not stores"),
       M("A lamp transfers 100 J of electrical energy and gives out 20 J of light. What is its efficiency?", ["20%", "80%", "0.8%", "5%"], "4.4", ao="AO2"),
       M("Which statement about energy is correct?", ["energy cannot be created or destroyed", "energy is used up by devices", "wasted energy disappears", "efficient devices create energy"], "4.3"),
       M("What is the unit of energy?", ["joule", "watt", "newton", "volt"], "4.1"),
       M("In a Sankey diagram, the width of each arrow represents", ["the amount of energy", "the time taken", "the efficiency", "the power of the device"], "4.5", d="4-6"),
       M("A stretched spring stores energy in which store?", ["elastic potential", "chemical", "thermal", "nuclear"], "4.2"),
       M("Energy is transferred from a battery to a motor mainly", ["electrically", "by heating", "by radiation", "mechanically"], "4.2", d="4-6"),
       M("What is the efficiency of a device that wastes 30 J for every 120 J supplied?", ["75%", "25%", "30%", "90%"], "4.4", ao="AO2", d="4-6"),
   ],
   recall=[
       K("State the principle of conservation of energy.", 1, ["energy cannot be created or destroyed, only transferred between stores"], "4.3", cmd="State"),
       K("State the equation linking efficiency, useful energy output and total energy input.", 1, ["efficiency = useful energy output ÷ total energy output | allow total energy input; allow × 100%"], "4.4", cmd="State"),
       K("Name **two** energy stores.", 2, ["kinetic", "chemical", "gravitational potential", "elastic potential", "nuclear", "thermal | allow internal", "magnetic", "electrostatic"], "4.2", cmd="Name"),
       K("Name **two** ways energy can be transferred between stores.", 2, ["mechanically (by forces)", "electrically", "by heating", "by radiation (light, sound, EM waves)"], "4.2", cmd="Name"),
       K("State what usually happens to wasted energy.", 1, ["spreads out into the surroundings as thermal energy | allow dissipated / heats the surroundings"], "4.3", cmd="State"),
       K("State the main energy store that increases when a car brakes to a stop.", 1, ["thermal store of the brakes and surroundings"], "4.2", cmd="State", d="4-6"),
   ],
   describe=[
       K("Describe the energy transfers when a battery-powered torch is switched on.", 3, ["chemical store in the battery", "transferred electrically to the bulb", "light (useful) and thermal (wasted) by radiation/heating"], "4.2 4.5", cmd="Describe"),
       K("Describe the energy transfers for a ball dropped from a height until just before it hits the ground.", 2, ["gravitational potential store decreases", "kinetic store increases (some to thermal by air resistance)"], "4.2 4.3", cmd="Describe"),
       K("Describe the energy transfers in an electric kettle.", 2, ["electrical energy transferred to thermal store of the water", "some wasted heating the kettle and surroundings / sound"], "4.5", cmd="Describe"),
       K("Describe the energy transfers when a person climbs a flight of stairs.", 2, ["chemical store in muscles decreases", "gravitational potential store increases; some thermal wasted"], "4.2", cmd="Describe"),
       K("Describe what a Sankey diagram shows.", 2, ["energy input and how it is split into useful and wasted outputs", "the width of each arrow is proportional to the energy"], "4.5", cmd="Describe", d="4-6"),
       K("Describe the energy transfers in a car engine.", 3, ["chemical store of the fuel", "transferred to kinetic store of the car", "much wasted as thermal energy (and sound)"], "4.2 4.5", cmd="Describe"),
   ])

kb(TH, ["keeping warm", "heating a room", "insulating a house", "cooking", "the vacuum flask", "sea breezes"],
   mcq=[
       M("By which process does energy travel from the Sun to the Earth?", ["radiation", "conduction", "convection", "evaporation"], "4.6"),
       M("Which surface is the best emitter of infrared radiation?", ["dull black", "shiny silver", "shiny white", "dull white"], "4.8"),
       M("Convection cannot happen in", ["solids", "liquids", "gases", "air"], "4.6 4.7"),
       M("Why is the heating element at the bottom of a kettle?", ["hot water rises, setting up a convection current", "heat sinks downwards", "conduction only works downwards", "radiation is strongest at the bottom"], "4.7", d="4-6"),
       M("Which material is the best thermal conductor?", ["copper", "wood", "air", "plastic"], "4.6"),
       M("Loft insulation reduces energy transfer mainly because it", ["traps air, a poor conductor", "reflects all radiation", "is a good conductor", "absorbs convection currents"], "4.10", d="4-6"),
       M("A hot object cools fastest when its surface is", ["dull black and very hot", "shiny and very hot", "dull black and warm", "shiny and warm"], "4.8", d="7-9"),
   ],
   recall=[
       K("Name the **three** ways thermal energy can be transferred.", 2, ["conduction, convection and radiation | all three for 2 marks; any two for 1 mark", "(all three correct)"], "4.6", cmd="Name"),
       K("Name the type of surface that is the best absorber of infrared radiation.", 1, ["dull/matt black"], "4.8", cmd="Name"),
       K("State **two** ways of reducing energy transfer from a house.", 2, ["loft insulation", "cavity wall insulation", "double glazing", "draught excluders", "carpets / curtains"], "4.10", cmd="State"),
       K("State why metals are good thermal conductors.", 1, ["free/delocalised electrons transfer energy quickly | allow particles close together"], "4.6", cmd="State", d="4-6"),
       K("State which type of thermal energy transfer can take place through a vacuum.", 1, ["radiation | allow infrared"], "4.6", cmd="State"),
       K("Name a material that is a good thermal insulator.", 1, ["air / plastic / wood / wool / polystyrene"], "4.6", cmd="Name"),
   ],
   describe=[
       K("Describe how energy is transferred through a metal bar by conduction.", 3, ["particles at the hot end vibrate more", "pass energy to neighbouring particles", "free electrons move and carry energy through the metal"], "4.6", cmd="Describe", d="4-6"),
       K("Describe how a convection current is set up in a room by a heater.", 3, ["air near heater is warmed and expands", "becomes less dense and rises", "cooler, denser air sinks to replace it"], "4.7", cmd="Describe"),
       K("Describe how a sea breeze forms during a sunny day.", 3, ["land heats up faster than the sea", "warm air above the land rises", "cooler air from over the sea moves in to replace it"], "4.7", cmd="Describe", d="7-9"),
       K("Describe how you could show that a dull black surface emits more radiation than a shiny surface.", 3, ["use a Leslie cube / two identical cans filled with the same hot water", "measure radiation with an infrared detector/thermometer at the same distance", "black surface gives the higher reading"], "4.8 4.9", cmd="Describe", ao="AO3"),
   ],
   explain=[
       K("Explain why double glazing reduces energy transfer from a house.", 2, ["the gap contains air / a vacuum", "air is a poor conductor and the gap is too narrow for convection | vacuum stops conduction and convection"], "4.10", cmd="Explain"),
       K("Explain why houses in hot countries are often painted white.", 2, ["white surfaces are poor absorbers / good reflectors of infrared", "so the house warms up less"], "4.8", cmd="Explain"),
       K("Explain why cooling fins on an engine are painted black.", 2, ["black surfaces are good emitters of infrared", "so engine loses energy faster"], "4.8", cmd="Explain", d="4-6"),
       K("Explain why a fluffy jumper keeps you warm.", 2, ["it traps air", "air is a poor conductor and trapped air cannot form convection currents"], "4.6 4.10", cmd="Explain"),
       K("Explain why a metal spoon feels colder than a wooden spoon at the same temperature.", 2, ["metal is a better conductor", "it transfers energy away from your hand faster"], "4.6", cmd="Explain", d="7-9"),
       K("Explain why the freezer compartment is at the top of a refrigerator.", 2, ["cold air is denser and sinks", "sets up a convection current which cools the whole fridge"], "4.7", cmd="Explain", d="4-6"),
   ],
   extended=[
       X("A vacuum flask keeps hot drinks hot. Explain how its design reduces energy transfer by conduction, convection and radiation.",
         ["vacuum between the walls", "no particles, so no conduction across the gap", "no convection across the gap", "silvered surfaces reflect infrared back into the drink",
          "shiny outer surface is a poor emitter", "stopper made of plastic/cork, a poor conductor", "stopper prevents convection/evaporation from the top", "thin glass walls limit conduction",
          "supports made of insulating material"], "4.6 4.8 4.10"),
       X("Explain how a house can be designed to reduce energy losses in winter. Refer to conduction, convection and radiation.",
         ["loft insulation traps air", "air is a poor conductor", "trapped air cannot form convection currents", "cavity wall insulation (foam) fills the gap and stops convection",
          "double glazing: air or vacuum gap reduces conduction", "draught excluders stop warm air escaping (convection)", "foil behind radiators reflects infrared back into the room",
          "thick curtains trap a layer of air", "carpets reduce conduction through floor"], "4.6 4.10"),
   ])

kb(WO, ["lifting loads", "moving vehicles", "falling objects", "roller coasters", "power of machines"],
   mcq=[
       M("What is the unit of power?", ["watt", "joule", "newton", "pascal"], "4.1 4.16"),
       M("A force of 20 N moves a box 3 m along the floor. How much work is done?", ["60 J", "6.7 J", "23 J", "17 J"], "4.11", ao="AO2"),
       M("A 2 kg mass is lifted 5 m. What is its gain in gravitational potential energy? (g = 10 N/kg)", ["100 J", "10 J", "50 J", "20 J"], "4.13", ao="AO2"),
       M("A 4 kg object moves at 3 m/s. What is its kinetic energy?", ["18 J", "12 J", "36 J", "6 J"], "4.14", ao="AO2", d="4-6"),
       M("Power is", ["the rate of doing work", "the force times distance", "the total energy transferred", "energy times time"], "4.16"),
       M("If the speed of a car doubles, its kinetic energy", ["is four times as big", "doubles", "halves", "stays the same"], "4.14", d="7-9"),
       M("Work done is equal to", ["energy transferred", "power transferred", "force divided by distance", "momentum gained"], "4.12"),
   ],
   recall=[
       K("State the equation linking work done, force and distance moved.", 1, ["work done = force × distance moved | allow W = F × d"], "4.11", cmd="State"),
       K("State the equation linking gravitational potential energy, mass, g and height.", 1, ["GPE = m × g × h"], "4.13", cmd="State"),
       K("State the equation linking kinetic energy, mass and speed.", 1, ["KE = ½ × m × v²"], "4.14", cmd="State"),
       K("State the equation linking power, work done and time taken.", 1, ["power = work done ÷ time taken"], "4.17", cmd="State"),
       K("State what is meant by *power*.", 1, ["the rate of transferring energy / doing work"], "4.16", cmd="State"),
       K("State the unit of work done.", 1, ["joule / J | allow N m"], "4.1 4.12", cmd="State"),
   ],
   explain=[
       K("A ball is dropped and bounces. Explain why it does not return to its original height.", 2, ["some energy is transferred to thermal store (and sound) on impact / by air resistance", "so less energy in GPE store at the top"], "4.15 4.3", cmd="Explain"),
       K("Explain why a roller coaster car's speed is greatest at the lowest point of the track.", 2, ["GPE is lowest there", "so most energy has been transferred to the kinetic store"], "4.15", cmd="Explain"),
       K("Two students climb the same stairs. Explain why the faster student has a greater power.", 2, ["same work done (if same weight)", "in less time, so energy transferred per second is greater"], "4.16 4.17", cmd="Explain", d="4-6"),
       K("Explain why doubling the speed of a car has a large effect on its braking distance.", 3, ["KE = ½mv² so KE is four times as big", "work done by brakes = force × distance", "same braking force needs four times the distance"], "4.14 4.11", cmd="Explain", d="7-9"),
       K("Explain why no work is done when you hold a heavy box still.", 2, ["work = force × distance moved", "box does not move, so distance is zero"], "4.11", cmd="Explain", d="4-6"),
   ])

kb(RE, ["generating electricity", "renewable energy", "power stations", "choosing an energy resource", "energy for a remote island"],
   mcq=[
       M("Which energy resource is non-renewable?", ["natural gas", "wind", "solar", "tidal"], "4.19P"),
       M("In a coal-fired power station, the steam is used to", ["turn a turbine", "cool the generator", "burn the coal", "make the fuel"], "4.18P"),
       M("Which energy resource uses the Earth's hot rocks?", ["geothermal", "hydroelectric", "nuclear", "tidal"], "4.18P"),
       M("Which is a disadvantage of wind turbines?", ["they do not generate when there is no wind", "they release carbon dioxide", "they use fuel", "they produce radioactive waste"], "4.19P"),
       M("A solar cell transfers energy from", ["light to electrical", "thermal to kinetic", "chemical to electrical", "kinetic to electrical"], "4.18P"),
       M("In a hydroelectric station, water falling through the dam transfers energy from", ["gravitational potential to kinetic", "chemical to thermal", "kinetic to nuclear", "thermal to gravitational"], "4.18P", d="4-6"),
       M("Which resource releases energy by nuclear fission?", ["nuclear power station using uranium", "gas power station", "geothermal plant", "biomass plant"], "4.18P"),
   ],
   recall=[
       K("Name **two** renewable energy resources.", 2, ["wind", "solar", "hydroelectric", "tidal", "wave", "geothermal", "biomass"], "4.19P", cmd="Name"),
       K("Name **two** fossil fuels.", 2, ["coal", "oil", "natural gas"], "4.19P", cmd="Name"),
       K("State what is meant by a *renewable* energy resource.", 1, ["one that will not run out / is replaced as fast as it is used"], "4.19P", cmd="State"),
       K("Give **one** advantage of using nuclear power stations.", 1, ["no carbon dioxide released | allow reliable; large output from small mass of fuel"], "4.19P", cmd="Give"),
       K("Give **one** disadvantage of burning fossil fuels.", 1, ["releases carbon dioxide (climate change) | allow sulfur dioxide / acid rain; non-renewable"], "4.19P", cmd="Give"),
       K("Name the device in a power station that transfers kinetic energy into electrical energy.", 1, ["generator"], "4.18P", cmd="Name"),
   ],
   describe=[
       K("Describe how electricity is generated in a gas-fired power station.", 3, ["gas is burned to heat water and produce steam", "steam turns a turbine", "turbine turns a generator"], "4.18P", cmd="Describe"),
       K("Describe the energy transfers in a wind turbine.", 2, ["kinetic store of the wind to kinetic store of the blades", "generator transfers this electrically"], "4.18P", cmd="Describe"),
       K("Describe how a hydroelectric power station generates electricity.", 3, ["water stored behind a dam has gravitational potential energy", "water flows down and turns turbines", "turbines turn generators"], "4.18P", cmd="Describe"),
       K("Describe how a geothermal power station works.", 2, ["water pumped down to hot rocks and returns as steam", "steam turns a turbine and generator"], "4.18P", cmd="Describe"),
   ],
   explain=[
       K("Explain why solar cells are not used on their own to supply a town with electricity.", 2, ["output depends on sunlight / none at night", "so supply is unreliable (need storage or backup)"], "4.19P", cmd="Explain"),
       K("Explain why tidal power is more reliable than wind power.", 2, ["tides happen twice a day at predictable times", "wind speed is variable"], "4.19P", cmd="Explain", d="4-6"),
       K("Explain why building a hydroelectric dam can harm the environment.", 2, ["flooding a valley destroys habitats / homes", "changes the river flow downstream"], "4.19P", cmd="Explain"),
       K("Explain why gas power stations are often used to meet sudden rises in demand.", 2, ["they have a short start-up time", "so output can be increased quickly"], "4.19P", cmd="Explain", d="7-9"),
       K("Explain why biomass is described as carbon neutral.", 2, ["plants absorb carbon dioxide as they grow", "the same amount is released when burned"], "4.19P", cmd="Explain", d="7-9"),
   ],
   extended=[
       X("A government is choosing between a coal-fired power station and a wind farm to supply a region. Evaluate the two options.",
         ["coal: reliable, output can be controlled", "coal: large output from one site", "coal: releases carbon dioxide (climate change) and sulfur dioxide (acid rain)", "coal is non-renewable and will run out",
          "wind: renewable, no fuel cost", "wind: no carbon dioxide while running", "wind: unreliable, depends on wind speed", "wind: needs many turbines and a large area; visual/noise impact",
          "wind needs backup or storage", "conclusion linked to reasons"], "4.18P 4.19P"),
       X("Compare the generation of electricity using a nuclear power station and a solar farm.",
         ["nuclear: fission of uranium releases energy to heat water", "steam turns turbine and generator", "nuclear: no carbon dioxide released", "nuclear: reliable, high output",
          "nuclear: radioactive waste must be stored for a long time", "nuclear: high building and decommissioning costs; risk of accidents",
          "solar: light transferred directly to electrical energy", "solar: renewable, no fuel, no emissions", "solar: output varies with weather and none at night",
          "solar: large area needed for high output"], "4.18P 4.19P"),
   ])


# ====================================================================== transfers: efficiency calc and Sankey diagrams

DEV = [("filament lamp", "light", "thermal"), ("LED lamp", "light", "thermal"), ("electric motor", "kinetic", "thermal and sound"),
       ("television", "light and sound", "thermal"), ("loudspeaker", "sound", "thermal"), ("electric kettle", "thermal energy of the water", "thermal energy of the surroundings"),
       ("hair dryer", "thermal and kinetic", "sound"), ("car engine", "kinetic", "thermal"), ("phone charger", "electrical (to the phone)", "thermal")]


@T(TR, "calc", 14, "tr-eff")
def tr_eff(r):
    dev, use, waste = pick(r, DEV)
    tot = nice(r, 50, 2000, 10)
    eff = nice(r, 0.1, 0.95, 0.05)
    useful = tot * eff
    mode = r.choice(["eff", "useful", "waste"])
    if mode == "eff":
        return calc_q(intro=f"A {dev} is supplied with {clean(tot)} J of energy. It transfers {clean(useful)} J usefully as {use}.", text="Calculate the efficiency of the device.",
                      eq="efficiency = useful energy output ÷ total energy input", working=[f"efficiency = {clean(useful)} ÷ {clean(tot)}"],
                      ans=f"{sf(eff, 2)} or {clean(eff * 100)}%", unit="", prefix="efficiency = ", refs=["4.4"], d="1-3", rearr=False,
                      values={"efficiency": eff}, notes="allow decimal or percentage; reject a % sign on a decimal answer",
                      state=("efficiency, useful energy output and total energy output", "efficiency = useful energy output ÷ total energy output", None) if r.random() < 0.5 else None)
    if mode == "useful":
        return calc_q(intro=f"A {dev} has an efficiency of {clean(eff * 100)}%. It is supplied with {clean(tot)} J.", text=f"Calculate the useful energy output.",
                      eq="efficiency = useful ÷ total", working=[f"{sf(eff, 2)} = useful ÷ {clean(tot)}", f"useful = {sf(eff, 2)} × {clean(tot)}"],
                      ans=num(useful, 3), unit="J", prefix="useful energy (J) = ", refs=["4.4"], d="4-6", values={"useful": useful}, notes=alts(useful))
    wasted = tot - useful
    return calc_q(intro=f"A {dev} is {clean(eff * 100)}% efficient. Each second it wastes {clean(wasted)} J as {waste}.", text="Calculate the total energy supplied to it each second.",
                  eq="efficiency = useful ÷ total", working=[f"wasted fraction = {sf(1 - eff, 2)}", f"total = {clean(wasted)} ÷ {sf(1 - eff, 2)}"],
                  ans=num(tot, 3), unit="J", prefix="total energy (J) = ", refs=["4.4", "4.3"], d="7-9", values={"total": tot}, notes=alts(tot))


@T(TR, "diagram", 14, "tr-sankey")
def tr_sankey(r):
    dev, use, waste = pick(r, DEV)
    tot = pick(r, [100, 200, 250, 400, 500, 800, 1000, 1200])
    eff = nice(r, 0.1, 0.9, 0.05)
    u = round(tot * eff)
    w = tot - u
    fig = {"type": "svg", "svg": S.sankey(("input", tot), [("useful", u), ("wasted", w)]), "width": 100, "caption": f"Sankey diagram for a {dev} (not to scale)"}
    variant = r.choice(["read", "draw"])
    if variant == "read":
        parts = [line_part("a", "State the amount of energy wasted.", 1, 1, prefix="wasted energy (J) = "),
                 line_part("b", f"State the form of the wasted energy for a {dev}.", 1, 1),
                 work_part("c", "Calculate the efficiency of the device.", 2, "efficiency = ")]
        rows = [row("(a)", f"{w} J;", 1), row("(b)", f"{waste};", 1),
                row("(c)", f"{u} ÷ {tot};", 1, None, "AO2"), row("(c)", f"{sf(eff, 2)} / {clean(eff * 100)}%;", 1, "allow ecf from (a)", "AO2")]
        intro = f"The diagram shows how energy is transferred by a {dev}. The total input is {tot} J and the useful output is {u} J."
        figs = [fig]
    else:
        parts = [{"label": "a", "text": f"On the grid, draw a labelled Sankey diagram for the {dev}. Use a scale of one square for {tot // 10} J.", "marks": 3, "space": "graph"},
                 line_part("b", "Explain how your diagram shows that energy is conserved.", 1, 2)]
        rows = [row("(a)", f"input arrow {10} squares wide labelled {tot} J;", 1), row("(a)", f"useful arrow {sf(u / (tot / 10), 2)} squares labelled {use};", 1),
                row("(a)", f"wasted arrow {sf(w / (tot / 10), 2)} squares, bending away, labelled {waste};", 1),
                row("(b)", "widths of the output arrows add up to the width of the input arrow;", 1)]
        intro = f"A {dev} is supplied with {tot} J of electrical energy. It transfers {u} J usefully as {use}; the rest is wasted as {waste}."
        figs = None
    q = dict(parts=parts, rows=rows, refs=["4.5", "4.4", "4.3"], cmd="Draw" if variant == "draw" else "Calculate", d="4-6", ao=["AO1", "AO2"],
             intro=intro, answer={"method": "python", "values": {"useful": u, "wasted": w, "efficiency": eff}, "checked": True})
    if figs:
        q["figures"] = figs
    return q


# ====================================================================== thermal practical

@T(TH, "practical", 7, "th-prac-cans")
def th_prac(r):
    cols = r.sample(["matt black", "shiny silver", "white", "dull grey", "shiny black"], 2)
    t0 = nice(r, 70, 90, 5)
    mins = pick(r, [5, 10, 15])
    a_drop = nice(r, 10, 25, 1)
    b_drop = a_drop - nice(r, 3, 9, 1)
    first = cols[0] if ("black" in cols[0] and "shiny" not in cols[0]) or "silver" in cols[1] else cols[1]
    tab = {"type": "table", "headers": ["can", "start temperature in °C", f"temperature after {mins} min in °C"],
           "rows": [["A (" + cols[0] + ")", clean(t0), clean(t0 - a_drop)], ["B (" + cols[1] + ")", clean(t0), clean(t0 - b_drop)]], "caption": "Results"}
    parts = [line_part("a", "State the independent variable in this investigation.", 1, 1),
             line_part("b", "Give **two** variables that should be controlled.", 2, 2),
             work_part("c", "Calculate the temperature drop for each can.", 2, "A = ........ °C   B = "),
             line_part("d", "State which surface is the better emitter of radiation. Give a reason from the results.", 2, 2)]
    rows = [row("(a)", "colour/type of surface;", 1, None, "AO3"),
            row("(b)", "any two from:\nvolume/mass of water;\nstarting temperature;\nsize/material of can;\nroom temperature;\nlid used or not;", 2, None, "AO3"),
            row("(c)", f"A: {clean(a_drop)} °C;", 1, None, "AO2"), row("(c)", f"B: {clean(b_drop)} °C;", 1, None, "AO2"),
            row("(d)", f"{cols[0]} (can A);", 1, None, "AO3"), row("(d)", "its temperature fell more in the same time;", 1, None, "AO3")]
    return dict(parts=parts, rows=rows, refs=["4.8", "4.9"], cmd="State", d="4-6", ao=["AO2", "AO3"], figures=[tab],
                intro=f"A student fills two identical metal cans with hot water. Can A is painted {cols[0]} and can B is painted {cols[1]}. She records the temperature of each after {mins} minutes.",
                answer={"method": "python", "values": {"dropA": a_drop, "dropB": b_drop}, "checked": True})


@T(TH, "practical", 7, "th-prac-insul")
def th_prac_insul(r):
    mats = r.sample(["cotton wool", "bubble wrap", "newspaper", "felt", "polystyrene beads", "aluminium foil", "wool"], 3)
    t0 = nice(r, 60, 85, 5)
    drops = sorted(r.sample(range(6, 30), 3))
    tab = {"type": "table", "headers": ["insulating material", "temperature drop in 10 min in °C"], "rows": [[m, str(d)] for m, d in zip(mats, drops)], "caption": "Results"}
    parts = [line_part("a", "Describe a method the student could use to obtain these results.", 4, 6),
             line_part("b", "State which material is the best insulator. Give a reason.", 2, 2),
             line_part("c", "Suggest **one** improvement to the investigation.", 1, 2)]
    rows = [row("(a)", "any four from:\nMP1. wrap identical beakers with the same thickness of each material;\nMP2. pour the same volume of hot water into each;\nMP3. measure the starting temperature with a thermometer;\n"
                       "MP4. start the stopwatch;\nMP5. measure temperature again after 10 minutes;\nMP6. use a lid on each beaker;\nMP7. include an unwrapped control beaker;", 4, None, "AO3"),
            row("(b)", f"{mats[0]};", 1, None, "AO3"), row("(b)", "smallest temperature drop;", 1, None, "AO3"),
            row("(c)", "repeat and find mean / use a data logger / same starting temperature / take readings every minute;", 1, None, "AO3")]
    return dict(parts=parts, rows=rows, refs=["4.9", "4.10"], cmd="Describe", d="4-6", ao=["AO3"], figures=[tab],
                intro=f"A student compares how well three materials reduce energy transfer from a beaker of water at {clean(t0)} °C.",
                answer={"method": "none", "values": {"best": mats[0]}, "checked": True})


# ====================================================================== work / GPE / KE / power calcs

@T(WO, "calc", 4, "wo-work")
def wo_work(r):
    ctx = pick(r, [("pushes a shopping trolley", 20, 150), ("pulls a sledge", 30, 200), ("drags a box", 50, 400), ("pushes a car", 200, 800), ("tows a trailer", 500, 3000)])
    what, lo, hi = ctx
    F = nice(r, lo, hi, 10)
    d = nice(r, 2, 80, 1)
    W = F * d
    if r.random() < 0.5:
        return calc_q(intro=f"A person {what} with a force of {clean(F)} N for a distance of {clean(d)} m.", text="Calculate the work done.",
                      eq="W = F × d", working=[f"W = {clean(F)} × {clean(d)}"], ans=num(W, 3), unit="J", prefix="work done (J) = ", refs=["4.11"], d="1-3", rearr=False,
                      values={"W": W}, notes=alts(W), state=("work done, force and distance moved", "work done = force × distance moved", None))
    return calc_q(intro=f"A person {what}. {num(W, 3)} J of work is done when the object moves {clean(d)} m.", text="Calculate the force applied.",
                  eq="W = F × d", working=[f"{num(W, 3)} = F × {clean(d)}", f"F = {num(W, 3)} ÷ {clean(d)}"], ans=num(F, 3), unit="N", prefix="force (N) = ",
                  refs=["4.11"], d="4-6", values={"F": F}, notes=alts(F))


@T(WO, "calc", 4, "wo-gpe")
def wo_gpe(r):
    obj, mlo, mhi = pick(r, [("crate", 5, 80), ("climber", 50, 90), ("bag of cement", 20, 50), ("lift car", 400, 1200), ("ball", 0.1, 0.6), ("bucket of water", 5, 15)])
    m = nice(r, mlo, mhi, 0.1 if mhi < 1 else 1)
    h = nice(r, 1.5, 40, 0.5)
    E = m * 10 * h
    if r.random() < 0.6:
        return calc_q(intro=f"A {obj} of mass {clean(m)} kg is raised through a height of {clean(h)} m. (g = 10 N/kg)", text="Calculate the gain in gravitational potential energy.",
                      eq="GPE = m × g × h", working=[f"GPE = {clean(m)} × 10 × {clean(h)}"], ans=num(E, 3), unit="J", prefix="GPE (J) = ", refs=["4.13"], d="1-3",
                      rearr=False, values={"E": E}, notes=alts(E))
    return calc_q(intro=f"A {obj} of mass {clean(m)} kg gains {num(E, 3)} J of gravitational potential energy when lifted. (g = 10 N/kg)", text="Calculate the height it is lifted through.",
                  eq="GPE = m × g × h", working=[f"{num(E, 3)} = {clean(m)} × 10 × h", f"h = {num(E, 3)} ÷ ({clean(m)} × 10)"], ans=num(h, 3), unit="m",
                  prefix="height (m) = ", refs=["4.13"], d="4-6", values={"h": h}, notes=alts(h))


@T(WO, "calc", 4, "wo-ke")
def wo_ke(r):
    obj, mlo, mhi, vlo, vhi = pick(r, [("car", 800, 1500, 5, 30), ("cyclist and bicycle", 60, 100, 3, 12), ("tennis ball", 0.05, 0.06, 10, 50), ("lorry", 8000, 20000, 5, 25), ("runner", 50, 80, 3, 9)])
    m = nice(r, mlo, mhi, 0.001 if mhi < 1 else 10 if mhi > 500 else 1)
    v = nice(r, vlo, vhi, 0.5)
    E = 0.5 * m * v * v
    if r.random() < 0.6:
        return calc_q(intro=f"A {obj} of mass {clean(m)} kg moves at {clean(v)} m/s.", text="Calculate its kinetic energy.", eq="KE = ½ × m × v²",
                      working=[f"KE = 0.5 × {clean(m)} × {clean(v)}²"], ans=num(E, 3), unit="J", prefix="kinetic energy (J) = ", refs=["4.14"], d="4-6", rearr=False,
                      values={"E": E}, notes=alts(E) + "; failure to square v loses the evaluation mark",
                      state=("kinetic energy, mass and speed", "KE = ½ × m × v²", None) if r.random() < 0.5 else None)
    return calc_q(intro=f"A {obj} of mass {clean(m)} kg has {num(E, 3)} J of kinetic energy.", text="Calculate its speed.", eq="KE = ½ × m × v²",
                  working=[f"{num(E, 3)} = 0.5 × {clean(m)} × v²", f"v² = {num(2 * E / m, 3)}", f"v = √{num(2 * E / m, 3)}"], ans=num(v, 3), unit="m/s",
                  prefix="speed (m/s) = ", refs=["4.14"], d="7-9", values={"v": v}, notes=alts(v))


@T(WO, "calc", 4, "wo-power")
def wo_power(r):
    dev, lo, hi, st = pick(r, [("crane", 2000, 20000, 500), ("electric motor", 50, 2000, 50), ("lift", 2000, 15000, 500),
                               ("student running upstairs", 300, 900, 10), ("winch", 500, 5000, 100), ("conveyor belt", 200, 3000, 100)])
    P = nice(r, lo, hi, st)
    t = nice(r, 2, 120, 1)
    W = P * t  # exact, so every printed value and the answer agree
    if r.random() < 0.5:
        return calc_q(intro=f"{'An' if dev[0] in 'aeiou' else 'A'} {dev} does {clean(W)} J of work in {clean(t)} s.", text="Calculate the power output.", eq="P = W ÷ t", working=[f"P = {clean(W)} ÷ {clean(t)}"],
                      ans=num(P, 3), unit="W", prefix="power (W) = ", refs=["4.17"], d="1-3", rearr=False, values={"P": P}, notes=alts(P),
                      state=("power, work done and time taken", "power = work done ÷ time taken", None))
    return calc_q(intro=f"{'An' if dev[0] in 'aeiou' else 'A'} {dev} has a useful power output of {num(P, 3)} W.", text=f"Calculate the time it takes to do {clean(W)} J of useful work.", eq="P = W ÷ t",
                  working=[f"{num(P, 3)} = {clean(W)} ÷ t", f"t = {clean(W)} ÷ {num(P, 3)}"], ans=num(t, 3), unit="s", prefix="time (s) = ", refs=["4.17", "4.16"],
                  d="4-6", values={"t": t}, notes=alts(t))


@T(WO, "calc", 6, "wo-cons")
def wo_cons(r):
    # (context, mass lo, hi, step in kg, height lo, hi, step in m) - realistic for each object
    ctx, mlo, mhi, mst, hlo, hhi, hst = pick(r, [
        ("A ball is dropped", 0.05, 0.6, 0.05, 1, 20, 0.5), ("A stone falls from a bridge", 0.1, 2, 0.1, 5, 30, 0.5),
        ("A diver steps off a board", 45, 90, 1, 1, 10, 0.5), ("An apple falls from a branch", 0.1, 0.3, 0.02, 1, 5, 0.5),
        ("A parcel slides off a shelf", 0.5, 10, 0.5, 1, 2.5, 0.1), ("A skateboarder rolls down a ramp", 40, 80, 1, 0.5, 4, 0.1)])
    m = nice(r, mlo, mhi, mst)
    h = nice(r, hlo, hhi, hst)
    v = (2 * 10 * h) ** 0.5
    parts = [work_part("a", "Calculate the loss in gravitational potential energy.", 2, "GPE (J) = "),
             work_part("b", "Assuming no air resistance, calculate the speed just before it reaches the bottom.", 3, "speed (m/s) = ")]
    E = m * 10 * h
    rows = [row("(a)", f"substitution: {clean(m)} × 10 × {clean(h)};", 1), row("(a)", f"{num(E, 3)} (J);", 1, alts(E)),
            row("(b)", "KE gained = GPE lost;", 1, "allow ecf from (a)"), row("(b)", f"{num(E, 3)} = 0.5 × {clean(m)} × v²;", 1),
            row("(b)", f"v = {num(v, 3)} (m/s);", 1, alts(v))]
    return dict(parts=parts, rows=rows, refs=["4.13", "4.14", "4.15"], cmd="Calculate", d="7-9", ao=["AO2"],
                intro=f"{ctx} through a vertical height of {clean(h)} m. Its mass is {clean(m)} kg. (g = 10 N/kg)",
                answer={"method": "python exact arithmetic", "values": {"E": E, "v": v}, "checked": True})
