"""Topic 3: Waves."""
import math

import physics_svg as S
from physics_util import (K, M, X, T, kb, calc_q, line_part, work_part, row, num, sf, clean, pick, nice, alts)

PR, EM, LI, SO = ("physics.waves.properties", "physics.waves.em", "physics.waves.light", "physics.waves.sound")

kb(PR, ["waves on water", "waves on a rope", "describing waves", "the Doppler effect", "wave behaviour"],
   mcq=[
       M("In which type of wave do the particles vibrate parallel to the direction of energy transfer?", ["longitudinal", "transverse", "electromagnetic", "light"], "3.2"),
       M("What is the amplitude of a wave?", ["the maximum displacement from the rest position", "the distance between two crests", "the number of waves per second", "the time for one wave"], "3.3"),
       M("A wave has a frequency of 50 Hz. What is its time period?", ["0.020 s", "50 s", "0.50 s", "2.0 s"], "3.6", ao="AO2"),
       M("Which of these is a transverse wave?", ["a wave on a stretched string", "a sound wave in air", "a compression wave in a spring", "an ultrasound wave"], "3.2"),
       M("Waves transfer", ["energy and information but not matter", "matter but not energy", "matter and energy", "only information"], "3.4"),
       M("A wave has a wavelength of 2.0 m and a frequency of 3.0 Hz. What is its speed?", ["6.0 m/s", "1.5 m/s", "0.67 m/s", "5.0 m/s"], "3.5", ao="AO2"),
       M("A police car with its siren on moves towards an observer. Compared with the siren at rest, the observer hears", ["a higher frequency", "a lower frequency", "the same frequency", "a louder sound only"], "3.8", d="4-6"),
       M("What is a wavefront?", ["a line joining points on a wave that are in step", "the front edge of a single wave", "the highest point of a wave", "the direction a wave travels"], "3.3", d="4-6"),
   ],
   recall=[
       K("State the equation linking wave speed, frequency and wavelength.", 1, ["wave speed = frequency × wavelength | allow v = f × λ"], "3.5", cmd="State"),
       K("State what is meant by the *frequency* of a wave.", 1, ["number of waves passing a point per second | allow number of vibrations per second"], "3.3", cmd="State"),
       K("State what is meant by the *wavelength* of a wave.", 1, ["distance between two adjacent crests / compressions | allow distance between matching points on neighbouring waves"], "3.3", cmd="State"),
       K("Give **one** example of a longitudinal wave and **one** example of a transverse wave.", 2, ["longitudinal: sound / ultrasound", "transverse: light / any EM wave / water wave / wave on a string"], "3.2", cmd="Give"),
       K("State the unit of frequency.", 1, ["hertz / Hz"], "3.1", cmd="State"),
       K("Name the effect that causes the pitch of a passing car's horn to change.", 1, ["Doppler effect"], "3.8", cmd="Name"),
       K("State **two** things that can happen to a wave when it meets a boundary between two materials.", 2, ["reflection", "refraction", "absorption | allow transmission"], "3.9", cmd="State"),
   ],
   describe=[
       K("Describe the difference between a transverse wave and a longitudinal wave.", 2, ["transverse: vibrations perpendicular to direction of energy transfer", "longitudinal: vibrations parallel to direction of energy transfer"], "3.2", cmd="Describe"),
       K("Describe how you could show that a wave on water transfers energy but not water.", 2, ["place a floating cork/object on the water", "it bobs up and down but does not move along with the wave"], "3.4", cmd="Describe", ao="AO3"),
       K("Describe what happens to water waves when they move from deep water into shallow water at an angle to the boundary.", 3, ["they slow down", "wavelength decreases (frequency unchanged)", "they change direction (refract)"], "3.9", cmd="Describe", d="7-9"),
       K("Describe how a longitudinal wave can be produced on a slinky spring.", 2, ["push and pull one end of the spring", "backwards and forwards along the length of the spring"], "3.2", cmd="Describe"),
   ],
   explain=[
       K("A source of sound moves towards an observer. Explain why the observer hears a higher frequency than the source emits.", 3,
         ["the source moves towards the waves it has just emitted", "so the wavefronts are closer together / wavelength is shorter in front of the source", "same speed so more waves arrive per second (higher frequency)"], "3.8", cmd="Explain", d="7-9"),
       K("Explain why the time period of a wave decreases when its frequency increases.", 2, ["T = 1/f", "so more waves each second means each wave takes less time"], "3.6", cmd="Explain", d="4-6"),
       K("A water wave has a constant frequency. Explain why its wavelength decreases when it slows down.", 2, ["v = f × λ", "frequency is unchanged so λ is proportional to v"], "3.5", cmd="Explain", d="7-9", ao="AO2"),
       K("Explain why sound waves can be described as longitudinal.", 2, ["air particles vibrate backwards and forwards", "in the same direction as the wave travels (making compressions and rarefactions)"], "3.2 3.23", cmd="Explain"),
   ])

kb(EM, ["the electromagnetic spectrum", "uses of electromagnetic waves", "dangers of electromagnetic radiation", "communications", "medical uses of radiation"],
   mcq=[
       M("Which electromagnetic wave has the longest wavelength?", ["radio waves", "microwaves", "infrared", "gamma rays"], "3.11"),
       M("Which electromagnetic wave has the highest frequency?", ["gamma rays", "X-rays", "ultraviolet", "radio waves"], "3.11"),
       M("Which colour of visible light has the shortest wavelength?", ["violet", "red", "green", "yellow"], "3.11", d="4-6"),
       M("Which radiation is used to sterilise surgical instruments?", ["gamma rays", "infrared", "microwaves", "radio waves"], "3.12"),
       M("Which radiation is used in night-vision cameras?", ["infrared", "ultraviolet", "X-rays", "radio waves"], "3.12"),
       M("Excessive exposure to which radiation causes damage to surface cells of the skin and to the eyes?", ["ultraviolet", "radio waves", "infrared", "microwaves"], "3.13"),
       M("All electromagnetic waves", ["travel at the same speed in a vacuum", "have the same frequency", "are longitudinal", "need a medium to travel through"], "3.10"),
       M("Which part of the spectrum lies between microwaves and visible light?", ["infrared", "ultraviolet", "X-rays", "radio waves"], "3.11"),
       M("Which radiation is used to see inside the body to check for broken bones?", ["X-rays", "microwaves", "infrared", "ultraviolet"], "3.12"),
   ],
   recall=[
       K("Name the part of the electromagnetic spectrum used for satellite communication.", 1, ["microwaves"], "3.12", cmd="Name"),
       K("Give **two** properties shared by all electromagnetic waves.", 2, ["transverse", "travel at the same speed in a vacuum / free space", "can travel through a vacuum", "transfer energy", "can be reflected and refracted"], "3.10", cmd="Give"),
       K("Name **one** use of ultraviolet radiation.", 1, ["fluorescent lamps | allow security marking, sterilising water, sunbeds"], "3.12", cmd="Name"),
       K("Give **one** harmful effect of too much exposure to gamma rays.", 1, ["cancer | allow mutation of cells/DNA; allow kills cells"], "3.13", cmd="Give"),
       K("Give **one** harmful effect of microwaves on the body.", 1, ["internal heating of body tissue | allow heats water in cells"], "3.13", cmd="Give"),
       K("State **one** simple way of reducing the risk from ultraviolet radiation in sunlight.", 1, ["sunscreen / sunglasses / cover up / stay in the shade"], "3.13", cmd="State"),
       K("List the seven parts of the electromagnetic spectrum in order of decreasing wavelength.", 2, ["radio, microwave, infrared, visible | 1 mark for first four in order", "ultraviolet, X-rays, gamma | 1 mark for last three in order"], "3.11", cmd="List", d="4-6"),
   ],
   explain=[
       K("Explain why X-rays can be used to produce images of bones.", 2, ["X-rays pass through soft tissue", "but are absorbed by bone (so bones show as shadows on the detector)"], "3.12", cmd="Explain"),
       K("Explain why gamma rays can be used to keep food fresh for longer.", 2, ["gamma rays kill bacteria / microorganisms", "food does not become radioactive"], "3.12", cmd="Explain", d="4-6"),
       K("Explain why radiographers stand behind a lead screen when taking X-ray images.", 2, ["X-rays are ionising / can damage cells or cause cancer", "lead absorbs X-rays, reducing their exposure"], "3.13", cmd="Explain"),
       K("Explain why infrared radiation can be used in a heater.", 2, ["infrared is absorbed by skin/objects", "and transfers energy, increasing their temperature"], "3.12", cmd="Explain"),
       K("Explain why microwaves rather than radio waves are used to communicate with satellites.", 2, ["microwaves pass through the atmosphere", "shorter wavelength allows a narrow beam to be aimed at the satellite"], "3.12", cmd="Explain", d="7-9"),
       K("Explain why a microwave oven has a metal grille in its door.", 2, ["metal reflects/absorbs microwaves", "so microwaves cannot escape and heat the user's body tissue"], "3.13", cmd="Explain", d="4-6"),
   ],
   extended=[
       X("Discuss the uses and dangers of ultraviolet, X-rays and gamma rays. Your answer should include ways of reducing the risks.",
         ["UV is used in fluorescent lamps / security marking", "X-rays are used to look inside the body or check welds and luggage", "gamma rays sterilise food and medical equipment / treat cancer",
          "all three have high frequency and carry more energy", "UV damages surface cells and eyes, causes sunburn and skin cancer", "X-rays and gamma are ionising and can cause cancer or mutations",
          "reduce UV risk with sunscreen and sunglasses", "X-ray workers use lead aprons/screens and minimise exposure time", "gamma sources handled with tongs, stored in lead containers",
          "monitor dose with film badges"], "3.12 3.13"),
       X("Explain how different parts of the electromagnetic spectrum are used in communications and cooking, and why they are suitable.",
         ["radio waves used for broadcasting TV/radio", "radio waves can travel long distances through the atmosphere", "microwaves used for satellite and mobile phone communication",
          "microwaves pass through the atmosphere", "microwaves used in ovens", "absorbed by water molecules in food, heating it", "infrared used in grills and toasters",
          "infrared absorbed by food surface", "visible light/infrared in optical fibres carry data", "all travel at the speed of light so signals are fast"], "3.12 3.10"),
   ])

kb(LI, ["reflection of light", "refraction of light", "optical fibres", "total internal reflection", "glass blocks and prisms"],
   mcq=[
       M("A ray of light hits a plane mirror at an angle of incidence of 35°. What is the angle of reflection?", ["35°", "55°", "70°", "145°"], "3.15"),
       M("When light passes from air into glass at an angle it", ["slows down and bends towards the normal", "speeds up and bends towards the normal", "slows down and bends away from the normal", "does not change speed"], "3.14 3.18", d="4-6"),
       M("The critical angle of a glass is 42°. A ray inside the glass hits the surface at 50°. What happens?", ["total internal reflection", "it refracts out along the surface", "it refracts out away from the normal", "it is absorbed"], "3.21", d="7-9"),
       M("A material has a refractive index of 1.5. What is its critical angle?", ["42°", "34°", "48°", "56°"], "3.22", ao="AO2", d="4-6"),
       M("Angles of incidence and refraction are always measured from", ["the normal", "the surface", "the incident ray", "the horizontal"], "3.15 3.16"),
       M("Optical fibres carry signals using", ["total internal reflection", "scattering", "refraction out of the fibre", "absorption"], "3.20"),
       M("Light is", ["a transverse wave", "a longitudinal wave", "a mechanical wave", "a stream of electrons"], "3.14"),
   ],
   recall=[
       K("State the law of reflection.", 1, ["angle of incidence = angle of reflection"], "3.15", cmd="State"),
       K("State the equation linking refractive index, angle of incidence and angle of refraction.", 1, ["n = sin i ÷ sin r | allow in words"], "3.18", cmd="State"),
       K("State what is meant by the *critical angle*.", 1, ["the angle of incidence (in the denser material) at which the angle of refraction is 90°"], "3.21", cmd="State"),
       K("State **two** conditions needed for total internal reflection.", 2, ["light travels from a denser to a less dense material | allow glass to air", "angle of incidence greater than the critical angle"], "3.20 3.21", cmd="State"),
       K("Give **two** uses of total internal reflection.", 2, ["optical fibres for communication", "endoscopes", "prisms in periscopes/binoculars", "reflectors / cat's eyes"], "3.20", cmd="Give"),
       K("State the equation linking critical angle and refractive index.", 1, ["sin c = 1 ÷ n"], "3.22", cmd="State"),
   ],
   explain=[
       K("Explain why a ray of light bends when it enters a glass block at an angle.", 2, ["light slows down in glass", "one side of the wavefront slows before the other so the direction changes"], "3.14", cmd="Explain", d="7-9"),
       K("Explain why a ray of light entering a glass block along the normal does not change direction.", 2, ["angle of incidence is zero", "whole wavefront slows at the same time, so no change of direction"], "3.14", cmd="Explain", d="7-9"),
       K("Explain how light travels along a curved optical fibre.", 3, ["light hits the inside surface of the core at an angle greater than the critical angle", "total internal reflection occurs", "repeatedly, so light stays in the fibre"], "3.20", cmd="Explain", d="4-6"),
       K("Explain why a right-angled glass prism can be used instead of a mirror in a periscope.", 2, ["light meets the inside face at 45°, which is greater than the critical angle (about 42°)", "so all the light is totally internally reflected through 90°"], "3.20 3.21", cmd="Explain", d="7-9"),
       K("Explain why diamond, with a refractive index of 2.4, sparkles more than glass.", 2, ["higher n gives a smaller critical angle", "so more light is totally internally reflected inside the diamond"], "3.22 3.20", cmd="Explain", d="7-9", ao="AO2"),
   ])

kb(SO, ["sound waves", "pitch and loudness", "displaying sound waves", "hearing", "echoes"],
   mcq=[
       M("What is the range of frequencies a healthy human can hear?", ["20 Hz to 20 000 Hz", "2 Hz to 2000 Hz", "200 Hz to 200 000 Hz", "20 kHz to 200 kHz"], "3.24P"),
       M("A sound becomes louder. What happens to the trace on an oscilloscope?", ["the amplitude increases", "the wavelength decreases", "the frequency increases", "the time period increases"], "3.29P"),
       M("A note has a higher pitch. Which property of the sound wave is larger?", ["frequency", "amplitude", "wavelength", "time period"], "3.28P"),
       M("Sound waves are", ["longitudinal", "transverse", "electromagnetic", "able to travel through a vacuum"], "3.23"),
       M("Which device converts a sound wave into an electrical signal for an oscilloscope?", ["microphone", "loudspeaker", "amplifier", "signal generator"], "3.26P"),
       M("An oscilloscope trace shows one complete wave across 4 divisions. The time base is 0.5 ms/division. What is the frequency?", ["500 Hz", "2000 Hz", "125 Hz", "2 Hz"], "3.27P", ao="AO2", d="7-9"),
       M("Which of these can sound waves NOT travel through?", ["a vacuum", "water", "steel", "air"], "3.23"),
   ],
   recall=[
       K("State the frequency range of human hearing.", 1, ["20 Hz to 20 000 Hz | allow 20 Hz to 20 kHz"], "3.24P", cmd="State"),
       K("State how the pitch of a sound depends on the vibration of its source.", 1, ["higher frequency of vibration gives higher pitch"], "3.28P", cmd="State"),
       K("State how the loudness of a sound depends on the vibration of its source.", 1, ["larger amplitude of vibration gives a louder sound"], "3.29P", cmd="State"),
       K("Name **two** pieces of equipment needed to display a sound wave as a trace.", 2, ["microphone", "oscilloscope | allow cathode ray oscilloscope / data logger with display"], "3.26P", cmd="Name"),
       K("State what is meant by an echo.", 1, ["a reflected sound wave"], "3.23", cmd="State"),
   ],
   explain=[
       K("Explain how a microphone and an oscilloscope can be used to show that two tuning forks have different frequencies.", 3,
         ["sound from each fork is detected by the microphone and displayed on the oscilloscope", "count the number of waves across the screen (with the same time base)", "the higher frequency fork shows more waves / shorter time period"], "3.26P 3.27P", cmd="Explain", d="4-6", ao="AO3"),
       K("Explain why sound cannot travel through space.", 2, ["sound needs particles/a medium to vibrate", "space is a vacuum with no particles"], "3.23", cmd="Explain"),
       K("Explain why a dog can hear a whistle that a person cannot.", 2, ["the whistle frequency is above 20 000 Hz", "a dog's hearing range extends to higher frequencies"], "3.24P", cmd="Explain"),
       K("A guitar string is plucked harder. Explain what happens to the sound produced.", 2, ["amplitude of vibration increases", "so the sound is louder (pitch unchanged)"], "3.29P", cmd="Explain"),
       K("Explain why the sound from a tightened drum skin has a higher pitch.", 2, ["the skin vibrates with a higher frequency", "higher frequency means higher pitch"], "3.28P", cmd="Explain", d="4-6"),
   ])


# ====================================================================== properties: calculations / diagrams

WAVE_CTX = [("water wave in a ripple tank", (2, 20, 1), "Hz", (0.5, 6, 0.5), "cm"), ("wave on a rope", (1, 6, 0.5), "Hz", (0.4, 3.0, 0.2), "m"),
            ("sound wave in air", (0.2, 8, 0.1), "kHz", None, None), ("seismic wave", (0.5, 4, 0.5), "Hz", (1000, 6000, 500), "m"),
            ("wave on a slinky spring", (1, 5, 0.5), "Hz", (0.2, 1.2, 0.1), "m"), ("ocean wave", (0.05, 0.25, 0.05), "Hz", (20, 120, 10), "m")]


@T(PR, "calc", 7, "pr-vfl")
def pr_vfl(r):
    name, fr, fu, lr, lu = pick(r, WAVE_CTX)
    f = nice(r, *fr)
    if name.startswith("sound"):
        v = 340
        lam = v / (f * 1000)
        return calc_q(intro=f"A {name} has a frequency of {clean(f)} kHz. The speed of sound in air is 340 m/s.", text="Calculate the wavelength of the sound.",
                      eq="v = f × λ", working=[f"f = {clean(f * 1000)} Hz", f"340 = {clean(f * 1000)} × λ", f"λ = 340 ÷ {clean(f * 1000)}"],
                      ans=num(lam, 2), unit="m", prefix="wavelength (m) = ", refs=["3.5", "3.7"], d="7-9", values={"f": f * 1000, "lambda": lam},
                      notes=alts(lam) + "; kHz must be converted to Hz")
    lam = nice(r, *lr)
    lm = lam / 100 if lu == "cm" else lam
    v = f * lm
    if r.random() < 0.5:
        return calc_q(intro=f"A {name} has a frequency of {clean(f)} Hz and a wavelength of {clean(lam)} {lu}.", text="Calculate the speed of the wave in m/s.",
                      eq="v = f × λ", working=([f"λ = {clean(lm)} m"] if lu == "cm" else []) + [f"v = {clean(f)} × {clean(lm)}"], ans=num(v, 3), unit="m/s",
                      prefix="speed (m/s) = ", refs=["3.5"], d="4-6" if lu == "cm" else "1-3", rearr=False, values={"f": f, "lambda": lm, "v": v}, notes=alts(v),
                      state=("wave speed, frequency and wavelength", "wave speed = frequency × wavelength", None))
    return calc_q(intro=f"A {name} travels at {num(v, 3)} m/s with a wavelength of {clean(lm)} m.", text="Calculate the frequency of the wave.", eq="v = f × λ",
                  working=[f"{num(v, 3)} = f × {clean(lm)}", f"f = {num(v, 3)} ÷ {clean(lm)}"], ans=num(f, 3), unit="Hz", prefix="frequency (Hz) = ",
                  refs=["3.5"], d="4-6", values={"f": f, "lambda": lm, "v": v}, notes=alts(f))


@T(PR, "calc", 6, "pr-period")
def pr_period(r):
    mode = r.choice(["f", "T", "both"])
    if mode == "f":
        Tms = nice(r, 0.5, 40, 0.5)
        f = 1000 / Tms
        return calc_q(intro=f"A wave has a time period of {clean(Tms)} ms.", text="Calculate the frequency of the wave.", eq="f = 1 ÷ T",
                      working=[f"T = {clean(Tms / 1000)} s", f"f = 1 ÷ {clean(Tms / 1000)}"], ans=num(f, 3), unit="Hz", prefix="frequency (Hz) = ",
                      refs=["3.6", "3.1"], d="4-6", rearr=False, values={"T_s": Tms / 1000, "f": f}, notes=alts(f) + "; ms must be converted to s")
    if mode == "T":
        f = nice(r, 2, 500, 2)
        Tp = 1 / f
        return calc_q(intro=f"A vibrating source produces waves with a frequency of {clean(f)} Hz.", text="Calculate the time period of the waves.", eq="f = 1 ÷ T",
                      working=[f"{clean(f)} = 1 ÷ T", f"T = 1 ÷ {clean(f)}"], ans=num(Tp, 2), unit="s", prefix="time period (s) = ", refs=["3.6"],
                      d="4-6", values={"f": f, "T": Tp}, notes=alts(Tp))
    n = r.randint(10, 60)
    t = nice(r, 2, 30, 0.5)
    f = n / t
    lam = nice(r, 0.2, 2.0, 0.1)
    v = f * lam
    return calc_q(intro=f"A student counts {n} waves passing a post in {clean(t)} s. The wavelength is {clean(lam)} m.",
                  text="Calculate the speed of the waves.", eq="v = f × λ", working=[f"f = {n} ÷ {clean(t)} = {num(f, 3)} Hz", f"v = {num(f, 3)} × {clean(lam)}"],
                  ans=num(v, 3), unit="m/s", prefix="speed (m/s) = ", refs=["3.5", "3.3"], d="7-9", values={"f": f, "v": v}, notes=alts(v))


@T(PR, "diagram", 7, "pr-label")
def pr_label(r):
    cyc = pick(r, [1.5, 2, 2.5, 3])
    scale = pick(r, [2, 5, 10, 20, 50])
    fig = {"type": "svg", "svg": S.transverse_wave(cycles=cyc, amp=35, wl=100), "width": 110, "caption": f"Scale: the dashed line is the rest position. One wavelength drawn = {scale} cm"}
    f = nice(r, 1, 12, 0.5)
    v = f * scale / 100
    parts = [{"label": "a", "text": "On the diagram, label the amplitude with the letter A and one wavelength with the letter W.", "marks": 2, "space": "none"},
             line_part("b", f"State the number of complete waves shown in the diagram.", 1, 1),
             work_part("c", f"The frequency of the wave is {clean(f)} Hz. Calculate the speed of the wave.", 2, "speed (m/s) = ")]
    rows = [row("(a)", "A: vertical distance from rest line to a crest or trough;", 1, "reject crest to trough"),
            row("(a)", "W: horizontal distance between two adjacent crests/troughs/equivalent points;", 1),
            row("(b)", f"{clean(cyc)};", 1),
            row("(c)", f"v = {clean(f)} × {clean(scale / 100)};", 1, "allow in cm/s"), row("(c)", f"{num(v, 3)} (m/s);", 1, f"allow {num(v * 100, 3)} cm/s")]
    return dict(parts=parts, rows=rows, refs=["3.3", "3.5"], cmd="Label", d="4-6", ao=["AO1", "AO2"], figures=[fig],
                intro="The diagram shows a transverse wave on a rope at one instant.", answer={"method": "python", "values": {"v": v, "cycles": cyc}, "checked": True})


def doppler_svg(direction=1):
    body = ""
    for k in range(1, 6):
        r_ = 22 * k
        cx = 200 - direction * 9 * k
        body += S.circle(cx, 110, r_, extra=' stroke-width="1"')
    body += S.circle(200, 110, 4, True) + S.arrow(200, 110, 200 + direction * 35, 110, 6, 1.5)
    body += S.text(40, 200, "P", bold=True) + S.text(360, 200, "Q", bold=True)
    return S.svg(400, 220, body)


@T(PR, "diagram", 6, "pr-doppler")
def pr_doppler(r):
    d = pick(r, [1, -1])
    src = pick(r, ["ambulance siren", "train horn", "racing car engine", "drone buzzer", "insect's buzz", "police car siren"])
    front = "Q" if d > 0 else "P"
    back = "P" if d > 0 else "Q"
    fig = {"type": "svg", "svg": doppler_svg(d), "width": 100, "caption": "Wavefronts from a moving source (arrow shows motion)"}
    parts = [line_part("a", f"State which observer, P or Q, hears the higher frequency. Give a reason using the diagram.", 2, 2),
             {"label": "b", "text": f"On the diagram, mark with an X a point where the wavelength is longest.", "marks": 1, "space": "none"},
             line_part("c", "Name this effect.", 1, 1)]
    rows = [row("(a)", f"{front};", 1), row("(a)", "wavefronts are closer together (shorter wavelength) in front of the moving source;", 1),
            row("(b)", f"X marked on the {back} side, where wavefronts are furthest apart;", 1), row("(c)", "Doppler effect;", 1)]
    return dict(parts=parts, rows=rows, refs=["3.8", "3.3"], cmd="State", d="7-9", ao=["AO2"], figures=[fig],
                intro=f"The diagram shows wavefronts of sound from a moving {src}. Observers P and Q stand on either side.",
                answer={"method": "geometry", "values": {"higher": front}, "checked": True})


# ====================================================================== EM calculations

EMW = [("radio station", "radio waves", (88, 108, 0.1), "MHz", 1e6), ("microwave link", "microwaves", (2, 30, 0.5), "GHz", 1e9),
       ("Wi-Fi router", "microwaves", (2.4, 5.0, 0.1), "GHz", 1e9), ("long-wave transmitter", "radio waves", (150, 280, 5), "kHz", 1e3),
       ("infrared remote control", "infrared", (300, 380, 10), "THz", 1e12)]


@T(EM, "calc", 7, "em-c")
def em_c(r):
    src, kind, fr, fu, mult = pick(r, EMW)
    f = nice(r, *fr)
    lam = 3.0e8 / (f * mult)
    return calc_q(intro=f"A {src} emits {kind} with a frequency of {clean(f)} {fu}. The speed of electromagnetic waves is 3.0 × 10⁸ m/s.",
                  text="Calculate the wavelength of the waves.", eq="v = f × λ",
                  working=[f"f = {num(f * mult, 3)} Hz", f"3.0 × 10⁸ = {num(f * mult, 3)} × λ", f"λ = 3.0 × 10⁸ ÷ {num(f * mult, 3)}"],
                  ans=num(lam, 2), unit="m", prefix="wavelength (m) = ", refs=["3.5", "3.7", "3.10"], d="7-9", values={"f": f * mult, "lambda": lam},
                  notes=alts(lam) + "; prefix must be converted")


@T(EM, "calc", 6, "em-time")
def em_time(r):
    ctx = pick(r, [("a communications satellite", 3.6e7), ("the Moon", 3.84e8), ("a GPS satellite", 2.0e7), ("a radar target aircraft", None), ("Mars at closest approach", 5.6e10)])
    name, d = ctx
    if d is None:
        d = nice(r, 20, 150, 5) * 1000
    echo = r.random() < 0.5
    tot = 2 * d if echo else d
    t = tot / 3.0e8
    what = f"for a signal to travel to {name} and back" if echo else f"for a signal to travel from {name} to the Earth"
    return calc_q(intro=f"The distance to {name} is {num(d, 3)} m. Electromagnetic waves travel at 3.0 × 10⁸ m/s.", text=f"Calculate the time taken {what}.",
                  eq="speed = distance ÷ time", working=([f"distance = 2 × {num(d, 3)} m"] if echo else []) + [f"t = {num(tot, 3)} ÷ 3.0 × 10⁸"],
                  ans=num(t, 2), unit="s", prefix="time (s) = ", refs=["3.10", "3.7"], d="7-9" if echo else "4-6", values={"d": tot, "t": t}, notes=alts(t))


# ====================================================================== light

@T(LI, "calc", 7, "li-snell")
def li_snell(r):
    mat, n = pick(r, [("glass", 1.50), ("perspex", 1.49), ("water", 1.33), ("diamond", 2.42), ("crown glass", 1.52), ("a plastic", 1.60)])
    i = r.randint(20, 70)
    rr = math.degrees(math.asin(math.sin(math.radians(i)) / n))
    mode = r.choice(["n", "r"])
    if mode == "n":
        rm = round(rr)
        nn = math.sin(math.radians(i)) / math.sin(math.radians(rm))
        return calc_q(intro=f"A ray of light passes from air into {mat}. The angle of incidence is {i}° and the angle of refraction is {rm}°.",
                      text=f"Calculate the refractive index of {mat}.", eq="n = sin i ÷ sin r", working=[f"n = sin {i} ÷ sin {rm}"], ans=num(nn, 3), unit="",
                      prefix="refractive index = ", refs=["3.18"], d="4-6", rearr=False, values={"i": i, "r": rm, "n": nn}, notes=alts(nn) + "; no unit",
                      state=("refractive index, angle of incidence and angle of refraction", "n = sin i ÷ sin r", None))
    return calc_q(intro=f"Light enters {mat} (refractive index {n}) from air with an angle of incidence of {i}°.", text="Calculate the angle of refraction.",
                  eq="n = sin i ÷ sin r", working=[f"{n} = sin {i} ÷ sin r", f"sin r = sin {i} ÷ {n} = {sf(math.sin(math.radians(i)) / n, 3)}", f"r = sin⁻¹({sf(math.sin(math.radians(i)) / n, 3)})"],
                  ans=num(rr, 2), unit="°", prefix="angle of refraction (°) = ", refs=["3.18"], d="7-9", values={"i": i, "n": n, "r": rr}, notes=alts(rr, ns=(2, 3)))


@T(LI, "calc", 6, "li-critical")
def li_crit(r):
    mat, n = pick(r, [("glass", 1.50), ("water", 1.33), ("diamond", 2.42), ("optical fibre core", 1.48), ("perspex", 1.49), ("flint glass", 1.62)])
    c = math.degrees(math.asin(1 / n))
    if r.random() < 0.5:
        q = calc_q(intro=f"The refractive index of {mat} is {n}.", text=f"Calculate the critical angle for {mat}.", eq="sin c = 1 ÷ n",
                   working=[f"sin c = 1 ÷ {n}", f"c = sin⁻¹({sf(1 / n, 3)})"], ans=num(c, 3), unit="°", prefix="critical angle (°) = ", refs=["3.22"],
                   d="4-6", values={"n": n, "c": c}, notes=alts(c, ns=(2, 3)))
        ai = round(c) + r.choice([-8, -5, 6, 10])
        q["parts"][0]["label"] = "a"
        for rw in q["rows"]:
            rw["part"] = "(a)"
        q["parts"].append(line_part("b", f"A ray inside the {mat} meets the surface with an angle of incidence of {ai}°. State what happens to the ray. Give a reason.", 2, 2))
        tir = ai > c
        q["rows"] += [row("(b)", "total internal reflection;" if tir else "it refracts out of the material (some partial reflection);", 1),
                      row("(b)", f"because {ai}° is {'greater' if tir else 'less'} than the critical angle;", 1, "allow ecf from (a)")]
        return q
    cm = round(c)
    nn = 1 / math.sin(math.radians(cm))
    return calc_q(intro=f"A student finds that the critical angle for a transparent block is {cm}°.", text="Calculate the refractive index of the block.",
                  eq="sin c = 1 ÷ n", working=[f"sin {cm} = 1 ÷ n", f"n = 1 ÷ sin {cm}"], ans=num(nn, 3), unit="", prefix="refractive index = ",
                  refs=["3.22"], d="4-6", values={"c": cm, "n": nn}, notes=alts(nn))


@T(LI, "practical", 7, "li-prac")
def li_prac(r):
    n = pick(r, [1.48, 1.50, 1.52, 1.55])
    angs = r.sample([20, 30, 40, 50, 60, 70], 4)
    angs.sort()
    data = [(i, round(math.degrees(math.asin(math.sin(math.radians(i)) / n)) + r.choice([-1, 0, 0, 1]))) for i in angs]
    tab = {"type": "table", "headers": ["angle of incidence i in °", "angle of refraction r in °"], "rows": [[str(a), str(b)] for a, b in data], "caption": "Results"}
    i0, r0 = data[1]
    nv = math.sin(math.radians(i0)) / math.sin(math.radians(r0))
    parts = [line_part("a", "Describe how the student can use a ray box, protractor and pencil to measure the angle of refraction for one angle of incidence.", 4, 6),
             work_part("b", f"Use the result for i = {i0}° to calculate the refractive index of the glass.", 2, "refractive index = "),
             line_part("c", "Suggest **one** way the student could improve the accuracy of her angle measurements.", 1, 2)]
    rows = [row("(a)", "any four from:\nMP1. draw round the block on paper;\nMP2. draw a normal at the point where the ray enters;\nMP3. shine the ray at a measured angle of incidence (using protractor);\n"
                       "MP4. mark the emerging ray with two or more crosses/dots;\nMP5. remove block and join the entry and exit points;\nMP6. measure the angle between this line and the normal with a protractor;", 4, None, "AO3"),
            row("(b)", f"substitution: n = sin {i0} ÷ sin {r0};", 1, None, "AO2"), row("(b)", f"{num(nv, 3)};", 1, alts(nv), "AO2"),
            row("(c)", "use a narrower ray / darken the room / mark points far apart / use a sharp pencil / repeat and take means / plot sin i against sin r;", 1, None, "AO3")]
    return dict(parts=parts, rows=rows, refs=["3.17", "3.19", "3.18"], cmd="Describe", d="4-6", ao=["AO2", "AO3"], figures=[tab],
                intro=f"A student investigates the refraction of light in a rectangular glass block. Her results are shown in the table.",
                answer={"method": "python", "values": {"n": nv, "data": data}, "checked": True})


@T(LI, "practical", 6, "li-prac-crit")
def li_prac_crit(r):
    blk = pick(r, ["semicircular glass block", "semicircular perspex block", "semicircular acrylic block"])
    c = pick(r, [40, 41, 42, 43, 44])
    parts = [line_part("a", f"Describe how a {blk} can be used to find the critical angle of the material.", 4, 6),
             work_part("b", f"The student finds the critical angle to be {c}°. Calculate the refractive index of the material.", 2, "refractive index = "),
             line_part("c", "Explain why the ray is aimed at the centre of the flat face.", 1, 2)]
    n = 1 / math.sin(math.radians(c))
    rows = [row("(a)", "any four from:\nMP1. aim a ray through the curved side towards the centre of the flat face;\nMP2. draw the normal at the centre;\nMP3. increase the angle of incidence gradually;\n"
                       "MP4. until the refracted ray just travels along the flat surface (angle of refraction 90°);\nMP5. mark the incident ray and measure the angle to the normal with a protractor;\nMP6. repeat and average;", 4, None, "AO3"),
            row("(b)", f"n = 1 ÷ sin {c};", 1, None, "AO2"), row("(b)", f"{num(n, 3)};", 1, alts(n), "AO2"),
            row("(c)", "so the ray meets the curved surface along a radius (normal) and does not refract on entry;", 1, None, "AO3")]
    return dict(parts=parts, rows=rows, refs=["3.17", "3.21", "3.22"], cmd="Describe", d="7-9", ao=["AO2", "AO3"],
                intro=f"A student is given a {blk}, a ray box and a protractor.", answer={"method": "python", "values": {"n": n}, "checked": True})


@T(LI, "data", 13, "li-data")
def li_data(r):
    n = pick(r, [1.45, 1.48, 1.50, 1.52, 1.56, 1.60])
    angs = [10, 20, 30, 40, 50, 60, 70]
    rs = [round(math.degrees(math.asin(math.sin(math.radians(i)) / n)) + r.choice([-1, 0, 0, 1])) for i in angs]
    tab = {"type": "table", "headers": ["i in °"] + [str(a) for a in angs], "rows": [["r in °"] + [str(x) for x in rs], ["sin i"] + [f"{math.sin(math.radians(a)):.2f}" for a in angs],
                                                                                 ["sin r"] + [f"{math.sin(math.radians(x)):.2f}" if k < 5 else "" for k, x in enumerate(rs)]],
           "caption": "Results"}
    parts = [line_part("a", "Complete the table by calculating sin r for the last two results.", 2, 1),
             {"label": "b", "text": "Plot a graph of sin i (y-axis) against sin r (x-axis) and draw a line of best fit.", "marks": 4, "space": "graph"},
             work_part("c", "Use the gradient of your graph to determine the refractive index of the material.", 2, "refractive index = ")]
    rows = [row("(a)", f"{math.sin(math.radians(rs[5])):.2f};", 1, "allow 2 or 3 d.p.", "AO2"), row("(a)", f"{math.sin(math.radians(rs[6])):.2f};", 1, None, "AO2"),
            row("(b)", "suitable linear scales (points occupy more than half the grid);", 1, None, "AO3"), row("(b)", "axes labelled (sin i, sin r);", 1, "no units needed", "AO3"),
            row("(b)", "points plotted to nearest half square;", 1, None, "AO3"), row("(b)", "straight line of best fit through the origin;", 1, None, "AO3"),
            row("(c)", "gradient found using a large triangle;", 1, None, "AO3"), row("(c)", f"{sf(n - 0.05, 3)} to {sf(n + 0.05, 3)};", 1, f"expected {n}", "AO2")]
    return dict(parts=parts, rows=rows, refs=["3.18", "3.19"], cmd="Plot", d="7-9", ao=["AO2", "AO3"], figures=[tab],
                intro=f"A student measures angles of refraction for light entering a {pick(r, ['glass', 'perspex', 'plastic', 'resin'])} block.",
                answer={"method": "python", "values": {"n": n, "r": rs}, "checked": True})


@T(LI, "diagram", 5, "li-block")
def li_block(r):
    i = pick(r, [30, 35, 40, 45, 50, 55, 60])
    n = pick(r, [1.5, 1.45, 1.6])
    s, rr = S.block_refraction(i, n, show_refracted=False)
    fig = {"type": "svg", "svg": s, "width": 100, "caption": "Ray of light incident on a glass block", "note": "Diagram NOT accurately drawn"}
    parts = [{"label": "a", "text": "Complete the diagram to show the path of the ray through the block and out into the air again.", "marks": 3, "space": "none"},
             work_part("b", f"The angle of incidence is {i}° and the refractive index is {n}. Calculate the angle of refraction inside the block.", 3, "angle (°) = ")]
    rows = [row("(a)", "ray bends towards the normal inside the block;", 1), row("(a)", "ray reaches the bottom face and bends away from the normal on leaving;", 1),
            row("(a)", "emerging ray parallel to the incident ray (laterally displaced);", 1, "judge by eye"),
            row("(b)", f"substitution: {n} = sin {i} ÷ sin r;", 1), row("(b)", "rearrangement: sin r = sin i ÷ n;", 1), row("(b)", f"{num(rr, 2)} (°);", 1, alts(rr, ns=(2, 3)))]
    return dict(parts=parts, rows=rows, refs=["3.16", "3.18"], cmd="Complete", d="4-6", ao=["AO1", "AO2"], figures=[fig],
                answer={"method": "python", "values": {"r": rr}, "checked": True})


@T(LI, "diagram", 4, "li-mirror")
def li_mirror(r):
    i = pick(r, [25, 30, 35, 40, 50, 55, 60, 65])
    fig = {"type": "svg", "svg": S.plane_mirror(i), "width": 90, "caption": "Ray of light hitting a plane mirror"}
    parts = [{"label": "a", "text": "Draw the reflected ray on the diagram.", "marks": 2, "space": "none"},
             line_part("b", f"The angle between the incident ray and the mirror surface is {90 - i}°. State the angle of reflection.", 1, 1, prefix="angle of reflection = ")]
    rows = [row("(a)", "reflected ray drawn from the point where the ray hits the mirror;", 1), row("(a)", "angle of reflection equal to angle of incidence (±2°) with arrow;", 1),
            row("(b)", f"{i}°;", 1, f"reject {90 - i}°")]
    return dict(parts=parts, rows=rows, refs=["3.15", "3.16"], cmd="Draw", d="4-6", ao=["AO1", "AO2"], figures=[fig],
                answer={"method": "geometry", "values": {"r": i}, "checked": True})


@T(LI, "diagram", 4, "li-semi")
def li_semi(r):
    n = pick(r, [1.5, 1.45, 1.6, 1.52])
    th = pick(r, [25, 30, 35, 48, 50, 55, 60])
    s, c = S.semicircle_block(th, n)
    tir = th > c
    fig = {"type": "svg", "svg": s, "width": 100, "caption": "Ray entering a semicircular block, aimed at the centre of the flat face"}
    parts = [{"label": "a", "text": f"The critical angle of the block is {num(c, 2)}°. The angle of incidence at the flat face is {th}°. Complete the diagram to show what happens to the ray at the flat face.", "marks": 2, "space": "none"},
             line_part("b", "Explain why the ray does not change direction when it enters the curved surface.", 1, 2)]
    if tir:
        rows = [row("(a)", "ray totally internally reflected at the flat face;", 1), row("(a)", f"angle of reflection equal to angle of incidence ({th}°);", 1)]
    else:
        rows = [row("(a)", "ray refracts out into the air;", 1), row("(a)", "bending away from the normal;", 1, "allow a weak reflected ray also shown")]
    rows.append(row("(b)", "it travels along a radius / along the normal, so the angle of incidence is zero;", 1))
    return dict(parts=parts, rows=rows, refs=["3.16", "3.20", "3.21"], cmd="Complete", d="7-9", ao=["AO2"], figures=[fig],
                answer={"method": "python", "values": {"c": c, "tir": tir}, "checked": True})


# ====================================================================== sound

@T(SO, "calc", 7, "so-echo")
def so_echo(r):
    ctx = pick(r, [("a cliff", 340), ("a school wall", 340), ("the sea bed", 1500), ("a shoal of fish", 1500), ("a canyon wall", 330)])
    place, v = ctx
    d = nice(r, 50, 900, 10) if v < 1000 else nice(r, 60, 3000, 20)
    t = 2 * d / v
    tt = float(sf(t, 2))
    vv = 2 * d / tt
    if r.random() < 0.5:
        return calc_q(intro=f"A student stands {clean(d)} m from {place}. A short pulse of sound reflects from it and the echo is heard {sf(t, 2)} s later.",
                      text="Calculate the speed of sound from these measurements.", eq="speed = distance ÷ time",
                      working=[f"distance = 2 × {clean(d)} = {clean(2 * d)} m", f"speed = {clean(2 * d)} ÷ {sf(t, 2)}"], ans=num(vv, 3), unit="m/s",
                      prefix="speed (m/s) = ", refs=["3.25P", "1.4"], d="7-9", rearr=False, values={"d": 2 * d, "t": tt, "v": vv},
                      notes=alts(vv) + "; the distance must be doubled for the evaluation mark")
    return calc_q(intro=f"A pulse of sound is sent towards {place}. The echo returns after {sf(t, 2)} s. Sound travels at {v} m/s in this medium.",
                  text=f"Calculate the distance to {place}.", eq="speed = distance ÷ time",
                  working=[f"total distance = {v} × {sf(t, 2)} = {clean(v * tt)} m", f"distance = {clean(v * tt)} ÷ 2"], ans=num(v * tt / 2, 3), unit="m",
                  prefix="distance (m) = ", refs=["3.23", "1.4"], d="7-9", values={"t": tt, "d": v * tt / 2}, notes=alts(v * tt / 2))


@T(SO, "calc", 6, "so-osc")
def so_osc(r):
    cyc = pick(r, [1, 1.5, 2, 2.5, 3, 4, 5])
    tb = pick(r, [0.1, 0.2, 0.5, 1, 2, 5])
    divs = 10
    Tp = divs / cyc * tb
    f = 1000 / Tp
    fig = {"type": "svg", "svg": S.oscilloscope(cyc, pick(r, [1.5, 2, 2.5, 3])), "width": 100, "caption": f"Oscilloscope trace; time base {clean(tb)} ms/division"}
    return calc_q(intro=f"A microphone is connected to an oscilloscope. The trace shows the sound from a tuning fork. The time base is set to {clean(tb)} ms per division.",
                  text="Determine the frequency of the sound.", eq="f = 1 ÷ T",
                  working=[f"one wave covers {sf(divs / cyc, 3)} divisions", f"T = {sf(divs / cyc, 3)} × {clean(tb)} ms = {sf(Tp / 1000, 3)} s", f"f = 1 ÷ {sf(Tp / 1000, 3)}"],
                  ans=num(f, 3), unit="Hz", prefix="frequency (Hz) = ", refs=["3.27P", "3.6"], d="7-9", values={"T_s": Tp / 1000, "f": f},
                  notes=alts(f) + "; first mark (substitution) for correct time period read from the trace", figs=[fig], cmd="Determine")


@T(SO, "practical", 7, "so-prac-echo")
def so_prac(r):
    method = pick(r, ["echo", "two microphones"])
    if method == "echo":
        d = nice(r, 50, 120, 5)
        n = pick(r, [10, 20, 30])
        t = 2 * d * n / 340 * r.uniform(0.97, 1.03)
        v = 2 * d * n / t
        parts = [line_part("a", f"Describe how the students can use clapping and echoes from a wall {clean(d)} m away to measure the speed of sound.", 4, 6),
                 work_part("b", f"They time {n} claps (each clap in time with the echo of the previous one) and record a time of {sf(t, 3)} s. Calculate the speed of sound.", 2, "speed (m/s) = "),
                 line_part("c", "Explain why timing many claps gives a more accurate result than timing a single echo.", 2, 3)]
        rows = [row("(a)", "any four from:\nMP1. measure distance to wall with a trundle wheel/tape;\nMP2. clap so that each clap coincides with the echo;\nMP3. second student times a number of claps with a stopwatch;\n"
                           "MP4. sound travels 2 × distance for each clap;\nMP5. speed = total distance ÷ time;\nMP6. repeat and find a mean;\nMP7. stand at least 50 m away / large open space;", 4, None, "AO3"),
                row("(b)", f"speed = (2 × {clean(d)} × {n}) ÷ {sf(t, 3)};", 1, None, "AO2"), row("(b)", f"{num(v, 3)} (m/s);", 1, alts(v), "AO2"),
                row("(c)", "reaction time is a smaller fraction of the total time measured;", 1, None, "AO3"), row("(c)", "so percentage error (uncertainty) is smaller;", 1, None, "AO3")]
        vals = {"v": v}
    else:
        d = nice(r, 0.5, 2.0, 0.1)
        tms = d / 340 * 1000 * r.uniform(0.97, 1.03)
        v = d / (tms / 1000)
        parts = [line_part("a", "Describe how two microphones connected to a fast timer can be used to measure the speed of sound in air.", 4, 6),
                 work_part("b", f"The microphones are {clean(d)} m apart. The timer records {sf(tms, 3)} ms. Calculate the speed of sound.", 3, "speed (m/s) = "),
                 line_part("c", "Suggest why this method is more accurate than using a stopwatch.", 1, 2)]
        rows = [row("(a)", "any four from:\nMP1. place two microphones a measured distance apart in a line with the sound source;\nMP2. make a sharp sound (clap/hammer) beyond the first microphone;\nMP3. timer starts when the first microphone detects the sound;\n"
                           "MP4. stops when the second microphone detects it;\nMP5. speed = distance ÷ time;\nMP6. repeat for different separations and average;", 4, None, "AO3"),
                row("(b)", f"conversion: {sf(tms, 3)} ms = {sf(tms / 1000, 3)} s;", 1, None, "AO2"),
                row("(b)", f"substitution: {clean(d)} ÷ {sf(tms / 1000, 3)};", 1, None, "AO2"), row("(b)", f"{num(v, 3)} (m/s);", 1, alts(v), "AO2"),
                row("(c)", "no human reaction time involved;", 1, None, "AO3")]
        vals = {"v": v}
    return dict(parts=parts, rows=rows, refs=["3.25P"], cmd="Describe", d="4-6", ao=["AO2", "AO3"],
                intro="Some students want to measure the speed of sound in air.", answer={"method": "python", "values": vals, "checked": True})


@T(SO, "practical", 6, "so-prac-osc")
def so_prac_osc(r):
    src = pick(r, ["tuning fork", "signal generator and loudspeaker", "guitar string", "recorder"])
    parts = [line_part("a", f"Describe how a microphone and oscilloscope can be used to find the frequency of the sound from a {src}.", 3, 5),
             line_part("b", "State how the trace would change if the sound was made louder but kept at the same pitch.", 1, 2),
             line_part("c", "State how the trace would change if the frequency was doubled.", 1, 2)]
    rows = [row("(a)", "any three from:\nMP1. connect the microphone to the oscilloscope and hold it near the source;\nMP2. adjust the time base so one or more complete waves are visible;\nMP3. measure the number of divisions for one (or several) complete waves;\n"
                       "MP4. multiply by the time base setting to find the time period;\nMP5. frequency = 1 ÷ time period;", 3, None, "AO3"),
            row("(b)", "taller waves / larger amplitude, same spacing;", 1, None, "AO1"),
            row("(c)", "twice as many waves on screen / waves half as wide;", 1, None, "AO1")]
    return dict(parts=parts, rows=rows, refs=["3.26P", "3.27P", "3.28P", "3.29P"], cmd="Describe", d="4-6", ao=["AO1", "AO3"],
                intro=f"A student investigates the sound produced by a {src}. {pick(r, ['The microphone is placed 20 cm from the source.', 'The room is kept quiet during the test.', 'The oscilloscope screen is ten divisions wide.', 'A second student records the readings.'])}", answer={"method": "none", "values": {}, "checked": True})


@T(SO, "data", 13, "so-data")
def so_data(r):
    c1, c2 = r.sample([1, 1.5, 2, 2.5, 3, 4], 2)
    a1, a2 = r.sample([1, 1.5, 2, 2.5, 3], 2)
    tb = pick(r, [0.2, 0.5, 1, 2])
    figs = [{"type": "svg", "svg": S.oscilloscope(c1, a1), "width": 80, "caption": "Trace X"}, {"type": "svg", "svg": S.oscilloscope(c2, a2), "width": 80, "caption": "Trace Y"}]
    T1 = 10 / c1 * tb / 1000
    f1 = 1 / T1
    f2 = c2 / 10 / (tb / 1000)
    hi = "X" if c1 > c2 else "Y"
    loud = "X" if a1 > a2 else "Y"
    parts = [line_part("a", "State which trace shows the sound with the higher pitch. Give a reason.", 2, 2),
             line_part("b", "State which trace shows the louder sound. Give a reason.", 2, 2),
             work_part("c", f"The time base is {clean(tb)} ms per division. Determine the frequency of the sound in trace X.", 3, "frequency (Hz) = ")]
    rows = [row("(a)", f"{hi};", 1, None, "AO3"), row("(a)", "more waves on the screen / shorter time period, so higher frequency;", 1, None, "AO3"),
            row("(b)", f"{loud};", 1, None, "AO3"), row("(b)", "larger amplitude / taller waves;", 1, None, "AO3"),
            row("(c)", f"one wave = {sf(10 / c1, 3)} divisions;", 1, None, "AO3"),
            row("(c)", f"T = {sf(10 / c1, 3)} × {clean(tb)} ms = {sf(T1, 3)} s;", 1, None, "AO2"), row("(c)", f"f = {num(f1, 3)} (Hz);", 1, alts(f1), "AO2")]
    return dict(parts=parts, rows=rows, refs=["3.27P", "3.28P", "3.29P", "3.6"], cmd="Determine", d="7-9", ao=["AO2", "AO3"], figures=figs,
                intro=f"A microphone and oscilloscope display two sounds, X and Y, using the same settings. Each screen is 10 divisions wide.",
                answer={"method": "python", "values": {"fX": f1, "fY": f2}, "checked": True})
