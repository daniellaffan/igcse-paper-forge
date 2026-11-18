"""Paper 2 Question 1: article comprehension.

Each item is an original article (our own writing) with numbered lines, followed by 8-9 parts that
mix line-referenced recall, suggest, an MCQ, a calculation using figures from the text, own-knowledge
explanations and an experimental-design part, totalling 16-18 marks.  Line numbers are computed after
wrapping, from markers «key» placed in the text; part texts refer to them as {L:key} or {L:a-b}.
"""
import random
import re
import textwrap

from biology_lib import reg, text_part, calc_part, row_, points_row, mcq_part, nf, sfig

HOST = "variety.characteristics"   # synoptic qtype: hosted in one subtopic, refs span the specification
WIDTH = 82


def wrap(text):
    lines, marks = [], {}
    for para in text.strip().split("\n\n"):
        para = " ".join(para.split())
        for ln in textwrap.wrap(para, WIDTH):
            for k in re.findall(r"«(\w+)»", ln):
                marks[k] = len(lines) + 1
            lines.append(re.sub(r"«\w+»", "", ln))
        lines.append("")
    while lines and not lines[-1]:
        lines.pop()
    # line number = count of non-empty lines up to that point (matches the site renderer)
    num, real = {}, 0
    out_idx = {}
    for i, l in enumerate(lines):
        if l.strip():
            real += 1
        out_idx[i + 1] = real
    marks = {k: out_idx[v] for k, v in marks.items()}
    return "\n".join(lines), marks


def lref(text, marks):
    def sub(m):
        key = m.group(1)
        if "-" in key:
            a, b = key.split("-")
            return f"lines {marks[a]} to {max(marks[b], marks[a] + 1)}"
        return f"line {marks[key]}"
    return re.sub(r"\{L:([\w-]+)\}", sub, text)


# part builders ------------------------------------------------------------
def PT(text, marks, pts, refs, cw="Explain", notes=None):
    return ("pt", text, marks, pts, refs, cw, notes)


def RW(text, marks, answer, refs, notes=None):
    return ("rw", text, marks, answer, refs, notes)


def MC(stem, correct, dists, refs):
    return ("mc", stem, correct, dists, refs)


def CA(text, marks, prefix, suffix, steps, final, refs, values, method):
    return ("ca", text, marks, prefix, suffix, steps, final, refs, values, method)


ARTICLES = []


def art(slug, title, text, parts):
    ARTICLES.append((slug, title, text, parts))


# 1 ---------------------------------------------------------------------------
pc1 = (2940 - 680) / 2940 * 100
art("dengue", "Bacteria against dengue", """
Dengue fever is caused by a virus that is passed to humans when they are bitten by female Aedes mosquitoes.
«sympt»Infected people develop a high temperature, severe headaches and pain in their joints, and in a small
number of cases the disease causes internal bleeding. There is no drug that kills the virus, so doctors can
only treat the symptoms.

Scientists have found a way to reduce the spread of dengue that does not rely on insecticides. «wolb»Wolbachia
is a bacterium that lives inside the cells of many insects but is not naturally found in Aedes mosquitoes.
When Wolbachia is introduced into the eggs of these mosquitoes, the adults that develop are much less able to
carry the dengue virus. «inherit»The bacterium is passed from a female mosquito to all of her offspring through
the cytoplasm of her eggs.

«release»In one trial, mosquitoes carrying Wolbachia were released once a week for twelve weeks in half of the
districts of a city. The other districts received no mosquitoes. After two years, the number of people who
needed hospital treatment for dengue was recorded in both groups of districts. «results»In the districts where
no mosquitoes were released there were 2 940 cases per 100 000 people, compared with 680 cases per 100 000
people in the districts where Wolbachia mosquitoes were released.

The scientists also took blood samples from patients who arrived at clinics with a fever. «blood»The samples
were tested for antibodies against the dengue virus. Patients who turned out not to have dengue were used as a
comparison group, because they had visited the same clinics during the same months.

«eco»Some people were worried that releasing millions of mosquitoes would harm other organisms. Mosquito larvae
live in water and are eaten by fish and dragonfly larvae, and adult mosquitoes are food for birds and bats.
However, the released mosquitoes belong to the same species that already lived in the city, so the size of the
population does not stay higher for long.

«cost»The method is cheaper than repeated spraying with insecticide, which has to be carried out every few
months. «resist»Spraying also has the problem that some mosquitoes survive because they are resistant to the
insecticide, and these survivors produce the next generation. Wolbachia offers a long-lasting solution, because
once it is established in a population it remains there without further releases.

«future»Health workers expect dengue to become a problem in new places during the coming decades. Aedes mosquitoes breed in small pools of still water, such as rainwater trapped in old tyres, plant pots and blocked gutters, and warmer winters allow the adults to survive further from the equator. A mosquito that carries a pathogen from one person to another in this way is called a vector. Teams in several countries are now rearing Wolbachia mosquitoes in large numbers, and they are asking householders to report where the insects are seen so that the spread of the bacterium can be mapped.
""", [
    RW("Name the type of pathogen that causes dengue fever.", 1, "virus (1)", ["1.4"]),
    RW("State the word used in the article for an organism that carries a pathogen from one person to another ({L:future}).", 1, "vector (1)", ["1.4"]),
    MC("Wolbachia is a bacterium ({L:wolb}). Which structure is found in a bacterial cell?", "plasmids", ["a nucleus", "chloroplasts", "a cell wall made of chitin"], ["1.3"]),
    PT("Suggest why the bacterium is passed to all of the offspring of an infected female mosquito ({L:inherit}).", 2,
       ["every offspring develops from an egg / zygote", "the egg provides the cytoplasm of the zygote", "sperm do not carry Wolbachia / only the mother's cytoplasm is passed on"], ["3.2"], "Suggest"),
    CA("Calculate the percentage decrease in dengue cases in the districts where Wolbachia mosquitoes were released ({L:results}).\n\nGive your answer to one decimal place.",
       3, "percentage decrease = ", "%", ["2 940 − 680 = 2 260", "2 260 ÷ 2 940 × 100"], f"{pc1:.1f}%", ["1.4"], {"percent_decrease": round(pc1, 1)}, "(old − new)/old × 100"),
    PT("Explain why testing a blood sample for antibodies can show whether a person has been infected with dengue ({L:blood}).", 2,
       ["lymphocytes make antibodies when the virus / antigen enters the body", "antibodies are specific to the dengue antigen", "so they are only present after infection"], ["2.62"]),
    PT("Suggest why mosquitoes were released in only half of the districts ({L:release}).", 2,
       ["the other districts act as a control", "to compare the number of cases", "to show the fall is caused by Wolbachia and not by another factor, e.g. weather"], ["1.4"], "Suggest"),
    PT("Explain how mosquitoes become resistant to an insecticide ({L:resist}).", 3,
       ["a mutation gives some mosquitoes resistance", "insecticide kills non-resistant mosquitoes", "resistant mosquitoes survive and reproduce", "pass on the resistance allele", "resistant mosquitoes become more common over generations"], ["3.38"]),
    PT("Using information from the passage and your own knowledge, suggest how a large fall in the mosquito population could affect other organisms ({L:eco}).", 2,
       ["less food for fish / dragonfly larvae / birds / bats", "populations of these predators may fall", "organisms that compete with mosquitoes may increase", "fewer people / animals infected with diseases"], ["4.7"], "Suggest"),
])

# 2 ---------------------------------------------------------------------------
r2 = 830 / 230
pc2 = (30 - 8) / 8 * 100
art("seagrass", "Meadows under the sea", """
Seagrasses are flowering plants that live completely under the sea in shallow coastal water. «roots»They have
roots that anchor them in sand and mud, and long thin leaves that sway in the current. «flow»Unlike seaweeds,
seagrasses produce flowers, and their pollen is carried from one plant to another by moving water.

Seagrass meadows are among the most productive habitats on Earth. «photo»The leaves absorb light and take in
carbon dioxide dissolved in the sea water, and use them to make glucose. «store»Much of the carbon is stored in
the roots and in the mud beneath the meadow, where dead leaves and roots decay very slowly because the mud
contains little oxygen. Scientists estimate that one hectare of seagrass can store up to 830 kg of carbon each
year, compared with 230 kg for one hectare of tropical rainforest.

«habitat»The meadows also provide food and shelter for many animals. Young fish hide among the leaves from
predators, turtles and dugongs graze on the leaves, and crabs and snails feed on the small algae that grow on
the leaf surface.

However, seagrass meadows are disappearing at a rate of about 7% of their total area each year. «runoff»One
major cause is fertiliser that is washed into the sea from farmland after heavy rain. This leads to rapid
growth of algae in the water above the meadows. «anchor»Other causes include damage from boat anchors and the
building of harbours.

«restore»In one restoration project, volunteers collected seeds from a healthy meadow and scattered them over
an area of bare sea floor. «counts»After four years the area covered by seagrass had increased from 0 to 36
hectares, and the number of fish species recorded at the site had increased from 8 to 30. «frames»To check
the success of the project, divers placed square frames with sides of 0.5 m at random positions and counted
the seagrass shoots inside each frame.

«climate»Protecting seagrass is now seen as one way to slow climate change. As well as storing carbon, healthy
meadows reduce the energy of waves and protect coastlines from erosion.

«monitor»To follow the recovery of the meadows, divers swim along fixed lines across the sea bed every spring and record how much of the ground is covered by leaves. They also cut small samples of leaf to measure how quickly new growth is produced. Local fishing groups have agreed to keep boats out of the areas that are being restored, because anchors and nets tear up the roots. Scientists hope that, within twenty years, the replanted meadows will once again provide shelter for young fish and food for turtles and sea birds.
""", [
    RW("Name the process in which pollen is transferred from one flower to another ({L:flow}).", 1, "pollination (1)", ["3.3"], "Reject fertilisation"),
    RW("Write the balanced chemical symbol equation for photosynthesis ({L:photo}).", 2,
       "6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂\ncorrect formulae (1)\ncorrectly balanced (1)", ["2.19"], "Ignore light / chlorophyll written over the arrow"),
    PT("Explain why dead leaves decay very slowly in the mud ({L:store}).", 2,
       ["decomposers / bacteria need oxygen", "for aerobic respiration", "so decomposition is slow and carbon is not released as carbon dioxide"], ["4.10"]),
    CA("Calculate how many times more carbon is stored each year by one hectare of seagrass than by one hectare of tropical rainforest ({L:store}).\n\nGive your answer to two significant figures.",
       2, "", "times", ["830 ÷ 230"], f"{sfig(r2, 2)} times", ["4.10"], {"ratio": float(sfig(r2, 2))}, "830/230"),
    PT("Explain how fertiliser washed into the sea could cause seagrass to die ({L:runoff}).", 3,
       ["fertiliser adds nitrate / phosphate ions to the water", "algae grow rapidly / algal bloom", "algae block light from reaching the seagrass", "less photosynthesis in seagrass", "decomposers use up oxygen when algae die"], ["4.17"]),
    CA("Calculate the percentage increase in the number of fish species recorded at the site ({L:counts}).", 2,
       "percentage increase = ", "%", ["(30 − 8) ÷ 8 × 100"], f"{nf(pc2)}%", ["4.3B"], {"percent_increase": pc2}, "(new − old)/old × 100"),
    PT("Describe how the divers could use the frames to estimate the number of seagrass shoots in the 36 hectares ({L:frames}).", 3,
       ["place frames / quadrats at random", "count the shoots in each frame", "use many frames and calculate the mean number per frame", "each frame is 0.25 m²; multiply the mean by the number of frames that would fit in the area", "36 hectares = 360 000 m²"], ["4.2"], "Describe"),
    PT("Suggest why protecting seagrass meadows could help to slow climate change ({L:climate}).", 2,
       ["seagrass absorbs carbon dioxide for photosynthesis", "carbon is stored for a long time in the mud", "less carbon dioxide / greenhouse gas in the atmosphere", "less global warming"], ["4.15"], "Suggest"),
])

# 3 ---------------------------------------------------------------------------
art("lactose", "Milk and the adult gut", """
Milk contains a sugar called lactose. «lactase»To be absorbed, lactose must first be broken down into two smaller
sugars, glucose and galactose, by an enzyme called lactase. Lactase is made by cells lining the small intestine.
«baby»All healthy babies produce lactase, because milk is their only food for the first months of life.

«adult»In most mammals, including most humans, lactase production falls sharply after a child stops feeding on
milk. Adults who cannot make enough lactase are described as lactose intolerant. «symptoms»When they drink milk,
the lactose passes undigested into the large intestine. There, bacteria use the lactose for anaerobic
respiration and produce gases and acids that cause bloating and pain.

«persist»In some human populations, however, most adults continue to make lactase throughout their lives. This
feature is called lactase persistence. It is caused by a change in the DNA close to the lactase gene. «dominant»The
allele for lactase persistence (L) is dominant to the allele for lactase non-persistence (l).

«map»Lactase persistence is common in people whose ancestors kept cattle, goats or camels for milk. For example,
about 89% of adults in Denmark are lactase persistent, compared with about 5% of adults in China. «select»Scientists
think that when people first began to keep animals for milk, individuals who could digest lactose as adults had
an advantage. Milk is a good source of energy, protein and calcium, and in times of food shortage these
individuals were more likely to survive and have children.

«yoghurt»Lactose-intolerant people can often eat yoghurt and hard cheese without any symptoms. During yoghurt
making, Lactobacillus bacteria convert much of the lactose into lactic acid. «tablets»Lactase can also be bought
as tablets, which are swallowed just before a meal containing milk.

«test»Doctors can test for lactose intolerance by giving a patient a drink containing 50 g of lactose and
measuring the concentration of glucose in the blood every 30 minutes for two hours. In a person who makes
lactase, the blood glucose concentration rises by more than 1.1 mmol per dm³. In a lactose-intolerant person it
hardly rises at all.

«products»People who cannot digest lactose do not always have to avoid dairy foods altogether. In yoghurt and many hard cheeses, bacteria have already broken down much of the lactose during manufacture, so these foods cause fewer symptoms. Some supermarkets also sell milk to which the enzyme lactase has been added at the factory. Doctors advise people who cut out dairy foods completely to find other sources of calcium, such as green leafy vegetables, nuts and fish with soft bones, because calcium is needed for healthy bones and teeth throughout life.
""", [
    RW("Name the type of biological molecule that lactase is ({L:lactase}).", 1, "enzyme / protein (1)", ["2.10"]),
    PT("Lactase works well at 37 °C but not at 60 °C. Explain why.", 2,
       ["37 °C is close to the optimum temperature", "at 60 °C the enzyme is denatured", "the active site changes shape so lactose no longer fits"], ["2.11"]),
    RW("Two parents are both heterozygous (Ll) for lactase persistence ({L:dominant}).\n\nUse a genetic diagram to find the probability that their child will be lactase non-persistent.", 3,
       "gametes L and l from each parent (1)\noffspring LL, Ll, Ll, ll (1)\nprobability 1/4 / 25% / 0.25 (1)", ["3.23", "3.25"], "Allow full marks for the correct probability with a correct Punnett square; reject 1 : 3"),
    MC("Which term describes the genotype Ll?", "heterozygous", ["homozygous dominant", "homozygous recessive", "codominant"], ["3.20"]),
    PT("Explain how natural selection could have led to a high proportion of lactase-persistent adults in Denmark ({L:select}).", 3,
       ["a mutation produced the persistence allele", "persistent adults could use milk for energy / protein in food shortages", "they were more likely to survive and reproduce", "they passed on the allele", "allele frequency increased over many generations"], ["3.38"]),
    PT("Suggest why eating yoghurt causes fewer symptoms than drinking milk ({L:yoghurt}).", 2,
       ["Lactobacillus has already converted much of the lactose to lactic acid", "less lactose reaches the large intestine", "less lactose for gut bacteria to respire / less gas produced"], ["5.7"], "Suggest"),
    PT("Explain why the blood glucose concentration rises after the test drink in a person who makes lactase ({L:test}).", 2,
       ["lactase breaks lactose down into glucose (and galactose)", "glucose is absorbed into the blood through the villi / wall of the small intestine"], ["2.32"]),
    PT("Explain why lactose-intolerant people produce gas after drinking milk ({L:symptoms}).", 2,
       ["lactose is not digested and reaches the large intestine", "bacteria respire it anaerobically", "producing carbon dioxide (gas)"], ["2.38"]),
    RW("Give one function of calcium in the human body ({L:select}).", 1, "formation of bones / teeth / blood clotting / muscle contraction (1)", ["2.25"]),
])

# 4 ---------------------------------------------------------------------------
pc4 = 25 / 10000 * 100
art("soil-antibiotic", "A new antibiotic from the soil", """
Most of the antibiotics used by doctors were first discovered in microorganisms that live in soil. «compete»Soil
contains billions of bacteria and fungi in every gram, and many of them release chemicals that kill or slow the
growth of their competitors. «penicillin»The first antibiotic to be widely used, penicillin, was obtained from a
mould called Penicillium.

«problem»Since the 1980s very few new types of antibiotic have been discovered, while bacteria that are resistant
to existing antibiotics have become more common. «mrsa»In some hospitals, infections caused by resistant bacteria
such as MRSA can no longer be treated with the usual drugs.

One reason for the lack of new antibiotics is that about 99% of soil bacteria will not grow on the nutrient agar
used in laboratories. «chip»To solve this problem, scientists designed a small plastic device with hundreds of
tiny holes. A sample of soil was diluted so that, on average, each hole received a single bacterial cell.
«membrane»The device was then covered with a partially permeable membrane and buried back in the soil. Nutrients
from the soil could diffuse into the holes, but the bacteria could not escape.

«colonies»After two weeks, colonies had grown in many of the holes. The scientists tested 10 000 of these colonies
for the ability to kill Staphylococcus bacteria and found 25 that did so. «new»One of them produced a new
antibiotic that kills bacteria by stopping them making their cell walls.

«mice»The new antibiotic was tested on mice that had been infected with a dose of Staphylococcus that is normally
fatal. «dose»All twelve mice that were given the antibiotic survived, while all twelve mice that were given an
injection of salt solution died within two days.

«noresist»The scientists also grew Staphylococcus in a low concentration of the new antibiotic for 27 days. No
resistant bacteria appeared during this time. «why»They suggested that this is because the antibiotic attacks
fatty molecules in the cell wall rather than a protein, so a single mutation in a gene is unlikely to change its
target.

«caution»Before the antibiotic can be used to treat people, it must be tested for safety in human volunteers.
This process usually takes more than ten years.

«future»Even if the new compound passes every stage of testing, it will be many years before doctors can prescribe it. Each stage costs large sums of money, and most compounds that look promising in the laboratory fail later because they are found to damage human cells. The researchers are therefore collecting thousands more soil samples from forests, deserts and river banks. They argue that the microorganisms in a single handful of soil may hold the answer to infections that cannot be treated today, provided that new drugs are used carefully once they are found.
""", [
    RW("Name the group of organisms to which Penicillium belongs ({L:penicillin}).", 1, "fungi (1)", ["1.2"]),
    PT("Suggest why soil bacteria release chemicals that kill their competitors ({L:compete}).", 2,
       ["they compete for nutrients / space", "killing competitors leaves more nutrients", "so they are more likely to survive and reproduce"], ["4.5"], "Suggest"),
    PT("Explain how nutrients from the soil reach the bacteria inside the device ({L:membrane}).", 3,
       ["by diffusion", "from a high concentration in the soil to a low concentration in the holes", "through the partially permeable membrane", "small molecules can pass through but bacteria cannot"], ["2.15"]),
    CA("Calculate the percentage of the colonies tested that could kill Staphylococcus ({L:colonies}).", 2,
       "percentage = ", "%", ["25 ÷ 10 000 × 100"], f"{nf(pc4)}%", ["3.39"], {"percent": pc4}, "part/whole × 100"),
    PT("Explain why one group of mice was given an injection of salt solution ({L:dose}).", 2,
       ["as a control", "to show that survival was caused by the antibiotic", "and not by the injection itself"], ["3.39"]),
    MC("The new antibiotic stops bacteria making their cell walls ({L:new}). Why does it not damage human cells?",
       "human cells do not have a cell wall", ["human cells have a cellulose cell wall", "human cells contain plasmids", "human cells are surrounded by a capsule"], ["2.4"]),
    PT("Explain how antibiotic-resistant bacteria such as MRSA become common in hospitals ({L:mrsa}).", 3,
       ["a mutation makes some bacteria resistant", "the antibiotic kills non-resistant bacteria", "resistant bacteria survive and reproduce", "the resistance gene is passed on", "overuse of antibiotics increases selection"], ["3.39"]),
    PT("Suggest why a single mutation is unlikely to make the bacteria resistant to the new antibiotic ({L:why}).", 2,
       ["a mutation changes the base sequence of a gene", "which changes the amino acid sequence of a protein", "the target is a fatty molecule, not a protein, so it is not changed directly"], ["3.35B"], "Suggest"),
    RW("Suggest one reason why the antibiotic must be tested on human volunteers before it is used ({L:caution}).", 1,
       "to check it is safe / has no harmful side effects / to find a safe dose (1)", ["3.39"]),
])

# 5 ---------------------------------------------------------------------------
r5 = 22.5 / 9.0
art("cassava", "Saving cassava", """
Cassava is a shrub grown for its large starchy roots. «food»It is the main source of carbohydrate for more than
500 million people in Africa, Asia and South America. «grow»Cassava grows well in poor soils and survives long
periods of drought, so it is an important crop for small farmers.

«virus»Cassava brown streak disease is caused by a virus that is spread by whiteflies, small insects that feed on
the sap in the phloem of cassava leaves. «roots»Infected plants show yellow patches on their leaves, and their
roots develop brown, dead areas that make them unfit to eat. In some regions the disease destroys up to 70% of
the crop.

«cuttings»Farmers usually grow new cassava plants from cuttings of stems taken from the previous year's crop. If
the parent plant was infected, the virus is present in the cuttings as well.

«gm»Scientists have produced genetically modified cassava that is resistant to the virus. «insert»They used a
restriction enzyme to cut a short section of DNA from the virus, and inserted it into a bacterial plasmid. The
plasmid was used as a vector to carry the DNA into cassava cells grown in a laboratory. «silence»When the modified
plants are infected, the inserted DNA allows the plant to destroy the genetic material of the virus before it can
multiply.

«trial»In a field trial, 200 modified plants and 200 unmodified plants were grown in the same field for one year.
At harvest, 4 of the modified plants and 152 of the unmodified plants had damaged roots. «yield»The mean yield of
roots was 22.5 tonnes per hectare for the modified plants and 9.0 tonnes per hectare for the unmodified plants.

«breeding»An alternative approach is selective breeding. Some cassava varieties grown in East Africa show partial
resistance to the disease. «cross»Breeders cross these varieties with high-yielding varieties and select the best
offspring over several generations.

«concern»Some people are concerned about growing genetically modified crops. They worry that genes may spread to
wild relatives of the crop, or that the crop may affect insects that feed on it. Others argue that the risk of
famine is a far greater danger than these possible effects.

«farmers»Training farmers is an important part of the project. Many farmers save stems from their own plants to start the next crop, so a plant that is infected but shows only mild symptoms can pass the virus on without anyone noticing. Advisers now visit villages to show farmers how to recognise yellow patches on the leaves and how to destroy infected plants by burning them. Farmers who plant only certified healthy stems have reported harvests that are almost twice as large as those of neighbours who reuse stems from diseased fields.
""", [
    RW("Name the carbohydrate stored in cassava roots ({L:food}).", 1, "starch (1)", ["2.8"]),
    PT("Explain why whiteflies feed on the sap in the phloem ({L:virus}).", 2,
       ["phloem transports sucrose / sugars", "and amino acids", "which provide the insects with energy / food"], ["2.53"]),
    PT("Explain why cuttings taken from an infected plant are also infected ({L:cuttings}).", 2,
       ["cuttings are asexual reproduction / produce clones", "new plant grows from cells of the parent by mitosis", "the virus is already inside the parent's cells"], ["3.7"]),
    RW("Name the enzyme that joins the section of virus DNA into the plasmid ({L:insert}).", 1, "ligase (1)", ["5.12"]),
    CA("Calculate the percentage of unmodified plants that had damaged roots ({L:trial}).", 2,
       "percentage = ", "%", ["152 ÷ 200 × 100"], f"{nf(152 / 200 * 100)}%", ["5.15"], {"percent_unmodified": 76.0, "percent_modified": 2.0}, "part/whole × 100"),
    CA("Calculate how many times greater the yield of the modified plants was than the yield of the unmodified plants ({L:yield}).", 2,
       "", "times", ["22.5 ÷ 9.0"], f"{nf(r5)} times", ["5.15"], {"ratio": r5}, "22.5/9.0"),
    PT("Describe how selective breeding could be used to produce a variety of cassava that is resistant to the disease and gives a high yield ({L:cross}).", 3,
       ["choose a resistant variety and a high-yielding variety as parents", "cross them", "select offspring that show both features", "breed these together", "repeat over many generations"], ["5.10"], "Describe"),
    PT("Discuss the advantages and disadvantages of growing genetically modified cassava ({L:concern}).", 3,
       ["higher yield / more food for people", "less of the crop destroyed by disease", "less risk of famine", "genes may spread to wild relatives", "may harm insects / food chains", "cost / ethical concerns"], ["5.15"], "Discuss", "Both an advantage and a disadvantage are needed for 3 marks"),
    RW("Give the term for an organism that contains genetic material from another species ({L:gm}).", 1, "transgenic (1)", ["5.16"]),
])

# 6 ---------------------------------------------------------------------------
pc6 = (42 - 17) / 42 * 100
art("coral", "When coral turns white", """
Coral reefs are built by tiny animals called coral polyps. «polyp»Each polyp has a soft body with a ring of
tentacles around its mouth, which it uses to catch small animals from the water, and it builds a hard skeleton of
calcium carbonate around itself. Over thousands of years these skeletons build up to form reefs that can be
hundreds of kilometres long.

«algae»Living inside the cells of the polyps are single-celled algae. The algae photosynthesise and pass most of
the glucose and amino acids they make to the coral. «give»In return, the coral provides the algae with carbon
dioxide and nitrogen-containing waste. The algae also give the coral its bright colours.

«bleach»When the temperature of the sea water rises by just 1 °C above its normal summer maximum for a few weeks,
the algae stop working properly and are expelled from the coral. «white»Without the algae the coral turns white,
which is called bleaching. Bleached coral is not dead, but if the algae do not return within a few weeks, the
coral starves.

«survey»Scientists surveyed 100 reefs in the Pacific Ocean. «data»Before a marine heatwave, the mean cover of
living coral was 42% of the sea floor. One year after the heatwave, it had fallen to 17%. «fish»The number of fish
species found on the reefs also decreased, because many fish feed on coral or shelter in it.

«cause»The increase in sea temperature is linked to global warming. «acid»As well as warming the oceans, carbon
dioxide dissolves in sea water and makes it more acidic. Corals find it harder to build their skeletons in more
acidic water.

«tolerant»Some corals survive heatwaves better than others. Scientists have found that the polyps that survived on
one reef contained a different type of alga that can tolerate higher temperatures. «breed»They are now growing
young corals from these survivors in tanks and transplanting them back onto damaged reefs.

«local»Reefs that are not damaged by other human activities, such as sewage, overfishing and sediment from building
sites, recover more quickly after bleaching.

«hope»Not all of the news is bad. Some corals on the same reef survive heatwaves that kill their neighbours, and scientists are studying these individuals to find out why. One idea is to grow young corals from the survivors in tanks and then attach them to damaged parts of the reef. Another is to shade small, valuable areas of reef during the hottest weeks of the year. Most researchers agree, however, that these methods can only buy time, and that reefs will not be safe unless the rise in sea temperature is slowed.
""", [
    RW("Name the group of organisms to which the single-celled algae belong ({L:algae}).", 1, "protoctists (1)", ["1.2"]),
    PT("Give two pieces of evidence from the passage that coral polyps are animals ({L:polyp}).", 2,
       ["they have a mouth / tentacles to catch food", "they feed on other organisms / small animals", "they rely on algae for photosynthesis / have no chloroplasts of their own"], ["1.2"], "Give"),
    PT("Explain how both the coral and the algae benefit from living together ({L:algae-give}).", 3,
       ["algae photosynthesise and make glucose", "coral uses the glucose for respiration / energy", "coral uses amino acids to make proteins / for growth", "coral provides carbon dioxide for photosynthesis", "nitrogen waste allows algae to make amino acids"], ["2.18"]),
    CA("Calculate the percentage decrease in the cover of living coral ({L:data}).\n\nGive your answer to one decimal place.", 2,
       "percentage decrease = ", "%", ["(42 − 17) ÷ 42 × 100"], f"{pc6:.1f}%", ["4.15"], {"percent_decrease": round(pc6, 1)}, "(old − new)/old × 100"),
    PT("Explain how human activities have caused the temperature of the sea to rise ({L:cause}).", 3,
       ["burning fossil fuels releases carbon dioxide", "deforestation / farming releases carbon dioxide or methane", "greenhouse gases absorb and re-emit infrared radiation / heat", "enhanced greenhouse effect", "global warming"], ["4.14", "4.15"]),
    MC("Which of these gases is a greenhouse gas released by cattle?", "methane", ["oxygen", "nitrogen", "sulfur dioxide"], ["4.13"]),
    PT("Suggest why the number of fish species on the reefs decreased after the heatwave ({L:fish}).", 2,
       ["less coral for fish to feed on", "less shelter so more fish eaten by predators", "fish move away / die"], ["4.5"], "Suggest"),
    PT("Explain how sewage entering the sea could slow the recovery of a reef ({L:local}).", 3,
       ["sewage provides food for bacteria", "bacteria multiply and respire aerobically", "oxygen in the water is used up", "coral / fish die from lack of oxygen", "nutrients cause algal growth that blocks light"], ["4.16"]),
])

# 7 ---------------------------------------------------------------------------
pc7 = (6.1 - 5.0) / 5.0 * 100
art("altitude", "Life in thin air", """
The air at the top of a high mountain contains the same percentage of oxygen as the air at sea level, about 21%.
«pressure»However, the air pressure is much lower, so each breath contains fewer oxygen molecules. At 5 000 m above
sea level, a breath of air contains only about half as much oxygen as the same volume of air at sea level.

«symptoms»Climbers who go up a mountain too quickly may suffer from altitude sickness. They have headaches, feel
sick and cannot sleep, and they find that even gentle exercise makes them breathless. «breath»Their breathing rate
and heart rate increase, even when they are resting.

«adjust»If a person stays at high altitude for several weeks, the body adjusts. «epo»The kidneys release a hormone
called EPO, which travels to the bone marrow and stimulates it to make more red blood cells. «count»In one study,
the concentration of red blood cells in the blood of eight climbers rose from a mean of 5.0 million per mm³ at sea
level to 6.1 million per mm³ after six weeks at 4 500 m.

«native»People whose families have lived at high altitude for many generations show other adaptations. Many people
in the Himalayas have a wider chest and larger lungs than people who live at sea level. «tibet»They also breathe
more rapidly and their blood vessels widen more easily, so more blood flows to the tissues. Scientists have found
that many of these people carry a particular allele of a gene involved in the response to low oxygen. This allele
is rare in populations that live at sea level.

«athletes»Some athletes train at high altitude before a competition at sea level. «lactic»They believe that after
training at altitude, their muscles will receive more oxygen during a race and will build up less lactic acid.
«rules»Others try to increase their red blood cell count by injecting EPO. This is banned in sport, partly because
it makes the blood thicker and increases the risk of blood clots and heart attacks.

«athletes»Athletes have learned to make use of these changes. Many long-distance runners spend several weeks training in mountain camps before an important race held near sea level. While they are at altitude their bodies produce extra red blood cells, and for a short time after they return these cells allow more oxygen to be carried to their muscles. Some athletes sleep in special tents in which the air contains less oxygen than normal, which produces a similar effect. Sports organisations have debated whether such tents give an unfair advantage over other competitors.
""", [
    PT("Explain why a climber's breathing rate increases at high altitude ({L:breath}).", 2,
       ["each breath contains less oxygen", "more breaths are needed to take in enough oxygen", "for aerobic respiration in cells"], ["2.48"]),
    PT("Describe how red blood cells are adapted to carry oxygen.", 2,
       ["contain haemoglobin that combines with oxygen", "no nucleus, so more room for haemoglobin", "biconcave shape gives a large surface area"], ["2.61"], "Describe"),
    MC("How does the hormone EPO travel from the kidneys to the bone marrow ({L:epo})?", "dissolved in the blood plasma", ["along neurones", "in the urine", "through the alveoli"], ["2.60"]),
    CA("Calculate the percentage increase in the concentration of red blood cells ({L:count}).", 2,
       "percentage increase = ", "%", ["(6.1 − 5.0) ÷ 5.0 × 100"], f"{nf(pc7, dp=0)}%", ["2.61"], {"percent_increase": round(pc7)}, "(new − old)/old × 100"),
    PT("Explain how natural selection could have made this allele common in people living in the Himalayas ({L:tibet}).", 3,
       ["the allele arose by mutation", "people with the allele were better able to get oxygen to their tissues", "more likely to survive and reproduce at altitude", "passed the allele to their children", "allele became more common over many generations"], ["3.38"]),
    PT("Explain why muscles produce lactic acid during a race ({L:lactic}).", 3,
       ["not enough oxygen reaches the muscles", "muscles respire anaerobically", "glucose is converted to lactic acid", "less energy is released than in aerobic respiration"], ["2.36", "2.38"]),
    PT("Suggest why having more red blood cells could improve an athlete's performance.", 2,
       ["more oxygen carried to the muscles", "more aerobic respiration", "more energy released / less lactic acid"], ["2.61"], "Suggest"),
    PT("Suggest how thicker blood could increase the risk of a heart attack ({L:rules}).", 2,
       ["a clot could block a coronary artery", "less oxygen / glucose reaches the heart muscle", "heart muscle cannot respire and dies"], ["2.67"], "Suggest"),
])

# 8 ---------------------------------------------------------------------------
pc8 = (13.7 - 2.0) / 13.7 * 100
art("bees", "Bees, crops and insecticides", """
About three quarters of the world's food crops depend at least partly on animals for pollination. «bees»Bees are
the most important pollinators. As a bee feeds on nectar, pollen grains stick to the hairs on its body and are
carried to the next flower it visits.

«nectar»Nectar is a sugary liquid made by flowers. Bees use it as their main source of energy, and they collect
pollen as a source of protein for their young. «colour»Flowers that are pollinated by insects often have large,
brightly coloured petals and a strong scent.

«decline»In many countries the number of bee colonies has fallen over the last thirty years. Scientists think there
are several causes, including loss of wild flowers, a parasitic mite that spreads viruses between bees, and a group
of insecticides called neonicotinoids.

«neonic»Neonicotinoids are taken up from the soil by crop plants and transported to all parts of the plant,
including the pollen and nectar. «nerve»They kill insect pests by binding to receptors at the synapses of nerve
cells, so that nerve impulses can no longer be controlled.

«trial»In one experiment, scientists set up 50 colonies of bumblebees. Twenty-five colonies were given pollen and
sugar solution containing a low concentration of a neonicotinoid, similar to that found in crops. The other
twenty-five colonies were given pollen and sugar solution with no insecticide. «queens»After six weeks, the
colonies were placed in a field and allowed to feed normally. At the end of the summer, the untreated colonies had
produced a mean of 13.7 new queens each, but the treated colonies produced a mean of only 2.0 new queens each.

«lost»Other studies have found that honeybees exposed to neonicotinoids are more likely to get lost when returning
to the hive.

«ban»Several countries have now restricted the use of neonicotinoids on flowering crops. «alternatives»Some farmers
are using biological control instead, for example by releasing ladybirds to eat aphids, or by planting strips of
wild flowers at the edges of fields to provide food and shelter for predatory insects.

«gardens»Ordinary people can also help pollinators. Planting a mixture of flowers that open at different times of year gives bees a supply of nectar and pollen from early spring to late autumn. Leaving areas of lawn uncut allows wild flowers such as clover to bloom, and piles of dead wood provide nesting sites for solitary bees. In one city, volunteers counted the insects visiting garden flowers each summer for five years, and they recorded more species of bee in gardens where no sprays were used than in gardens that were regularly treated.
""", [
    RW("Name the part of a flower that produces pollen ({L:bees}).", 1, "anther (1)", ["3.3"]),
    PT("Describe how flowers that are pollinated by insects are adapted to attract bees ({L:colour}).", 3,
       ["large, brightly coloured petals", "strong scent", "produce nectar", "anthers / stigma inside the flower so the insect brushes against them", "sticky / spiky pollen grains"], ["3.3"], "Describe"),
    PT("Explain how neonicotinoids taken up from the soil reach the pollen and nectar ({L:neonic}).", 2,
       ["absorbed by the roots / root hair cells", "transported in the xylem / phloem", "to the flowers"], ["2.53"]),
    PT("Describe how a nerve impulse is passed across a synapse ({L:nerve}).", 2,
       ["impulse causes release of neurotransmitter", "neurotransmitter diffuses across the gap", "binds to receptors on the next neurone", "starts a new impulse"], ["2.89"], "Describe"),
    CA("Calculate the percentage decrease in the mean number of new queens produced by the treated colonies ({L:queens}).\n\nGive your answer to one decimal place.", 2,
       "percentage decrease = ", "%", ["(13.7 − 2.0) ÷ 13.7 × 100"], f"{pc8:.1f}%", ["5.4"], {"percent_decrease": round(pc8, 1)}, "(old − new)/old × 100"),
    PT("Give two variables that were controlled in this experiment ({L:trial}).", 2,
       ["species of bee", "number of colonies in each group", "type / volume of food", "time before release", "same field / feeding conditions"], ["5.4"], "Give"),
    PT("Suggest how a fall in the number of bees could affect the yield of crops.", 3,
       ["fewer flowers pollinated", "less fertilisation", "fewer seeds / fruits form", "lower yield"], ["3.4"], "Suggest"),
    PT("Explain the advantages of using biological control rather than insecticides ({L:alternatives}).", 2,
       ["biological control is specific to the pest", "does not kill pollinators such as bees", "no chemical residues in food / environment", "pests do not become resistant"], ["5.4"]),
])

# 9 ---------------------------------------------------------------------------
n9 = 537 * 0.9
art("diabetes", "Walking away from diabetes", """
The concentration of glucose in the blood is normally kept between about 4 and 7 mmol per dm³. «insulin»After a
meal, the pancreas releases the hormone insulin, which causes liver and muscle cells to take up glucose from the
blood. «glycogen»In the liver, the extra glucose is converted to glycogen and stored.

«type2»In type 2 diabetes, the pancreas still produces insulin, but the cells of the body no longer respond to it
properly. As a result, the blood glucose concentration stays high for long periods. «damage»Over many years, high
blood glucose damages small blood vessels in the eyes, kidneys and feet, and increases the risk of heart disease.

«numbers»Worldwide, about 537 million adults had diabetes in 2021, and about 90% of these had type 2 diabetes.
«risk»The main risk factors are being overweight, lack of physical activity and a diet high in sugar and fat. The
risk also increases with age and is higher in people with a family history of the disease.

«study»In one study, 3 000 adults with high blood glucose were divided into two groups. One group was given advice
on diet and asked to walk briskly for 30 minutes a day, five days a week. The other group was given no advice.
«follow»After three years, 14% of the group given advice had developed type 2 diabetes, compared with 29% of the
group given no advice.

«muscle»Exercise helps because working muscles take up glucose from the blood even without insulin. «mito»Regular
exercise also increases the number of mitochondria in muscle cells and the number of capillaries around them.

«urine»Before blood tests were available, doctors identified diabetes by testing the urine for glucose. «kidney»In a
healthy person, all the glucose filtered into the nephrons is reabsorbed back into the blood, but when the blood
glucose concentration is very high, some glucose remains in the urine.

«treat»People with type 2 diabetes are first treated with changes to their diet and exercise. If this is not
enough, they are given drugs that make their cells more sensitive to insulin.

«screen»Because type 2 diabetes develops slowly, many people have the condition for years before it is diagnosed. Some health services now offer a simple test to adults over the age of forty, in which a small sample of blood is taken to measure the glucose concentration. People whose glucose levels are higher than normal, but not yet high enough to count as diabetes, are invited to join exercise and diet programmes. Early results suggest that these programmes are cheaper to run than treating the damage to eyes, kidneys and feet that uncontrolled diabetes can cause.
""", [
    RW("Name the organ that releases insulin ({L:insulin}).", 1, "pancreas (1)", ["2.94"]),
    PT("Explain how insulin returns the blood glucose concentration to normal after a meal ({L:insulin-glycogen}).", 3,
       ["rise in blood glucose is detected by the pancreas", "insulin is released into the blood", "liver and muscle cells take up glucose", "glucose is converted to glycogen", "negative feedback"], ["2.94"]),
    CA("Calculate the number of adults who had type 2 diabetes in 2021 ({L:numbers}).\n\nGive your answer in millions to three significant figures.", 2,
       "number = ", "million", ["537 × 90 ÷ 100"], f"{sfig(n9, 3)} million", ["2.94"], {"millions": float(sfig(n9, 3))}, "537 × 0.9"),
    PT("Explain why exercise lowers the blood glucose concentration ({L:muscle}).", 2,
       ["muscles respire faster during exercise", "respiration uses glucose", "so muscles take up more glucose from the blood"], ["2.34"]),
    PT("Explain how having more mitochondria in muscle cells helps a person to exercise ({L:mito}).", 2,
       ["mitochondria are the site of aerobic respiration", "more energy / ATP released from glucose", "for muscle contraction"], ["2.35"]),
    PT("Suggest two reasons why the results of this study can be trusted ({L:study}).", 2,
       ["large number of people / 3 000 adults", "a control group given no advice", "people had similar starting blood glucose", "study lasted a long time / three years"], ["2.94"], "Suggest"),
    MC("Which part of a nephron reabsorbs glucose?", "proximal convoluted tubule", ["loop of Henle", "collecting duct", "Bowman's capsule"], ["2.77B"]),
    PT("Explain why glucose is found in the urine when the blood glucose concentration is very high ({L:kidney}).", 2,
       ["glucose is filtered into the Bowman's capsule by ultrafiltration", "too much glucose to be all reabsorbed in the proximal convoluted tubule", "so some remains in the urine"], ["2.75B", "2.77B"]),
    PT("Suggest why the risk of type 2 diabetes is higher in people with a family history of the disease ({L:risk}).", 2,
       ["alleles / genes that increase the risk are inherited", "family members may share the same diet / lifestyle"], ["3.33"], "Suggest"),
])

# 10 --------------------------------------------------------------------------
art("sickle", "A gene, a parasite and a map", """
Sickle-cell disease is an inherited condition that affects the haemoglobin in red blood cells. «mutation»It is
caused by a change in a single base in the gene that codes for one of the haemoglobin proteins. «aa»This change
causes one amino acid in the protein to be replaced by a different amino acid.

«shape»People with two copies of the sickle-cell allele make abnormal haemoglobin. When the concentration of oxygen
in their blood is low, the abnormal haemoglobin molecules join together into long fibres, and the red blood cells
become stiff and curved like a sickle. «block»Sickle cells can block capillaries, causing severe pain, and they are
destroyed more quickly than normal red blood cells, so the person often feels tired and weak.

«carrier»People with one normal allele (A) and one sickle-cell allele (S) are said to be carriers. They make enough
normal haemoglobin to be healthy, although they may have mild symptoms when oxygen is very scarce.

«malaria»Malaria is caused by a single-celled parasite called Plasmodium, which is passed to humans by mosquitoes.
The parasite spends part of its life cycle inside red blood cells. «protect»Carriers of the sickle-cell allele are
much less likely to die from malaria than people with two normal alleles, because their infected red blood cells
are removed from the blood more quickly.

«map»Maps show that the sickle-cell allele is most common in parts of Africa, the Middle East and India where
malaria is, or was, common. «freq»In some parts of West Africa, up to 25% of the population are carriers, but in
northern Europe the allele is almost absent.

«screen»In many countries, newborn babies are now tested for sickle-cell disease using a drop of blood taken from
the heel. «couples»Couples who know that they are both carriers can be given advice about the chance that their
children will inherit the disease.

«treatment»Treatment includes drinking plenty of water, painkillers and antibiotics to prevent infections.
«transplant»Some patients have been cured by a transplant of bone marrow from a healthy donor. The bone marrow
contains stem cells that divide to produce all the types of blood cell.

«treat»Treatment for sickle cell disease has improved greatly. Children with the condition are given extra fluids and pain relief during a crisis, and some take a daily drug that increases the amount of a different form of haemoglobin in their red blood cells. In a small number of patients, doctors have replaced the stem cells in the bone marrow with healthy cells taken from a brother or sister. Newer trials are testing ways to correct the faulty gene in the patient's own stem cells, so that no donor is needed and the cells are not rejected.
""", [
    RW("Give the term for a change in a single base in a gene ({L:mutation}).", 1, "(gene) mutation (1)", ["3.34"]),
    PT("Explain why a change in a single base can change one amino acid in the protein ({L:aa}).", 2,
       ["three bases code for one amino acid / triplet code", "the change alters one triplet", "so a different amino acid is coded for / inserted"], ["3.35B"]),
    PT("Explain why people with sickle-cell disease often feel tired ({L:block}).", 2,
       ["fewer red blood cells / less working haemoglobin", "less oxygen carried to cells", "less aerobic respiration / less energy released"], ["2.61"]),
    MC("Plasmodium ({L:malaria}) belongs to which group of organisms?", "protoctists", ["bacteria", "fungi", "viruses"], ["1.4"]),
    RW("Two carriers (AS) have a child ({L:couples}).\n\nUse a genetic diagram to find the probability that the child has sickle-cell disease.", 3,
       "gametes A and S from each parent (1)\noffspring AA, AS, AS, SS (1)\nprobability 1/4 / 25% / 0.25 (1)", ["3.23", "3.25"], "Reject 1 : 3; allow full marks for a correct answer shown in a Punnett square"),
    PT("Explain why the sickle-cell allele is common in areas where malaria is common ({L:protect-map}).", 3,
       ["carriers are less likely to die from malaria", "carriers survive and reproduce", "pass on the sickle-cell allele", "natural selection keeps the allele frequency high", "where there is no malaria, carriers have no advantage"], ["3.38"]),
    PT("Explain why a bone marrow transplant can cure sickle-cell disease ({L:transplant}).", 2,
       ["donor stem cells divide by mitosis", "and differentiate into red blood cells", "donor cells carry the normal allele / make normal haemoglobin"], ["3.29"]),
    PT("Suggest one advantage and one disadvantage of testing newborn babies for sickle-cell disease ({L:screen}).", 2,
       ["advantage: early treatment / antibiotics to prevent infection", "disadvantage: worry for parents / cost / small risk of false result"], ["3.25"], "Suggest"),
    CA("A village in West Africa has 2 400 people. Calculate how many of them might be carriers ({L:freq}).", 1,
       "number = ", "", [], "600", ["3.25"], {"carriers": 600}, "25% of 2 400"),
])

# 11 --------------------------------------------------------------------------
r11 = 105 / 3.5
art("vertical-farm", "Farming upwards", """
By 2050 the world's population is expected to reach almost 10 billion, and much of the extra food will be needed in
cities. «vertical»One possible solution is vertical farming, in which crops are grown indoors on shelves stacked one
above another, sometimes in buildings that are twenty storeys high.

«hydro»Most vertical farms do not use soil. Instead, the roots of the plants hang in a solution of water containing
all the mineral ions the plants need, including nitrate and magnesium. Air is bubbled through the solution all the
time. «recycle»The solution is pumped around the farm and reused, so a vertical farm uses up to 95% less water than
a field growing the same crop.

«leds»The plants are lit by light-emitting diodes (LEDs) that produce mainly red and blue light. «absorb»Chlorophyll
absorbs red and blue light strongly, but reflects most green light. LEDs also produce much less heat than the lamps
used in older glasshouses, so they can be placed close to the leaves.

«control»Inside the building, the temperature is kept at 24 °C and the carbon dioxide concentration is raised to
about three times the concentration in normal air. «hours»Computers control the lights so that the plants receive
18 hours of light each day.

«yield»Lettuce grown in one vertical farm reached harvest size in 30 days, compared with 60 days in a field. «trays»The
farm produced 105 kg of lettuce per square metre of floor area each year, compared with about 3.5 kg per square
metre per year in a field.

«pests»Because the farm is sealed, there are very few insect pests, and no pesticides are needed. «biocontrol»If
pests do get in, they are controlled by releasing predatory insects.

«energy»The biggest disadvantage of vertical farming is the cost of the electricity used to power the lights, pumps
and air conditioning. If the electricity comes from burning fossil fuels, the farm may contribute to climate change.
«crops»At present, vertical farming is only profitable for fast-growing, high-value crops such as salad leaves and
herbs. Staple crops such as wheat and rice still need to be grown in fields.

«future»Supporters of vertical farming argue that costs will fall as the technology improves. LEDs have become far more efficient over the last twenty years, and some farms now buy their electricity from solar and wind power. Building farms close to the shops that sell the produce means that vegetables travel only a few kilometres, so they are fresher and less fuel is used for transport. Critics reply that a field uses free light from the Sun, and that it will be difficult for a building full of lamps ever to compete on price.
""", [
    RW("Give one reason from the article why vegetables from a vertical farm near a city may need less fuel for transport ({L:future}).", 1, "the farm is close to the shops / produce travels only a few kilometres (1)", ["5.1"]),
    PT("Explain why the solution contains nitrate ions and magnesium ions ({L:hydro}).", 2,
       ["nitrate is needed to make amino acids / proteins", "magnesium is needed to make chlorophyll"], ["2.22"]),
    PT("Suggest why air is bubbled through the solution ({L:hydro}).", 2,
       ["roots need oxygen", "for aerobic respiration", "to release energy for active transport of mineral ions"], ["2.34"], "Suggest"),
    PT("Explain why the LEDs produce mainly red and blue light ({L:absorb}).", 2,
       ["chlorophyll absorbs red and blue light", "this light energy is used for photosynthesis", "green light is reflected, so producing it would waste energy"], ["2.18"]),
    PT("Explain why raising the carbon dioxide concentration and keeping the temperature at 24 °C increase the growth of the lettuce ({L:control}).", 3,
       ["carbon dioxide is a limiting factor", "more carbon dioxide gives a faster rate of photosynthesis", "more glucose for growth / respiration", "24 °C keeps enzymes working quickly without denaturing them"], ["2.20", "5.2"]),
    CA("Calculate how many times more lettuce is produced per square metre per year in the vertical farm than in a field ({L:trays}).", 2,
       "", "times", ["105 ÷ 3.5"], f"{nf(r11)} times", ["5.1"], {"ratio": r11}, "105/3.5"),
    MC("The plants receive 18 hours of light each day ({L:hours}). Which process happens in the leaves only when they are lit?", "photosynthesis", ["respiration", "diffusion", "osmosis"], ["2.18"]),
    PT("Give two advantages of using predatory insects rather than pesticides to control pests ({L:biocontrol}).", 2,
       ["no chemical residues on the food", "does not harm other / useful insects", "pests do not become resistant", "does not need to be applied repeatedly"], ["5.4"], "Give"),
    PT("Discuss whether vertical farming is better for the environment than growing crops in fields ({L:recycle} and {L:energy}).", 2,
       ["uses much less water", "no pesticides", "less land needed so less deforestation / habitat loss", "uses a lot of electricity", "burning fossil fuels releases carbon dioxide / adds to global warming"], ["5.1", "4.14"], "Discuss", "One mark for a valid point for, one mark for a valid point against"),
])

# 12 --------------------------------------------------------------------------
pc12 = 1.3 / 10.6 * 100
art("tb", "An old disease, a new vaccine", """
Tuberculosis (TB) is caused by a bacterium called Mycobacterium tuberculosis. «spread»It is spread through the air
when a person with the disease coughs or sneezes, releasing tiny droplets that contain the bacteria. «lungs»When the
droplets are breathed in, the bacteria settle in the alveoli of the lungs.

«phago»In most healthy people, phagocytes engulf the bacteria, but some bacteria survive inside the phagocytes.
«latent»These bacteria can remain inactive for many years without causing symptoms. If the immune system becomes
weak, for example because of malnutrition or another infection, the bacteria start to multiply.

«symptoms»The symptoms of active TB include a cough that lasts for more than three weeks, coughing up blood, fever,
night sweats and loss of body mass. «damage»The bacteria destroy the walls of the alveoli and cause scar tissue to
form in the lungs, so the patient becomes breathless.

«figures»In 2022, about 10.6 million people became ill with TB, and 1.3 million died from the disease. Most of
these cases were in Asia and Africa.

«treat»TB can be cured with a combination of four antibiotics taken every day for six months. «course»Patients often
feel better after a few weeks, and some stop taking their medicine before the end of the course. «mdr»This has led
to strains of TB that are resistant to the two most effective antibiotics.

«bcg»The BCG vaccine contains a weakened strain of a related bacterium that causes TB in cattle. «bcgwork»It is
given to babies in countries where TB is common and protects young children well, but it is less effective in
adults.

«newvac»Scientists are testing new vaccines. In one trial, 3 500 adults who had inactive TB bacteria were given
either the new vaccine or an injection of salt solution. «trial»Neither the volunteers nor the doctors knew which
injection each person had received. After three years, 13 people in the vaccine group and 26 people in the salt
solution group had developed active TB.

«next»If the new vaccine is approved, the next challenge will be to make and deliver enough doses for the countries that need it most. Many of the people at greatest risk live far from hospitals, so health workers will need to travel to villages with supplies kept cold in refrigerated boxes. Researchers also want to find out how long the protection lasts, and whether a second dose is needed several years later. They will continue to follow the volunteers from the trial for at least ten years.
""", [
    RW("Name the type of pathogen that causes TB ({L:spread}).", 1, "bacterium (1)", ["1.4"]),
    PT("Describe how phagocytes destroy bacteria ({L:phago}).", 2,
       ["phagocytes engulf / surround the bacteria", "digest them using enzymes"], ["2.62"], "Describe"),
    PT("Explain why damage to the alveoli makes a patient breathless ({L:damage}).", 3,
       ["smaller surface area for gas exchange", "scar tissue increases the diffusion distance", "less oxygen diffuses into the blood", "less aerobic respiration", "patient breathes faster to compensate"], ["2.48"]),
    CA("Calculate the percentage of people who became ill with TB in 2022 who died from the disease ({L:figures}).\n\nGive your answer to one decimal place.", 2,
       "percentage = ", "%", ["1.3 ÷ 10.6 × 100"], f"{pc12:.1f}%", ["1.4"], {"percent": round(pc12, 1)}, "part/whole × 100"),
    PT("Explain how the BCG vaccine protects a child from TB ({L:bcg}).", 3,
       ["vaccine contains antigens", "lymphocytes produce antibodies", "memory cells are made", "on infection memory cells cause faster / larger antibody production", "bacteria destroyed before symptoms develop"], ["2.63B"]),
    PT("Explain why stopping a course of antibiotics early can lead to resistant strains of TB ({L:course-mdr}).", 3,
       ["not all bacteria are killed", "the most resistant bacteria survive", "they reproduce", "pass on the resistance gene", "resistant strain spreads"], ["3.39"]),
    PT("Suggest why neither the volunteers nor the doctors knew which injection each person received ({L:trial}).", 2,
       ["to avoid bias", "doctors might treat / record the groups differently", "volunteers might behave differently / placebo effect"], ["2.63B"], "Suggest"),
    MC("In the trial, what was the injection of salt solution ({L:newvac})?", "a placebo", ["a vaccine", "an antibiotic", "an antigen"], ["2.63B"]),
])


def build_item(slug, title, text, parts, k):
    body, marks = wrap(text)
    fig = {"type": "passage", "title": title, "text": body, "numbered": True}
    rng = random.Random(f"comp-{slug}")
    P, R, refs, values = [], [], [], {}
    labs = "abcdefghij"
    for i, sp in enumerate(parts):
        lab = labs[i]
        kind = sp[0]
        if kind == "pt":
            _, t, m, pts, rf, cw, notes = sp
            P.append(text_part(lab, lref(t, marks), m))
            R.append(points_row(lab, m, pts, cw, notes, "AO2"))
        elif kind == "rw":
            _, t, m, ans, rf, notes = sp
            sp_ = "table" if False else None
            P.append(text_part(lab, lref(t, marks), m, lines=max(1, m * 2) if m > 1 else 1))
            R.append(row_(lab, ans, m, notes, "AO1"))
        elif kind == "mc":
            _, t, cor, ds, rf = sp
            p, r = mcq_part(rng, lab, lref(t, marks), cor, ds)
            P.append(p)
            R.append(r)
        else:
            _, t, m, prefix, suffix, steps, final, rf, vals, method = sp
            P.append(calc_part(lab, lref(t, marks), m, prefix, suffix=suffix or None))
            for s in steps:
                R.append(row_(lab, s + " (1)", 1, None, "AO2"))
            R.append(row_(lab, final + " (1)", m - len(steps), "Allow full marks for the correct answer with no working", "AO2"))
            values.update(vals)
        for x in rf:
            if x not in refs:
                refs.append(x)
    answer = {"method": "values computed from figures in the passage", "values": values, "checked": True} if values else None
    return dict(parts=P, rows=R, refs=refs, cw="Explain", diff="7-9" if k % 2 else "4-6",
                intro="Read the article, then answer the questions that follow. Line numbers are given in the margin.",
                figures=[fig], answer=answer, template=f"comprehension-{slug}",
                general="Answers may use information from the article and the candidate's own knowledge. Credit line-referenced information only where it answers the question asked.")


@reg(HOST, "comprehension", "comprehension")
def comprehension():
    return [build_item(*a, k) for k, a in enumerate(ARTICLES)]
