"""Original content for Area C: The world around us (C1-C6). Format: see spanish.py."""

C = {}

C["C1"] = dict(
    theme="su país y su región", tema="Mi país y mi región",
    scene=["Estás en {city} con {fr}. Estáis mirando un mapa del mundo.",
           "Estás en un campamento internacional cerca de {city} con {fr}. Habláis de vuestros países."],
    ex="""
{fr} dice:#Este verano voy {v} con mis padres.#¿Adónde va {fr} este verano?#pais
{fr} dice:#Mi tío trabaja {v}.#¿Dónde trabaja el tío de {fr}?#continente
{fr} dice:#Mi pueblo está {v} del país.#¿Dónde está el pueblo de {fr}?#punto
{fr} dice:#Mi nueva compañera de clase es {v}.#¿De dónde es la compañera de {fr}?#nacionalidad
{fr} dice:#Mi idioma favorito es {v}.#¿Qué idioma prefiere {fr}?#idioma
{fr} dice:#El año pasado fuimos {v}.#¿Adónde fue {fr} el año pasado?#pais
{fr} dice:#Mis abuelos viven {v}.#¿Dónde viven los abuelos de {fr}?#punto
{fr} dice:#Mi vecina es {v} y me enseña a cocinar platos de su país.#¿De dónde es la vecina de {fr}?#nacionalidad
{fr} dice:#Me gustaría vivir {v}.#¿Dónde le gustaría vivir a {fr}?#continente
""",
    ann=dict(title="Un festival internacional", desc="un anuncio sobre un festival internacional en un parque", sp="Locutora",
             open="Bienvenidos al Festival de los Pueblos del Mundo, en el parque central de {city}.",
             close="Disfruten del festival y de la diversidad de nuestro planeta.",
             facts="""
Este año participan personas de más de {n=cuarenta|treinta|cincuenta|sesenta} países.#¿Cuántos países participan?#más de {n}
En la zona norte del parque hay puestos de comida de América del Sur.#En la zona norte hay comida de:#América del Sur;Asia;África;Europa
Los países asiáticos presentan sus bailes tradicionales en el escenario principal.#En el escenario principal hay bailes de:#Asia;Europa;Oceanía;África
Hay un mapa gigante donde los visitantes pueden marcar su país de origen.#En el mapa gigante los visitantes pueden:#marcar su país;ganar un premio;hacerse una foto;comprar billetes
Los niños pueden aprender a decir hola en veinte idiomas.#Los niños pueden aprender a decir:#hola en veinte idiomas;adiós en diez idiomas;gracias en cinco idiomas;los números
A las seis hay una charla sobre los volcanes de Centroamérica.#La charla de las seis es sobre:#los volcanes;los ríos;las playas;los animales
El festival termina el domingo con un desfile de trajes típicos.#El festival termina con:#un desfile;fuegos artificiales;un partido;un concierto de rock
Está prohibido traer bebidas de fuera del parque.#Está prohibido:#traer bebidas de fuera;hacer fotos;venir con perros;bailar
"""),
    facts="""
Vivo en {city}, en {reg} del país.#¿Dónde vives exactamente?#¿En qué parte del país vive {N}?#(En) {reg}#Refuse {city} on its own#*reg#Su ciudad está en {reg} de su país.#Vive fuera de su país.#1
Mi región es famosa por sus montañas y por el queso que se hace allí.#¿Por qué es famosa tu región?#¿Por qué es famosa la región de {N}? (Menciona una cosa.)#(Sus) montañas / (el) queso#Refuse famosa tc#Por sus montañas y su queso.;Por sus playas.;Por su vino.;Por sus fábricas.#Su región es conocida por un producto alimenticio.#Su región es completamente llana.#1#mount
Mi madre es de aquí, pero mi padre es inglés, así que tengo dos nacionalidades.#¿De dónde son tus padres?#¿Cuántas nacionalidades tiene {N}?#Dos#Refuse inglés#dos;una;tres;ninguna#Su padre viene de otro país.#Sus padres son de la misma ciudad.#1
En casa hablamos dos idiomas, español con mi madre e inglés con mi padre.#¿Qué idiomas habláis en casa?#¿Qué idioma habla {N} con su padre?#Inglés#Refuse español#inglés;español;francés;alemán#Es bilingüe.#Solo habla un idioma.#1
Lo que más me gusta de mi región es que la gente es muy abierta y acogedora.#¿Qué te gusta de la gente de tu región?#¿Cómo es la gente de la región de {N}?#(Muy) abierta y acogedora / simpática#Refuse la región tc#Abierta y acogedora.;Seria y tímida.;Antipática.;Muy trabajadora.#La gente de su región recibe bien a los visitantes.#La gente de su región es muy cerrada.#2
El problema es que muchos jóvenes de mi región se van a la capital para buscar trabajo.#¿Hay algún problema en tu región?#¿Por qué se van muchos jóvenes a la capital?#Para buscar trabajo#Refuse a la capital#Para buscar trabajo.;Para estudiar.;Para ir de vacaciones.;Porque hace frío.#Faltan empleos en su zona.#Llegan muchos jóvenes a su región para trabajar.#2#!capital
El verano pasado visité otra región de mi país y me sorprendió lo diferentes que son las casas.#¿Has visitado otras partes de tu país?#¿Qué le sorprendió a {N} en otra región de su país?#Las casas (son muy diferentes)#Refuse el verano pasado#Las casas.;La comida.;El clima.;El idioma.#Notó diferencias en la arquitectura.#No ha salido nunca de su región.#2
Mi capital favorita es Lisboa, porque es una ciudad tranquila y está al lado del mar.#¿Cuál es tu capital favorita?#¿Por qué le gusta Lisboa a {N}? (Menciona una cosa.)#(Es) tranquila / está al lado del mar#Refuse es una capital#Porque es tranquila y está junto al mar.;Porque es muy grande.;Porque tiene muchas tiendas.;Porque hace frío.#Le gusta una capital costera.#Su capital preferida está en el interior.#2
Nunca he estado en otro continente, pero me encantaría conocer Asia.#¿Has estado en otro continente?#¿Qué continente quiere conocer {N}?#Asia#Refuse otro continente tc#Asia;África;América;Oceanía#Todavía no ha viajado fuera de su continente.#Ha viajado por todo el mundo.#2#-livedabroad
Cuando era pequeñ<o|a> vivía en Ecuador, porque mis padres trabajaban allí como médicos.#¿Has vivido en otro país?#¿Por qué vivía {N} en Ecuador?#(Porque) sus padres trabajaban allí (como médicos)#Refuse mis padres#Porque sus padres trabajaban allí.;Porque estudiaba allí.;Porque sus abuelos vivían allí.;Por vacaciones.#Vivió en el extranjero de niñ<o|a>.#Siempre ha vivido en el mismo país.#2#!ecuador +livedabroad
Creo que vivir en otro país te ayuda a entender mejor a otras personas.#¿Es bueno vivir en otro país?#Según {N}, ¿qué ventaja tiene vivir en otro país?#Entiendes mejor a otras personas#Refuse vivir en otro país tc#Ayuda a entender a otras personas.;Se gana más dinero.;Hace mejor tiempo.;Es más barato.#Cree que vivir fuera abre la mente.#Piensa que vivir fuera es una pérdida de tiempo.#3
En mi clase hay alumnos de doce nacionalidades distintas y eso hace las clases más interesantes.#¿Hay alumnos de otros países en tu clase?#¿Qué piensa {N} de tener compañeros de tantas nacionalidades?#Hace las clases más interesantes#Refuse doce nacionalidades#Hace las clases más interesantes.;Es difícil.;Es aburrido.;No le importa.#Le gusta la diversidad de su clase.#Todos sus compañeros son del mismo país.#3
El clima de mi región es seco; casi nunca llueve en verano.#¿Cómo es el clima de tu región?#¿Cómo es el clima de la región de {N}?#Seco / casi nunca llueve#Refuse en verano#seco;húmedo;frío;lluvioso#En su región llueve poco.#En su región llueve todos los días.#1#dry
Dentro de unos años quiero viajar por América del Sur en tren y en autobús.#¿Qué viaje te gustaría hacer?#¿Cómo quiere viajar {N} por América del Sur?#En tren y en autobús#Refuse dentro de unos años#en tren y en autobús;en avión;en coche;en bicicleta#Quiere recorrer un continente por tierra.#Quiere viajar por Asia en barco.#2
Me gustaría vivir en el norte de Europa, aunque allí hace mucho frío.#¿Dónde te gustaría vivir en el futuro?#¿Qué inconveniente tiene el norte de Europa para {N}?#(Hace mucho) frío#Refuse el norte de Europa#El frío.;La comida.;El idioma.;Los precios.#Sabe que el clima del norte es duro.#Piensa que en el norte de Europa hace calor.#3
Mi ciudad está muy bien comunicada y desde aquí es fácil viajar a todas partes.#¿Cómo es la situación de tu ciudad?#¿Por qué es buena la situación de la ciudad de {N}?#Es fácil viajar a todas partes / está (muy) bien comunicada#Refuse es muy bonita#Es fácil viajar a todas partes.;Está cerca del mar.;Tiene aeropuerto.;Es muy bonita.#Desde su ciudad se viaja fácilmente.#Su ciudad está muy aislada.#3
""",
    tq="""
p#¿Dónde está tu ciudad o tu pueblo?#¿En qué parte de tu país vives?#Location using compass points, e.g. *Vivo en el norte.*
p#¿Cómo es tu región?#Describe tu región.#Geography, climate, features.
p#¿Qué idiomas hablas?#¿Qué idiomas se hablan en tu país?#Languages with detail.
o#¿Te gusta vivir en tu región? ¿Por qué (no)?#¿Qué es lo mejor de tu región? ¿Por qué?#Opinion + reason.
o#¿Es importante conocer otros países? ¿Por qué (no)?#¿Qué país te parece más interesante? ¿Por qué?#Opinion + justification.
pa#¿Qué otro país o región visitaste? ¿Qué tal fue?#Háblame de un sitio que visitaste en tu país.#Past narrative + opinion.
pa#¿Dónde vivías cuando eras pequeño/pequeña?#¿Siempre has vivido en el mismo sitio?#Imperfect/preterite.
f#¿Qué país vas a visitar en el futuro?#¿Adónde vas a viajar el año que viene?#Future plans.
c#¿En qué país te gustaría vivir? ¿Por qué?#Si pudieras vivir en otro continente, ¿cuál elegirías? ¿Por qué?#Conditional + reason.
d#Describe un país que te interesa.#¿Qué sabes de un país hispanohablante?#Description: location, people, culture.
f#¿Dónde vas a vivir cuando seas mayor?#¿Vas a vivir en tu región en el futuro?#Future.
""",
)

C["C2"] = dict(
    theme="el medio ambiente y la naturaleza", tema="El medio ambiente",
    scene=["Estás de excursión en el campo cerca de {city} con {fr}.",
           "Estás en {city} con {fr}. Estáis preparando un proyecto sobre la naturaleza."],
    ex="""
{fr} dice:#Hoy {v} en {city}.#¿Qué tiempo hace hoy?#tiempo
{fr} dice:#Según la radio, por la tarde {v}.#¿Qué tiempo hará por la tarde?#tiempo
{fr} dice:#Lo que más me gusta de esta región es {v}.#¿Qué le gusta a {fr} de la región?#paisaje
{fr} dice:#Este verano vamos a visitar {v}.#¿Qué van a visitar este verano?#paisaje
{fr} dice:#¡Mira! Allí hay {v}.#¿Qué animal ve {fr}?#animal
{fr} dice:#En mi casa reciclamos {v}.#¿Qué reciclan en casa de {fr}?#reciclaje
{fr} pregunta:#¿Dónde se tira{n} {v}?#¿Qué quiere tirar {fr}?#reciclaje
{fr} dice:#Mi animal favorito es {v}.#¿Cuál es el animal favorito de {fr}?#animal
{fr} dice:#Ayer fuimos a {v} y estaba muy sucio.#¿Qué lugar estaba sucio?#paisaje
""".replace("Ayer fuimos a {v} y estaba muy sucio.#¿Qué lugar estaba sucio?", "Ayer limpiamos {v} con el club de ecología.#¿Qué limpiaron ayer?"),
    signs=("En un parque natural", """
Prohibido hacer fuego#No se puede cocinar una barbacoa aquí.#fire
No dar de comer a los animales#Los patos no pueden comer nuestro pan.
Lleve su basura a casa#Tenemos que guardar los papeles en la mochila.
Perros atados#Mi perro no puede correr libre.
Zona de acampada#Aquí podemos poner la tienda de campaña.
Agua potable#Aquí se puede llenar la botella para beber.
No salir del camino#Hay que seguir el sendero.
Prohibido coger flores#Las plantas tienen que quedarse donde están.
Peligro: riesgo de incendio#Hace mucho calor y el bosque puede quemarse fácilmente.#fire
Mirador: vista del lago#Desde aquí podemos ver el agua desde arriba.
"""),
    ann=dict(title="Una semana verde en la ciudad", desc="un anuncio en la radio sobre el medio ambiente", sp="Locutor",
             open="Buenos días. El ayuntamiento de {city} organiza la Semana Verde para cuidar nuestro planeta.",
             close="Entre todos podemos cambiar las cosas. ¡Participa!",
             facts="""
El lunes los autobuses de la ciudad serán gratis para reducir el uso del coche.#El lunes los autobuses serán:#gratis;más rápidos;eléctricos;más caros
El martes vamos a plantar {n=quinientos|doscientos|mil|trescientos} árboles en el parque del río.#¿Cuántos árboles van a plantar?#{n}
El miércoles se puede llevar ropa vieja al ayuntamiento para reciclarla.#El miércoles se puede llevar al ayuntamiento:#ropa vieja;papel;pilas;muebles
El jueves los colegios apagarán las luces durante una hora.#El jueves los colegios van a:#apagar las luces;cerrar;plantar flores;limpiar las playas
El viernes hay una limpieza de la playa; traed guantes y una bolsa.#Para la limpieza de la playa hay que traer:#guantes y una bolsa;una toalla;comida;un cubo
Habrá un concurso de fotografía sobre la naturaleza para jóvenes.#El concurso es de:#fotografía;dibujo;poesía;cocina
^El premio es una excursión de un día para ver ballenas.#El premio es una excursión para ver:#ballenas;volcanes;osos;tortugas
"""),
    facts="""
En mi casa reciclamos todo: el papel, el plástico y el vidrio van a contenedores diferentes.#¿Recicláis en casa?#¿Qué hace la familia de {N} con el papel, el plástico y el vidrio?#Los separan / los reciclan (en contenedores diferentes)#Refuse reciclamos tc in first person#Los separan para reciclar.;Los tiran juntos.;Los venden.;Los queman.#Su familia separa la basura.#Su familia no recicla nada.#1
Voy al instituto en bicicleta para no contaminar.#¿Qué haces tú para proteger el medio ambiente?#¿Por qué va {N} al instituto en bicicleta?#Para no contaminar#Refuse en bicicleta#Para no contaminar.;Porque es rápido.;Porque no hay autobús.;Para hacer deporte.#Elige un transporte limpio.#Va al instituto en coche.#1
Me ducho en cinco minutos para ahorrar agua.#¿Ahorras agua en casa?#¿Cuánto tiempo tarda {N} en ducharse?#Cinco minutos#Refuse para ahorrar agua#cinco minutos;diez minutos;media hora;un minuto#Se ducha rápido.#Se baña durante una hora.#1
En mi ciudad el aire está muy contaminado por el tráfico.#¿Qué problemas medioambientales hay en tu ciudad?#¿Por qué está contaminado el aire de la ciudad de {N}?#Por el tráfico / los coches#Refuse la ciudad tc#Por el tráfico.;Por las fábricas.;Por los incendios.;Por los aviones.#El tráfico ensucia el aire de su ciudad.#El aire de su ciudad es muy limpio.#2
El año pasado hubo un incendio enorme en el bosque cerca de mi ciudad y murieron muchos animales.#¿Ha pasado algo grave en tu región?#¿Qué pasó el año pasado cerca de la ciudad de {N}?#(Hubo) un incendio (en el bosque)#Refuse murieron animales tc#Hubo un incendio.;Hubo una inundación.;Nevó mucho.;Hubo un terremoto.#Un fuego destruyó parte del bosque.#El bosque cerca de su ciudad está intacto.#2
Ahora soy voluntari<o|a> en un grupo que limpia el río los domingos.#¿Participas en algún grupo ecologista?#¿Qué hace {N} los domingos?#Limpia el río (con un grupo)#Refuse soy voluntario#Limpia el río.;Planta árboles.;Recicla ropa.;Cuida animales.#Ayuda a limpiar la naturaleza como voluntari<o|a>.#Los domingos se queda en casa.#2
Me preocupa el cambio climático porque los veranos son cada vez más calurosos.#¿Qué piensas del cambio climático?#¿Por qué le preocupa el cambio climático a {N}?#(Porque) los veranos son (cada vez) más calurosos#Refuse me preocupa#Porque los veranos son más calurosos.;Porque llueve más.;Porque nieva mucho.;Porque hay más tráfico.#Ha notado que el calor aumenta.#Dice que los veranos son ahora más frescos.#3#temperate
Creo que los gobiernos deberían hacer más, pero cada persona también puede ayudar.#¿Quién debe proteger el medio ambiente?#Según {N}, ¿quién puede ayudar además de los gobiernos?#Cada persona / todos#Refuse los gobiernos#Cada persona.;Solo los científicos.;Las empresas.;Nadie.#Piensa que todos tenemos responsabilidad.#Cree que solo el gobierno puede ayudar.#3
Mi animal favorito es el oso, pero en mi país está en peligro de extinción.#¿Cuál es tu animal favorito?#¿Qué problema tiene el oso en el país de {N}?#Está en peligro de extinción#Refuse es su favorito#Está en peligro de extinción.;Es peligroso.;Come mucho.;Vive en el zoo.#Quedan pocos osos en su país.#Hay muchísimos osos en su país.#2#oso
En mi instituto han puesto paneles solares en el tejado.#¿Qué hace tu instituto por el medio ambiente?#¿Qué ha puesto el instituto de {N} en el tejado?#Paneles solares#Refuse el tejado#paneles solares;un jardín;una piscina;una antena#El instituto produce energía del sol.#El instituto no hace nada por el medio ambiente.#2
Me encanta el campo; los fines de semana hago senderismo por las montañas.#¿Te gusta la naturaleza?#¿Qué hace {N} los fines de semana?#(Hace) senderismo (por las montañas)#Refuse el campo#Hace senderismo.;Va a la playa.;Va de compras.;Juega al fútbol.#Camina por la montaña.#Odia el campo.#1
Antes usaba muchas bolsas de plástico, pero ahora siempre llevo una bolsa de tela.#¿Has cambiado algún hábito?#¿Qué lleva siempre {N} ahora?#Una bolsa de tela#Refuse bolsas de plástico#una bolsa de tela;una botella de agua;una mochila;un paraguas#Ha dejado de usar bolsas de plástico.#Sigue usando muchas bolsas de plástico.#2
En mi región el clima es suave: en invierno no hace mucho frío y en verano no hace demasiado calor.#¿Cómo es el clima de tu región?#¿Cómo es el clima en la región de {N}?#Suave / ni mucho frío ni demasiado calor#Refuse en invierno tc#Suave.;Muy frío.;Muy caluroso.;Muy lluvioso.#Su región tiene un clima templado.#En su región el clima es extremo.#2#mild
El próximo verano voy a trabajar en un centro de recuperación de tortugas.#¿Qué vas a hacer el próximo verano?#¿Dónde va a trabajar {N} el próximo verano?#En un centro de (recuperación de) tortugas#Refuse el próximo verano#En un centro de tortugas.;En un zoo.;En una granja.;En un parque.#Va a ayudar a unos animales marinos.#Va a trabajar en una oficina.#2
Si fuera alcalde de mi ciudad, prohibiría los coches en el centro.#¿Qué harías para mejorar tu ciudad?#¿Qué haría {N} si fuera alcalde?#Prohibiría los coches en el centro#Refuse prohibir tc#Prohibiría los coches en el centro.;Construiría más parques.;Pondría más autobuses.;Cerraría las fábricas.#Quiere un centro sin coches.#Construiría más aparcamientos.#3
Cuando hay tormenta, mi perro se esconde debajo de la cama.#¿Te gustan las tormentas?#¿Qué hace el perro de {N} cuando hay tormenta?#Se esconde (debajo de la cama)#Refuse la cama tc#Se esconde debajo de la cama.;Ladra mucho.;Sale al jardín.;Duerme.#Su perro tiene miedo de las tormentas.#A su perro le encantan las tormentas.#2
""",
    tq="""
p#¿Cómo es el clima en tu región?#¿Qué tiempo hace normalmente en tu región?#Weather and seasons.
p#¿Qué haces tú para proteger el medio ambiente?#¿Reciclas en casa?#Personal actions, e.g. *Reciclo el papel.*
p#¿Qué problemas medioambientales hay en tu ciudad?#¿Hay mucha contaminación en tu ciudad?#Problems with detail.
o#¿Es importante reciclar? ¿Por qué (no)?#¿Te preocupa el medio ambiente? ¿Por qué (no)?#Opinion + reason.
o#¿Prefieres el campo o la ciudad? ¿Por qué?#¿Te gusta la naturaleza? ¿Por qué (no)?#Preference + reason.
pa#¿Qué hiciste la semana pasada para ayudar al medio ambiente?#Háblame de una excursión a la naturaleza que hiciste.#Past actions / narrative.
pa#¿Qué tiempo hizo durante tus últimas vacaciones?#¿Cómo fue el tiempo el verano pasado?#Past weather.
f#¿Qué vas a hacer en el futuro para proteger el planeta?#¿Cómo vas a ayudar al medio ambiente?#Future actions.
c#Si fueras presidente de tu país, ¿qué harías por el medio ambiente?#¿Qué cambiarías en tu ciudad para el medio ambiente?#Conditional.
d#Describe un lugar natural que te gusta.#¿Cuál es tu lugar favorito en la naturaleza? ¿Cómo es?#Description of a landscape.
f#¿Cómo será el clima dentro de cincuenta años?#¿Cómo será el planeta en el futuro?#Future prediction.
""",
)

C["C3"] = dict(
    theme="la tecnología y las redes sociales", tema="La tecnología",
    scene=["Estás en {city} con {fr}. {fr} te habla de su nuevo móvil.",
           "Estás en una tienda de tecnología en {city} con {fr}."],
    ex="""
{fr} dice:#Se me ha olvidado {v} en casa.#¿Qué ha olvidado {fr}?#aparato
{fr} dice:#Mis padres me han regalado {v}.#¿Qué le han regalado a {fr}?#aparato
{fr} dice:#Necesito {v} para hacer los deberes.#¿Qué necesita {fr}?#aparato
{fr} dice:#Lo que más hago con el móvil es {v}.#¿Qué hace {fr} con el móvil?#accion_digital
{fr} dice:#Esta noche voy a {v} con mis primos.#¿Qué va a hacer {fr} esta noche?#accion_digital
{fr} pregunta:#¿Me dejas {v}?#¿Qué quiere {fr}?#aparato
{fr} dice:#Ahora mismo no puedo; tengo que {v}.#¿Qué tiene que hacer {fr}?#accion_digital
{fr} dice:#Quiero comprar {v} nuevo.#¿Qué quiere comprar {fr}?#aparato
{fr} dice:#Antes de dormir me gusta {v}.#¿Qué hace {fr} antes de dormir?#accion_digital
""".replace("Quiero comprar {v} nuevo.", "Esta tienda vende {v} muy baratos.").replace("Esta tienda vende {v} muy baratos.#¿Qué quiere comprar {fr}?", "En esta tienda están de oferta {v}.#¿Qué está de oferta?").replace("En esta tienda están de oferta {v}.", "Hoy hay una oferta especial en {v}."),
    ann=dict(title="Una feria de tecnología para jóvenes", desc="un anuncio en una feria de tecnología", sp="Guía",
             open="Hola a todos y bienvenidos a la Feria Digital de {city}.",
             close="Y recordad: ¡usad la tecnología con cabeza!",
             facts="""
En la sala uno podéis probar gafas de realidad virtual.#En la sala uno se pueden probar:#gafas de realidad virtual;móviles nuevos;videojuegos antiguos;robots de cocina
A las {h=once|doce|cinco|cuatro} hay un taller para aprender a programar un robot.#El taller de robots es a las:#{h}
Los padres pueden asistir a una charla sobre la seguridad en internet.#La charla para padres es sobre:#la seguridad en internet;los precios de los móviles;los videojuegos;la música
Hay un concurso de vídeos cortos sobre el instituto del futuro.#El concurso es de:#vídeos cortos;fotos;dibujos;canciones
^El ganador del concurso recibirá una tableta nueva.#El ganador del concurso recibirá:#una tableta;un móvil;un portátil;unos auriculares
Hay conexión wifi gratis en toda la feria.#En toda la feria hay:#wifi gratis;comida gratis;música en directo;cargadores
Está prohibido grabar vídeos en la sala de presentaciones.#En la sala de presentaciones está prohibido:#grabar vídeos;hablar;comer;usar el ordenador
En la salida podéis reciclar móviles viejos.#En la salida se pueden reciclar:#móviles viejos;pilas;papel;botellas
"""),
    facts="""
Tengo móvil desde los doce años y lo uso sobre todo para hablar con mis amigos.#¿Para qué usas el móvil?#¿Para qué usa {N} el móvil sobre todo?#(Para) hablar con sus amigos#Refuse desde los doce años#Para hablar con sus amigos.;Para jugar.;Para estudiar.;Para hacer fotos.#Usa el móvil para comunicarse con amigos.#Nunca habla con sus amigos por el móvil.#1
Mis padres no me dejan usar el móvil durante la cena.#¿Hay normas en tu casa sobre el móvil?#¿Cuándo no puede usar {N} el móvil?#Durante la cena#Refuse mis padres#durante la cena;por la mañana;en el autobús;los fines de semana#En la mesa no se usa el móvil.#Puede usar el móvil durante la cena.#1
Uso el portátil para hacer los deberes y buscar información para mis proyectos.#¿Usas el ordenador para estudiar?#¿Para qué usa {N} el portátil? (Menciona una cosa.)#Hacer los deberes / buscar información#Refuse el portátil#Para hacer los deberes.;Para ver películas.;Para jugar en línea.;Para comprar ropa.#El portátil le sirve para estudiar.#No tiene ordenador.#1
Lo bueno de las redes sociales es que puedo hablar con mi prima que vive en Canadá.#¿Qué es lo bueno de las redes sociales?#¿Por qué le gustan a {N} las redes sociales?#Puede hablar con su prima (de Canadá)#Refuse Canadá on its own#Puede hablar con su prima.;Puede ver famosos.;Gana dinero.;Ve noticias.#Las redes le permiten estar en contacto con una familiar lejana.#Odia las redes sociales.#2
Lo malo de las redes sociales es que a veces la gente escribe comentarios crueles.#¿Y qué es lo malo de las redes sociales?#¿Qué es lo malo de las redes sociales según {N}?#(La gente escribe) comentarios crueles#Refuse a veces#Los comentarios crueles.;Los anuncios.;Son caras.;Son lentas.#Ha visto mensajes desagradables en internet.#Dice que en las redes todos son amables.#2
El mes pasado me robaron la contraseña y alguien publicó fotos en mi cuenta.#¿Has tenido algún problema en internet?#¿Qué le pasó a {N} el mes pasado?#Le robaron la contraseña#Refuse me robaron#Le robaron la contraseña.;Perdió el móvil.;Se le rompió el portátil.;Le llegó una factura enorme.#Alguien entró en su cuenta.#Nunca ha tenido problemas en internet.#2
^Desde entonces cambio la contraseña cada mes y nunca la comparto.#¿Qué haces ahora para estar segur<o|a>?#¿Cada cuánto cambia {N} su contraseña?#Cada mes#Refuse nunca la comparto#cada mes;cada semana;cada año;nunca#Ahora es más prudente.#Comparte su contraseña con todos.#2
Paso unas tres horas al día delante de la pantalla, y creo que es demasiado.#¿Cuánto tiempo pasas delante de la pantalla?#¿Qué opina {N} de las horas que pasa delante de la pantalla?#Es demasiado#Refuse tres horas#Que es demasiado.;Que es poco.;Que es normal.;Que no le importa.#Reconoce que usa demasiado las pantallas.#Cree que debería usar más la pantalla.#3
Mi abuela no sabía usar el móvil, pero le enseñé a hacer videollamadas.#¿Tu familia usa la tecnología?#¿Qué le enseñó {N} a su abuela?#(A hacer) videollamadas#Refuse no sabía#a hacer videollamadas;a mandar fotos;a jugar;a comprar por internet#Ayudó a su abuela con la tecnología.#Su abuela le enseñó a usar el móvil.#2
Prefiero leer libros de papel porque la pantalla me cansa los ojos.#¿Lees en papel o en pantalla?#¿Por qué prefiere {N} los libros de papel?#(Porque) la pantalla le cansa los ojos#Refuse prefiero leer#Porque la pantalla le cansa los ojos.;Porque son baratos.;Porque huelen bien.;Porque no tiene tableta.#Las pantallas le molestan a la vista.#Solo lee en la tableta.#2
En mi instituto está prohibido usar el móvil en clase, y estoy de acuerdo.#¿Se puede usar el móvil en tu instituto?#¿Qué piensa {N} de la norma del instituto?#Está de acuerdo#Refuse está prohibido tc#Está de acuerdo.;Le parece injusta.;No le importa.;No la conoce.#Apoya la prohibición del móvil en clase.#Se opone a la norma del instituto.#3
Ayer descargué una aplicación para aprender idiomas y ya he aprendido veinte palabras en japonés.#¿Usas aplicaciones para aprender?#¿Qué ha aprendido {N} con la aplicación?#Veinte palabras en japonés#Refuse una aplicación#veinte palabras en japonés;a cocinar;a programar;veinte palabras en chino#Está aprendiendo un idioma con el móvil.#Ayer borró todas sus aplicaciones.#2
Me gustaría estudiar informática y diseñar videojuegos en el futuro.#¿Qué te gustaría estudiar?#¿Qué le gustaría diseñar a {N}?#Videojuegos#Refuse informática#videojuegos;páginas web;robots;móviles#Le interesa crear juegos.#No le interesa la informática.#2
Creo que dentro de veinte años los coches no necesitarán conductor.#¿Cómo será la tecnología en el futuro?#¿Qué cree {N} sobre los coches del futuro?#No necesitarán conductor#Refuse dentro de veinte años#No necesitarán conductor.;Volarán.;Serán más baratos.;Desaparecerán.#Imagina coches que se conducen solos.#Piensa que los coches no cambiarán.#3
Antes jugaba en línea hasta muy tarde, pero ahora apago el móvil a las diez.#¿Ha cambiado tu uso de la tecnología?#¿A qué hora apaga {N} el móvil ahora?#A las diez#Refuse hasta muy tarde#a las diez;a medianoche;a las ocho;nunca#Ahora tiene una hora límite para el móvil.#Ahora juega hasta más tarde que antes.#2
Escribo un blog sobre cocina y cada semana subo una receta nueva.#¿Tienes un blog o un canal?#¿Qué sube {N} a su blog cada semana?#Una receta (nueva)#Refuse sobre cocina tc#una receta;un vídeo de música;fotos de viajes;noticias#Comparte recetas en internet.#Su blog es sobre deportes.#1
""",
    tq="""
p#¿Para qué usas el móvil?#¿Qué aparatos tecnológicos usas cada día?#Uses of devices.
p#¿Cuánto tiempo pasas en internet cada día?#¿Cuándo usas internet?#Time/frequency of use.
p#¿Qué redes sociales usas?#¿Usas las redes sociales?#Social media habits.
o#¿Qué ventajas tiene internet? ¿Por qué?#¿Es útil la tecnología para estudiar? ¿Por qué (no)?#Opinion + reason.
o#¿Son peligrosas las redes sociales? ¿Por qué (no)?#¿Qué desventajas tiene el móvil? ¿Por qué?#Opinion on risks.
pa#¿Cómo usaste la tecnología ayer?#¿Qué hiciste en internet el fin de semana pasado?#Past uses.
pa#¿Cuándo tuviste tu primer móvil? ¿Cómo era?#¿Cómo usabas la tecnología cuando eras pequeño/pequeña?#Past/imperfect.
f#¿Qué aparato vas a comprar en el futuro?#¿Cómo vas a usar la tecnología en tu futuro trabajo?#Future.
c#¿Podrías vivir una semana sin móvil? ¿Por qué (no)?#¿Qué inventarías para mejorar la vida de las personas?#Conditional + reason.
d#Explica cómo usan la tecnología los jóvenes de tu país.#Describe el papel de la tecnología en tu vida.#Description/explanation.
f#¿Cómo será la tecnología dentro de veinte años?#¿Cómo cambiará internet en el futuro?#Future prediction.
""",
    ads=("Tecnología y servicios digitales", """
Mi ordenador va muy lento y no sé por qué.#‘InfoDoctor’: reparamos y limpiamos ordenadores. Diagnóstico gratis en una hora.#‘Mundo Portátil’: venta de ordenadores nuevos con descuento.
Tengo ochenta años y quiero aprender a usar el móvil para hablar con mis nietos.#‘Mayores Conectados’: clases de móvil e internet para personas mayores, en grupos pequeños.#‘Código Joven’: cursos de programación para adolescentes.
Quiero hacer vídeos para mi canal, pero no sé cómo editarlos.#‘Taller de Vídeo’: aprende a grabar y editar vídeos con tu móvil en cuatro sesiones.#‘Cine Club’: proyecciones de películas clásicas los jueves.
Se me ha roto la pantalla del móvil y la necesito arreglada hoy.#‘Pantalla Express’: cambiamos la pantalla de tu móvil en 30 minutos.#‘MóvilNuevo’: los últimos modelos de móviles con pago a plazos.
Mi hijo pasa demasiadas horas con los videojuegos y no sé qué hacer.#‘Familias Digitales’: talleres para padres sobre el uso sano de las pantallas.#‘GameZone’: torneos de videojuegos para jóvenes todos los fines de semana.
Busco unos auriculares baratos para escuchar música cuando corro.#‘Sonido Sport’: auriculares deportivos resistentes al agua desde 15 euros.#‘Alta Fidelidad’: equipos de música profesionales para estudios de grabación.
Quiero aprender a crear mi propia página web para vender mis dibujos.#‘Web Fácil’: curso en línea para crear tu tienda en internet paso a paso.#‘Imprenta Rápida’: impresión de carteles y tarjetas.
"""),
)

C["C4"] = dict(
    theme="su barrio y su ciudad", tema="Mi ciudad y mi barrio",
    scene=["Estás en el centro de {city} con {fr}. Vais a hacer unos recados.",
           "Estás en {city} con {fr}. {fr} te enseña su barrio."],
    ex="""
{fr} dice:#Primero tengo que ir {v}.#¿Adónde tiene que ir {fr} primero?#tienda
{fr} dice:#Mi edificio favorito de la ciudad es {v}.#¿Cuál es el edificio favorito de {fr}?#lugar_ciudad
{fr} dice:#La parada del autobús está {v}.#¿Dónde está la parada del autobús?#direccion
{fr} dice:#Lo mejor de mi barrio es {v}.#¿Qué es lo mejor del barrio de {fr}?#lugar_ciudad
{fr} dice:#Esto cuesta {v}.#¿Cuánto cuesta?#precio
{fr} pregunta:#¿Sabes si {v} abre hoy?#¿Qué lugar quiere visitar {fr}?#lugar_ciudad
{fr} dice:#Mi madre trabaja {v}.#¿Dónde trabaja la madre de {fr}?#lugar_trabajo
{fr} dice:#Después tenemos que ir {v}.#¿Adónde tienen que ir después?#tienda
{fr} dice:#Puedes pagar {v}.#¿Cómo se puede pagar?#pago
""",
    signs=("En el centro de la ciudad", """
Zona peatonal#Por esta calle no pueden pasar los coches.#street
Ayuntamiento: información al ciudadano#Aquí puedo preguntar por los servicios de la ciudad.
Oficina de correos#Tengo que mandar un paquete a mi abuela.
Cajero automático#Necesito sacar dinero.
Aparcamiento completo#No hay sitio para dejar el coche.
Obras: calle cortada#No podemos pasar por aquí hoy.#street
Comisaría de policía#Me han robado la cartera y tengo que denunciarlo.
Mercado municipal: abierto por la mañana#Para comprar fruta fresca, hay que venir antes de comer.
Biblioteca: devolución de libros#Aquí dejo el libro que ya he leído.
Carril bici#Aquí sí se puede ir en bicicleta.#street
"""),
    ann=dict(title="La visita guiada por la ciudad", desc="una guía turística que habla a un grupo", sp="Guía",
             open="Buenos días a todos. Bienvenidos a esta visita por el centro histórico de {city}.",
             close="Y con esto terminamos la visita. Espero que les haya gustado.",
             facts="""
Primero vamos a ver la catedral, que tiene más de {n=quinientos|cuatrocientos|seiscientos|ochocientos} años.#La catedral tiene más de:#{n} años
^Después pasaremos por el mercado, donde pueden probar productos locales.#En el mercado se pueden:#probar productos locales;comprar ropa;ver una película;nadar
La plaza mayor es el centro de la vida de la ciudad; allí se celebran conciertos en verano.#En verano en la plaza mayor hay:#conciertos;partidos de fútbol;una feria de libros;un mercado de flores
El ayuntamiento es un edificio moderno de cristal.#El ayuntamiento es un edificio:#de cristal;de piedra;de madera;muy antiguo
Hay que tener cuidado al cruzar porque las calles son muy estrechas.#Hay que tener cuidado porque las calles son:#estrechas;oscuras;largas;peligrosas por la noche
La visita termina en el puerto a la una.#La visita termina en:#el puerto;la estación;el museo;el parque
Los billetes del autobús turístico se compran en la oficina de turismo.#Los billetes del autobús turístico se compran:#en la oficina de turismo;en el autobús;en el hotel;en la estación
"""),
    facts="""
Vivo en un barrio tranquilo a las afueras de la ciudad, cerca de un parque grande.#¿Dónde vives?#¿Dónde está el barrio de {N}?#(A las) afueras (de la ciudad)#Refuse cerca de un parque#a las afueras;en el centro;en el puerto;en el campo#Vive lejos del centro.#Vive en pleno centro.#1#+quiet
En mi barrio hay un supermercado, una farmacia y un polideportivo, pero no hay cine.#¿Qué hay en tu barrio?#¿Qué no hay en el barrio de {N}?#(Un) cine#Refuse supermercado#un cine;una farmacia;un polideportivo;un supermercado#Para ver una película tiene que salir de su barrio.#Hay tres cines en su barrio.#1
Lo mejor de vivir en la ciudad es que hay muchas cosas que hacer.#¿Qué es lo mejor de vivir en la ciudad?#¿Qué es lo mejor de la ciudad para {N}?#Hay muchas cosas que hacer#Refuse vivir en la ciudad tc#Hay muchas cosas que hacer.;Es tranquila.;Es barata.;Hay mucha naturaleza.#La ciudad ofrece mucho ocio.#Dice que en la ciudad no hay nada que hacer.#1
El centro de mi ciudad es muy bonito, con edificios antiguos y calles peatonales.#¿Cómo es el centro de tu ciudad?#¿Cómo son las calles del centro de la ciudad de {N}?#Peatonales / sin coches#Refuse antiguos#peatonales;muy anchas;muy sucias;oscuras#En el centro no hay coches en muchas calles.#En el centro hay atascos en todas las calles.#2
Lo que no me gusta es que los pisos son muy caros y muchas familias se van a otros pueblos.#¿Qué no te gusta de tu ciudad?#¿Por qué se van muchas familias a otros pueblos?#(Porque) los pisos son (muy) caros#Refuse no me gusta#Porque los pisos son caros.;Porque no hay trabajo.;Porque hay ruido.;Porque hace frío.#La vivienda es demasiado cara en su ciudad.#En su ciudad los pisos son baratos.#2
Hace dos años abrieron una biblioteca nueva y ahora voy allí a estudiar.#¿Ha cambiado tu barrio?#¿Qué abrieron hace dos años en el barrio de {N}?#Una biblioteca (nueva)#Refuse hace dos años#una biblioteca;un cine;un hospital;un centro comercial#Su barrio tiene un nuevo servicio público.#Hace dos años cerraron la biblioteca.#2
Los sábados voy al mercado con mi madre porque allí todo es más fresco.#¿Dónde hacéis la compra?#¿Por qué va {N} al mercado?#(Porque) todo es más fresco#Refuse con mi madre#Porque todo es más fresco.;Porque es más barato.;Porque está cerca.;Porque abre tarde.#Prefiere comprar productos frescos.#Nunca va al mercado.#1#+market
Prefiero ir de compras al centro comercial porque está todo en el mismo sitio.#¿Dónde prefieres ir de compras?#¿Por qué prefiere {N} el centro comercial?#(Porque) está todo en el mismo sitio#Refuse prefiero tc#Porque está todo en el mismo sitio.;Porque es barato.;Porque hay cine.;Porque está cerca.#Le resulta práctico el centro comercial.#Odia los centros comerciales.#2#-market
El año pasado perdí la cartera en el autobús y la policía me la devolvió al día siguiente.#¿Te ha pasado algo en la ciudad?#¿Quién le devolvió la cartera a {N}?#La policía#Refuse al día siguiente#la policía;el conductor;un amigo;una señora#Recuperó algo que había perdido.#Nunca encontró su cartera.#2
Cuando era pequeñ<o|a> vivíamos en un pueblo y no había ni tiendas ni autobuses.#¿Dónde vivías antes?#¿Qué no había en el pueblo donde vivía {N}? (Menciona una cosa.)#Tiendas / autobuses#Refuse un pueblo#Tiendas.;Escuelas.;Parques.;Casas.#Antes vivía en un lugar con pocos servicios.#Siempre ha vivido en la ciudad.#2
Creo que mi ciudad necesita más zonas verdes y menos coches.#¿Cómo se podría mejorar tu ciudad?#¿Qué necesita la ciudad de {N}? (Menciona una cosa.)#Más zonas verdes / menos coches#Refuse mi ciudad tc#Más zonas verdes.;Más tiendas.;Más coches.;Más hoteles.#Quiere más espacios con naturaleza en su ciudad.#Cree que la ciudad necesita más coches.#3
Si pudiera elegir, viviría en un pueblo, porque la vida es más tranquila.#¿Preferirías vivir en un pueblo o en una ciudad?#¿Por qué viviría {N} en un pueblo?#(Porque) la vida es más tranquila#Refuse viviría tc#Porque la vida es más tranquila.;Porque es más barato.;Porque tiene amigos allí.;Porque hay más trabajo.#Le atrae la tranquilidad de los pueblos.#Prefiere vivir en una gran ciudad.#3
Mi tienda favorita es una librería pequeña donde el dueño siempre me recomienda libros.#¿Cuál es tu tienda favorita?#¿Qué hace el dueño de la librería?#Le recomienda libros#Refuse es pequeña#Le recomienda libros.;Le hace descuentos.;Le regala libros.;Le habla de música.#El librero le da consejos de lectura.#Su tienda favorita es una zapatería.#2
Por la noche, mi barrio es un poco peligroso porque hay poca luz en las calles.#¿Es seguro tu barrio?#¿Por qué es un poco peligroso el barrio de {N} por la noche?#(Porque) hay poca luz (en las calles)#Refuse por la noche#Porque hay poca luz.;Porque hay mucho tráfico.;Porque hay ladrones.;Porque hay perros.#Faltan farolas en su barrio.#Su barrio es muy seguro por la noche.#3#-quiet
El próximo año van a construir una estación de metro al lado de mi casa.#¿Qué van a construir en tu barrio?#¿Qué van a construir al lado de la casa de {N}?#Una estación de metro#Refuse el próximo año#una estación de metro;un hospital;un centro comercial;un estadio#Pronto tendrá el metro muy cerca.#Van a cerrar la estación de metro.#2
Para ahorrar dinero, siempre comparo los precios en internet antes de comprar algo.#¿Cómo ahorras dinero cuando vas de compras?#¿Qué hace {N} antes de comprar algo?#Compara los precios (en internet)#Refuse ahorrar dinero#Compara los precios.;Pide dinero a sus padres.;Espera a las rebajas.;Pregunta a sus amigos.#Busca el mejor precio.#Compra sin mirar los precios.#2
""",
    tq="""
p#¿Cómo es tu barrio?#¿Qué hay en tu barrio?#Description of local area and facilities.
p#¿Dónde haces la compra?#¿Qué tiendas hay cerca de tu casa?#Shops and shopping habits.
p#¿Qué se puede hacer en tu ciudad?#¿Qué hay para los jóvenes en tu ciudad?#Activities and places.
o#¿Te gusta vivir en tu barrio? ¿Por qué (no)?#¿Qué es lo mejor de tu ciudad? ¿Por qué?#Opinion + reason.
o#¿Prefieres comprar en tiendas o por internet? ¿Por qué?#¿Te gusta ir de compras? ¿Por qué (no)?#Preference + reason.
pa#¿Qué hiciste en el centro de tu ciudad la última vez?#¿Qué compraste la última vez que fuiste de compras?#Past.
pa#¿Cómo era tu barrio hace diez años?#¿Cómo ha cambiado tu ciudad?#Imperfect / perfect.
f#¿Qué vas a hacer en tu ciudad este fin de semana?#¿Adónde vas a ir de compras la semana que viene?#Future.
c#¿Qué cambiarías en tu barrio? ¿Por qué?#¿Cómo sería tu ciudad ideal?#Conditional.
d#Describe un edificio importante de tu ciudad.#Describe el centro de tu ciudad.#Description.
f#¿Vas a vivir en la misma ciudad en el futuro? ¿Por qué (no)?#¿Dónde vas a vivir cuando termines tus estudios?#Future + reason.
""",
    ads=("Servicios de la ciudad", """
Acabo de llegar a la ciudad y necesito abrir una cuenta para recibir mi sueldo.#‘Banco Ciudad’: abre tu cuenta en diez minutos, sin comisiones para nuevos residentes.#‘Cambio de Divisas Plaza’: cambiamos euros, dólares y libras al mejor precio.
Quiero mandar un paquete grande a mi familia en otro país.#‘EnvíaMundo’: envío de paquetes a todo el mundo en cinco días.#‘Mensajería Local’: entregamos cartas dentro de la ciudad en una hora.
Tengo que hacer una fotocopia de mi pasaporte y no tengo impresora.#‘Copistería Centro’: fotocopias, impresión y escáner. Abierto también los sábados.#‘Foto Estudio Arte’: fotos profesionales para bodas.
Busco un sitio tranquilo para estudiar por las tardes con wifi.#‘Biblioteca Municipal’: salas de estudio con wifi gratis, de 9:00 a 21:00.#‘Café Ruidoso’: música en directo todas las tardes.
Quiero visitar la ciudad en poco tiempo y sin cansarme.#‘Bus Turístico’: recorre los monumentos en dos horas. Sube y baja cuando quieras.#‘Rutas a Pie’: paseos de cinco horas por el casco antiguo.
Necesito comprar flores para el cumpleaños de mi madre esta tarde.#‘Floristería Rosa’: ramos preparados al momento, abierto hasta las nueve.#‘Vivero Sur’: árboles y plantas grandes para jardines.
Mi bicicleta tiene una rueda pinchada y la necesito mañana para ir a trabajar.#‘Taller Bici Rápida’: reparación de bicicletas en el día.#‘Bicis de Alquiler’: alquila una bici por horas en el centro.
"""),
)

C["C5"] = dict(
    theme="las medidas", tema="Las medidas",
    scene=["Estás en el mercado de {city} con {fr}. Vais a comprar ingredientes para una receta.",
           "Estás en casa de {fr} en {city}. {fr} está decorando su habitación."],
    ex="""
{fr} dice:#Quiero {v} de queso, por favor.#¿Cuánto queso quiere {fr}?#peso
{fr} dice:#Para la receta necesitamos {v} de harina.#¿Cuánta harina necesitan?#peso
{fr} dice:#Compra también {v} de leche.#¿Cuánta leche hay que comprar?#volumen
{fr} dice:#Para la fiesta necesitamos {v} de zumo.#¿Cuánto zumo necesitan?#volumen
{fr} dice:#Mi nueva mesa es {v}.#¿Cómo es la mesa nueva de {fr}?#forma
{fr} dice:#La alfombra mide {v}.#¿Cuánto mide la alfombra?#longitud
{fr} dice:#El colegio está a {v} de mi casa.#¿A qué distancia está el colegio?#distancia
{fr} dice:#Mi habitación es {v}.#¿Cómo es la habitación de {fr}?#tamano
{fr} dice:#La ventana de la cocina es {v}.#¿Cómo es la ventana de la cocina?#forma
{fr} dice:#La playa está a {v} del hotel.#¿A qué distancia está la playa del hotel?#distancia
{fr} dice:#La estantería mide {v} de alto.#¿Cuánto mide la estantería?#longitud
""",
)

C["C6"] = dict(
    theme="los materiales", tema="Los materiales",
    scene=["Estás en una tienda de regalos en {city} con {fr}.",
           "Estás en un mercado de artesanía en {city} con {fr}."],
    ex="""
{fr} dice:#Esta mesa es {v}.#¿De qué material es la mesa?#materia
{fr} dice:#Me he comprado una pulsera {v}.#¿De qué es la pulsera de {fr}?#materia
{fr} dice:#Mi jersey favorito es {v}.#¿De qué es el jersey favorito de {fr}?#tela
{fr} dice:#Quiero un bolso {v}.#¿Qué tipo de bolso quiere {fr}?#tela
{fr} dice:#La caja de los juguetes es {v}.#¿De qué es la caja?#materia
{fr} dice:#Las botellas de esta tienda son {v}.#¿De qué material son las botellas?#materia
{fr} dice:#Esta camiseta es {v}.#¿De qué es la camiseta?#tela
{fr} pregunta:#¿Tienen esta lámpara {v}?#¿De qué material quiere la lámpara {fr}?#materia
{fr} dice:#Mi abuela me ha hecho unos guantes {v}.#¿De qué son los guantes?#tela
{fr} dice:#La estatua de la plaza es {v}.#¿De qué es la estatua?#materia
""",
)
