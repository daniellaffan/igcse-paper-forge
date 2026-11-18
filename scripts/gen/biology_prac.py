"""Practical / experimental-design templates.

Each context describes one investigation in our own words.  Kinds generated per context:
variables, plan (CORMS-style, point-marked "six of the following"), describe method,
repeats + control, explain a step (one per reason), hazard and precaution.
"""
from collections import namedtuple

from biology_lib import reg, text_part, row_, points_row

P = namedtuple("P", "ref aim intro iv dv controls org method repeat control reasons hazard plan_extra")


def ctx(ref, aim, intro, iv, dv, controls, org, method, control, reasons, hazard, repeat=None, plan_extra=()):
    return P(ref, aim, intro, iv, dv, controls, org, method, repeat or "repeat each test at least three times and calculate a mean",
             control, reasons, hazard, plan_extra)


CTX = {
    "structures.molecules": [
        ctx("2.12", "the effect of temperature on the activity of amylase",
            "A student mixed amylase solution with starch solution in water baths at different temperatures. Every 30 seconds a drop of the mixture was added to iodine solution on a spotting tile.",
            "temperature", "time taken until the iodine no longer turns blue-black",
            ["volume of amylase solution", "concentration of amylase", "volume and concentration of starch solution", "pH (use a buffer)"],
            None,
            ["place starch and amylase in separate tubes in a water bath at each temperature", "leave them to reach the temperature before mixing",
             "mix the solutions and start a stop clock", "take a drop every 30 seconds and add to iodine on a spotting tile",
             "record the time when the iodine stays orange-brown", "use at least five temperatures, e.g. 20 °C to 60 °C"],
            ("a tube of boiled (denatured) amylase with starch", "shows that the enzyme causes the starch to break down"),
            [("leave the enzyme and starch in the water bath before mixing them",
              ["so that the solutions reach the temperature being tested", "so the reaction happens at that temperature from the start"]),
             ("add a buffer solution to each tube",
              ["to keep the pH the same", "because pH also affects the activity of the enzyme", "so only temperature is changed"])],
            ("hot water from the water bath could scald", "use tongs or a test-tube rack; keep water below 70 °C")),
        ctx("2.14B", "the effect of pH on the activity of catalase",
            "A student added discs of potato to hydrogen peroxide solution mixed with buffers of different pH. The oxygen produced was collected in an upturned measuring cylinder.",
            "pH", "volume of oxygen collected in two minutes",
            ["number and size of potato discs", "volume and concentration of hydrogen peroxide", "temperature (use a water bath)", "time of collection"],
            "use discs cut from the same potato",
            ["cut potato discs of the same size with a cork borer", "add a buffer of known pH to the hydrogen peroxide", "add the discs and start the stop clock",
             "collect the gas in an upturned measuring cylinder or gas syringe", "read the volume after two minutes", "test at least five pH values, e.g. pH 3 to pH 9"],
            ("boiled potato discs at each pH", "shows that the oxygen is produced because of the enzyme"),
            [("cut all the potato discs with the same cork borer and to the same thickness",
              ["so the discs have the same surface area / mass", "so the amount of enzyme is the same", "so that the test is fair"]),
             ("use a gas syringe instead of counting bubbles",
              ["bubbles can be different sizes", "a syringe measures the volume accurately"])],
            ("hydrogen peroxide is an irritant to eyes and skin", "wear eye protection / goggles and wash off any spills")),
        ctx("2.12", "the effect of temperature on the digestion of milk protein by protease",
            "A student mixed protease solution with dilute milk at different temperatures and timed how long the milk took to turn clear.",
            "temperature", "time taken for the milk to turn clear",
            ["volume and concentration of protease", "volume and type of milk", "pH", "how cloudiness is judged (e.g. a cross under the tube)"],
            None,
            ["warm the milk and protease separately in a water bath at each temperature", "mix them and start timing",
             "place the tube in front of a printed cross", "stop timing when the cross can be seen clearly",
             "use a range of temperatures, e.g. 10 °C to 70 °C", "calculate a rate as 1 ÷ time"],
            ("boiled protease with milk", "shows that it is the enzyme that clears the milk"),
            [("place a printed cross behind the tube",
              ["gives a fixed end point", "so the end point is judged the same way each time", "makes timing more accurate"]),
             ("calculate 1 ÷ time for each result", ["converts time into a rate", "a shorter time means a faster rate"])],
            ("enzymes may cause allergic reactions", "avoid skin contact / wear gloves and eye protection")),
    ],
    "structures.movement": [
        ctx("2.17", "the effect of sucrose concentration on the mass of potato tissue",
            "A student cut potato cylinders, weighed them and left them in sucrose solutions of different concentrations for 30 minutes. They were then blotted and reweighed.",
            "concentration of sucrose solution", "percentage change in mass of the potato",
            ["size / length of the potato cylinders", "volume of solution", "time left in the solution", "temperature"],
            "cut all cylinders from the same potato",
            ["cut cylinders of the same length with a cork borer", "blot and weigh each cylinder at the start", "place each in a different concentration of sucrose",
             "leave for the same time, e.g. 30 minutes", "remove, blot dry and reweigh", "calculate percentage change in mass", "use at least five concentrations, e.g. 0 to 1.0 mol dm⁻³"],
            ("a cylinder in distilled water", "for comparison with no sucrose present"),
            [("blot the cylinders dry before reweighing",
              ["to remove surface water", "surface water would add to the mass", "so only water taken in by osmosis is measured"]),
             ("calculate percentage change in mass rather than change in mass",
              ["the cylinders had different starting masses", "allows results to be compared fairly"])],
            ("cork borer / scalpel is sharp", "cut away from the body on a white tile")),
        ctx("2.16", "the effect of surface area to volume ratio on the rate of diffusion",
            "A student cut cubes of agar jelly coloured pink with an indicator and placed them in dilute acid. The time for each cube to become colourless was recorded.",
            "size of agar cube (surface area to volume ratio)", "time taken for the cube to become colourless",
            ["concentration of acid", "volume of acid", "temperature", "type and concentration of agar / indicator"],
            None,
            ["cut cubes with sides of e.g. 0.5 cm, 1 cm, 1.5 cm and 2 cm", "measure each cube with a ruler", "place each cube in the same volume of acid",
             "start a stop clock", "record the time for the colour to disappear", "calculate the surface area to volume ratio of each cube"],
            ("a cube placed in water instead of acid", "shows that the colour change is caused by the acid"),
            [("cut the cubes with a sharp scalpel and measure them with a ruler",
              ["so the dimensions are accurate", "so the surface area to volume ratio can be calculated correctly"]),
             ("use the same volume of acid for each cube", ["so the concentration gradient is the same", "so that only cube size affects the rate"])],
            ("acid is an irritant", "wear eye protection; use dilute acid")),
        ctx("2.16", "the effect of temperature on the rate of diffusion",
            "A student placed tea bags (or crystals of potassium manganate(VII)) in beakers of water at different temperatures and timed how long the colour took to spread evenly.",
            "temperature of the water", "time for the colour to spread evenly",
            ["volume of water", "mass of crystal / type of tea bag", "size of beaker", "no stirring"],
            None,
            ["heat water to a range of temperatures using a water bath or kettle", "measure the temperature with a thermometer",
             "add a crystal of the same mass to each beaker", "start the stop clock", "time until the colour is evenly spread", "use at least five temperatures"],
            ("not applicable – compare with water at room temperature", "gives a baseline for comparison"),
            [("do not stir the water", ["stirring would mix the solution", "the colour would spread by mixing not diffusion"]),
             ("measure the temperature at the start and end", ["the water cools down", "so a mean temperature can be used"])],
            ("hot water could scald", "do not exceed 60 °C; place beakers on a heatproof mat")),
    ],
    "structures.plant-nutrition": [
        ctx("2.20", "the effect of light intensity on the rate of photosynthesis",
            "A student placed a piece of pondweed in a test tube of water and put a lamp at different distances from it. The number of bubbles released in one minute was counted.",
            "distance of the lamp (light intensity)", "number of bubbles released per minute",
            ["temperature (use a heat shield / water bath)", "carbon dioxide concentration (add sodium hydrogencarbonate)", "same piece of pondweed", "time of counting"],
            "use the same piece of pondweed",
            ["place the lamp at a set distance measured with a ruler", "leave for five minutes to acclimatise", "count bubbles for one minute",
             "move the lamp to a new distance", "use at least five distances", "carry out in a darkened room"],
            ("a tube with the lamp switched off / covered in foil", "shows that light is needed for the bubbles"),
            [("put a beaker of water between the lamp and the plant",
              ["the lamp gives out heat", "the water absorbs heat / acts as a heat shield", "so temperature stays the same"]),
             ("leave the pondweed for five minutes before counting at each new distance",
              ["so the plant can adjust to the new light intensity", "so the rate becomes steady"]),
             ("add sodium hydrogencarbonate to the water", ["provides carbon dioxide", "so carbon dioxide is not a limiting factor"])],
            ("the lamp becomes hot / water near electrical equipment", "do not touch the bulb; keep water away from the lamp and plug")),
        ctx("2.23", "whether chlorophyll is needed for photosynthesis",
            "A student used a plant with variegated leaves (green and white areas). After the plant had been in light, a leaf was tested for starch.",
            "presence of chlorophyll (green or white parts of the leaf)", "colour of the leaf with iodine (starch present or absent)",
            ["light intensity", "time in the light", "temperature", "carbon dioxide availability"],
            "destarch the plant first by keeping it in the dark for 48 hours",
            ["destarch the plant in the dark for 48 hours", "place in bright light for several hours", "draw the leaf to record the pattern",
             "boil the leaf in water", "place in hot ethanol to remove chlorophyll", "rinse and spread on a white tile", "add iodine solution"],
            ("the white (non-green) areas of the same leaf act as the control", "shows starch is only made where chlorophyll is present / any difference is due to chlorophyll"),
            [("place the leaf in hot ethanol", ["removes the chlorophyll", "so the colour change with iodine can be seen"]),
             ("boil the leaf in water first", ["kills the cells / stops reactions", "breaks down membranes so iodine can enter"]),
             ("keep the plant in the dark for 48 hours before the experiment", ["the plant uses up its stored starch", "so any starch found was made during the experiment"])],
            ("ethanol is flammable", "heat ethanol in a water bath, not over a flame")),
        ctx("2.20", "the effect of carbon dioxide concentration on the rate of photosynthesis",
            "A student placed pondweed in solutions with different concentrations of sodium hydrogencarbonate and measured the oxygen produced.",
            "concentration of sodium hydrogencarbonate (carbon dioxide)", "volume of oxygen produced in five minutes",
            ["light intensity / distance of lamp", "temperature", "length / mass of pondweed", "volume of solution"],
            "use pondweed of the same length from the same plant",
            ["make up a range of hydrogencarbonate concentrations", "place pondweed in each with the lamp at a fixed distance",
             "leave to acclimatise", "collect gas in a gas syringe or capillary tube", "measure volume in five minutes", "use at least five concentrations"],
            ("pondweed in boiled water with no hydrogencarbonate", "shows the effect of very little carbon dioxide"),
            [("collect the gas in a capillary tube and measure the length of the bubble",
              ["more accurate than counting bubbles", "bubbles can vary in size"]),
             ("keep the lamp at the same distance", ["light intensity is a limiting factor", "so only carbon dioxide concentration changes"])],
            ("the lamp becomes hot", "do not touch the bulb; switch off when not in use")),
    ],
    "structures.human-nutrition": [
        ctx("2.33B", "how much energy different foods contain",
            "A student burned a sample of food under a boiling tube of water and measured the temperature rise of the water.",
            "type of food", "temperature rise of the water (energy per gram)",
            ["volume of water", "distance of food from the tube", "starting temperature of the water", "mass of food (or calculate per gram)"],
            None,
            ["measure 20 cm³ of water into a boiling tube", "record the starting temperature", "weigh the food",
             "set the food alight with a Bunsen burner and hold it under the tube", "relight until the food will not burn",
             "record the highest temperature", "calculate energy per gram = mass of water × 4.2 × temperature rise ÷ mass of food"],
            ("not applicable", "each food is compared with the others"),
            [("stir the water before reading the final temperature", ["so heat is evenly spread", "so the reading is accurate"]),
             ("relight the food until it no longer burns", ["so all the energy in the food is released", "otherwise the energy would be underestimated"]),
             ("hold the food at the same distance below the tube each time", ["less heat is lost", "makes the test fair"])],
            ("burning food / boiling tube is hot; nut allergies", "use tongs and a heatproof mat; do not use nuts if anyone is allergic")),
        ctx("2.29", "the effect of bile salts on the digestion of fat by lipase",
            "A student mixed milk, lipase and an indicator that changes colour as the pH falls. One set of tubes also contained bile salts.",
            "presence of bile salts", "time taken for the indicator to change colour",
            ["volume and concentration of lipase", "volume of milk", "temperature", "volume of indicator"],
            None,
            ["add milk and sodium carbonate solution to a tube", "add a few drops of indicator", "add bile salts to half the tubes",
             "add lipase and start timing", "record the time for the colour to change", "keep tubes in a water bath at 35 °C"],
            ("a tube with boiled lipase", "shows the colour change is caused by the enzyme"),
            [("keep the tubes in a water bath at 35 °C", ["enzymes work best near body temperature", "temperature must be kept constant"]),
             ("add an indicator to the tubes", ["fatty acids are produced", "fatty acids lower the pH", "the colour change shows that digestion has happened"])],
            ("enzymes can irritate skin", "wear eye protection and wash spills")),
    ],
    "structures.respiration": [
        ctx("2.39", "whether germinating seeds release heat",
            "A student put germinating peas in one vacuum flask and boiled (dead) peas in another. A thermometer was placed in each flask, and the temperature was recorded over three days.",
            "whether the peas are alive", "temperature inside the flask",
            ["number / mass of peas", "type of flask", "starting temperature", "room temperature"],
            "use the same type of pea",
            ["soak peas for 24 hours so they start to germinate", "boil half of them", "rinse both sets in disinfectant",
             "place each set in a vacuum flask with a thermometer", "plug the flask with cotton wool", "record the temperature each day for three days"],
            ("a flask of boiled peas", "shows the heat comes from respiration of living peas"),
            [("rinse both sets of peas in disinfectant", ["kills microorganisms", "microorganisms on the dead peas would respire and release heat"]),
             ("use a vacuum flask", ["reduces heat loss", "so the temperature rise can be detected"]),
             ("plug the flask with cotton wool rather than a bung", ["lets oxygen in", "so aerobic respiration can continue / carbon dioxide can escape"])],
            ("disinfectant can irritate skin", "wear gloves and eye protection")),
        ctx("2.39", "the effect of temperature on the rate of respiration of woodlice",
            "A student placed woodlice in a respirometer containing soda lime. The distance moved by a drop of coloured liquid in a capillary tube was measured at different temperatures.",
            "temperature", "distance moved by the liquid drop in five minutes",
            ["number / mass of woodlice", "mass of soda lime", "time", "size of capillary tube"],
            "use woodlice of similar size",
            ["place woodlice in the tube on a gauze above soda lime", "put the respirometer in a water bath", "leave to reach the temperature",
             "measure the distance moved by the drop in five minutes", "reset the drop with the syringe", "repeat at five different temperatures"],
            ("a respirometer with glass beads of the same volume instead of woodlice", "shows any movement caused by changes in temperature or pressure"),
            [("add soda lime to the tube", ["absorbs carbon dioxide", "so the movement of the drop is due to oxygen being taken in"]),
             ("leave the respirometer in the water bath for ten minutes before taking readings", ["so the air inside reaches the temperature", "gas expansion would otherwise move the drop"])],
            ("soda lime is corrosive", "do not let the woodlice or skin touch it; use gloves and eye protection")),
        ctx("2.39", "whether yeast releases carbon dioxide when it respires",
            "A student set up a tube of yeast in glucose solution and bubbled the gas produced through limewater.",
            "presence of living yeast", "time taken for the limewater to turn cloudy",
            ["volume and concentration of glucose", "mass of yeast", "temperature", "volume of limewater"],
            None,
            ["mix yeast with glucose solution in a tube", "cover with a layer of oil", "connect a delivery tube into limewater",
             "keep in a water bath at 35 °C", "record the time for the limewater to turn cloudy"],
            ("a tube of boiled yeast in glucose", "shows that living yeast produces the carbon dioxide"),
            [("cover the yeast mixture with a layer of oil", ["stops oxygen getting in", "so the yeast respires anaerobically"]),
             ("boil the glucose solution and cool it before adding yeast", ["removes dissolved oxygen", "cooling stops the yeast being killed"])],
            ("hot water bath could scald", "use a thermostatically controlled bath and test tube holders")),
    ],
    "structures.gas-exchange-plants": [
        ctx("2.45B", "the effect of light intensity on net gas exchange in leaves",
            "A student placed leaves in tubes containing hydrogencarbonate indicator. The tubes were placed at different distances from a lamp, and one was covered in foil.",
            "light intensity", "colour of the hydrogencarbonate indicator after two hours",
            ["number / size of leaves", "volume of indicator", "temperature", "time"],
            "use leaves of the same size from the same plant",
            ["put the same volume of indicator in each tube", "add a leaf held above the indicator on gauze", "seal each tube with a bung",
             "cover one tube in foil", "place the others at different distances from a lamp", "record the colour after two hours"],
            ("a tube with no leaf at each light intensity", "shows any colour change is caused by the leaf"),
            [("cover one tube with aluminium foil", ["no light reaches the leaf", "so only respiration takes place", "carbon dioxide rises / indicator turns yellow"]),
             ("seal the tubes with bungs", ["stops gases entering or leaving", "so changes are only caused by the leaf"])],
            ("the lamp becomes hot", "do not touch the bulb; keep water away from the lamp")),
        ctx("2.43B", "which surface of a leaf loses more water vapour through stomata",
            "A student coated the upper surface of one leaf and the lower surface of another with petroleum jelly. The leaves were weighed each day.",
            "surface of the leaf coated", "loss in mass of the leaf over five days",
            ["size of leaves", "type / age of leaf", "temperature", "humidity / air movement"],
            "use leaves from the same plant",
            ["coat surfaces with petroleum jelly", "weigh each leaf", "hang the leaves on a line in the same place",
             "reweigh each day for five days", "calculate percentage loss in mass"],
            ("an uncoated leaf", "shows the total water loss without blocking stomata"),
            [("coat the leaf with petroleum jelly", ["blocks the stomata", "stops water vapour leaving that surface"]),
             ("calculate the percentage loss in mass", ["the leaves have different starting masses", "so results can be compared"])],
            ("none significant", "wash hands after handling plants")),
    ],
    "structures.gas-exchange-humans": [
        ctx("2.50", "the effect of exercise on breathing rate",
            "Students measured their breathing rate at rest and then after exercising for different lengths of time.",
            "time spent exercising", "breathing rate (breaths per minute)",
            ["type of exercise", "intensity of exercise", "time of measurement after exercise", "same person"],
            "use people of the same age, sex and fitness",
            ["measure resting breathing rate by counting breaths for one minute", "exercise for a set time, e.g. 1 minute",
             "count breaths for one minute immediately afterwards", "rest until breathing returns to normal", "repeat for 2, 3, 4 and 5 minutes of exercise"],
            ("the resting breathing rate", "gives a baseline for comparison"),
            [("rest until breathing rate returns to normal before the next test", ["so the starting rate is the same", "so the effect of the previous exercise is removed"]),
             ("count breaths for a full minute rather than 10 seconds", ["more accurate", "reduces the effect of a counting error"])],
            ("people with asthma / heart conditions could become ill", "check health first; stop if feeling unwell")),
        ctx("2.50", "whether inhaled or exhaled air contains more carbon dioxide",
            "A student breathed in and out through a pair of tubes containing limewater, so that inhaled air passed through one tube and exhaled air through the other.",
            "inhaled or exhaled air", "time taken for the limewater to turn cloudy",
            ["volume of limewater", "number of breaths", "size of tubes", "rate of breathing"],
            None,
            ["set up two tubes of limewater connected to a mouthpiece", "breathe gently in and out through the mouthpiece",
             "inhaled air passes through one tube and exhaled air through the other", "record how long each tube takes to turn cloudy"],
            ("not applicable – the two tubes are compared", "the inhaled-air tube acts as a comparison"),
            [("breathe gently through the mouthpiece", ["to avoid sucking limewater into the mouth", "keeps the airflow steady"]),
             ("use the same volume of limewater in both tubes", ["so the test is fair", "so the time to turn cloudy can be compared"])],
            ("limewater could be sucked into the mouth", "breathe gently; use a non-return valve; wear eye protection")),
    ],
    "structures.transport-plants": [
        ctx("2.58B", "the effect of air movement on the rate of transpiration",
            "A student set up a potometer with a leafy shoot and measured how far an air bubble moved with a fan at different distances from the shoot.",
            "wind speed (distance of fan)", "distance moved by the air bubble in five minutes",
            ["temperature", "light intensity", "humidity", "same shoot / number of leaves"],
            "use the same leafy shoot throughout",
            ["cut the shoot under water", "fit it into the potometer under water", "seal joints with petroleum jelly", "introduce an air bubble",
             "place a fan at a set distance", "measure the distance moved by the bubble in five minutes", "reset the bubble with the reservoir", "repeat at different fan distances"],
            ("readings with the fan switched off", "gives the rate in still air for comparison"),
            [("cut the shoot under water", ["stops air entering the xylem", "air bubbles would block water flow"]),
             ("seal the joints with petroleum jelly", ["makes the apparatus airtight", "so water is only lost from the shoot"]),
             ("dry the leaves before starting", ["water on the leaves would evaporate", "rate would not be due to transpiration alone"])],
            ("fan blades / water near electricity", "keep fingers clear and keep water away from the fan plug")),
        ctx("2.57B", "the effect of temperature on the rate of transpiration",
            "A student weighed potted plants with their soil covered in plastic bags, kept at different temperatures, every day for four days.",
            "temperature", "loss in mass of the plant",
            ["light intensity", "humidity", "air movement", "size / species of plant"],
            "use plants of the same species, size and age",
            ["cover the pot and soil with a plastic bag", "weigh each plant", "place in incubators / rooms at different temperatures",
             "reweigh every day", "calculate the loss in mass per day"],
            ("not applicable", "plants at different temperatures are compared"),
            [("cover the soil with a plastic bag", ["stops water evaporating from the soil", "so mass loss is only from the plant"]),
             ("water each plant with the same volume at the start", ["so all have the same water available", "makes the test fair"])],
            ("incubators can be hot", "use oven gloves when moving plants")),
    ],
    "structures.plant-responses": [
        ctx("2.84", "the effect of light from one side on the growth of shoots",
            "A student grew seedlings in boxes. One box had a slit on one side letting light in, one was in all-round light and one was in darkness.",
            "direction of light", "direction of growth / angle of the shoot",
            ["type of seedling", "temperature", "water given", "time"],
            "use seedlings of the same species and age",
            ["plant ten seedlings in each dish", "place one dish in a box with a slit", "place one in all-round light and one in the dark",
             "leave for three days", "measure the angle of the shoot tips with a protractor"],
            ("seedlings in all-round light", "shows how seedlings grow without directional light"),
            [("use ten seedlings in each dish", ["seedlings vary", "makes the results more reliable / allows a mean to be calculated"]),
             ("measure the angle of curvature with a protractor", ["gives a quantitative result", "more accurate than describing the direction"])],
            ("none significant", "wash hands after handling compost")),
        ctx("2.84", "the effect of gravity on the growth of roots",
            "A student pinned germinating bean seeds to damp cotton wool in a dish. One dish was placed on a clinostat that turned slowly, and another was left still.",
            "whether the seeds are rotated on a clinostat", "direction of growth of the roots",
            ["temperature", "moisture", "light (keep in dark)", "type and age of seed"],
            "use bean seeds of the same type and age",
            ["pin seeds to damp cotton wool with roots pointing in different directions", "fix one dish to a clinostat", "leave one dish still",
             "keep both in the dark", "observe after two days", "draw or measure the direction of root growth"],
            ("the clinostat dish", "rotation cancels the effect of gravity"),
            [("keep both dishes in the dark", ["so light does not affect growth", "only gravity is tested"]),
             ("keep the cotton wool damp", ["seeds need water to germinate and grow", "prevents the seeds / roots drying out and dying, so the response can be observed"])],
            ("pins are sharp", "handle carefully")),
    ],
    "structures.nervous": [
        ctx("2.88", "the effect of caffeine on reaction time",
            "Students tested their reaction time by catching a ruler dropped between their fingers, before and after drinking a cola drink.",
            "caffeine (drinking cola or not)", "distance the ruler falls before it is caught",
            ["height the ruler is dropped from", "same hand", "same person dropping", "time after drinking"],
            "use the same people and similar ages",
            ["hold the ruler with zero level with the person's thumb", "drop the ruler without warning", "record the distance where it is caught",
             "repeat ten times", "drink a caffeinated drink and wait 15 minutes", "repeat the test", "convert distance to reaction time with a table"],
            ("a decaffeinated drink", "shows the effect is due to caffeine"),
            [("drop the ruler without warning", ["the person cannot anticipate", "so it measures a true reaction time"]),
             ("repeat the test ten times", ["the person may improve with practice", "to calculate a mean", "to identify anomalies"])],
            ("caffeine may affect some people", "check medical conditions; use small amounts")),
        ctx("2.92", "the effect of light intensity on pupil diameter",
            "A student measured the diameter of a partner's pupil in a dim room and then in bright light.",
            "light intensity", "diameter of the pupil",
            ["distance from the light", "same person", "time in the light before measuring", "same eye"],
            None,
            ["sit in a dim room for two minutes", "measure the pupil diameter with a ruler held close to the eye", "shine a lamp towards the eye from a set distance",
             "measure the diameter again", "repeat for different lamp distances", "use a light meter to measure intensity"],
            ("measurements in dim light", "acts as the baseline"),
            [("wait two minutes after changing light before measuring", ["the iris needs time to respond", "so the pupil has reached its final size"]),
             ("use a light meter", ["gives a measured light intensity", "more accurate than relying on the lamp distance"])],
            ("bright light could damage the eye", "do not shine light directly into the eye; use a low-power lamp")),
    ],
    "reproduction.plant-reproduction": [
        ctx("3.5", "whether seeds need water, oxygen and warmth to germinate",
            "A student set up four tubes of cress seeds. One had all conditions, and the others each lacked water, oxygen or warmth.",
            "presence of water, oxygen or warmth", "number of seeds that germinate",
            ["number of seeds", "type of seed", "time", "light"],
            "use seeds of the same type",
            ["place ten seeds on cotton wool in each tube", "tube A: damp cotton wool, room temperature", "tube B: dry cotton wool",
             "tube C: boiled cooled water covered with oil", "tube D: damp cotton wool in a fridge", "count the germinated seeds after five days"],
            ("tube A with water, oxygen and warmth", "shows seeds germinate when all conditions are present"),
            [("boil the water and cover it with a layer of oil", ["boiling removes dissolved oxygen", "oil stops oxygen dissolving again"]),
             ("use ten seeds in each tube", ["some seeds may not be viable", "allows the percentage germinating to be found"])],
            ("none significant", "wash hands after handling seeds")),
        ctx("3.5", "the effect of temperature on the germination of seeds",
            "A student placed dishes of seeds on damp filter paper at different temperatures and counted how many germinated each day.",
            "temperature", "percentage of seeds germinated after four days",
            ["number of seeds", "volume of water", "type of seed", "light"],
            "use seeds of the same species and batch",
            ["place 20 seeds on damp filter paper in each dish", "put each dish at a different temperature", "add the same volume of water each day",
             "count germinated seeds each day", "calculate percentage germination", "use at least five temperatures"],
            ("not applicable", "dishes at different temperatures are compared"),
            [("add the same volume of water to each dish", ["water is needed for germination", "so water is not a variable"]),
             ("count a seed as germinated when the root is visible", ["gives a clear end point", "the same rule is used for every seed"])],
            ("mould growth on seeds", "keep dishes covered and wash hands")),
    ],
    "ecology.environment": [
        ctx("4.2", "whether the number of daisies is different on a sports field and a lawn",
            "Students used quadrats to compare the population of daisies in two areas of the school grounds.",
            "area sampled", "number of daisies per quadrat",
            ["size of quadrat", "number of quadrats", "time of year", "method of placing the quadrats"],
            None,
            ["lay out two tape measures at right angles", "use random numbers to find coordinates", "place a 0.25 m² quadrat at each coordinate",
             "count the daisies in the quadrat", "take at least ten quadrats in each area", "calculate the mean number per quadrat"],
            ("not applicable", "the two areas are compared"),
            [("place the quadrats at random coordinates", ["avoids bias", "so the sample is representative"]),
             ("use at least ten quadrats in each area", ["gives a more reliable mean", "reduces the effect of unusual quadrats"])],
            ("uneven ground / stinging plants", "wear suitable shoes and gloves")),
        ctx("4.4B", "how the distribution of a plant changes with distance from a hedge",
            "A student ran a tape measure from a hedge across a field and placed a quadrat at regular intervals along it.",
            "distance from the hedge", "percentage cover of the plant in each quadrat",
            ["size of quadrat", "time of day", "same person judging percentage cover", "same interval between quadrats"],
            None,
            ["lay a tape measure from the hedge across the field (a transect)", "place a quadrat every 2 m along the tape",
             "estimate the percentage cover of the plant", "measure light intensity at each quadrat", "repeat along two more transects"],
            ("not applicable", "different distances are compared"),
            [("measure light intensity at each quadrat", ["light is an abiotic factor", "may explain the distribution"]),
             ("repeat the transect in two other places", ["one transect may not be typical", "makes results more reliable"])],
            ("uneven ground", "wear suitable shoes and stay away from roads")),
        ctx("4.4B", "the biodiversity of two areas of a rocky shore",
            "Students placed quadrats at random on two areas of a rocky shore and recorded the species in each quadrat.",
            "area of the shore", "number of different species per quadrat",
            ["size of quadrat", "number of quadrats", "time after low tide", "same identification key"],
            None,
            ["use random coordinates in each area", "place a quadrat at each coordinate", "identify each species with a key",
             "record the number of species and individuals", "use at least ten quadrats per area", "compare the mean number of species"],
            ("not applicable", "the two areas are compared"),
            [("use an identification key", ["species are identified correctly", "so the number of species is accurate"]),
             ("sample both areas at the same time after low tide", ["organisms move as the tide changes", "so conditions are the same"])],
            ("slippery rocks / incoming tide", "wear grippy shoes; check tide times; work in pairs")),
    ],
    "resources.crops": [
        ctx("5.2", "the effect of carbon dioxide concentration on the growth of lettuces in a glasshouse",
            "A grower wanted to find out whether adding carbon dioxide to a glasshouse would increase the yield of lettuces.",
            "carbon dioxide concentration", "mass of lettuces harvested",
            ["temperature", "light intensity", "water and fertiliser", "variety of lettuce"],
            "use lettuces of the same variety and age",
            ["set up glasshouses with different carbon dioxide concentrations", "plant the same number of lettuces in each", "grow for the same time, e.g. six weeks",
             "harvest the lettuces", "measure the mass of each lettuce", "calculate the mean mass"],
            ("a glasshouse with normal air", "for comparison with no added carbon dioxide"),
            [("keep the temperature the same in each glasshouse", ["temperature affects the rate of photosynthesis", "so only carbon dioxide is changed"]),
             ("grow 50 lettuces at each concentration", ["individual plants vary", "a large sample gives a reliable mean"])],
            ("paraffin heaters produce carbon monoxide", "make sure the glasshouse is ventilated")),
        ctx("5.3", "the effect of fertiliser on the yield of tomato plants",
            "A student grew tomato plants with different masses of fertiliser added to the compost.",
            "mass of fertiliser", "mass of tomatoes produced per plant",
            ["volume of water", "type and volume of compost", "light and temperature", "variety of tomato"],
            "use plants of the same variety and age",
            ["add different masses of fertiliser to the same mass of compost", "plant one seedling in each pot", "water each pot equally",
             "grow for the same time", "weigh all tomatoes from each plant", "use at least five masses of fertiliser"],
            ("plants with no fertiliser", "shows the effect of fertiliser"),
            [("give each pot the same volume of water", ["water affects growth", "so the test is fair"]),
             ("grow five plants for each mass of fertiliser", ["plants vary", "allows a mean to be calculated"])],
            ("fertiliser can irritate skin", "wear gloves and wash hands")),
    ],
    "resources.microorganisms": [
        ctx("5.6", "the effect of temperature on the rate of respiration in yeast",
            "A student mixed yeast with sugar solution in a tube and counted the bubbles of gas released in water baths at different temperatures.",
            "temperature", "number of bubbles of carbon dioxide per minute",
            ["mass of yeast", "volume and concentration of sugar solution", "type of sugar", "time"],
            None,
            ["mix yeast and sugar solution in a boiling tube", "connect a delivery tube into water", "place the tube in a water bath",
             "leave for five minutes to adjust", "count the bubbles for one minute", "repeat at five different temperatures"],
            ("boiled yeast with sugar solution", "shows that living yeast releases the gas"),
            [("leave the tube in the water bath for five minutes before counting", ["so the mixture reaches the temperature", "so the rate is steady"]),
             ("collect the gas in a gas syringe instead of counting bubbles", ["bubbles vary in size", "gives the volume accurately"])],
            ("hot water could scald", "use a thermostatic water bath below 60 °C")),
        ctx("5.6", "the effect of sugar concentration on the rate of anaerobic respiration in yeast",
            "A student measured the volume of carbon dioxide released by yeast in sugar solutions of different concentrations.",
            "concentration of sugar solution", "volume of carbon dioxide in ten minutes",
            ["temperature", "mass of yeast", "volume of solution", "pH"],
            None,
            ["make up sugar solutions of 0 to 10%", "add the same mass of yeast to each", "cover with a layer of oil", "collect gas in a gas syringe",
             "record the volume after ten minutes", "keep all tubes in a water bath at 30 °C"],
            ("yeast in water with no sugar", "shows the gas is produced from sugar"),
            [("cover the mixture with oil", ["prevents oxygen entering", "so respiration is anaerobic"]),
             ("keep all tubes at 30 °C", ["temperature affects enzyme activity / rate", "so only sugar concentration changes"])],
            ("glassware could break", "handle carefully and wear eye protection")),
    ],
}


# C point for categorical / two-level independent variables (keyed by subtopic, context index)
CPOINT = {
    ("structures.plant-nutrition", 1): "C – compare the green areas with the white areas of the same variegated leaf",
    ("structures.human-nutrition", 0): "C – compare several different foods (at least three)",
    ("structures.human-nutrition", 1): "C – compare tubes with and without bile salts",
    ("structures.respiration", 0): "C – compare living (germinating) peas with boiled (dead) peas that have been disinfected",
    ("structures.respiration", 2): "C – compare living yeast with boiled (dead) yeast",
    ("structures.gas-exchange-plants", 1): "C – compare leaves coated on the upper surface, the lower surface, both surfaces and neither surface",
    ("structures.gas-exchange-humans", 1): "C – compare inhaled air with exhaled air",
    ("structures.plant-responses", 0): "C – compare seedlings lit from one side with seedlings in all-round light",
    ("structures.plant-responses", 1): "C – compare seeds on a rotating clinostat with seeds on a stationary clinostat",
    ("structures.nervous", 0): "C – compare reaction times with and without a caffeinated drink",
    ("reproduction.plant-reproduction", 0): "C – remove one condition (water, oxygen or warmth) from each tube and compare with a tube that has all three",
    ("ecology.environment", 0): "C – compare the two areas (sports field and lawn)",
    ("ecology.environment", 1): "C – place quadrats at regular distances from the hedge (at least five distances)",
    ("ecology.environment", 2): "C – compare the two areas of the shore",
}
FIELD_ORG = {0: "identify the daisies correctly / count only the same species",
             1: "identify the plant species correctly using a key",
             2: "use the same identification key to identify each species"}


# habitat-specific variables for field work, phrased as how to keep them the same (environment context index)
FIELD_CTRL = {
    # IV = area (sports field vs lawn): trampling and mowing differ between the areas, so they are not listed as controls
    0: ("named variable, e.g. soil moisture / soil pH / shade from trees or buildings / time of year",
        "keep it the same, e.g. choose areas with similar soil moisture and pH / sample open areas away from trees and buildings in both places / sample both areas on the same day"),
    # IV = distance from the hedge: light / shade co-varies with distance, so it is not listed as a control
    1: ("named variable, e.g. soil moisture / soil pH / soil mineral content / trampling / grazing",
        "keep it the same, e.g. run the transect across ground of one soil type / away from paths and gateways / where no animals graze / sample all quadrats on the same day"),
    # IV = area of the shore; mobile animals move with the tide, time of day and weather
    2: ("named variable, e.g. height on the shore / time after low tide / time of day / weather / aspect / season",
        "keep it the same, e.g. sample both areas at the same height on the shore, at the same time after low tide, on the same day in similar weather, on rocks facing the same direction"),
}


def who_of(c):
    t = c.intro.lower()
    return "the grower" if t.startswith("a grower") else "the students" if t.startswith("students") else "the student"


def is_field(c):
    return "quadrat" in c.intro.lower()


def accuracy(c):
    d, t = c.dv.lower(), c.intro.lower()
    if is_field(c):
        return "use an identification key / use a gridded quadrat / have the same person count every quadrat / search the quadrat carefully (1)"
    if "mass" in d and ("lettuce" in d or "tomato" in d):
        return "use a balance with a higher resolution / remove soil and excess water before weighing / weigh several and find a mean (1)"
    if "mass" in d:
        return "use a balance with a higher resolution, e.g. 0.01 g / blot dry before weighing (1)"
    if "bubble" in d or "volume" in d:
        return "collect the gas in a gas syringe / measuring cylinder instead of counting bubbles (1)"
    if "temperature" in d:
        return "use a digital thermometer / temperature probe (1)"
    if "distance" in d and "ruler" in d:
        return "read the ruler at eye level at the top of the thumb / use a ruler with smaller divisions (1)"
    if "distance" in d or "diameter" in d:
        return "use a ruler / scale with smaller divisions and read it at eye level (1)"
    if "time" in d or "colour" in d:
        return "compare with a colour standard / use a colorimeter / use a stop clock and decide the end point in advance (1)"
    return "use more precise apparatus suited to the measurement (1)"


def _short(sub):
    return sub.split(".")[-1]


def gen_sub(sub):
    out = []
    for ci, c in enumerate(CTX[sub]):
        nm = _short(sub)
        refs = [c.ref]
        who = who_of(c)
        field = is_field(c)
        # 1. variables
        conts = c.controls
        p = [text_part("a", f"State the independent variable in this investigation.", 1, 1),
             text_part("b", "State the dependent variable.", 1, 1),
             text_part("c", "Give two variables that should be controlled.", 2, 2)]
        r = [row_("a", c.iv + " (1)", 1, None, "AO3"), row_("b", c.dv + " (1)", 1, "Accept a description of how it is measured", "AO3"),
             points_row("c", 2, conts, "Give", "Ignore 'amount' unless qualified, e.g. volume or mass", "AO3")]
        out.append(dict(parts=p, rows=r, refs=refs, cw="State", diff="1-3", intro=c.intro, template=f"{nm}-prac-vars"))
        # 2. plan (CORMS style, point-marked)
        cpt = CPOINT.get((sub, ci), f"C – change the {c.iv} (at least five values / a suitable range)")
        org = c.org or (FIELD_ORG.get(ci) if field else None)
        pts = [cpt,
               f"O – {org}" if org else "O – use the same type / source of biological material",
               f"R – {c.repeat}",
               f"M1 – measure the {c.dv}",
               "M2 – measure over the same period of time / at the same time",
               f"S1 – control {conts[0]}", f"S2 – control {conts[1]}"] + [f"S – control {x}" for x in conts[2:3]] + list(c.plan_extra)
        p = [text_part("", f"Design an investigation to find out {c.aim}.\n\nInclude experimental details in your answer and write in full sentences.", 6, 12)]
        r = [points_row("", 6, pts, "A plan", "Allow S marks for any two other relevant control variables; credit a correctly described control experiment in place of one S mark", "AO3")]
        r[0]["answer"] = r[0]["answer"].replace("A plan that", "An answer that")
        out.append(dict(parts=p, rows=r, refs=refs, cw="Design", diff="7-9", template=f"{nm}-prac-plan"))
        # 3. describe method
        p = [text_part("", f"Describe how {who} could carry out this investigation of {c.aim}.", 4, 8)]
        r = [points_row("", 4, c.method, "Describe", "Accept a suitable alternative method", "AO3")]
        out.append(dict(parts=p, rows=r, refs=refs, cw="Describe", diff="4-6", intro=c.intro, template=f"{nm}-prac-method"))
        # 4. repeats + control
        ctl, why = c.control
        p = [text_part("a", f"Explain why {who} should repeat the investigation.", 2, 3)]
        r = [points_row("a", 2, ["to calculate a mean", "to identify anomalous results", "to make the results more reliable / reduce the effect of random errors",
                                  "biological material / measurements vary"], "Explain", "Reject 'to make it accurate' on its own; reject 'fair test'", "AO3")]
        if not ctl.startswith("not applicable"):
            p.append(text_part("b", "Describe a suitable control for this investigation and explain why it is needed.", 2, 3))
            r.append(points_row("b", 2, [ctl, why], "Describe", None, "AO3"))
        else:
            p.append(text_part("b", f"Suggest one variable, other than the {c.iv}, that could affect the {c.dv}. Explain how it could be controlled.", 2, 3))
            if field:
                bp = list(FIELD_CTRL[ci])
            else:
                bp = [f"named variable, e.g. {conts[0]}", f"a suitable method of controlling the named variable, e.g. keep the {conts[0]} the same each time / measure and record it"]
            r.append(points_row("b", 2, bp, "Suggest", "Accept any valid equivalent variable that affects the measurement, with a matching way of keeping it the same" if field else None, "AO3"))
        out.append(dict(parts=p, rows=r, refs=refs, cw="Explain", diff="4-6", intro=c.intro, template=f"{nm}-prac-reliab"))
        # 5. explain steps
        for si, (step, why_pts) in enumerate(c.reasons):
            m = min(2, len(why_pts))
            p = [text_part("", f"In this investigation, {who} {'were' if who.endswith('students') else 'was'} told to {step}.\n\nExplain why.", m, 3)]
            r = [points_row("", m, why_pts, "Explain", None, "AO3")]
            out.append(dict(parts=p, rows=r, refs=refs, cw="Explain", diff="4-6" if si % 2 == 0 else "7-9", intro=c.intro, template=f"{nm}-prac-step"))
        # 6. hazard + expected result
        hz, prec = c.hazard
        if not hz.startswith("none"):
            p = [text_part("a", "Identify one hazard in this investigation and suggest how the risk could be reduced.", 2, 3),
                 text_part("b", f"Suggest one way {who} could make the measurement of the {c.dv} more accurate.", 1, 2)]
            r = [points_row("a", 2, [hz, prec], "Suggest", "Allow other sensible hazards with a matching precaution", "AO3"),
                 row_("b", accuracy(c), 1, "Accept any sensible method linked to this investigation", "AO3")]
            out.append(dict(parts=p, rows=r, refs=refs, cw="Suggest", diff="1-3", intro=c.intro, template=f"{nm}-prac-risk"))
    return out


def _make(sub):
    @reg(sub, "practical", f"{_short(sub)}-prac")
    def f():
        return gen_sub(sub)
    return f


for _s in CTX:
    _make(_s)
