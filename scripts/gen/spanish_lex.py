"""Shared lexicon for the Spanish (Cambridge 0530) generator: names, places and
picture-style vocabulary sets.  All original word lists.

Vocabulary categories: "spanish form=English picture caption; ...".  The Spanish
form is inserted into a template exactly as written; the caption is what the
"picture" shows (the bank writes pictures as words: "[picture: apples]").
"""

MALE = ("Pablo Javier Diego Andrés Mateo Daniel Hugo Álvaro Sergio Tomás Marcos Rubén Iván Raúl "
        "Nicolás Gonzalo Joaquín Felipe Emilio Rodrigo Óscar Adrián Lucas Martín Bruno Samuel "
        "Alejandro Manuel Jorge Carlos Ignacio Santiago Héctor Fernando Gabriel Julián").split()
FEMALE = ("Lucía Marta Elena Carmen Paula Sara Alba Laura Irene Claudia Natalia Julia Sofía Valentina "
          "Camila Inés Noelia Rocío Beatriz Patricia Ana Andrea Celia Lorena Nuria Silvia Teresa "
          "Ximena Daniela Gabriela Mariana Pilar Victoria Adriana Elisa Carolina").split()
SURNAMES = ("García Martínez López Sánchez Romero Navarro Torres Ramos Gil Serrano Molina Ortiz Delgado "
            "Castro Vargas Rojas Herrera Medina Aguilar Flores Rivera Mendoza Cabrera Vidal Fuentes "
            "Campos Paredes Salazar Ibáñez Morales").split()

# city, country, nationality m, nationality f
PLACES = [
    ("Sevilla", "España", "español", "española"), ("Valencia", "España", "español", "española"),
    ("Bilbao", "España", "español", "española"), ("Salamanca", "España", "español", "española"),
    ("Granada", "España", "español", "española"), ("Zaragoza", "España", "español", "española"),
    ("Málaga", "España", "español", "española"), ("Santander", "España", "español", "española"),
    ("Ciudad de México", "México", "mexicano", "mexicana"), ("Guadalajara", "México", "mexicano", "mexicana"),
    ("Oaxaca", "México", "mexicano", "mexicana"), ("Puebla", "México", "mexicano", "mexicana"),
    ("Bogotá", "Colombia", "colombiano", "colombiana"), ("Medellín", "Colombia", "colombiano", "colombiana"),
    ("Cali", "Colombia", "colombiano", "colombiana"),
    ("Lima", "Perú", "peruano", "peruana"), ("Arequipa", "Perú", "peruano", "peruana"),
    ("Cusco", "Perú", "peruano", "peruana"),
    ("Buenos Aires", "Argentina", "argentino", "argentina"), ("Mendoza", "Argentina", "argentino", "argentina"),
    ("Rosario", "Argentina", "argentino", "argentina"),
    ("Santiago", "Chile", "chileno", "chilena"), ("Valparaíso", "Chile", "chileno", "chilena"),
    ("Montevideo", "Uruguay", "uruguayo", "uruguaya"), ("Quito", "Ecuador", "ecuatoriano", "ecuatoriana"),
    ("Guayaquil", "Ecuador", "ecuatoriano", "ecuatoriana"), ("La Paz", "Bolivia", "boliviano", "boliviana"),
    ("Asunción", "Paraguay", "paraguayo", "paraguaya"), ("San José", "Costa Rica", "costarricense", "costarricense"),
    ("Panamá", "Panamá", "panameño", "panameña"), ("Santo Domingo", "República Dominicana", "dominicano", "dominicana"),
    ("Caracas", "Venezuela", "venezolano", "venezolana"), ("Antigua", "Guatemala", "guatemalteco", "guatemalteca"),
]

CATS_RAW = {
    # food and drink
    "fruta": "manzanas=apples; plátanos=bananas; fresas=strawberries; naranjas=oranges; uvas=grapes; "
             "peras=pears; cerezas=cherries; melocotones=peaches; piñas=pineapples; limones=lemons",
    "verdura": "zanahorias=carrots; tomates=tomatoes; patatas=potatoes; cebollas=onions; pimientos=peppers; "
               "lechugas=lettuces; champiñones=mushrooms; guisantes=peas",
    "bebida": "un zumo de naranja=a glass of orange juice; un café=a cup of coffee; un té=a cup of tea; "
              "agua con gas=a bottle of sparkling water; un batido de chocolate=a chocolate milkshake; "
              "una limonada=a glass of lemonade; un chocolate caliente=a mug of hot chocolate; leche=a glass of milk",
    "plato": "una tortilla de patatas=a Spanish omelette; una ensalada=a salad; una pizza=a pizza; "
             "una sopa de verduras=a bowl of vegetable soup; pollo con arroz=chicken with rice; "
             "pescado a la plancha=grilled fish; una hamburguesa=a burger; espaguetis=a plate of spaghetti; "
             "unos tacos=tacos; una paella=a paella",
    "postre": "un helado de fresa=a strawberry ice cream; un flan=a crème caramel; una tarta de chocolate=a chocolate cake; "
              "fruta del tiempo=fresh fruit; un yogur=a yoghurt; unas galletas=biscuits; arroz con leche=rice pudding",
    "comida_hora": "el desayuno=breakfast; el almuerzo=lunch; la merienda=an afternoon snack; la cena=dinner",
    # body and health
    "cuerpo": "la cabeza=head; la espalda=back; el estómago=stomach; la garganta=throat; el brazo=arm; "
              "la pierna=leg; el pie=foot; la rodilla=knee; el oído=ear; la mano=hand; el cuello=neck",
    "remedio": "unas pastillas=a packet of tablets; un jarabe=a bottle of cough syrup; una crema=a tube of cream; "
               "una venda=a bandage; unas tiritas=plasters; unas gotas=eye drops",
    "salud_lugar": "a la farmacia=a chemist's; al hospital=a hospital; al dentista=a dentist's chair; "
                   "al centro de salud=a health centre; a urgencias=an emergency department",
    # transport and places
    "transporte": "en tren=a train; en autobús=a bus; en metro=an underground train; en avión=a plane; "
                  "en barco=a boat; en bicicleta=a bicycle; en taxi=a taxi; a pie=someone walking; en coche=a car",
    "lugar_ciudad": "la estación=a railway station; el ayuntamiento=a town hall; el museo=a museum; "
                    "la biblioteca=a library; el mercado=a market; la piscina=a swimming pool; "
                    "el polideportivo=a sports centre; la catedral=a cathedral; el parque=a park; "
                    "la oficina de correos=a post office; el puerto=a harbour; el estadio=a stadium",
    "direccion": "todo recto=an arrow pointing straight ahead; a la derecha=an arrow pointing right; "
                 "a la izquierda=an arrow pointing left; al final de la calle=the end of a street; "
                 "en la esquina=a street corner; enfrente del banco=a building opposite a bank; "
                 "al lado de la farmacia=a shop next to a chemist's; detrás de la iglesia=the back of a church",
    "billete": "un billete de ida=a single ticket; un billete de ida y vuelta=a return ticket; "
               "un abono mensual=a monthly travel pass; un billete de primera clase=a first-class ticket",
    # time
    "hora": "a las ocho y media=8:30; a las nueve menos cuarto=8:45; a las diez y cuarto=10:15; "
            "a las once=11:00; a las doce y media=12:30; a las cuatro y veinte=4:20; "
            "a las siete menos diez=6:50; a las seis y cuarto=6:15; a las tres y media=3:30; a la una=1:00",
    "dia": "el lunes=Monday; el martes=Tuesday; el miércoles=Wednesday; el jueves=Thursday; "
           "el viernes=Friday; el sábado=Saturday; el domingo=Sunday",
    "mes": "en enero=January; en marzo=March; en abril=April; en junio=June; en julio=July; "
           "en septiembre=September; en octubre=October; en diciembre=December",
    "estacion": "la primavera=spring blossom; el verano=a summer beach; el otoño=autumn leaves; el invierno=winter snow",
    "fecha": "el tres de mayo=3 May; el quince de agosto=15 August; el veinte de febrero=20 February; "
             "el uno de noviembre=1 November; el doce de octubre=12 October; el veintiocho de junio=28 June",
    # weather and nature
    "tiempo": "hace sol=sunshine; está lloviendo=rain; hace viento=wind; está nevando=snow; hay niebla=fog; "
              "hace mucho calor=a thermometer showing 38°C; hace frío=a person shivering; hay tormenta=a thunderstorm",
    "paisaje": "la montaña=mountains; el río=a river; el lago=a lake; el bosque=a forest; la playa=a beach; "
               "el desierto=a desert; la selva=a rainforest; la isla=an island; el volcán=a volcano",
    "animal": "un caballo=a horse; un perro=a dog; un gato=a cat; un conejo=a rabbit; un pájaro=a bird; "
              "una tortuga=a tortoise; un pez=a goldfish; una vaca=a cow; una oveja=a sheep; un loro=a parrot",
    "reciclaje": "las botellas de plástico=plastic bottles; el papel=old newspapers; las latas=drinks cans; "
                 "el vidrio=glass jars; la ropa vieja=old clothes; las pilas=batteries",
    # people and home
    "familiar": "mi abuela=a grandmother; mi abuelo=a grandfather; mi tío=an uncle; mi tía=an aunt; "
                "mi primo=a male cousin; mi hermana pequeña=a little sister; mi hermano mayor=an older brother; "
                "mi madre=a mother; mi padre=a father",
    "caracter": "simpática=a smiling face; tímida=a shy face; habladora=a person talking a lot; "
                "seria=a serious face; generosa=a person sharing sweets; divertida=a person laughing",
    "pelo": "el pelo rizado=curly hair; el pelo liso=straight hair; el pelo corto=short hair; "
            "el pelo largo=long hair; el pelo rubio=blond hair; barba=a beard",
    "habitacion": "la cocina=a kitchen; el salón=a living room; el cuarto de baño=a bathroom; "
                  "el jardín=a garden; el comedor=a dining room; la terraza=a balcony; el garaje=a garage; "
                  "mi dormitorio=a bedroom",
    "mueble": "la mesa=a table; el sofá=a sofa; la estantería=a bookcase; el armario=a wardrobe; "
              "la lámpara=a lamp; la alfombra=a rug; el espejo=a mirror; la cama=a bed",
    "tarea": "pasar la aspiradora=a vacuum cleaner; lavar los platos=a sink full of dishes; "
             "hacer la cama=a bed being made; sacar la basura=a rubbish bin; planchar=an iron; "
             "poner la mesa=a table being laid; regar las plantas=a watering can; cocinar=a pan on a cooker",
    # leisure
    "deporte": "al tenis=a tennis racket; al baloncesto=a basketball; al fútbol=a football; "
               "al voleibol=a volleyball; al golf=a golf club; al béisbol=a baseball bat; al hockey=a hockey stick",
    "actividad": "nadar=a swimmer; montar a caballo=a horse rider; patinar=roller skates; ir de pesca=a fishing rod; "
                 "hacer escalada=a climbing wall; bailar=dancers; pintar=a paintbrush; leer=a pile of books; "
                 "hacer senderismo=hiking boots; ir en piragua=a canoe",
    "instrumento": "la guitarra=a guitar; el piano=a piano; la batería=a drum kit; el violín=a violin; "
                   "la flauta=a flute; la trompeta=a trumpet",
    "pelicula": "de miedo=a ghost; de dibujos animados=a cartoon character; de ciencia ficción=a spaceship; "
                "romántica=a heart; de acción=a car chase; del oeste=a cowboy; de humor=a clown",
    "evento": "un concierto=a concert stage; una obra de teatro=a theatre stage; un partido=a football match; "
              "una exposición=paintings in a gallery; un festival de cine=a film festival poster; un circo=a circus tent",
    # special occasions
    "regalo": "un reloj=a watch; una pulsera=a bracelet; un libro=a book; unos auriculares=headphones; "
              "una camiseta=a T-shirt; unas flores=a bunch of flowers; un videojuego=a video game; una bufanda=a scarf",
    "fiesta_cosa": "una tarta=a birthday cake; unas velas=candles; unos globos=balloons; unos fuegos artificiales=fireworks; "
                   "unas máscaras=masks; un disfraz=a fancy-dress costume; unas invitaciones=invitation cards",
    # shopping and clothes
    "ropa": "una chaqueta=a jacket; unos vaqueros=jeans; una falda=a skirt; unas botas=boots; un jersey=a jumper; "
            "una gorra=a cap; un vestido=a dress; unas zapatillas de deporte=trainers; un abrigo=a coat; un bañador=a swimsuit",
    "color": "rojo=red; azul=blue; verde=green; negro=black; blanco=white; amarillo=yellow; gris=grey; marrón=brown; "
             "rosa=pink; naranja=orange; morado=purple",
    "color_f": "roja=red; azul=blue; verde=green; negra=black; blanca=white; amarilla=yellow; gris=grey; marrón=brown; "
               "rosa=pink; naranja=orange; morada=purple",
    "color_pl": "rojos=red; azules=blue; verdes=green; negros=black; blancos=white; amarillos=yellow; grises=grey; "
                "marrones=brown; rosas=pink; morados=purple",
    # measurements and materials
    "forma": "redonda=a round shape; cuadrada=a square shape; rectangular=a rectangle; triangular=a triangle; "
             "ovalada=an oval",
    "tamano": "muy grande=something very large; pequeña=something small; enorme=something enormous; "
              "larga=something long; corta=something short; estrecha=something narrow; ancha=something wide; "
              "alta=something tall; baja=something low",
    "peso": "un kilo=a 1 kg weight; medio kilo=a ½ kg weight; doscientos gramos=a 200 g packet; "
            "tres kilos=a 3 kg bag; cien gramos=a 100 g packet; dos kilos=a 2 kg bag",
    "volumen": "un litro=a 1 litre bottle; dos litros=a 2 litre bottle; medio litro=a ½ litre bottle; "
               "tres litros=a 3 litre carton; litro y medio=a 1.5 litre bottle",
    "longitud": "un metro=a 1 m tape measure; dos metros=a 2 m tape measure; cincuenta centímetros=a 50 cm ruler; "
                "treinta centímetros=a 30 cm ruler; metro y medio=a 1.5 m tape measure",
    "distancia": "dos kilómetros=a sign showing 2 km; quinientos metros=a sign showing 500 m; diez kilómetros=a sign showing 10 km; "
                 "cien metros=a sign showing 100 m; cinco kilómetros=a sign showing 5 km",
    "materia": "de madera=wood; de metal=metal; de plástico=plastic; de cristal=glass; de piedra=stone; "
               "de oro=gold; de cartón=cardboard; de plata=silver",
    "tela": "de algodón=cotton; de lana=wool; de cuero=leather; de seda=silk; de plástico reciclado=recycled plastic; de lino=linen",
    # places in the world
    "punto": "en el norte=a map with the north marked; en el sur=a map with the south marked; "
             "en el este=a map with the east marked; en el oeste=a map with the west marked; "
             "en el centro=a map with the centre marked; en la costa=a map with the coast marked",
    "continente": "en Europa=Europe; en Asia=Asia; en África=Africa; en América del Sur=South America; "
                  "en América del Norte=North America; en Oceanía=Oceania",
    "nacionalidad": "alemana=a German flag; francesa=a French flag; italiana=an Italian flag; inglesa=an English flag; "
                    "japonesa=a Japanese flag; china=a Chinese flag; portuguesa=a Portuguese flag; griega=a Greek flag; "
                    "canadiense=a Canadian flag; marroquí=a Moroccan flag",
    "festividad": "la Navidad=a Christmas tree; la Semana Santa=an Easter procession; el Año Nuevo=New Year fireworks; "
                  "el Día de Muertos=a decorated altar with marigolds; el Carnaval=carnival costumes; "
                  "el Ramadán=a crescent moon over a family meal; el Diwali=oil lamps; el Día de Reyes=three kings with gifts; "
                  "una boda=a wedding",
    "tienda": "a la panadería=a bakery; a la carnicería=a butcher's; a la librería=a bookshop; "
              "a la frutería=a greengrocer's; a la zapatería=a shoe shop; a la pastelería=a cake shop; "
              "al quiosco=a newspaper kiosk; a la floristería=a flower shop",
    "precio": "tres euros con cincuenta=€3.50; cuatro euros=€4.00; seis euros con veinte=€6.20; "
              "nueve euros con noventa=€9.90; doce euros=€12.00; quince euros con cincuenta=€15.50; "
              "veinte euros=€20.00; dos euros con setenta y cinco=€2.75",
    "pago": "con tarjeta=a bank card; en efectivo=banknotes and coins; con el móvil=a mobile phone being used to pay; "
            "con un cheque regalo=a gift voucher",
    # technology
    "aparato": "el móvil=a mobile phone; el portátil=a laptop; la tableta=a tablet; los auriculares=headphones; "
               "la cámara=a camera; el cargador=a phone charger; la impresora=a printer; el reloj inteligente=a smartwatch",
    "accion_digital": "mandar un mensaje=a text message; hacer una videollamada=a video call; "
                      "subir una foto=a photo being uploaded; descargar música=music being downloaded; "
                      "buscar información=a search engine; jugar en línea=an online game; ver un vídeo=a video player",
    # education and work
    "asignatura": "las matemáticas=maths; la historia=history; la geografía=geography; el inglés=English; "
                  "la química=chemistry; la biología=biology; la música=music; el dibujo=art; "
                  "la educación física=PE; la informática=computing",
    "material": "una regla=a ruler; un diccionario=a dictionary; una calculadora=a calculator; "
                "un estuche=a pencil case; unas tijeras=scissors; un cuaderno=an exercise book; una mochila=a school bag",
    "lugar_escuela": "el laboratorio=a science laboratory; el gimnasio=a sports hall; la biblioteca=a school library; "
                     "el comedor=a canteen; el patio=a playground; la sala de informática=a computer room; "
                     "el salón de actos=an assembly hall",
    "profesion": "médico=a doctor; enfermero=a nurse; profesor=a teacher; cocinero=a chef; piloto=a pilot; "
                 "veterinario=a vet; periodista=a journalist; arquitecto=an architect; policía=a police officer; "
                 "mecánico=a mechanic; abogado=a lawyer; ingeniero=an engineer",
    "lugar_trabajo": "en una oficina=an office; en un hospital=a hospital; en una tienda=a shop; "
                     "en un hotel=a hotel; en una granja=a farm; en un restaurante=a restaurant; "
                     "en una fábrica=a factory; en un aeropuerto=an airport",
    # holidays and travel
    "alojamiento": "un hotel=a hotel; un camping=a campsite; un albergue juvenil=a youth hostel; "
                   "un apartamento=a block of holiday flats; una casa rural=a country cottage; un barco=a cruise ship",
    "equipaje": "la maleta=a suitcase; el pasaporte=a passport; las gafas de sol=sunglasses; la crema solar=sun cream; "
                "el mapa=a map; la toalla=a beach towel; la mochila=a rucksack; la cámara de fotos=a camera",
    "pais": "a Italia=Italy; a Francia=France; a Japón=Japan; a Portugal=Portugal; a Marruecos=Morocco; "
            "a Canadá=Canada; a Grecia=Greece; a Egipto=Egypt; a China=China; a Brasil=Brazil",
    "idioma": "el francés=French; el alemán=German; el chino=Chinese; el portugués=Portuguese; "
              "el árabe=Arabic; el italiano=Italian; el japonés=Japanese; el inglés=English",
}


def _parse(raw):
    out = []
    for chunk in raw.split(";"):
        chunk = chunk.strip()
        if not chunk:
            continue
        es, en = chunk.split("=", 1)
        out.append((es.strip(), en.strip()))
    return out


CATS = {k: _parse(v) for k, v in CATS_RAW.items()}

# ---------------------------------------------------------------- place profiles
# One coherent, true record per place.  A narrator's text is built from ONE record:
# reg = part of the country (as said in Spanish), tags = true attributes that facts
# may require ("cond" field of a fact, e.g. "temperate", "!capital", "spain").
#   capital   national capital            coast   on (or right by) the sea
#   temperate clear four seasons, short winter days      mount  mountains in or next to the city
#   hotsummer very hot summers            mild    mild all year (no great heat or cold)
#   dry       dry climate / little summer rain           oso    bears live wild in the country
#   north     northern hemisphere (school year ends in June, August = summer)
PROFILE = {
    "Sevilla": ("el sur", "spain temperate hotsummer dry north"),
    "Valencia": ("el este", "spain coast temperate hotsummer dry north"),
    "Bilbao": ("el norte", "spain coast temperate mount mild north"),
    "Salamanca": ("el oeste", "spain temperate dry north"),
    "Granada": ("el sur", "spain temperate mount hotsummer dry north"),
    "Zaragoza": ("el norte", "spain temperate hotsummer dry north"),
    "Málaga": ("el sur", "spain coast temperate mount hotsummer dry north"),
    "Santander": ("el norte", "spain coast temperate mount mild north"),
    "Ciudad de México": ("el centro", "capital mount mild north"),
    "Guadalajara": ("el oeste", "mild north"),
    "Oaxaca": ("el sur", "mount north"),
    "Puebla": ("el centro", "mount mild north"),
    "Bogotá": ("el centro", "capital mount mild oso north"),
    "Medellín": ("el oeste", "mount mild oso north"),
    "Cali": ("el oeste", "mount oso north"),
    "Lima": ("el centro", "capital coast dry mild oso"),
    "Arequipa": ("el sur", "mount dry oso"),
    "Cusco": ("el sur", "mount oso"),
    "Buenos Aires": ("el este", "capital temperate hotsummer"),
    "Mendoza": ("el oeste", "temperate mount hotsummer dry"),
    "Rosario": ("el centro", "temperate hotsummer"),
    "Santiago": ("el centro", "capital temperate mount hotsummer dry"),
    "Valparaíso": ("el centro", "coast temperate mild dry"),
    "Montevideo": ("el sur", "capital coast temperate"),
    "Quito": ("el norte", "capital mount mild oso north"),
    "Guayaquil": ("el oeste", "coast oso"),
    "La Paz": ("el oeste", "capital mount oso"),
    "Asunción": ("el centro", "capital hotsummer"),
    "San José": ("el centro", "capital mount mild north"),
    "Panamá": ("el centro", "capital coast north"),
    "Santo Domingo": ("el sur", "capital coast north"),
    "Caracas": ("el norte", "capital mount mild oso north"),
    "Antigua": ("el sur", "mount mild north"),
}
REGIONS = ["el norte", "el sur", "el este", "el oeste", "el centro"]
CURRENCY = {"España": "euros", "México": "pesos", "Colombia": "pesos", "Argentina": "pesos", "Chile": "pesos",
            "Uruguay": "pesos", "Perú": "soles", "Ecuador": "dólares", "Bolivia": "bolivianos",
            "Paraguay": "guaraníes", "Costa Rica": "colones", "Panamá": "balboas", "República Dominicana": "pesos",
            "Venezuela": "bolívares", "Guatemala": "quetzales"}
# Narrators for texts about LEARNING Spanish come from non-Spanish-speaking places.
LEARNER_PLACES = [
    ("Londres", "Inglaterra", "inglés", "inglesa"), ("Manchester", "Inglaterra", "inglés", "inglesa"),
    ("Edimburgo", "Escocia", "escocés", "escocesa"), ("Dublín", "Irlanda", "irlandés", "irlandesa"),
    ("Toronto", "Canadá", "canadiense", "canadiense"), ("Sídney", "Australia", "australiano", "australiana"),
    ("Cardiff", "Gales", "galés", "galesa"), ("Auckland", "Nueva Zelanda", "neozelandés", "neozelandesa"),
]
LEARNER_PROFILE = {"Londres": ("el sur", "learner capital temperate north"), "Manchester": ("el norte", "learner temperate north"),
                   "Edimburgo": ("el este", "learner capital coast temperate north"), "Dublín": ("el este", "learner capital coast temperate north"),
                   "Toronto": ("el este", "learner temperate north"), "Sídney": ("el este", "learner coast"),
                   "Cardiff": ("el sur", "learner capital coast temperate north"), "Auckland": ("el norte", "learner coast mild")}
for _c, _co, _m, _f in PLACES + LEARNER_PLACES:
    assert _c in PROFILE or _c in LEARNER_PROFILE, _c

# Key concepts for picture/option ambiguity checks: values that share a concept must
# never appear as two options of one task (a French flag vs France vs French).
CONCEPT = {}
for _grp in ("alemana Alemania alemán", "francesa Francia francés", "italiana Italia italiano", "inglesa Inglaterra inglés",
             "japonesa Japón japonés", "china China chino", "portuguesa Portugal portugués", "griega Grecia griego",
             "canadiense Canadá", "marroquí Marruecos árabe", "egipcio Egipto", "brasileña Brasil"):
    _ws = _grp.split()
    for _w in _ws:
        CONCEPT[_w.lower()] = _ws[0]
# extra words a sentence may use for the same thing as a picture
SYNONYMS = {"dormitorio": "habitación cuarto cama", "habitación": "dormitorio cuarto", "móvil": "teléfono celular",
            "salón": "sofá", "cocina": "cocinar", "cocinar": "cocina", "gimnasio": "deporte", "biblioteca": "libro libros leer",
            "leer": "libro libros biblioteca", "piscina": "nadar", "nadar": "piscina", "cama": "dormitorio dormir",
            "comedor": "comer", "playa": "mar", "baño": "ducha", "portátil": "ordenador", "ordenador": "portátil"}
