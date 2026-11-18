"""Data / graph analysis templates.

Each dataset has a fixed shape (rise, fall, peak, dip, rise_plateau, fall_level) and base values that are
scaled per question, so the describe-trend mark points always match the data shown.
Kinds: graph + describe + explain; table + plot (space "graph") + describe; table + % change + explain;
graph + read-off + rate of change + explain.
"""
import math
import random
from collections import namedtuple

from biology_lib import (reg, text_part, calc_part, row_, points_row, table_fig, svg_fig, line_graph, graph_ms,
                         nf, sfig)

DS = namedtuple("DS", "ref intro xname xunit yname yunit xs ys shape explain_q explain dp")


def ds(ref, intro, xname, xunit, yname, yunit, xs, ys, shape, explain_q, explain, dp=1):
    return DS(ref, intro, xname, xunit, yname, yunit, xs, ys, shape, explain_q, explain, dp)


DATA = {
    "structures.molecules": [
        ds("2.11", "A student measured the rate of an enzyme-controlled reaction at different temperatures.", "temperature", "°C",
           "rate of reaction", "arbitrary units", [10, 20, 30, 40, 50, 60, 70], [8, 18, 34, 52, 30, 6, 0], "peak",
           "Explain the results shown.",
           ["as temperature rises, molecules have more kinetic energy", "more collisions between enzyme and substrate / more enzyme–substrate complexes",
            "above the optimum the enzyme is denatured", "the shape of the active site changes", "substrate no longer fits the active site"]),
        ds("2.13", "A student investigated how pH affects the activity of an enzyme from the small intestine.", "pH", "",
           "volume of product formed in five minutes", "cm³", [4, 5, 6, 7, 8, 9, 10], [2, 6, 13, 21, 25, 14, 4], "peak",
           "Explain why the enzyme is less active at pH 4 than at pH 8.",
           ["pH 8 is the optimum pH", "at pH 4 the active site changes shape / the enzyme is denatured", "substrate cannot fit / bind to the active site",
            "fewer enzyme–substrate complexes form"]),
    ],
    "structures.movement": [
        ds("2.17", "Potato cylinders were placed in sucrose solutions of different concentration for 30 minutes and their percentage change in mass was calculated.",
           "concentration of sucrose", "mol dm⁻³", "percentage change in mass", "%", [0.0, 0.2, 0.4, 0.6, 0.8, 1.0], [18, 9, 1, -7, -14, -18], "fall",
           "Explain the results for the cylinders in 0.0 and 1.0 mol dm⁻³ sucrose solution.",
           ["in 0.0 mol dm⁻³ water moves into the cells", "by osmosis", "from a dilute solution to a more concentrated solution / down a water concentration gradient",
            "through a partially permeable membrane", "in 1.0 mol dm⁻³ water moves out of the cells", "so the mass decreases"]),
        ds("2.16", "Agar cubes of different size were placed in acid and the time for the indicator inside each cube to change colour was recorded.",
           "length of side of cube", "cm", "time for colour to change", "s", [0.5, 1.0, 1.5, 2.0, 2.5], [40, 110, 230, 390, 600], "rise",
           "Explain why the time taken increases as the size of the cube increases.",
           ["larger cubes have a smaller surface area to volume ratio", "acid has further to diffuse to reach the centre", "less surface for diffusion relative to volume",
            "diffusion is slower over longer distances"], dp=0),
    ],
    "structures.plant-nutrition": [
        ds("2.20", "The rate of photosynthesis of a water plant was measured at different light intensities.", "light intensity", "arbitrary units",
           "rate of photosynthesis", "bubbles per minute", [0, 10, 20, 30, 40, 50, 60], [0, 14, 27, 36, 40, 41, 41], "rise_plateau",
           "Explain the shape of the graph.",
           ["at low light intensity, light is the limiting factor", "more light gives more energy for photosynthesis", "at high light intensity another factor limits the rate",
            "such as carbon dioxide concentration or temperature", "chlorophyll / enzymes are working at the maximum rate"], dp=0),
        ds("2.20", "The rate of photosynthesis of a crop plant was measured at different temperatures, with light and carbon dioxide kept high.", "temperature", "°C",
           "rate of carbon dioxide uptake", "arbitrary units", [5, 10, 15, 20, 25, 30, 35, 40], [4, 9, 16, 24, 30, 33, 22, 8], "peak",
           "Explain the results above 30 °C.",
           ["photosynthesis is controlled by enzymes", "enzymes are denatured at high temperature", "active site changes shape", "fewer enzyme–substrate complexes"], dp=0),
    ],
    "structures.human-nutrition": [
        ds("2.29", "Amylase was added to starch solution at 37 °C and the concentration of starch remaining was measured every two minutes.", "time", "minutes",
           "concentration of starch", "g per dm³", [0, 2, 4, 6, 8, 10, 12], [10.0, 6.8, 4.4, 2.6, 1.4, 0.6, 0.6], "fall_level",
           "Explain the change in starch concentration.",
           ["amylase breaks down / digests starch", "into maltose", "the rate slows as less starch is left / fewer substrate collisions", "all starch is used up / reaction stops"]),
        ds("2.26", "The table shows the mean daily energy requirement of males of different ages.", "age", "years",
           "daily energy requirement", "kJ", [2, 6, 10, 14, 18, 30], [4800, 7200, 8800, 11000, 12000, 11500], "peak",
           "Explain why energy requirement increases between age 2 and 14.",
           ["growth requires energy", "body mass / size increases so more respiration", "more physical activity", "more cells to maintain"], dp=0),
    ],
    "structures.respiration": [
        ds("2.39", "Germinating peas were put in a vacuum flask and the temperature was recorded every day.", "time", "days",
           "temperature", "°C", [0, 1, 2, 3, 4, 5], [20, 22, 24, 26, 28, 30], "rise",
           "Explain why the temperature rose.",
           ["the peas are respiring", "respiration releases energy", "some energy is released as heat", "the vacuum flask reduces heat loss"], dp=0),
        ds("2.39", "The distance moved by a liquid drop in a respirometer containing maggots was measured at different temperatures.", "temperature", "°C",
           "distance moved in five minutes", "mm", [10, 15, 20, 25, 30, 35], [6, 10, 15, 21, 28, 34], "rise",
           "Explain why the liquid drop moved further at higher temperatures.",
           ["rate of respiration increases", "enzymes have more kinetic energy / more collisions", "more oxygen is taken in", "carbon dioxide is absorbed by soda lime",
            "so pressure in the tube falls more quickly"], dp=0),
    ],
    "structures.gas-exchange-plants": [
        ds("2.44B", "The net uptake of carbon dioxide by a leaf was measured at different light intensities. A negative value means carbon dioxide is released.",
           "light intensity", "arbitrary units", "net carbon dioxide uptake", "arbitrary units", [0, 10, 20, 30, 40, 50, 60], [-6, -1, 5, 11, 15, 17, 17], "rise_plateau",
           "Explain why the value is negative at a light intensity of 0.",
           ["no photosynthesis in the dark", "the leaf still respires", "respiration releases carbon dioxide", "so more carbon dioxide is released than taken in"], dp=0),
    ],
    "structures.gas-exchange-humans": [
        ds("2.50", "A student's breathing rate was measured before, during and after five minutes of running.", "time", "minutes",
           "breathing rate", "breaths per minute", [0, 2, 4, 6, 8, 10, 12], [14, 22, 30, 32, 22, 16, 14], "peak",
           "Explain why the breathing rate increased during exercise.",
           ["muscles respire faster", "need more oxygen", "more carbon dioxide must be removed", "faster breathing increases gas exchange in alveoli",
            "carbon dioxide concentration in blood rises"], dp=0),
        ds("2.49", "The graph shows the number of deaths from lung cancer for groups of men who smoked different numbers of cigarettes per day.",
           "number of cigarettes smoked per day", "", "deaths from lung cancer per 100 000 men per year", "", [0, 5, 10, 15, 20, 25, 30, 35],
           [10, 50, 95, 140, 190, 240, 285, 330], "rise",
           "Explain how smoking increases the risk of lung cancer.",
           ["tobacco smoke contains tar", "tar contains carcinogens", "carcinogens cause mutations in DNA", "cells divide uncontrollably / form a tumour"], dp=0),
    ],
    "structures.transport-plants": [
        ds("2.57B", "The rate of water uptake by a leafy shoot was measured with a potometer at different wind speeds.", "wind speed", "m per s",
           "rate of water uptake", "mm per minute", [0, 1, 2, 3, 4, 5], [4, 9, 13, 16, 17, 17], "rise_plateau",
           "Explain why the rate increases as wind speed increases from 0 to 3 m per s.",
           ["wind removes water vapour from around the leaf", "increases the concentration gradient", "more evaporation / diffusion of water vapour out of stomata",
            "more water is drawn up the xylem"], dp=0),
        ds("2.57B", "The rate of transpiration of a plant was measured at different humidities.", "relative humidity", "%",
           "rate of transpiration", "arbitrary units", [20, 30, 40, 50, 60, 70, 80, 90], [36, 32, 27, 22, 17, 12, 8, 4], "fall",
           "Explain the effect of humidity on the rate of transpiration.",
           ["higher humidity means more water vapour in the air", "smaller concentration gradient", "less diffusion of water vapour out of the stomata",
            "so less evaporation"], dp=0),
    ],
    "structures.blood": [
        ds("2.63B", "The concentration of antibody in a person's blood was measured after a vaccination.", "time after vaccination", "days",
           "antibody concentration", "arbitrary units", [0, 5, 10, 15, 20, 25, 30, 35], [0, 2, 10, 18, 14, 8, 5, 4], "peak",
           "Explain the changes in antibody concentration.",
           ["vaccine contains antigens", "lymphocytes recognise the antigen", "lymphocytes produce antibodies", "antibodies are specific",
            "antibodies are broken down / no longer needed", "memory cells remain"], dp=0),
        ds("2.62", "The number of white blood cells in a patient's blood was measured during an infection.", "time", "days",
           "white blood cells", "thousands per mm³", [0, 1, 2, 3, 4, 5, 6], [7, 9, 13, 16, 14, 10, 8], "peak",
           "Explain why the number of white blood cells increased.",
           ["pathogens enter the body", "phagocytes engulf and digest pathogens", "lymphocytes produce antibodies", "more white blood cells are made to fight the infection"], dp=0),
    ],
    "structures.heart": [
        ds("2.66", "The heart rate of an athlete was measured at different running speeds.", "running speed", "km per hour",
           "heart rate", "beats per minute", [0, 4, 8, 12, 16, 20], [62, 85, 108, 132, 156, 178], "rise",
           "Explain why heart rate increases as running speed increases.",
           ["muscles respire faster", "need more oxygen and glucose", "more carbon dioxide to remove", "blood is pumped faster to the muscles"], dp=0),
        ds("2.67", "The graph shows the risk of coronary heart disease in groups of people with different blood cholesterol.", "blood cholesterol", "mmol per dm³",
           "relative risk of coronary heart disease", "", [4, 5, 6, 7, 8, 9], [1.0, 1.4, 2.0, 2.9, 4.0, 5.3], "rise",
           "Explain how a high cholesterol level can lead to a heart attack.",
           ["fatty deposits build up in coronary arteries", "arteries become narrower", "less blood / oxygen reaches heart muscle", "heart muscle cannot respire / dies",
            "blood clot may block the artery"]),
    ],
    "structures.excretion": [
        ds("2.78B", "A person drank different volumes of water and the volume of urine produced in the next two hours was measured.", "volume of water drunk", "cm³",
           "volume of urine produced", "cm³", [0, 250, 500, 750, 1000, 1250], [60, 190, 380, 560, 760, 950], "rise",
           "Explain why more urine is produced when more water is drunk.",
           ["water content of blood increases", "detected by the brain / hypothalamus", "less ADH released by the pituitary gland", "collecting duct becomes less permeable",
            "less water reabsorbed", "so more dilute urine"], dp=0),
        ds("2.77B", "The concentration of glucose was measured at different points along a nephron.", "distance along nephron", "arbitrary units",
           "glucose concentration", "g per dm³", [0, 1, 2, 3, 4, 5, 6], [1.0, 1.0, 0.6, 0.2, 0.0, 0.0, 0.0], "fall_level",
           "Explain the change in glucose concentration.",
           ["glucose is filtered into the Bowman's capsule", "glucose is reabsorbed in the proximal convoluted tubule", "by active transport / selective reabsorption",
            "so no glucose is in the urine"]),
    ],
    "structures.plant-responses": [
        ds("2.85", "Shoot tips were treated with different concentrations of auxin and the curvature was measured.", "auxin concentration", "parts per million",
           "angle of curvature", "degrees", [0, 0.1, 0.2, 0.3, 0.4, 0.5], [0, 8, 15, 20, 14, 6], "peak",
           "Explain how auxin causes the shoot to bend.",
           ["auxin moves to one side of the shoot", "auxin causes cell elongation", "cells on that side grow longer", "so the shoot curves"], dp=0),
        ds("2.84", "Seedlings were grown with light from one side and the angle of bending towards the light was measured each day.", "time", "days",
           "angle of bending", "degrees", [0, 1, 2, 3, 4, 5], [0, 12, 26, 38, 44, 45], "rise_plateau",
           "Explain why the seedlings bend towards the light.",
           ["auxin moves to the shaded side", "cells on the shaded side elongate more", "positive phototropism", "more light for photosynthesis"], dp=0),
    ],
    "structures.nervous": [
        ds("2.92", "The diameter of a person's pupil was measured at different light intensities.", "light intensity", "arbitrary units",
           "pupil diameter", "mm", [0, 10, 20, 30, 40, 50, 60], [7.6, 6.2, 4.8, 3.8, 3.0, 2.6, 2.5], "fall_level",
           "Explain how the eye causes the change in pupil diameter.",
           ["light detected by the retina / receptors", "reflex action", "circular muscles of the iris contract", "radial muscles relax", "less light enters the eye",
            "protects the retina from damage"]),
        ds("2.88", "A student measured her reaction time in eight trials using a computer test.", "trial number", "",
           "reaction time", "ms", [1, 2, 3, 4, 5, 6, 7, 8], [420, 360, 320, 290, 275, 270, 268, 266], "fall_level",
           "Suggest why the reaction time decreased over the first few trials.",
           ["the student learned / practised the task", "anticipates the signal", "the brain became familiar with the task", "improved concentration / attention"], dp=0),
    ],
    "structures.homeostasis": [
        ds("2.94", "The concentration of glucose in a person's blood was measured after a meal.", "time after meal", "minutes",
           "blood glucose concentration", "mg per 100 cm³", [0, 30, 60, 90, 120, 150, 180], [90, 140, 125, 105, 92, 90, 90], "peak",
           "Explain the changes in blood glucose concentration after 30 minutes.",
           ["glucose detected by the pancreas", "insulin is released", "insulin causes liver and muscles to take in glucose", "glucose converted to glycogen",
            "blood glucose returns to normal"], dp=0),
        ds("2.93", "The rate of sweating of a person was measured at different air temperatures.", "air temperature", "°C",
           "rate of sweating", "cm³ per hour", [20, 25, 30, 35, 40, 45], [20, 60, 150, 300, 480, 640], "rise",
           "Explain how sweating helps to control body temperature.",
           ["sweat is secreted onto the skin", "water evaporates", "evaporation uses heat energy from the skin", "so the body is cooled"], dp=0),
    ],
    "reproduction.plant-reproduction": [
        ds("3.5", "Seeds were kept at different temperatures and the percentage that germinated in five days was recorded.", "temperature", "°C",
           "seeds germinated", "%", [5, 10, 15, 20, 25, 30, 35, 40], [4, 22, 58, 82, 90, 76, 40, 8], "peak",
           "Explain the results.",
           ["germination needs enzymes", "enzymes break down stored food", "low temperature: little kinetic energy / few collisions", "high temperature: enzymes are denatured",
            "optimum around 25 °C"], dp=0),
        ds("3.6", "The dry mass of germinating seeds was measured each day after they were planted in the dark.", "time", "days",
           "dry mass", "g", [0, 2, 4, 6, 8, 10], [4.0, 3.7, 3.3, 3.0, 2.8, 2.7], "fall_level",
           "Explain why the dry mass decreased.",
           ["seeds use stored food", "for respiration", "carbon dioxide released", "cannot photosynthesise in the dark / no leaves yet"]),
    ],
    "reproduction.human-reproduction": [
        ds("3.9", "The concentration of progesterone in a woman's blood was measured during one menstrual cycle.", "day of cycle", "",
           "progesterone concentration", "arbitrary units", [1, 5, 9, 13, 17, 21, 25, 28], [2, 2, 3, 4, 12, 20, 9, 3], "peak",
           "Explain the change in progesterone concentration after day 21.",
           ["no pregnancy / no fertilisation", "corpus luteum breaks down", "progesterone falls", "uterus lining is no longer maintained", "lining breaks down / menstruation"], dp=0),
    ],
    "reproduction.division-variation": [
        ds("3.37B", "Bacteria were exposed to different doses of ultraviolet radiation and the number of mutant colonies was counted.", "dose of radiation", "arbitrary units",
           "number of mutant colonies", "", [0, 10, 20, 30, 40, 50], [2, 10, 19, 31, 40, 52], "rise",
           "Explain the results.",
           ["radiation damages DNA", "changes the base sequence", "increases mutation rate", "more dose means more damage"], dp=0),
        ds("3.33", "The heights of plants of the same variety grown in soil with different amounts of nitrate were measured.", "nitrate added", "g per m²",
           "mean height", "cm", [0, 10, 20, 30, 40, 50], [24, 36, 46, 52, 54, 54], "rise_plateau",
           "Explain what these results show about the cause of variation in height.",
           ["plants are genetically similar / same variety", "so variation is caused by the environment", "nitrate needed for amino acids / proteins", "for growth"], dp=0),
    ],
    "reproduction.evolution": [
        ds("3.39", "The percentage of bacteria in a hospital that were resistant to an antibiotic was recorded over several years.", "years since antibiotic first used", "",
           "resistant bacteria", "%", [0, 2, 4, 6, 8, 10, 12], [1, 4, 12, 26, 40, 48, 50], "rise_plateau",
           "Explain why the percentage of resistant bacteria increased.",
           ["a mutation gives resistance", "antibiotic kills non-resistant bacteria", "resistant bacteria survive", "resistant bacteria reproduce", "pass on the resistance allele / gene",
            "natural selection"], dp=0),
    ],
    "ecology.environment": [
        ds("4.5", "Quadrats were placed at different distances from a large tree and the number of grass plants was counted.", "distance from tree", "m",
           "mean number of grass plants per quadrat", "", [0, 2, 4, 6, 8, 10], [3, 7, 14, 22, 26, 27], "rise_plateau",
           "Explain why there are fewer grass plants close to the tree.",
           ["tree shades the ground / less light", "less photosynthesis", "competition for water / mineral ions with tree roots", "less growth"], dp=0),
        ds("4.5", "The number of limpets per quadrat was counted at different heights above low tide on a rocky shore.", "height above low tide", "m",
           "mean number of limpets per quadrat", "", [0, 1, 2, 3, 4, 5], [28, 24, 18, 11, 5, 1], "fall",
           "Suggest why there are fewer limpets further up the shore.",
           ["covered by sea for less time", "limpets dry out", "higher temperature / more exposure", "less time to feed"], dp=0),
    ],
    "ecology.feeding": [
        ds("4.9", "The energy at each trophic level of a food chain was measured.", "trophic level", "",
           "energy", "kJ per m² per year", [1, 2, 3, 4], [24000, 2400, 260, 25], "fall",
           "Explain why energy decreases at each trophic level.",
           ["energy lost in respiration", "lost as heat", "not all of the organism is eaten", "energy lost in faeces / not digested", "lost in excretion"], dp=0),
        ds("4.8", "The population of aphids on a crop was counted each week after ladybirds were released.", "time after release", "weeks",
           "number of aphids", "", [0, 1, 2, 3, 4, 5, 6], [800, 620, 420, 260, 160, 120, 110], "fall_level",
           "Explain the change in aphid population.",
           ["ladybirds eat aphids / predators", "aphid deaths exceed births", "fewer aphids so harder for ladybirds to find food", "ladybird numbers fall, so fewer aphids are eaten / predator and prey numbers balance"], dp=0),
    ],
    "ecology.human-impact": [
        ds("4.14", "The mean concentration of carbon dioxide in the atmosphere was measured at a research station.", "year", "",
           "carbon dioxide concentration", "ppm", [1960, 1970, 1980, 1990, 2000, 2010, 2020], [317, 326, 339, 354, 369, 390, 413], "rise",
           "Explain why carbon dioxide concentration has increased.",
           ["burning fossil fuels", "deforestation", "fewer trees to absorb carbon dioxide by photosynthesis", "increased population / industry"], dp=0),
        ds("4.16", "The concentration of oxygen in a river was measured at different distances downstream from a sewage outlet.", "distance downstream", "km",
           "oxygen concentration", "mg per dm³", [-1, 0, 1, 2, 3, 4, 5, 6], [9.5, 9.0, 4.2, 2.0, 3.0, 5.5, 7.8, 9.0], "dip",
           "Explain why the oxygen concentration falls below the sewage outlet.",
           ["sewage provides food for bacteria", "bacteria multiply", "bacteria respire aerobically", "use up oxygen in the water", "fish / animals die"]),
    ],
    "resources.crops": [
        ds("5.2", "The yield of tomatoes in a glasshouse was measured at different carbon dioxide concentrations.", "carbon dioxide concentration", "ppm",
           "yield", "kg per m²", [300, 500, 700, 900, 1100, 1300], [20, 28, 34, 37, 38, 38], "rise_plateau",
           "Explain the shape of the graph.",
           ["carbon dioxide is a limiting factor at low concentration", "more carbon dioxide gives faster photosynthesis", "more glucose for growth",
            "at high concentration another factor limits, e.g. light or temperature"], dp=0),
        ds("5.3", "The yield of wheat was measured with different masses of nitrate fertiliser added.", "fertiliser added", "kg per hectare",
           "yield", "tonnes per hectare", [0, 50, 100, 150, 200, 250], [3.0, 4.6, 5.8, 6.4, 6.6, 6.6], "rise_plateau",
           "Explain why adding fertiliser increases the yield.",
           ["nitrate is needed to make amino acids", "for proteins", "for growth", "magnesium / other ions for chlorophyll"]),
    ],
    "resources.microorganisms": [
        ds("5.6", "The volume of carbon dioxide produced by yeast in ten minutes was measured at different temperatures.", "temperature", "°C",
           "volume of carbon dioxide", "cm³", [10, 20, 30, 40, 50, 60], [2, 7, 15, 22, 9, 1], "peak",
           "Explain the results.",
           ["respiration is controlled by enzymes", "temperature increases kinetic energy / collisions", "optimum at about 40 °C", "above the optimum, enzymes denature",
            "active site changes shape"], dp=0),
        ds("5.7", "The pH of milk was measured during the making of yoghurt.", "time", "hours",
           "pH", "", [0, 1, 2, 3, 4, 5, 6], [6.6, 6.2, 5.6, 5.0, 4.6, 4.5, 4.5], "fall_level",
           "Explain why the pH decreases.",
           ["Lactobacillus bacteria ferment lactose", "produce lactic acid", "acid lowers the pH", "pH levels off as bacteria slow / are inhibited by acid"]),
    ],
}


def _lab(name, unit):
    return f"{name[:1].upper()}{name[1:]}" + (f" in {unit}" if unit else "")


def _sing(u):
    return {"weeks": "week", "days": "day", "minutes": "minute", "years": "year", "hours": "hour", "seconds": "second"}.get(u, u)


def _yu(yname):
    """Name the real quantity when the y variable has no unit (used in rate units)."""
    for pre in ("mean number of ", "number of "):
        if yname.startswith(pre):
            return yname[len(pre):]
    return {"pH": "pH units", "relative risk of coronary heart disease": "relative risk"}.get(yname, yname)


def _xs(d, x):
    if d.xunit:
        return f"{nf(x)} {_sing(d.xunit) if x == 1 else d.xunit}"
    if d.xname == "year":
        return nf(x)
    return f"{'trial' if d.xname == 'trial number' else d.xname} {nf(x)}"


def _ys(d, y):
    if d.yunit == "%":
        return f"{nf(y)}%"
    return f"{nf(y)} {d.yunit}".strip() if d.yunit not in ("", "arbitrary units") else f"{nf(y)}" + (" arbitrary units" if d.yunit == "arbitrary units" else "")


def check_shape(d, ys):
    inc = all(b >= a for a, b in zip(ys, ys[1:]))
    dec = all(b <= a for a, b in zip(ys, ys[1:]))
    i_max = max(range(len(ys)), key=lambda i: ys[i])
    i_min = min(range(len(ys)), key=lambda i: ys[i])
    ok = {"rise": inc, "rise_plateau": inc, "fall": dec, "fall_level": dec,
          "peak": 0 < i_max < len(ys) - 1, "dip": 0 < i_min < len(ys) - 1}[d.shape]
    assert ok, (d.intro, d.shape, ys)


def readable(ys):
    """Can every value be read from a linear axis to about 2% of its range?"""
    top = max(abs(y) for y in ys)
    return all(y == 0 or abs(y) >= 0.05 * top for y in ys)


def trend_points(d, xs, ys):
    check_shape(d, ys)
    i_max = max(range(len(ys)), key=lambda i: ys[i])
    i_min = min(range(len(ys)), key=lambda i: ys[i])
    X, Y = d.xname, d.yname
    quote = f"uses data, e.g. {_ys(d, ys[0])} at {_xs(d, xs[0])} and {_ys(d, ys[-1])} at {_xs(d, xs[-1])}"
    if d.shape == "rise":
        return 2, [f"as {X} increases, {Y} increases / positive correlation", quote]
    if d.shape == "fall":
        return 2, [f"as {X} increases, {Y} decreases / negative correlation", quote]
    if d.shape == "peak":
        after = "decreases slightly" if ys[-1] >= 0.9 * ys[i_max] else "decreases"
        return 3, [f"{Y} increases up to {_xs(d, xs[i_max])}", f"then {Y} {after}", f"maximum of {_ys(d, ys[i_max])} at {_xs(d, xs[i_max])}",
                   quote]
    if d.shape == "dip":
        return 3, [f"{Y} decreases up to {_xs(d, xs[i_min])}", f"then {Y} increases / recovers", f"minimum of {_ys(d, ys[i_min])} at {_xs(d, xs[i_min])}", quote]
    j = next(i for i in range(1, len(ys)) if abs(ys[i] - ys[-1]) <= abs(ys[-1] - ys[0]) * 0.06 + 1e-9)
    if d.shape == "rise_plateau":
        return 3, [f"{Y} increases as {X} increases", f"then levels off / stays constant from about {_xs(d, xs[j])}", quote,
                   "rate of increase slows down"]
    return 3, [f"{Y} decreases as {X} increases", f"then levels off from about {_xs(d, xs[j])}", quote, "rate of decrease slows down"]


def make(sub, d, di, k):
    r = random.Random(f"{sub}-{di}-{k}")
    SC = [1.0, 0.9, 1.2, 0.8, 1.1, 1.25, 0.85, 1.15, 0.95, 1.3, 0.75]
    s = SC[(k // 4 + k) % len(SC)]
    if d.yname == "pH" or d.xname == "year":
        s = 1.0  # real-world data kept fixed; variety comes from the kind and the values asked about
    if d.yunit == "%" and "change" not in d.yname and max(d.ys) * s > 100:
        s = 1.0  # a percentage of a whole cannot exceed 100
    ys = [round(v * s, d.dp) if d.dp else round(v * s) for v in d.ys]
    if d.dp == 0:
        ys = [int(v) for v in ys]
    xs = d.xs
    kind = k % 4
    xl, yl = _lab(d.xname, d.xunit), _lab(d.yname, d.yunit)
    tbl = table_fig([xl, yl], [[nf(x), nf(y)] for x, y in zip(xs, ys)])
    ymax = 100 if d.yunit == "%" and "change" not in d.yname else None
    graph = svg_fig(line_graph([("", list(zip(xs, ys)))], xl, yl, xmin=min(0, min(xs)) if min(xs) >= 0 else min(xs),
                               ymin=min(0, min(ys)), xmax=max(xs), ymax=ymax, curve=d.shape in ("peak", "dip", "rise_plateau", "fall_level")), 100)
    tm, tp = trend_points(d, xs, ys)
    em = 3 if len(d.explain) >= 4 else 2
    if kind == 1 and k >= 4:
        em = 2
    explain_row = lambda lab: points_row(lab, em, d.explain, "Explain", "Do not credit a description of the trend alone", "AO2")
    nm = sub.split(".")[-1]
    refs = [d.ref]
    answer = None
    on_graph = kind == 0 or (kind == 3 and readable(ys))
    fig_word = "graph" if on_graph else "table"
    intro = d.intro.replace("The table shows", "The graph shows" if fig_word == "graph" else "The table shows").replace(
        "The graph shows", "The graph shows" if fig_word == "graph" else "The table shows")
    eq = d.explain_q
    if fig_word == "table" and kind != 1:
        eq = eq.replace("Explain the shape of the graph.", "Explain the trend shown by the data in the table.").replace("the graph", "the table")
    elif kind == 1:
        eq = eq.replace("the shape of the graph", "the shape of your graph")
    if kind == 0:
        parts = [text_part("a", f"Describe the relationship between {d.xname} and {d.yname} shown in the graph.", tm, figures=[graph]),
                 text_part("b", eq, em)]
        rows = [points_row("a", tm, tp, "Describe", "Data quoted must include units", "AO3"), explain_row("b")]
        cw, diff = "Describe", "4-6"
        answer = {"method": "values plotted on the graph (used for quoted data)", "values": {"x": list(xs), "y": list(ys)}, "checked": True}
    elif kind == 1:
        parts = [text_part("a", f"Plot a graph of the data in the table.\n\nJoin your points with {'a smooth curve' if d.shape != 'rise' else 'straight lines or a line of best fit'}.", 4,
                           space="graph", figures=[tbl]),
                 text_part("b", f"Describe the trend shown by your graph.", tm)]
        rows = graph_ms("a", d.xname, d.yname) + [points_row("b", tm, tp, "Describe", None, "AO3")]
        cw, diff = "Plot", "4-6" if k < 8 else "7-9"
        answer = {"method": "points to be plotted", "values": {"x": list(xs), "y": list(ys)}, "checked": True}
    elif kind == 2:
        pos = [i for i, y in enumerate(ys) if y > 0]
        i, j = pos[0], pos[-1]
        if k % 8 == 6 and len(pos) > 3:
            i, j = pos[1], pos[-2]
        if ys[i] == ys[j]:
            i, j = pos[0], pos[len(pos) // 2]
        pc = (ys[j] - ys[i]) / ys[i] * 100
        word = "increase" if pc > 0 else "decrease"
        parts = [calc_part("a", f"Calculate the percentage {word} in {d.yname} between {_xs(d, xs[i])} and {_xs(d, xs[j])}.\n\nGive your answer to the nearest whole number.",
                           2, "percentage change = ", suffix="%"),
                 text_part("b", eq, em)]
        parts[0]["figures"] = [tbl]
        rows = [row_("a", f"({nf(ys[j])} − {nf(ys[i])}) ÷ {nf(ys[i])} × 100 (1)", 1, None, "AO2"),
                row_("a", f"{nf(abs(pc), dp=0)}% (1)", 1, "Allow full marks for correct answer with no working; allow a negative sign for a decrease", "AO2"),
                explain_row("b")]
        answer = {"method": "(y2 − y1)/y1 × 100", "values": {"percent_change": float(nf(pc, dp=0))}, "checked": True}
        cw, diff = "Calculate", "4-6"
    else:
        idx = list(range(len(xs)))
        a = idx[(k // 4) % len(xs)]
        i, j = (1, len(xs) - 2) if (k // 4) % 2 else (0, len(xs) // 2)
        if xs[j] == xs[i]:
            j = i + 1
        rate = (ys[j] - ys[i]) / (xs[j] - xs[i])
        if on_graph:
            parts = [text_part("a", f"Use the graph to give the {d.yname} at {_xs(d, xs[a])}.", 1, 1, figures=[graph])]
            rows = [row_("a", f"{_ys(d, ys[a])} (1)", 1, "Allow ± half a small square", "AO3")]
        else:
            parts = [text_part("a", f"Use the table to give the {d.yname} at {_xs(d, xs[a])}.", 1, 1, figures=[tbl])]
            rows = [row_("a", f"{_ys(d, ys[a])} (1)", 1, None, "AO3")]
        if d.xunit and d.xname not in ("year",):
            per = _sing(d.xunit) if not d.xunit.startswith("°") else "°C"
            yu = d.yunit or _yu(d.yname)
            parts.append(calc_part("b", f"Calculate the mean rate of change of {'the ' if d.yname.startswith(('number', 'mean number')) else ''}{d.yname} between {_xs(d, xs[i])} and {_xs(d, xs[j])}.", 2,
                                   f"rate = ", 4, suffix=f"{yu} per {per}"))
            rows += [row_("b", f"({nf(ys[j])} − {nf(ys[i])}) ÷ ({nf(xs[j])} − {nf(xs[i])}) (1)", 1, None, "AO2"),
                     row_("b", f"{sfig(rate, 3)} {yu} per {per} (1)", 1, "Allow ecf from incorrect readings; ignore sign", "AO2")]
            answer = {"method": "Δy/Δx", "values": {"read": ys[a], "rate": float(sfig(rate, 3))}, "checked": True}
        else:
            diffv = ys[j] - ys[i]
            parts.append(calc_part("b", f"Calculate the difference in {d.yname} between {_xs(d, xs[i])} and {_xs(d, xs[j])}.", 1, "difference = ", 3))
            rows.append(row_("b", f"{nf(abs(diffv))} (1)", 1, "Allow ecf from incorrect readings", "AO2"))
            answer = {"method": "y2 − y1", "values": {"read": ys[a], "difference": abs(diffv)}, "checked": True}
        parts.append(text_part("c", eq, em))
        rows.append(explain_row("c"))
        cw, diff = "Calculate", "4-6" if k % 3 else "7-9"
    return dict(parts=parts, rows=rows, refs=refs, cw=cw, diff=diff, answer=answer, template=f"{nm}-data-{['graph','plot','pct','read'][kind]}") | {"intro": intro}


def _make(sub):
    @reg(sub, "data", f"{sub.split('.')[-1]}-data")
    def f():
        sets = DATA[sub]
        per = math.ceil(14 / len(sets)) + 1
        out, seen = [], set()
        for di, d in enumerate(sets):
            got, k = 0, 0
            while got < per and k < 80:
                q = make(sub, d, di, k)
                k += 1
                key = repr([(p["text"], p.get("figures")) for p in q["parts"]])
                if key in seen:
                    continue
                seen.add(key)
                out.append(q)
                got += 1
        return out
    return f


for _s in DATA:
    _make(_s)
