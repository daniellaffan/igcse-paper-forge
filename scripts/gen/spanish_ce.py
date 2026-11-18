"""Original content for Area E: The international world (E1-E2). Format: see spanish.py."""

C = {}

C["E1"] = dict(
    theme="los idiomas y los viajes al extranjero", tema="Los idiomas y los viajes al extranjero",
    scene=["Estás en el aeropuerto de {city} con {fr}. Vais a hacer un viaje al extranjero.",
           "Estás en una escuela de idiomas en {city} con {fr}."],
    ex="""
{fr} dice:#Este año estudio {v}.#¿Qué idioma estudia {fr} este año?#idioma
{fr} dice:#Mi abuelo habla muy bien {v}.#¿Qué idioma habla el abuelo de {fr}?#idioma
{fr} dice:#En agosto viajamos {v}.#¿Adónde viajan en agosto?#pais
{fr} dice:#Mi profesora de música es {v}.#¿De qué nacionalidad es la profesora de música?#nacionalidad
{fr} dice:#Para el viaje necesito {v}.#¿Qué necesita {fr} para el viaje?#equipaje
{fr} dice:#Vamos a dormir en {v}.#¿Dónde van a dormir?#alojamiento
{fr} dice:#El verano pasado fuimos {v}.#¿Adónde fueron el verano pasado?#pais
{fr} pregunta:#¿Has visto {v}? No lo encuentro.#¿Qué busca {fr}?#equipaje
{fr} dice:#Mi compañera de habitación es {v}.#¿De dónde es la compañera de habitación?#nacionalidad
""".replace("{fr} pregunta:#¿Has visto {v}? No lo encuentro.#¿Qué busca {fr}?#equipaje", "{fr} dice:#Se me ha olvidado {v} en el hotel.#¿Qué ha olvidado {fr}?#equipaje"),
    signs=("En el aeropuerto", """
Facturación#Aquí dejamos las maletas antes de volar.
Control de pasaportes#Hay que enseñar el documento de identidad.
Puerta de embarque 12#Nuestro avión sale por aquí.
Recogida de equipaje#Ahora vamos a buscar las maletas.
Cambio de moneda#Necesito dinero del país que voy a visitar.
Prohibido llevar líquidos de más de 100 ml#No puedo pasar con la botella grande de agua.
Vuelos retrasados#El avión no va a salir a su hora.
Tienda libre de impuestos#Aquí los perfumes son más baratos.
Alquiler de coches#Queremos un coche para recorrer la isla.
Información turística#Quiero un mapa de la ciudad y consejos.
"""),
    ann=dict(title="Información en el aeropuerto", desc="un anuncio en un aeropuerto", sp="Locutor",
             open="Señoras y señores, buenos días. Bienvenidos al aeropuerto de {city}.",
             close="Gracias por su atención y buen viaje.",
             facts="""
El vuelo a Roma saldrá con {r=media hora|una hora|dos horas|veinte minutos} de retraso.#El vuelo a Roma sale con un retraso de:#{r}
Los pasajeros del vuelo a Londres deben ir a la puerta catorce.#Los pasajeros a Londres deben ir a:#la puerta catorce;la puerta cuatro;la cafetería;la salida
Recuerden que no pueden dejar las maletas solas.#Los pasajeros no pueden:#dejar las maletas solas;comer en el aeropuerto;usar el móvil;comprar regalos
La oficina de cambio de moneda está en la planta baja.#La oficina de cambio está:#en la planta baja;en el primer piso;fuera del aeropuerto;al lado de la puerta catorce
Hay un servicio de autobús al centro de la ciudad cada veinte minutos.#El autobús al centro sale cada:#veinte minutos;hora;diez minutos;media hora
Los niños que viajan solos deben presentarse en el mostrador azul.#Los niños que viajan solos deben ir:#al mostrador azul;a la puerta catorce;a la cafetería;a la tienda
Hoy hace mucho calor; pueden encontrar agua gratis en las fuentes de la terminal.#En la terminal hay:#agua gratis;comida gratis;periódicos gratis;wifi de pago
"""),
    facts="""
Estudio inglés y francés en el instituto, pero mi idioma favorito es el español.#¿Qué idiomas estudias?#¿Cuál es el idioma favorito de {N}?#(El) español#Refuse inglés y francés#el español;el inglés;el francés;el alemán#Aprende varios idiomas en clase.#Solo estudia un idioma.#1
Me gusta aprender idiomas porque así puedo hablar con gente de otros países.#¿Por qué te gusta aprender idiomas?#¿Por qué le gusta a {N} aprender idiomas?#(Para) hablar con gente de otros países#Refuse me gusta#Para hablar con gente de otros países.;Para sacar buenas notas.;Porque sus padres lo quieren.;Para ver películas.#Los idiomas le ayudan a comunicarse con extranjeros.#No le interesan los idiomas.#1
Lo más difícil para mí es la pronunciación, sobre todo la letra erre.#¿Qué es lo más difícil de aprender español?#¿Qué le resulta difícil a {N}?#La pronunciación / la letra erre#Refuse el español tc#La pronunciación.;La gramática.;El vocabulario.;Escribir.#Le cuesta pronunciar algunos sonidos.#Pronunciar le parece facilísimo.#2
Para mejorar, veo series en versión original con subtítulos.#¿Qué haces para mejorar tu español?#¿Qué hace {N} para mejorar? #Ve series (en versión original) (con subtítulos)#Refuse para mejorar#Ve series con subtítulos.;Lee el periódico.;Va a clases particulares.;Escucha la radio.#Aprende con la televisión.#Nunca ve series en otro idioma.#2
El año pasado fui a Perú con mi clase y me alojé con una familia en Cusco.#¿Has viajado a un país hispanohablante?#¿Dónde se alojó {N} en Perú?#Con una familia (en Cusco)#Refuse con mi clase#con una familia;en un hotel;en un albergue;en un camping#Durante el viaje vivió con una familia.#Se alojó en un hotel.#2
Al principio no entendía nada porque hablaban muy rápido.#¿Fue fácil entender a la gente?#¿Por qué no entendía nada {N} al principio?#(Porque) hablaban muy rápido#Refuse no entendía nada#Porque hablaban muy rápido.;Porque hablaban otro idioma.;Porque estaba cansad<o|a>.;Porque había ruido.#Le costó entender al principio.#Lo entendía todo desde el primer día.#2
Lo que más me impresionó fue Machu Picchu, aunque tuvimos que levantarnos a las cuatro.#¿Qué te impresionó más?#¿A qué hora se levantaron para ir a Machu Picchu?#A las cuatro#Refuse Machu Picchu#a las cuatro;a las seis;a las ocho;a mediodía#Madrugaron mucho para la excursión.#Se levantaron tarde para ir a Machu Picchu.#2
Un día perdí el pasaporte, pero lo encontré en el bolsillo de mi chaqueta.#¿Tuviste algún problema durante el viaje?#¿Dónde encontró {N} el pasaporte?#En el bolsillo de su chaqueta#Refuse perdí el pasaporte#en el bolsillo de su chaqueta;en el hotel;en el autobús;en la maleta#El pasaporte no estaba perdido de verdad.#Tuvo que ir a la embajada por el pasaporte.#2
Viajar al extranjero es caro, pero creo que vale la pena porque aprendes mucho.#¿Merece la pena viajar al extranjero?#¿Por qué vale la pena viajar al extranjero para {N}?#(Porque) aprendes mucho#Refuse es caro#Porque se aprende mucho.;Porque es barato.;Porque hace calor.;Porque se compra mucho.#Para {N} viajar es una forma de aprender.#Cree que viajar no sirve para nada.#3
Mi madre es portuguesa, así que en casa a veces hablamos portugués.#¿De dónde es tu familia?#¿Por qué habla {N} portugués en casa a veces?#(Porque) su madre es portuguesa#Refuse a veces#Porque su madre es portuguesa.;Porque vive en Portugal.;Porque lo estudia.;Porque tiene amigos portugueses.#Tiene un familiar portugués.#Nadie de su familia habla portugués.#1
Creo que el inglés es útil, pero no es suficiente: hay que hablar más idiomas.#¿Es suficiente hablar inglés?#¿Qué opina {N} del inglés?#Es útil pero no es suficiente#Refuse es útil on its own tc#Es útil pero no suficiente.;Es inútil.;Es el único idioma necesario.;Es difícil.#Piensa que hay que saber más idiomas además del inglés.#Cree que con el inglés es suficiente.#3
El verano que viene voy a hacer un curso de alemán en Berlín.#¿Qué vas a hacer el verano que viene?#¿Dónde va a hacer {N} un curso de alemán?#(En) Berlín#Refuse el verano que viene#en Berlín;en Viena;en Múnich;en Zúrich#Va a estudiar alemán en Alemania.#Va a estudiar francés en París.#1
Cuando viajo, siempre intento probar la comida típica del país.#¿Qué te gusta hacer cuando viajas?#¿Qué intenta hacer {N} siempre cuando viaja?#Probar la comida típica (del país)#Refuse viajar tc#Probar la comida típica.;Comprar ropa.;Visitar museos.;Ir a la playa.#Le interesa la gastronomía de otros países.#Cuando viaja solo come comida de su país.#2
Me gustaría trabajar como traductor<|a> porque me encantan los idiomas.#¿Te gustaría usar los idiomas en tu trabajo?#¿Qué trabajo le gustaría hacer a {N}?#Traductor<|a>#Refuse los idiomas#traductor<|a>;profesor<|a>;guía turístic<o|a>;piloto#Quiere un trabajo relacionado con los idiomas.#No quiere usar idiomas en su trabajo.#2
Si pudiera vivir en otro país, elegiría Japón por su cultura.#¿En qué país te gustaría vivir?#¿Por qué elegiría {N} Japón?#Por su cultura#Refuse otro país#Por su cultura.;Por su clima.;Por su comida.;Por su música.#Le atrae la cultura japonesa.#No le interesa Japón.#3
En el viaje de vuelta, el avión tuvo un retraso de seis horas.#¿Cómo fue el viaje de vuelta?#¿Qué problema hubo en el viaje de vuelta de {N}?#(El avión tuvo) un retraso (de seis horas)#Refuse seis horas on its own tc#Un retraso de seis horas.;Perdió la maleta.;Se puso enferm<o|a>.;Perdió el avión.#Su vuelo de vuelta salió muy tarde.#Su vuelo salió a su hora.#2
""",
    tq="""
p#¿Qué idiomas hablas?#¿Qué idiomas estudias en el instituto?#Languages with level/detail.
p#¿Qué haces para aprender español?#¿Cómo estudias los idiomas?#Learning methods.
p#¿Adónde vas normalmente de vacaciones?#¿Viajas al extranjero con tu familia?#Holiday destinations.
o#¿Es importante aprender idiomas? ¿Por qué (no)?#¿Te gusta aprender idiomas? ¿Por qué (no)?#Opinion + reason.
o#¿Prefieres viajar a tu país o al extranjero? ¿Por qué?#¿Qué es lo mejor de viajar al extranjero? ¿Por qué?#Preference + reason.
pa#Háblame de un viaje al extranjero que hiciste.#¿Qué país visitaste la última vez? ¿Qué tal?#Past narrative.
pa#¿Tuviste algún problema durante un viaje?#¿Qué hiciste en tus últimas vacaciones?#Past.
f#¿Qué país vas a visitar en el futuro?#¿Qué idioma vas a aprender en el futuro?#Future.
c#Si pudieras vivir en otro país, ¿cuál elegirías? ¿Por qué?#¿Te gustaría trabajar en el extranjero? ¿Por qué (no)?#Conditional + reason.
d#Describe un país hispanohablante que te gustaría conocer.#¿Qué sabes de la cultura de un país hispanohablante?#Description.
f#¿Cómo vas a usar los idiomas en tu vida?#¿Vas a seguir estudiando español? ¿Por qué (no)?#Future + reason.
""",
    rp=[dict(ctx=["Estás de vacaciones en {city}. Llegas a un hotel. Hablas con el recepcionista / la recepcionista.#El recepcionista / La recepcionista",
                  "Estás en {city}. Quieres apuntarte a un curso de español. Hablas con el profesor / la profesora de la escuela de idiomas.#El profesor / La profesora"],
             slots=["""
Buenas tardes, ¿qué tipo de habitación quiere?#Room type, e.g. *Una habitación doble.*
Hola, ¿por qué quieres estudiar español?#Reason, e.g. *Para viajar.*
""", """
¿Cuántas noches va a quedarse?#Number of nights, e.g. *Tres noches.*
¿Cuánto tiempo hace que estudias español?#Duration, e.g. *Dos años.*
""", """
¿Quiere desayuno? [PAUSA] ¿Qué le gusta desayunar?#Yes/no + food.
¿Qué es lo más difícil del español? [PAUSA] ¿Por qué?#Aspect + reason.
""", """
¿Cómo fue el viaje?#Past opinion, e.g. *Fue largo pero bien.*
¿Has visitado otros países hispanohablantes?#Perfect/past, e.g. *Sí, fui a México.*
""", """
¿Qué va a visitar en la ciudad?#Future, e.g. *Voy a ver el museo.*
¿Qué te gustaría hacer con el español en el futuro?#Conditional, e.g. *Me gustaría trabajar en España.*
"""])],
    form=dict(titles=["Inscripción en la escuela de idiomas", "Ficha de viaje"],
              ctx=["Quieres hacer un curso de idiomas en el extranjero.", "Tu instituto organiza un viaje a otro país."],
              gaps="""
Idioma que quieres aprender:#Any language, e.g. español.#Countries.#1
Idiomas que hablas:#Any language(s), e.g. inglés.#Nationalities.#1
País que has visitado:#Any country, e.g. Francia.#Cities alone where a country is clear are acceptable.#1
Alojamiento preferido:#Any accommodation, e.g. con una familia, hotel.#Places in town.#1
Dos cosas que vas a llevar en la maleta:#Any two items, e.g. pasaporte, ropa.#The same item twice.#2
Actividad que te gustaría hacer en el viaje:#Any activity, e.g. visitar museos.#Places alone.#1
"""),
    ads=("Viajes y cursos de idiomas", """
Quiero mejorar mi inglés este verano viviendo con una familia.#‘Idiomas en Familia’: cursos de inglés en Irlanda con alojamiento en casas de familias.#‘English Online’: clases de inglés por internet desde tu casa.
Somos una familia con dos niños pequeños y buscamos un hotel en la playa con actividades infantiles.#‘Hotel Delfín’: primera línea de playa, club infantil y piscina para niños.#‘Hotel Silencio’: hotel de montaña solo para adultos.
Me encanta la aventura y quiero viajar por la selva de Costa Rica.#‘Selva Viva’: rutas de aventura por los parques naturales de Costa Rica con guía.#‘Cruceros del Mar’: viajes en barco por el Mediterráneo.
Tengo poco dinero y quiero dormir en un sitio barato en el centro de Madrid.#‘Albergue Centro’: camas desde 15 euros la noche, a dos minutos de la Puerta del Sol.#‘Palacio Real Hotel’: suites de lujo con vistas.
Necesito traducir unos documentos del inglés al español para mi trabajo.#‘Traducciones Rápidas’: traductores profesionales; documentos en 48 horas.#‘Academia Hablemos’: clases de conversación en español.
Me gustaría hacer un voluntariado en el extranjero durante un mes.#‘Manos Unidas Jóvenes’: voluntariado en escuelas de Bolivia; estancias de cuatro semanas.#‘Trabajo en Cruceros’: empleos remunerados en barcos de turistas durante seis meses.
Quiero aprender a cocinar platos tradicionales en un viaje a México.#‘Sabores de Oaxaca’: viajes gastronómicos con clases de cocina tradicional mexicana.#‘Restaurante Azteca’: comida mexicana en el centro de la ciudad.
"""),
)

C["E2"] = dict(
    theme="las fiestas y las tradiciones", tema="Las fiestas y las tradiciones",
    scene=["Estás en {city} con {fr} durante las fiestas de la ciudad.",
           "Estás en casa de {fr} en {city}. Su familia está preparando una celebración."],
    ex="""
{fr} dice:#Mi fiesta favorita es {v}.#¿Cuál es la fiesta favorita de {fr}?#festividad
{fr} dice:#Este año celebramos {v} en casa de mis abuelos.#¿Qué celebran en casa de los abuelos?#festividad
{fr} dice:#Para la fiesta necesitamos {v}.#¿Qué necesitan para la fiesta?#fiesta_cosa
{fr} dice:#Mi abuela me ha regalado {v}.#¿Qué le ha regalado su abuela?#regalo
{fr} dice:#Para el cumpleaños de mi hermano compramos {v}.#¿Qué compraron para el cumpleaños?#fiesta_cosa
{fr} dice:#Voy a regalarle {v} a mi madre.#¿Qué le va a regalar {fr} a su madre?#regalo
{fr} dice:#Lo que más me gusta de las fiestas son {v}.#¿Qué le gusta más a {fr} de las fiestas?#fiesta_cosa
{fr} dice:#En mi colegio vamos a celebrar {v}.#¿Qué van a celebrar en el colegio?#festividad
{fr} dice:#¿Te gusta {v} que te he comprado?#¿Qué le ha comprado {fr}?#regalo
""".replace("Lo que más me gusta de las fiestas son {v}.", "Lo que más me gusta de la fiesta es preparar {v}.").replace("¿Te gusta {v} que te he comprado?#¿Qué le ha comprado {fr}?", "Te he comprado {v} para tu cumpleaños.#¿Qué te ha comprado {fr}?"),
    ann=dict(title="Las fiestas de la ciudad", desc="un anuncio en la radio sobre las fiestas de una ciudad", sp="Locutora",
             open="¡Buenos días! Ya llegan las fiestas mayores de {city}. Os contamos el programa.",
             close="¡Felices fiestas a todos!",
             facts="""
Las fiestas empiezan el viernes con un desfile por las calles del centro.#Las fiestas empiezan con:#un desfile;un concierto;una cena;un partido
El sábado hay una comida popular en la plaza para {n=dos mil|mil|tres mil|quinientas} personas.#¿Para cuántas personas es la comida popular?#{n} personas
Los niños pueden disfrazarse y participar en un concurso de disfraces.#Los niños pueden participar en un concurso de:#disfraces;baile;dibujo;canto
A medianoche habrá fuegos artificiales en el puerto.#Los fuegos artificiales serán:#en el puerto;en la plaza;en el parque;en el estadio
El domingo hay una misa en la catedral y después una procesión.#El domingo después de la misa hay:#una procesión;un mercado;una carrera;un concierto
Durante las fiestas no habrá clases en los colegios el lunes.#El lunes los colegios:#estarán cerrados;abrirán más tarde;tendrán una fiesta;harán exámenes
Las calles del centro estarán cerradas al tráfico todo el fin de semana.#Durante el fin de semana las calles del centro:#estarán cerradas al tráfico;tendrán más autobuses;estarán decoradas con flores;estarán vacías
"""),
    facts="""
En mi familia celebramos la Navidad con una gran cena el veinticuatro de diciembre.#¿Cómo celebráis la Navidad?#¿Cuándo es la gran cena de Navidad en la familia de {N}?#El veinticuatro de diciembre / en Nochebuena#Refuse el veinticinco#el veinticuatro de diciembre;el veinticinco de diciembre;el treinta y uno de diciembre;el seis de enero#Celebran con una cena la noche antes de Navidad.#No celebran la Navidad.#1
El seis de enero los niños reciben regalos de los Reyes Magos.#¿Cuándo recibís los regalos?#¿Quién trae los regalos a los niños el seis de enero?#Los Reyes Magos#Refuse el seis de enero#los Reyes Magos;Papá Noel;sus padres;sus abuelos#Los regalos llegan en enero.#No hay regalos en su familia.#1
Mi fiesta favorita es el Carnaval porque me encanta disfrazarme.#¿Cuál es tu fiesta favorita?#¿Por qué le gusta el Carnaval a {N}?#(Porque) le encanta disfrazarse#Refuse me encanta#Le encanta disfrazarse.;Hay mucha comida.;No hay colegio.;Recibe regalos.#Le gusta ponerse disfraces.#No le gusta disfrazarse.#1
El año pasado me disfracé de pirata y gané el premio al mejor disfraz.#¿De qué te disfrazaste el año pasado?#¿Qué ganó {N} el año pasado?#El premio al mejor disfraz#Refuse pirata#el premio al mejor disfraz;un viaje;un concurso de baile;una medalla de oro#Su disfraz fue el mejor.#El año pasado no se disfrazó.#2
Mi mejor amiga es musulmana y durante el Ramadán no come durante el día.#¿Tienes amigos de otras religiones?#¿Qué hace la amiga de {N} durante el Ramadán?#No come durante el día#Refuse es musulmana#No come durante el día.;Va de vacaciones.;Come mucho.;Hace regalos.#Su amiga ayuna en un mes especial.#Su amiga come mucho durante el día en Ramadán.#2
Al final del Ramadán me invitó a una cena con su familia y probé muchos platos nuevos.#¿Has participado en alguna celebración de otra cultura?#¿Qué hizo {N} en la cena con la familia de su amiga?#Probó muchos platos nuevos#Refuse me invitó#Probó platos nuevos.;Cocinó.;Bailó.;Cantó.#Conoció comida diferente.#No fue a la cena.#2
En mi pueblo la fiesta más importante es en agosto, en honor a la Virgen.#¿Cuál es la fiesta más importante de tu pueblo?#¿Cuándo es la fiesta más importante del pueblo de {N}?#En agosto#Refuse la Virgen#en agosto;en mayo;en diciembre;en enero#La gran fiesta del pueblo es en verano.#La fiesta del pueblo es en invierno.#1
Durante las fiestas hay música en la plaza hasta las cuatro de la mañana.#¿Qué se hace en las fiestas de tu pueblo?#¿Hasta qué hora hay música en la plaza?#Hasta las cuatro (de la mañana)#Refuse la plaza#hasta las cuatro;hasta medianoche;hasta las dos;hasta las seis#La música dura hasta muy tarde.#La música termina a las diez.#2
A mis abuelos no les gustan las fiestas modernas porque hay demasiado ruido.#¿Qué piensan tus abuelos de las fiestas?#¿Por qué no les gustan a los abuelos de {N} las fiestas modernas?#(Porque) hay demasiado ruido#Refuse las fiestas modernas#Porque hay demasiado ruido.;Porque son caras.;Porque hay poca comida.;Porque terminan pronto.#El ruido molesta a sus abuelos.#A sus abuelos les encantan las fiestas modernas.#2
Creo que es importante conservar las tradiciones porque forman parte de nuestra identidad.#¿Es importante conservar las tradiciones?#¿Por qué es importante conservar las tradiciones según {N}?#(Porque) forman parte de nuestra identidad#Refuse es importante tc#Forman parte de nuestra identidad.;Atraen turistas.;Son divertidas.;Dan dinero.#Relaciona las tradiciones con la identidad.#Piensa que las tradiciones no importan.#3
Sin embargo, algunas tradiciones con animales me parecen crueles y deberían prohibirse.#¿Hay alguna tradición que no te guste?#¿Qué piensa {N} de algunas tradiciones con animales?#Son crueles / deberían prohibirse#Refuse los animales tc#Son crueles.;Son divertidas.;Son necesarias.;Son baratas.#Critica algunas tradiciones con animales.#Le gustan todas las tradiciones con animales.#3
Para mi cumpleaños hice una fiesta en casa con veinte amigos.#¿Cómo celebraste tu último cumpleaños?#¿Dónde hizo {N} la fiesta de cumpleaños?#En (su) casa#Refuse veinte amigos#en casa;en un restaurante;en la playa;en el colegio#Celebró su cumpleaños en casa.#No celebró su cumpleaños.#1
El regalo que más me gustó fue un viaje a Londres con mi padre.#¿Cuál fue tu mejor regalo?#¿Con quién viajó {N} a Londres?#Con su padre#Refuse Londres#con su padre;con su madre;con su clase;con sus amigos#Recibió un viaje como regalo.#Su mejor regalo fue un móvil.#2
El mes que viene se casa mi tía y vamos a celebrar la boda en una casa de campo.#¿Vas a ir a alguna celebración pronto?#¿Dónde van a celebrar la boda de la tía de {N}?#En una casa de campo#Refuse el mes que viene#en una casa de campo;en un hotel;en la playa;en un restaurante#Pronto habrá una boda en su familia.#Su tía se casó el año pasado.#2
Me gustaría ver las fiestas de San Fermín en Pamplona, aunque los toros me dan miedo.#¿Qué fiesta te gustaría ver?#¿Qué le da miedo a {N}?#Los toros#Refuse San Fermín#los toros;la gente;el ruido;los fuegos artificiales#Quiere ir a una fiesta famosa aunque le asuste algo.#No tiene ningún interés en San Fermín.#3
En mi casa, en Año Nuevo comemos doce uvas, una por cada campanada.#¿Qué hacéis en Año Nuevo?#¿Qué come la familia de {N} en Año Nuevo?#(Doce) uvas#Refuse doce on its own#doce uvas;turrón;pescado;tarta#Siguen una tradición con fruta.#En Año Nuevo no comen nada especial.#1
""",
    tq="""
p#¿Cuál es tu fiesta favorita?#¿Qué fiestas celebras con tu familia?#Names a festival with detail.
p#¿Cómo celebras tu cumpleaños?#¿Qué haces normalmente en tu cumpleaños?#Present habits.
p#¿Qué fiestas son importantes en tu país?#¿Hay una fiesta típica en tu ciudad?#Festivals in own country/town.
o#¿Es importante conservar las tradiciones? ¿Por qué (no)?#¿Te gustan las fiestas tradicionales? ¿Por qué (no)?#Opinion + reason.
o#¿Prefieres las fiestas en familia o con amigos? ¿Por qué?#¿Qué fiesta te gusta menos? ¿Por qué?#Preference + reason.
pa#¿Cómo celebraste tu último cumpleaños?#Háblame de una fiesta reciente.#Past narrative.
pa#¿Qué hiciste el año pasado en Navidad o en otra fiesta?#¿Cómo celebrabas las fiestas cuando eras pequeño/pequeña?#Past/imperfect.
f#¿Cómo vas a celebrar tu próximo cumpleaños?#¿Qué vas a hacer en las próximas fiestas?#Future.
c#¿Qué fiesta de otro país te gustaría ver? ¿Por qué?#Si pudieras organizar una fiesta, ¿cómo sería?#Conditional + reason.
d#Describe una fiesta típica de tu país.#Explica cómo se celebra una fiesta religiosa o cultural.#Description.
f#¿Cómo serán las fiestas en el futuro?#¿Vas a mantener las tradiciones de tu familia? ¿Por qué (no)?#Future.
""",
    rp=[dict(ctx=["Estás en {city} durante las fiestas. Hablas con un amigo / una amiga español/española sobre las fiestas.#El amigo / La amiga",
                  "Estás en {city}. Quieres comprar un regalo de cumpleaños para un amigo. Hablas con el dependiente / la dependienta.#El dependiente / La dependienta"],
             slots=["""
¡Hola! ¿Te gustan las fiestas de aquí?#Opinion, e.g. *Sí, son muy divertidas.*
Buenos días, ¿para quién es el regalo?#Recipient, e.g. *Para un amigo.*
""", """
¿Qué fiesta es la más importante en tu país?#Names a festival, e.g. *La Navidad.*
¿Cuántos años cumple?#Age, e.g. *Diecisiete.*
""", """
¿Cómo se celebra? [PAUSA] ¿Te gusta?#Description + opinion.
¿Qué le gusta hacer? [PAUSA] ¿Qué regalo prefieres?#Hobby + gift.
""", """
¿Qué hiciste ayer en las fiestas?#Past, e.g. *Vi los fuegos artificiales.*
¿Qué le regalaste el año pasado?#Past, e.g. *Le regalé un libro.*
""", """
¿Qué vas a hacer esta noche?#Future, e.g. *Voy a bailar en la plaza.*
¿Cómo vais a celebrar su cumpleaños?#Future, e.g. *Vamos a cenar juntos.*
"""])],
    form=dict(titles=["Encuesta: las fiestas y tú", "Inscripción en el concurso de las fiestas"],
              ctx=["Una revista hace una encuesta sobre las fiestas.", "Quieres participar en un concurso durante las fiestas de tu ciudad."],
              gaps="""
Fiesta favorita:#Any festival or celebration, e.g. Navidad.#Months alone.#1
Mes de tu fiesta favorita:#Any month, e.g. diciembre.#Days.#1
Comida típica de una fiesta:#Any food, e.g. turrón.#Drinks alone are acceptable if typical; refuse non-food.#1
Regalo que te gustaría recibir:#Any gift, e.g. un libro.#Festivals.#1
Dos cosas que haces en tu cumpleaños:#Any two activities, e.g. comer tarta, bailar.#The same activity twice.#2
Disfraz para el concurso:#Any costume, e.g. de pirata.#Colours alone.#1
"""),
)
