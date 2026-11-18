"""Six-mark extended-response templates, point-marked as on live papers: one "six of the following"
row listing the creditable points (each worth 1), with the note "max 6"."""
from biology_lib import reg, text_part, row_, points_row

GRID = [
    {"level": "0", "marks": "0", "descriptor": "No rewardable material."},
    {"level": "1", "marks": "1–2", "descriptor": "A few relevant biological points are made, but they are mostly isolated statements with little or no explanation. Limited use of scientific terms."},
    {"level": "2", "marks": "3–4", "descriptor": "Several relevant points are made, some of them linked to give a partial explanation. The answer has some structure and uses some correct scientific terms."},
    {"level": "3", "marks": "5–6", "descriptor": "A detailed answer covering most of the main ideas, with points clearly linked to give a logical, well-sequenced explanation. Scientific terms are used accurately throughout."},
]
GENERAL = ("Marked with the levels grid: decide the level from the overall quality of the answer, then the mark within the level from how much "
           "of the indicative content is covered. Live papers for this course point-mark 6-mark questions; the indicative content can be used "
           "as a 'six of the following' list for point marking.")

# sub: [(ref(s), stem with {c}, [contexts], [indicative], credit_note, cw)]
EXT = {
    "structures.cells": [
        ("2.5B", "Explain why cells in {c} become specialised as the organism develops, and how specialisation helps the organism.",
         ["a human embryo", "a growing plant", "a multicellular animal"],
         ["early embryo cells are unspecialised / stem cells", "cells differentiate into different types", "different genes are switched on", "specialised cells have structures suited to one function",
          "e.g. red blood cells have no nucleus and carry oxygen", "e.g. root hair cells have a large surface area for absorption", "cells form tissues, organs and organ systems", "division of labour makes the organism more efficient"],
         "Credit any correctly described specialised cell with its adaptation.", "Explain"),
        ("2.6B", "Discuss the possible benefits and problems of using stem cells to treat {c}.",
         ["damaged nerve tissue", "type 1 diabetes", "heart muscle damaged by a heart attack"],
         ["stem cells can divide and differentiate into many cell types", "could replace damaged or lost cells", "embryonic stem cells can form any cell type", "adult stem cells are more limited",
          "cells from the patient avoid rejection", "rejection by the immune system if from a donor", "risk of uncontrolled division / tumours", "ethical concerns about using embryos", "treatments are expensive / still being tested"],
         "Both benefits and problems are needed for Level 3.", "Discuss"),
        ("2.4", "Compare the structure of {c} with the structure of an animal cell such as a cheek cell.",
         ["a palisade mesophyll cell", "a root hair cell", "a typical plant cell"],
         ["both have a nucleus, cytoplasm, cell membrane, mitochondria and ribosomes", "plant cell has a cellulose cell wall", "plant cell has a large permanent vacuole containing cell sap",
          "palisade / leaf cells have chloroplasts", "root hair cells have no chloroplasts", "animal cells have no cell wall, so shape is irregular", "animal cells may have small temporary vacuoles", "plant cells store starch; animal cells store glycogen"],
         "Comparative statements are needed; a list of structures of one cell only is limited to Level 1.", "Compare"),
    ],
    "structures.molecules": [
        ("2.11", "Explain how temperature affects the rate of a reaction controlled by {c}.",
         ["amylase", "catalase", "a protease"],
         ["as temperature rises, molecules gain kinetic energy", "more frequent collisions between enzyme and substrate", "more enzyme–substrate complexes form", "rate is fastest at the optimum temperature",
          "above the optimum, bonds holding the enzyme in shape break", "the active site changes shape", "the substrate no longer fits / is not complementary", "enzyme is denatured; this is permanent"],
         "Answers must link the rate to the active site for Level 3.", "Explain"),
        ("2.13", "Explain why {c} works well in one part of the gut but not in another.",
         ["pepsin (a stomach protease)", "pancreatic amylase", "lipase"],
         ["each enzyme has an optimum pH", "stomach is acidic (about pH 2)", "small intestine is slightly alkaline", "bile neutralises acid", "at the wrong pH the active site changes shape",
          "substrate cannot bind", "fewer enzyme–substrate complexes", "enzyme is denatured"],
         None, "Explain"),
        ("2.9", "Describe how a student could test {c} to find out which food groups it contains.",
         ["a sample of milk", "a breakfast cereal", "a mixture of foods"],
         ["grind with water / make a solution", "iodine solution turns blue-black with starch", "Benedict's solution and heat in a water bath", "turns orange/red (brick red) with glucose / reducing sugar",
          "biuret solution turns purple with protein", "ethanol then water gives a cloudy white emulsion with fat", "compare with a control of water", "safety: eye protection / care with hot water and ethanol"],
         "A test must include the reagent and the positive result to gain credit.", "Describe"),
        ("2.8", "Describe the structure of carbohydrates, proteins and lipids and explain why {c}.",
         ["they must be digested before they can be absorbed", "large molecules are broken into small units", "enzymes are needed to digest them"],
         ["carbohydrates contain carbon, hydrogen and oxygen", "starch / glycogen is made of glucose units", "proteins are made of amino acids", "proteins also contain nitrogen",
          "lipids are made of fatty acids and glycerol", "large molecules are insoluble / too large to pass through the gut wall", "digestion produces small soluble molecules", "which can be absorbed into the blood"],
         None, "Describe"),
        ("2.12", "Plan an investigation to find the effect of temperature on the activity of {c}.",
         ["amylase on starch", "catalase from potato", "protease on milk"],
         ["use a range of at least five temperatures", "water baths to control temperature", "same volume and concentration of enzyme and substrate", "control pH with a buffer",
          "measure the time / volume for a set end point", "repeat and calculate a mean", "boiled enzyme as a control", "calculate rate and plot against temperature"],
         "Credit relevant safety only if linked to the method.", "Plan"),
    ],
    "structures.plant-nutrition": [
        ("2.21", "Explain how the structure of a leaf of {c} is adapted for photosynthesis.",
         ["a broad-leaved tree", "a bean plant", "a sunflower"],
         ["large surface area to absorb light", "thin, so short diffusion distance for gases", "transparent upper epidermis lets light through", "palisade cells near the top with many chloroplasts",
          "chlorophyll absorbs light", "air spaces in spongy mesophyll allow diffusion of carbon dioxide", "stomata let carbon dioxide in and oxygen out", "xylem brings water; phloem removes sugars"],
         "Each feature must be linked to its function for Level 2 and above.", "Explain"),
        ("2.20", "Explain how {c} affects the rate of photosynthesis.",
         ["light intensity", "carbon dioxide concentration", "temperature"],
         ["rate increases as the factor increases", "the factor is limiting at low levels", "more energy / more raw material for photosynthesis", "eventually another factor becomes limiting",
          "graph levels off", "photosynthesis is controlled by enzymes", "very high temperature denatures enzymes", "named other limiting factor"],
         None, "Explain"),
        ("2.22", "Explain why plants need mineral ions and describe the effects of {c}.",
         ["a lack of magnesium ions", "a lack of nitrate ions", "a shortage of both magnesium and nitrate ions"],
         ["mineral ions are absorbed from soil by root hair cells", "by active transport", "magnesium is needed to make chlorophyll", "lack of magnesium causes yellow leaves",
          "less light absorbed so less photosynthesis", "nitrate is needed to make amino acids / proteins", "lack of nitrate causes poor / stunted growth", "fertilisers can replace these ions"],
         None, "Explain"),
        ("2.23", "Describe an experiment to show that {c} is needed for photosynthesis.",
         ["light", "carbon dioxide", "chlorophyll"],
         ["destarch the plant in the dark for 48 hours", "set up the test condition (cover part of a leaf with foil / soda lime in a bag / variegated leaf)", "leave in bright light for several hours",
          "boil the leaf in water", "place in hot ethanol to remove chlorophyll", "add iodine solution", "blue-black where starch is present", "orange-brown where there is no starch / compare with control"],
         None, "Describe"),
    ],
    "structures.human-nutrition": [
        ("2.27, 2.29", "Describe how {c} is digested and absorbed in the human body.",
         ["starch in a piece of bread", "protein in an egg", "fat in a portion of cheese"],
         ["mechanical digestion by teeth / churning in the stomach", "named enzyme breaks down the molecule", "e.g. amylase / maltase, protease / pepsin, lipase", "into small soluble molecules",
          "glucose / amino acids / fatty acids and glycerol", "digestion in the mouth, stomach or small intestine", "absorbed through the wall of the small intestine / villi", "into the blood / lacteals"],
         "The products must match the food named.", "Describe"),
        ("2.32", "Explain how the small intestine is adapted for {c}.",
         ["the absorption of digested food", "the efficient uptake of glucose and amino acids", "absorbing the products of digestion"],
         ["very long, so time for absorption", "folded with villi to increase surface area", "microvilli on the cells increase surface area further", "wall of villi is one cell thick / short diffusion distance",
          "good blood supply / capillaries", "maintains a concentration gradient", "lacteals absorb fatty acids and glycerol", "cells have many mitochondria for active transport"],
         None, "Explain"),
        ("2.30, 2.31", "Explain the role of bile in {c}.",
         ["the digestion of fats", "providing the right conditions for enzymes in the small intestine", "the digestion of a fatty meal"],
         ["bile is made in the liver", "stored in the gall bladder", "released into the duodenum", "bile is alkaline", "neutralises hydrochloric acid from the stomach", "gives the optimum pH for enzymes in the small intestine",
          "emulsifies fats into small droplets", "increases surface area for lipase"],
         None, "Explain"),
        ("2.24, 2.25", "Explain why {c} needs a balanced diet and describe what it should contain.",
         ["a teenager", "a pregnant woman", "an athlete"],
         ["carbohydrates and lipids provide energy", "protein for growth and repair", "vitamin C prevents scurvy", "vitamin D and calcium for bones and teeth", "iron to make haemoglobin",
          "fibre prevents constipation / helps peristalsis", "water for chemical reactions / transport", "energy needs depend on activity, age and pregnancy"],
         "Credit links between the person named and their particular needs.", "Explain"),
    ],
    "structures.gas-exchange-humans": [
        ("2.47", "Describe how {c}.",
         ["air is drawn into the lungs", "the lungs are ventilated", "breathing in and breathing out happen"],
         ["external intercostal muscles contract", "ribs move up and out", "diaphragm contracts and flattens", "volume of thorax increases", "pressure inside falls below atmospheric pressure",
          "air moves in", "on breathing out, muscles relax / diaphragm domes", "volume decreases, pressure increases, air forced out"],
         "Volume and pressure must be linked for Level 3.", "Describe"),
        ("2.48", "Explain how the alveoli are adapted for {c}.",
         ["efficient gas exchange", "the rapid diffusion of oxygen and carbon dioxide", "exchanging gases with the blood"],
         ["very large total surface area", "walls one cell thick / thin", "short diffusion distance", "surrounded by many capillaries", "good blood supply keeps a concentration gradient",
          "ventilation keeps a concentration gradient", "moist lining so gases dissolve", "oxygen diffuses into blood; carbon dioxide diffuses out"],
         None, "Explain"),
        ("2.49", "Explain the effects of smoking on {c}.",
         ["the lungs", "the circulatory system", "the health of a long-term smoker"],
         ["tar contains carcinogens that cause lung cancer", "tar damages cilia / mucus builds up", "chronic bronchitis / coughing", "emphysema: alveoli walls break down, less surface area",
          "carbon monoxide combines with haemoglobin", "less oxygen carried", "nicotine raises heart rate / blood pressure", "increased risk of coronary heart disease"],
         None, "Explain"),
    ],
    "structures.blood": [
        ("2.62", "Explain how white blood cells protect the body against {c}.",
         ["a bacterial infection", "a virus", "pathogens that enter a cut"],
         ["phagocytes engulf pathogens", "and digest them with enzymes", "lymphocytes recognise antigens", "lymphocytes produce antibodies", "antibodies are specific to an antigen",
          "antibodies cause pathogens to clump / mark them for destruction", "antitoxins neutralise toxins", "memory cells give a faster response later"],
         None, "Explain"),
        ("2.63B", "Explain how vaccination against {c} protects a person from the disease.",
         ["measles", "polio", "a strain of influenza"],
         ["vaccine contains dead / weakened pathogen or antigens", "lymphocytes recognise the antigen", "antibodies are made", "memory cells are produced", "on later infection memory cells respond",
          "antibodies produced faster", "and in larger amounts", "pathogen destroyed before symptoms develop"],
         "Credit a correctly described graph of primary and secondary response.", "Explain"),
        ("2.61, 2.64B", "Explain how {c} is adapted to its function.",
         ["a red blood cell", "the blood as a whole", "each type of blood cell"],
         ["red blood cells contain haemoglobin", "haemoglobin combines with oxygen", "no nucleus so more room for haemoglobin", "biconcave shape gives large surface area", "small and flexible to pass through capillaries",
          "plasma transports carbon dioxide, digested food, urea, hormones and heat", "platelets help blood to clot", "clotting prevents blood loss and entry of pathogens"],
         None, "Explain"),
    ],
    "structures.heart": [
        ("2.65", "Describe how the heart pumps blood {c}.",
         ["to the lungs and to the body", "through its four chambers", "in one complete heartbeat"],
         ["deoxygenated blood enters the right atrium from the vena cava", "oxygenated blood enters the left atrium from the pulmonary vein", "atria contract and push blood into ventricles",
          "valves between atria and ventricles open", "ventricles contract", "right ventricle pumps blood to lungs in pulmonary artery", "left ventricle pumps blood to the body in the aorta", "valves prevent backflow"],
         None, "Describe"),
        ("2.67", "Explain how {c} increases the risk of coronary heart disease.",
         ["a diet high in saturated fat", "smoking", "a lack of exercise"],
         ["fatty deposits / cholesterol build up in coronary arteries", "arteries narrow", "less blood flow to heart muscle", "less oxygen and glucose reach heart muscle", "heart muscle cannot respire",
          "muscle dies / heart attack", "blood clots may form and block arteries", "high blood pressure damages artery walls"],
         None, "Explain"),
        ("2.68", "Compare the structure of {c} and relate each to its function.",
         ["arteries and veins", "arteries, veins and capillaries", "capillaries and arteries"],
         ["arteries have thick muscular and elastic walls", "to withstand high pressure", "veins have thinner walls and a wide lumen", "veins have valves to prevent backflow", "blood in veins is at low pressure",
          "capillaries have walls one cell thick", "short diffusion distance for exchange", "capillaries have a narrow lumen"],
         "Structures must be linked to functions for Level 2 and above.", "Compare"),
        ("2.66", "Explain how and why heart rate changes {c}.",
         ["during exercise", "when a person is frightened", "during and after a race"],
         ["heart rate increases", "muscles respire more", "need more oxygen and glucose", "more carbon dioxide must be removed", "adrenaline is released by the adrenal glands",
          "adrenaline increases heart rate", "more blood pumped per minute", "rate returns to normal after"],
         None, "Explain"),
    ],
    "structures.excretion": [
        ("2.75B, 2.77B", "Describe how the kidney produces urine from {c}.",
         ["the blood plasma", "the blood entering the glomerulus", "blood with a high urea concentration"],
         ["high pressure in the glomerulus", "ultrafiltration into the Bowman's capsule", "small molecules such as water, glucose, urea and ions filtered", "large proteins and cells stay in the blood",
          "glucose selectively reabsorbed in the proximal convoluted tubule", "water reabsorbed in the collecting duct", "urine contains urea, water and ions", "urine passes to the bladder"],
         None, "Describe"),
        ("2.78B", "Explain how the body controls the water content of the blood when {c}.",
         ["a person is dehydrated", "a person has drunk a lot of water", "a person sweats heavily"],
         ["change detected by the hypothalamus / brain", "pituitary gland releases more / less ADH", "ADH travels in the blood", "ADH makes the collecting duct more permeable",
          "more water reabsorbed into the blood", "small volume of concentrated urine", "less ADH: less water reabsorbed", "large volume of dilute urine; negative feedback"],
         None, "Explain"),
        ("2.71, 2.72B", "Explain the roles of {c} in excretion.",
         ["the lungs, kidneys and skin", "the kidneys", "the organs that remove waste from the body"],
         ["excretion is the removal of metabolic waste", "lungs excrete carbon dioxide from respiration", "kidneys excrete urea", "urea made in the liver from excess amino acids", "kidneys remove excess water and ions",
          "skin excretes water, salts and urea in sweat", "kidneys also control water content / osmoregulation", "waste would be toxic if not removed"],
         None, "Explain"),
    ],
    "structures.homeostasis": [
        ("2.93", "Explain how the body responds to {c}.",
         ["a rise in body temperature", "a fall in body temperature", "very hot weather"],
         ["change detected by the brain / thermoregulatory centre", "sweating: sweat evaporates and removes heat", "vasodilation: arterioles widen", "more blood flows near the skin surface, heat lost by radiation",
          "when cold, vasoconstriction reduces blood flow to the skin", "shivering releases heat by respiration", "less sweating when cold", "negative feedback returns temperature to normal"],
         None, "Explain"),
        ("2.94", "Explain how insulin controls blood glucose concentration after {c}.",
         ["a meal rich in carbohydrate", "drinking a sugary drink", "eating breakfast"],
         ["blood glucose rises", "detected by the pancreas", "pancreas releases insulin", "insulin carried in the blood", "liver and muscle cells take in glucose",
          "glucose converted to glycogen", "blood glucose falls back to normal", "negative feedback"],
         None, "Explain"),
        ("2.94", "Compare nervous and hormonal control, using {c} as examples.",
         ["a reflex and the action of adrenaline", "the pupil reflex and insulin", "withdrawing a hand from heat and the menstrual cycle"],
         ["nervous control uses electrical impulses", "hormones are chemicals carried in the blood", "nervous responses are rapid", "hormonal responses are slower", "nervous responses are short-lived",
          "hormonal responses last longer", "nerves act on specific effectors", "hormones act on target organs / may affect several organs"],
         "Comparative statements are needed for Level 2 and above.", "Compare"),
        ("2.81", "Explain why homeostasis is important, using {c} as examples.",
         ["water content and body temperature", "body temperature", "water content of the blood"],
         ["homeostasis keeps internal conditions constant", "enzymes work best at an optimum temperature", "too hot: enzymes denature", "too cold: reactions too slow",
          "water content affects cells by osmosis", "too much water: cells swell / burst", "too little: cells shrink / lose water", "control by negative feedback"],
         None, "Explain"),
    ],
    "reproduction.evolution": [
        ("3.38", "Explain how natural selection could lead to {c}.",
         ["moths with dark wings becoming more common in polluted areas", "giraffes with longer necks", "a species of finch with larger beaks"],
         ["variation in the population", "caused by mutation / different alleles", "competition / selection pressure, e.g. predation or food supply", "individuals with the advantageous feature are more likely to survive",
          "they reproduce", "pass on the allele to offspring", "allele becomes more common over many generations", "this is evolution"],
         None, "Explain"),
        ("3.39", "Explain how {c} can become resistant to antibiotics and why this is a problem.",
         ["bacteria in a hospital", "the bacteria that cause tuberculosis", "MRSA"],
         ["random mutation gives resistance", "antibiotic kills non-resistant bacteria", "resistant bacteria survive", "and reproduce rapidly", "pass on the resistance gene", "population becomes mostly resistant",
          "infections are hard to treat", "overuse / not completing the course increases resistance"],
         None, "Explain"),
        ("3.38", "Suggest how {c} could change over many generations by natural selection.",
         ["a population of rabbits after a cold climate develops", "a population of fish in a lake with a new predator", "a population of insects after a pesticide is used"],
         ["variation exists in the population", "due to mutation / genetic variation", "a change in the environment / selection pressure", "some individuals are better adapted",
          "they survive and reproduce", "pass on favourable alleles", "over many generations", "the favourable feature becomes more common"],
         "Credit features relevant to the context named.", "Suggest"),
        ("3.39", "Discuss how doctors and patients can reduce the spread of {c}.",
         ["antibiotic-resistant bacteria", "resistant strains of bacteria in hospitals", "antibiotic resistance"],
         ["only prescribe antibiotics when needed", "not for viral infections", "complete the whole course", "so all bacteria are killed / resistant ones do not survive", "use different antibiotics",
          "good hygiene / hand washing in hospitals", "isolate infected patients", "reduce use in farming"],
         None, "Discuss"),
    ],
    "ecology.cycles": [
        ("4.10", "Describe how carbon is cycled between {c}.",
         ["the atmosphere, plants and animals", "living organisms and the air", "a forest and the atmosphere"],
         ["plants absorb carbon dioxide for photosynthesis", "carbon becomes part of carbohydrates / plant tissue", "animals eat plants and carbon passes along the food chain", "respiration by plants and animals releases carbon dioxide",
          "decomposers break down dead organisms and waste", "decomposers respire releasing carbon dioxide", "combustion of fossil fuels / wood releases carbon dioxide", "fossil fuels form from dead organisms over millions of years"],
         None, "Describe"),
        ("4.11B", "Describe the roles of bacteria in the nitrogen cycle and how {c}.",
         ["plants obtain nitrogen", "nitrogen from dead animals returns to plants", "nitrogen is returned to the air"],
         ["nitrogen-fixing bacteria convert nitrogen gas into ammonium / nitrogen compounds", "in root nodules of legumes or in soil", "decomposers break down proteins / urea into ammonium",
          "nitrifying bacteria convert ammonium to nitrite then nitrate", "plants absorb nitrate through roots", "nitrate used to make amino acids / proteins", "denitrifying bacteria convert nitrate to nitrogen gas",
          "lightning also fixes nitrogen"],
         None, "Describe"),
        ("4.11B", "Explain why {c} can improve the nitrogen content of soil.",
         ["growing peas or beans", "ploughing and draining waterlogged fields", "adding manure and compost"],
         ["legumes have root nodules with nitrogen-fixing bacteria", "nitrogen gas fixed into ammonium / nitrogen compounds", "ploughing / draining adds oxygen to the soil", "aerobic conditions help nitrifying bacteria",
          "reduces denitrifying bacteria that need anaerobic conditions", "decomposers break down manure releasing ammonium", "nitrifying bacteria make nitrate", "nitrate absorbed for protein synthesis"],
         None, "Explain"),
        ("4.10", "Explain how {c} affects the amount of carbon dioxide in the atmosphere.",
         ["cutting down and burning a forest", "burning fossil fuels in power stations", "planting large areas of new forest"],
         ["photosynthesis removes carbon dioxide from the air", "fewer trees means less carbon dioxide absorbed", "burning / combustion releases carbon dioxide", "decomposition of remaining wood releases carbon dioxide",
          "fossil fuels contain carbon locked away for millions of years", "new trees absorb carbon dioxide as they grow", "carbon stored in wood", "carbon dioxide is a greenhouse gas"],
         None, "Explain"),
    ],
    "ecology.human-impact": [
        ("4.17", "Explain how {c} can lead to the death of fish in a lake.",
         ["fertiliser washed from nearby farmland", "leaching of nitrates after heavy rain", "runoff from fields after fertiliser is applied"],
         ["nitrate / phosphate enters the water", "algae grow rapidly (algal bloom)", "light is blocked from plants below", "plants cannot photosynthesise and die", "decomposers / bacteria feed on dead material",
          "bacteria multiply and respire aerobically", "oxygen in the water is used up", "fish die from lack of oxygen"],
         None, "Explain"),
        ("4.15", "Explain how {c} could lead to global warming and describe possible effects.",
         ["an increase in carbon dioxide", "an increase in methane from farming", "the release of greenhouse gases"],
         ["named greenhouse gases: carbon dioxide, methane, water vapour, nitrous oxide, CFCs", "short-wave radiation from the Sun reaches Earth", "Earth re-emits longer-wave infrared radiation",
          "greenhouse gases absorb and re-radiate heat", "more gas causes an enhanced greenhouse effect", "mean global temperature rises", "ice caps melt / sea levels rise", "climate change / extinction / changes in species distribution"],
         None, "Explain"),
        ("4.18B", "Explain the effects of deforestation on {c}.",
         ["the soil", "the atmosphere", "the local environment"],
         ["fewer trees so less photosynthesis", "less carbon dioxide absorbed / more in atmosphere", "burning releases carbon dioxide", "less oxygen produced", "soil erosion as roots no longer hold soil",
          "loss of soil nutrients / leaching", "less transpiration so less water vapour / rain", "flooding / disruption of the water cycle", "loss of habitats and biodiversity"],
         None, "Explain"),
        ("4.12, 4.16", "Explain how {c} affects living organisms.",
         ["sulfur dioxide from burning coal", "untreated sewage entering a river", "carbon monoxide from car exhausts"],
         ["sulfur dioxide dissolves to form acid rain", "acid rain damages leaves / kills trees", "acidifies lakes so fish die", "carbon monoxide combines irreversibly with haemoglobin", "less oxygen carried by blood",
          "sewage provides food for bacteria", "bacteria use oxygen in respiration", "aquatic animals die from lack of oxygen"],
         "Credit only points relevant to the pollutant named.", "Explain"),
    ],
    "resources.microorganisms": [
        ("5.8", "Explain why conditions inside an industrial fermenter used to grow {c} are carefully controlled.",
         ["a fungus that makes penicillin", "bacteria that make a useful protein", "microorganisms for food production"],
         ["aseptic conditions: sterilised with steam", "prevents contamination by other microorganisms", "nutrients supply energy / raw materials for growth", "optimum temperature for enzymes",
          "water jacket removes heat from respiration", "optimum pH monitored with a probe", "oxygen supplied for aerobic respiration", "stirring mixes contents evenly"],
         None, "Explain"),
        ("5.5, 5.6", "Explain the role of yeast in {c}.",
         ["making bread", "brewing beer", "making bread rise"],
         ["yeast respires anaerobically", "glucose → ethanol + carbon dioxide", "enzymes in yeast / flour break down starch to sugar", "carbon dioxide bubbles make dough rise / beer fizzy",
          "warm temperature for enzyme activity", "baking kills yeast", "ethanol evaporates during baking", "ethanol remains in beer"],
         None, "Explain"),
        ("5.7", "Describe how {c} is made using bacteria.",
         ["yoghurt", "natural yoghurt from cow's milk", "yoghurt on a large scale"],
         ["milk is pasteurised / heated to kill microorganisms", "cooled to about 40 °C", "Lactobacillus bacteria added", "incubated at a warm temperature", "bacteria ferment lactose", "lactic acid produced",
          "pH falls so milk proteins coagulate / thicken", "cooled to stop the process; acid stops harmful bacteria"],
         None, "Describe"),
        ("5.9B", "Explain how fish farmers can produce large numbers of {c}.",
         ["salmon", "tilapia", "trout"],
         ["water quality monitored / oxygen and waste removed", "fish kept in nets / tanks to protect from predators", "feeding controlled with high-protein food", "less energy wasted on movement",
          "disease controlled with antibiotics or pesticides", "selective breeding for fast growth", "separate species / ages to avoid fighting", "problems: disease spreads easily / pollution / escapes"],
         None, "Explain"),
    ],
    "resources.breeding-gm": [
        ("5.12, 5.13, 5.14", "Describe how {c} can be produced using genetic modification.",
         ["human insulin", "a human protein for medicine", "insulin made by bacteria"],
         ["the human gene is cut out with a restriction enzyme", "the plasmid is cut with the same restriction enzyme", "sticky ends join", "ligase joins the gene into the plasmid",
          "recombinant plasmid is a vector", "inserted into bacteria", "bacteria grown in a fermenter", "insulin extracted and purified"],
         None, "Describe"),
        ("5.10, 5.11", "Describe how a farmer could use selective breeding to produce {c}.",
         ["cows that give more milk", "wheat plants with a higher yield", "sheep with thicker wool"],
         ["choose parents with the desired feature", "breed them together", "select the offspring with the best feature", "breed these together", "repeat over many generations",
          "until all offspring show the feature", "reduced genetic variation", "risk of inherited disease / inbreeding"],
         None, "Describe"),
        ("5.15, 5.16", "Discuss the advantages and disadvantages of growing {c}.",
         ["genetically modified crops", "crops modified to resist insect pests", "herbicide-resistant crops"],
         ["higher yield / more food", "resistant to pests so less pesticide used", "herbicide resistance makes weed control easier", "can grow in drought / poor soil", "improved nutrition, e.g. extra vitamin",
          "genes may spread to wild plants", "effects on food chains / insects", "seeds can be expensive / ethical concerns"],
         "Both advantages and disadvantages are needed for Level 3.", "Discuss"),
        ("5.10, 5.15", "Compare selective breeding and genetic modification as ways of producing {c}.",
         ["better crop plants", "disease-resistant plants", "improved farm animals"],
         ["selective breeding uses natural reproduction", "genetic modification transfers genes directly", "GM can use genes from another species / transgenic", "GM is faster",
          "selective breeding takes many generations", "both produce organisms with useful features", "both can reduce genetic variation", "GM needs restriction enzymes, ligase and vectors"],
         "Comparative statements are needed for Level 2 and above.", "Compare"),
    ],
}


# Indicative content tailored to the exact context named in the question: (subtopic, item index, context) -> points
IND = {
    ("structures.plant-nutrition", 1, "light intensity"): [
        "light provides the energy for photosynthesis", "absorbed by chlorophyll", "as light intensity increases the rate increases",
        "light is the limiting factor at low intensity", "rate is proportional to light intensity at first", "at high intensity the rate levels off",
        "another factor, e.g. carbon dioxide concentration or temperature, becomes limiting", "very bright light may damage chlorophyll / cause stomata to close"],
    ("structures.plant-nutrition", 1, "carbon dioxide concentration"): [
        "carbon dioxide is a raw material / reactant for photosynthesis", "it diffuses in through the stomata", "as concentration increases the rate increases",
        "carbon dioxide is the limiting factor at low concentration", "more carbon dioxide is combined to make glucose", "at high concentration the rate levels off",
        "another factor, e.g. light intensity or temperature, becomes limiting", "glasshouse growers add carbon dioxide to increase yield"],
    ("structures.plant-nutrition", 1, "temperature"): [
        "photosynthesis is controlled by enzymes", "rising temperature gives molecules more kinetic energy", "more collisions between enzymes and substrates / more enzyme–substrate complexes",
        "so the rate rises as temperature increases", "temperature is limiting at low temperatures", "rate is fastest at the optimum temperature (about 25–35 °C)",
        "above the optimum the enzymes denature / the active site changes shape", "so the rate falls rapidly", "at high temperature stomata may close, reducing carbon dioxide uptake"],
    ("structures.plant-nutrition", 3, "light"): [
        "destarch the plant in the dark for 48 hours", "cover part of a leaf with black paper / foil", "leave the plant in bright light for several hours",
        "remove the leaf and boil it in water", "place in hot ethanol (in a water bath) to remove chlorophyll", "rinse and add iodine solution",
        "uncovered part turns blue-black: starch present", "covered part stays orange-brown: no starch, so light is needed"],
    ("structures.plant-nutrition", 3, "carbon dioxide"): [
        "destarch the plant in the dark for 48 hours", "enclose a leaf in a clear bag containing soda lime / sodium hydroxide", "soda lime absorbs carbon dioxide",
        "control leaf in a bag without soda lime", "leave in bright light for several hours", "boil the leaf, then place it in hot ethanol to remove chlorophyll",
        "add iodine solution", "leaf with no carbon dioxide stays orange-brown; control turns blue-black"],
    ("structures.plant-nutrition", 3, "chlorophyll"): [
        "use a plant with variegated (green and white) leaves", "destarch the plant in the dark for 48 hours", "leave in bright light for several hours",
        "draw the pattern of green and white areas", "boil the leaf, then place it in hot ethanol to remove chlorophyll", "add iodine solution",
        "green areas turn blue-black: starch present", "white areas stay orange-brown: no starch, so chlorophyll is needed"],
    ("structures.human-nutrition", 0, "starch in a piece of bread"): [
        "teeth chew the bread / mechanical digestion increases surface area", "salivary amylase starts to digest starch in the mouth", "amylase breaks starch into maltose",
        "amylase is denatured by acid in the stomach", "pancreatic amylase continues digestion in the small intestine", "maltase breaks maltose into glucose",
        "glucose is absorbed through the villi of the small intestine", "into the blood capillaries"],
    ("structures.human-nutrition", 0, "protein in an egg"): [
        "teeth chew the food / mechanical digestion increases surface area", "churning in the stomach mixes food with gastric juice", "pepsin / protease in the stomach digests protein",
        "hydrochloric acid gives the low optimum pH for pepsin", "proteases from the pancreas continue digestion in the small intestine", "protein is broken down into amino acids",
        "amino acids are absorbed through the villi of the small intestine", "into the blood capillaries"],
    ("structures.human-nutrition", 0, "fat in a portion of cheese"): [
        "teeth chew the food / mechanical digestion", "bile from the liver / gall bladder enters the duodenum", "bile emulsifies fat into small droplets",
        "increasing the surface area for lipase", "bile neutralises stomach acid, giving the optimum pH", "lipase from the pancreas digests fat",
        "into fatty acids and glycerol", "absorbed through the villi into the lacteals"],
    ("structures.gas-exchange-humans", 2, "the lungs"): [
        "tar contains carcinogens", "which cause mutations / lung cancer", "tar paralyses / damages cilia", "mucus builds up and is not removed",
        "chronic bronchitis / smoker's cough", "infections are more likely", "emphysema: walls of alveoli break down", "smaller surface area so less gas exchange / breathlessness"],
    ("structures.gas-exchange-humans", 2, "the circulatory system"): [
        "carbon monoxide combines with haemoglobin", "forming carboxyhaemoglobin, so less oxygen is carried", "heart must work harder to supply oxygen", "nicotine increases heart rate",
        "nicotine narrows blood vessels / raises blood pressure", "fatty deposits build up in arteries", "blood is more likely to clot", "increased risk of coronary heart disease / heart attack / stroke"],
    ("structures.blood", 2, "a red blood cell"): [
        "contains haemoglobin", "haemoglobin combines with oxygen in the lungs to form oxyhaemoglobin", "oxyhaemoglobin releases oxygen in respiring tissues",
        "no nucleus, so more room for haemoglobin", "biconcave shape gives a large surface area for diffusion of oxygen", "thin, so a short diffusion distance",
        "small and flexible to squeeze through capillaries", "very many red cells give a large total surface area"],
    ("structures.blood", 2, "the blood as a whole"): [
        "red blood cells contain haemoglobin to carry oxygen", "no nucleus / biconcave shape for oxygen transport", "plasma transports carbon dioxide, digested food, urea and hormones",
        "plasma distributes heat around the body", "phagocytes engulf pathogens", "lymphocytes produce antibodies", "platelets help blood to clot", "clotting prevents blood loss and entry of pathogens"],
    ("structures.blood", 2, "each type of blood cell"): [
        "red blood cells contain haemoglobin to carry oxygen", "red cells have no nucleus, so more room for haemoglobin", "red cells are biconcave for a large surface area",
        "phagocytes change shape to engulf pathogens", "phagocytes contain enzymes to digest pathogens", "lymphocytes produce specific antibodies",
        "lymphocytes form memory cells", "platelets (cell fragments) help blood to clot"],
    ("structures.heart", 1, "a diet high in saturated fat"): [
        "saturated fat raises blood cholesterol", "fatty deposits / cholesterol build up in the walls of coronary arteries", "arteries narrow", "less blood flows to the heart muscle",
        "less oxygen and glucose reach the heart muscle", "heart muscle cannot respire aerobically", "a blood clot may block the narrowed artery", "heart muscle dies / heart attack"],
    ("structures.heart", 1, "smoking"): [
        "nicotine increases heart rate and blood pressure", "high blood pressure damages artery walls", "fatty deposits build up at damaged areas of coronary arteries",
        "smoking makes blood more likely to clot", "carbon monoxide reduces oxygen carried by haemoglobin", "coronary arteries narrow / are blocked",
        "less oxygen reaches the heart muscle", "heart muscle dies / heart attack"],
    ("structures.heart", 1, "a lack of exercise"): [
        "less energy is used, so a person may become overweight / obese", "higher blood pressure", "higher blood cholesterol", "fatty deposits build up in coronary arteries",
        "arteries narrow", "less blood, oxygen and glucose reach the heart muscle", "a blood clot may block an artery", "heart muscle dies / heart attack"],
    ("structures.heart", 2, "arteries and veins"): [
        "arteries have thick walls with muscle and elastic tissue", "to withstand / maintain high pressure", "elastic tissue recoils to even out blood flow", "arteries have a narrow lumen",
        "veins have thinner walls", "veins have a wide lumen so blood flows easily at low pressure", "veins have valves", "valves prevent backflow"],
    ("structures.heart", 2, "capillaries and arteries"): [
        "arteries have thick walls with muscle and elastic tissue", "to withstand high pressure", "elastic tissue recoils to even out blood flow",
        "capillaries have walls one cell thick", "giving a short diffusion distance", "for exchange of substances with tissues", "capillaries have a very narrow lumen / red cells pass in single file",
        "capillaries are very numerous so a large surface area"],
    ("structures.heart", 3, "when a person is frightened"): [
        "the brain detects the danger", "adrenal glands release adrenaline", "adrenaline is carried in the blood", "adrenaline increases heart rate",
        "more blood pumped per minute", "more oxygen and glucose supplied to muscles", "muscles can respire faster for 'fight or flight'", "heart rate returns to normal when the danger passes"],
    ("structures.excretion", 2, "the kidneys"): [
        "blood enters the glomerulus at high pressure", "ultrafiltration of small molecules into the Bowman's capsule", "large proteins and blood cells stay in the blood",
        "glucose is selectively reabsorbed in the proximal convoluted tubule", "water is reabsorbed in the loop of Henle / collecting duct", "ADH controls how much water is reabsorbed",
        "urea, excess water and ions leave as urine", "urine passes along the ureter to the bladder"],
    ("structures.homeostasis", 2, "a reflex and the action of adrenaline"): [
        "a reflex uses electrical impulses along neurones", "adrenaline is a hormone carried in the blood", "the reflex response is very rapid", "adrenaline acts more slowly",
        "the reflex is short-lived", "the effect of adrenaline lasts longer", "a reflex acts on one effector, e.g. a muscle", "adrenaline affects several target organs, e.g. heart and liver"],
    ("structures.homeostasis", 2, "the pupil reflex and insulin"): [
        "the pupil reflex uses electrical impulses along neurones", "insulin is a hormone carried in the blood", "light is detected by the retina",
        "impulses pass along a reflex arc to the muscles of the iris", "the pupil changes size in less than a second", "insulin is secreted by the pancreas",
        "insulin causes the liver to convert glucose to glycogen", "insulin acts over minutes or hours / its effect lasts longer"],
    ("structures.homeostasis", 2, "withdrawing a hand from heat and the menstrual cycle"): [
        "withdrawal uses electrical impulses along neurones", "menstrual cycle hormones are carried in the blood", "withdrawal is very rapid", "the hormonal effect is slow",
        "withdrawal is short-lived", "the menstrual cycle lasts about 28 days", "withdrawal acts on one effector, a muscle", "hormones such as oestrogen and progesterone act on target organs, e.g. the uterus"],
    ("structures.homeostasis", 3, "body temperature"): [
        "homeostasis keeps internal conditions constant", "body temperature is kept at about 37 °C", "enzymes work best at an optimum temperature", "too hot: enzymes denature / active site changes shape",
        "too cold: reactions are too slow", "detected by the thermoregulatory centre in the brain", "responses such as sweating, shivering, vasodilation, vasoconstriction", "control by negative feedback"],
    ("structures.homeostasis", 3, "water content of the blood"): [
        "homeostasis keeps internal conditions constant", "water content affects cells by osmosis", "too much water: cells swell / may burst", "too little water: cells shrink / lose water",
        "detected by the hypothalamus", "pituitary gland releases ADH", "ADH controls water reabsorption in the kidney", "control by negative feedback"],
    ("ecology.cycles", 2, "growing peas or beans"): [
        "peas and beans are legumes", "they have root nodules", "containing nitrogen-fixing bacteria", "which convert nitrogen gas into ammonium / nitrogen compounds",
        "the plant uses these to make amino acids / proteins", "when the plants die or are ploughed in, decomposers release ammonium", "nitrifying bacteria convert ammonium to nitrate", "nitrate is then available for the next crop"],
    ("ecology.cycles", 2, "ploughing and draining waterlogged fields"): [
        "ploughing / draining adds air / oxygen to the soil", "aerobic conditions favour nitrifying bacteria", "nitrifying bacteria convert ammonium to nitrite then nitrate",
        "denitrifying bacteria need anaerobic / waterlogged conditions", "so fewer denitrifying bacteria", "less nitrate converted to nitrogen gas", "more nitrate stays in the soil",
        "nitrate absorbed by roots to make proteins"],
    ("ecology.cycles", 2, "adding manure and compost"): [
        "manure and compost contain proteins and urea / nitrogen compounds", "decomposers (bacteria and fungi) break these down", "releasing ammonium (ammonification)",
        "nitrifying bacteria convert ammonium to nitrite", "and then to nitrate", "compost improves soil structure / aeration", "aeration favours nitrifying bacteria and reduces denitrification",
        "plants absorb nitrate by active transport to make amino acids / proteins"],
    ("ecology.cycles", 3, "cutting down and burning a forest"): [
        "trees remove carbon dioxide by photosynthesis", "fewer trees so less carbon dioxide is absorbed", "burning releases carbon dioxide", "carbon stored in wood is released quickly",
        "decomposers respire as they break down remaining wood / roots", "releasing more carbon dioxide", "so the carbon dioxide concentration in the air rises", "carbon dioxide is a greenhouse gas / contributes to global warming"],
    ("ecology.cycles", 3, "burning fossil fuels in power stations"): [
        "fossil fuels contain carbon", "the carbon was locked away for millions of years", "from organisms that did not decay", "combustion releases carbon dioxide",
        "carbon dioxide is released faster than plants can absorb it", "so the carbon dioxide concentration in the air rises", "carbon dioxide is a greenhouse gas", "contributes to global warming / climate change"],
    ("ecology.cycles", 3, "planting large areas of new forest"): [
        "young trees photosynthesise", "absorbing carbon dioxide from the air", "growing trees store carbon in wood / cellulose", "carbon is removed from the atmosphere for many years",
        "trees also respire, but take in more carbon dioxide than they release while growing", "so the carbon dioxide concentration falls / rises less", "reduces the greenhouse effect", "wood must not be burned later, or the carbon is released"],
    ("ecology.human-impact", 2, "the soil"): [
        "tree roots no longer hold the soil", "soil is washed away by rain / blown away (erosion)", "no leaf litter, so fewer nutrients returned to the soil", "minerals are leached out by rain",
        "soil becomes infertile", "less transpiration so the water cycle is disrupted", "eroded soil causes flooding / silts rivers", "crops grow poorly on the cleared land"],
    ("ecology.human-impact", 2, "the atmosphere"): [
        "fewer trees so less photosynthesis", "less carbon dioxide absorbed", "burning trees releases carbon dioxide", "decomposition of remaining wood releases carbon dioxide",
        "carbon dioxide concentration rises", "enhanced greenhouse effect / global warming", "less oxygen released", "less transpiration so less water vapour / rainfall"],
    ("ecology.human-impact", 3, "sulfur dioxide from burning coal"): [
        "sulfur in coal is oxidised when it burns", "sulfur dioxide dissolves in rainwater", "forming acid rain", "acid rain damages leaves / kills trees",
        "acid rain leaches minerals from soil", "lakes become acidic", "fish and other aquatic organisms die", "sulfur dioxide irritates the lungs / causes breathing problems"],
    ("ecology.human-impact", 3, "untreated sewage entering a river"): [
        "sewage contains organic matter and nitrates / phosphates", "it provides food for bacteria / decomposers", "bacteria multiply", "bacteria respire aerobically",
        "oxygen in the water is used up", "fish and other aquatic animals die from lack of oxygen", "nitrates cause algal blooms / eutrophication", "sewage may contain pathogens that cause disease"],
    ("ecology.human-impact", 3, "carbon monoxide from car exhausts"): [
        "carbon monoxide comes from incomplete combustion of fuel", "it is colourless and odourless", "it combines with haemoglobin", "binding is irreversible / stronger than oxygen",
        "less oxygen is carried by the blood", "less aerobic respiration in cells", "causes tiredness, headaches or death", "heart must work harder / strain on the heart"],
    ("resources.microorganisms", 1, "brewing beer"): [
        "barley seeds are germinated / malted", "enzymes break down starch into sugar (maltose)", "yeast is added to the sugary solution", "yeast respires anaerobically",
        "glucose → ethanol + carbon dioxide", "ethanol is the alcohol in beer", "carbon dioxide makes beer fizzy", "warm temperature for yeast enzymes / airtight container to keep it anaerobic"],
}
for k in [("ecology.human-impact", 2, "the local environment")]:
    IND[k] = IND[("ecology.human-impact", 2, "the soil")][:4] + ["loss of habitats", "loss of biodiversity / species become extinct",
                                                               "less transpiration so less rainfall", "more flooding"]
# point-marked wording for notes that still referred to levels
NOTE = {
    "Both benefits and problems are needed for Level 3.": "Credit both benefits and problems; at least one of each is needed for full marks.",
    "Comparative statements are needed; a list of structures of one cell only is limited to Level 1.": "Points must be comparative; a list of the structures of one cell only gains a maximum of 2 marks.",
    "Answers must link the rate to the active site for Level 3.": "Credit links between rate and the active site.",
    "Each feature must be linked to its function for Level 2 and above.": "Each feature must be linked to its function to gain the mark.",
    "Volume and pressure must be linked for Level 3.": "Credit volume and pressure changes only when linked.",
    "Structures must be linked to functions for Level 2 and above.": "Each structure must be linked to its function to gain the mark.",
    "Comparative statements are needed for Level 2 and above.": "Points must be comparative and may use the examples named.",
    "Both advantages and disadvantages are needed for Level 3.": "At least one advantage and one disadvantage are needed for full marks.",
}


def gen(sub):
    out = []
    nm = sub.split(".")[-1]
    items = EXT[sub]
    SUFFIX = ["", "\n\nYour answer should include clear links between the points you make.",
              "\n\nUse your knowledge of biology to support your answer."]
    combos = [(i, j, f) for f in range(3) for j in range(3) for i in range(len(items))]
    seen = set()
    for n, (i, j, f) in enumerate(combos):
        if len(out) >= 15:
            break
        refs, stem, ctxs, ind, credit, cw = items[i]
        c = ctxs[j]
        text = stem.format(c=c) + SUFFIX[(f + j) % 3]
        if text in seen:
            continue
        seen.add(text)
        ind = IND.get((sub, i, c), ind)
        assert len(ind) >= 6, (sub, i, c)
        credit = NOTE.get(credit, credit)
        parts = [text_part("", text, 6, 12)]
        note = "max 6. " + (credit or "Credit any other valid biological points.")
        rows = [points_row("", 6, ind, cw, note, "AO1")]
        out.append(dict(parts=parts, rows=rows, refs=[r.strip() for r in refs.split(",")], cw=cw,
                        diff="7-9" if n % 2 == 0 else "4-6", template=f"{nm}-ext"))
    return out


def _make(sub):
    @reg(sub, "extended", f"{sub.split('.')[-1]}-ext")
    def f():
        return gen(sub)
    return f


for _s in EXT:
    _make(_s)
