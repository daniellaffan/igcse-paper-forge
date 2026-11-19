"""Topic 6: Magnetism and electromagnetism."""
import physics_svg as S
from physics_util import (K, M, X, T, kb, calc_q, line_part, work_part, row, num, sf, clean, pick, nice, alts)

MG, EM, IN, TF = ("physics.magnetism.magnets", "physics.magnetism.em", "physics.magnetism.induction", "physics.magnetism.transformers")

kb(MG, ["bar magnets", "magnetic materials", "compasses", "magnetic fields", "uniform fields"],
   mcq=[
       M("Which material is magnetic?", ["iron", "copper", "aluminium", "brass"], "6.2"),
       M("Two north poles are placed close together. They", ["repel", "attract", "have no effect on each other", "attract then repel"], "6.2"),
       M("Which is a hard magnetic material?", ["steel", "soft iron", "copper", "glass"], "6.3"),
       M("Magnetic field lines point", ["from north to south", "from south to north", "only towards north poles", "in circles around the poles"], "6.4"),
       M("A soft iron nail is placed near a magnet. It", ["becomes an induced magnet and is attracted", "is repelled", "becomes a permanent magnet", "is unaffected"], "6.5", d="4-6"),
       M("Where is the magnetic field of a bar magnet strongest?", ["at the poles", "at the middle", "far from the magnet", "it is the same everywhere"], "6.4"),
       M("A uniform magnetic field can be produced between", ["opposite poles of two flat magnets placed close together", "two north poles", "the ends of one bar magnet", "two pieces of copper"], "6.7", d="4-6"),
   ],
   recall=[
       K("State what is meant by a *magnetic field*.", 1, ["region where a magnetic material/magnet experiences a force"], "6.4", cmd="State"),
       K("Name **two** magnetic materials.", 2, ["iron", "steel", "nickel", "cobalt"], "6.2", cmd="Name"),
       K("State the difference between a hard and a soft magnetic material.", 2, ["hard: keeps its magnetism (hard to magnetise/demagnetise)", "soft: loses its magnetism easily"], "6.3", cmd="State"),
       K("State what is shown by the direction of a magnetic field line.", 1, ["direction of the force on a north pole"], "6.4", cmd="State", d="4-6"),
       K("State how a uniform field is shown by field lines.", 1, ["parallel, equally spaced lines"], "6.7", cmd="State"),
       K("Give **one** use of a soft magnetic material.", 1, ["electromagnet core / transformer core"], "6.3", cmd="Give"),
   ],
   describe=[
       K("Describe how to test whether a metal bar is a permanent magnet.", 2, ["bring each end towards a pole of a known magnet", "only a magnet can repel"], "6.2", cmd="Describe", d="4-6", ao="AO3"),
       K("Describe the magnetic field pattern around a bar magnet.", 3, ["lines go from N to S", "lines closest together at the poles", "lines do not cross"], "6.4", cmd="Describe"),
       K("Describe what happens when a steel paperclip touches a magnet and is then removed.", 2, ["it becomes magnetised (induced)", "steel is hard so it stays magnetised"], "6.3 6.5", cmd="Describe"),
       K("Describe the field pattern between a north pole and a south pole placed facing each other.", 2, ["lines go straight across from N to S", "parallel and evenly spaced in the middle (uniform)"], "6.6 6.7", cmd="Describe"),
   ])

kb(EM, ["electromagnets", "the motor effect", "loudspeakers", "electric motors", "currents in wires"],
   mcq=[
       M("The field lines around a straight wire carrying a current are", ["concentric circles", "straight parallel lines", "radial lines", "spirals"], "6.10P 6.8"),
       M("Which change would make an electromagnet stronger?", ["more turns of wire", "a copper core", "a smaller current", "fewer turns"], "6.9P"),
       M("In Fleming's left-hand rule the first finger points in the direction of", ["the magnetic field", "the current", "the force", "the motion of electrons"], "6.13"),
       M("Reversing the current in a wire in a magnetic field", ["reverses the force", "doubles the force", "removes the force", "makes the force vertical"], "6.14"),
       M("Which of these uses the motor effect?", ["loudspeaker", "microphone", "transformer", "generator"], "6.12"),
       M("A wire carrying a current is parallel to a magnetic field. The force on it is", ["zero", "maximum", "along the wire", "towards the north pole"], "6.12", d="7-9"),
       M("The field inside a long solenoid is", ["strong and uniform", "zero", "circular", "weakest in the middle"], "6.10P", d="4-6"),
       M("The core of an electromagnet is made of soft iron because", ["it magnetises and demagnetises easily", "it is a permanent magnet", "it conducts electricity", "it is non-magnetic"], "6.9P 6.3", d="4-6"),
   ],
   recall=[
       K("State **two** ways of increasing the force on a current-carrying wire in a magnetic field.", 2, ["increase the current", "use a stronger magnetic field", "longer length of wire in the field"], "6.14", cmd="State"),
       K("State what Fleming's left-hand rule is used for.", 1, ["finding the direction of the force on a current-carrying wire in a magnetic field"], "6.13", cmd="State"),
       K("State **two** ways to make an electromagnet stronger.", 2, ["more turns", "larger current", "soft iron core"], "6.9P", cmd="State"),
       K("State **two** ways of making a d.c. motor spin faster.", 2, ["larger current", "stronger magnet", "more turns on the coil"], "6.12 6.14", cmd="State"),
       K("State what happens to a beam of electrons moving at right angles to a magnetic field.", 1, ["it experiences a force and is deflected / curves"], "6.11P", cmd="State"),
       K("State **two** ways of reversing the direction of rotation of a d.c. motor.", 2, ["reverse the current", "reverse the magnetic field"], "6.12 6.14", cmd="State"),
   ],
   describe=[
       K("Describe how an electromagnet can be made in a school laboratory.", 3, ["coil insulated wire around a soft iron core / nail", "connect to a d.c. supply / cell", "switch on current; switch off to demagnetise"], "6.9P", cmd="Describe"),
       K("Describe the field pattern of a solenoid.", 2, ["similar to a bar magnet outside", "strong, uniform field (parallel lines) inside"], "6.10P", cmd="Describe"),
       K("Describe how to use plotting compasses to show the field around a straight wire carrying a current.", 3, ["wire passes vertically through a horizontal card", "place compasses around the wire and switch on", "compasses point in circles around the wire; reverse current reverses them"], "6.10P", cmd="Describe", ao="AO3"),
       K("Describe how a loudspeaker produces sound.", 3, ["alternating current flows in the coil in a magnetic field", "force on the coil reverses as the current reverses", "coil and cone vibrate, producing sound waves"], "6.12", cmd="Describe", d="4-6"),
   ],
   explain=[
       K("Explain why a coil carrying a current in a magnetic field rotates.", 3, ["current in each side of the coil feels a force", "forces are in opposite directions on the two sides", "producing a turning effect (moment)"], "6.12", cmd="Explain", d="4-6"),
       K("Explain the purpose of the split-ring commutator in a d.c. motor.", 2, ["reverses the current in the coil every half turn", "so the coil keeps turning in the same direction"], "6.12", cmd="Explain", d="7-9"),
       K("Explain why a current-carrying wire placed between two magnets experiences a force.", 2, ["the current produces its own magnetic field", "which interacts with the field of the magnets"], "6.12 6.8", cmd="Explain", d="7-9"),
       K("Explain why an electromagnet is used in a scrapyard crane rather than a permanent magnet.", 2, ["it can be switched off", "so the scrap can be dropped where it is needed"], "6.9P", cmd="Explain"),
       K("Explain why the cone of a loudspeaker vibrates at the same frequency as the a.c. supply.", 2, ["force direction changes each time the current changes direction", "so the cone moves backwards and forwards at that frequency"], "6.12 6.14", cmd="Explain", d="7-9"),
   ],
   extended=[
       X("Explain how a simple d.c. electric motor works and how its speed and direction of rotation can be changed.",
         ["coil of wire between poles of a magnet", "current in the coil", "force on each side of coil (motor effect / Fleming's left-hand rule)", "forces in opposite directions create a turning effect",
          "split-ring commutator reverses current every half turn", "brushes make contact with the commutator", "keeps rotation in one direction", "faster: bigger current, stronger magnet, more turns",
          "reverse direction by reversing current or magnet poles"], "6.12 6.13 6.14"),
       X("Explain how a moving-coil loudspeaker converts an electrical signal into sound.",
         ["permanent magnet with a coil in its field", "coil attached to a paper/plastic cone", "alternating current in the coil", "force on the coil from the motor effect",
          "direction of force reverses as current reverses", "coil and cone vibrate", "cone pushes air to make compressions and rarefactions", "frequency of sound matches frequency of the current",
          "larger current gives larger amplitude / louder sound"], "6.12 6.14"),
   ])

kb(IN, ["generators", "bicycle dynamos", "electromagnetic induction", "power stations", "moving magnets in coils"],
   mcq=[
       M("A voltage is induced in a wire when it", ["moves across magnetic field lines", "is held still in a field", "is made of iron", "carries a large current"], "6.15"),
       M("Pushing a magnet into a coil induces a current. Pulling it out", ["induces a current in the opposite direction", "induces no current", "induces a larger current in the same direction", "demagnetises it"], "6.15", d="4-6"),
       M("Which change would increase the voltage from a generator?", ["rotating the coil faster", "using fewer turns", "using a weaker magnet", "rotating it more slowly"], "6.15 6.16"),
       M("A generator transfers energy from", ["kinetic to electrical", "electrical to kinetic", "chemical to electrical", "thermal to kinetic"], "6.16"),
       M("A magnet is held still inside a coil. The induced voltage is", ["zero", "maximum", "alternating", "constant and large"], "6.15", d="4-6"),
       M("The output of a simple a.c. generator is", ["a voltage that changes direction", "a steady direct voltage", "always zero", "a static charge"], "6.16"),
   ],
   recall=[
       K("State **three** ways of increasing the voltage induced in a coil by a moving magnet.", 3, ["move the magnet faster", "use a stronger magnet", "more turns on the coil", "larger area of coil"], "6.15", cmd="State"),
       K("Name the effect used to generate electricity in a generator.", 1, ["electromagnetic induction"], "6.15 6.16", cmd="Name"),
       K("State **two** ways of reversing the direction of an induced current.", 2, ["reverse the direction of motion", "reverse the magnet / poles"], "6.15", cmd="State"),
       K("State the energy transfer in a generator.", 1, ["kinetic to electrical"], "6.16", cmd="State"),
       K("State what is needed for a voltage to be induced in a conductor.", 1, ["relative movement between conductor and magnetic field / changing field"], "6.15", cmd="State"),
       K("Give **one** device that uses electromagnetic induction.", 1, ["generator / dynamo / transformer / microphone"], "6.15 6.16", cmd="Give"),
   ],
   describe=[
       K("Describe how you could show that a voltage is induced when a magnet moves into a coil.", 3, ["connect the coil to a sensitive ammeter/galvanometer", "push magnet into coil and the meter deflects", "deflection reverses when the magnet is removed; none when stationary"], "6.15", cmd="Describe", ao="AO3"),
       K("Describe how a simple a.c. generator produces a voltage.", 3, ["coil rotated in a magnetic field", "coil sides cut field lines, inducing a voltage", "slip rings and brushes connect to the circuit; voltage reverses each half turn"], "6.16", cmd="Describe", d="4-6"),
       K("Describe how a bicycle dynamo produces electricity.", 2, ["wheel turns a magnet inside a coil", "changing field induces a voltage in the coil"], "6.16", cmd="Describe"),
   ],
   explain=[
       K("Explain why the output of a generator alternates.", 2, ["each side of the coil moves up then down through the field every turn", "so the induced voltage reverses direction every half turn"], "6.16", cmd="Explain", d="7-9"),
       K("Explain why no current is induced when a magnet is held stationary in a coil.", 2, ["field through the coil is not changing", "no field lines being cut"], "6.15", cmd="Explain"),
       K("Explain why turning a generator becomes harder when a lamp is connected to it.", 2, ["current flows in the coil", "the current in the field produces a force opposing the motion / more energy must be transferred"], "6.15 6.16", cmd="Explain", d="7-9"),
       K("Explain why moving a magnet faster into a coil gives a bigger reading on a meter.", 2, ["field lines are cut at a faster rate", "so a larger voltage is induced"], "6.15", cmd="Explain", d="4-6"),
   ],
   extended=[
       X("Describe how electromagnetic induction can be demonstrated with a magnet, a coil and a meter, and explain what affects the size and direction of the induced current.",
         ["connect coil to a centre-zero meter", "move magnet into coil: meter deflects", "magnet stationary: no reading", "pull magnet out: deflection in opposite direction",
          "reverse magnet pole: deflection reversed", "faster movement gives larger deflection", "stronger magnet gives larger deflection", "more turns gives larger deflection",
          "voltage induced as field lines are cut / field changes"], "6.15"),
       X("Explain how a power station generator produces an alternating voltage, and how its output can be increased.",
         ["turbine turns a coil (or electromagnet) in a magnetic field", "coil cuts field lines", "voltage induced by electromagnetic induction", "each side moves up then down every rotation",
          "induced voltage reverses each half turn so it is alternating", "slip rings and brushes connect coil to circuit", "faster rotation increases voltage and frequency",
          "stronger field / more turns increases voltage", "kinetic energy transferred to electrical"], "6.15 6.16"),
   ])

kb(TF, ["transformers", "the National Grid", "phone chargers", "power transmission", "step-up and step-down"],
   mcq=[
       M("A transformer will only work with", ["alternating current", "direct current", "static electricity", "batteries"], "6.17P"),
       M("A step-up transformer has", ["more turns on the secondary coil than the primary", "more turns on the primary coil", "equal numbers of turns", "no iron core"], "6.18P"),
       M("A transformer has 100 primary turns and 500 secondary turns. The primary voltage is 12 V. What is the secondary voltage?", ["60 V", "2.4 V", "12 V", "600 V"], "6.19P", ao="AO2", d="4-6"),
       M("Electricity is transmitted at high voltage to", ["reduce the current and energy losses in the cables", "increase the current", "make it safer at home", "increase the frequency"], "6.18P", d="4-6"),
       M("The core of a transformer is made of", ["soft iron", "copper", "steel magnets", "plastic"], "6.17P"),
       M("For an ideal transformer, which quantity is the same in both coils?", ["power", "voltage", "current", "number of turns"], "6.20P", d="7-9"),
   ],
   recall=[
       K("State the equation linking the voltages and numbers of turns of a transformer.", 1, ["Vp ÷ Vs = Np ÷ Ns"], "6.19P", cmd="State"),
       K("State the equation for the input and output power of a 100% efficient transformer.", 1, ["Vp × Ip = Vs × Is"], "6.20P", cmd="State"),
       K("State where step-down transformers are used in the transmission of electricity.", 1, ["near homes / factories / at substations"], "6.18P", cmd="State"),
       K("Describe the structure of a transformer.", 2, ["two coils of insulated wire", "wound on a (soft) iron core"], "6.17P", cmd="Describe"),
       K("State why the core of a transformer is made from soft iron.", 1, ["easily magnetised and demagnetised as the current alternates"], "6.17P 6.3", cmd="State", d="4-6"),
   ],
   explain=[
       K("Explain how a transformer produces an output voltage.", 3, ["alternating current in primary produces a changing magnetic field", "iron core carries the changing field to the secondary", "changing field induces an alternating voltage in the secondary coil"], "6.17P 6.15", cmd="Explain", d="7-9"),
       K("Explain why transmitting electricity at high voltage reduces energy losses.", 3, ["for the same power, higher voltage means lower current (P = VI)", "heating in cables depends on current", "so less energy is wasted in the cables"], "6.18P", cmd="Explain", d="7-9"),
       K("Explain why a transformer does not work with a steady direct current.", 2, ["a steady current gives a constant magnetic field", "no change in field, so no voltage induced in the secondary"], "6.17P", cmd="Explain", d="7-9"),
       K("Explain why step-down transformers are needed before electricity reaches homes.", 2, ["transmission voltages are very high / dangerous", "appliances need about 230 V"], "6.18P", cmd="Explain"),
   ])


# ====================================================================== magnets: practical & diagrams

@T(MG, "practical", 7, "mg-prac-plot")
def mg_prac(r):
    setup = pick(r, ["a single bar magnet", "two bar magnets with north poles facing", "two bar magnets with opposite poles facing", "a horseshoe magnet"])
    tool = pick(r, ["plotting compasses", "iron filings"])
    parts = [line_part("a", f"Describe how to use {tool} to show the magnetic field pattern of {setup}.", 4, 6),
             line_part("b", "State **one** precaution to obtain a clear pattern.", 1, 2),
             line_part("c", f"Describe the pattern you would expect for {setup}.", 2, 3)]
    if tool == "plotting compasses":
        a = "any four from:\nMP1. place the magnet on a sheet of paper and draw round it;\nMP2. put a plotting compass near one pole;\nMP3. mark the position the compass needle points to with a dot;\nMP4. move the compass so its tail is at the dot and mark again;\nMP5. join the dots to give a field line with an arrow N to S;\nMP6. repeat from different starting points;"
    else:
        a = "any four from:\nMP1. place a sheet of paper/card over the magnet;\nMP2. sprinkle iron filings thinly over the paper;\nMP3. tap the paper gently;\nMP4. filings line up along field lines;\nMP5. draw/photograph the pattern;\nMP6. use a compass to find the direction of the lines;"
    pat = {"a single bar magnet": ("lines from N to S around the magnet;", "closest together at the poles;"),
           "two bar magnets with north poles facing": ("lines curve away from each other between the magnets;", "a neutral point midway where there is no field;"),
           "two bar magnets with opposite poles facing": ("lines go straight across from N to S;", "parallel, evenly spaced (uniform) between the poles;"),
           "a horseshoe magnet": ("lines go across the gap from N to S;", "nearly parallel and evenly spaced in the gap;")}[setup]
    rows = [row("(a)", a, 4, None, "AO3"), row("(b)", "keep other magnets/iron objects away / use a thin layer of filings / tap gently;", 1, None, "AO3"),
            row("(c)", pat[0], 1, None, "AO1"), row("(c)", pat[1], 1, None, "AO1")]
    return dict(parts=parts, rows=rows, refs=["6.6", "6.4", "6.7"], cmd="Describe", d="4-6", ao=["AO1", "AO3"],
                intro=f"A student is investigating the magnetic field of {setup}.", answer={"method": "none", "values": {}, "checked": True})


@T(MG, "practical", 6, "mg-prac-strength")
def mg_prac_strength(r):
    mags = r.sample(["A", "B", "C", "D"], 3)
    clips = r.sample(range(3, 20), 3)
    tab = {"type": "table", "headers": ["magnet", "number of paperclips held"], "rows": [[m, str(c)] for m, c in zip(mags, clips)], "caption": "Results"}
    best = mags[clips.index(max(clips))]
    parts = [line_part("a", "State **two** variables that should be controlled.", 2, 2),
             line_part("b", "State which magnet is strongest.", 1, 1),
             line_part("c", "Suggest **one** improvement to the method.", 1, 2),
             line_part("d", "Describe another way to compare the strength of the magnets.", 2, 3)]
    rows = [row("(a)", "any two from:\nsize/type of paperclips;\nsame pole used;\nhow clips are attached (chain from one clip);\nsame starting position;", 2, None, "AO3"),
            row("(b)", f"{best};", 1, None, "AO3"), row("(c)", "repeat and average / use smaller identical objects / use a top-pan balance method;", 1, None, "AO3"),
            row("(d)", "move a compass towards each magnet and measure distance at which needle deflects;", 1, "allow any valid method", "AO3"),
            row("(d)", "the greater the distance the stronger the magnet;", 1, None, "AO3")]
    return dict(parts=parts, rows=rows, refs=["6.2", "6.5"], cmd="State", d="4-6", ao=["AO3"], figures=[tab],
                intro="A student compares the strength of three magnets by counting how many paperclips each can hold in a chain.",
                answer={"method": "none", "values": {"best": best}, "checked": True})


@T(MG, "diagram", 7, "mg-draw")
def mg_draw(r):
    facing = pick(r, [("N", "S"), ("N", "N"), ("S", "S"), ("S", "N")])
    attract = facing[0] != facing[1]
    fig = {"type": "svg", "svg": S.two_magnets(facing=facing), "width": 100, "caption": "Two bar magnets"}
    parts = [{"label": "a", "text": "Draw the magnetic field pattern in the space between the two magnets. Include arrows.", "marks": 3, "space": "none"},
             line_part("b", "State whether the magnets attract or repel.", 1, 1)]
    if attract:
        rows = [row("(a)", "at least three lines going from one magnet to the other;", 1), row("(a)", "lines straight/parallel in the middle;", 1),
                row("(a)", "arrows pointing from N to S;", 1)]
    else:
        rows = [row("(a)", "lines curving away from each other;", 1), row("(a)", "neutral point shown midway (no lines cross);", 1),
                row("(a)", f"arrows pointing {'away from' if facing[0] == 'N' else 'towards'} both poles;", 1)]
    rows.append(row("(b)", "attract;" if attract else "repel;", 1))
    return dict(parts=parts, rows=rows, refs=["6.2", "6.4", "6.7"], cmd="Draw", d="4-6", ao=["AO1", "AO2"], figures=[fig],
                intro=f"The diagram shows two bar magnets with a {facing[0]} pole facing a {facing[1]} pole.", answer={"method": "none", "values": {"attract": attract}, "checked": True})


@T(MG, "diagram", 6, "mg-single")
def mg_single(r):
    fig = {"type": "svg", "svg": S.bar_magnet_field(lines_drawn=False), "width": 100, "caption": "Bar magnet"}
    pos = pick(r, ["to the right of the north pole", "to the left of the south pole", "above the middle of the magnet", "below the middle of the magnet"])
    dirn = {"to the right of the north pole": "away from the magnet (to the right)", "to the left of the south pole": "towards the magnet (to the right)",
            "above the middle of the magnet": "parallel to the magnet from N to S", "below the middle of the magnet": "parallel to the magnet from N to S"}[pos]
    parts = [{"label": "a", "text": "Draw at least **four** field lines around the magnet. Include arrows.", "marks": 3, "space": "none"},
             line_part("b", f"A plotting compass is placed {pos}. State the direction its north end points.", 1, 2),
             line_part("c", "Mark with a P a place where the field is strongest. Give a reason.", 1, 2)]
    rows = [row("(a)", "lines from one pole to the other;", 1), row("(a)", "arrows from N to S;", 1), row("(a)", "lines closer at the poles and do not cross;", 1),
            row("(b)", f"{dirn};", 1), row("(c)", "P at a pole, where the lines are closest together;", 1)]
    return dict(parts=parts, rows=rows, refs=["6.4", "6.6"], cmd="Draw", d="1-3" if "pole" in pos else "4-6", ao=["AO1", "AO2"], figures=[fig],
                intro="The diagram shows a bar magnet.", answer={"method": "none", "values": {}, "checked": True})


# ====================================================================== electromagnetism diagrams

@T(EM, "diagram", 7, "em-flhr")
def em_flhr(r):
    field = pick(r, ["left to right", "right to left", "into the page", "out of the page"])
    cur = pick(r, ["up the page", "down the page", "into the page", "out of the page", "left to right"])
    axes = {"left to right": (1, 0, 0), "right to left": (-1, 0, 0), "up the page": (0, 1, 0), "down the page": (0, -1, 0), "into the page": (0, 0, -1), "out of the page": (0, 0, 1)}
    B, I = axes[field], axes[cur]
    F = (I[1] * B[2] - I[2] * B[1], I[2] * B[0] - I[0] * B[2], I[0] * B[1] - I[1] * B[0])
    inv = {v: k for k, v in axes.items()}
    if F == (0, 0, 0):
        ans = "no force (current parallel to field)"
    else:
        ans = inv[F]
    fig = {"type": "svg", "svg": S.wire_field_top(current_out=pick(r, [True, False])), "width": 60, "caption": "Field around a wire carrying a current (top view)"}
    parts = [line_part("a", f"A wire carries a current {cur} in a magnetic field directed {field}. Use Fleming's left-hand rule to state the direction of the force on the wire.", 1, 1),
             line_part("b", "The diagram shows the field around a wire seen from above. Describe the shape of the field.", 2, 2),
             line_part("c", "State **two** changes that would increase the force on the wire.", 2, 2)]
    rows = [row("(a)", f"{ans};", 1, None, "AO2"), row("(b)", "concentric circles around the wire;", 1), row("(b)", "further apart further from the wire / direction reverses with current;", 1),
            row("(c)", "any two from:\nlarger current;\nstronger magnet/field;\nlonger length of wire in the field;", 2)]
    return dict(parts=parts, rows=rows, refs=["6.13", "6.10P", "6.14"], cmd="State", d="7-9", ao=["AO1", "AO2"], figures=[fig],
                intro="This question is about the force on a wire in a magnetic field.", answer={"method": "vector cross product", "values": {"force": ans}, "checked": True})


@T(EM, "diagram", 6, "em-solenoid")
def em_solenoid(r):
    core = pick(r, [True, False])
    turns = pick(r, [6, 8, 10, 12])
    fig = {"type": "svg", "svg": S.solenoid(turns=turns, core=core), "width": 100, "caption": "A solenoid connected to a d.c. supply"}
    parts = [{"label": "a", "text": "Draw the magnetic field pattern inside and around the solenoid.", "marks": 3, "space": "none"},
             line_part("b", "State **two** ways of making the field stronger." if not core else "Explain why the soft iron core makes the field stronger.", 2, 2),
             line_part("c", "State what happens to the field if the current is reversed.", 1, 1)]
    rows = [row("(a)", "parallel, evenly spaced lines inside;", 1), row("(a)", "lines outside like a bar magnet's, joining the ends;", 1), row("(a)", "arrows consistent from one end to the other;", 1)]
    rows += ([row("(b)", "any two from:\nmore turns;\nbigger current;\nadd a soft iron core;", 2)] if not core else
             [row("(b)", "the iron becomes magnetised (induced magnet);", 1), row("(b)", "its field adds to the field of the coil;", 1)])
    rows.append(row("(c)", "the poles / field direction reverse;", 1))
    return dict(parts=parts, rows=rows, refs=["6.10P", "6.9P"], cmd="Draw", d="4-6", ao=["AO1", "AO2"], figures=[fig],
                intro=f"The diagram shows a solenoid with {turns} turns{' wound on a soft iron core' if core else ''}.", answer={"method": "none", "values": {}, "checked": True})


@T(EM, "diagram", 5, "em-motor")
def em_motor(r):
    fig = {"type": "svg", "svg": S.motor_diagram(), "width": 100, "caption": "A simple d.c. motor"}
    what = pick(r, ["split-ring commutator", "brushes", "coil", "magnets"])
    use = {"split-ring commutator": "reverses the current in the coil every half turn;", "brushes": "make sliding electrical contact with the commutator;",
           "coil": "carries the current so forces act on it;", "magnets": "provide the magnetic field;"}[what]
    parts = [{"label": "a", "text": "On the diagram, draw arrows to show the direction of the force on each side of the coil.", "marks": 2, "space": "none"},
             line_part("b", f"State the purpose of the {what}.", 1, 2),
             line_part("c", "State **two** ways of making the motor turn in the opposite direction.", 2, 2)]
    rows = [row("(a)", "forces on the two sides of the coil in opposite directions;", 1), row("(a)", "directions consistent with Fleming's left-hand rule for the current shown;", 1),
            row("(b)", use, 1), row("(c)", "reverse the current;", 1), row("(c)", "reverse the magnetic field / swap the magnets;", 1)]
    return dict(parts=parts, rows=rows, refs=["6.12", "6.13", "6.14"], cmd="Draw", d="4-6", ao=["AO1", "AO2"], figures=[fig],
                intro=f"The diagram shows a simple d.c. motor. The current {pick(r, ['flows clockwise', 'flows anticlockwise'])} around the coil as seen from above.",
                answer={"method": "none", "values": {}, "checked": True})


# ====================================================================== transformers calc

@T(TF, "calc", 7, "tf-turns")
def tf_turns(r):
    Np = pick(r, [50, 100, 200, 250, 400, 500, 800, 1000, 2000, 4600])
    Ns = pick(r, [20, 40, 60, 100, 300, 600, 1500, 5000, 10000])
    if Np == Ns:
        Ns *= 2
    Vp = pick(r, [12, 24, 230, 400, 11000, 25000])
    Vs = Vp * Ns / Np
    kind = "step-up" if Ns > Np else "step-down"
    fig = {"type": "svg", "svg": S.transformer(Np, Ns), "width": 90, "caption": "Transformer"}
    if r.random() < 0.6:
        q = calc_q(intro=f"A transformer has {Np} turns on the primary coil and {Ns} turns on the secondary coil. The primary voltage is {Vp} V.",
                   text="Calculate the secondary voltage.", eq="Vp ÷ Vs = Np ÷ Ns", working=[f"{Vp} ÷ Vs = {Np} ÷ {Ns}", f"Vs = {Vp} × {Ns} ÷ {Np}"],
                   ans=num(Vs, 3), unit="V", prefix="secondary voltage (V) = ", refs=["6.19P"], d="4-6", values={"Vs": Vs}, notes=alts(Vs), figs=[fig])
    else:
        q = calc_q(intro=f"A transformer changes {Vp} V to {num(Vs, 3)} V. The primary coil has {Np} turns.", text="Calculate the number of turns on the secondary coil.",
                   eq="Vp ÷ Vs = Np ÷ Ns", working=[f"{Vp} ÷ {num(Vs, 3)} = {Np} ÷ Ns", f"Ns = {Np} × {num(Vs, 3)} ÷ {Vp}"], ans=str(Ns), unit="",
                   prefix="number of turns = ", refs=["6.19P"], d="4-6", values={"Ns": Ns}, notes="answer must be a whole number", figs=[fig])
    q["parts"][0]["label"] = "a"
    for rw in q["rows"]:
        rw["part"] = "(a)"
    q["parts"].append(line_part("b", "State whether this is a step-up or step-down transformer. Give a reason.", 1, 2))
    q["rows"].append(row("(b)", f"{kind}, because the secondary has {'more' if Ns > Np else 'fewer'} turns than the primary;", 1))
    return q


@T(TF, "calc", 7, "tf-power")
def tf_power(r):
    # (context, input voltages, output voltages, input current range lo, hi, step) - realistic for each device
    ctx, vps, vss, lo, hi, st = pick(r, [
        ("a phone charger", [230], [5, 9], 0.02, 0.09, 0.01),
        ("a laptop power unit", [230], [19, 20], 0.2, 0.5, 0.05),
        ("a model railway transformer", [230], [12, 16], 0.1, 0.4, 0.05),
        ("a substation transformer", [132000], [33000, 11000], 50, 300, 10),
        ("a local substation transformer", [11000], [400, 230], 10, 50, 1),
        ("a power station transformer", [25000], [400000, 132000], 1000, 20000, 500)])
    Vp, Vs = pick(r, vps), pick(r, vss)
    Ip = nice(r, lo, hi, st)
    Is = Vp * Ip / Vs
    if r.random() < 0.5:
        return calc_q(intro=f"{ctx.capitalize()} is 100% efficient. The input is {Vp} V and {clean(Ip)} A. The output voltage is {Vs} V.", text="Calculate the output current.",
                      eq="Vp × Ip = Vs × Is", working=[f"{Vp} × {clean(Ip)} = {Vs} × Is", f"Is = {num(Vp * Ip, 4)} ÷ {Vs}"], ans=num(Is, 3), unit="A",
                      prefix="current (A) = ", refs=["6.20P"], d="7-9", values={"Is": Is}, notes=alts(Is),
                      state=("input voltage, input current, output voltage and output current", "Vp × Ip = Vs × Is", None) if r.random() < 0.5 else None)
    P = float(sf(Vp * Ip, 3))  # the printed power; the answer is computed from it
    Is = P / Vs
    return calc_q(intro=f"{ctx.capitalize()} is 100% efficient and delivers {num(P, 3)} W at {Vs} V.", text="Calculate the current in the secondary coil.",
                  eq="P = I × V", working=[f"{num(P, 3)} = Is × {Vs}", f"Is = {num(P, 3)} ÷ {Vs}"], ans=num(Is, 3), unit="A", prefix="current (A) = ",
                  refs=["6.20P", "2.4"], d="4-6", values={"Is": Is}, notes=alts(Is))


kb(IN, [], describe=[
    K("Describe what happens to the reading on a meter connected to a coil as a magnet is dropped through it.", 2, ["meter deflects one way as the magnet enters", "and the opposite way as it leaves"], "6.15", cmd="Describe", d="7-9"),
    K("Describe how a wire can be moved to induce a voltage across it in a magnetic field.", 2, ["move the wire at right angles to the field lines", "so that it cuts the field lines"], "6.15", cmd="Describe"),
    K("Describe how the output of a generator changes when the coil is turned twice as fast.", 2, ["peak voltage is larger", "frequency of the alternating output doubles"], "6.16", cmd="Describe", d="7-9"),
    K("Describe the energy transfers in a wind turbine generator.", 2, ["kinetic energy of the wind turns the blades and coil", "electromagnetic induction transfers it electrically"], "6.16", cmd="Describe"),
])


@T(MG, "diagram", 7, "mg-induced")
def mg_induced(r):
    pole = pick(r, ["N", "S"])
    obj = pick(r, ["soft iron nail", "steel paperclip", "iron rod", "soft iron bar", "steel pin", "iron key"])
    side = pick(r, ["left", "right"])
    other = "S" if pole == "N" else "N"
    hard = "steel" in obj
    parts = [{"label": "a", "text": f"On the diagram, label the induced poles on the {obj}.", "marks": 2, "space": "none"},
             line_part("b", f"Explain why the {obj} is attracted to the magnet.", 2, 2),
             line_part("c", f"State what happens to the {obj} when the magnet is removed.", 1, 1)]
    rows = [row("(a)", f"{other} at the end nearest the magnet's {pole} pole;", 1), row("(a)", f"{pole} at the far end;", 1),
            row("(b)", "it becomes an induced magnet;", 1), row("(b)", "the nearest end has the opposite pole, and opposite poles attract;", 1),
            row("(c)", "it keeps (some of) its magnetism, as steel is a hard magnetic material;" if hard else "it loses its magnetism, as iron is a soft magnetic material;", 1)]
    fig = {"type": "svg", "svg": S.magnet_and_bar(pole, side), "width": 100,
           "caption": f"Bar magnet and {obj}"}
    return dict(parts=parts, rows=rows, refs=["6.5", "6.3", "6.2"], cmd="Label", d="4-6", ao=["AO1", "AO2"], figures=[fig],
                intro=f"A {obj} is placed near the {pole} pole of a bar magnet, on its {side}.", answer={"method": "none", "values": {}, "checked": True})
