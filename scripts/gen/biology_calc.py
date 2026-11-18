"""Calculation templates (magnification, percentage change, rates, means, ratios, efficiency, estimates).

Every answer is computed here and stored in answer.values; mark-scheme rows quote the same numbers.
"""
import math
import random

from biology_lib import reg, calc_part, text_part, row_, table_fig, nf, sfig, points_row, a_an, unit_of

N = 14


def cq(text, marks, prefix, steps, final, refs, diff, values, method, intro=None, figures=None,
       final_note="Allow full marks for the correct answer with no working", extra=None, cw="Calculate"):
    """Single calculation part (optionally followed by an extra non-calc part in `extra`)."""
    lab = "a" if extra else ""
    parts = [calc_part(lab, text, marks, prefix, suffix=unit_of(final))]
    rows = [row_(lab, s + " (1)", 1, None, "AO2") for s in steps]
    rows.append(row_(lab, final + " (1)", 1, final_note, "AO2"))
    assert len(rows) == marks, (text, marks, len(rows))
    if extra:
        p, r = extra
        p["label"] = "b"
        r["part"] = "b"
        parts.append(p)
        rows.append(r)
    return dict(parts=parts, rows=rows, refs=refs, cw=cw, diff=diff, intro=intro, figures=figures,
                answer={"method": method, "values": values, "checked": True})


def loop(name, fn, n=N):
    out, seen = [], set()
    k = 0
    while len(out) < n and k < n * 20:
        q = fn(random.Random(f"{name}-{k}"), k)
        k += 1
        key = repr(q["answer"]["values"]) + q["parts"][0]["text"]
        if key in seen:
            continue
        seen.add(key)
        out.append(q)
    return out


# ---------------------------------------------------------------- cells: magnification
CELLS = [("a cheek cell", 60), ("a palisade mesophyll cell", 80), ("a red blood cell", 7.5), ("a root hair cell", 250),
         ("a bacterium", 2.5), ("a yeast cell", 8), ("a pollen grain", 30), ("an Amoeba", 400), ("a chloroplast", 5),
         ("a mitochondrion", 2), ("a guard cell", 40), ("a white blood cell", 12), ("a sperm cell head", 5), ("a Chlorella cell", 6)]


@reg("structures.cells", "calculation")
def magnification():
    def f(r, k):
        name, um = CELLS[k % len(CELLS)]
        mag = r.choice([200, 400, 500, 1000, 1500, 2000, 2500, 4000, 5000, 8000])
        image_mm = um * mag / 1000
        if image_mm < 4 or image_mm > 150:
            mag = r.choice([m for m in (40, 100, 200, 400, 500, 1000, 2000, 5000, 10000) if 4 <= um * m / 1000 <= 150] or [1000])
            image_mm = um * mag / 1000
        image_mm = round(image_mm, 1)
        um_s = nf(um)
        mode = k % 3
        if mode == 0:
            m = image_mm * 1000 / um
            return cq(f"A drawing of {name} has a length of {nf(image_mm)} mm. The actual length of {name.split(' ', 1)[1]} is {um_s} µm.\n\nCalculate the magnification of the drawing.",
                      3, "magnification = ×", [f"converts {nf(image_mm)} mm to {nf(image_mm*1000)} µm or {um_s} µm to {nf(um/1000)} mm",
                                              f"{nf(image_mm*1000)} ÷ {um_s}"], f"×{sfig(m, 3)}",
                      ["2.2"], "4-6", {"magnification": float(sfig(m, 3))}, "magnification = image size / actual size (same units)",
                      final_note="Allow full marks for correct answer with no working; allow ecf from an incorrect unit conversion for mp2")
        if mode == 1:
            act = image_mm * 1000 / mag
            return cq(f"A photograph of {name} is magnified ×{mag}. The image of the cell is {nf(image_mm)} mm long.\n\nCalculate the actual length of the cell in micrometres (µm).",
                      3, "actual length = ", [f"{nf(image_mm)} ÷ {mag} = {sfig(image_mm/mag, 3)} mm", "× 1000 to convert to µm"],
                      f"{sfig(act, 3)} µm", ["2.2"], "4-6", {"actual_um": float(sfig(act, 3))}, "actual size = image size / magnification",
                      final_note="Allow full marks for correct answer with no working; allow ecf for conversion")
        # scale bar
        bar_um = r.choice([10, 20, 50, 100])
        bar_mm = round(bar_um * mag / 1000, 1)
        if bar_mm < 5 or bar_mm > 60:
            bar_um = max(1, round(20000 / mag / 10) * 10 or 10)
            bar_mm = round(bar_um * mag / 1000, 1)
        mg = bar_mm * 1000 / bar_um
        act = image_mm * 1000 / mg
        return cq(f"A micrograph of {name} has a scale bar labelled {bar_um} µm. The scale bar measures {nf(bar_mm)} mm on the micrograph and the image of the cell measures {nf(image_mm)} mm.\n\nCalculate the actual length of the cell.",
                  3, "actual length = ", [f"magnification = {nf(bar_mm*1000)} ÷ {bar_um} = ×{sfig(mg, 3)}", f"{nf(image_mm*1000)} ÷ {sfig(mg, 3)}"],
                  f"{sfig(act, 3)} µm", ["2.2"], "7-9", {"magnification": float(sfig(mg, 3)), "actual_um": float(sfig(act, 3))},
                  "magnification from scale bar, then actual = image / magnification")
    return loop("mag", f)


# ---------------------------------------------------------------- molecules: enzyme rates
ENZ = [("amylase", "starch", "the time taken for the starch to disappear"), ("catalase from potato", "hydrogen peroxide", "the volume of oxygen collected"),
       ("protease", "milk protein", "the time taken for the milk to turn clear"), ("lipase", "milk fat", "the time taken for the pH indicator to change colour")]


@reg("structures.molecules", "calculation")
def enzyme_rate():
    def f(r, k):
        enz, sub, dv = ENZ[k % 4]
        temps = [20, 30, 40]
        if "volume" in dv:
            vol = r.choice([12, 15, 18, 21, 24, 27, 30, 36])
            mins = r.choice([2, 3, 4, 5])
            rate = vol / mins
            if k % 2:
                vol2 = vol + r.choice([3, 6, 9, 12])
                pc = (vol2 - vol) / vol * 100
                return cq(f"A student used {enz} to break down {sub}. At {temps[0]} °C, {vol} cm³ of oxygen was collected in {mins} minutes. At {temps[1]} °C, {vol2} cm³ was collected in the same time.\n\nCalculate the percentage increase in the volume of oxygen collected.\n\nGive your answer to one decimal place.",
                          2, "percentage increase = ", [f"({vol2} − {vol}) ÷ {vol} × 100"], f"{nf(pc, dp=1)}%", ["2.12"], "4-6",
                          {"percent_increase": float(nf(pc, dp=1))}, "(new − old)/old × 100")
            return cq(f"A student used {enz} to break down {sub}. In {mins} minutes, {vol} cm³ of oxygen was collected.\n\nCalculate the mean rate of oxygen production in cm³ per minute.",
                      2, "rate = ", [f"{vol} ÷ {mins}"], f"{sfig(rate, 3)} cm³ per minute", ["2.12"], "1-3",
                      {"rate_cm3_per_min": float(sfig(rate, 3))}, "volume / time")
        t = r.choice([40, 50, 64, 80, 100, 125, 160, 200, 250])
        if k % 3 == 2:
            base = r.choice([40, 50, 60, 75, 90, 120, 150])
            ts = sorted(base + dv_ for dv_ in r.sample([-6, -4, -2, 0, 2, 4, 6], 3))  # repeats agree: no anomaly
            mn = sum(ts) / 3
            return cq(f"A student repeated an experiment with {enz} at 35 °C three times. The results for {dv} were {ts[0]} s, {ts[1]} s and {ts[2]} s.\n\nCalculate the mean rate of reaction as 1000 ÷ mean time.",
                      3, "mean rate = ", [f"mean time = {nf(mn, dp=1)} s", f"1000 ÷ {nf(mn, dp=1)}"], f"{sfig(1000/mn, 3)} s⁻¹",
                      ["2.12"], "4-6", {"mean_time_s": float(nf(mn, dp=1)), "rate": float(sfig(1000/mn, 3))}, "mean, then 1000/t",
                      final_note="Allow full marks for correct answer with no working; allow ecf for an incorrect mean")
        rate = 1000 / t
        return cq(f"A student investigated {enz} acting on {sub}. At {temps[k % 3]} °C, {dv} was {t} seconds.\n\nThe rate of reaction can be calculated as 1000 ÷ time.\n\nCalculate the rate of reaction.",
                  2, "rate = ", [f"1000 ÷ {t}"], f"{sfig(rate, 3)} s⁻¹", ["2.12"], "1-3", {"rate": float(sfig(rate, 3))}, "1000/t")
    return loop("enz", f)


# ---------------------------------------------------------------- movement: % change, SA:V
TISSUES = ["potato", "carrot", "sweet potato", "beetroot", "apple", "radish", "turnip"]


@reg("structures.movement", "calculation")
def osmosis_pc():
    def f(r, k):
        tis = TISSUES[k % len(TISSUES)]
        m0 = round(r.uniform(1.8, 4.5), 2)
        if k % 4 == 3:
            s = r.choice([0.5, 1, 1.5, 2, 2.5, 3, 4, 5])
            sa, v = 6 * s * s, s ** 3
            return cq(f"A cube of agar jelly has sides of length {nf(s)} cm.\n\nCalculate the surface area to volume ratio of the cube.\n\nGive your answer in the form n : 1",
                      3, "ratio = ", [f"surface area = 6 × {nf(s)} × {nf(s)} = {nf(sa)} cm²", f"volume = {nf(s)}³ = {nf(v)} cm³"], f"{sfig(sa/v, 3)} : 1",
                      ["2.16"], "4-6", {"surface_area": sa, "volume": v, "ratio": float(sfig(sa / v, 3))}, "SA = 6s², V = s³")
        conc = r.choice([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
        change = (0.5 - conc) * r.uniform(0.12, 0.3)
        m1 = round(m0 * (1 + change), 2)
        if m1 == m0:
            m1 = round(m0 + 0.05, 2)
        pc = (m1 - m0) / m0 * 100
        word = "increase" if pc > 0 else "decrease"
        if k % 4 == 2:
            vals = [round(pc + r.uniform(-1.5, 1.5), 1) for _ in range(3)]
            mn = sum(vals) / 3
            return cq(f"Three {tis} cylinders were placed in {nf(conc)} mol dm⁻³ sucrose solution. Their percentage changes in mass were {vals[0]}%, {vals[1]}% and {vals[2]}%.\n\nCalculate the mean percentage change in mass.\n\nGive your answer to one decimal place.",
                      2, "mean = ", [f"({vals[0]} + {vals[1]} + {vals[2]}) ÷ 3"], f"{nf(mn, dp=1)}%", ["2.17"], "1-3",
                      {"mean_percent": float(nf(mn, dp=1))}, "mean of three")
        return cq(f"{a_an(tis).capitalize()} {tis} cylinder had a mass of {m0:.2f} g. It was placed in {nf(conc)} mol dm⁻³ sucrose solution for 30 minutes. Its final mass was {m1:.2f} g.\n\nCalculate the percentage change in mass.\n\nGive your answer to one decimal place.",
                  3, "percentage change = ", [f"change in mass = {m1 - m0:+.2f} g", f"{m1 - m0:+.2f} ÷ {m0:.2f} × 100"], f"{nf(pc, dp=1)}%",
                  ["2.17"], "4-6", {"percent_change": float(nf(pc, dp=1))}, "(final − initial)/initial × 100",
                  final_note=f"Answer must show {word} (negative sign or the word {word}) for mp3; allow ecf")
    return loop("osm", f)


# ---------------------------------------------------------------- plant nutrition: bubble rates
PLANTS = ["pondweed", "Elodea", "Cabomba", "a water plant", "Egeria"]


@reg("structures.plant-nutrition", "calculation")
def bubbles():
    def f(r, k):
        pl = PLANTS[k % 5]
        d = r.choice([10, 15, 20, 25, 30, 40, 50])
        t = r.choice([2, 3, 4, 5])
        base = r.randint(20, 60)
        counts = [base + r.randint(-4, 4) for _ in range(3)]  # repeats agree closely: no anomaly
        if k % 3 == 1 and (k // 3) % 3 == 1:
            counts[2] = base * 2 + r.randint(5, 15)  # one obvious anomaly, which must be excluded
            mn = (counts[0] + counts[1]) / 2
            rate = mn / t
            return cq(f"A student counted bubbles from {pl} in {t} minutes on three occasions: {counts[0]}, {counts[1]} and {counts[2]}.\n\nOne result is anomalous. Calculate the mean rate of bubble production per minute, leaving out the anomalous result.",
                      3, "mean rate = ", [f"ignores {counts[2]} as anomalous; mean = ({counts[0]} + {counts[1]}) ÷ 2 = {nf(mn, dp=1)}", f"{nf(mn, dp=1)} ÷ {t}"],
                      f"{sfig(rate, 3)} bubbles per minute", ["2.23"], "7-9",
                      {"mean": float(nf(mn, dp=1)), "rate": float(sfig(rate, 3))}, "mean of non-anomalous results then divide by time",
                      final_note=f"The anomalous result ({counts[2]}) must be excluded from the mean; allow ecf for an incorrect mean")
        if k % 3 == 0:
            rate = counts[0] / t
            return cq(f"A student placed {pl} {d} cm from a lamp and counted {counts[0]} bubbles of gas in {t} minutes.\n\nCalculate the rate of bubble production per minute.",
                      2, "rate = ", [f"{counts[0]} ÷ {t}"], f"{sfig(rate, 3)} bubbles per minute", ["2.23"], "1-3",
                      {"rate": float(sfig(rate, 3))}, "count / time")
        if k % 3 == 1:
            mn = sum(counts) / 3
            rate = mn / t
            return cq(f"A student counted bubbles from {pl} in {t} minutes on three occasions: {counts[0]}, {counts[1]} and {counts[2]}.\n\nCalculate the mean rate of bubble production per minute.",
                      3, "mean rate = ", [f"mean = {nf(mn, dp=1)}", f"{nf(mn, dp=1)} ÷ {t}"], f"{sfig(rate, 3)} bubbles per minute", ["2.23"], "4-6",
                      {"mean": float(nf(mn, dp=1)), "rate": float(sfig(rate, 3))}, "mean then divide by time",
                      final_note="No result is anomalous, so all three are used; allow full marks for correct answer with no working; allow ecf for an incorrect mean")
        a, b = sorted(r.sample(range(12, 80), 2))
        pc = (b - a) / a * 100
        return cq(f"When the lamp was moved from {d + 20} cm to {d} cm away from {pl}, the number of bubbles per minute rose from {a} to {b}.\n\nCalculate the percentage increase.\n\nGive your answer to the nearest whole number.",
                  2, "percentage increase = ", [f"({b} − {a}) ÷ {a} × 100"], f"{nf(pc, dp=0)}%", ["2.20"], "4-6",
                  {"percent_increase": float(nf(pc, dp=0))}, "(new − old)/old × 100")
    return loop("bub", f)


# ---------------------------------------------------------------- human nutrition: energy in food
FOODS = ["a peanut", "a cashew nut", "a piece of bread", "a crisp", "a piece of popcorn", "a piece of dried pasta", "a brazil nut", "a cracker"]


@reg("structures.human-nutrition", "calculation")
def food_energy():
    def f(r, k):
        food = FOODS[k % len(FOODS)]
        if k % 3 == 2:
            meal = r.choice([1800, 2400, 2700, 3200, 3600])
            need = r.choice([8500, 9500, 10500, 11000, 12000])
            who = r.choice(["a teenage boy", "a pregnant woman", "an office worker", "a builder"])
            pc = meal / need * 100
            return cq(f"The daily energy requirement of {who} is {need} kJ. One meal provides {meal} kJ.\n\nCalculate the percentage of the daily energy requirement provided by the meal.\n\nGive your answer to one decimal place.",
                      2, "percentage = ", [f"{meal} ÷ {need} × 100"], f"{nf(pc, dp=1)}%", ["2.26"], "1-3",
                      {"percent": float(nf(pc, dp=1))}, "part/whole × 100")
        mass = round(r.uniform(0.4, 1.6), 2)
        vol = r.choice([20, 25, 30, 40, 50])
        dT = r.choice([12, 15, 18, 21, 24, 27, 30, 33])
        E = vol * 4.2 * dT
        epg = E / mass
        return cq(f"A student burned {food} of mass {mass:.2f} g under a boiling tube containing {vol} cm³ of water. The temperature of the water rose by {dT} °C.\n\nEnergy (J) = mass of water (g) × 4.2 × temperature rise (°C); 1 cm³ of water has a mass of 1 g.\n\nCalculate the energy released per gram of food in J per g.",
                  3, "energy = ", [f"{vol} × 4.2 × {dT} = {nf(E)} J", f"{nf(E)} ÷ {mass:.2f}"], f"{sfig(epg, 3)} J per g",
                  ["2.33B"], "4-6", {"energy_J": E, "energy_per_g": float(sfig(epg, 3))}, "m × 4.2 × ΔT / mass of food")
    return loop("food", f)


# ---------------------------------------------------------------- respiration: respirometer
ORGS = ["germinating peas", "woodlice", "maggots", "germinating mung beans", "crickets", "yeast beads", "germinating wheat seeds"]


@reg("structures.respiration", "calculation")
def respirometer():
    def f(r, k):
        org = ORGS[k % len(ORGS)]
        d = r.choice([12, 15, 18, 24, 27, 30, 36, 42])
        t = r.choice([3, 5, 6, 10])
        if k % 3 == 0:
            rate = d / t
            return cq(f"A respirometer containing {org} was set up. The coloured liquid in the capillary tube moved {d} mm in {t} minutes.\n\nCalculate the rate of movement of the liquid in mm per minute.",
                      2, "rate = ", [f"{d} ÷ {t}"], f"{sfig(rate, 3)} mm per minute", ["2.39"], "1-3", {"rate": float(sfig(rate, 3))}, "distance / time")
        if k % 3 == 1:
            rad = r.choice([0.5, 0.75, 1.0])
            vol = math.pi * rad * rad * d
            return cq(f"A respirometer containing {org} was set up. The liquid moved {d} mm along a capillary tube of radius {nf(rad)} mm in {t} minutes.\n\nVolume of a cylinder = πr²l\n\nCalculate the volume of oxygen absorbed per minute in mm³.",
                      3, "volume per minute = ", [f"π × {nf(rad)}² × {d} = {sfig(vol, 3)} mm³", f"{sfig(vol, 3)} ÷ {t}"], f"{sfig(vol/t, 3)} mm³ per minute",
                      ["2.39"], "7-9", {"volume_mm3": float(sfig(vol, 3)), "rate": float(sfig(vol / t, 3))}, "πr²l / t")
        a = r.randint(19, 24)
        b = a + r.choice([2, 3, 4, 5, 6])
        return cq(f"A vacuum flask containing {org} had a temperature of {a} °C at the start. After three days the temperature was {b} °C.\n\nCalculate the percentage increase in temperature.\n\nGive your answer to one decimal place.",
                  2, "percentage increase = ", [f"({b} − {a}) ÷ {a} × 100"], f"{nf((b-a)/a*100, dp=1)}%", ["2.39"], "4-6",
                  {"percent_increase": float(nf((b - a) / a * 100, dp=1))}, "(new − old)/old × 100")
    return loop("resp", f)


# ---------------------------------------------------------------- gas exchange humans
@reg("structures.gas-exchange-humans", "calculation")
def breathing():
    def f(r, k):
        name = ["Ali", "Mei", "Sam", "Priya", "Tomas", "Zara", "Kofi"][k % 7]
        if k % 3 == 0:
            n = r.randint(6, 11)
            return cq(f"{name} counted {n} breaths in 30 seconds while resting.\n\nCalculate {name}'s breathing rate in breaths per minute.",
                      1, "breathing rate = ", [], f"{n*2} breaths per minute", ["2.50"], "1-3", {"rate": n * 2}, "count × 2")
        tv = r.choice([0.4, 0.5, 0.6]) if k % 3 == 1 else r.choice([1.5, 2.0, 2.5])
        br = r.choice([12, 14, 16]) if k % 3 == 1 else r.choice([24, 28, 30, 32, 35])
        if k % 3 == 1:
            v = tv * br
            return cq(f"At rest, {name} breathes {br} times per minute and the volume of each breath is {nf(tv)} dm³.\n\nCalculate the volume of air breathed in per minute.",
                      2, "volume = ", [f"{nf(tv)} × {br}"], f"{nf(v)} dm³ per minute", ["2.50"], "4-6", {"volume": round(v, 3)}, "tidal volume × rate")
        a = r.choice([12, 14, 15, 16])
        pc = (br - a) / a * 100
        return cq(f"{name}'s breathing rate was {a} breaths per minute at rest and {br} breaths per minute after running for five minutes.\n\nCalculate the percentage increase in breathing rate.\n\nGive your answer to the nearest whole number.",
                  2, "percentage increase = ", [f"({br} − {a}) ÷ {a} × 100"], f"{nf(pc, dp=0)}%", ["2.50"], "4-6",
                  {"percent_increase": float(nf(pc, dp=0))}, "(new − old)/old × 100")
    return loop("breath", f)


# ---------------------------------------------------------------- transport plants: potometer
SHOOTS = ["a leafy shoot of privet", "a geranium shoot", "a laurel shoot", "a willow shoot", "a bean shoot", "a holly shoot"]


@reg("structures.transport-plants", "calculation")
def potometer():
    def f(r, k):
        sh = SHOOTS[k % 6]
        d = r.choice([18, 24, 30, 36, 45, 54, 60])
        t = r.choice([3, 5, 6, 10])
        if k % 3 == 0:
            return cq(f"The air bubble in a potometer fitted with {sh} moved {d} mm in {t} minutes.\n\nCalculate the rate of water uptake in mm per minute.",
                      2, "rate = ", [f"{d} ÷ {t}"], f"{sfig(d/t, 3)} mm per minute", ["2.58B"], "1-3", {"rate": float(sfig(d / t, 3))}, "distance / time")
        if k % 3 == 1:
            rad = r.choice([0.5, 0.6, 0.8, 1.0])
            vol = math.pi * rad ** 2 * d
            return cq(f"The air bubble in a potometer fitted with {sh} moved {d} mm in {t} minutes. The capillary tube has a radius of {nf(rad)} mm.\n\nVolume = πr²l\n\nCalculate the rate of water uptake in mm³ per minute.",
                      3, "rate = ", [f"π × {nf(rad)}² × {d} = {sfig(vol, 3)} mm³", f"{sfig(vol, 3)} ÷ {t}"], f"{sfig(vol/t, 3)} mm³ per minute",
                      ["2.58B"], "7-9", {"volume_mm3": float(sfig(vol, 3)), "rate": float(sfig(vol / t, 3))}, "πr²l / t")
        a = r.choice([4, 5, 6, 8])
        b = a * r.choice([1.5, 2, 2.5, 3])
        pc = (b - a) / a * 100
        return cq(f"When a fan was switched on, the rate of water uptake by {sh} rose from {a} mm per minute to {nf(b)} mm per minute.\n\nCalculate the percentage increase in the rate of water uptake.",
                  2, "percentage increase = ", [f"({nf(b)} − {a}) ÷ {a} × 100"], f"{nf(pc)}%", ["2.57B"], "4-6", {"percent_increase": round(pc, 2)}, "(new − old)/old × 100")
    return loop("pot", f)


# ---------------------------------------------------------------- heart
@reg("structures.heart", "calculation")
def heart_rate():
    def f(r, k):
        name = ["An athlete", "A student", "A teacher", "A swimmer", "A cyclist"][k % 5]
        if k % 3 == 0:
            n = r.randint(16, 24)
            return cq(f"{name} counted {n} pulse beats in 15 seconds.\n\nCalculate the heart rate in beats per minute.",
                      1, "heart rate = ", [], f"{n*4} beats per minute", ["2.66"], "1-3", {"rate": n * 4}, "count × 4")
        a = r.choice([60, 64, 68, 70, 72, 75, 80])
        b = r.choice([110, 120, 132, 140, 150, 160, 168])
        if k % 3 == 1:
            pc = (b - a) / a * 100
            return cq(f"{name} has a resting heart rate of {a} beats per minute. During exercise the heart rate rises to {b} beats per minute.\n\nCalculate the percentage increase in heart rate.\n\nGive your answer to the nearest whole number.",
                      2, "percentage increase = ", [f"({b} − {a}) ÷ {a} × 100"], f"{nf(pc, dp=0)}%", ["2.66"], "4-6",
                      {"percent_increase": float(nf(pc, dp=0))}, "(new − old)/old × 100")
        sv = r.choice([70, 75, 80, 90, 100, 110])
        co = sv * b / 1000
        return cq(f"During exercise, {name.lower()}'s heart rate is {b} beats per minute and each beat pumps {sv} cm³ of blood.\n\nCalculate the volume of blood pumped per minute in dm³.",
                  2, "volume = ", [f"{sv} × {b} = {sv*b} cm³"], f"{nf(co)} dm³ per minute", ["2.66"], "4-6", {"cardiac_output_dm3": co},
                  "stroke volume × heart rate ÷ 1000")
    return loop("hr", f)


# ---------------------------------------------------------------- excretion
@reg("structures.excretion", "calculation")
def kidney():
    def f(r, k):
        if k % 2 == 0:
            filt = r.choice([150, 160, 170, 180, 190])
            urine = r.choice([1.2, 1.5, 1.8, 2.0, 2.4, 3.0])
            pc = (filt - urine) / filt * 100
            return cq(f"The kidneys of a person produce {filt} dm³ of glomerular filtrate in a day but only {nf(urine)} dm³ of urine.\n\nCalculate the percentage of the filtrate that is reabsorbed.\n\nGive your answer to one decimal place.",
                      2, "percentage reabsorbed = ", [f"({filt} − {nf(urine)}) ÷ {filt} × 100"], f"{nf(pc, dp=1)}%", ["2.76B"], "4-6",
                      {"percent": float(nf(pc, dp=1))}, "(filtrate − urine)/filtrate × 100")
        p = r.choice([0.2, 0.25, 0.3, 0.4])
        u = r.choice([15, 18, 20, 24, 30])
        return cq(f"The concentration of urea is {nf(p)} g per dm³ in blood plasma and {u} g per dm³ in urine.\n\nCalculate how many times more concentrated urea is in urine than in plasma.",
                  2, "", [f"{u} ÷ {nf(p)}"], f"{nf(u/p)} times", ["2.79B"], "4-6", {"ratio": round(u / p, 3)}, "urine / plasma")
    return loop("kid", f)


# ---------------------------------------------------------------- dna
@reg("reproduction.dna", "calculation")
def bases():
    def f(r, k):
        b = ["adenine", "thymine", "guanine", "cytosine"][k % 4]
        pair = {"adenine": "thymine", "thymine": "adenine", "guanine": "cytosine", "cytosine": "guanine"}[b]
        other = {"adenine": "guanine", "thymine": "cytosine", "guanine": "adenine", "cytosine": "thymine"}[b]
        if k % 3 == 2:
            aa = r.choice([120, 146, 210, 300, 333, 451])
            return cq(f"A protein is made of {aa} amino acids.\n\nCalculate the minimum number of bases in the mRNA that codes for this protein.",
                      1, "number of bases = ", [], f"{aa*3}", ["3.18B"], "4-6", {"bases": aa * 3}, "3 bases per amino acid",
                      final_note="Ignore extra bases for a stop codon")
        x = r.choice([12, 15, 18, 21, 22, 27, 28, 31, 34])
        o = (100 - 2 * x) / 2
        return cq(f"In a sample of DNA, {x}% of the bases are {b}.\n\nCalculate the percentage of bases that are {other}.",
                  2, "percentage = ", [f"{pair} = {x}% so {b} + {pair} = {2*x}%"], f"{nf(o)}%", ["3.16B"], "7-9",
                  {"percent_other": o}, "base pairing rules: A=T, C=G")
    return loop("dna", f)


# ---------------------------------------------------------------- evolution: bacterial growth
@reg("reproduction.evolution", "calculation")
def bacteria():
    def f(r, k):
        g = r.choice([20, 30, 40, 60])
        h = r.choice([2, 3, 4, 5, 6])
        n0 = r.choice([1, 10, 50, 100, 200])
        if k % 2 == 0:
            gens = h * 60 // g
            n = n0 * 2 ** gens
            return cq(f"A population of {n0} antibiotic-resistant bacteria divides once every {g} minutes.\n\nCalculate the number of bacteria after {h} hours.\n\nGive your answer in standard form.",
                      3, "number = ", [f"number of divisions = {h} × 60 ÷ {g} = {gens}", f"{n0} × 2^{gens}"], f"{sfig(n, 3)} ({n:.2e})".replace("e+", " × 10^"),
                      ["3.39"], "7-9", {"divisions": gens, "number": n}, "N = N0 × 2^n")
        tot = r.choice([400, 500, 800, 1000, 1250])
        res = r.randint(8, 60) * (tot // 100)
        pc = res / tot * 100
        return cq(f"After treatment with an antibiotic, {res} of the {tot} bacteria tested in a sample were resistant.\n\nCalculate the percentage of resistant bacteria.",
                  2, "percentage = ", [f"{res} ÷ {tot} × 100"], f"{nf(pc)}%", ["3.39"], "1-3", {"percent": round(pc, 3)}, "part/whole × 100")
    return loop("bact", f)


# ---------------------------------------------------------------- environment: quadrat estimates
SPECIES = ["daisies", "dandelions", "buttercups", "clover plants", "plantains", "limpets", "barnacles", "thistles"]


@reg("ecology.environment", "calculation")
def quadrats():
    def f(r, k):
        sp = SPECIES[k % len(SPECIES)]
        q = r.choice([0.25, 0.5, 1.0])
        counts = [r.randint(0, 14) for _ in range(r.choice([5, 6, 8]))]
        mn = sum(counts) / len(counts)
        L, W = r.choice([(20, 15), (30, 25), (40, 20), (50, 30), (25, 12), (60, 40)])
        area = L * W
        est = mn / q * area
        qa = "0.25 m² (50 cm × 50 cm)" if q == 0.25 else ("0.5 m²" if q == 0.5 else "1 m²")
        tbl = table_fig(["Quadrat"] + [str(i + 1) for i in range(len(counts))], [[f"Number of {sp}"] + counts])
        return cq(f"A student placed {len(counts)} quadrats of area {qa} at random in a field measuring {L} m by {W} m. The table shows the number of {sp} in each quadrat.\n\nEstimate the population of {sp} in the field.",
                  3, "estimated population = ", [f"mean = {nf(mn, dp=2)} per quadrat", f"field area = {area} m² so {nf(mn, dp=2)} × {area} ÷ {nf(q)}"],
                  f"{round(est)}", ["4.2"], "4-6", {"mean": round(mn, 4), "estimate": round(est)}, "mean per quadrat × field area / quadrat area",
                  figures=[tbl], final_note="Allow full marks for correct answer with no working; allow ecf from incorrect mean; accept answers rounded to 2 s.f.")
    return loop("quad", f)


# ---------------------------------------------------------------- feeding: energy efficiency
CHAINS = [("grass", "grasshoppers", "frogs"), ("phytoplankton", "zooplankton", "small fish"), ("oak leaves", "caterpillars", "blue tits"),
          ("maize", "cattle", "humans"), ("seaweed", "periwinkles", "crabs"), ("algae", "mayfly larvae", "trout")]


@reg("ecology.feeding", "calculation")
def efficiency():
    def f(r, k):
        a, b, c = CHAINS[k % len(CHAINS)]
        e1 = r.choice([12000, 15000, 18000, 20000, 24000, 30000, 45000])
        pc1 = r.choice([8, 9, 10, 11, 12, 15])
        e2 = e1 * pc1 // 100
        if k % 2 == 0:
            eff = e2 / e1 * 100
            return cq(f"In a food chain, {a} contain {e1} kJ per m² per year and {b} contain {e2} kJ per m² per year.\n\nCalculate the efficiency of energy transfer from {a} to {b}.",
                      2, "efficiency = ", [f"{e2} ÷ {e1} × 100"], f"{nf(eff)}%", ["4.9"], "4-6", {"efficiency": eff}, "energy out / energy in × 100")
        e3 = round(e2 * r.choice([0.08, 0.1, 0.12, 0.15]))
        lost = e2 - e3
        return cq(f"{cap_(b)} take in {e2} kJ per m² per year. Only {e3} kJ per m² per year is passed on to {c}.\n\nCalculate the percentage of energy taken in by the {b} that is NOT passed on to {c}.\n\nGive your answer to one decimal place.",
                  3, "percentage = ", [f"energy not passed on = {e2} − {e3} = {lost} kJ", f"{lost} ÷ {e2} × 100"], f"{nf(lost/e2*100, dp=1)}%",
                  ["4.9"], "7-9", {"lost": lost, "percent_lost": float(nf(lost / e2 * 100, dp=1))}, "(in − out)/in × 100")
    return loop("eff", f)


def cap_(s):
    return s[:1].upper() + s[1:]


# ---------------------------------------------------------------- human impact
@reg("ecology.human-impact", "calculation")
def co2_change():
    def f(r, k):
        y1 = r.choice([1960, 1970, 1980, 1990])
        y2 = y1 + r.choice([20, 25, 30, 40])
        c1 = round(316 + (y1 - 1960) * 1.3 + r.uniform(-2, 2))
        c2 = round(c1 + (y2 - y1) * r.uniform(1.5, 2.2))
        if k % 3 == 0:
            pc = (c2 - c1) / c1 * 100
            return cq(f"The mean concentration of carbon dioxide in the atmosphere was {c1} parts per million (ppm) in {y1} and {c2} ppm in {y2}.\n\nCalculate the percentage increase.\n\nGive your answer to one decimal place.",
                      2, "percentage increase = ", [f"({c2} − {c1}) ÷ {c1} × 100"], f"{nf(pc, dp=1)}%", ["4.14"], "4-6",
                      {"percent_increase": float(nf(pc, dp=1))}, "(new − old)/old × 100")
        if k % 3 == 1:
            rate = (c2 - c1) / (y2 - y1)
            return cq(f"The carbon dioxide concentration in the atmosphere rose from {c1} ppm in {y1} to {c2} ppm in {y2}.\n\nCalculate the mean rate of increase in ppm per year.",
                      2, "rate = ", [f"({c2} − {c1}) ÷ ({y2} − {y1})"], f"{sfig(rate, 3)} ppm per year", ["4.14"], "4-6",
                      {"rate": float(sfig(rate, 3))}, "change / time")
        o1 = r.choice([8.5, 9.0, 9.5, 10.0])
        o2 = round(o1 * r.uniform(0.2, 0.6), 1)
        pc = (o1 - o2) / o1 * 100
        return cq(f"The oxygen concentration in a lake fell from {nf(o1)} mg per dm³ to {nf(o2)} mg per dm³ after an algal bloom.\n\nCalculate the percentage decrease in oxygen concentration.\n\nGive your answer to the nearest whole number.",
                  2, "percentage decrease = ", [f"({nf(o1)} − {nf(o2)}) ÷ {nf(o1)} × 100"], f"{nf(pc, dp=0)}%", ["4.17"], "4-6",
                  {"percent_decrease": float(nf(pc, dp=0))}, "(old − new)/old × 100")
    return loop("co2", f)


# ---------------------------------------------------------------- crops
CROPS = ["tomatoes", "lettuces", "cucumbers", "peppers", "strawberries", "wheat", "maize"]


@reg("resources.crops", "calculation")
def crop_yield():
    def f(r, k):
        c = CROPS[k % len(CROPS)]
        y1 = r.choice([24, 30, 36, 40, 45, 52, 60])
        y2 = round(y1 * r.uniform(1.1, 1.6))
        cond = ["with extra carbon dioxide", "with fertiliser", "in a heated glasshouse", "in a polythene tunnel", "with biological pest control"][k % 5]
        ref = {"with extra carbon dioxide": "5.2", "with fertiliser": "5.3", "in a heated glasshouse": "5.2", "in a polythene tunnel": "5.1",
               "with biological pest control": "5.4"}[cond]
        if k % 3 == 2:
            area = r.choice([0.5, 2, 2.5, 4, 5])
            tot = round(y2 * area * 10) / 10
            return cq(f"A farmer harvested {nf(tot)} tonnes of {c} grown {cond} from a field of {nf(area)} hectares.\n\nCalculate the yield in tonnes per hectare.",
                      2, "yield = ", [f"{nf(tot)} ÷ {nf(area)}"], f"{sfig(tot/area, 3)} tonnes per hectare", [ref], "1-3",
                      {"yield": float(sfig(tot / area, 3))}, "total / area")
        pc = (y2 - y1) / y1 * 100
        return cq(f"The yield of {c} was {y1} kg per m² without treatment and {y2} kg per m² when grown {cond}.\n\nCalculate the percentage increase in yield.\n\nGive your answer to one decimal place.",
                  2, "percentage increase = ", [f"({y2} − {y1}) ÷ {y1} × 100"], f"{nf(pc, dp=1)}%", [ref], "4-6",
                  {"percent_increase": float(nf(pc, dp=1))}, "(new − old)/old × 100")
    return loop("crop", f)


# ---------------------------------------------------------------- microorganisms
@reg("resources.microorganisms", "calculation")
def yeast_rate():
    def f(r, k):
        if k % 3 == 0:
            v = r.choice([6.0, 7.5, 9.0, 12.0, 13.5, 15.0, 18.0])
            t = r.choice([5, 10, 15, 20])
            temp = r.choice([25, 30, 35, 40])
            return cq(f"Yeast in sugar solution at {temp} °C produced {nf(v)} cm³ of carbon dioxide in {t} minutes.\n\nCalculate the rate of carbon dioxide production in cm³ per minute.",
                      2, "rate = ", [f"{nf(v)} ÷ {t}"], f"{sfig(v/t, 3)} cm³ per minute", ["5.6"], "1-3", {"rate": float(sfig(v / t, 3))}, "volume / time")
        if k % 3 == 1:
            g = r.choice([20, 30, 40])
            h = r.choice([2, 3, 4])
            n0 = r.choice([100, 500, 1000, 5000])
            gens = h * 60 // g
            n = n0 * 2 ** gens
            return cq(f"A fermenter is started with {n0} bacteria per cm³. The bacteria divide every {g} minutes.\n\nCalculate the number of bacteria per cm³ after {h} hours.",
                      3, "number = ", [f"{gens} divisions", f"{n0} × 2^{gens}"], f"{n}", ["5.8"], "7-9", {"divisions": gens, "number": n}, "N0 × 2^n",
                      final_note="Accept answer in standard form")
        b1 = r.randint(8, 20)
        b2 = b1 + r.randint(5, 25)
        pc = (b2 - b1) / b1 * 100
        return cq(f"Yeast produced {b1} bubbles per minute in 5% sugar solution and {b2} bubbles per minute in 10% sugar solution.\n\nCalculate the percentage increase in the rate of bubble production.\n\nGive your answer to the nearest whole number.",
                  2, "percentage increase = ", [f"({b2} − {b1}) ÷ {b1} × 100"], f"{nf(pc, dp=0)}%", ["5.6"], "4-6",
                  {"percent_increase": float(nf(pc, dp=0))}, "(new − old)/old × 100")
    return loop("yeast", f)
