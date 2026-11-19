"""Topic 8: Astrophysics."""
import math

import physics_svg as S
from physics_util import (K, M, X, T, kb, calc_q, line_part, work_part, row, num, sf, clean, pick, nice, alts)

UN, STR, CO = ("physics.astrophysics.universe", "physics.astrophysics.stars", "physics.astrophysics.cosmology")

kb(UN, ["the Solar System", "galaxies", "orbits", "satellites", "gravity on other worlds", "comets"],
   mcq=[
       M("What is the name of our galaxy?", ["the Milky Way", "Andromeda", "the Solar System", "the Local Group"], "8.2"),
       M("Which list is in order of increasing size?", ["planet, star, galaxy, universe", "star, planet, galaxy, universe", "galaxy, star, planet, universe", "universe, galaxy, star, planet"], "8.2"),
       M("What keeps the Moon in orbit around the Earth?", ["gravitational force", "magnetic force", "air resistance", "electrostatic force"], "8.4"),
       M("Why is the gravitational field strength on the Moon less than on the Earth?", ["the Moon has a smaller mass", "the Moon has no atmosphere", "the Moon is further from the Sun", "the Moon spins more slowly"], "8.3", d="4-6"),
       M("The orbit of a comet is usually", ["a very elongated ellipse", "a circle", "a straight line", "the same as the Earth's"], "8.5"),
       M("Where does a comet travel fastest?", ["closest to the Sun", "furthest from the Sun", "at the same speed everywhere", "halfway round its orbit"], "8.5", d="7-9"),
       M("A planet orbits the Sun at radius r with period T. Its orbital speed is", ["2πr ÷ T", "T ÷ 2πr", "2πT ÷ r", "πr² ÷ T"], "8.6"),
       M("A 2 kg mass is on a planet where g = 4 N/kg. What is its weight?", ["8 N", "2 N", "0.5 N", "20 N"], "8.3 1.18", ao="AO2"),
   ],
   recall=[
       K("State the equation linking orbital speed, orbital radius and time period.", 1, ["orbital speed = (2 × π × orbital radius) ÷ time period"], "8.6", cmd="State"),
       K("Name the force that keeps planets in orbit around the Sun.", 1, ["gravity / gravitational force"], "8.4", cmd="Name"),
       K("State what a galaxy is.", 1, ["a large collection of (billions of) stars"], "8.2", cmd="State"),
       K("State **two** differences between the orbit of a comet and the orbit of a planet.", 2, ["comet orbit is highly elliptical; planet nearly circular", "comet speed changes a lot; planet roughly constant", "comet orbits may be at a different angle/plane"], "8.5", cmd="State"),
       K("Name **two** types of object that orbit planets.", 2, ["moons", "artificial satellites"], "8.4", cmd="Name"),
       K("State what determines the gravitational field strength at the surface of a planet.", 1, ["its mass (and radius)"], "8.3", cmd="State", d="4-6"),
   ],
   describe=[
       K("Describe how the speed of a comet changes as it moves around its orbit.", 2, ["speeds up as it approaches the Sun", "slowest when furthest from the Sun"], "8.5", cmd="Describe"),
       K("Describe the structure of the universe.", 2, ["billions of galaxies", "each containing billions of stars"], "8.2", cmd="Describe"),
       K("Describe the differences between the orbits of a moon and a planet.", 2, ["a moon orbits a planet", "a planet orbits a star / the Sun"], "8.4 8.5", cmd="Describe"),
       K("Describe what happens to the weight of an astronaut who travels from the Earth to the Moon.", 2, ["weight decreases", "mass stays the same"], "8.3", cmd="Describe"),
   ],
   explain=[
       K("Explain why a satellite in a circular orbit is accelerating even though its speed is constant.", 2, ["its direction is always changing so velocity changes", "gravity acts towards the centre of the orbit"], "8.4", cmd="Explain", d="7-9"),
       K("Explain why a comet speeds up as it approaches the Sun.", 2, ["gravitational force from the Sun increases as it gets closer", "GPE transferred to KE"], "8.5", cmd="Explain", d="7-9"),
       K("Explain why an astronaut can jump higher on the Moon than on the Earth.", 2, ["gravitational field strength is lower on the Moon", "so less weight / smaller downward force"], "8.3", cmd="Explain"),
       K("Explain why planets further from the Sun take longer to orbit it.", 2, ["they travel a greater distance in one orbit", "and move more slowly (weaker gravity)"], "8.5 8.6", cmd="Explain", d="7-9"),
   ])

kb(STR, ["the life cycle of stars", "the Sun", "star colours", "supernovae", "the Hertzsprung-Russell diagram"],
   mcq=[
       M("Which colour of star has the highest surface temperature?", ["blue", "red", "yellow", "orange"], "8.8"),
       M("A star like the Sun will end its life as", ["a white dwarf", "a black hole", "a neutron star", "a supernova"], "8.9"),
       M("Stars form from", ["clouds of dust and gas (nebulae)", "black holes", "planets", "white dwarfs"], "8.9"),
       M("Which stage comes after main sequence for a star much more massive than the Sun?", ["red supergiant", "white dwarf", "nebula", "protostar"], "8.10"),
       M("A massive star may end as", ["a neutron star or black hole", "a white dwarf only", "a planet", "a red giant only"], "8.10"),
       M("Absolute magnitude is a measure of a star's", ["brightness at a standard distance", "distance from Earth", "surface temperature", "mass"], "8.11P"),
       M("On a Hertzsprung-Russell diagram, white dwarfs are found", ["at the bottom left", "at the top right", "at the top left", "along the middle"], "8.12P", d="4-6"),
       M("The Sun is currently a", ["main sequence star", "red giant", "white dwarf", "protostar"], "8.9"),
   ],
   recall=[
       K("State the stages in the life cycle of a star like the Sun in order.", 3, ["nebula → (protostar) → main sequence", "→ red giant", "→ white dwarf"], "8.9", cmd="State"),
       K("State what determines the colour of a star.", 1, ["its surface temperature"], "8.8", cmd="State"),
       K("State what is meant by *absolute magnitude*.", 1, ["the brightness of a star at a standard distance (10 parsecs)"], "8.11P", cmd="State"),
       K("Name the explosion that happens at the end of the life of a very massive star.", 1, ["supernova"], "8.10", cmd="Name"),
       K("Name the **two** quantities plotted on the axes of a Hertzsprung-Russell diagram.", 2, ["absolute magnitude", "surface temperature (or colour)"], "8.12P", cmd="Name"),
       K("State the order of star colours from coolest to hottest.", 2, ["red, orange, yellow", "white, blue"], "8.7 8.8", cmd="State"),
   ],
   describe=[
       K("Describe the life cycle of a star much more massive than the Sun.", 3, ["nebula → main sequence", "→ red supergiant → supernova", "→ neutron star or black hole"], "8.10", cmd="Describe"),
       K("Describe how a star forms.", 3, ["gravity pulls dust and gas in a nebula together", "it heats up as it collapses (protostar)", "when hot enough, fusion of hydrogen starts"], "8.9", cmd="Describe", d="4-6"),
       K("Describe the positions of main sequence stars, red giants and white dwarfs on an HR diagram.", 3, ["main sequence: diagonal band from top left to bottom right", "red giants: top right", "white dwarfs: bottom left"], "8.12P", cmd="Describe", d="7-9"),
       K("Describe what happens to a Sun-like star when the hydrogen in its core runs out.", 2, ["it expands to become a red giant", "outer layers drift away leaving a white dwarf"], "8.9", cmd="Describe"),
   ],
   explain=[
       K("Explain why a main sequence star is stable for a long time.", 2, ["inward gravitational force", "balanced by outward pressure from fusion energy"], "8.9", cmd="Explain", d="7-9"),
       K("Explain why white dwarfs are hot but have a low absolute magnitude.", 2, ["they are very small", "so emit little light overall despite high temperature"], "8.11P 8.12P", cmd="Explain", d="7-9"),
       K("Explain why two stars that look equally bright from Earth may have different absolute magnitudes.", 2, ["they may be at different distances", "the further one must actually be brighter"], "8.11P", cmd="Explain", d="7-9"),
       K("Explain why a red giant appears red.", 2, ["its outer layers expand and cool", "cooler surface emits more red light"], "8.8 8.9", cmd="Explain", d="4-6"),
   ])

kb(CO, ["the Big Bang", "red-shift", "the expanding universe", "cosmic microwave background", "the Doppler effect in light"],
   mcq=[
       M("Light from a distant galaxy is red-shifted. This means the galaxy is", ["moving away from us", "moving towards us", "stationary", "getting hotter"], "8.14P 8.15P"),
       M("Which observation is evidence for the Big Bang?", ["cosmic microwave background radiation", "the Sun's yellow colour", "the Moon's orbit", "comets"], "8.14P"),
       M("More distant galaxies show", ["a greater red-shift", "a smaller red-shift", "the same red-shift as nearer galaxies", "no shift"], "8.17P"),
       M("The equation linking red-shift and speed of a galaxy is", ["Δλ/λ0 = v/c", "v = fλ", "v = 2πr/T", "λ = c/f²"], "8.16P"),
       M("Red-shift causes the observed wavelength of light to", ["increase", "decrease", "stay the same", "become zero"], "8.15P"),
       M("The cosmic microwave background radiation is thought to be", ["radiation left over from the early universe", "radiation from the Sun", "microwaves from mobile phones", "light from nearby stars"], "8.14P", d="4-6"),
   ],
   recall=[
       K("State what is meant by *red-shift*.", 1, ["increase in observed wavelength of light from a source moving away"], "8.15P", cmd="State"),
       K("State **two** pieces of evidence for the Big Bang theory.", 2, ["red-shift of light from distant galaxies", "cosmic microwave background radiation"], "8.14P", cmd="State"),
       K("State the equation linking change in wavelength, reference wavelength, speed of a galaxy and speed of light.", 1, ["Δλ ÷ λ0 = v ÷ c"], "8.16P", cmd="State"),
       K("State what the Big Bang theory says about the origin of the universe.", 2, ["the universe began from a very small, hot, dense point", "and has been expanding ever since"], "8.13P", cmd="State"),
       K("State how the red-shift of a galaxy is related to its distance.", 1, ["the more distant the galaxy, the greater the red-shift"], "8.17P", cmd="State"),
       K("State what would happen to the wavelength of light from a galaxy moving towards us.", 1, ["it would decrease"], "8.15P", cmd="State", d="4-6"),
   ],
   explain=[
       K("Explain how red-shift shows that the universe is expanding.", 3, ["light from almost all galaxies is red-shifted, so they are moving away", "more distant galaxies have greater red-shift", "so they move away faster, as expected if space is expanding"], "8.17P 8.18P", cmd="Explain", d="7-9"),
       K("Explain why the cosmic microwave background supports the Big Bang theory.", 2, ["it is radiation from the hot early universe", "stretched to microwave wavelengths as the universe expanded"], "8.14P", cmd="Explain", d="7-9"),
       K("Explain how astronomers measure the red-shift of a galaxy.", 2, ["compare the absorption lines in its spectrum with those from a laboratory source", "lines are shifted towards the red end"], "8.15P 8.16P", cmd="Explain", d="7-9"),
       K("Explain why the red-shift of a galaxy tells us its speed.", 2, ["the shift in wavelength depends on the speed of the source", "Δλ/λ0 = v/c, so a bigger shift means a faster speed"], "8.15P 8.16P", cmd="Explain", d="4-6"),
   ],
   extended=[
       X("Describe the Big Bang theory and explain the evidence that supports it.",
         ["universe began about 13.8 billion years ago from a very hot, dense point", "it has expanded and cooled since", "light from distant galaxies is red-shifted",
          "red-shift means galaxies are moving away", "greater distance gives greater red-shift", "so galaxies further away move faster: universe expanding", "running the expansion backwards gives a single starting point",
          "CMB radiation detected from all directions", "CMB is the cooled radiation from the early universe", "steady state theory cannot explain the CMB"], "8.13P 8.14P 8.17P 8.18P"),
       X("Explain how the Doppler effect applies to light from galaxies and what this tells us about the universe.",
         ["a moving source changes the observed wavelength and frequency", "source moving away: wavelength increases (red-shift)", "source moving towards the observer: wavelength decreases", "absorption lines shift towards red end of spectrum",
          "Δλ/λ0 = v/c lets us calculate the speed", "almost all galaxies are red-shifted", "more distant galaxies have a larger red-shift", "universe is expanding", "evidence for the Big Bang"], "8.15P 8.16P 8.17P 8.18P"),
   ])


# ====================================================================== universe: orbital speed / weight calcs

ORB = [("the Earth", "Sun", 1.5e11, 365.25 * 24 * 3600, "1 year"), ("the Moon", "Earth", 3.84e8, 27.3 * 24 * 3600, "27.3 days"),
       ("Mars", "Sun", 2.28e11, 687 * 24 * 3600, "687 days"), ("a communications satellite", "Earth", 4.2e7, 24 * 3600, "24 hours"),
       ("the International Space Station", "Earth", 6.8e6, 92 * 60, "92 minutes"), ("Jupiter", "Sun", 7.8e11, 11.9 * 365.25 * 24 * 3600, "11.9 years"),
       ("a GPS satellite", "Earth", 2.66e7, 12 * 3600, "12 hours"), ("Io", "Jupiter", 4.22e8, 1.77 * 24 * 3600, "1.77 days")]


@T(UN, "calc", 9, "un-orbit")
def un_orbit(r):
    obj, centre, rad, Tp, Ts = pick(r, ORB)
    v = 2 * math.pi * rad / Tp
    if r.random() < 0.6:
        conv = Ts.split()
        return calc_q(intro=f"{obj[0].upper() + obj[1:]} orbits {'the ' if centre in ('Sun', 'Earth') else ''}{centre} in a circular orbit of radius {num(rad, 3)} m. The time period of the orbit is {Ts}.",
                      text="Calculate the orbital speed.", eq="v = 2πr ÷ T", working=[f"T = {num(Tp, 3)} s", f"v = 2 × π × {num(rad, 3)} ÷ {num(Tp, 3)}"],
                      ans=num(v, 3), unit="m/s", prefix="orbital speed (m/s) = ", refs=["8.6"], d="7-9", rearr=False, values={"T_s": Tp, "v": v},
                      notes=alts(v) + "; time must be converted to seconds", state=("orbital speed, orbital radius and time period", "v = (2 × π × r) ÷ T", None) if r.random() < 0.4 else None)
    return calc_q(intro=f"{obj[0].upper() + obj[1:]} moves at {num(v, 3)} m/s in a circular orbit of radius {num(rad, 3)} m.", text="Calculate the time period of the orbit in seconds.",
                  eq="v = 2πr ÷ T", working=[f"{num(v, 3)} = 2 × π × {num(rad, 3)} ÷ T", f"T = 2 × π × {num(rad, 3)} ÷ {num(v, 3)}"], ans=num(Tp, 3), unit="s",
                  prefix="time period (s) = ", refs=["8.6"], d="7-9", values={"T": Tp}, notes=alts(Tp))


@T(UN, "calc", 6, "un-weight")
def un_weight(r):
    body, g = pick(r, [("the Moon", 1.6), ("Mars", 3.7), ("Jupiter", 25), ("Venus", 8.9), ("Mercury", 3.7), ("Titan", 1.4)])
    obj, m = pick(r, [("rover", nice(r, 100, 1000, 10)), ("astronaut in a spacesuit", nice(r, 100, 180, 5)), ("lander", nice(r, 300, 2000, 50)), ("rock sample", nice(r, 0.5, 5, 0.1))])
    W = m * g
    if r.random() < 0.5:
        return calc_q(intro=f"A {obj} of mass {clean(m)} kg is on {body}, where the gravitational field strength is {g} N/kg.", text="Calculate its weight there.",
                      eq="W = m × g", working=[f"W = {clean(m)} × {g}"], ans=num(W, 3), unit="N", prefix="weight (N) = ", refs=["8.3", "1.18"], d="1-3", rearr=False,
                      values={"W": W}, notes=alts(W))
    return calc_q(intro=f"A {obj} of mass {clean(m)} kg has a weight of {num(W, 3)} N on a planet.", text="Calculate the gravitational field strength on the planet.",
                  eq="W = m × g", working=[f"{num(W, 3)} = {clean(m)} × g", f"g = {num(W, 3)} ÷ {clean(m)}"], ans=num(g, 2), unit="N/kg", prefix="g (N/kg) = ",
                  refs=["8.3", "8.1"], d="4-6", values={"g": g}, notes=alts(g))


# ====================================================================== stars: HR diagram

@T(STR, "diagram", 7, "str-hr")
def str_hr(r):
    star = pick(r, [("the Sun", "main sequence"), ("Betelgeuse", "red supergiant"), ("Sirius B", "white dwarf"), ("Rigel", "blue supergiant"), ("Proxima Centauri", "red dwarf (main sequence)"), ("Aldebaran", "red giant")])
    fig = {"type": "svg", "svg": S.hr_axes(regions=True, labels=[]), "width": 100, "caption": "Hertzsprung-Russell diagram"}
    where = {"main sequence": "on the main sequence band, near the middle", "red supergiant": "top right", "white dwarf": "bottom left", "blue supergiant": "top left",
             "red dwarf (main sequence)": "bottom right end of the main sequence", "red giant": "upper right, below the supergiants"}[star[1]]
    parts = [{"label": "a", "text": "Label the main sequence, the red giants and the white dwarfs on the diagram.", "marks": 3, "space": "none"},
             {"label": "b", "text": f"{star[0]} is a {star[1]} star. Mark its position with an X.", "marks": 1, "space": "none"},
             line_part("c", "State why the temperature axis of the diagram runs from hot on the left to cool on the right.", 1, 2) if r.random() < 0.5 else
             line_part("c", f"Describe how the position of the Sun on the diagram will change during the rest of its life.", 2, 3)]
    rows = [row("(a)", "main sequence: diagonal band;", 1), row("(a)", "red giants: top right region;", 1), row("(a)", "white dwarfs: bottom left region;", 1),
            row("(b)", f"X {where};", 1)]
    if parts[2]["marks"] == 1:
        rows.append(row("(c)", "it is a convention (historical choice based on star colour from blue to red);", 1))
    else:
        rows += [row("(c)", "moves up and to the right as it becomes a red giant;", 1), row("(c)", "then down to the bottom left as a white dwarf;", 1)]
    return dict(parts=parts, rows=rows, refs=["8.12P", "8.11P", "8.9", "8.8"], cmd="Label", d="7-9", ao=["AO1", "AO2"], figures=[fig],
                intro="The diagram shows the axes and main regions of a Hertzsprung-Russell (HR) diagram.", answer={"method": "none", "values": {}, "checked": True})


@T(STR, "diagram", 7, "str-cycle")
def str_cycle(r):
    massive = pick(r, [True, False])
    stages = ["nebula", "main sequence", "red supergiant", "supernova", pick(r, ["neutron star", "black hole"])] if massive else ["nebula", "main sequence", "red giant", "white dwarf"]
    gap = r.randrange(1, len(stages))
    shown = [s if i != gap else "........" for i, s in enumerate(stages)]
    parts = [line_part("a", f"Complete the flow chart for the life cycle of a star {'much more massive than' if massive else 'with a similar mass to'} the Sun.\n\n" + " → ".join(shown), 1, 1),
             line_part("b", "State the process that releases energy in a main sequence star.", 1, 1),
             line_part("c", "Explain what happens to a star at the end of its main sequence stage.", 2, 3)]
    rows = [row("(a)", f"{stages[gap]};", 1), row("(b)", "nuclear fusion (of hydrogen to helium);", 1),
            row("(c)", "hydrogen in the core runs out;", 1), row("(c)", f"the star expands and cools to become a red {'supergiant' if massive else 'giant'};", 1)]
    return dict(parts=parts, rows=rows, refs=["8.10" if massive else "8.9", "7.25"], cmd="Complete", d="4-6", ao=["AO1"],
                intro=f"This question is about the life cycle of {pick(r, ['stars', 'a star', 'different stars'])}.", answer={"method": "none", "values": {"missing": stages[gap]}, "checked": True})


# ====================================================================== cosmology: red-shift calc

LINES = [("hydrogen", 656.3), ("hydrogen", 486.1), ("calcium", 393.4), ("sodium", 589.0), ("helium", 587.6), ("magnesium", 518.4)]


@T(CO, "calc", 14, "co-redshift")
def co_redshift(r):
    el, l0 = pick(r, LINES)
    v = float(sf(nice(r, 1000, 60000, 500) * 1000, 2))  # printed at 2 s.f., so compute from that value
    dl = l0 * v / 3e8
    mode = r.choice(["v", "v", "dl"])
    gal = pick(r, ["A distant galaxy", "A galaxy in a cluster", "A quasar", "A spiral galaxy", "An elliptical galaxy"])
    if mode == "v":
        lob = float(sf(l0 + dl, 4))  # the printed observed wavelength; answer computed from it
        return calc_q(intro=f"{gal} shows a {el} line at {sf(lob, 4)} nm. In the laboratory this line has a wavelength of {l0} nm. The speed of light is 3.0 × 10⁸ m/s.",
                      text="Calculate the speed at which the galaxy is moving away from the Earth.", eq="Δλ ÷ λ0 = v ÷ c",
                      working=[f"Δλ = {sf(lob, 4)} - {l0} = {sf(lob - l0, 3)} nm", f"v = {sf(lob - l0, 3)} ÷ {l0} × 3.0 × 10⁸"],
                      ans=num((lob - l0) / l0 * 3e8, 2), unit="m/s", prefix="speed (m/s) = ", refs=["8.16P", "8.15P"], d="7-9", values={"v": (lob - l0) / l0 * 3e8},
                      notes=alts((lob - l0) / l0 * 3e8, ns=(2, 3)) + "; first mark for Δλ")
    return calc_q(intro=f"{gal} is moving away from the Earth at {num(v, 2)} m/s. A {el} line has a laboratory wavelength of {l0} nm. The speed of light is 3.0 × 10⁸ m/s.",
                  text="Calculate the change in wavelength of this line.", eq="Δλ ÷ λ0 = v ÷ c", working=[f"Δλ = {l0} × {num(v, 2)} ÷ 3.0 × 10⁸"],
                  ans=num(dl, 3), unit="nm", prefix="change in wavelength (nm) = ", refs=["8.16P"], d="7-9", values={"dl": dl}, notes=alts(dl))
