"""Pictures for the Spanish picture items (l-short, r-pictures).

The bank keeps each picture as "[picture: <English caption>]".  The site draws a picture for every caption
listed here and falls back to the caption in a box for anything else (colours, days, months, flags,
languages: things a black-and-white line drawing cannot show without printing the English word).

Spec format: "icon1+icon2|label"
  icons   Tabler outline icon names (MIT licence, https://tabler.io/icons); "clock:H:M" draws a clock face,
          "body:<part>" draws a figure with that body part ringed.
  label   optional short text printed under the drawing (numbers, units and prices only, never English words).

Build the site's picture file with:
  python scripts/gen/spanish_pictures.py <path to @tabler/icons package>
which writes site/src/lib/spanish-pictures.json (only the icons used here).
"""
import json
import re
import sys
from pathlib import Path

PICS = {
    # times / prices / quantities
    "10:15": "clock:10:15", "11:00": "clock:11:00", "12:30": "clock:12:30", "1:00": "clock:1:00", "3:30": "clock:3:30",
    "4:20": "clock:4:20", "6:15": "clock:6:15", "6:50": "clock:6:50", "8:30": "clock:8:30", "8:45": "clock:8:45",
    "1 November": "calendar|1/11", "12 October": "calendar|12/10", "15 August": "calendar|15/8", "20 February": "calendar|20/2",
    "28 June": "calendar|28/6", "3 May": "calendar|3/5",
    "€12.00": "tag|12,00 €", "€15.50": "tag|15,50 €", "€2.75": "tag|2,75 €", "€20.00": "tag|20,00 €", "€3.50": "tag|3,50 €",
    "€4.00": "tag|4,00 €", "€6.20": "tag|6,20 €", "€9.90": "tag|9,90 €",
    "a 1 kg weight": "weight|1 kg", "a ½ kg weight": "weight|½ kg", "a 2 kg bag": "shopping-bag|2 kg", "a 3 kg bag": "shopping-bag|3 kg",
    "a 100 g packet": "package|100 g", "a 200 g packet": "package|200 g",
    "a 1 litre bottle": "bottle|1 l", "a 1.5 litre bottle": "bottle|1,5 l", "a 2 litre bottle": "bottle|2 l", "a ½ litre bottle": "bottle|½ l",
    "a 3 litre carton": "milk|3 l",
    "a 1 m tape measure": "ruler-measure|1 m", "a 1.5 m tape measure": "ruler-measure|1,5 m", "a 2 m tape measure": "ruler-measure|2 m",
    "a 30 cm ruler": "ruler|30 cm", "a 50 cm ruler": "ruler|50 cm",
    "a sign showing 10 km": "road-sign|10 km", "a sign showing 100 m": "road-sign|100 m", "a sign showing 2 km": "road-sign|2 km",
    "a sign showing 5 km": "road-sign|5 km", "a sign showing 500 m": "road-sign|500 m",
    "a thermometer showing 38°C": "thermometer|38 °C",
    # food and drink
    "apples": "apple+apple", "bananas": "banana", "cherries": "cherry", "grapes": "grape", "lemons": "lemon+lemon", "oranges": "lemon-2+lemon-2",
    "carrots": "carrot+carrot", "peppers": "pepper", "mushrooms": "mushroom", "fresh fruit": "apple+banana", "biscuits": "cookie",
    "a burger": "burger", "a pizza": "pizza", "a salad": "salad", "a bowl of vegetable soup": "soup", "a yoghurt": "cup",
    "a glass of milk": "milk", "a glass of orange juice": "glass-full", "a glass of lemonade": "glass-full+lemon",
    "a cup of coffee": "coffee", "a cup of tea": "cup", "a chocolate milkshake": "milkshake", "a mug of hot chocolate": "mug",
    "a bottle of sparkling water": "bottle", "a strawberry ice cream": "ice-cream", "a chocolate cake": "cake", "a birthday cake": "cake",
    "a plate of spaghetti": "tools-kitchen-2+bowl", "grilled fish": "fish+grill", "chicken with rice": "meat+bowl",
    "breakfast": "egg-fried+coffee", "lunch": "tools-kitchen-2+soup", "dinner": "tools-kitchen-2+moon", "an afternoon snack": "cookie+milk",
    "rice pudding": "bowl-spoon",
    # health
    "a packet of tablets": "pills", "a bottle of cough syrup": "medicine-syrup", "a tube of cream": "first-aid-kit", "a bandage": "bandage",
    "plasters": "bandage+bandage", "eye drops": "eye+droplet", "sun cream": "sun+bottle", "a chemist's": "building-store+first-aid-kit",
    "a hospital": "building-hospital", "a dentist's chair": "dental", "a doctor": "stethoscope", "a health centre": "building+stethoscope",
    "an emergency department": "ambulance", "a nurse": "nurse",
    "head": "body:head", "back": "body:back", "stomach": "body:stomach", "throat": "body:throat", "arm": "body:arm", "leg": "body:leg",
    "foot": "body:foot", "hand": "body:hand", "knee": "body:knee", "neck": "body:neck", "ear": "ear",
    # transport and directions
    "a train": "train", "a bus": "bus", "an underground train": "train+building-tunnel", "a plane": "plane", "a car": "car", "a taxi": "car|TAXI",
    "a bicycle": "bike", "a boat": "sailboat", "a cruise ship": "ship", "someone walking": "walk", "a canoe": "kayak",
    "an arrow pointing left": "arrow-big-left", "an arrow pointing right": "arrow-big-right", "an arrow pointing straight ahead": "arrow-big-up",
    "a single ticket": "ticket|→", "a return ticket": "ticket|⇄", "a passport": "e-passport", "a suitcase": "luggage", "a rucksack": "backpack",
    "a map": "map", "a railway station": "train+building", "an airport": "building-airport", "a bus stop": "bus-stop",
    "a map with the north marked": "map-north", "a map with the south marked": "map-south", "a map with the east marked": "map-east",
    "a map with the west marked": "map-west", "a map with the centre marked": "map-pin", "a map with the coast marked": "building-lighthouse",
    # town
    "a town hall": "building-community", "a museum": "building-bank", "a cathedral": "building-church", "a library": "books",
    "a park": "trees+fountain", "a market": "building-store", "a shop": "building-store", "a bakery": "bread", "a cake shop": "cake-roll",
    "a butcher's": "meat", "a bookshop": "books+building-store", "a shoe shop": "shoe+building-store", "a flower shop": "flower+building-store",
    "a greengrocer's": "carrot+apple", "a post office": "mail+building", "a hotel": "building+bed", "a restaurant": "tools-kitchen-2",
    "a swimming pool": "pool", "a sports centre": "ball-football+building", "a stadium": "building-stadium", "a factory": "building-factory",
    "a harbour": "anchor", "a newspaper kiosk": "news", "a campsite": "tent", "a youth hostel": "bed+users",
    "a playground": "monkeybar", "a garage": "car-garage", "a farm": "building-cottage+fence", "a country cottage": "building-cottage",
    "an office": "briefcase", "a block of holiday flats": "building+beach",
    # weather, landscape, animals
    "sunshine": "sun", "rain": "cloud-rain", "wind": "wind", "snow": "cloud-snow", "fog": "cloud-fog", "a thunderstorm": "cloud-storm",
    "spring blossom": "flower", "a summer beach": "beach", "autumn leaves": "leaf-maple", "winter snow": "snowflake",
    "mountains": "mountain", "a river": "building-bridge", "a forest": "trees", "a beach": "beach", "a desert": "cactus",
    "a volcano": "volcano", "a lake": "sailboat", "an island": "beach", "a rainforest": "trees+cloud-rain",
    "a horse": "horse", "a dog": "dog", "a cat": "cat", "a rabbit": "carrot+paw", "a bird": "feather", "a parrot": "feather",
    "a cow": "milk+paw", "a goldfish": "fish", "a tortoise": "paw", "a sheep": "paw",
    # environment
    "plastic bottles": "bottle+bottle", "old newspapers": "news+recycle", "drinks cans": "recycle", "glass jars": "recycle", "old clothes": "shirt+recycle",
    "a rubbish bin": "trash", "batteries": "battery-2", "cardboard": "package",
    # people and family
    "a grandmother": "old", "a grandfather": "old", "a mother": "woman", "a father": "man", "a male cousin": "man", "a little sister": "mood-kid",
    "an older brother": "man", "an aunt": "woman", "an uncle": "man",
    "a smiling face": "mood-smile", "a shy face": "mood-look-down", "a serious face": "mood-neutral", "a person laughing": "mood-xd",
    "a person talking a lot": "message-dots+message-dots", "a person shivering": "temperature-minus",
    "a beard": "moustache", "curly hair": "user|~~~",
    # home
    "a kitchen": "tools-kitchen-2+fridge", "a living room": "sofa+device-tv", "a bathroom": "bath", "a bedroom": "bed", "a dining room": "table+tools-kitchen-2",
    "a garden": "plant+fence", "a balcony": "window", "a table": "table", "a sofa": "sofa", "a bookcase": "books", "a wardrobe": "hanger",
    "a bed": "bed", "a lamp": "lamp",
    "a vacuum cleaner": "vacuum-cleaner", "a sink full of dishes": "tools-kitchen-2+droplet", "an iron": "ironing",
    "a bed being made": "bed+pillow", "a table being laid": "table+tools-kitchen-2", "a watering can": "plant+droplet",
    "a pan on a cooker": "cooker",
    # free time
    "a tennis racket": "ball-tennis", "a basketball": "ball-basketball", "a football": "ball-football", "a volleyball": "ball-volleyball",
    "a baseball bat": "ball-baseball", "a golf club": "golf", "a hockey stick": "ice-skating",
    "a swimmer": "swimming", "a horse rider": "horse", "roller skates": "roller-skating", "a fishing rod": "fish-hook", "a climbing wall": "mountain",
    "a guitar": "guitar-pick", "a piano": "piano", "a flute": "music",
    "a ghost": "ghost", "a cartoon character": "mickey", "a spaceship": "rocket", "a car chase": "car+car",
    "a concert stage": "microphone-2+music", "a theatre stage": "masks-theater", "a football match": "ball-football+building-stadium",
    "a circus tent": "building-circus", "a clown": "building-circus",
    "a watch": "clock", "a bracelet": "diamond", "a book": "book", "headphones": "headphones", "a gift voucher": "gift-card",
    "balloons": "balloon+balloon", "candles": "candle+candle", "fireworks": "sparkles", "invitation cards": "mail-opened",
    "a camera": "camera", "a video game": "device-gamepad-2", "an online game": "device-gamepad-2+world",
    "a wedding": "rings", "a Christmas tree": "christmas-tree", "masks": "mask", "carnival costumes": "masks-theater+confetti",
    "New Year fireworks": "sparkles+confetti", "dancers": "music+users",
    # clothes
    "a jacket": "jacket", "a coat": "jacket", "a T-shirt": "shirt", "a cap": "cap-straight", "boots": "shoe", "trainers": "shoe",
    "hiking boots": "shoe+mountain", "sunglasses": "sunglasses", "a swimsuit": "swimming", "a beach towel": "beach",
    # shapes and sizes
    "a round shape": "circle", "a square shape": "square", "a rectangle": "rectangle", "a triangle": "triangle", "an oval": "oval",
    # school and work
    "maths": "math", "art": "palette", "music": "music", "chemistry": "flask", "biology": "dna", "computing": "device-desktop",
    "geography": "world", "history": "building-castle", "PE": "run",
    "a calculator": "calculator", "a ruler": "ruler", "a dictionary": "vocabulary", "an exercise book": "notebook", "a pencil case": "pencil",
    "a school bag": "backpack", "scissors": "scissors", "a paintbrush": "brush", "a pile of books": "books",
    "a science laboratory": "flask+microscope", "a computer room": "device-desktop+device-desktop", "a school library": "books+school",
    "a sports hall": "ball-basketball+building", "an assembly hall": "school+users", "a canteen": "tools-kitchen-2+school",
    "a teacher": "chalkboard-teacher", "a chef": "chef-hat", "a police officer": "shield", "a pilot": "plane+user", "a mechanic": "tools",
    "a vet": "paw+stethoscope", "an engineer": "helmet", "a journalist": "news+pencil", "an architect": "ruler-measure+building",
    "a lawyer": "scale",
    # technology and money
    "a mobile phone": "device-mobile", "a laptop": "device-laptop", "a tablet": "device-tablet", "a smartwatch": "device-watch",
    "a printer": "printer", "a phone charger": "plug", "a text message": "device-mobile-message", "a video call": "video",
    "a search engine": "search", "a photo being uploaded": "photo+upload", "music being downloaded": "music+download",
    "a video player": "player-play",
    "a bank card": "credit-card", "banknotes and coins": "cash-banknote+coins", "a mobile phone being used to pay": "device-mobile+credit-card-pay",
    # festivals, art and odds and ends
    "a bunch of flowers": "flower+flower", "a heart": "heart", "a crescent moon over a family meal": "moon+tools-kitchen-2",
    "three kings with gifts": "crown+gift", "a person sharing sweets": "candy+users", "a monthly travel pass": "id-badge+bus",
    "a first-class ticket": "ticket|1ª", "paintings in a gallery": "frame+frame", "a film festival poster": "movie",
    "an Easter procession": "candle+building-church", "a decorated altar with marigolds": "candle+flower", "a cowboy": "horse+lasso",
    "a fancy-dress costume": "mask", "lettuces": "leaf+leaf", "wood": "wood",
    "something tall": "arrows-vertical", "something wide": "arrows-horizontal", "something very large": "arrows-maximize",
    "something small": "arrows-minimize",
}


def load_icon(pkg: Path, name: str) -> str:
    src = (pkg / "icons" / "outline" / f"{name}.svg").read_text()
    inner = re.search(r">\s*(.*)</svg>", src, re.S).group(1)
    inner = re.sub(r'<path stroke="none" d="M0 0h24v24H0z" fill="none"\s*/>', "", inner)
    return re.sub(r"\s+", " ", inner).strip()


def main(pkg):
    pkg = Path(pkg)
    names = {p.stem for p in (pkg / "icons" / "outline").glob("*.svg")}
    icons, missing = {}, []
    for cap, spec in PICS.items():
        for ic in spec.split("|")[0].split("+"):
            if ic.startswith(("clock:", "body:")):
                continue
            if ic not in names:
                missing.append((cap, ic))
            else:
                icons[ic] = load_icon(pkg, ic)
    if missing:
        sys.exit("missing icons: " + ", ".join(f"{c} -> {i}" for c, i in missing))
    out = Path(__file__).resolve().parents[2] / "site" / "src" / "lib" / "spanish-pictures.json"
    out.write_text(json.dumps({"licence": "Icons from Tabler Icons (MIT licence, https://tabler.io/icons), (c) Paweł Kuna",
                               "pictures": PICS, "icons": icons}, ensure_ascii=False, separators=(",", ":")))
    print(f"{len(PICS)} pictures, {len(icons)} icons -> {out}")


if __name__ == "__main__":
    main(sys.argv[1])
