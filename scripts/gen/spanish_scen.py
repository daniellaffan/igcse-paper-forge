"""Role-play and form scenario records for the Spanish (Cambridge 0530) generator.

Each role play / form is ONE scenario record: its context, the examiner's role and register,
and only the questions (or form fields) that belong to that scenario.  Original content.

RP[ref]   = [dict(ctx, role, formal, slots=[5 x "q#expected" alternatives, one per line])]
            formal=True: the examiner (shop assistant, receptionist, official...) uses usted throughout.
FORMS[ref] = [dict(title, ctx, gaps="label#accept#refuse#n" lines)]
"""

RP = {}
FORMS = {}

# ---------------------------------------------------------------------------------- A
RP["A1"] = [
    dict(ctx="Estás en {city} de vacaciones. Quieres visitar un museo con tu amigo/amiga. Llamas por teléfono a tu amigo/amiga para organizar la visita.",
         role="el amigo / la amiga", formal=False, slots=[
             "¡Hola! ¿Qué día quieres ir al museo?#States a day, e.g. *El sábado.*\n¡Hola! ¿Cuándo te viene bien ir al museo?#States a day or a time of day, e.g. *El domingo por la mañana.*",
             "¿A qué hora quedamos?#Gives a time, e.g. *A las diez.*",
             "¿Dónde quedamos?#States a meeting place, e.g. *En la plaza.*\n¿Cómo vamos al museo? [PAUSA] ¿Por qué?#Means of transport + reason, e.g. *En autobús porque es barato.*",
             "¿Qué hiciste el fin de semana pasado?#An activity in a past tense, e.g. *Fui al cine.*\n¿Qué hiciste ayer por la tarde?#An activity in a past tense, e.g. *Jugué al tenis.*",
             "¿Qué te gustaría hacer después del museo?#An activity using a conditional, e.g. *Me gustaría comer pizza.*"]),
    dict(ctx="Estás de intercambio en {city}. Quieres ir a un concierto con tu compañero/compañera de clase. Hablas con él/ella para organizarlo.",
         role="el compañero / la compañera", formal=False, slots=[
             "¡Hola! ¿Qué día quieres ir al concierto?#States a day, e.g. *El viernes.*",
             "¿A qué hora salimos de casa?#Gives a time, e.g. *A las siete y media.*",
             "¿Cómo vamos al concierto? [PAUSA] ¿Por qué?#Means of transport + reason, e.g. *En metro porque es rápido.*",
             "¿Qué hiciste el fin de semana pasado?#An activity in a past tense, e.g. *Fui a la playa.*\n¿A qué concierto fuiste la última vez?#Past tense, e.g. *Fui a un concierto de rock.*",
             "¿Qué vas a hacer mañana?#An activity in a future time frame, e.g. *Voy a estudiar.*\n¿Qué te gustaría hacer después del concierto?#Conditional, e.g. *Me gustaría cenar algo.*"]),
]
RP["A2"] = [
    dict(ctx="Estás en {city} con una familia. Vas al mercado para comprar fruta para la cena. Hablas con el vendedor / la vendedora.",
         role="el vendedor / la vendedora", formal=True, slots=[
             "Buenos días, ¿qué fruta quiere?#Names a fruit, e.g. *Manzanas, por favor.*",
             "¿Cuántos kilos quiere?#Gives a quantity, e.g. *Dos kilos.*",
             "¿Para cuántas personas es la cena?#Gives a number of people, e.g. *Para cuatro personas.*",
             "¿Qué comió ayer?#Food in a past tense, e.g. *Comí pescado.*\n¿Ha probado ya algún plato típico de aquí? [PAUSA] ¿Qué tal?#Past (perfect/preterite) + opinion, e.g. *Sí, probé la sopa; estaba rica.*",
             "¿Qué va a cocinar esta noche?#Future time frame, e.g. *Voy a hacer una ensalada de fruta.*"]),
    dict(ctx="Estás de vacaciones en {city}. Vas a una tienda de alimentación para comprar comida para un picnic. Hablas con el dependiente / la dependienta.",
         role="el dependiente / la dependienta", formal=True, slots=[
             "Hola, ¿qué necesita hoy?#Names at least one food item, e.g. *Pan y queso.*",
             "¿Cuánto quiere?#Gives a quantity, e.g. *Medio kilo.*",
             "¿Quiere algo para beber? [PAUSA] ¿Qué?#Yes/no + a drink, e.g. *Sí, agua.*",
             "¿Ha probado ya algún plato típico de aquí? [PAUSA] ¿Qué tal?#Past (perfect/preterite) + opinion, e.g. *Sí, probé las empanadas; estaban ricas.*\n¿Adónde fue de picnic la última vez?#Past tense, e.g. *Fui al parque.*",
             "¿Adónde va a ir de picnic?#Future time frame, e.g. *Voy a ir al parque.*\n¿Qué plato le gustaría aprender a preparar?#Conditional, e.g. *Me gustaría aprender a hacer tortilla.*"]),
]
RP["A3"] = [
    dict(ctx="Estás de vacaciones en {city}. Te sientes mal y vas a la farmacia. Hablas con el farmacéutico / la farmacéutica.",
         role="el farmacéutico / la farmacéutica", formal=True, slots=[
             "Buenos días, ¿qué le pasa?#Symptom, e.g. *Me duele la cabeza.*",
             "¿Desde cuándo está así?#Time, e.g. *Desde ayer.*",
             "¿Tiene alergia a algún medicamento?#Yes/no (+ detail), e.g. *No, a ninguno.*",
             "¿Qué comió ayer?#Food in a past tense, e.g. *Comí marisco.*\n¿Qué hizo ayer? [PAUSA] ¿Y dónde?#Past activity + place, e.g. *Nadé en la piscina del hotel.*",
             "¿Qué va a hacer esta tarde?#Future, e.g. *Voy a descansar en el hotel.*"]),
    dict(ctx="Estás de intercambio en {city}. No te encuentras bien y vas al centro de salud. Hablas con el médico / la médica.",
         role="el médico / la médica", formal=True, slots=[
             "Hola, ¿qué le duele?#Part of the body, e.g. *Me duele el estómago.*",
             "¿Tiene fiebre?#Yes/no (+ detail), e.g. *Sí, un poco.*\n¿Desde cuándo está así?#Time, e.g. *Desde el lunes.*",
             "¿Cuántos años tiene?#Age, e.g. *Dieciséis.*",
             "¿Qué hizo ayer? [PAUSA] ¿Y dónde?#Past activity + place, e.g. *Jugué al fútbol en el parque.*",
             "Si mañana está mejor, ¿qué le gustaría hacer?#Conditional, e.g. *Me gustaría ir a la playa.*"]),
]
RP["A4"] = [
    dict(ctx="Estás en {city} de vacaciones. Quieres ir a otra ciudad en tren. Vas a la taquilla de la estación. Hablas con el empleado / la empleada.",
         role="el empleado / la empleada", formal=True, slots=[
             "Buenos días, ¿adónde quiere ir?#Destination, e.g. *A la capital.*",
             "¿Cuántos billetes necesita?#Number, e.g. *Dos, por favor.*",
             "¿Prefiere viajar por la mañana o por la tarde? [PAUSA] ¿Por qué?#Preference + reason, e.g. *Por la mañana, porque hay más tiempo.*",
             "¿Cómo vino a {city}?#Past, e.g. *Vine en avión.*",
             "¿Qué va a visitar allí?#Future, e.g. *Voy a visitar el museo.*"]),
    dict(ctx="Estás de intercambio en {city}. Quieres hacer una excursión en autobús. Hablas con el empleado / la empleada de la estación de autobuses.",
         role="el empleado / la empleada", formal=True, slots=[
             "Hola, ¿qué tipo de billete quiere?#Ticket type, e.g. *De ida y vuelta.*",
             "¿Para qué día es el billete?#A day, e.g. *Para el sábado.*",
             "¿Va a viajar con otras personas? [PAUSA] ¿Con quién?#Yes/no + who, e.g. *Sí, con mi hermano.*",
             "¿Qué hizo ayer en la ciudad?#Past, e.g. *Visité el castillo.*",
             "¿Qué le gustaría hacer en la excursión?#Conditional, e.g. *Me gustaría ver el lago.*"]),
]
# ---------------------------------------------------------------------------------- B
RP["B1"] = [
    dict(ctx="Llegas a {city} para hacer un intercambio. Conoces a la madre / al padre de tu familia de intercambio.",
         role="la madre / el padre", formal=False, slots=[
             "¡Bienvenido/Bienvenida! ¿De dónde eres?#Town/country, e.g. *Soy de Londres.*",
             "¿Tienes hermanos?#Yes/no + detail, e.g. *Sí, tengo una hermana.*",
             "¿Tienes mascotas? [PAUSA] ¿Cómo se llama(n)?#Pet + name, e.g. *Sí, un perro; se llama Max.*",
             "¿Cómo fue el viaje a {city}?#Past opinion, e.g. *Fue largo pero bien.*",
             "¿Qué te gustaría hacer con nosotros este fin de semana?#Conditional, e.g. *Me gustaría ver la ciudad.*"]),
    dict(ctx="Estás en {city}. Conoces a un chico / una chica en un club para jóvenes.",
         role="el chico / la chica", formal=False, slots=[
             "¡Hola! ¿Cómo te llamas?#Name, e.g. *Me llamo Sam.*",
             "¿Cuántas personas hay en tu familia?#Number + members, e.g. *Cuatro: mis padres, mi hermano y yo.*",
             "¿Cómo eres de carácter?#Personality adjectives, e.g. *Soy simpático y un poco tímido.*",
             "¿Qué hiciste el sábado pasado con tus amigos?#Past, e.g. *Fuimos al cine.*",
             "¿Qué vas a hacer mañana?#Future, e.g. *Voy a jugar al fútbol.*"]),
]
RP["B2"] = [
    dict(ctx="Estás de intercambio en {city}. Acabas de llegar a la casa de tu familia de intercambio. Hablas con la madre / el padre.",
         role="la madre / el padre", formal=False, slots=[
             "¡Bienvenido/Bienvenida! ¿Qué te parece la casa?#Opinion, e.g. *Es muy bonita.*",
             "¿A qué hora te levantas normalmente?#A time, e.g. *A las siete.*",
             "¿Qué te gusta desayunar?#Food/drink, e.g. *Cereales y zumo.*\n¿Cómo es tu casa en tu país? [PAUSA] ¿Y tu habitación?#Description of home + bedroom, e.g. *Es grande; mi habitación es pequeña.*",
             "¿Cómo ayudaste en casa la semana pasada?#Past chore, e.g. *Lavé los platos.*",
             "¿Qué te gustaría hacer en casa este fin de semana?#Conditional, e.g. *Me gustaría cocinar con vosotros.*\n¿Qué vas a hacer esta tarde?#Future, e.g. *Voy a deshacer la maleta.*"]),
    dict(ctx="Estás en {city}. Quieres alquilar una habitación en un piso para el verano. Hablas con el dueño / la dueña.",
         role="el dueño / la dueña", formal=True, slots=[
             "Buenos días, ¿qué tipo de habitación busca?#Room type, e.g. *Una habitación grande con baño.*",
             "¿Cuánto tiempo va a quedarse?#Duration, e.g. *Dos meses.*",
             "¿Cómo es su casa en su país? [PAUSA] ¿Y su habitación?#Description of home + bedroom, e.g. *Es un piso; mi habitación es pequeña.*",
             "¿Dónde pasó el verano pasado?#Past, e.g. *Lo pasé en la playa con mi familia.*",
             "¿Qué va a hacer en {city} este verano?#Future, e.g. *Voy a estudiar español.*"]),
]
RP["B4"] = [
    dict(ctx="Estás de vacaciones en {city}. Quieres comprar una camiseta. Hablas con el dependiente / la dependienta de una tienda de ropa.",
         role="el dependiente / la dependienta", formal=True, slots=[
             "Buenos días, ¿qué talla usa?#Size, e.g. *La talla M.*",
             "¿De qué color la quiere?#Colour, e.g. *Negra.*",
             "¿Para quién es la camiseta? [PAUSA] ¿Por qué?#Recipient + reason, e.g. *Para mi hermano, es su cumpleaños.*\n¿Cuánto quiere gastar?#An amount of money, e.g. *Unos veinte.*",
             "¿Qué ropa compró la última vez?#Past, e.g. *Compré unos vaqueros.*",
             "¿Qué va a hacer esta tarde?#Future, e.g. *Voy a ir a la playa.*"]),
    dict(ctx="Estás en {city}. Has comprado unos pantalones y quieres cambiarlos. Hablas con el dependiente / la dependienta.",
         role="el dependiente / la dependienta", formal=True, slots=[
             "Hola, ¿qué problema tienen los pantalones?#Problem, e.g. *Son muy pequeños.*",
             "¿De qué color los quiere ahora?#Colour, e.g. *Negros.*",
             "¿Qué talla necesita?#Size, e.g. *La talla cuarenta.*",
             "¿Cuándo compró los pantalones?#Past, e.g. *Los compré ayer.*",
             "¿Qué va a llevar en la fiesta de esta noche?#Future, e.g. *Voy a llevar los pantalones nuevos.*"]),
]
RP["B5"] = [
    dict(ctx="Estás de vacaciones en {city}. Quieres apuntarte a una actividad en el polideportivo. Hablas con el recepcionista / la recepcionista.",
         role="el recepcionista / la recepcionista", formal=True, slots=[
             "Hola, ¿qué actividad le interesa?#Activity, e.g. *La natación.*",
             "¿Cuántas veces por semana quiere venir?#Frequency, e.g. *Dos veces.*",
             "¿Prefiere clases por la mañana o por la tarde? [PAUSA] ¿Por qué?#Preference + reason, e.g. *Por la tarde, porque me levanto tarde.*",
             "¿Qué deporte hizo el año pasado?#Past, e.g. *Jugué al baloncesto.*\n¿Ha practicado este deporte antes? [PAUSA] ¿Dónde?#Past/perfect + place, e.g. *Sí, en mi instituto.*",
             "¿Qué va a hacer después de la clase?#Future, e.g. *Voy a volver al hotel.*"]),
    dict(ctx="Estás de intercambio en {city}. Tu amigo/amiga te invita a ir al cine este fin de semana. Habláis por teléfono.",
         role="el amigo / la amiga", formal=False, slots=[
             "¡Hola! ¿Qué día prefieres ir al cine?#A day, e.g. *El sábado.*",
             "¿A qué hora quedamos?#A time, e.g. *A las seis.*",
             "¿Qué tipo de película te gusta? [PAUSA] ¿Por qué?#Film type + reason, e.g. *Las de acción, son emocionantes.*",
             "¿Qué hiciste el fin de semana pasado?#Past, e.g. *Fui a la playa.*",
             "¿Qué te gustaría hacer después de la película?#Conditional, e.g. *Me gustaría cenar una pizza.*"]),
]
# ---------------------------------------------------------------------------------- C
RP["C1"] = [
    dict(ctx="Estás en un campamento internacional en {city}. Hablas con el monitor / la monitora del campamento.",
         role="el monitor / la monitora", formal=False, slots=[
             "¡Hola! ¿De dónde eres?#Country/nationality, e.g. *Soy de Inglaterra.*",
             "¿En qué parte de tu país vives?#Compass point / location, e.g. *En el sur.*",
             "¿Cómo es el clima en tu región?#Weather/climate, e.g. *Llueve mucho.*",
             "¿Cuándo llegaste a {city}?#Past time, e.g. *Llegué ayer.*",
             "¿Qué vas a hacer en el campamento mañana?#Future, e.g. *Voy a hacer una excursión.*"]),
    dict(ctx="Estás en {city}. Quieres participar en un programa de radio para jóvenes de muchos países. Hablas con el locutor / la locutora.",
         role="el locutor / la locutora", formal=False, slots=[
             "Hola, ¿qué nacionalidad tienes?#Nationality, e.g. *Soy británico.*",
             "¿Qué idiomas hablas?#Language(s), e.g. *Inglés y un poco de español.*",
             "¿Qué es lo mejor de tu país? [PAUSA] ¿Por qué?#Feature + reason, e.g. *Los parques, son bonitos.*",
             "¿Qué otros países has visitado?#Past/perfect, e.g. *He visitado Francia.*",
             "¿Qué país te gustaría visitar en el futuro?#Conditional, e.g. *Me gustaría ir a México.*"]),
]
RP["C2"] = [
    dict(ctx="Estás en {city}. Quieres hacer de voluntario/voluntaria en un parque natural. Hablas con el guarda / la guarda del parque.",
         role="el guarda / la guarda", formal=False, slots=[
             "Hola, ¿por qué quieres ayudar en el parque?#Reason, e.g. *Me encanta la naturaleza.*",
             "¿Qué día puedes venir?#A day, e.g. *El sábado.*",
             "¿Qué haces en tu casa para proteger el medio ambiente?#Action, e.g. *Reciclo el plástico.*",
             "¿Qué hiciste el año pasado para ayudar a la naturaleza?#Past action, e.g. *Planté árboles.*",
             "¿Qué te gustaría hacer en el parque?#Conditional, e.g. *Me gustaría cuidar los animales.*"]),
    dict(ctx="Estás en {city}. Vas a la oficina de turismo para informarte sobre una excursión a la montaña. Hablas con el empleado / la empleada.",
         role="el empleado / la empleada", formal=True, slots=[
             "Buenos días, ¿qué tipo de excursión busca?#Type of trip, e.g. *Una excursión a pie.*",
             "¿Cuántas personas son?#A number, e.g. *Somos tres.*",
             "¿Qué tiempo prefiere para la excursión? [PAUSA] ¿Por qué?#Weather + reason, e.g. *Sol, porque quiero hacer fotos.*",
             "¿Qué excursión hizo la última vez?#Past, e.g. *Fui a un lago.*\n¿Ha hecho alguna excursión a la montaña antes? [PAUSA] ¿Dónde?#Perfect/past + place, e.g. *Sí, en los Alpes.*",
             "¿Qué va a llevar en la mochila?#Future, e.g. *Voy a llevar agua y comida.*"]),
]
RP["C3"] = [
    dict(ctx="Estás de vacaciones en {city}. Tu móvil no funciona y vas a una tienda de móviles. Hablas con el dependiente / la dependienta.",
         role="el dependiente / la dependienta", formal=True, slots=[
             "Hola, ¿qué problema tiene su móvil?#States problem, e.g. *No se enciende.*",
             "¿Cuándo empezó el problema?#Time, e.g. *Esta mañana.*",
             "¿Para qué usa más el móvil? [PAUSA] ¿Por qué?#Use + reason, e.g. *Para hablar con mi familia, estoy lejos.*",
             "¿Qué hizo con el móvil antes del problema?#Past, e.g. *Hice fotos en la playa.*",
             "¿Qué va a hacer si no podemos arreglarlo hoy?#Future, e.g. *Voy a comprar otro.*"]),
    dict(ctx="Estás de intercambio en {city}. Quieres usar el ordenador de la biblioteca. Hablas con el bibliotecario / la bibliotecaria.",
         role="el bibliotecario / la bibliotecaria", formal=True, slots=[
             "Buenos días, ¿para qué quiere usar el ordenador?#Purpose, e.g. *Para mandar un correo.*",
             "¿Cuánto tiempo lo necesita?#Duration, e.g. *Media hora.*",
             "¿Prefiere usar el ordenador o el móvil? [PAUSA] ¿Por qué?#Preference + reason, e.g. *El ordenador, la pantalla es grande.*",
             "¿Qué hizo ayer en internet?#Past, e.g. *Vi una película.*",
             "¿Qué va a hacer después?#Future, e.g. *Voy a volver a casa.*"]),
]
RP["C4"] = [
    dict(ctx="Estás de vacaciones en {city}. Vas a la oficina de turismo para pedir información sobre la ciudad. Hablas con el empleado / la empleada.",
         role="el empleado / la empleada", formal=True, slots=[
             "Buenos días, ¿en qué puedo ayudarle?#Request, e.g. *Quiero un plano de la ciudad.*",
             "¿Cuántos días va a estar en la ciudad?#Duration, e.g. *Tres días.*",
             "¿Qué le interesa visitar? [PAUSA] ¿Por qué?#Place + reason, e.g. *El museo, me gusta el arte.*",
             "¿Qué visitó ayer?#Past, e.g. *Visité la catedral.*",
             "¿Qué va a hacer esta noche?#Future, e.g. *Voy a cenar en un restaurante.*"]),
    dict(ctx="Estás en {city}. Estás perdido/perdida y preguntas a un señor / una señora por la calle.",
         role="el señor / la señora", formal=False, slots=[
             "Hola, ¿adónde quieres ir?#A place, e.g. *A la estación.*",
             "¿Vas a ir a pie o en autobús?#Means, e.g. *A pie.*",
             "¿Por qué quieres ir allí?#Reason, e.g. *Mi tren sale a las cinco.*",
             "¿Qué hiciste esta mañana?#Past, e.g. *Fui al mercado.*",
             "¿Qué vas a hacer allí?#Future, e.g. *Voy a comprar un billete.*"]),
]
# ---------------------------------------------------------------------------------- D
RP["D1"] = [
    dict(ctx="Estás de intercambio en {city}. Es tu primer día en el instituto. Hablas con el profesor / la profesora de español.",
         role="el profesor / la profesora", formal=False, slots=[
             "Hola, bienvenido/bienvenida. ¿Cuántos años tienes?#Age, e.g. *Tengo quince años.*",
             "¿Qué asignaturas estudias en tu país?#Subjects, e.g. *Matemáticas, inglés y ciencias.*",
             "¿Cuál es tu asignatura favorita? [PAUSA] ¿Por qué?#Subject + reason, e.g. *La historia, es interesante.*",
             "¿Qué hiciste ayer en clase?#Past, e.g. *Hice un examen.*",
             "¿Qué vas a estudiar en el futuro?#Future, e.g. *Voy a estudiar ciencias.*"]),
    dict(ctx="Estás en {city}. Quieres hacer un curso de verano en una escuela de idiomas. Hablas con el secretario / la secretaria.",
         role="el secretario / la secretaria", formal=True, slots=[
             "Buenos días, ¿qué curso quiere hacer?#Course, e.g. *Un curso de español.*",
             "¿Cuántas semanas quiere estudiar?#Duration, e.g. *Tres semanas.*",
             "¿Prefiere clases por la mañana o por la tarde? [PAUSA] ¿Por qué?#Preference + reason, e.g. *Por la mañana, por la tarde hace calor.*",
             "¿Dónde estudió español antes?#Past, e.g. *En mi instituto.*",
             "¿Qué le gustaría hacer después de las clases?#Conditional, e.g. *Me gustaría visitar la ciudad.*"]),
]
RP["D2"] = [
    dict(ctx="Estás en {city} y quieres trabajar en un restaurante este verano. Tienes una entrevista con el gerente / la gerente.",
         role="el gerente / la gerente", formal=True, slots=[
             "Buenos días. ¿Por qué quiere este trabajo?#Reason, e.g. *Me gusta trabajar con gente.*",
             "¿Qué idiomas habla?#Languages, e.g. *Inglés y español.*",
             "¿Cómo es usted de carácter?#Personality, e.g. *Soy trabajador y puntual.*",
             "¿Ha trabajado antes? [PAUSA] ¿Dónde?#Perfect/past + place, e.g. *Sí, en una cafetería.*",
             "¿Qué va a hacer con el dinero?#Future, e.g. *Voy a viajar.*"]),
    dict(ctx="Estás en {city}. Quieres un trabajo de verano en un hotel. Hablas con el director / la directora de personal.",
         role="el director / la directora", formal=True, slots=[
             "Hola, ¿qué trabajo le interesa en el hotel?#Job, e.g. *Trabajar en la recepción.*",
             "¿Cuándo puede empezar?#Time, e.g. *En julio.*",
             "¿Prefiere trabajar por la mañana o por la tarde? [PAUSA] ¿Por qué?#Preference + reason.",
             "¿Qué hizo el verano pasado?#Past, e.g. *Trabajé en una tienda.*",
             "¿Qué trabajo le gustaría hacer en el futuro?#Conditional, e.g. *Me gustaría ser profesor.*"]),
]
# ---------------------------------------------------------------------------------- E
RP["E1"] = [
    dict(ctx="Estás de vacaciones en {city}. Llegas a un hotel. Hablas con el recepcionista / la recepcionista.",
         role="el recepcionista / la recepcionista", formal=True, slots=[
             "Buenas tardes, ¿qué tipo de habitación quiere?#Room type, e.g. *Una habitación doble.*",
             "¿Cuántas noches va a quedarse?#Number of nights, e.g. *Tres noches.*",
             "¿Quiere desayuno? [PAUSA] ¿Qué le gusta desayunar?#Yes/no + food, e.g. *Sí; café y tostadas.*\n¿Prefiere una habitación que da a la calle o al patio? [PAUSA] ¿Por qué?#Preference + reason, e.g. *Al patio, es más tranquila.*",
             "¿Cómo fue el viaje?#Past opinion, e.g. *Fue largo pero bien.*",
             "¿Qué va a visitar en la ciudad?#Future, e.g. *Voy a ver el museo.*"]),
    dict(ctx="Estás en {city}. Quieres apuntarte a un curso de español. Hablas con el profesor / la profesora de la escuela de idiomas.",
         role="el profesor / la profesora", formal=False, slots=[
             "Hola, ¿por qué quieres estudiar español?#Reason, e.g. *Para viajar.*",
             "¿Cuánto tiempo hace que estudias español?#Duration, e.g. *Dos años.*",
             "¿Qué es lo más difícil del español? [PAUSA] ¿Por qué?#Aspect + reason, e.g. *Los verbos, hay muchos.*",
             "¿Has visitado otros países hispanohablantes?#Perfect/past, e.g. *Sí, fui a México.*",
             "¿Qué te gustaría hacer con el español en el futuro?#Conditional, e.g. *Me gustaría trabajar en Perú.*"]),
]
RP["E2"] = [
    dict(ctx="Estás en {city} durante las fiestas. Hablas con un amigo / una amiga de aquí sobre las fiestas.",
         role="el amigo / la amiga", formal=False, slots=[
             "¡Hola! ¿Te gustan las fiestas de aquí?#Opinion, e.g. *Sí, son muy divertidas.*",
             "¿Qué fiesta es la más importante en tu país?#Names a festival, e.g. *La Navidad.*",
             "¿Cómo se celebra? [PAUSA] ¿Te gusta?#Description + opinion, e.g. *Con una cena en familia; me encanta.*",
             "¿Qué hiciste ayer en las fiestas?#Past, e.g. *Vi los fuegos artificiales.*",
             "¿Qué vas a hacer esta noche?#Future, e.g. *Voy a bailar en la plaza.*"]),
    dict(ctx="Estás en {city}. Quieres comprar un regalo de cumpleaños para un amigo / una amiga. Hablas con el dependiente / la dependienta.",
         role="el dependiente / la dependienta", formal=True, slots=[
             "Buenos días, ¿qué tipo de regalo busca?#Type of gift, e.g. *Un libro.*",
             "¿Cuántos años cumple su amigo o amiga?#Age, e.g. *Diecisiete.*",
             "¿Qué le gusta hacer? [PAUSA] ¿Qué regalo le va a comprar?#Hobby + gift, e.g. *Le gusta la música; unos auriculares.*",
             "¿Qué le regaló el año pasado?#Past, e.g. *Le regalé una camiseta.*",
             "¿Cómo van a celebrar su cumpleaños?#Future, e.g. *Vamos a cenar juntos.*"]),
]

# ======================================================================== forms
FORMS["A1"] = [
    dict(title="Inscripción en el club de verano", ctx="Quieres apuntarte a un club de verano para jóvenes.", gaps="""
Día de la semana que prefieres:#Any day of the week, e.g. sábado.#Anything that is not a day.#1
Hora a la que puedes llegar:#Any clock time, in words or figures, e.g. a las diez.#Anything that is not a time.#1
Mes de tu cumpleaños:#Any month, e.g. mayo.#Anything that is not a month.#1
Estación del año favorita:#Any season, e.g. verano.#Months or weather on their own.#1
Actividades que te gusta hacer por la mañana:#Any two activities, e.g. nadar, correr.#Non-activities; the same activity twice.#2
Comida que no te gusta:#Any food, e.g. pescado.#Drinks; non-food items.#1
"""),
    dict(title="Ficha para el campamento de vacaciones", ctx="Quieres participar en un campamento durante las vacaciones.", gaps="""
Mes en que quieres ir al campamento:#Any month, e.g. julio.#Anything that is not a month.#1
Hora a la que te levantas:#Any clock time, e.g. a las ocho.#Anything that is not a time.#1
Mes de tu cumpleaños:#Any month, e.g. mayo.#Anything that is not a month.#1
Estación del año favorita:#Any season, e.g. verano.#Months or weather on their own.#1
Actividades que te gusta hacer por la mañana:#Any two activities, e.g. nadar, correr.#Non-activities; the same activity twice.#2
Comida que no te gusta:#Any food, e.g. pescado.#Drinks; non-food items.#1
"""),
]
FORMS["A2"] = [
    dict(title="Encuesta: los hábitos alimentarios de los jóvenes", ctx="Participas en una encuesta sobre la comida.", gaps="""
Fruta favorita:#Any fruit, e.g. naranja.#Vegetables; other foods.#1
Bebida que tomas en el desayuno:#Any drink, e.g. leche, zumo.#Foods; non-drinks.#1
Comida que no te gusta:#Any food or dish, e.g. pescado.#Drinks.#1
Platos que sabes cocinar:#Any two dishes or foods, e.g. tortilla, pasta.#Non-food items; the same dish twice.#2
Lugar donde comes a mediodía:#Any appropriate place, e.g. en casa, en el comedor.#Times; foods.#1
Ingrediente que compras en el mercado:#Any food item, e.g. tomates.#Non-food items.#1
"""),
    dict(title="Ficha del curso de cocina", ctx="Quieres apuntarte a un curso de cocina para jóvenes.", gaps="""
Plato que quieres aprender a cocinar:#Any dish, e.g. paella.#Non-food items.#1
Comida que no te gusta:#Any food or dish, e.g. pescado.#Drinks.#1
Platos que sabes cocinar:#Any two dishes or foods, e.g. tortilla, pasta.#Non-food items; the same dish twice.#2
Alergia o comida que no puedes comer:#Any food, e.g. nueces; or ninguna.#Non-food items.#1
Ingrediente favorito:#Any food item, e.g. tomates.#Non-food items.#1
Día preferido para el curso:#Any day of the week, e.g. sábado.#Anything that is not a day.#1
"""),
]
FORMS["A3"] = [
    dict(title="Ficha médica para el campamento", ctx="Vas a un campamento de verano y tienes que rellenar una ficha de salud.", gaps="""
Deporte que practicas:#Any sport or physical activity, e.g. tenis.#Non-sports.#1
Alergia o comida que no puedes comer:#Any allergen or food, e.g. nueces; or ninguna.#Parts of the body.#1
Horas que duermes:#Any number of hours, e.g. ocho.#Times of day.#1
Parte del cuerpo que te duele a veces:#Any part of the body, e.g. espalda.#Illnesses.#1
Actividades para relajarte:#Any two activities, e.g. leer, nadar.#Non-activities; the same activity twice.#2
Medicamento que tomas:#Any medicine, e.g. pastillas para la alergia; or ninguno.#Foods.#1
"""),
    dict(title="Inscripción en el gimnasio", ctx="Quieres apuntarte a un gimnasio nuevo de tu barrio.", gaps="""
Deporte que practicas:#Any sport or physical activity, e.g. tenis.#Non-sports.#1
Horas de ejercicio a la semana:#Any number of hours, e.g. tres.#Times of day.#1
Parte del cuerpo que quieres fortalecer:#Any part of the body, e.g. las piernas.#Illnesses.#1
Actividades para estar en forma:#Any two activities, e.g. correr, nadar.#Non-activities; the same activity twice.#2
Bebida que tomas después de hacer deporte:#Any drink, e.g. agua.#Foods.#1
Hora a la que prefieres venir:#Any time, e.g. a las seis.#Days.#1
"""),
]
FORMS["A4"] = [
    dict(title="Objetos perdidos: estación de tren", ctx="Has perdido tu mochila en el tren y vas a la oficina de objetos perdidos.", gaps="""
Color de tu mochila:#Any colour, e.g. azul.#Non-colours.#1
Cosas que había dentro de la mochila:#Any two objects, e.g. libros, llaves.#Non-objects; the same thing twice.#2
Hora del viaje:#Any time, e.g. las ocho.#Days.#1
Día del viaje:#Any day, e.g. el lunes, ayer.#Times alone.#1
Destino del viaje:#Any town or place, e.g. la capital.#Means of transport.#1
Sitio del tren donde dejaste la mochila:#Any place, e.g. debajo del asiento.#Objects.#1
"""),
    dict(title="Encuesta sobre el transporte", ctx="Participas en una encuesta sobre el transporte de tu ciudad.", gaps="""
Medio de transporte que usas cada día:#Any means of transport, e.g. autobús.#Places.#1
Tiempo que tardas en llegar al instituto:#Any length of time, e.g. veinte minutos.#Clock times.#1
Hora a la que sales de casa:#Any time, e.g. a las ocho.#Days.#1
Cosas que haces durante el viaje:#Any two activities, e.g. leer, escuchar música.#Non-activities; the same activity twice.#2
Transporte que prefieres para viajes largos:#Any means of transport, e.g. tren.#Places.#1
Lo que no te gusta del transporte:#Any appropriate word or short phrase, e.g. caro, lento.#Means of transport on their own.#1
"""),
]
FORMS["B1"] = [
    dict(title="Ficha de intercambio escolar", ctx="Vas a participar en un intercambio con un instituto de otro país.", gaps="""
Número de hermanos:#Any number, e.g. dos, ninguno.#Names of people.#1
Descripción física:#Any appropriate adjective or phrase, e.g. alto, pelo corto.#Personality only.#1
Carácter:#Any personality adjective, e.g. simpático.#Physical description.#1
Mascota:#Any animal, e.g. un gato; or ninguna.#Non-animals.#1
Dos personas de tu familia:#Any two family members, e.g. madre, abuelo.#Names alone; the same person twice.#2
Lo que te gusta hacer con tus amigos:#Any activity, e.g. ir al cine.#Places alone.#1
"""),
    dict(title="Inscripción en el club de jóvenes", ctx="Quieres hacerte socio/socia de un club para jóvenes.", gaps="""
Carácter:#Any personality adjective, e.g. simpático.#Physical description.#1
Lo que te gusta hacer con tus amigos:#Any activity, e.g. ir al cine.#Places alone.#1
Número de hermanos:#Any number, e.g. dos, ninguno.#Names of people.#1
Mascota:#Any animal, e.g. un gato; or ninguna.#Non-animals.#1
Dos actividades que te gustaría hacer en el club:#Any two activities, e.g. bailar, jugar al ajedrez.#The same activity twice.#2
Día que puedes venir al club:#Any day, e.g. viernes.#Times alone.#1
"""),
]
FORMS["B2"] = [
    dict(title="Ficha para la familia de acogida", ctx="Vas a vivir con una familia en otro país y tienes que describir tu casa.", gaps="""
Tipo de casa:#Any type of home, e.g. piso, casa.#Rooms alone.#1
Habitación favorita:#Any room, e.g. el salón.#Furniture.#1
Mueble de tu dormitorio:#Any piece of furniture, e.g. cama.#Rooms.#1
Tarea que haces en casa:#Any household chore, e.g. lavar los platos.#Leisure activities.#1
Dos aparatos que hay en tu cocina:#Any two kitchen appliances or items, e.g. nevera, horno.#Furniture from other rooms only; the same item twice.#2
Hora a la que te levantas:#Any time, e.g. a las siete.#Days.#1
"""),
    dict(title="Encuesta: la vida en casa", ctx="Participas en una encuesta sobre la vida en casa de los jóvenes.", gaps="""
Tipo de casa:#Any type of home, e.g. piso, casa.#Rooms alone.#1
Habitación favorita:#Any room, e.g. el salón.#Furniture.#1
Tarea que haces en casa:#Any household chore, e.g. lavar los platos.#Leisure activities.#1
Tarea que no te gusta hacer:#Any household chore, e.g. planchar.#Leisure activities.#1
Dos cosas que haces en casa los fines de semana:#Any two activities, e.g. ver películas, cocinar.#The same activity twice.#2
Hora a la que te levantas:#Any time, e.g. a las siete.#Days.#1
"""),
]
FORMS["B3"] = [
    dict(title="Concurso de diseño: tu habitación ideal", ctx="Participas en un concurso para diseñar una habitación.", gaps="""
Color favorito:#Any colour, e.g. azul.#Non-colours.#1
Color que no te gusta:#Any colour, e.g. marrón.#Non-colours.#1
Color de las paredes de tu habitación:#Any colour, e.g. blanco.#Furniture.#1
Color de la cama de tu habitación ideal:#Any colour, e.g. gris.#Furniture alone.#1
Color de la alfombra:#Any colour, e.g. rojo.#Non-colours.#1
Dos colores para tu habitación ideal:#Any two colours, e.g. verde, amarillo.#The same colour twice; non-colours.#2
"""),
    dict(title="Encuesta: los colores y tú", ctx="Una revista hace una encuesta sobre los colores favoritos de los jóvenes.", gaps="""
Color favorito:#Any colour, e.g. azul.#Non-colours.#1
Color que no te gusta:#Any colour, e.g. marrón.#Non-colours.#1
Color de tus ojos:#Any plausible eye colour, e.g. marrones, azules, verdes.#Non-colours.#1
Color de tu ropa favorita:#Any colour, e.g. negro.#Items of clothing alone.#1
Color de las paredes de tu habitación:#Any colour, e.g. blanco.#Furniture.#1
Dos colores que te ponen de buen humor:#Any two colours, e.g. verde, amarillo.#The same colour twice; non-colours.#2
"""),
]
FORMS["B4"] = [
    dict(title="Concurso: diseña el uniforme del instituto", ctx="Tu instituto organiza un concurso para elegir un nuevo uniforme.", gaps="""
Prenda para el invierno:#Any item of winter clothing, e.g. abrigo.#Colours alone.#1
Color preferido para el uniforme:#Any colour, e.g. azul.#Clothes.#1
Ropa para la clase de educación física:#Any sports clothing, e.g. chándal, zapatillas.#Sports.#1
Calzado para el uniforme:#Any footwear, e.g. zapatos negros.#Colours alone.#1
Dos prendas para el uniforme:#Any two items of clothing, e.g. camisa, falda.#The same item twice.#2
Complemento permitido:#Any accessory, e.g. reloj, gorra.#Colours.#1
"""),
    dict(title="Encuesta: los jóvenes y la ropa", ctx="Una tienda de ropa hace una encuesta a los jóvenes.", gaps="""
Prenda que llevas en invierno:#Any item of winter clothing, e.g. abrigo.#Colours alone.#1
Color preferido para la ropa:#Any colour, e.g. negro.#Clothes.#1
Tienda donde compras ropa:#Any appropriate shop or place, e.g. en el centro comercial, por internet.#Clothes.#1
Ropa que llevas para hacer deporte:#Any sports clothing, e.g. chándal, zapatillas.#Sports.#1
Dos prendas que llevas los fines de semana:#Any two items of clothing, e.g. vaqueros, camiseta.#The same item twice.#2
Complemento favorito:#Any accessory, e.g. reloj, gorra.#Colours.#1
"""),
]
FORMS["B5"] = [
    dict(title="Inscripción en el polideportivo", ctx="Quieres hacerte socio/socia del polideportivo de tu barrio.", gaps="""
Deporte que practicas:#Any sport, e.g. baloncesto.#Places.#1
Otro deporte que te gustaría probar:#Any sport, e.g. natación.#Non-sports.#1
Horario preferido:#Any time of day or clock time, e.g. por la tarde.#Days alone.#1
Día libre de la semana:#Any day, e.g. domingo.#Times.#1
Dos actividades del polideportivo que te interesan:#Any two sports or activities, e.g. tenis, yoga.#The same activity twice.#2
Equipo o club en el que juegas:#Any team or club, or ninguno.#Sports alone are acceptable.#1
"""),
    dict(title="Ficha del club juvenil", ctx="Te apuntas a un club de actividades para jóvenes.", gaps="""
Deporte que practicas:#Any sport, e.g. baloncesto.#Places.#1
Instrumento que tocas:#Any instrument, e.g. guitarra; or ninguno.#Types of music.#1
Tipo de película favorita:#Any film type, e.g. de acción.#Titles alone are acceptable if they communicate; refuse non-films.#1
Día libre de la semana:#Any day, e.g. domingo.#Times.#1
Dos pasatiempos:#Any two hobbies, e.g. leer, pintar.#The same hobby twice.#2
Lugar donde quedas con tus amigos:#Any place, e.g. el parque.#People.#1
"""),
]
FORMS["C1"] = [
    dict(title="Inscripción: campamento internacional", ctx="Vas a un campamento con jóvenes de muchos países.", gaps="""
País donde vives:#Any country, e.g. Inglaterra.#Cities alone where a country is asked (accept if clearly a country).#1
Nacionalidad:#Any nationality, e.g. inglés.#Countries.#1
Región o zona de tu país:#Any region or compass point, e.g. el norte.#Countries.#1
Idioma que hablas en casa:#Any language, e.g. inglés.#Countries; nationalities.#1
Dos países que quieres visitar:#Any two countries, e.g. México, Japón.#The same country twice.#2
Continente favorito:#Any continent, e.g. Asia.#Countries.#1
"""),
    dict(title="Inscripción en el club de idiomas", ctx="Te apuntas a un club de idiomas en tu ciudad.", gaps="""
Nacionalidad:#Any nationality, e.g. inglés.#Countries.#1
Idioma que hablas en casa:#Any language, e.g. inglés.#Countries; nationalities.#1
Idioma que quieres practicar:#Any language, e.g. español.#Countries; nationalities.#1
País donde se habla ese idioma:#Any country, e.g. México.#Languages.#1
Dos países que quieres visitar:#Any two countries, e.g. México, Japón.#The same country twice.#2
Día que puedes venir al club:#Any day, e.g. martes.#Times alone.#1
"""),
]
FORMS["C2"] = [
    dict(title="Club de ecología: inscripción", ctx="Quieres hacerte socio/socia del club de ecología de tu barrio.", gaps="""
Tiempo que prefieres para las actividades:#Any weather, e.g. sol.#Seasons alone.#1
Animal favorito:#Any animal, e.g. delfín.#Plants.#1
Lugar natural favorito:#Any natural place, e.g. la playa.#Towns.#1
Lo que reciclas en casa:#Any recyclable item, e.g. papel.#Food.#1
Dos cosas que haces para ahorrar energía:#Any two actions, e.g. apagar la luz, ir en bici.#The same action twice.#2
Problema medioambiental de tu ciudad:#Any environmental problem, e.g. contaminación.#Weather alone.#1
"""),
    dict(title="Encuesta sobre el medio ambiente", ctx="Participas en una encuesta sobre el medio ambiente.", gaps="""
Tiempo que prefieres:#Any weather, e.g. sol.#Seasons alone.#1
Animal favorito:#Any animal, e.g. delfín.#Plants.#1
Lugar natural favorito:#Any natural place, e.g. la playa.#Towns.#1
Lo que reciclas en casa:#Any recyclable item, e.g. papel.#Food.#1
Dos cosas que haces para ahorrar energía:#Any two actions, e.g. apagar la luz, ir en bici.#The same action twice.#2
Problema medioambiental de tu ciudad:#Any environmental problem, e.g. contaminación.#Weather alone.#1
"""),
]
FORMS["C3"] = [
    dict(title="Encuesta: los jóvenes y la tecnología", ctx="Participas en una encuesta sobre la tecnología.", gaps="""
Aparato que usas más:#Any device, e.g. móvil.#Activities.#1
Horas al día delante de la pantalla:#Any number of hours, e.g. dos.#Times of day.#1
Red social o aplicación favorita:#Any app or social network; or a type of app, e.g. una aplicación de música.#Devices.#1
Lo que haces en internet:#Any online activity, e.g. ver vídeos.#Devices.#1
Dos ventajas de la tecnología:#Any two advantages, e.g. rápida, útil para estudiar.#The same point twice.#2
Lo que no te gusta de internet:#Any disadvantage, e.g. los anuncios.#Devices.#1
"""),
    dict(title="Inscripción en un curso de informática", ctx="Quieres hacer un curso de informática en verano.", gaps="""
Aparato que usas más:#Any device, e.g. portátil.#Activities.#1
Programa o aplicación que sabes usar:#Any app or program, e.g. un procesador de textos.#Devices.#1
Lo que quieres aprender en el curso:#Any computing skill, e.g. programar, hacer páginas web.#Devices.#1
Horas al día delante de la pantalla:#Any number of hours, e.g. dos.#Times of day.#1
Dos cosas que haces con el ordenador:#Any two activities, e.g. hacer los deberes, ver vídeos.#The same activity twice.#2
Mes en que puedes hacer el curso:#Any month, e.g. julio.#Days.#1
"""),
]
FORMS["C4"] = [
    dict(title="Encuesta del ayuntamiento sobre el barrio", ctx="El ayuntamiento quiere saber la opinión de los jóvenes sobre su barrio.", gaps="""
Lugar favorito de tu barrio:#Any place, e.g. el parque.#People.#1
Tienda que visitas a menudo:#Any shop, e.g. la panadería.#Products.#1
Transporte que usas en la ciudad:#Any transport, e.g. autobús.#Places.#1
Lo que no te gusta de tu barrio:#Any appropriate problem, e.g. el ruido.#Places alone.#1
Dos cosas que faltan en tu barrio:#Any two facilities, e.g. un cine, una piscina.#The same item twice.#2
Edificio importante de tu ciudad:#Any building, e.g. la catedral.#Shops already given are acceptable.#1
"""),
    dict(title="Concurso: mi ciudad ideal", ctx="Participas en un concurso de ideas para mejorar tu ciudad.", gaps="""
Lugar favorito de tu ciudad:#Any place, e.g. el parque.#People.#1
Transporte para tu ciudad ideal:#Any transport, e.g. tranvía.#Places.#1
Lo que no te gusta de tu ciudad:#Any appropriate problem, e.g. el tráfico.#Places alone.#1
Edificio nuevo que propones:#Any building or facility, e.g. un polideportivo.#People.#1
Dos cosas que faltan en tu ciudad:#Any two facilities, e.g. un cine, una piscina.#The same item twice.#2
Edificio importante de tu ciudad:#Any building, e.g. la catedral.#Shops already given are acceptable.#1
"""),
]
FORMS["D1"] = [
    dict(title="Inscripción en el intercambio escolar", ctx="Vas a participar en un intercambio con un instituto español.", gaps="""
Asignatura favorita:#Any school subject, e.g. historia.#Teachers' names.#1
Asignatura que no te gusta:#Any school subject, e.g. química.#Non-subjects.#1
Actividad extraescolar:#Any club or activity, e.g. el coro.#Subjects.#1
Material que necesitas en clase:#Any classroom item, e.g. calculadora.#Subjects.#1
Dos lugares de tu instituto:#Any two places in school, e.g. la biblioteca, el gimnasio.#The same place twice.#2
Lo que quieres estudiar en el futuro:#Any subject or course, e.g. medicina.#Jobs alone are acceptable if they communicate a course of study; refuse non-studies.#1
"""),
    dict(title="Ficha del curso de verano", ctx="Te apuntas a un curso de verano en una escuela.", gaps="""
Curso que quieres hacer:#Any subject or course, e.g. inglés, teatro.#Non-studies.#1
Asignatura favorita:#Any school subject, e.g. historia.#Teachers' names.#1
Asignatura que no te gusta:#Any school subject, e.g. química.#Non-subjects.#1
Material que necesitas en clase:#Any classroom item, e.g. calculadora.#Subjects.#1
Dos actividades que te gustaría hacer en el curso:#Any two activities, e.g. excursiones, deportes.#The same activity twice.#2
Lo que quieres estudiar en el futuro:#Any subject or course, e.g. medicina.#Jobs alone are acceptable if they communicate a course of study; refuse non-studies.#1
"""),
]
FORMS["D2"] = [
    dict(title="Solicitud de trabajo de verano", ctx="Quieres trabajar este verano en un hotel de la costa.", gaps="""
Trabajo que te interesa:#Any job, e.g. camarero.#Places alone.#1
Idioma que hablas:#Any language, e.g. inglés.#Countries.#1
Experiencia de trabajo:#Any job or work experience, e.g. en una tienda; or ninguna.#Hobbies.#1
Días que puedes trabajar:#Any day(s), e.g. sábado.#Times alone.#1
Dos cualidades personales:#Any two qualities, e.g. trabajador, puntual.#The same quality twice.#2
Trabajo que quieres hacer en el futuro:#Any job, e.g. médico.#Subjects alone.#1
"""),
    dict(title="Ficha de prácticas en empresas", ctx="Vas a hacer prácticas en una empresa de tu ciudad.", gaps="""
Tipo de empresa que te interesa:#Any type of company or workplace, e.g. una oficina, un hospital.#Jobs alone are acceptable.#1
Idioma que hablas:#Any language, e.g. inglés.#Countries.#1
Asignatura favorita:#Any school subject, e.g. informática.#Jobs.#1
Días que puedes ir:#Any day(s), e.g. lunes.#Times alone.#1
Dos cualidades personales:#Any two qualities, e.g. trabajador, puntual.#The same quality twice.#2
Trabajo que quieres hacer en el futuro:#Any job, e.g. médico.#Subjects alone.#1
"""),
]
FORMS["E1"] = [
    dict(title="Inscripción en la escuela de idiomas", ctx="Quieres hacer un curso de idiomas en el extranjero.", gaps="""
Idioma que quieres aprender:#Any language, e.g. español.#Countries.#1
Idiomas que hablas:#Any language(s), e.g. inglés.#Nationalities.#1
País que has visitado:#Any country, e.g. Francia.#Cities alone where a country is clear are acceptable.#1
Alojamiento preferido:#Any accommodation, e.g. con una familia, hotel.#Places in town.#1
Dos actividades que te gustaría hacer después de las clases:#Any two activities, e.g. visitar museos, nadar.#The same activity twice.#2
Número de semanas del curso:#Any number, e.g. tres.#Days of the week.#1
"""),
    dict(title="Inscripción para el viaje escolar", ctx="Tu instituto organiza un viaje a otro país.", gaps="""
País que quieres visitar:#Any country, e.g. México.#Cities alone where a country is clear are acceptable.#1
Idiomas que hablas:#Any language(s), e.g. inglés.#Nationalities.#1
País que has visitado:#Any country, e.g. Francia.#Cities alone where a country is clear are acceptable.#1
Alojamiento preferido:#Any accommodation, e.g. con una familia, hotel.#Places in town.#1
Dos cosas que vas a llevar en la maleta:#Any two items, e.g. pasaporte, ropa.#The same item twice.#2
Actividad que te gustaría hacer en el viaje:#Any activity, e.g. visitar museos.#Places alone.#1
"""),
]
FORMS["E2"] = [
    dict(title="Encuesta: las fiestas y tú", ctx="Una revista hace una encuesta sobre las fiestas.", gaps="""
Fiesta favorita:#Any festival or celebration, e.g. Navidad.#Months alone.#1
Mes de tu fiesta favorita:#Any month, e.g. diciembre.#Days.#1
Comida típica de una fiesta:#Any food, e.g. turrón.#Drinks alone are acceptable if typical; refuse non-food.#1
Regalo que te gustaría recibir:#Any gift, e.g. un libro.#Festivals.#1
Dos cosas que haces en tu cumpleaños:#Any two activities, e.g. comer tarta, bailar.#The same activity twice.#2
Fiesta de otro país que te gustaría ver:#Any festival, e.g. el Carnaval de Río.#Countries alone.#1
"""),
    dict(title="Inscripción en el concurso de las fiestas", ctx="Quieres participar en un concurso de disfraces durante las fiestas de tu ciudad.", gaps="""
Disfraz para el concurso:#Any costume, e.g. de pirata.#Colours alone.#1
Color principal del disfraz:#Any colour, e.g. rojo.#Non-colours.#1
Fiesta favorita:#Any festival or celebration, e.g. Carnaval.#Months alone.#1
Mes de tu fiesta favorita:#Any month, e.g. febrero.#Days.#1
Dos cosas que necesitas para el disfraz:#Any two items, e.g. un sombrero, una espada.#The same item twice.#2
Disfraz que llevaste el año pasado:#Any costume, e.g. de fantasma; or ninguno.#Colours alone.#1
"""),
]
