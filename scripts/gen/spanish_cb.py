"""Original content for Area B: Personal and social life (B1-B5). Format: see spanish.py."""

C = {}

C["B1"] = dict(
    theme="su familia y sus amigos", tema="La familia y los amigos",
    scene=["Estás en casa de {fr} en {city}. {fr} te enseña unas fotos de su familia.",
           "Estás en una fiesta en {city} con {fr}. {fr} te habla de la gente que hay en la fiesta."],
    ex="""
{fr} dice:#Vivo con {v} y con mis dos hermanos.#¿Con quién vive {fr}?#familiar
{fr} dice:#Esta foto es de {v} en la playa.#¿Quién está en la foto?#familiar
{fr} dice:#Mi hermana es muy {v}.#¿Cómo es la hermana de {fr}?#caracter
{fr} dice:#Mi mejor amiga es bastante {v}.#¿Cómo es la mejor amiga de {fr}?#caracter
{fr} dice:#Mi primo tiene {v}.#¿Cómo es el primo de {fr}?#pelo
{fr} dice:#Mi padre tiene {v}.#¿Cómo es el padre de {fr}?#pelo
{fr} dice:#En la granja de mis tíos hay {v}.#¿Qué animal hay en la granja?#animal
{fr} dice:#Mi abuela me ha regalado {v}.#¿Qué animal le ha regalado su abuela?#animal
{fr} dice:#Mañana viene a comer {v}.#¿Quién viene a comer mañana?#familiar
""",
    ann=dict(title="Una fiesta para toda la familia", desc="un anuncio en la radio sobre una fiesta de familias", sp="Locutora",
             open="¡Hola a todos! Este fin de semana se celebra en {city} el Día de la Familia.",
             close="¡Os esperamos con vuestras familias y vuestros amigos!",
             facts="""
La fiesta empieza el sábado {h=a las once|a las diez|a las doce|a las cuatro}.#La fiesta empieza el sábado:#*h
Se celebra en el parque grande, al lado del río.#La fiesta es en:#el parque;la playa;el polideportivo;el ayuntamiento
Habrá juegos para los niños y un concurso de fotos de familia.#Habrá un concurso de:#fotos de familia;cocina;baile;canto
Los abuelos pueden participar en una clase de baile tradicional.#Los abuelos pueden hacer una clase de:#baile;cocina;pintura;yoga
Las mascotas pueden venir, pero los perros tienen que llevar correa.#Los perros tienen que:#llevar correa;quedarse en casa;estar en el coche;llevar un collar rojo
La entrada cuesta {p=dos|tres|cinco|cuatro} euros por familia.#¿Cuánto cuesta la entrada por familia?#{p} euros
Si llueve, la fiesta se hará en el polideportivo.#Si llueve, la fiesta será en:#el polideportivo;el colegio;el cine;el teatro
El domingo por la tarde habrá un concierto de música para jóvenes.#El concierto del domingo es para:#los jóvenes;los abuelos;los niños pequeños;los padres
"""),
    facts="""
Tengo dos hermanos: Marcos tiene veinte años y estudia en la universidad, y Paula tiene solo seis.#¿Tienes hermanos?#¿Cuántos años tiene la hermana de {N}?#Seis (años)#Refuse veinte#seis años;veinte años;dieciséis años;diez años#Tiene una hermana pequeña.#Es hij<o|a> únic<o|a>.#1
Me llevo muy bien con mi hermano mayor porque siempre me ayuda con los deberes.#¿Te llevas bien con tus hermanos?#¿Por qué se lleva bien {N} con su hermano?#(Porque) le ayuda con los deberes#Refuse me ayuda#Porque le ayuda con los deberes.;Porque juegan al fútbol juntos.;Porque le da dinero.;Porque viven juntos.#Su hermano le echa una mano con las tareas del colegio.#Se lleva fatal con su hermano.#1
Con mi hermana pequeña es diferente: entra en mi habitación sin permiso y coge mis cosas.#¿Y con tu hermana pequeña?#¿Qué hace la hermana de {N} que le molesta? (Menciona una cosa.)#Entra en su habitación (sin permiso) / coge sus cosas#Refuse entra en mi habitación#Coge sus cosas.;Pone la música alta.;Llora mucho.;Le cuenta mentiras.#Su hermana usa sus cosas sin preguntar.#Su hermana nunca entra en su habitación.#2
Mis padres están divorciados, así que paso los fines de semana en casa de mi padre.#¿Con quién vives?#¿Dónde pasa {N} los fines de semana?#(En) casa de su padre#Refuse en casa de mi padre#en casa de su padre;en casa de su madre;en casa de sus abuelos;en casa de un amigo#El fin de semana está con su padre.#Sus padres viven juntos.#2
Soy bastante alt<o|a>, tengo el pelo castaño y llevo gafas para leer.#¿Cómo eres físicamente?#¿Para qué lleva gafas {N}?#Para leer#Refuse lleva gafas tc#para leer;para ver la tele;para conducir;para hacer deporte#Usa gafas cuando lee.#Nunca lleva gafas.#1
Mis amigos dicen que soy divertid<o|a> y generos<o|a>, pero a veces soy un poco impacient<e|e>.#¿Cómo eres de carácter?#¿Qué defecto tiene {N}, según sus amigos?#(Es un poco) impaciente#Refuse divertido/generoso#impaciente;perezos<o|a>;tímid<o|a>;egoísta#Reconoce que le falta paciencia a veces.#Sus amigos dicen que es muy serio.#2
Mi mejor amiga se llama Lucía; la conocí hace diez años en la guardería.#¿Quién es tu mejor amigo o amiga?#¿Dónde conoció {N} a su mejor amiga?#En la guardería#Refuse hace diez años#en la guardería;en el instituto;en la playa;en un campamento#Conoce a su mejor amiga desde que era pequeñ<o|a>.#Conoció a su mejor amiga el año pasado.#2
Lo que más me gusta de Lucía es que siempre dice la verdad, aunque a veces duele.#¿Qué te gusta de tu mejor amiga?#¿Qué es lo que más le gusta a {N} de su amiga?#Siempre dice la verdad / es sincera#Refuse duele#Que siempre dice la verdad.;Que es muy guapa.;Que le hace regalos.;Que es muy graciosa.#Valora la sinceridad de su amiga.#Su amiga miente a menudo.#2
Tenemos un perro que se llama Rufo; es viejo y duerme casi todo el día.#¿Tienes mascotas?#¿Qué hace el perro de {N} casi todo el día?#Dormir / duerme#Refuse es viejo#Duerme.;Corre por el jardín.;Ladra.;Juega con los niños.#Su perro es mayor y muy tranquilo.#Su perro es joven y muy activo.#1
El año pasado discutí con un amigo por una tontería y no nos hablamos durante un mes.#¿Has discutido alguna vez con un amigo?#¿Cuánto tiempo estuvieron sin hablarse {N} y su amigo?#Un mes#Refuse un año#un mes;una semana;un año;dos días#Se enfadó con un amigo por algo sin importancia.#Nunca discute con sus amigos.#2
Creo que un buen amigo tiene que saber escuchar y no criticar a los demás.#¿Cómo es un buen amigo para ti?#Según {N}, ¿qué tiene que saber hacer un buen amigo?#Escuchar#Refuse no criticar on its own tc#escuchar;cocinar;hablar idiomas;hacer deporte#Para {N} la amistad exige saber escuchar.#Cree que un buen amigo tiene que ser rico.#3
Mis abuelos viven en un pueblo pequeño y los visito todos los veranos.#¿Ves mucho a tus abuelos?#¿Cuándo visita {N} a sus abuelos?#(Todos los) veranos / en verano#Refuse en un pueblo#todos los veranos;cada fin de semana;en Navidad;nunca#Va al pueblo de sus abuelos en verano.#Sus abuelos viven en su casa.#1
Mi abuelo me enseñó a jugar al ajedrez cuando tenía siete años.#¿Qué te enseñaron tus abuelos?#¿Qué le enseñó a {N} su abuelo?#(A jugar al) ajedrez#Refuse siete años#a jugar al ajedrez;a nadar;a cocinar;a montar en bici#Aprendió un juego de mesa con su abuelo.#Su abuela le enseñó a jugar al ajedrez.#2
A veces mis padres son demasiado estrictos: tengo que volver a casa antes de las diez.#¿Tus padres son estrictos?#¿A qué hora tiene que volver {N} a casa?#Antes de las diez#Refuse a las diez on its own tc#antes de las diez;antes de las doce;antes de las ocho;cuando quiere#Tiene una hora límite para volver por la noche.#Puede volver a casa a la hora que quiere.#2
En el futuro me gustaría tener una familia grande, con tres o cuatro hijos.#¿Te gustaría tener hijos en el futuro?#¿Qué tipo de familia le gustaría tener a {N}?#(Una familia) grande / con tres o cuatro hijos#Refuse hijos tc#una familia grande;una familia pequeña;ningún hijo;un solo hijo#Quiere muchos hijos.#No quiere tener hijos.#2
Cuando sea mayor, quiero vivir cerca de mis padres para poder ayudarlos.#¿Dónde vivirás cuando seas mayor?#¿Por qué quiere {N} vivir cerca de sus padres?#Para (poder) ayudarlos#Refuse quiero ayudarlos#Para poder ayudarlos.;Porque es más barato.;Para no cocinar.;Porque le gusta el barrio.#Piensa cuidar de sus padres en el futuro.#Quiere vivir lejos de su familia.#3
""",
    tq="""
p#¿Cómo es tu familia?#¿Cuántas personas hay en tu familia?#Family members with brief description, e.g. *Somos cuatro: mis padres, mi hermano y yo.*
p#Descríbete físicamente.#¿Cómo eres?#Physical description, e.g. *Soy alto y tengo el pelo corto.*
p#¿Tienes mascotas?#¿Tienes algún animal en casa?#Pets or none, with details, e.g. *Tengo un gato negro.*
o#¿Te llevas bien con tu familia? ¿Por qué (no)?#¿Con quién te llevas mejor en tu familia? ¿Por qué?#Opinion + reason about relationships.
o#¿Qué cualidades debe tener un buen amigo? ¿Por qué?#¿Cómo es un buen amigo para ti? ¿Por qué?#Qualities + justification.
pa#¿Qué hiciste el fin de semana pasado con tus amigos?#¿Qué hiciste la última vez que saliste con tus amigos?#Past activities with friends.
pa#Háblame de cómo conociste a tu mejor amigo o amiga.#¿Dónde conociste a tu mejor amigo o amiga?#Past narrative: where/when they met.
f#¿Qué vas a hacer con tu familia el próximo fin de semana?#¿Qué planes tienes con tu familia?#Future plans with family.
c#¿Te gustaría tener una familia grande en el futuro? ¿Por qué (no)?#En el futuro, ¿cuántos hijos te gustaría tener? ¿Por qué?#Conditional + reason.
d#Describe a una persona importante en tu vida.#¿Quién es la persona más importante para ti? ¿Cómo es?#Description of a person: appearance, character, why important.
f#¿Cómo vas a celebrar tu próximo cumpleaños con tus amigos?#¿Qué harás con tus amigos en las vacaciones?#Future activities.
""",
)

C["B2"] = dict(
    theme="su casa y la vida en casa", tema="Mi casa",
    scene=["Estás en casa de {fr} en {city}. {fr} te enseña la casa.",
           "Vas a pasar una semana en el piso de la familia de {fr} en {city}."],
    ex="""
{fr} dice:#Mi lugar favorito de la casa es {v}.#¿Cuál es el lugar favorito de la casa de {fr}?#habitacion
{fr} dice:#Mi padre está en {v}.#¿Dónde está el padre de {fr}?#habitacion
{fr} dice:#En casa siempre tengo que {v}.#¿Qué tiene que hacer {fr} en casa?#tarea
{fr} dice:#Lo que más odio es {v}.#¿Qué tarea odia {fr}?#tarea
{fr} dice:#Me encanta {v} de mi habitación.#¿Qué le encanta a {fr} de su habitación?#mueble
{fr} dice:#Ayer mis padres compraron {v} para el salón.#¿Qué compraron los padres de {fr}?#mueble
{fr} dice:#Hoy desayunamos en {v}.#¿Dónde desayunan hoy?#habitacion
{fr} pregunta:#¿Puedes ayudarme a {v}?#¿Qué tienes que hacer?#tarea
{fr} dice:#Tu maleta está al lado de {v}.#¿Dónde está tu maleta?#mueble
""",
    signs=("En un bloque de pisos", """
Ascensor averiado#Hoy tenemos que subir a pie hasta el quinto piso.
No dejar bicicletas en la escalera#La bici tiene que ir a otro sitio, no aquí.
Cierre la puerta del garaje#Después de sacar el coche, hay que bajar la puerta.
Prohibido tender la ropa en el balcón#No se pueden secar las camisetas fuera de la ventana.
Buzones#Aquí recogemos las cartas.
Basura: bajarla después de las ocho de la tarde#No podemos sacar la bolsa por la mañana.
Piscina comunitaria: solo para vecinos#Mis amigos no pueden bañarse aquí conmigo.
Recién pintado#No toques la pared, que todavía no está seca.
Silencio a partir de las diez de la noche#Esta noche no podemos poner la música alta.
Se vende piso: tres dormitorios#Hay una casa grande en venta en este edificio.
"""),
    ann=dict(title="Una feria de casas", desc="un anuncio sobre una feria de la vivienda", sp="Locutor",
             open="Buenas tardes. Este mes llega a {city} la Feria de la Casa y el Hogar.",
             close="La entrada es libre. ¡Les esperamos!",
             facts="""
La feria está abierta del {d=diez al veinte|uno al quince|cinco al doce|veinte al treinta} de mayo.#La feria está abierta del:#{d} de mayo
En la primera sala hay muebles modernos para el salón y el dormitorio.#En la primera sala hay:#muebles;coches;ropa;libros
En la segunda planta se presentan cocinas que ahorran energía.#Las cocinas de la segunda planta:#ahorran energía;son muy baratas;son de madera;son muy grandes
Hay un taller para aprender a cuidar las plantas del jardín y de la terraza.#El taller enseña a:#cuidar las plantas;pintar paredes;cocinar;reparar muebles
Los niños pueden decorar una casa de muñecas en la zona infantil.#En la zona infantil los niños pueden:#decorar una casa de muñecas;ver películas;nadar;comer helados
Los visitantes pueden participar en un sorteo de una lavadora.#En el sorteo se puede ganar:#una lavadora;un sofá;un viaje;una televisión
La feria abre todos los días excepto el lunes.#La feria está cerrada:#el lunes;el domingo;el sábado;el viernes
Hay un autobús gratuito desde la estación de tren.#Desde la estación hay:#un autobús gratuito;un tren especial;taxis baratos;bicicletas gratis
"""),
    facts="""
Vivo en la cuarta planta de un edificio antiguo en el centro de la ciudad.#¿Dónde vives?#¿En qué planta vive {N}?#(En la) cuarta (planta) / (en el) cuarto (piso)#Refuse en el centro tc#en la cuarta planta;en la primera planta;en la planta baja;en la décima planta#Vive en un apartamento en el centro.#Vive en una casa en el campo.#1
El piso es pequeño: tiene dos dormitorios, un salón, una cocina y un solo cuarto de baño.#¿Cómo es tu piso?#¿Cuántos cuartos de baño hay en el piso de {N}?#Uno / un cuarto de baño#Refuse dos#uno;dos;tres;ninguno#Solo hay un baño en su casa.#Su piso tiene tres cuartos de baño.#1
Comparto el dormitorio con mi hermano y a veces es difícil porque él se acuesta muy tarde.#¿Tienes tu propia habitación?#¿Por qué es difícil para {N} compartir el dormitorio?#(Porque su hermano) se acuesta (muy) tarde#Refuse comparto el dormitorio#Porque su hermano se acuesta tarde.;Porque es muy pequeño.;Porque su hermano ronca.;Porque no hay armario.#No tiene un dormitorio para <él|ella> sol<o|a>.#Tiene una habitación para <él|ella> sol<o|a>.#2
Lo que más me gusta de mi casa es la terraza, porque allí cenamos en verano.#¿Qué es lo que más te gusta de tu casa?#¿Qué hace la familia de {N} en la terraza en verano?#Cenar / cenan#Refuse es la terraza tc#Cenar.;Dormir.;Tomar el sol.;Jugar a las cartas.#En verano comen fuera por la noche.#No tienen terraza.#1
En mi habitación tengo una cama, un escritorio para estudiar y muchos pósteres en las paredes.#¿Cómo es tu habitación?#¿Qué hay en las paredes de la habitación de {N}?#(Muchos) pósteres#Refuse una cama#muchos pósteres;muchas fotos;un espejo grande;nada#Ha decorado las paredes de su cuarto.#Las paredes de su cuarto están vacías.#1
Por la mañana me levanto a las siete, me ducho rápidamente y desayuno en la cocina.#¿Qué haces por la mañana antes de ir al instituto?#¿Dónde desayuna {N}?#En la cocina#Refuse en el comedor#en la cocina;en el salón;en el instituto;en su habitación#Desayuna en casa.#Desayuna en una cafetería.#1
En casa todos ayudamos: yo pongo la mesa y saco la basura, pero no me gusta nada planchar.#¿Ayudas en casa?#¿Qué tarea no le gusta a {N}?#Planchar#Refuse sacar la basura#planchar;poner la mesa;sacar la basura;cocinar#No le gusta planchar la ropa.#Le encanta planchar.#2
Mi madre dice que mi habitación siempre está desordenada, ¡y tiene razón!#¿Es ordenada tu habitación?#¿Qué piensa {N} de lo que dice su madre?#Tiene razón / está de acuerdo#Refuse está desordenada tc#Que tiene razón.;Que es injusto.;Que exagera.;Que no es verdad.#Admite que su cuarto no está ordenado.#Dice que su cuarto está siempre ordenado.#3
Antes vivíamos en una casa con jardín en las afueras, pero nos mudamos porque mi padre encontró trabajo aquí.#¿Siempre has vivido en esta casa?#¿Por qué se mudó la familia de {N}?#(Porque) su padre encontró trabajo (aquí)#Refuse vivíamos en las afueras#Porque su padre encontró trabajo.;Porque la casa era pequeña.;Porque querían un jardín.;Porque era cara.#Cambiaron de casa por el trabajo de su padre.#Siempre ha vivido en el mismo sitio.#2
Echo de menos el jardín de la otra casa, donde jugaba con mi perro.#¿Qué echas de menos de tu antigua casa?#¿Qué echa de menos {N}?#El jardín#Refuse el perro#el jardín;su habitación;sus vecinos;la piscina#Recuerda con cariño el jardín de antes.#Prefiere su piso actual en todo.#2
Lo malo de vivir en el centro es el ruido de los coches por la noche.#¿Qué es lo malo de vivir en el centro?#¿Qué es lo malo de vivir en el centro, según {N}?#El ruido (de los coches) (por la noche)#Refuse los coches on its own tc#el ruido;el precio;la contaminación;la falta de tiendas#Le molesta el ruido nocturno.#Dice que el centro es muy tranquilo.#2
Este fin de semana vamos a pintar el salón de amarillo para que tenga más luz.#¿Vais a cambiar algo en casa?#¿Por qué van a pintar el salón de amarillo?#Para que tenga más luz / para tener más luz#Refuse amarillo tc#Para que tenga más luz.;Porque es su color favorito.;Porque es barato.;Porque está sucio.#Quieren un salón más luminoso.#Van a pintar el salón de negro.#3
Mi sueño es vivir en una casa con piscina cerca del mar.#¿Cómo sería tu casa ideal?#¿Dónde estaría la casa ideal de {N}?#Cerca del mar / en la costa#Refuse con piscina#cerca del mar;en la montaña;en el centro;en el campo#Le gustaría vivir junto al mar.#Su casa ideal está en la montaña.#2
Nuestros vecinos son muy amables; cuando nos vamos de vacaciones, riegan nuestras plantas.#¿Cómo son tus vecinos?#¿Qué hacen los vecinos de {N} cuando la familia se va de vacaciones?#Riegan las plantas#Refuse son amables tc#Riegan las plantas.;Cuidan del perro.;Recogen las cartas.;Limpian la casa.#Sus vecinos les ayudan cuando están fuera.#Sus vecinos son muy antipáticos.#2
Ayer se rompió la lavadora y tuvimos que lavar la ropa a mano. ¡Qué lío!#¿Pasó algo en casa ayer?#¿Qué se rompió ayer en casa de {N}?#La lavadora#Refuse la ropa#la lavadora;la nevera;el horno;la televisión#Un aparato de la casa dejó de funcionar.#Ayer compraron una lavadora nueva.#2
Cuando tenga mi propio piso, tendré un gato y muchas plantas.#¿Qué tendrás cuando tengas tu propio piso?#¿Qué animal tendrá {N} en su propio piso?#Un gato#Refuse plantas#un gato;un perro;un pájaro;un pez#Planea vivir con un gato.#Nunca tendrá animales.#2
""",
    tq="""
p#¿Dónde vives?#¿Vives en una casa o en un piso?#Type and location of home, e.g. *Vivo en un piso en el centro.*
p#Describe tu habitación.#¿Qué hay en tu dormitorio?#Furniture and description of bedroom.
p#¿Qué haces para ayudar en casa?#¿Qué tareas haces en casa?#Chores in the present, e.g. *Pongo la mesa.*
o#¿Te gusta tu casa? ¿Por qué (no)?#¿Qué es lo que más te gusta de tu casa? ¿Por qué?#Opinion + reason.
o#¿Es justo que los jóvenes ayuden en casa? ¿Por qué (no)?#¿Deben los jóvenes ayudar en casa? ¿Por qué (no)?#Opinion + justification.
pa#¿Qué hiciste en casa el fin de semana pasado?#¿Cómo ayudaste en casa la semana pasada?#Past activities at home.
pa#¿Cómo era la casa donde vivías cuando eras pequeño/pequeña?#Describe la casa de tu infancia.#Imperfect description of a previous home.
f#¿Qué vas a hacer en casa esta tarde?#¿Qué vas a hacer este fin de semana en casa?#Future plans at home.
c#¿Cómo sería tu casa ideal?#Si pudieras cambiar algo de tu casa, ¿qué cambiarías?#Conditional description.
d#Describe un día normal en tu casa.#¿Cómo es tu rutina diaria en casa?#Daily routine with reflexive verbs.
f#¿Dónde vas a vivir en el futuro?#¿En qué tipo de casa vivirás de mayor?#Future: type and location of home.
""",
    ads=("Casas, muebles y servicios para el hogar", """
Busco un piso pequeño para alquilar cerca de la universidad; soy estudiante y no tengo mucho dinero.#‘Pisos Campus’: estudios baratos a cinco minutos de la universidad. Precios especiales para estudiantes.#‘Villas del Sol’: casas de lujo con piscina en la costa, para comprar.
Me mudo a un piso nuevo y necesito muebles baratos para el salón.#‘Mueble Fácil’: sofás, mesas y estanterías a precios bajos. Te lo llevamos a casa.#‘Antigüedades Rey’: muebles antiguos de gran valor para coleccionistas.
No tengo tiempo para limpiar la casa porque trabajo muchas horas.#‘Casa Limpia’: limpieza de pisos y casas por horas, también los fines de semana.#‘Jardín Verde’: cuidamos tu jardín y tus plantas.
Se me ha roto la lavadora y necesito que alguien la repare hoy mismo.#‘Reparaciones Rápidas’: arreglamos lavadoras, neveras y hornos en el mismo día.#‘ElectroHogar’: venta de electrodomésticos nuevos con entrega en una semana.
Quiero pintar mi dormitorio pero no sé qué color elegir.#‘Color y Hogar’: pinturas y consejos de decoradores para elegir el color perfecto.#‘Pintores Express’: pintamos fachadas y edificios grandes.
Tenemos un jardín grande y queremos plantar árboles frutales.#‘Vivero Naranjo’: árboles frutales, plantas y consejos para tu jardín.#‘Flores Marisa’: ramos de flores para regalar.
Vamos a pasar un mes en el campo y buscamos una casa con espacio para el perro.#‘Casas Rurales con Mascota’: casas en el campo con jardín vallado. Se admiten animales.#‘Hotel Urbano’: habitaciones en el centro. No se admiten animales.
"""),
)

C["B3"] = dict(
    theme="los colores", tema="Los colores",
    scene=["Estás en una tienda de {city} con {fr}. {fr} te habla de los colores de las cosas.",
           "Estás en casa de {fr} en {city}. {fr} va a pintar su habitación y habláis de colores."],
    ex="""
{fr} dice:#Mi color favorito es el {v}.#¿Cuál es el color favorito de {fr}?#color
{fr} dice:#Quiero pintar mi habitación de {v}.#¿De qué color quiere pintar su habitación?#color
{fr} dice:#Mi bicicleta nueva es {v}.#¿De qué color es la bicicleta de {fr}?#color_f
{fr} dice:#Hoy llevo una camiseta {v}.#¿De qué color es la camiseta de {fr}?#color_f
{fr} dice:#Me he comprado unos calcetines {v}.#¿De qué color son los calcetines?#color_pl
{fr} dice:#El coche de mis padres es {v}.#¿De qué color es el coche?#color
{fr} dice:#La puerta de mi casa es {v}.#¿De qué color es la puerta de la casa de {fr}?#color_f
{fr} dice:#Los autobuses de mi ciudad son {v}.#¿De qué color son los autobuses?#color_pl
{fr} pregunta:#¿Tienen esta chaqueta en {v}?#¿En qué color quiere la chaqueta {fr}?#color
{fr} dice:#Mi gato es completamente {v}.#¿De qué color es el gato de {fr}?#color
""",
)

C["B4"] = dict(
    theme="la ropa y la moda", tema="La ropa y la moda",
    scene=["Estás en un centro comercial de {city} con {fr}. Vais a comprar ropa.",
           "Estás en casa de {fr} en {city}. {fr} está preparando la maleta para un viaje."],
    ex="""
{fr} dice:#Para la fiesta voy a comprar {v}.#¿Qué va a comprar {fr} para la fiesta?#ropa
{fr} dice:#Para el invierno necesito {v}.#¿Qué necesita {fr} para el invierno?#ropa
{fr} dice:#En la maleta llevo {v}.#¿Qué lleva {fr} en la maleta?#ropa
{fr} dice:#Esta camiseta cuesta {v}.#¿Cuánto cuesta la camiseta?#precio
{fr} dice:#Voy a pagar {v}.#¿Cómo va a pagar {fr}?#pago
{fr} dice:#Ahora vamos {v}.#¿Adónde van ahora?#tienda
{fr} pregunta:#Este jersey, ¿lo tienen en {v}?#¿De qué color quiere el jersey {fr}?#color
{fr} dice:#Los vaqueros cuestan {v}.#¿Cuánto cuestan los vaqueros?#precio
{fr} dice:#Mi abuela me ha regalado {v}.#¿Qué le ha regalado su abuela a {fr}?#ropa
""",
    signs=("En unos grandes almacenes", """
Probadores#Antes de comprar los pantalones, quiero ver si me quedan bien.#pantalones
Rebajas: hasta el 50 %#Hoy la ropa está mucho más barata que de costumbre.
Moda infantil: tercera planta#Busco ropa para mi hermano pequeño de cuatro años.
Zapatería#Necesito unas botas nuevas.#shoes
Caja: pague aquí#Ya he elegido la falda; ahora tengo que pagarla.
No se admiten devoluciones de ropa interior#No puedes cambiar los calcetines después de comprarlos.
Complementos: bolsos, cinturones y gafas de sol#Quiero un regalo para mi madre que no sea ropa.
Servicio de arreglos#Los pantalones son demasiado largos y hay que cortarlos.#pantalones
Ropa deportiva#Me hacen falta unas zapatillas para correr.#shoes
Salida#Ya hemos terminado las compras y nos vamos a casa.
"""),
    ann=dict(title="Las rebajas en el centro comercial", desc="un anuncio en un centro comercial", sp="Locutora",
             open="Atención, señores clientes. Bienvenidos al centro comercial Las Torres de {city}.",
             close="Gracias por su visita y felices compras.",
             facts="""
Hoy empiezan las rebajas de verano en todas las tiendas de ropa.#Hoy empiezan las rebajas de:#verano;invierno;primavera;Navidad
En la tienda de deportes, las zapatillas tienen un descuento del {p=cuarenta|treinta|veinte|sesenta} por ciento.#Las zapatillas tienen un descuento del:#{p} por ciento
La tienda de ropa infantil está ahora en la primera planta.#La tienda de ropa infantil está:#en la primera planta;en la planta baja;en la segunda planta;en el aparcamiento
Si compran dos camisetas, la tercera es gratis.#Si compras dos camisetas:#la tercera es gratis;te dan un bolso;pagas la mitad;te dan un café
Los probadores de la segunda planta están cerrados por obras.#Los probadores cerrados están:#en la segunda planta;en la primera planta;en la planta baja;en la tercera planta
A las seis de la tarde hay un desfile de moda en la plaza central.#A las seis hay:#un desfile de moda;un concierto;un concurso;una película
Los clientes con la tarjeta del centro comercial tienen aparcamiento gratis.#Con la tarjeta del centro comercial tienes:#aparcamiento gratis;un regalo;un café gratis;un descuento en el cine
El centro comercial cierra hoy a las diez de la noche.#Hoy el centro comercial cierra:#a las diez de la noche;a las ocho de la tarde;a medianoche;a las nueve de la noche
"""),
    facts="""
En mi instituto llevamos uniforme: una camisa blanca, un jersey azul y pantalones grises.#¿Llevas uniforme en el instituto?#¿De qué color es el jersey del uniforme de {N}?#Azul#Refuse blanco#azul;gris;blanco;negro#Tiene que llevar uniforme en clase.#En su instituto no hay uniforme.#1
Me parece bien llevar uniforme porque por la mañana no pierdo tiempo eligiendo ropa.#¿Qué opinas del uniforme?#¿Por qué le parece bien el uniforme a {N}?#(Porque) no pierde tiempo eligiendo ropa (por la mañana)#Refuse no pierdo tiempo#Porque no pierde tiempo por la mañana.;Porque es barato.;Porque es bonito.;Porque es cómodo.#El uniforme le ahorra tiempo.#Odia el uniforme.#2
Los fines de semana prefiero ropa cómoda: vaqueros, una sudadera y zapatillas.#¿Qué ropa llevas los fines de semana?#¿Qué tipo de ropa prefiere {N} los fines de semana?#(Ropa) cómoda#Refuse vaqueros on its own tc#ropa cómoda;ropa elegante;ropa de marca;ropa deportiva#No le gusta ir elegante en su tiempo libre.#Los sábados siempre lleva traje.#1
No me interesa mucho la moda; no compro ropa de marca porque es demasiado cara.#¿Te interesa la moda?#¿Por qué no compra {N} ropa de marca?#(Porque) es (demasiado) cara#Refuse no me interesa#Porque es demasiado cara.;Porque es fea.;Porque no hay tiendas.;Porque sus padres no le dejan.#El precio de las marcas le parece excesivo.#Solo compra ropa de marca.#1
Compro casi toda mi ropa en tiendas de segunda mano, porque así ayudo al medio ambiente.#¿Dónde compras tu ropa?#¿Dónde compra {N} casi toda su ropa?#En tiendas de segunda mano#Refuse en internet#en tiendas de segunda mano;por internet;en el mercado;en grandes almacenes#Prefiere la ropa usada.#Siempre compra ropa nueva.#2
La semana pasada compré una chaqueta por internet, pero me quedaba pequeña y tuve que devolverla.#¿Has comprado ropa por internet?#¿Qué problema tuvo {N} con la chaqueta?#(Le quedaba) pequeña#Refuse tuve que devolverla#Le quedaba pequeña.;Era de otro color.;Llegó rota.;No llegó.#La chaqueta no era de su talla.#La chaqueta le quedaba perfecta.#2
Mi prenda favorita es una bufanda roja que me hizo mi abuela.#¿Cuál es tu prenda de ropa favorita?#¿Quién hizo la bufanda de {N}?#Su abuela#Refuse mi abuela#su abuela;su madre;su tía;una amiga#Tiene una bufanda hecha a mano.#Compró su bufanda en una tienda.#1
Para la boda de mi prima llevé un traje azul oscuro y unos zapatos nuevos que me hacían daño.#¿Qué llevaste a la última boda?#¿Qué problema tuvo {N} en la boda?#Los zapatos le hacían daño#Refuse me hacían daño#Los zapatos le hacían daño.;El traje era grande.;Tenía frío.;Se manchó la camisa.#Sus zapatos eran incómodos.#Llevó zapatillas a la boda.#2
Creo que la gente gasta demasiado dinero en ropa que solo se pone una o dos veces.#¿Gastamos demasiado en ropa?#¿Qué critica {N}?#Que la gente gasta demasiado (dinero) en ropa / compra ropa que casi no usa#Refuse gasta dinero tc#Que se compra ropa que casi no se usa.;Que la ropa es fea.;Que las tiendas cierran pronto.;Que no hay rebajas.#Critica el consumo excesivo de ropa.#Cree que hay que comprar más ropa.#3
Mi hermana trabaja en una tienda de ropa los sábados y le hacen descuento.#¿Alguien de tu familia trabaja en una tienda?#¿Qué ventaja tiene la hermana de {N} por trabajar en la tienda?#(Le hacen) descuento#Refuse los sábados#Le hacen descuento.;Gana mucho dinero.;Trabaja poco.;Tiene ropa gratis.#Su hermana paga menos por la ropa.#Su hermana trabaja en un banco.#2
Cuando era pequeñ<o|a>, mi madre elegía mi ropa y yo lo odiaba.#¿Quién elegía tu ropa cuando eras pequeñ<o|a>?#¿Qué pensaba {N} cuando su madre elegía su ropa?#Lo odiaba / no le gustaba#Refuse mi madre elegía#Lo odiaba.;Le encantaba.;No le importaba.;Le daba risa.#De niñ<o|a> no podía elegir su ropa.#Siempre ha elegido su propia ropa.#2
Me gusta ir de compras con mis amigos, pero cuando voy sol<o|a> compro más rápido.#¿Te gusta ir de compras?#¿Qué ventaja tiene para {N} ir de compras sol<o|a>?#Compra más rápido#Refuse con mis amigos#Compra más rápido.;Gasta menos.;Encuentra más cosas.;Se divierte más.#Tarda menos cuando compra sin compañía.#Odia ir de compras con sus amigos.#3
Para el viaje a Noruega tengo que comprar un abrigo muy caliente y unos guantes.#¿Qué ropa necesitas para tu viaje?#¿Qué tiene que comprar {N} para el viaje? (Menciona una cosa.)#(Un) abrigo / (unos) guantes#Refuse Noruega#Un abrigo y unos guantes.;Un bañador.;Unas sandalias.;Una gorra.#Necesita ropa de invierno para el viaje.#Va a un país muy caluroso.#2
El año que viene quiero aprender a coser para hacer mi propia ropa.#¿Qué te gustaría aprender?#¿Para qué quiere aprender a coser {N}?#Para hacer su propia ropa#Refuse el año que viene#Para hacer su propia ropa.;Para trabajar en una tienda.;Para ayudar a su abuela.;Para ahorrar.#Quiere diseñar y fabricar su ropa.#Ya sabe coser muy bien.#2
Si fuera ric<o|a>, no compraría ropa cara; preferiría viajar.#¿Qué harías si fueras ric<o|a>?#¿Qué preferiría hacer {N} con mucho dinero?#Viajar#Refuse comprar ropa cara#Viajar.;Comprar ropa cara.;Comprar un coche.;Ahorrar.#No gastaría el dinero en ropa.#Gastaría todo en ropa de marca.#3
Llevo el pelo largo y siempre uso pendientes; es mi estilo.#¿Cómo describirías tu estilo?#¿Qué complemento lleva siempre {N}?#Pendientes#Refuse el pelo largo#pendientes;un collar;una gorra;un reloj#Siempre lleva pendientes.#Nunca lleva complementos.#1
""",
    tq="""
p#¿Qué ropa llevas normalmente los fines de semana?#¿Qué te pones para salir con tus amigos?#Clothes with colours, e.g. *Llevo vaqueros y una camiseta negra.*
p#¿Llevas uniforme en tu instituto? ¿Cómo es?#Describe la ropa que llevas para ir al instituto.#Description of uniform/clothes.
p#¿Dónde compras tu ropa?#¿Con quién vas de compras?#Shops/online + companions.
o#¿Qué opinas del uniforme escolar? ¿Por qué?#¿Te gusta llevar uniforme? ¿Por qué (no)?#Opinion + reason.
o#¿Es importante llevar ropa de marca? ¿Por qué (no)?#¿Qué piensas de la moda? ¿Por qué?#Opinion + justification.
pa#¿Qué ropa compraste la última vez que fuiste de compras?#Háblame de la última vez que fuiste de compras.#Past: purchases, prices, opinion.
pa#¿Qué llevaste en una fiesta reciente?#¿Qué ropa llevaste el fin de semana pasado?#Past description of clothes worn.
f#¿Qué ropa vas a comprar para el verano?#¿Qué vas a llevar en tu próxima fiesta?#Future: clothes planned.
c#Si tuvieras mucho dinero, ¿qué ropa comprarías?#¿Cómo sería tu ropa ideal?#Conditional.
d#Describe la ropa que está de moda entre los jóvenes de tu país.#¿Cómo se visten los jóvenes en tu país?#Description of fashion.
f#¿Cómo vas a vestirte en tu próxima celebración familiar?#¿Qué ropa llevarás de vacaciones?#Future.
""",
    ads=("Tiendas de ropa y complementos", """
Busco ropa elegante para una boda, pero no quiero gastar mucho y solo la voy a llevar una vez.#‘Viste y Devuelve’: alquiler de trajes y vestidos de fiesta. Precios desde 30 euros.#‘Alta Costura Lola’: vestidos de novia exclusivos hechos a mano.
Me encanta correr y necesito zapatillas especiales para correr por la montaña.#‘Corre Libre’: calzado técnico para correr en montaña. Prueba las zapatillas en nuestra pista.#‘Zapatería Clásica’: zapatos de piel para oficina y ceremonias.
Mi bebé crece muy rápido y quiero ropa de segunda mano en buen estado.#‘Pequeños Pasos’: ropa usada para bebés y niños, limpia y como nueva.#‘Juguetería Osito’: juguetes para bebés.
Quiero comprar ropa sin salir de casa y que me la traigan en un día.#‘ModaYa’: tienda en línea con entrega en 24 horas y devolución gratis.#‘Mercadillo de los Domingos’: ropa barata en la plaza, solo los domingos por la mañana.
Tengo unos pantalones preferidos que se han roto y quiero que los arreglen.#‘La Aguja de Oro’: arreglos de ropa rápidos: cremalleras, botones, pantalones.#‘Tintorería Blanca’: limpieza en seco de trajes y abrigos.
Necesito un regalo para mi novia: le encantan los complementos originales.#‘Bisutería Luna’: pendientes, pulseras y collares diseñados por artistas locales.#‘Relojes Exactos’: reparación de relojes de todas las marcas.
Hago esquí cada invierno y necesito una chaqueta que no deje pasar el frío.#‘Nieve Total’: ropa de esquí impermeable y muy caliente, para adultos y niños.#‘Playa Bonita’: bañadores y ropa de verano.
"""),
)

C["B5"] = dict(
    theme="su tiempo libre", tema="El tiempo libre",
    scene=["Estás en {city} con {fr}. Habláis de lo que hacéis en vuestro tiempo libre.",
           "Estás en casa de {fr} en {city}. Estáis organizando el fin de semana."],
    ex="""
{fr} dice:#Los sábados juego {v}.#¿A qué juega {fr} los sábados?#deporte
{fr} dice:#Mi hermano juega {v} en un equipo.#¿A qué juega el hermano de {fr}?#deporte
{fr} dice:#En mi tiempo libre me encanta {v}.#¿Qué le encanta hacer a {fr}?#actividad
{fr} dice:#En verano me gusta mucho {v}.#¿Qué le gusta hacer a {fr} en verano?#actividad
{fr} dice:#Desde hace dos años toco {v}.#¿Qué instrumento toca {fr}?#instrumento
{fr} dice:#Esta noche vamos a ver una película {v}.#¿Qué tipo de película van a ver?#pelicula
{fr} pregunta:#¿Quieres ir a ver {v} el sábado?#¿Qué quiere ver {fr} el sábado?#evento
{fr} dice:#Mi película favorita es {v}.#¿Qué tipo de película prefiere {fr}?#pelicula
{fr} dice:#Ayer fuimos a ver {v}.#¿Qué fueron a ver ayer?#evento
{fr} dice:#Mi hermana quiere aprender a tocar {v}.#¿Qué instrumento quiere aprender la hermana de {fr}?#instrumento
""",
    signs=("En el polideportivo", """
Piscina cubierta#Aunque llueva, podemos nadar aquí.
Gorro de baño obligatorio#No puedes nadar sin cubrirte el pelo.
Vestuarios#Aquí nos cambiamos de ropa antes del partido.
Prohibido saltar desde el borde#No se puede entrar en el agua de un salto.
Pista de tenis: reserve en recepción#Para jugar con la raqueta, primero hay que pedir la pista.
Gimnasio: mayores de 16 años#Mi hermano de doce años no puede entrar en esta sala.
Clases de baile: martes y jueves#Si quieres bailar, tienes que venir dos días a la semana.
Cafetería#Después de entrenar podemos tomar algo.
Taquillas: traiga su candado#Para guardar tu mochila, necesitas tu propio cierre.
No se permite comer en la piscina#El bocadillo tiene que esperar hasta salir del agua.
"""),
    ann=dict(title="Las actividades de verano para jóvenes", desc="un anuncio en la radio sobre actividades de verano", sp="Locutor",
             open="¡Hola, chicos y chicas! El ayuntamiento de {city} presenta las actividades de verano para jóvenes.",
             close="Las plazas son limitadas, así que apuntaos pronto.",
             facts="""
Las actividades empiezan el primer lunes de julio.#Las actividades empiezan:#en julio;en junio;en agosto;en septiembre
Hay cursos de vela en el lago para jóvenes de {e=doce a dieciséis|catorce a dieciocho|diez a catorce|trece a diecisiete} años.#Los cursos de vela son para jóvenes de:#{e} años
Para el curso de vela hay que saber nadar.#Para el curso de vela es necesario:#saber nadar;tener barco;llevar un amigo;pagar en efectivo
También hay un taller de teatro que termina con una obra en agosto.#El taller de teatro termina con:#una obra;un concierto;una excursión;una fiesta
Los amantes de la música pueden formar un grupo y grabar una canción.#En el taller de música los jóvenes pueden:#grabar una canción;comprar instrumentos;ir a un concierto;aprender a bailar
Todos los viernes hay cine al aire libre en la plaza.#El cine al aire libre es:#los viernes;los sábados;los domingos;los lunes
Las excursiones a la montaña salen a las ocho de la mañana desde el ayuntamiento.#Las excursiones salen desde:#el ayuntamiento;la estación;el polideportivo;el colegio
Para apuntarse, hay que rellenar un formulario en la página web.#Para apuntarse hay que:#rellenar un formulario en la web;llamar por teléfono;ir al ayuntamiento;mandar una carta
"""),
    facts="""
Entre semana tengo poco tiempo libre porque tengo muchos deberes.#¿Tienes mucho tiempo libre?#¿Por qué tiene poco tiempo libre {N} entre semana?#(Porque tiene) muchos deberes#Refuse tengo deberes#Porque tiene muchos deberes.;Porque trabaja.;Porque cuida a su hermano.;Porque entrena todos los días.#Las tareas del colegio le ocupan mucho tiempo.#Entre semana tiene mucho tiempo libre.#1
Mi pasatiempo favorito es la fotografía; siempre llevo la cámara cuando salgo.#¿Cuál es tu pasatiempo favorito?#¿Qué lleva siempre {N} cuando sale?#La cámara#Refuse la fotografía#la cámara;el móvil;un libro;la guitarra#Le encanta hacer fotos.#Nunca hace fotos.#1
Juego al baloncesto en el equipo del barrio y entrenamos los martes y los jueves.#¿Haces algún deporte?#¿Cuándo entrena {N}?#(Los) martes y (los) jueves#Refuse los fines de semana#los martes y los jueves;los lunes y los miércoles;los sábados;todos los días#Entrena dos días a la semana.#Entrena todos los días.#1
El mes pasado ganamos el campeonato regional y lo celebramos con una cena.#¿Habéis ganado algún partido importante?#¿Cómo celebró el equipo de {N} la victoria?#Con una cena#Refuse ganamos el campeonato#Con una cena.;Con una fiesta en la playa.;Con un viaje.;Con un concierto.#Su equipo tuvo éxito recientemente.#Su equipo perdió el campeonato.#2
Me encanta leer novelas de misterio antes de dormir.#¿Te gusta leer?#¿Cuándo lee {N}?#Antes de dormir / por la noche#Refuse novelas de misterio#antes de dormir;en el autobús;en el recreo;por la mañana#Lee por la noche.#Odia leer.#1
No veo mucho la tele; prefiero ver series en el móvil cuando quiero.#¿Ves mucho la televisión?#¿Por qué prefiere {N} ver series en el móvil?#Puede verlas cuando quiere#Refuse no veo la tele#Porque puede verlas cuando quiere.;Porque la tele está rota.;Porque es gratis.;Porque se ve mejor.#Le gusta elegir cuándo ve las series.#Ve la tele cinco horas al día.#2
Antes tocaba el violín, pero lo dejé porque el profesor era muy exigente.#¿Tocas algún instrumento?#¿Por qué dejó {N} el violín?#(Porque) el profesor era (muy) exigente#Refuse tocaba el violín#Porque el profesor era muy exigente.;Porque era caro.;Porque se rompió.;Porque no tenía tiempo.#Abandonó la música por un profesor estricto.#Todavía toca el violín.#2
Los sábados por la noche suelo ir al cine con mis amigos, aunque las entradas son caras.#¿Qué haces los sábados por la noche?#¿Qué es lo malo de ir al cine, según {N}?#Las entradas son caras#Refuse con mis amigos#Las entradas son caras.;Las películas son malas.;El cine está lejos.;Hay mucha gente.#Ir al cine le cuesta bastante dinero.#Las entradas del cine son gratis.#2
El verano pasado hice un curso de surf en la costa y me encantó, aunque me caí muchas veces.#¿Qué hiciste el verano pasado?#¿Qué aprendió {N} el verano pasado?#(A hacer) surf#Refuse me caí#surf;vela;buceo;tenis#Probó un deporte de agua en verano.#El verano pasado no salió de casa.#2
Creo que los jóvenes pasan demasiado tiempo con los videojuegos y poco tiempo al aire libre.#¿Qué opinas de los videojuegos?#¿Qué opina {N} de los jóvenes?#Pasan demasiado tiempo con los videojuegos / poco tiempo al aire libre#Refuse los videojuegos tc#Pasan poco tiempo al aire libre.;Leen mucho.;Hacen mucho deporte.;Trabajan demasiado.#Le preocupa que los jóvenes no salgan.#Cree que los jóvenes salen demasiado.#3
Me gustaría hacer paracaidismo algún día, pero a mi madre le da miedo.#¿Hay algo que te gustaría probar?#¿Quién no quiere que {N} haga paracaidismo?#Su madre#Refuse le da miedo tc#su madre;su padre;su hermano;su entrenador#Su madre se preocupa por esta actividad.#Su madre también quiere hacer paracaidismo.#3
Este sábado voy a ir a un concierto de mi grupo favorito con mi prima.#¿Qué vas a hacer este fin de semana?#¿Con quién va a ir {N} al concierto?#(Con) su prima#Refuse mi prima#con su prima;con su hermano;con sus padres;con un amigo#Va a ver a su grupo preferido.#Va al concierto sol<o|a>.#1
Para mí, lo mejor del tiempo libre es poder desconectar de los estudios.#¿Para qué sirve el tiempo libre?#Según {N}, ¿qué es lo mejor del tiempo libre?#(Poder) desconectar de los estudios#Refuse los estudios tc#Desconectar de los estudios.;Ganar dinero.;Dormir.;Ver a la familia.#El tiempo libre le ayuda a olvidarse del colegio.#En su tiempo libre estudia más.#3
Cuando hace mal tiempo, juego a juegos de mesa con mi familia.#¿Qué haces cuando llueve?#¿Qué hace {N} cuando hace mal tiempo?#Juega a juegos de mesa (con su familia)#Refuse juego#Juega a juegos de mesa.;Ve películas.;Duerme.;Va al gimnasio.#Los días de lluvia juega con su familia.#Cuando llueve sale a correr.#2
El año que viene quiero apuntarme a un club de ajedrez del barrio.#¿Qué actividad nueva te gustaría hacer?#¿A qué quiere apuntarse {N} el año que viene?#(A un club de) ajedrez#Refuse el año que viene#a un club de ajedrez;a un equipo de fútbol;a clases de baile;a un coro#Quiere entrar en un club de ajedrez.#Ya es miembro de un club de ajedrez.#2
Mis padres me dan diez euros a la semana y los gasto casi todos en salir con mis amigos.#¿Cuánto dinero gastas en tu tiempo libre?#¿En qué gasta {N} su dinero?#(En) salir con sus amigos#Refuse diez euros#en salir con sus amigos;en ropa;en videojuegos;en libros#Usa su paga para salir.#Ahorra todo su dinero.#2#spain
""",
    tq="""
p#¿Qué haces en tu tiempo libre?#¿Qué te gusta hacer cuando no tienes clase?#Activities in the present, e.g. *Juego al fútbol y leo.*
p#¿Practicas algún deporte?#¿Qué deporte haces?#Sport with frequency, e.g. *Nado dos veces a la semana.*
p#¿Qué tipo de música te gusta?#¿Tocas algún instrumento?#Music preferences or instrument.
o#¿Prefieres ver una película en casa o en el cine? ¿Por qué?#¿Te gusta ir al cine? ¿Por qué (no)?#Preference + reason.
o#¿Es importante tener tiempo libre? ¿Por qué (no)?#¿Tienes bastante tiempo libre? ¿Por qué (no)?#Opinion + justification.
pa#¿Qué hiciste el fin de semana pasado?#¿Qué hiciste el sábado pasado?#Past activities.
pa#Háblame de un evento (concierto, partido…) al que fuiste.#¿Fuiste a algún concierto o partido el año pasado? ¿Qué tal?#Past narrative + opinion.
f#¿Qué vas a hacer el próximo fin de semana?#¿Qué planes tienes para el sábado?#Future plans.
c#¿Qué deporte o actividad nueva te gustaría probar? ¿Por qué?#Si tuvieras más tiempo libre, ¿qué harías?#Conditional + reason.
d#Describe tu fin de semana ideal.#¿Cómo sería un sábado perfecto para ti?#Description with conditional/present.
f#¿Qué vas a hacer durante las próximas vacaciones?#¿Adónde vas a ir en verano?#Future activities.
""",
    ads=("Actividades de tiempo libre", """
Me encanta cantar y busco un grupo para cantar con otras personas una vez por semana.#‘Coro Voces del Barrio’: ensayos todos los miércoles. No hace falta experiencia.#‘Academia Solista’: clases individuales de canto para profesionales.
Quiero aprender a bailar salsa, pero no tengo pareja.#‘Salsa para todos’: clases en grupo; te buscamos pareja de baile.#‘Ballet Clásico Infantil’: clases para niñas y niños de 4 a 10 años.
Tengo un perro y me gustaría hacer senderismo con otras personas que también tienen perros.#‘Rutas con Patas’: excursiones a la montaña con tu perro cada domingo.#‘Rutas Urbanas’: paseos guiados por el centro histórico. No se admiten animales.
Me interesa la pintura y quiero pintar al aire libre.#‘Pinta el Paisaje’: talleres de pintura en el campo y en la playa.#‘Museo de Arte Moderno’: exposición de pintura abstracta hasta diciembre.
Mis hijos quieren hacer un deporte de equipo los sábados por la mañana.#‘Club Deportivo Infantil’: fútbol y baloncesto para niños, sábados de 10 a 12.#‘Gimnasio Fitness 24’: máquinas y pesas para adultos, abierto día y noche.
Me gustan mucho los juegos de mesa y quiero conocer a gente nueva.#‘La Partida’: café con más de 300 juegos de mesa. Torneos los viernes.#‘Videojuegos Pixel’: tienda de consolas y videojuegos.
Quiero aprender a tocar la guitarra en casa, a mi ritmo.#‘Guitarra en Línea’: vídeos y clases por internet para principiantes.#‘Conservatorio Municipal’: estudios de música clásica con examen de entrada.
"""),
)
