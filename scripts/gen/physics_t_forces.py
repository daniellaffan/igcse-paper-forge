"""Topic 1: Forces and motion."""
import math

import physics_svg as S
from physics_util import (K, M, X, T, kb, calc_q, line_part, work_part, mcq_part, row, num, sf, clean, pick, nice,
                          calc_rows, eq_row, alts)

MO, FO, EL, MOM, MON = ("physics.forces.motion", "physics.forces.forces", "physics.forces.elasticity",
                        "physics.forces.momentum", "physics.forces.moments")

# ====================================================================== knowledge items
kb(MO, ["the motion of vehicles", "describing motion with graphs", "a cyclist on a journey", "objects moving in a straight line",
        "speed and acceleration"],
   mcq=[
       M("Which of these is the unit of acceleration?", ["m/s²", "m/s", "N/kg²", "m²/s"], "1.1 1.6", why="m/s is speed; the others are not units of acceleration"),
       M("What does the gradient of a distance-time graph show?", ["speed", "acceleration", "distance travelled", "force"], "1.3"),
       M("What does the area under a velocity-time graph represent?", ["distance travelled", "acceleration", "average speed", "time taken"], "1.9"),
       M("A velocity-time graph is a horizontal straight line above the time axis. What is the object doing?",
         ["moving at a constant velocity", "stationary", "accelerating uniformly", "decelerating"], "1.7"),
       M("Which quantity is a vector?", ["velocity", "speed", "distance", "time"], "1.3 1.6", d="4-6"),
       M("A distance-time graph is a horizontal line. What can you say about the object?",
         ["it is stationary", "it has constant non-zero speed", "it is accelerating", "it is decelerating"], "1.3"),
       M("A car's velocity falls from 20 m/s to 8 m/s in 4 s. What is its acceleration?",
         ["-3 m/s²", "-2 m/s²", "3 m/s²", "7 m/s²"], "1.6", d="4-6", ordered=True, ao="AO2"),
       M("Which unit is a correct unit for speed?", ["km/h", "m/s²", "N/m", "kg m"], "1.1"),
       M("On a velocity-time graph, a straight line with a negative gradient shows",
         ["uniform deceleration", "uniform acceleration", "constant velocity", "an object at rest"], "1.7 1.8"),
   ],
   recall=[
       K("State the equation linking average speed, distance moved and time taken.", 1,
         ["average speed = distance moved ÷ time taken | allow s = d/t, v = d/t; allow rearrangements"], "1.4", cmd="State"),
       K("State the equation linking acceleration, change in velocity and time taken.", 1,
         ["acceleration = change in velocity ÷ time taken | allow a = (v-u)/t; allow rearrangements"], "1.6", cmd="State"),
       K("Give the unit of acceleration.", 1, ["m/s² | allow m s⁻²; reject m/s"], "1.1", cmd="Give"),
       K("State what is meant by the term *acceleration*.", 1, ["rate of change of velocity | allow change in velocity per unit time; condone speed for velocity"], "1.6", cmd="State"),
       K("State what quantity is given by the gradient of a velocity-time graph.", 1, ["acceleration | allow deceleration for a negative gradient"], "1.8", cmd="State"),
       K("State what quantity is given by the area under a velocity-time graph.", 1, ["distance (travelled) | allow displacement"], "1.9", cmd="State"),
       K("Name **two** pieces of measuring equipment needed to find the average speed of a toy car rolling across a floor.", 2,
         ["metre rule / tape measure | allow ruler", "stopwatch / timer | allow light gates and data logger"], "1.5", cmd="Name"),
       K("Give the difference between speed and velocity.", 1, ["velocity has a direction but speed does not | allow velocity is a vector and speed is a scalar"], "1.3 1.6", cmd="Give", d="4-6"),
   ],
   describe=[
       K("Describe how the gradient of a distance-time graph can be used to find the speed of an object.", 2,
         ["choose two points far apart on the line / draw a tangent", "speed = change in distance ÷ change in time (gradient) | allow rise over run"], "1.3", cmd="Describe"),
       K("Describe how the motion of an object is shown on a distance-time graph when it speeds up.", 2,
         ["the line curves upwards | allow the graph gets steeper", "because the gradient (speed) increases"], "1.3", cmd="Describe", d="4-6"),
       K("Describe how a velocity-time graph can be used to find the distance travelled by an object.", 2,
         ["find the area between the line and the time axis", "split into rectangles/triangles and add the areas | allow counting squares and multiplying by the value of one square"], "1.9", cmd="Describe"),
       K("Describe how a student could use light gates to measure the speed of a trolley as it passes a point.", 3,
         ["fix a card of known length to the trolley | allow interrupt card", "light gate/data logger records the time the beam is blocked",
          "speed = length of card ÷ time | allow data logger calculates the speed",
          "measure the card length with a ruler"], "1.5", cmd="Describe", d="4-6", ao="AO3"),
       K("Describe the motion shown by a velocity-time graph that starts at the origin, rises as a straight line, then becomes horizontal.", 3,
         ["starts from rest", "uniform/constant acceleration", "then constant velocity | allow steady speed"], "1.7", cmd="Describe"),
       K("Describe what a curved line on a velocity-time graph that gets less steep shows about the motion.", 2,
         ["velocity increasing", "acceleration decreasing"], "1.7 1.8", cmd="Describe", d="4-6"),
   ])

kb(FO, ["forces on vehicles", "falling objects", "road safety", "forces and their effects", "the forces acting on a skydiver",
        "weight on different planets"],
   mcq=[
       M("Which of these is a scalar quantity?", ["mass", "force", "velocity", "weight"], "1.13"),
       M("Which of these is a vector quantity?", ["force", "energy", "speed", "mass"], "1.13 1.14"),
       M("Which force always opposes the motion of an object sliding across a surface?", ["friction", "weight", "upthrust", "magnetic force"], "1.16"),
       M("A 2 kg object has a resultant force of 8 N acting on it. What is its acceleration?", ["4 m/s²", "0.25 m/s²", "10 m/s²", "16 m/s²"],
         "1.17", ao="AO2", d="1-3"),
       M("A skydiver is falling at terminal velocity. Which statement is correct?",
         ["the air resistance equals the weight", "the air resistance is zero", "the weight is greater than the air resistance", "the skydiver is accelerating"], "1.21", d="4-6"),
       M("Which of these increases the thinking distance of a driver?", ["drinking alcohol", "worn tyres", "a wet road", "a heavier car"], "1.20", d="4-6"),
       M("Which of these increases the braking distance but not the thinking distance?", ["an icy road", "tiredness", "using a mobile phone", "taking drugs"], "1.20", d="4-6"),
       M("Which force acts between two charged balloons?", ["electrostatic", "gravitational only", "friction", "tension"], "1.12"),
       M("What is the weight of a 5.0 kg bag on Earth (g = 10 N/kg)?", ["50 N", "0.5 N", "5.0 N", "15 N"], "1.18", ordered=False, ao="AO2"),
   ],
   recall=[
       K("State **two** effects a force can have on an object.", 2, ["change its speed", "change its direction", "change its shape | allow deform/stretch/squash"], "1.11", cmd="State"),
       K("State the difference between a vector and a scalar quantity.", 1, ["a vector has a direction (and size) but a scalar has only a size | allow magnitude for size"], "1.13", cmd="State"),
       K("Give **two** examples of vector quantities.", 2, ["force | allow named force e.g. weight", "velocity", "acceleration", "momentum", "displacement"], "1.13 1.14", cmd="Give"),
       K("State the equation linking weight, mass and gravitational field strength.", 1, ["weight = mass × gravitational field strength | allow W = m × g"], "1.18", cmd="State"),
       K("State the equation linking unbalanced force, mass and acceleration.", 1, ["force = mass × acceleration | allow F = m × a"], "1.17", cmd="State"),
       K("State what is meant by the *stopping distance* of a car.", 1, ["thinking distance + braking distance | allow the total distance travelled from seeing a hazard to stopping"], "1.19", cmd="State"),
       K("Give **two** factors that increase the braking distance of a car.", 2, ["higher speed", "greater mass | allow more passengers/load", "wet or icy road", "worn tyres", "worn brakes"], "1.20", cmd="Give"),
       K("Give **two** factors that increase the thinking distance of a driver.", 2, ["higher speed", "tiredness", "alcohol / drugs", "distractions | allow using a phone"], "1.20", cmd="Give"),
       K("Name the type of force that acts between the Earth and the Moon.", 1, ["gravitational | allow gravity; reject gravitational potential"], "1.12", cmd="Name"),
   ],
   describe=[
       K("Describe how the forces on a falling skydiver change from the moment she leaves the aircraft until she reaches terminal velocity.", 3,
         ["weight stays the same | allow weight is constant", "air resistance increases as speed increases", "until air resistance equals weight"], "1.21", cmd="Describe", d="4-6"),
       K("Describe what happens to the thinking distance and the braking distance when a car travels faster.", 2,
         ["thinking distance increases (in proportion to speed)", "braking distance increases (by more than the thinking distance)"], "1.20", cmd="Describe"),
       K("Describe how a resultant force can be found when two forces act on an object along the same line.", 2,
         ["add the forces if they act in the same direction", "subtract the smaller from the larger if they act in opposite directions"], "1.15", cmd="Describe"),
       K("Describe the effect of friction on a box being pushed across a floor.", 2, ["friction acts in the opposite direction to the motion", "reduces the resultant force / acceleration | allow box slows down when pushing stops"], "1.16", cmd="Describe"),
   ],
   explain=[
       K("Explain why a falling object eventually reaches a terminal velocity.", 3,
         ["air resistance/drag increases with speed", "until drag equals weight | allow forces balance", "so resultant force is zero (and acceleration is zero)"], "1.21", cmd="Explain", d="4-6"),
       K("Explain why a skydiver slows down when the parachute opens.", 3,
         ["parachute has a larger (surface) area", "so air resistance increases", "air resistance becomes greater than weight so resultant force is upwards"], "1.21", cmd="Explain", d="4-6"),
       K("Explain why a car travelling on an icy road needs a greater stopping distance.", 2,
         ["less friction between tyres and road", "so a smaller braking force/deceleration, so braking distance increases"], "1.20", cmd="Explain"),
       K("Explain why an object has the same mass on the Moon but a smaller weight.", 2,
         ["mass is the amount of matter and does not depend on location", "weight depends on g, which is smaller on the Moon"], "1.18", cmd="Explain", d="4-6"),
       K("Explain why a tired driver is more likely to have an accident.", 2, ["longer reaction time", "so thinking distance (and stopping distance) increases"], "1.20", cmd="Explain"),
       K("Explain why a heavily loaded lorry takes longer to stop than an empty one travelling at the same speed with the same braking force.", 2,
         ["greater mass", "so smaller deceleration for the same force (a = F/m), so braking distance is greater"], "1.17 1.20", cmd="Explain", d="7-9", ao="AO2"),
   ],
   extended=[
       X("Explain the motion of a skydiver from the moment she jumps from a stationary balloon until she lands, after opening her parachute part of the way down.",
         ["at the start, speed is zero so there is no air resistance", "the resultant force is her weight, so she accelerates (at about 10 m/s²)",
          "as speed increases, air resistance increases", "resultant force decreases so acceleration decreases",
          "air resistance becomes equal to weight; resultant force is zero", "she falls at a (first) terminal velocity",
          "when the parachute opens the area increases so air resistance increases greatly", "air resistance is greater than weight, resultant force upwards, she decelerates",
          "air resistance decreases as she slows until it again equals weight", "a new lower terminal velocity is reached before landing"], "1.21 1.11"),
       X("Discuss the factors that affect the stopping distance of a car. Your answer should refer to thinking distance and braking distance.",
         ["stopping distance = thinking distance + braking distance", "thinking distance increases with speed",
          "thinking distance increases with longer reaction time", "tiredness, alcohol, drugs and distractions increase reaction time",
          "braking distance increases with speed (roughly with speed squared)", "greater mass increases braking distance (smaller deceleration)",
          "wet or icy roads reduce friction and increase braking distance", "worn tyres or brakes increase braking distance",
          "weather/road conditions do not affect thinking distance"], "1.19 1.20", title="Stopping distance"),
       X("A ball bearing is dropped into a tall tube of oil. Explain how the forces on the ball bearing change as it falls, and why it reaches a constant speed.",
         ["weight acts downwards and stays constant", "drag/viscous force acts upwards, opposing motion", "upthrust may also act upwards",
          "at first drag is small so resultant force is downwards and it accelerates", "drag increases as speed increases",
          "resultant force decreases, so acceleration decreases", "eventually drag (+ upthrust) equals weight", "resultant force zero, so no acceleration",
          "ball moves at terminal velocity"], "1.21 1.16"),
   ])

kb(EL, ["stretching springs", "elastic materials", "investigating rubber bands", "force-extension graphs"],
   mcq=[
       M("A spring obeys Hooke's law. What happens to its extension when the force on it is doubled?", ["it doubles", "it halves", "it stays the same", "it increases four times"], "1.23", d="4-6"),
       M("Which word describes a material that returns to its original shape when the force is removed?", ["elastic", "plastic", "brittle", "rigid"], "1.24"),
       M("The extension of a spring is", ["its stretched length minus its original length", "its stretched length", "its original length", "its stretched length plus its original length"], "1.22"),
       M("Which part of a force-extension graph shows Hooke's law?", ["the initial straight-line section through the origin", "the curved section at large forces", "the horizontal section", "any part of the graph"], "1.23"),
       M("A spring extends by 3.0 cm with a load of 2.0 N. It obeys Hooke's law. What load gives an extension of 7.5 cm?", ["5.0 N", "4.5 N", "11 N", "2.8 N"], "1.23", ao="AO2", d="4-6"),
       M("Which piece of apparatus is used to measure the extension of a spring?", ["metre rule", "newtonmeter", "stopwatch", "top-pan balance"], "1.22"),
   ],
   recall=[
       K("State Hooke's law.", 1, ["extension is (directly) proportional to the force/load | allow up to the limit of proportionality"], "1.23", cmd="State"),
       K("State what is meant by *elastic behaviour*.", 1, ["the material returns to its original shape/length when the force is removed"], "1.24", cmd="State"),
       K("Give **one** safety precaution when stretching a spring by hanging masses on it.", 1,
         ["wear eye protection / goggles | allow safety glasses", "place a tray/soft mat under the masses | allow keep feet clear", "clamp the stand to the bench"], "1.22", cmd="Give"),
       K("State how to calculate the extension of a spring from length measurements.", 1, ["extension = new length - original length"], "1.22", cmd="State"),
       K("Name the point on a force-extension graph beyond which the graph is no longer a straight line.", 1, ["limit of proportionality | allow elastic limit"], "1.23", cmd="Name", d="4-6"),
   ],
   explain=[
       K("Explain how the force-extension graph of a spring shows that it obeys Hooke's law.", 2,
         ["straight line", "passing through the origin"], "1.23", cmd="Explain"),
       K("Explain why a rubber band does not obey Hooke's law.", 2, ["its force-extension graph is curved / not a straight line", "so extension is not proportional to force"], "1.22 1.23", cmd="Explain", d="4-6"),
       K("Explain why a spring that has been stretched beyond its limit of proportionality may not return to its original length.", 2,
         ["it has been permanently deformed | allow behaved plastically", "so it no longer shows elastic behaviour"], "1.24", cmd="Explain", d="7-9"),
       K("Explain why a student should read the pointer on the ruler with her eye level with the pointer.", 2,
         ["to avoid parallax error", "so the reading of length/extension is accurate"], "1.22", cmd="Explain", ao="AO3"),
       K("Explain why the student should wait a few seconds after adding each mass before measuring the length of the spring.", 2,
         ["the spring may be oscillating/bouncing", "so the reading is taken when it is stationary and more accurate"], "1.22", cmd="Explain", ao="AO3", d="4-6"),
   ])

kb(MOM, ["momentum in collisions", "car safety features", "rocket and recoil motion", "Newton's third law", "sports and momentum"],
   mcq=[
       M("What is the unit of momentum?", ["kg m/s", "N/m", "kg m/s²", "J/s"], "1.2P 1.25P"),
       M("A 0.50 kg ball moves at 6.0 m/s. What is its momentum?", ["3.0 kg m/s", "12 kg m/s", "0.083 kg m/s", "9.0 kg m/s"], "1.25P", ao="AO2"),
       M("Which statement about a collision between two trolleys with no external forces is correct?",
         ["total momentum before equals total momentum after", "total kinetic energy always stays the same", "the faster trolley always stops", "momentum is lost as heat"], "1.27P", d="4-6"),
       M("An airbag reduces injury in a crash because it", ["increases the time taken for the head to stop", "reduces the change in momentum of the head",
                                                           "increases the force on the head", "increases the speed of the head"], "1.26P", d="4-6"),
       M("A book rests on a table. The Newton's third law partner of the Earth's pull on the book is", ["the book's pull on the Earth", "the table's push on the book",
                                                                                                    "the book's push on the table", "the Earth's pull on the table"], "1.29P", d="7-9"),
       M("A force of 20 N acts on a trolley for 3.0 s. What is the change in momentum?", ["60 kg m/s", "6.7 kg m/s", "23 kg m/s", "0.15 kg m/s"], "1.28P", ao="AO2", d="4-6"),
       M("Momentum is a vector. This means it", ["has a direction as well as a size", "can never be zero", "is always conserved in every situation", "is measured in newtons"], "1.25P"),
   ],
   recall=[
       K("State the equation linking momentum, mass and velocity.", 1, ["momentum = mass × velocity | allow p = m × v"], "1.25P", cmd="State"),
       K("State the principle of conservation of momentum.", 2, ["total momentum (of a system) stays the same", "provided no external/resultant force acts | allow in a closed system; allow momentum before = momentum after"], "1.27P", cmd="State", d="4-6"),
       K("State Newton's third law.", 2, ["when two bodies interact they exert forces on each other that are equal (in size)", "and opposite (in direction) | allow act on different bodies"], "1.29P", cmd="State"),
       K("Give the unit of momentum.", 1, ["kg m/s | allow N s"], "1.2P", cmd="Give"),
       K("Name **two** car safety features that work by increasing the time taken for a passenger to stop.", 2, ["seat belt", "airbag", "crumple zone", "collapsible steering column | allow head restraint"], "1.26P", cmd="Name"),
   ],
   explain=[
       K("Explain how a crumple zone reduces the force on passengers in a crash.", 3,
         ["crumple zone increases the time of the collision", "for the same change in momentum", "force = change in momentum ÷ time, so the force is smaller"], "1.26P 1.28P", cmd="Explain", d="4-6"),
       K("Explain why a gun recoils when a bullet is fired.", 3, ["momentum before firing is zero", "bullet gains momentum forwards", "gun gains equal momentum backwards so total stays zero"], "1.27P", cmd="Explain", d="4-6"),
       K("Explain why a cycle helmet with a soft, crushable lining reduces injury when a cyclist's head hits the ground.", 3,
         ["lining squashes so head takes longer to stop", "change in momentum is the same", "so the force on the head is smaller (F = Δp/t)"], "1.26P 1.28P", cmd="Explain", d="4-6"),
       K("A swimmer pushes backwards on the water. Use Newton's third law to explain why she moves forwards.", 2,
         ["water pushes forwards on the swimmer", "with a force equal in size and opposite in direction"], "1.29P", cmd="Explain"),
       K("Explain why a goalkeeper pulls her hands back when catching a fast ball.", 2,
         ["increases the time taken to stop the ball", "so smaller force for the same change in momentum"], "1.26P 1.28P", cmd="Explain"),
       K("Explain why a rocket accelerates upwards when it pushes exhaust gases downwards.", 2,
         ["gases gain downward momentum", "rocket gains equal upward momentum | allow gases push up on the rocket with an equal and opposite force"], "1.27P 1.29P", cmd="Explain", d="4-6"),
   ])

kb(MON, ["turning effects of forces", "balancing beams", "levers and spanners", "centre of gravity", "see-saws and cranes"],
   mcq=[
       M("What is the unit of a moment?", ["N m", "N/m", "kg m/s", "J/s"], "1.2P 1.30P"),
       M("A force of 30 N acts 0.40 m from a pivot. What is the moment?", ["12 N m", "75 N m", "0.013 N m", "30 N m"], "1.30P", ao="AO2"),
       M("An object is balanced. Which statement is correct?", ["the sum of clockwise moments equals the sum of anticlockwise moments", "all forces act at the pivot",
                                                              "the clockwise moments are bigger", "there are no forces acting"], "1.32P"),
       M("A heavy load moves from the centre of a beam towards its right-hand support. What happens to the force from the right-hand support?",
         ["it increases", "it decreases", "it stays the same", "it becomes zero"], "1.33P", d="7-9"),
       M("The weight of an object can be thought of as acting at its", ["centre of gravity", "pivot", "lowest point", "edge"], "1.31P"),
       M("It is easier to undo a tight nut with a long spanner because", ["the same force gives a larger moment", "the force needed is larger", "the moment is smaller", "the pivot moves"], "1.30P", d="4-6"),
   ],
   recall=[
       K("State the equation linking moment, force and perpendicular distance from the pivot.", 1, ["moment = force × perpendicular distance (from the pivot) | reject distance without 'from the pivot' only if 'perpendicular' also missing"], "1.30P", cmd="State"),
       K("State the principle of moments.", 2, ["for an object in equilibrium / balanced", "sum of clockwise moments = sum of anticlockwise moments (about any point)"], "1.32P", cmd="State"),
       K("State what is meant by the *centre of gravity* of an object.", 1, ["the point through which the weight (of the object) acts"], "1.31P", cmd="State"),
       K("Give the unit of a moment.", 1, ["N m | allow newton metre; reject J"], "1.2P", cmd="Give"),
       K("State **two** ways of increasing the moment of a force about a pivot.", 2, ["increase the force", "increase the (perpendicular) distance from the pivot", "apply the force at 90° to the lever"], "1.30P", cmd="State"),
   ],
   explain=[
       K("Explain why a door handle is placed at the edge of the door furthest from the hinges.", 2, ["largest distance from pivot/hinge", "so a smaller force gives the moment needed"], "1.30P", cmd="Explain"),
       K("Explain why a crane has a heavy counterweight on the opposite side of the tower from the load.", 3,
         ["the load produces a moment about the tower/pivot", "the counterweight produces a moment in the opposite direction", "so moments balance and the crane does not topple"], "1.32P", cmd="Explain", d="4-6"),
       K("A plank rests on two supports, one at each end. A person walks from the left end to the right end. Explain how the force on each support changes.", 3,
         ["force on the right support increases", "force on the left support decreases", "because the moment of the person's weight about the other support changes as the distance changes | allow sum of support forces stays equal to total weight"], "1.33P", cmd="Explain", d="7-9", ao="AO2"),
       K("Explain how you could find the centre of gravity of a uniform metre rule by balancing it.", 2, ["balance the rule on a pivot/knife edge", "the centre of gravity is directly above the balance point"], "1.31P", cmd="Explain", ao="AO3"),
       K("Explain why a lorry with a high load is more likely to topple over on a slope.", 3,
         ["centre of gravity is higher", "line of action of weight moves outside the base sooner", "weight produces a moment that turns it over"], "1.31P 1.32P", cmd="Explain", d="7-9"),
   ])

# ====================================================================== motion: calculations

SPEED_CTX = [("cyclist", "rides", (1.2, 9.6, 0.1), "km", (8, 40, 1), "minutes"),
             ("train", "travels", (12, 96, 1), "km", (10, 55, 1), "minutes"),
             ("runner", "runs", (400, 10000, 100), "m", (60, 2400, 30), "s"),
             ("drone", "flies", (300, 2400, 50), "m", (40, 300, 5), "s"),
             ("ferry", "sails", (6, 45, 1), "km", (20, 90, 5), "minutes"),
             ("snail", "crawls", (12, 60, 2), "cm", (2, 10, 1), "minutes")]


@T(MO, "calc", 8, "mo-speed")
def mo_speed(r):
    who, verb, drange, du, trange, tu = pick(r, SPEED_CTX)
    d = nice(r, *drange)
    t = nice(r, *trange)
    dm = d * {"km": 1000, "m": 1, "cm": 0.01}[du]
    ts = t * (60 if tu == "minutes" else 1)
    v = dm / ts
    ask_unit = r.random() < 0.5 and (du != "m" or tu != "s")
    intro = f"A {who} {verb} {clean(d)} {du} in {clean(t)} {tu}."
    if ask_unit:
        text = "Calculate the average speed of the " + who + " in m/s."
        working = [f"distance = {clean(dm)} m, time = {clean(ts)} s", f"speed = {clean(dm)} ÷ {clean(ts)}"]
        q = calc_q(intro=intro, text=text, eq="average speed = distance ÷ time", working=working, ans=num(v, 2), unit="m/s",
                   prefix="average speed (m/s) = ", refs=["1.4", "1.1"], d="4-6", rearr=False,
                   values={"distance_m": dm, "time_s": ts, "speed_ms": v}, notes=alts(v) + "; conversion of units is needed for full marks")
        q["parts"][-1]["marks"] = 3
        q["rows"].insert(1, row(q["rows"][0]["part"], "conversion to metres and seconds;", 1))
    else:
        # rearrangement: find time from speed and distance
        text = f"Another {who} moves at an average speed of {num(v * 1.25, 2)} m/s over the same distance. Calculate the time it takes, in seconds."
        v2 = float(num(v * 1.25, 2))
        t2 = dm / v2
        q = calc_q(intro=intro, text=text, eq="average speed = distance ÷ time",
                   working=[f"{num(v2, 2)} = {clean(dm)} ÷ time", f"time = {clean(dm)} ÷ {num(v2, 2)}"], ans=num(t2, 3), unit="s",
                   prefix="time (s) = ", refs=["1.4"], d="4-6", values={"distance_m": dm, "speed": v2, "time_s": t2}, notes=alts(t2),
                   state=("average speed, distance moved and time taken", "average speed = distance moved ÷ time taken", None))
    return q


@T(MO, "calc", 7, "mo-accel")
def mo_accel(r):
    ctx = pick(r, [("car", 0, 35), ("motorcycle", 0, 40), ("train", 5, 60), ("sprinter", 0, 11), ("bus", 2, 18), ("lift", 0, 4), ("aircraft", 10, 80)])
    who, lo, hi = ctx
    u = r.randint(lo, max(lo, hi // 3))
    v = r.randint(u + 2, hi) if hi - u > 2 else hi
    t = nice(r, 1.5, 25, 0.5)
    a = (v - u) / t
    mode = r.choice(["a", "a", "t", "v"])
    intro = f"A {who} accelerates uniformly from {u} m/s to {v} m/s in {clean(t)} s." if mode == "a" else \
        f"A {who} accelerates uniformly at {num(a, 2)} m/s²."
    if mode == "a":
        return calc_q(intro=intro, text=f"Calculate the acceleration of the {who}.", eq="a = (v − u) ÷ t",
                      working=[f"a = ({v} − {u}) ÷ {clean(t)}"], ans=num(a, 2), unit="m/s²", prefix="acceleration (m/s²) = ",
                      refs=["1.6"], d="1-3", rearr=False, values={"u": u, "v": v, "t": t, "a": a}, notes=alts(a),
                      state=("acceleration, change in velocity and time taken", "acceleration = change in velocity ÷ time taken", None))
    a2 = float(num(a, 2))
    if mode == "t":
        tt = (v - u) / a2
        return calc_q(intro=intro, text=f"Calculate the time it takes for the {who} to go from {u} m/s to {v} m/s.", eq="a = (v − u) ÷ t",
                      working=[f"{num(a2, 2)} = ({v} − {u}) ÷ t", f"t = ({v} − {u}) ÷ {num(a2, 2)}"], ans=num(tt, 2), unit="s",
                      prefix="time (s) = ", refs=["1.6"], d="4-6", values={"u": u, "v": v, "a": a2, "t": tt}, notes=alts(tt))
    vv = u + a2 * t
    return calc_q(intro=intro + f" Its initial velocity is {u} m/s.", text=f"Calculate the velocity of the {who} after {clean(t)} s.",
                  eq="a = (v − u) ÷ t", working=[f"{num(a2, 2)} = (v − {u}) ÷ {clean(t)}", f"v = {u} + ({num(a2, 2)} × {clean(t)})"],
                  ans=num(vv, 3), unit="m/s", prefix="velocity (m/s) = ", refs=["1.6"], d="4-6",
                  values={"u": u, "a": a2, "t": t, "v": vv}, notes=alts(vv))


@T(MO, "calc", 7, "mo-suvat")
def mo_suvat(r):
    mode = r.choice(["s", "a", "v", "v0"])
    who = pick(r, ["a cyclist", "a car", "a skateboarder", "a stone dropped from a bridge", "a trolley on a ramp", "a jet on a runway", "a lift"])
    if mode == "s":
        u, v = r.randint(0, 6), r.randint(10, 30)
        a = nice(r, 0.5, 4.0, 0.5)
        s = (v * v - u * u) / (2 * a)
        return calc_q(intro=f"{who.capitalize()} accelerates uniformly at {clean(a)} m/s² from {u} m/s to {v} m/s.",
                      text="Calculate the distance travelled while it accelerates.", eq="v² = u² + 2as",
                      working=[f"{v}² = {u}² + (2 × {clean(a)} × s)", f"s = ({v}² − {u}²) ÷ (2 × {clean(a)})"], ans=num(s, 3), unit="m",
                      prefix="distance (m) = ", refs=["1.10"], d="4-6", values={"u": u, "v": v, "a": a, "s": s}, notes=alts(s))
    if mode == "a":
        u, v = r.randint(12, 32), 0
        s = r.randint(15, 90)
        a = (v * v - u * u) / (2 * s)
        return calc_q(intro=f"{who.capitalize()} travelling at {u} m/s brakes uniformly and stops in a distance of {s} m.",
                      text="Calculate the deceleration.", eq="v² = u² + 2as",
                      working=[f"0 = {u}² + (2 × a × {s})", f"a = −{u}² ÷ (2 × {s})"], ans=num(-a, 2), unit="m/s²",
                      prefix="deceleration (m/s²) = ", refs=["1.10"], d="7-9", values={"u": u, "s": s, "a": a},
                      notes=alts(-a) + "; allow a negative value for acceleration")
    if mode == "v":
        h = nice(r, 1.8, 45, 0.2)
        v = math.sqrt(2 * 10 * h)
        return calc_q(intro=f"A ball is dropped from rest from a height of {clean(h)} m. Ignore air resistance. The acceleration of free fall is 10 m/s².",
                      text="Calculate the speed of the ball just before it hits the ground.", eq="v² = u² + 2as",
                      working=[f"v² = 0² + (2 × 10 × {clean(h)})", f"v = √{clean(2 * 10 * h)}"], ans=num(v, 3), unit="m/s",
                      prefix="speed (m/s) = ", refs=["1.10"], d="4-6", values={"h": h, "v": v}, notes=alts(v))
    v = r.randint(20, 70)
    a = nice(r, 1.0, 3.0, 0.5)
    s = r.randint(300, 1500)
    u2 = v * v - 2 * a * s
    if u2 < 0:
        return None
    u = math.sqrt(u2)
    return calc_q(intro=f"An aircraft accelerates uniformly at {clean(a)} m/s² along a runway of length {s} m and reaches {v} m/s at the end.",
                  text="Calculate its speed at the start of the runway.", eq="v² = u² + 2as",
                  working=[f"{v}² = u² + (2 × {clean(a)} × {s})", f"u = √({v}² − 2 × {clean(a)} × {s})"], ans=num(u, 3), unit="m/s",
                  prefix="initial speed (m/s) = ", refs=["1.10"], d="7-9", values={"v": v, "a": a, "s": s, "u": u}, notes=alts(u))


# ====================================================================== motion: practical

@T(MO, "practical", 13, "mo-prac-ramp")
def mo_prac(r):
    obj = pick(r, ["toy car", "tennis ball", "marble", "trolley", "cylinder"])
    d = nice(r, 0.80, 2.40, 0.05)
    base = d / nice(r, 0.6, 1.8, 0.05)
    times = [round(base + r.uniform(-0.06, 0.06), 2) for _ in range(3)]
    anomaly = r.random() < 0.5
    if anomaly:
        k = r.randrange(3)
        times[k] = round(times[k] + pick(r, [0.4, 0.5, -0.35]), 2)
    good = [t for i, t in enumerate(times) if not (anomaly and i == k)]
    mean = sum(good) / len(good)
    v = d / mean
    intro = (f"A student investigates the motion of a {obj} rolling along the floor after it leaves a ramp.\n\n"
             f"She marks two lines on the floor {clean(d)} m apart and times the {obj} between the lines with a stopwatch. "
             "The table shows her results.")
    fig = {"type": "table", "headers": ["", "trial 1", "trial 2", "trial 3"],
           "rows": [["time in s"] + [f"{t:.2f}" for t in times]], "caption": "Time for the " + obj + " to travel between the lines"}
    parts, rows = [], []
    parts.append(line_part("a", "Suggest a suitable instrument for measuring the distance between the lines.", 1, 1))
    rows.append(row("(a)", "metre rule / tape measure;", 1, "allow trundle wheel; reject ruler on its own if 30 cm specified", "AO3"))
    if anomaly:
        parts.append(work_part("b", "Calculate the mean time, ignoring any anomalous result.", 2, "mean time (s) = "))
        rows += [row("(b)", f"anomalous value ({times[k]:.2f} s) excluded;", 1, None, "AO3"),
                 row("(b)", f"mean = {sf(mean, 3)} (s);", 1, "allow 2 or more s.f.; ecf if wrong value excluded", "AO3")]
    else:
        parts.append(work_part("b", "Calculate the mean time.", 1, "mean time (s) = "))
        rows.append(row("(b)", f"mean = {sf(mean, 3)} (s);", 1, "allow 2 or more s.f.", "AO3"))
    parts.append(work_part("c", f"Calculate the average speed of the {obj} between the lines.", 2, "average speed (m/s) = "))
    rows += [row("(c)", f"substitution into speed = distance ÷ time, e.g. {clean(d)} ÷ {sf(mean, 3)};", 1, "allow ecf from (b)", "AO2"),
             row("(c)", f"evaluation: {num(v, 2)} (m/s);", 1, alts(v), "AO2")]
    parts.append(line_part("d", "Explain **one** way the student could make her timing more accurate.", 2, 3))
    rows.append(row("(d)", "any two from:\nMP1. use light gates (and data logger);\nMP2. which remove human reaction time;\nMP3. use a longer distance between the lines;\nMP4. so the reaction time is a smaller fraction of the total time;\nMP5. repeat and calculate a mean;\nMP6. to reduce the effect of random errors;", 2,
                    "explanation must match the method suggested", "AO3"))
    return dict(parts=parts, rows=rows, refs=["1.5", "1.4"], cmd="Calculate", d="4-6", ao=["AO2", "AO3"], intro=intro, figures=[fig],
                answer={"method": "python", "values": {"times": times, "mean": mean, "speed": v}, "checked": True})


# ====================================================================== motion: data / graphs

@T(MO, "data", 7, "mo-dt-graph")
def mo_dt(r):
    who = pick(r, ["a jogger", "a delivery robot", "a model boat", "a cyclist", "a walker"])
    t1 = r.choice([20, 30, 40])
    v1 = nice(r, 1.0, 4.0, 0.5)
    d1 = v1 * t1
    t2 = t1 + r.choice([10, 20])
    t3 = t2 + r.choice([20, 30, 40])
    d3 = d1 + nice(r, 20, 80, 10)
    pts = [(0, 0), (t1, d1), (t2, d1), (t3, d3)]
    ymax = math.ceil(d3 / 20) * 20 + 20
    xmax = math.ceil(t3 / 20) * 20
    fig = {"type": "svg", "svg": S.graph(xmax, ymax, "time in s", "distance in m", series=[{"pts": pts, "join": True, "marker": None}]),
           "width": 120, "caption": f"Distance-time graph for {who}"}
    v3 = (d3 - d1) / (t3 - t2)
    parts = [line_part("a", f"Describe the motion of {who} between {t1} s and {t2} s.", 1, 1),
             work_part("b", f"Use the graph to determine the speed of {who} during the first {t1} s.", 2, "speed (m/s) = "),
             line_part("c", f"State how the graph shows that {who} moved faster in the first section than in the last section.", 1, 1),
             work_part("d", f"Calculate the average speed of {who} for the whole journey.", 2, "average speed (m/s) = ")]
    vav = d3 / t3
    faster = v1 > v3
    rows = [row("(a)", "stationary / not moving;", 1, "allow at rest", "AO3"),
            row("(b)", f"use of gradient, e.g. {clean(d1)} ÷ {t1};", 1, None, "AO3"),
            row("(b)", f"{num(v1, 2)} (m/s);", 1, None, "AO2"),
            row("(c)", ("first section is steeper / has a greater gradient;" if faster else
                        "the first section is less steep, so actually it moved more slowly at first;"), 1,
                "answer must refer to gradient or steepness", "AO3"),
            row("(d)", f"total distance ÷ total time, e.g. {clean(d3)} ÷ {t3};", 1, None, "AO2"),
            row("(d)", f"{num(vav, 2)} (m/s);", 1, alts(vav), "AO2")]
    if not faster:
        parts[2]["text"] = f"State how the graph shows whether {who} moved faster in the first section or in the last section."
        rows[3] = row("(c)", "last section is steeper / has a greater gradient (so faster at the end);", 1, "answer must refer to gradient or steepness", "AO3")
    return dict(parts=parts, rows=rows, refs=["1.3", "1.4"], cmd="Determine", d="4-6", ao=["AO2", "AO3"], figures=[fig],
                intro=f"The graph shows how the distance travelled by {who} changes with time.",
                answer={"method": "python", "values": {"v1": v1, "v3": v3, "vav": vav}, "checked": True})


@T(MO, "data", 7, "mo-vt-graph")
def mo_vt(r):
    who = pick(r, ["a car", "a tram", "a bus", "an electric scooter", "a lift", "a train"])
    v = r.choice([8, 10, 12, 15, 16, 20, 24])
    t1 = r.choice([4, 5, 8, 10])
    t2 = t1 + r.choice([10, 15, 20])
    t3 = t2 + r.choice([4, 5, 6, 8, 10])
    pts = [(0, 0), (t1, v), (t2, v), (t3, 0)]
    a1 = v / t1
    dist = 0.5 * t1 * v + (t2 - t1) * v + 0.5 * (t3 - t2) * v
    xmax = math.ceil(t3 / 5) * 5
    ymax = math.ceil((v + 2) / 5) * 5
    fig = {"type": "svg", "svg": S.graph(xmax, ymax, "time in s", "velocity in m/s", series=[{"pts": pts, "join": True, "marker": None}]),
           "width": 120, "caption": f"Velocity-time graph for {who}"}
    parts = [work_part("a", f"Determine the acceleration of {who} in the first {t1} s.", 2, "acceleration (m/s²) = "),
             work_part("b", f"Determine the total distance travelled by {who}.", 3, "distance (m) = "),
             line_part("c", f"Describe the motion of {who} between {t2} s and {t3} s.", 2, 2)]
    rows = [row("(a)", f"gradient = change in velocity ÷ time, e.g. {v} ÷ {t1};", 1, None, "AO3"),
            row("(a)", f"{num(a1, 2)} (m/s²);", 1, None, "AO2"),
            row("(b)", "use of area under the graph;", 1, "e.g. splitting into two triangles and a rectangle", "AO3"),
            row("(b)", f"correct areas, e.g. ½ × {t1} × {v} + {t2 - t1} × {v} + ½ × {t3 - t2} × {v};", 1, None, "AO2"),
            row("(b)", f"{clean(dist)} (m);", 1, None, "AO2"),
            row("(c)", "(uniform) deceleration;", 1, "allow slowing down at a constant rate", "AO3"),
            row("(c)", f"comes to rest at {t3} s;", 1, f"allow from {v} m/s to 0", "AO3")]
    return dict(parts=parts, rows=rows, refs=["1.7", "1.8", "1.9"], cmd="Determine", d="4-6", ao=["AO2", "AO3"], figures=[fig],
                intro=f"The graph shows how the velocity of {who} changes during a short journey.",
                answer={"method": "python", "values": {"a": a1, "distance": dist}, "checked": True})


@T(MO, "data", 6, "mo-plot")
def mo_plot(r):
    a = nice(r, 0.4, 2.0, 0.2)
    u = r.choice([0, 0, 1, 2])
    ts = [0, 2, 4, 6, 8, 10]
    vs = [round(u + a * t + r.uniform(-0.15, 0.15), 1) for t in ts]
    vs[0] = float(u)
    tq = r.choice([3, 5, 7, 9])
    vq = u + a * tq
    fig = {"type": "table", "headers": ["time in s"] + [str(t) for t in ts], "rows": [["velocity in m/s"] + [f"{v:.1f}" for v in vs]],
           "caption": "Velocity of a trolley rolling down a slope"}
    parts = [{"label": "a", "text": "Plot a graph of velocity against time on the grid. Draw the line of best fit.", "marks": 4, "space": "graph"},
             work_part("b", "Use your graph to determine the acceleration of the trolley.", 2, "acceleration (m/s²) = "),
             line_part("c", f"Use your graph to find the velocity of the trolley at {tq} s.", 1, 1, prefix="velocity = ")]
    rows = [row("(a)", "suitable linear scales chosen (points occupy more than half the grid);", 1, "ignore orientation", "AO3"),
            row("(a)", "axes labelled with quantities and units;", 1, None, "AO3"),
            row("(a)", "all points plotted correctly to the nearest half square;", 1, "-1 for each plotting error", "AO3"),
            row("(a)", "straight line of best fit;", 1, "judge by eye; reject dot-to-dot", "AO3"),
            row("(b)", "gradient calculated using a large triangle on the line;", 1, None, "AO3"),
            row("(b)", f"value in range {sf(a * 0.93, 2)} to {sf(a * 1.07, 2)} (m/s²);", 1, f"expected {sf(a, 2)}", "AO2"),
            row("(c)", f"value in range {sf(vq - 0.3, 2)} to {sf(vq + 0.3, 2)} (m/s);", 1, "allow ecf from candidate's line", "AO3")]
    return dict(parts=parts, rows=rows, refs=["1.7", "1.8"], cmd="Plot", d="4-6", ao=["AO3"], figures=[fig],
                intro="A student releases a trolley at the top of a long slope and uses a data logger to record its velocity every 2 s.",
                answer={"method": "python", "values": {"a": a, "v_at": vq, "data": vs}, "checked": True})


# ====================================================================== forces: calculations and diagrams

@T(FO, "calc", 5, "fo-fma")
def fo_fma(r):
    who = pick(r, [("car", 900, 1600, 50), ("van", 1800, 3200, 100), ("trolley", 0.5, 2.5, 0.1), ("cyclist and bicycle", 60, 110, 5),
                   ("rocket", 2000, 9000, 500), ("shopping cart", 12, 40, 1)])
    name, lo, hi, st = who
    m = nice(r, lo, hi, st)
    drive = nice(r, m * 1.5, m * 4, st if st >= 1 else 0.1) if m > 5 else nice(r, 2, 8, 0.5)
    fric = round(drive * r.uniform(0.2, 0.6), 0 if drive > 20 else 1)
    res = drive - fric
    a = res / m
    intro = f"A {name} of mass {clean(m)} kg has a driving force of {clean(drive)} N acting forwards and a resistive force of {clean(fric)} N acting backwards."
    pre = [line_part("a", f"Calculate the resultant force on the {name}.", 1, 1, prefix="resultant force = ")]
    prer = [row("(a)", f"{clean(res)} (N) (forwards);", 1, "allow ecf in (b)", "AO2")]
    q = calc_q(intro=intro, text=f"Calculate the acceleration of the {name}.", eq="F = m × a",
               working=[f"{clean(res)} = {clean(m)} × a", f"a = {clean(res)} ÷ {clean(m)}"], ans=num(a, 2), unit="m/s²",
               prefix="acceleration (m/s²) = ", refs=["1.15", "1.17"], d="4-6", values={"m": m, "F": res, "a": a},
               notes=alts(a) + "; allow ecf from (a)", pre_parts=pre, pre_rows=prer)
    return q


@T(FO, "calc", 4, "fo-weight")
def fo_weight(r):
    body, g = pick(r, [("the Moon", 1.6), ("Mars", 3.7), ("Jupiter", 25), ("Venus", 8.9), ("Mercury", 3.7), ("Titan", 1.4)])
    obj = pick(r, ["an astronaut", "a rover", "a science probe", "a lander", "a robot"])
    m = nice(r, 60, 950, 5)
    w_e = m * 10
    w_b = m * g
    mode = r.choice(["w", "m"])
    if mode == "w":
        return calc_q(intro=f"{obj.capitalize()} has a mass of {clean(m)} kg. The gravitational field strength on {body} is {clean(g)} N/kg.",
                      text=f"Calculate the weight of {obj} on {body}.", eq="W = m × g", working=[f"W = {clean(m)} × {clean(g)}"],
                      ans=num(w_b, 3), unit="N", prefix="weight (N) = ", refs=["1.18"], d="1-3", rearr=False,
                      values={"m": m, "g": g, "W": w_b}, notes=alts(w_b),
                      state=("weight, mass and gravitational field strength", "weight = mass × gravitational field strength", None))
    return calc_q(intro=f"{obj.capitalize()} has a weight of {clean(w_b)} N on {body}, where the gravitational field strength is {clean(g)} N/kg.",
                  text=f"Calculate the mass of {obj} and its weight on Earth (g = 10 N/kg). Give the weight on Earth as your answer.",
                  eq="W = m × g", working=[f"m = {clean(w_b)} ÷ {clean(g)} = {clean(m)} kg", f"W(Earth) = {clean(m)} × 10"],
                  ans=num(w_e, 3), unit="N", prefix="weight on Earth (N) = ", refs=["1.18"], d="7-9",
                  values={"m": m, "W_body": w_b, "W_earth": w_e}, notes="award the rearrangement mark for m = W ÷ g")


@T(FO, "calc", 4, "fo-stopping")
def fo_stop(r):
    v = r.choice([10, 12, 14, 15, 18, 20, 22, 25, 30])
    rt = nice(r, 0.5, 1.2, 0.1)
    br = round(v * v / (2 * nice(r, 5, 8, 0.5)), 0)
    think = v * rt
    stop = think + br
    intro = (f"A driver is travelling at {v} m/s when she sees a hazard. Her reaction time is {clean(rt)} s. "
             f"The braking distance of the car is {clean(br)} m.")
    pre = [work_part("a", "Calculate the thinking distance.", 2, "thinking distance (m) = ")]
    prer = [row("(a)", f"substitution into distance = speed × time, e.g. {v} × {clean(rt)};", 1),
            row("(a)", f"{num(think, 3)} (m);", 1)]
    parts = pre + [work_part("b", "Calculate the stopping distance of the car.", 1, "stopping distance (m) = "),
                   line_part("c", "The driver is very tired. State and explain the effect this has on the stopping distance.", 2, 2)]
    rows = prer + [row("(b)", f"{num(stop, 3)} (m);", 1, "allow ecf from (a): (a) + braking distance"),
                   row("(c)", "stopping distance increases;", 1),
                   row("(c)", "because reaction time and so thinking distance increases;", 1, "ignore braking distance changes")]
    return dict(parts=parts, rows=rows, refs=["1.19", "1.20", "1.4"], cmd="Calculate", d="4-6", ao=["AO1", "AO2"], intro=intro,
                answer={"method": "python", "values": {"thinking": think, "stopping": stop}, "checked": True})


FD_CASES = [
    ("car", "a car moving along a level road at a steady speed",
     ["driving force (forwards, equal length to drag)", "air resistance/friction (backwards)", "weight (down)", "reaction from road (up, equal to weight)"],
     "arrows for forward and backward forces drawn equal in length"),
    ("parachutist", "a parachutist falling at a constant speed",
     ["weight (downwards)", "air resistance/drag (upwards)"], "arrows equal in length because the speed is constant"),
    ("box", "a box resting on a table",
     ["weight (downwards)", "normal reaction/contact force from the table (upwards)"], "arrows equal in length, both starting on the box"),
    ("ball", "a ball that has just been thrown vertically upwards",
     ["weight (downwards)", "air resistance (downwards, opposing upward motion)"], "both arrows point down; no upward force once released"),
    ("car", "a car braking on a level road",
     ["friction/braking force (backwards)", "air resistance (backwards)", "weight (down)", "reaction (up)"], "no forward force drawn; backward forces shown"),
    ("box", "a crate being pushed across a rough floor at a steady speed",
     ["push (forwards)", "friction (backwards, equal length)", "weight (down)", "reaction (up)"], "push and friction arrows equal in length"),
]


@T(FO, "diagram", 13, "fo-force-diagram")
def fo_fd(r):
    obj, desc, forces, cond = pick(r, FD_CASES)
    k = min(len(forces), 2 if len(forces) == 2 else r.choice([2, 4]))
    fig = {"type": "svg", "svg": S.force_diagram(obj), "width": 70, "caption": desc.capitalize()}
    m = 2 if len(forces) == 2 else 3
    parts = [{"label": "a", "text": f"The diagram shows {desc}.\n\nOn the diagram, draw and label arrows to show the forces acting on the {obj}.", "marks": m, "space": "none"}]
    if m == 2:
        rows = [row("(a)", f"{forces[0]};", 1, "arrow must touch or start from the object"),
                row("(a)", f"{forces[1]} with {cond};", 1)]
    else:
        rows = [row("(a)", "any three from:\n" + "\n".join(f"MP{i + 1}. {f};" for i, f in enumerate(forces)) + f"\nMP{len(forces) + 1}. {cond};", 3,
                    "labels required for each arrow")]
    F1 = r.randint(200, 900)
    F2 = F1 + r.choice([-150, -80, 0, 60, 120])
    res = F1 - F2
    parts.append(line_part("b", f"At one moment the forward force is {F1} N and the backward force is {F2} N. Determine the size and direction of the resultant force.", 2, 1,
                           prefix="resultant force = "))
    if res == 0:
        rows += [row("(b)", "0 N;", 1), row("(b)", "no direction / forces balanced;", 1, "allow 'no resultant force'")]
    else:
        rows += [row("(b)", f"{abs(res)} N;", 1), row("(b)", "forwards;" if res > 0 else "backwards;", 1, "direction mark is independent")]
    return dict(parts=parts, rows=rows, refs=["1.11", "1.12", "1.15", "1.21"], cmd="Draw", d="4-6", ao=["AO1", "AO2"], figures=[fig],
                answer={"method": "python", "values": {"resultant": res}, "checked": True})


# ====================================================================== elasticity: practical and data

def spring_data(r, mat):
    if mat == "spring":
        k = nice(r, 8, 40, 2)  # N/m
        loads = [0, 1, 2, 3, 4, 5, 6]
        ext = [round(L / k * 100 + r.uniform(-0.15, 0.15), 1) for L in loads]
        ext[0] = 0.0
        lim = None
        if r.random() < 0.5:
            ext[-1] = round(ext[-1] + r.uniform(1.5, 3.0), 1)
            lim = 5
        return loads, ext, k, lim
    loads = [0, 1, 2, 3, 4, 5, 6]
    base = nice(r, 1.0, 2.5, 0.5)
    ext = [round(base * L * (1 + 0.18 * L) + r.uniform(-0.1, 0.1), 1) for L in loads]
    ext[0] = 0.0
    return loads, ext, None, None


@T(EL, "practical", 7, "el-prac-spring")
def el_prac(r):
    L0 = nice(r, 3.0, 9.0, 0.5)
    loads, ext, k, lim = spring_data(r, "spring")
    lengths = [round(L0 + e, 1) for e in ext]
    i = r.randint(2, 5)
    fig = {"type": "svg", "svg": S.spring_apparatus(), "width": 60, "caption": "Apparatus"}
    tab = {"type": "table", "headers": ["load in N"] + [str(x) for x in loads[:5]],
           "rows": [["length in cm"] + [f"{x:.1f}" for x in lengths[:5]]], "caption": "Results"}
    parts = [line_part("a", "State the independent variable and the dependent variable in this investigation.", 2, 2),
             line_part("b", "Give **one** variable that the student should keep constant.", 1, 1),
             work_part("c", f"Calculate the extension of the spring when the load is {loads[i]} N.", 1, "extension (cm) = "),
             line_part("d", "Describe how the student can make sure that her length measurements are accurate.", 2, 3)]
    rows = [row("(a)", "independent: load / force / weight (added);", 1, None, "AO3"),
            row("(a)", "dependent: length / extension (of the spring);", 1, None, "AO3"),
            row("(b)", "the same spring / temperature / same type of masses;", 1, "accept any one sensible control", "AO3"),
            row("(c)", f"{lengths[i]:.1f} − {L0:.1f} = {lengths[i] - L0:.1f} (cm);", 1, None, "AO2") if i < 5 else
            row("(c)", f"{lengths[i]:.1f} − {L0:.1f} = {lengths[i] - L0:.1f} (cm);", 1, None, "AO2"),
            row("(d)", "any two from:\nMP1. eye level with the pointer/bottom of spring;\nMP2. use a fixed pointer/marker attached to the spring;\nMP3. ruler vertical / clamped next to spring;\nMP4. wait until the spring stops moving;\nMP5. repeat readings and find a mean;", 2, "allow use of set square", "AO3")]
    if i >= 5:
        tab["headers"] = ["load in N"] + [str(x) for x in loads[:i + 1]]
        tab["rows"] = [["length in cm"] + [f"{x:.1f}" for x in lengths[:i + 1]]]
    return dict(parts=parts, rows=rows, refs=["1.22"], cmd="State", d="1-3" if r.random() < 0.5 else "4-6", ao=["AO3", "AO2"],
                intro=f"A student investigates how the length of a spring changes as she hangs loads on it. The original length of the spring is {L0:.1f} cm.",
                figures=[fig, tab], answer={"method": "python", "values": {"extension": lengths[i] - L0}, "checked": True})


@T(EL, "practical", 6, "el-prac-band")
def el_band(r):
    mat = pick(r, ["rubber band", "length of fishing line", "strip of polythene", "thin copper wire"])
    parts = [line_part("a", f"Describe a method the student could use to investigate how the extension of a {mat} depends on the force applied to it.", 4, 6),
             line_part("b", "State **one** hazard in this investigation and how to reduce the risk.", 2, 2),
             line_part("c", "Suggest why the student should take readings both as the load is increased and as it is removed.", 1, 2)]
    rows = [row("(a)", "any four from:\nMP1. clamp one end / hang from a clamp stand;\nMP2. measure the original length with a ruler;\nMP3. add masses/weights in equal steps;\nMP4. measure the new length each time;\nMP5. extension = new length − original length;\nMP6. use a marker and read at eye level;\nMP7. repeat and calculate means;", 4,
                "marks can be awarded from a labelled diagram", "AO3"),
            row("(b)", f"hazard: the {mat} may snap and fly back / masses may fall;", 1, None, "AO3"),
            row("(b)", "precaution: wear goggles / put a tray or cushion below the masses;", 1, "precaution must match hazard", "AO3"),
            row("(c)", "to see if it returns to its original length (elastic behaviour) | allow to check for permanent stretching;", 1, None, "AO3")]
    return dict(parts=parts, rows=rows, refs=["1.22", "1.24"], cmd="Describe", d="4-6", ao=["AO3"],
                intro=f"A student wants to find out whether a {mat} behaves like a spring. She has a set of {pick(r, ['50 g', '100 g', '20 g'])} slotted masses, a clamp stand and a {pick(r, ['metre rule', '30 cm ruler', 'half-metre rule'])}.",
                answer={"method": "none", "values": {}, "checked": True})


@T(EL, "data", 13, "el-data")
def el_data(r):
    mat = r.choice(["spring", "spring", "rubber band"])
    loads, ext, k, lim = spring_data(r, mat)
    tab = {"type": "table", "headers": ["force in N"] + [str(x) for x in loads], "rows": [["extension in cm"] + [f"{x:.1f}" for x in ext]],
           "caption": f"Results for a {mat}"}
    parts = [{"label": "a", "text": "Plot a graph of extension against force. Draw the line or curve of best fit.", "marks": 4, "space": "graph"}]
    rows = [row("(a)", "suitable linear scales (points occupy more than half the grid);", 1, None, "AO3"),
            row("(a)", "axes labelled with quantities and units;", 1, None, "AO3"),
            row("(a)", "all points plotted to the nearest half square;", 1, None, "AO3"),
            row("(a)", "line/curve of best fit;" if mat == "spring" else "smooth curve of best fit;", 1, "reject dot-to-dot", "AO3")]
    if mat == "spring":
        Fq = pick(r, [1.5, 2.5, 3.5])
        eq = Fq / k * 100
        parts.append(line_part("b", f"Use your graph to find the extension when the force is {Fq} N.", 1, 1, prefix="extension = "))
        rows.append(row("(b)", f"{sf(eq - 0.2, 2)} to {sf(eq + 0.2, 2)} (cm);", 1, "allow ecf from line", "AO3"))
        if lim:
            parts.append(line_part("c", "State the force at which the spring stops obeying Hooke's law. Give a reason for your answer.", 2, 2))
            rows += [row("(c)", "(about) 5 N;", 1, "allow between 5 and 6 N", "AO3"), row("(c)", "the graph stops being a straight line after this point;", 1, None, "AO3")]
        else:
            parts.append(line_part("c", "Explain whether the spring obeys Hooke's law.", 2, 2))
            rows += [row("(c)", "yes, it obeys Hooke's law;", 1, None, "AO3"), row("(c)", "straight line through the origin / extension proportional to force;", 1, None, "AO3")]
        vals = {"k_N_per_m": k, "e_at": eq}
    else:
        parts.append(line_part("b", "Explain whether the rubber band obeys Hooke's law.", 2, 2))
        rows += [row("(b)", "no;", 1, None, "AO3"), row("(b)", "graph is curved / extension not proportional to force;", 1, None, "AO3")]
        vals = {"data": ext}
    return dict(parts=parts, rows=rows, refs=["1.22", "1.23"], cmd="Plot", d="4-6", ao=["AO3"], figures=[tab],
                intro=f"A student measures the extension of a {mat} for different forces.",
                answer={"method": "python", "values": vals, "checked": True})


# ====================================================================== momentum

@T(MOM, "calc", 4, "mom-p")
def mom_p(r):
    obj, lo, hi, st, vlo, vhi = pick(r, [("tennis ball", 0.055, 0.060, 0.001, 20, 55), ("lorry", 9000, 40000, 500, 8, 25), ("sprinter", 55, 90, 1, 6, 10),
                                         ("bullet", 0.004, 0.012, 0.001, 300, 900), ("hockey puck", 0.15, 0.17, 0.01, 10, 40), ("ship", 2.0e6, 8.0e6, 0.5e6, 3, 12)])
    m = nice(r, lo, hi, st)
    v = r.randint(vlo, vhi)
    p = m * v
    mode = r.choice(["p", "v"])
    if mode == "p":
        return calc_q(intro=f"A {obj} of mass {num(m, 3)} kg moves at {v} m/s.", text=f"Calculate the momentum of the {obj}.", eq="p = m × v",
                      working=[f"p = {num(m, 3)} × {v}"], ans=num(p, 3), unit="kg m/s", prefix="momentum (kg m/s) = ", refs=["1.25P", "1.2P"],
                      d="1-3", rearr=False, values={"m": m, "v": v, "p": p}, notes=alts(p),
                      state=("momentum, mass and velocity", "momentum = mass × velocity", None))
    return calc_q(intro=f"A {obj} of mass {num(m, 3)} kg has a momentum of {num(p, 3)} kg m/s.", text=f"Calculate the velocity of the {obj}.",
                  eq="p = m × v", working=[f"{num(p, 3)} = {num(m, 3)} × v", f"v = {num(p, 3)} ÷ {num(m, 3)}"], ans=num(v, 3), unit="m/s",
                  prefix="velocity (m/s) = ", refs=["1.25P"], d="4-6", values={"m": m, "p": p, "v": v}, notes=alts(v))


@T(MOM, "calc", 5, "mom-collide")
def mom_collide(r):
    kind = r.choice(["stick", "stick", "recoil", "chase"])
    if kind == "stick":
        a, b = pick(r, [("trolley A", "trolley B"), ("railway wagon", "stationary wagon"), ("ice skater", "stationary skater"), ("car", "stationary van")])
        m1 = nice(r, 0.5, 3.0, 0.1) if "trolley" in a else nice(r, 50, 2000, 10)
        m2 = nice(r, 0.5, 3.0, 0.1) if "trolley" in a else nice(r, 50, 2500, 10)
        u1 = nice(r, 0.5, 6, 0.5) if "trolley" in a else nice(r, 2, 20, 1)
        v = m1 * u1 / (m1 + m2)
        intro = f"A {a} of mass {clean(m1)} kg moving at {clean(u1)} m/s collides with a {b} of mass {clean(m2)} kg at rest. They join together and move off together."
        return calc_q(intro=intro, text="Calculate the velocity of the two objects just after the collision.", eq="conservation of momentum (p = m × v)",
                      working=[f"momentum before = {clean(m1)} × {clean(u1)} = {num(m1 * u1, 4)} kg m/s", f"{num(m1 * u1, 4)} = ({clean(m1)} + {clean(m2)}) × v",
                               f"v = {num(m1 * u1, 4)} ÷ {clean(m1 + m2)}"], ans=num(v, 3), unit="m/s", prefix="velocity (m/s) = ",
                      refs=["1.27P", "1.25P"], d="7-9", values={"m1": m1, "m2": m2, "u1": u1, "v": v}, notes=alts(v) + "; allow ecf for momentum before",
                      ao=("AO2",))
    if kind == "recoil":
        gun, shot = pick(r, [("cannon", "cannonball"), ("rifle", "bullet"), ("toy launcher", "foam dart"), ("skater pushing off a wall", None)])
        if shot is None:
            return None
        M_ = {"cannon": nice(r, 400, 1500, 50), "rifle": nice(r, 3.0, 5.0, 0.5), "toy launcher": nice(r, 0.2, 0.6, 0.05)}[gun]
        m = {"cannon": nice(r, 4, 15, 1), "rifle": nice(r, 0.008, 0.015, 0.001), "toy launcher": nice(r, 0.005, 0.02, 0.001)}[gun]
        vb = {"cannon": r.randint(80, 200), "rifle": r.randint(400, 900), "toy launcher": r.randint(8, 20)}[gun]
        V = m * vb / M_
        intro = f"A {gun} of mass {num(M_, 3)} kg fires a {shot} of mass {num(m, 3)} kg at {vb} m/s. The {gun} is free to move and is initially at rest."
        return calc_q(intro=intro, text=f"Calculate the recoil velocity of the {gun}.", eq="conservation of momentum (p = m × v)",
                      working=["total momentum before = 0", f"{num(m, 3)} × {vb} = {num(M_, 3)} × V", f"V = {num(m * vb, 4)} ÷ {num(M_, 3)}"],
                      ans=num(V, 2), unit="m/s", prefix="recoil velocity (m/s) = ", refs=["1.27P"], d="7-9",
                      values={"M": M_, "m": m, "v": vb, "V": V}, notes=alts(V) + "; ignore sign")
    m1, m2 = nice(r, 0.5, 2.0, 0.1), nice(r, 0.5, 2.0, 0.1)
    u1, u2 = nice(r, 2, 5, 0.5), nice(r, 0.5, 1.5, 0.5)
    v2 = nice(r, u2 + 1, u1 + 1, 0.5)
    v1 = (m1 * u1 + m2 * u2 - m2 * v2) / m1
    if v1 < 0:
        return None
    intro = (f"Trolley P (mass {clean(m1)} kg) moves at {clean(u1)} m/s and catches up with trolley Q (mass {clean(m2)} kg) moving at {clean(u2)} m/s in the same direction. "
             f"After the collision Q moves at {clean(v2)} m/s.")
    return calc_q(intro=intro, text="Calculate the velocity of P after the collision.", eq="conservation of momentum",
                  working=[f"{clean(m1)} × {clean(u1)} + {clean(m2)} × {clean(u2)} = {clean(m1)} × v + {clean(m2)} × {clean(v2)}",
                           f"v = ({num(m1 * u1 + m2 * u2, 4)} − {num(m2 * v2, 4)}) ÷ {clean(m1)}"], ans=num(v1, 2), unit="m/s",
                  prefix="velocity of P (m/s) = ", refs=["1.27P"], d="7-9", values={"v1": v1}, notes=alts(v1))


@T(MOM, "calc", 5, "mom-force")
def mom_force(r):
    ctx = pick(r, [("a footballer kicks a ball", 0.43, 0, (15, 30), (0.008, 0.02)), ("a car crashes into a barrier", 1200, (12, 25), 0, (0.08, 0.3)),
                   ("a golf club hits a ball", 0.046, 0, (40, 70), (0.0005, 0.002)), ("a tennis racket returns a ball", 0.058, -20, (25, 45), (0.003, 0.008)),
                   ("a crash-test dummy is stopped by an airbag", 70, (10, 18), 0, (0.05, 0.2))])
    desc, m, u, v, tr = ctx
    m = m if isinstance(m, (int, float)) else m
    u = r.randint(*u) if isinstance(u, tuple) else u
    v = r.randint(*v) if isinstance(v, tuple) else v
    t = round(r.uniform(*tr), 4)
    t = float(sf(t, 2))
    dp = m * (v - u)
    F = dp / t
    intro = f"In a test, {desc}. The mass is {clean(m)} kg, the velocity changes from {u} m/s to {v} m/s and the contact time is {num(t, 2)} s."
    return calc_q(intro=intro, text="Calculate the size of the average force.", eq="F = (mv − mu) ÷ t",
                  working=[f"F = ({clean(m)} × {v} − {clean(m)} × {u}) ÷ {num(t, 2)}"], ans=num(abs(F), 2), unit="N",
                  prefix="force (N) = ", refs=["1.28P"], d="7-9" if u < 0 else "4-6", rearr=False,
                  values={"m": m, "u": u, "v": v, "t": t, "F": abs(F)}, notes=alts(abs(F)) + "; ignore sign")


# ====================================================================== moments

@T(MON, "calc", 5, "mon-moment")
def mon_moment(r):
    obj = pick(r, ["spanner", "door handle", "wheelbarrow", "crowbar", "bottle opener", "tap"])
    F = nice(r, 5, 300, 5)
    d = nice(r, 0.05, 1.5, 0.05)
    Mm = F * d
    mode = r.choice(["M", "F", "dcm"])
    if mode == "M":
        return calc_q(intro=f"A force of {clean(F)} N is applied at right angles to a {obj}, {clean(d)} m from the pivot.",
                      text="Calculate the moment of the force about the pivot.", eq="moment = force × perpendicular distance",
                      working=[f"moment = {clean(F)} × {clean(d)}"], ans=num(Mm, 3), unit="N m", prefix="moment (N m) = ",
                      refs=["1.30P", "1.2P"], d="1-3", rearr=False, values={"F": F, "d": d, "moment": Mm}, notes=alts(Mm),
                      state=("moment, force and perpendicular distance from the pivot", "moment = force × perpendicular distance from the pivot", None))
    if mode == "F":
        return calc_q(intro=f"A moment of {num(Mm, 3)} N m is needed to turn a {obj}. The force is applied at right angles, {clean(d)} m from the pivot.",
                      text="Calculate the force needed.", eq="moment = force × perpendicular distance",
                      working=[f"{num(Mm, 3)} = F × {clean(d)}", f"F = {num(Mm, 3)} ÷ {clean(d)}"], ans=num(F, 3), unit="N",
                      prefix="force (N) = ", refs=["1.30P"], d="4-6", values={"moment": Mm, "d": d, "F": F}, notes=alts(F))
    dcm = d * 100
    return calc_q(intro=f"A force of {clean(F)} N acting at right angles to a {obj} produces a moment of {num(Mm, 3)} N m.",
                  text="Calculate the perpendicular distance of the force from the pivot. Give your answer in centimetres.",
                  eq="moment = force × perpendicular distance", working=[f"d = {num(Mm, 3)} ÷ {clean(F)} = {clean(d)} m", f"d = {clean(dcm)} cm"],
                  ans=clean(dcm), unit="cm", prefix="distance (cm) = ", refs=["1.30P"], d="7-9", values={"d_cm": dcm},
                  notes="answer must be in cm for the evaluation mark")


@T(MON, "calc", 4, "mon-balance")
def mon_balance(r):
    W1 = nice(r, 1, 8, 0.5)
    d1 = r.choice([10, 15, 20, 25, 30, 35, 40])
    d2 = r.choice([x for x in (10, 15, 20, 25, 30, 35, 40, 45) if x != d1])
    W2 = W1 * d1 / d2
    fig = {"type": "svg", "svg": S.beam(50, [(50 - d1, f"{clean(W1)} N", "down"), (50 + d2, "W", "down")], length=100), "width": 110,
           "caption": "Metre rule balanced at its centre", "note": "Diagram NOT accurately drawn"}
    return calc_q(intro=f"A uniform metre rule is balanced on a pivot at its 50 cm mark. A weight of {clean(W1)} N hangs {d1} cm to the left of the pivot and an unknown weight W hangs {d2} cm to the right.",
                  text="Calculate the weight W.", eq="principle of moments", working=[f"{clean(W1)} × {d1} = W × {d2}", f"W = {num(W1 * d1, 4)} ÷ {d2}"],
                  ans=num(W2, 3), unit="N", prefix="W (N) = ", refs=["1.32P", "1.30P"], d="4-6", values={"W1": W1, "d1": d1, "d2": d2, "W": W2},
                  notes=alts(W2) + "; distances may be in m or cm if consistent", figs=[fig])


@T(MON, "calc", 4, "mon-beam")
def mon_beam(r):
    Lb = r.choice([4, 5, 6, 8, 10])
    Wl = nice(r, 200, 1500, 50)
    x = nice(r, 0.5, Lb - 0.5, 0.5)
    if x == Lb / 2:
        return None
    Fr = Wl * x / Lb
    Fl = Wl - Fr
    fig = {"type": "svg", "svg": S.beam(0, [(x, f"{clean(Wl)} N", "down"), (0.1, "X", "up"), (Lb - 0.1, "Y", "up")], length=Lb, support="ends"),
           "width": 110, "caption": "Light beam on two supports", "note": "Diagram NOT accurately drawn"}
    q = calc_q(intro=f"A light plank of length {Lb} m rests on supports X and Y at its ends. A load of weight {clean(Wl)} N is placed {clean(x)} m from X.",
               text="Take moments about X to calculate the upward force from support Y.", eq="principle of moments",
               working=[f"Y × {Lb} = {clean(Wl)} × {clean(x)}", f"Y = {num(Wl * x, 4)} ÷ {Lb}"], ans=num(Fr, 3), unit="N", prefix="force from Y (N) = ",
               refs=["1.32P", "1.33P"], d="7-9", values={"Y": Fr, "X": Fl}, notes=alts(Fr), figs=[fig])
    q["parts"].append(line_part("b", "Calculate the upward force from support X.", 1, 1, prefix="force from X (N) = "))
    q["parts"][0]["label"] = "a"
    for rw in q["rows"]:
        rw["part"] = "(a)"
    q["rows"].append(row("(b)", f"{num(Fl, 3)} (N);", 1, "allow ecf: total weight − answer to (a)"))
    return q


@T(MON, "practical", 13, "mon-prac")
def mon_prac(r):
    W = nice(r, 1.0, 3.0, 0.5)
    rows_ = []
    for _ in range(4):
        d1 = r.choice([10, 15, 20, 25, 30, 40])
        W2 = nice(r, 0.5, 4.0, 0.5)
        d2 = W * d1 / W2
        if d2 > 48 or d2 < 4:
            continue
        meas = round(d2 + r.uniform(-0.4, 0.4), 1)
        rows_.append((d1, W2, meas))
    if len(rows_) < 3:
        return None
    rows_ = rows_[:3]
    tab = {"type": "table", "headers": ["distance of " + clean(W) + " N weight from pivot in cm", "second weight in N", "balance distance of second weight in cm"],
           "rows": [[str(a), clean(b), f"{c:.1f}"] for a, b, c in rows_], "caption": "Results"}
    d1, W2, meas = rows_[0]
    cw = W2 * meas
    acw = W * d1
    parts = [line_part("a", "State **two** variables the student must measure for each balance.", 2, 2),
             work_part("b", "Use the first row of results to calculate the anticlockwise and the clockwise moments. Comment on whether the results support the principle of moments.", 3, ""),
             line_part("c", "Suggest **one** reason why the two moments are not exactly equal.", 1, 2),
             line_part("d", "Suggest **one** improvement to the experiment.", 1, 2)]
    rows = [row("(a)", "distance of each weight from the pivot;", 1, None, "AO3"), row("(a)", "the size of each weight (or mass);", 1, None, "AO3"),
            row("(b)", f"{clean(W)} × {d1} = {clean(acw)} (N cm);", 1, "allow in N m", "AO2"),
            row("(b)", f"{clean(W2)} × {meas:.1f} = {sf(cw, 3)} (N cm);", 1, None, "AO2"),
            row("(b)", "values are (approximately) equal so support the principle;", 1, "conclusion must follow from candidate's values", "AO3"),
            row("(c)", "difficult to judge exact balance / rule not uniform / hanging thread has width / reading error;", 1, None, "AO3"),
            row("(d)", "use a pointer and read at eye level / thinner thread or knife-edge loops / repeat and average;", 1, None, "AO3")]
    return dict(parts=parts, rows=rows, refs=["1.32P", "1.30P"], cmd="Calculate", d="4-6", ao=["AO2", "AO3"], figures=[tab],
                intro=f"A student balances a metre rule at its centre. She hangs a {clean(W)} N weight on one side and moves a second weight on the other side until the rule balances.",
                answer={"method": "python", "values": {"acw": acw, "cw": cw}, "checked": True})
