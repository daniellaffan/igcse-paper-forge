"""Topic 7: Radioactivity and particles."""
import physics_svg as S
from physics_util import (K, M, X, T, kb, calc_q, line_part, work_part, row, num, sf, clean, pick, nice, alts)

AT, HL, NU = ("physics.radioactivity.atoms", "physics.radioactivity.halflife", "physics.radioactivity.nuclear")

kb(AT, ["atomic structure", "isotopes", "alpha, beta and gamma radiation", "detecting radiation", "nuclear equations"],
   mcq=[
       M("What is the charge on an alpha particle?", ["+2", "-1", "0", "+1"], "7.5"),
       M("Which radiation is most penetrating?", ["gamma", "alpha", "beta", "they are all the same"], "7.5"),
       M("Which radiation is the most strongly ionising?", ["alpha", "beta", "gamma", "X-rays"], "7.5"),
       M("Isotopes of an element have the same number of", ["protons", "neutrons", "nucleons", "particles in the nucleus"], "7.3"),
       M("What is a beta particle?", ["a fast-moving electron from the nucleus", "a helium nucleus", "an electromagnetic wave", "a proton"], "7.5"),
       M("When a nucleus emits an alpha particle, its mass number", ["decreases by 4", "decreases by 2", "increases by 1", "stays the same"], "7.7", d="4-6"),
       M("When a nucleus emits a beta particle, its atomic number", ["increases by 1", "decreases by 1", "decreases by 2", "stays the same"], "7.7", d="4-6"),
       M("Which is stopped by a few millimetres of aluminium but not by paper?", ["beta", "alpha", "gamma", "neutrons"], "7.5"),
       M("Which detector is used to measure the count rate from a source?", ["Geiger-Müller tube", "thermometer", "voltmeter", "oscilloscope"], "7.9"),
   ],
   recall=[
       K("State what is meant by *isotopes*.", 2, ["atoms with the same number of protons", "but different numbers of neutrons"], "7.3", cmd="State"),
       K("State what is meant by the *mass number* of a nucleus.", 1, ["total number of protons and neutrons"], "7.3", cmd="State"),
       K("State what is meant by the *atomic number*.", 1, ["number of protons"], "7.3", cmd="State"),
       K("Name **two** ways of detecting ionising radiation.", 2, ["photographic film", "Geiger-Müller tube (and counter)"], "7.9", cmd="Name"),
       K("State what an alpha particle consists of.", 1, ["two protons and two neutrons | allow helium nucleus"], "7.5", cmd="State"),
       K("State what gamma radiation is.", 1, ["high-frequency electromagnetic wave (from the nucleus)"], "7.5", cmd="State"),
       K("State what is meant by *ionisation*.", 1, ["atom gains or loses electrons to become charged"], "7.4", cmd="State", d="4-6"),
       K("State what is meant by radioactive decay being *random*.", 1, ["cannot predict when a particular nucleus will decay"], "7.4", cmd="State", d="4-6"),
   ],
   describe=[
       K("Describe the structure of an atom.", 3, ["small, dense nucleus containing protons and neutrons", "electrons orbit the nucleus", "most of the atom is empty space"], "7.2", cmd="Describe"),
       K("Describe what happens to a nucleus when it emits a gamma ray.", 2, ["it loses energy", "atomic and mass numbers do not change"], "7.7", cmd="Describe", d="4-6"),
       K("Describe what happens to a nucleus during beta decay.", 2, ["a neutron changes into a proton and an electron", "electron emitted; atomic number up by 1, mass number unchanged"], "7.7", cmd="Describe", d="7-9"),
       K("Describe how a Geiger-Müller tube and counter are used to measure count rate.", 2, ["place tube near source and count the clicks/counts", "over a measured time; subtract background"], "7.9 7.6", cmd="Describe", ao="AO3"),
       K("Describe the differences between alpha and gamma radiation.", 3, ["alpha is a particle; gamma is an electromagnetic wave", "alpha strongly ionising; gamma weakly", "alpha stopped by paper; gamma needs thick lead"], "7.5", cmd="Describe"),
   ],
   explain=[
       K("Explain why alpha particles are the most dangerous radiation inside the body.", 2, ["alpha is the most ionising", "cannot escape, so all energy absorbed by nearby cells"], "7.5", cmd="Explain", d="7-9"),
       K("Explain why atoms are neutral.", 2, ["number of protons equals number of electrons", "proton and electron charges are equal and opposite"], "7.2", cmd="Explain"),
       K("Explain why gamma radiation passes through materials more easily than alpha radiation.", 2, ["gamma is weakly ionising so loses little energy", "alpha is strongly ionising and loses its energy quickly"], "7.5", cmd="Explain", d="7-9"),
       K("Explain why a nucleus with too many neutrons may undergo beta decay.", 2, ["a neutron changes to a proton (and electron)", "making the nucleus more stable"], "7.7", cmd="Explain", d="7-9"),
       K("Explain why carbon-12 and carbon-14 are isotopes.", 2, ["both have 6 protons", "they have different numbers of neutrons (6 and 8)"], "7.3", cmd="Explain"),
   ])

kb(HL, ["background radiation", "half-life", "uses of radioactivity", "medical tracers", "safety with radioactive sources", "radioactive waste"],
   mcq=[
       M("What is the unit of activity?", ["becquerel", "sievert", "hertz", "joule"], "7.1 7.11"),
       M("Which is a natural source of background radiation?", ["radon gas", "X-ray machines", "nuclear weapons tests", "microwave ovens"], "7.10"),
       M("A source has a half-life of 2 hours. What fraction remains after 6 hours?", ["1/8", "1/6", "1/3", "1/4"], "7.13", ao="AO2", d="4-6"),
       M("The half-life of a sample is the time for", ["half the unstable nuclei to decay", "all the nuclei to decay", "the mass to halve by evaporation", "the activity to double"], "7.12"),
       M("Which radiation is used to sterilise medical equipment?", ["gamma", "alpha", "beta", "neutrons"], "7.14"),
       M("An object that has been irradiated", ["does not become radioactive", "becomes radioactive", "emits alpha particles", "has radioactive atoms on its surface"], "7.15", d="4-6"),
       M("A medical tracer should have a half-life of", ["a few hours", "a few seconds", "thousands of years", "millions of years"], "7.14", d="7-9"),
       M("Which device controls paper thickness in a paper mill?", ["a beta source and detector", "an alpha source", "a gamma source in a lead box", "a smoke detector"], "7.14", d="4-6"),
   ],
   recall=[
       K("State what is meant by *half-life*.", 1, ["time for half the unstable nuclei to decay | allow time for activity/count rate to halve"], "7.12", cmd="State"),
       K("Name **two** sources of background radiation.", 2, ["radon gas", "rocks / soil / buildings", "cosmic rays", "food and drink", "medical X-rays", "nuclear industry"], "7.10", cmd="Name"),
       K("State what is meant by *activity* of a source.", 1, ["number of nuclei that decay per second"], "7.11", cmd="State"),
       K("State the difference between contamination and irradiation.", 2, ["contamination: radioactive material is on or inside an object", "irradiation: object exposed to radiation from outside, does not become radioactive"], "7.15", cmd="State", d="4-6"),
       K("Give **two** precautions when handling radioactive sources.", 2, ["use tongs / handle at arm's length", "store in a lead-lined box", "minimise time of exposure", "never point at people", "wash hands"], "7.16", cmd="Give"),
       K("Give **two** uses of radioactivity in medicine.", 2, ["tracers", "radiotherapy (killing cancer cells)", "sterilising equipment"], "7.14", cmd="Give"),
       K("Give **one** use of radioactivity in industry.", 1, ["thickness control / leak detection / smoke detectors / sterilising / dating"], "7.14", cmd="Give"),
   ],
   explain=[
       K("Explain why a gamma emitter is used as a medical tracer rather than an alpha emitter.", 2, ["gamma passes out of the body and can be detected", "alpha would be absorbed and damage cells"], "7.14", cmd="Explain", d="4-6"),
       K("Explain why radioactive waste must be stored for a long time.", 2, ["some isotopes have very long half-lives", "remain dangerously active for thousands of years"], "7.16", cmd="Explain"),
       K("Explain why a beta source is used to control the thickness of aluminium foil.", 2, ["alpha would be completely absorbed; gamma would pass through almost unaffected", "count rate of beta changes with small changes in thickness"], "7.14", cmd="Explain", d="7-9"),
       K("Explain why a count rate measured with a GM tube must be corrected.", 2, ["background radiation is always present", "subtract the background count to find the count from the source"], "7.10", cmd="Explain", d="4-6"),
       K("Explain why ionising radiation is harmful to living cells.", 2, ["ionises atoms in cells / damages DNA", "can kill cells or cause mutations leading to cancer"], "7.16", cmd="Explain"),
       K("Explain why contamination is usually more dangerous than irradiation.", 2, ["contaminating material stays in/on the body", "so exposure continues for a long time"], "7.15", cmd="Explain", d="7-9"),
   ],
   extended=[
       X("Discuss the uses of radioactive isotopes in hospitals and the precautions needed to protect patients and staff.",
         ["tracers inject a gamma emitter to image organs", "tracer has short half-life so it does not stay active", "radiotherapy uses gamma rays aimed at a tumour", "beam rotated to limit dose to healthy tissue",
          "gamma sterilises equipment", "ionising radiation damages cells / DNA", "staff wear film badges to monitor dose", "lead aprons and screens", "sources stored in lead containers",
          "minimise time and keep distance from source"], "7.14 7.16"),
       X("Explain what is meant by half-life and how it can be measured using a Geiger-Müller tube. Include how background radiation is dealt with.",
         ["half-life is the time for half the nuclei to decay / count rate to halve", "decay is random but predictable for large numbers", "measure background count with source removed",
          "place GM tube a fixed distance from the source", "record counts in fixed time intervals", "subtract background from each reading", "plot corrected count rate against time",
          "read time for count rate to fall to half from graph", "repeat from different starting points and average"], "7.12 7.13 7.10"),
   ])

kb(NU, ["nuclear fission", "nuclear reactors", "chain reactions", "nuclear fusion", "energy from the nucleus"],
   mcq=[
       M("Which nucleus is commonly used as fuel in fission reactors?", ["uranium-235", "hydrogen-1", "carbon-14", "helium-4"], "7.18"),
       M("What causes a uranium-235 nucleus to split?", ["absorbing a neutron", "absorbing an electron", "being heated", "emitting a gamma ray"], "7.18"),
       M("The control rods in a reactor", ["absorb neutrons", "slow down neutrons", "absorb heat", "speed up fission"], "7.21"),
       M("The moderator in a reactor", ["slows down neutrons", "absorbs neutrons", "absorbs gamma rays", "cools the reactor"], "7.21"),
       M("Nuclear fusion is", ["the joining of two light nuclei", "the splitting of a heavy nucleus", "the emission of alpha particles", "the absorption of neutrons"], "7.23"),
       M("Fusion requires very high temperatures because", ["the positive nuclei repel each other", "neutrons must be slowed", "electrons must be removed", "gamma rays are needed"], "7.26", d="7-9"),
       M("A fission event usually releases", ["two or three neutrons", "only one proton", "no particles", "a single alpha particle"], "7.19"),
       M("The energy released by fission is mainly transferred to", ["the kinetic energy of the products", "light", "chemical energy", "gravitational potential energy"], "7.18", d="4-6"),
   ],
   recall=[
       K("State what is meant by *nuclear fission*.", 1, ["splitting of a large nucleus into two smaller nuclei"], "7.18 7.23", cmd="State"),
       K("State what is meant by *nuclear fusion*.", 1, ["joining of two small nuclei to form a larger nucleus"], "7.23", cmd="State"),
       K("State the products of the fission of uranium-235.", 2, ["two daughter nuclei (radioactive)", "two or three neutrons (and energy)"], "7.19", cmd="State"),
       K("Name a material used as a moderator.", 1, ["graphite / water"], "7.21", cmd="Name"),
       K("Name a material used for control rods.", 1, ["boron / cadmium"], "7.21", cmd="Name"),
       K("State what powers stars.", 1, ["nuclear fusion (of hydrogen into helium)"], "7.25", cmd="State"),
       K("State the purpose of the thick concrete shielding around a reactor.", 1, ["absorbs radiation / neutrons escaping from the core"], "7.22", cmd="State"),
   ],
   describe=[
       K("Describe what happens in a chain reaction.", 3, ["neutron absorbed by U-235 nucleus, which splits", "releasing 2 or 3 neutrons", "which go on to cause further fissions"], "7.20", cmd="Describe"),
       K("Describe how the rate of fission in a reactor is controlled.", 2, ["control rods absorb neutrons", "lowered further to slow the reaction; raised to speed it up"], "7.21", cmd="Describe"),
       K("Describe how energy from a nuclear reactor is used to generate electricity.", 3, ["fission heats the coolant/water", "producing steam", "which turns a turbine and generator"], "7.18 4.18P", cmd="Describe"),
       K("Describe the process of fusion in the Sun.", 2, ["hydrogen nuclei fuse to form helium", "small loss of mass released as energy"], "7.24 7.25", cmd="Describe"),
   ],
   explain=[
       K("Explain why the neutrons released in fission must be slowed down.", 2, ["slow neutrons are more likely to be absorbed by U-235", "so the chain reaction can continue"], "7.21", cmd="Explain", d="7-9"),
       K("Explain why fusion does not happen at normal temperatures.", 2, ["nuclei are positive and repel each other", "need very high temperature/pressure so they move fast enough to get close"], "7.26", cmd="Explain", d="4-6"),
       K("Explain why the waste from a fission reactor is dangerous.", 2, ["daughter products are radioactive", "some have long half-lives"], "7.19 7.16", cmd="Explain"),
       K("Explain what would happen if all the control rods were removed from a reactor.", 2, ["more neutrons available to cause fission", "chain reaction would go out of control / overheat"], "7.20 7.21", cmd="Explain", d="7-9"),
       K("Explain why fusion is not yet used in power stations.", 2, ["very high temperatures and pressures are needed", "difficult to contain / more energy put in than produced so far"], "7.26", cmd="Explain", d="7-9"),
   ],
   extended=[
       X("Describe how a nuclear fission reactor produces energy and how the reaction is kept under control.",
         ["neutron absorbed by uranium-235", "nucleus splits into two daughter nuclei", "releases two or three neutrons and energy", "energy as kinetic energy of products, heats the core",
          "released neutrons cause further fissions: chain reaction", "moderator (graphite/water) slows neutrons", "control rods (boron) absorb neutrons", "rods raised or lowered to control rate",
          "coolant carries heat to make steam", "shielding absorbs radiation"], "7.18 7.19 7.20 7.21 7.22"),
       X("Compare nuclear fission and nuclear fusion.",
         ["fission splits a heavy nucleus; fusion joins light nuclei", "both release energy", "fission uses uranium/plutonium; fusion uses hydrogen isotopes", "fission is started by absorbing a neutron",
          "fusion needs very high temperature and pressure", "to overcome repulsion between positive nuclei", "fission produces radioactive waste; fusion produces little", "fission used in power stations now",
          "fusion powers stars", "fusion releases energy from a small loss of mass"], "7.17 7.23 7.24 7.26"),
   ])


# ====================================================================== atoms: nuclear equations / decay charts

NUC = [("radium", "Ra", 88, 226), ("uranium", "U", 92, 238), ("polonium", "Po", 84, 210), ("thorium", "Th", 90, 232), ("americium", "Am", 95, 241),
       ("carbon", "C", 6, 14), ("strontium", "Sr", 38, 90), ("iodine", "I", 53, 131), ("cobalt", "Co", 27, 60), ("caesium", "Cs", 55, 137), ("radon", "Rn", 86, 222)]


@T(AT, "diagram", 7, "at-chart")
def at_chart(r):
    name, sym, Z, A = pick(r, NUC)
    kind = "alpha" if Z > 80 else pick(r, ["beta", "beta", "alpha"]) if Z > 50 else "beta"
    N = A - Z
    if kind == "alpha":
        Z2, A2 = Z - 2, A - 4
    else:
        Z2, A2 = Z + 1, A
    N2 = A2 - Z2
    fig = {"type": "svg", "svg": S.nz_chart([(Z, N, f"{sym}-{A}")], (min(Z, Z2) - 1, max(Z, Z2) + 1), (min(N, N2) - 1, max(N, N2) + 1)), "width": 80,
           "caption": "Neutron number against proton number"}
    parts = [line_part("a", f"State the number of protons and neutrons in a nucleus of {name}-{A}.", 2, 2),
             {"label": "b", "text": f"{name.capitalize()}-{A} decays by {kind} emission. Mark on the chart the position of the daughter nucleus and draw an arrow showing the decay.", "marks": 2, "space": "none"},
             line_part("c", "State the mass number and atomic number of the daughter nucleus.", 2, 2)]
    rows = [row("(a)", f"{Z} protons;", 1), row("(a)", f"{N} neutrons;", 1),
            row("(b)", f"point at Z = {Z2}, N = {N2};", 1), row("(b)", f"arrow from ({Z}, {N}) to ({Z2}, {N2});", 1),
            row("(c)", f"mass number {A2};", 1, "allow ecf from (b)"), row("(c)", f"atomic number {Z2};", 1)]
    return dict(parts=parts, rows=rows, refs=["7.2", "7.3", "7.7"], cmd="Mark", d="7-9", ao=["AO1", "AO2"], figures=[fig],
                intro=f"The chart shows the nucleus of {name}-{A}.", answer={"method": "python", "values": {"Z2": Z2, "A2": A2}, "checked": True})


@T(AT, "diagram", 7, "at-equation")
def at_equation(r):
    name, sym, Z, A = pick(r, NUC)
    kind = pick(r, ["alpha", "beta"])
    if kind == "alpha":
        Z2, A2, part_ = Z - 2, A - 4, "⁴₂He (α)"
    else:
        Z2, A2, part_ = Z + 1, A, "⁰₋₁e (β)"
    parts = [{"label": "a", "text": f"Complete the nuclear equation for the {kind} decay of {name}-{A} (atomic number {Z}). The daughter nucleus is X.\n\n{A}/{Z} {sym} → ..../.... X + ....", "marks": 3, "space": "lines", "lines": 2},
             line_part("b", "Explain how you know the equation is balanced.", 2, 2)]
    rows = [row("(a)", f"X: mass number {A2};", 1), row("(a)", f"X: atomic number {Z2};", 1), row("(a)", f"{part_} with correct numbers;", 1),
            row("(b)", "mass numbers on each side add up to the same total;", 1), row("(b)", "atomic numbers (charge) on each side add up to the same total;", 1)]
    return dict(parts=parts, rows=rows, refs=["7.7", "7.8"], cmd="Complete", d="7-9", ao=["AO2"],
                intro=f"{name.capitalize()}-{A} is radioactive.", answer={"method": "python", "values": {"Z2": Z2, "A2": A2}, "checked": True})


@T(AT, "practical", 7, "at-prac-abs")
def at_prac(r):
    kind = pick(r, ["alpha", "beta", "gamma", "beta and gamma", "alpha and beta"])
    bg = r.randint(15, 30)
    mats = ["no absorber", "paper", "3 mm aluminium", "2 cm lead"]
    base = r.randint(400, 900)
    stop = {"alpha": 1, "beta": 2, "gamma": 4, "beta and gamma": 2, "alpha and beta": 1}[kind]
    counts = []
    for k, m in enumerate(mats):
        if kind == "beta and gamma":
            c = base if k < 2 else (base // 5 if k == 2 else base // 25)
        elif kind == "alpha and beta":
            c = base if k == 0 else (base // 3 if k == 1 else 0)
        elif k < stop:
            c = base if k == 0 else int(base * 0.95)
        elif kind == "gamma":
            c = base // 4
        else:
            c = 0
        counts.append(c + bg)
    tab = {"type": "table", "headers": ["absorber", "count in 1 minute"], "rows": [[m, str(c)] for m, c in zip(mats, counts)], "caption": f"Results (background count {bg} per minute)"}
    parts = [line_part("a", "Describe how the student should measure the background count.", 2, 2),
             line_part("b", "Use the results to identify the type or types of radiation emitted. Give reasons.", 3, 4),
             line_part("c", "Give **two** safety precautions the student should take.", 2, 2)]
    rows = [row("(a)", "remove all sources from the area;", 1, None, "AO3"), row("(a)", "record count with the GM tube over a fixed time (and repeat for a mean);", 1, None, "AO3"),
            row("(b)", f"{kind};", 1, None, "AO3")]
    reasons = {"alpha": ["count falls to background with paper;", "so radiation is stopped by paper;"],
               "beta": ["little change with paper;", "falls to background with aluminium;"],
               "gamma": ["little change with paper or aluminium;", "lead reduces but does not stop it;"],
               "beta and gamma": ["count falls a lot with aluminium (beta stopped);", "some count remains through lead (gamma);"],
               "alpha and beta": ["count falls with paper (alpha stopped);", "falls to background with aluminium (beta stopped);"]}[kind]
    rows += [row("(b)", reasons[0], 1, None, "AO3"), row("(b)", reasons[1], 1, None, "AO3"),
             row("(c)", "any two from:\nhandle source with tongs;\nkeep source at arm's length;\nreturn to lead box quickly;\nnever point source at people;\nminimise time of exposure;", 2, None, "AO3")]
    return dict(parts=parts, rows=rows, refs=["7.6", "7.5", "7.9", "7.10"], cmd="Describe", d="7-9", ao=["AO3"], figures=[tab, {"type": "svg", "svg": S.gm_absorber(), "width": 80, "caption": "Apparatus"}],
                intro="A student places different absorbers between a radioactive source and a GM tube connected to a counter.",
                answer={"method": "none", "values": {"type": kind}, "checked": True})


# ====================================================================== half-life calc / data

ISO = [("iodine-131", 8, "days"), ("technetium-99m", 6, "hours"), ("radon-222", 3.8, "days"), ("cobalt-60", 5.3, "years"), ("strontium-90", 29, "years"),
       ("carbon-14", 5700, "years"), ("phosphorus-32", 14, "days"), ("sodium-24", 15, "hours"), ("an unknown isotope", 20, "minutes")]


@T(HL, "calc", 7, "hl-frac")
def hl_frac(r):
    iso, th, unit = pick(r, ISO)
    n = r.randint(2, 5)
    A0 = pick(r, [800, 1200, 1600, 2400, 3200, 4800, 6400])
    A = A0 / 2 ** n
    t = th * n
    if r.random() < 0.5:
        return calc_q(intro=f"A sample of {iso} has an activity of {A0} Bq. Its half-life is {clean(th)} {unit}.", text=f"Calculate the activity after {clean(t)} {unit}.",
                      eq="activity halves each half-life", working=[f"number of half-lives = {clean(t)} ÷ {clean(th)} = {n}", f"activity = {A0} ÷ 2^{n}"],
                      ans=num(A, 3), unit="Bq", prefix="activity (Bq) = ", refs=["7.13", "7.11"], d="4-6", rearr=False, values={"n": n, "A": A}, notes=alts(A))
    return calc_q(intro=f"The activity of a sample of {iso} falls from {A0} Bq to {num(A, 3)} Bq in {clean(t)} {unit}.", text="Calculate the half-life.",
                  eq="activity halves each half-life", working=[f"{A0} → {' → '.join(num(A0 / 2 ** k, 3) for k in range(1, n + 1))}", f"{n} half-lives in {clean(t)} {unit}", f"half-life = {clean(t)} ÷ {n}"],
                  ans=clean(th), unit=unit, prefix=f"half-life ({unit}) = ", refs=["7.13"], d="4-6", rearr=False, values={"n": n, "th": th}, notes="first mark for number of half-lives")


@T(HL, "calc", 7, "hl-remain")
def hl_remain(r):
    iso, th, unit = pick(r, ISO)
    n = r.randint(2, 6)
    m0 = pick(r, [8, 16, 32, 40, 64, 80, 120])
    frac = 1 / 2 ** n
    if r.random() < 0.5:
        return calc_q(intro=f"A sample contains {m0} mg of {iso} (half-life {clean(th)} {unit}).", text=f"Calculate the mass of {iso} remaining after {clean(th * n)} {unit}.",
                      eq="amount halves each half-life", working=[f"{n} half-lives", f"mass = {m0} × (½)^{n}"], ans=num(m0 * frac, 3), unit="mg", prefix="mass (mg) = ",
                      refs=["7.13", "7.12"], d="4-6", rearr=False, values={"m": m0 * frac}, notes=alts(m0 * frac))
    return calc_q(intro=f"The half-life of {iso} is {clean(th)} {unit}.", text=f"Calculate the fraction of the original nuclei that remain undecayed after {clean(th * n)} {unit}.",
                  eq="fraction = (½)^n", working=[f"n = {clean(th * n)} ÷ {clean(th)} = {n}", f"fraction = (½)^{n}"], ans=f"1/{2 ** n}", unit="", prefix="fraction = ",
                  refs=["7.13", "7.12"], d="4-6", rearr=False, values={"fraction": frac}, notes=f"allow {sf(frac, 3)} or {sf(frac * 100, 3)}%")


@T(HL, "data", 14, "hl-graph")
def hl_graph(r):
    th = pick(r, [2, 3, 4, 5, 6, 8, 10, 12])
    unit = pick(r, ["minutes", "hours", "days"])
    C0 = pick(r, [400, 480, 600, 640, 800, 960])
    bg = pick(r, [0, 0, 20, 30])
    ts = [k * th / 2 for k in range(0, 11)]
    src = C0 - bg  # C0 is the plotted (total) count rate at t = 0; only the source part halves
    cs = [round(src * 0.5 ** (t / th)) + bg for t in ts]
    tmax = ts[-1]
    pts = [(t, c) for t, c in zip(ts, cs)]
    fig = {"type": "svg", "svg": S.graph(tmax, max(cs) * 1.1, f"time in {unit}", "count rate in counts/min", series=[{"pts": pts, "join": "curve", "marker": "x"}]),
           "width": 100, "caption": "Count rate against time"}
    parts = [line_part("a", "Use the graph to determine the half-life of the source. Show your working on the graph.", 2, 2, prefix=f"half-life ({unit}) = "),
             work_part("b", f"Predict the count rate after {clean(5 * th)} {unit}.", 2, "count rate (counts/min) = "),
             line_part("c", "Explain why the points do not lie exactly on a smooth curve in a real experiment.", 1, 2)]
    if bg:
        parts[0]["text"] = f"The background count rate is {bg} counts/min and is included in the graph. Use the graph to determine the half-life of the source. Show your working."
    # The graph plots source + background, so subtract bg before halving and add it back.
    pred = src / 32 + bg
    step = f"({C0} - {bg}) ÷ 32 + {bg}" if bg else f"{C0} ÷ 32"
    rows = [row("(a)", "lines drawn on graph showing count rate (minus background) halving;", 1, None, "AO3"), row("(a)", f"{clean(th)} {unit};", 1, "allow ±half a small square", "AO3"),
            row("(b)", f"5 half-lives: {step};", 1, "allow ecf" + ("; subtract background before halving, then add it back" if bg else ""), "AO2"), row("(b)", f"{sf(pred, 3)} counts/min;", 1, alts(pred), "AO2"),
            row("(c)", "radioactive decay is random;", 1, None, "AO1")]
    return dict(parts=parts, rows=rows, refs=["7.12", "7.13", "7.4", "7.10"], cmd="Determine", d="7-9" if bg else "4-6", ao=["AO2", "AO3"], figures=[fig],
                intro=f"A student measures the count rate from a radioactive source every {clean(th / 2)} {unit}.",
                answer={"method": "python", "values": {"half_life": th, "pred": pred}, "checked": True})


@T(AT, "practical", 7, "at-prac-thick")
def at_prac_thick(r):
    bg = r.randint(15, 35)
    c0 = r.randint(500, 1200)
    k = r.uniform(0.35, 0.6)
    th = [0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
    cs = [round(c0 * 2.718 ** (-k * x / 0.5 * 0.7)) + bg for x in th]
    cs[-1] = bg + r.randint(0, 3)
    tab = {"type": "table", "headers": ["aluminium thickness in mm"] + [clean(x) for x in th], "rows": [["count in 1 min"] + [str(c) for c in cs]], "caption": "Results"}
    parts = [line_part("a", "State the independent and dependent variables.", 2, 2),
             work_part("b", f"The background count is {bg} per minute. Calculate the corrected count for 1.0 mm of aluminium.", 1, "corrected count = "),
             line_part("c", "State the type of radiation emitted by the source. Give a reason using the results.", 2, 3),
             line_part("d", "Suggest why the student repeats each reading three times.", 1, 2)]
    rows = [row("(a)", "independent: thickness of aluminium;", 1, None, "AO3"), row("(a)", "dependent: count (rate);", 1, None, "AO3"),
            row("(b)", f"{cs[2] - bg};", 1, None, "AO2"),
            row("(c)", "beta;", 1, None, "AO3"), row("(c)", "count falls to background with a few mm of aluminium;", 1, None, "AO3"),
            row("(d)", "decay is random, so a mean is more reliable;", 1, None, "AO3")]
    return dict(parts=parts, rows=rows, refs=["7.6", "7.5", "7.10", "7.4"], cmd="State", d="4-6", ao=["AO2", "AO3"], figures=[tab],
                intro=f"A student places sheets of aluminium of increasing thickness between a {pick(r, ['radioactive source', 'sealed source', 'school source'])} and a GM tube {pick(r, ['3 cm', '4 cm', '5 cm'])} away.",
                answer={"method": "python", "values": {"corrected": cs[2] - bg}, "checked": True})
