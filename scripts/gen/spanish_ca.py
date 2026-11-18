"""Original content for Area A: Everyday activities (A1-A4). Format: see spanish.py."""

C = {}

C["A1"] = dict(
    theme="la organización del tiempo", tema="El tiempo y los horarios",
    scene=["Estás en {city} con {fr}. Estáis organizando vuestra semana.",
           "Pasas unos días en casa de {fr} en {city}. Habláis de los planes de la semana."],
    ex="""
{fr} dice:#La película empieza {v}.#¿A qué hora empieza la película?#hora
{fr} dice:#Mi clase de baile es {v}.#¿Qué día es la clase de baile?#dia
{fr} pregunta:#¿Quedamos {v} para ir al parque?#¿Qué día quiere quedar {fr}?#dia
{fr} dice:#Nos vamos de vacaciones {v}.#¿Cuándo se va de vacaciones {fr}?#mes
{fr} dice:#Mi estación favorita es {v}.#¿Cuál es la estación favorita de {fr}?#estacion
{fr} dice:#Mi cumpleaños es {v}.#¿Cuándo es el cumpleaños de {fr}?#fecha
{fr} dice:#El autobús sale {v}.#¿A qué hora sale el autobús?#hora
{fr} dice:#¡Mira por la ventana: {v}!#¿Qué tiempo hace?#tiempo
{fr} dice:#El mercado de artesanía solo abre {v}.#¿Qué día abre el mercado?#dia
{fr} dice:#El concierto del colegio es {v}.#¿Cuándo es el concierto?#fecha
""",
    signs=("Horarios y avisos en el centro de la ciudad", """
Abierto 24 horas#Aquí puedes comprar algo a las tres de la madrugada.
Cerrado por vacaciones del 1 al 31 de agosto#En verano tenemos que buscar otra tienda.#verano
Horario de verano: de 8:00 a 14:00#Esta oficina no abre por la tarde en julio.#verano
Domingos y festivos: cerrado#Mañana es domingo, así que no podemos ir.
Último pase: 19:30#Hay que entrar antes de las siete y media de la tarde.
Visitas guiadas cada hora en punto#La próxima visita con guía empieza a las cinco exactamente.
Recogida de basura: lunes, miércoles y viernes#No saques la bolsa el martes.
Hora punta: no se permiten bicicletas en el metro#Entre las ocho y las nueve no puedo llevar la bici en el tren.
Desayunos hasta las 11:30#Todavía podemos desayunar aquí si llegamos a las once.
Abrimos de nuevo el 7 de enero#Después de las fiestas de Navidad, la tienda vuelve a abrir.
"""),
    ann=dict(title="El nuevo horario del centro cultural", desc="un anuncio sobre el horario de un centro cultural", sp="Locutora",
             open="Buenos días. Les informamos del nuevo horario del Centro Cultural de {city}.",
             close="Para más información, visiten nuestra página web. Muchas gracias.",
             facts="""
El centro abre de lunes a sábado {h=a las nueve|a las diez|a las ocho y media|a las once} de la mañana.#Por la mañana, el centro abre:#*h
Los domingos el centro está cerrado, excepto el primer domingo de cada mes.#¿Qué domingo abre el centro?#el primero del mes;todos los domingos;el último del mes;ningún domingo
La biblioteca del centro cierra a mediodía, de dos a cuatro.#La biblioteca está cerrada:#a mediodía;por la mañana;los lunes;por la noche
Las clases de baile empiezan {m=en octubre|en septiembre|en noviembre|en enero}.#Las clases de baile empiezan:#*m
Las clases de pintura son los {d=martes|jueves|miércoles|viernes} por la tarde.#¿Qué día hay clases de pintura?#*d
En verano, el centro cierra más temprano, a las ocho de la tarde.#En verano el centro cierra:#a las ocho de la tarde;a las diez de la noche;a las seis de la tarde;a mediodía
Las entradas para el concierto de Navidad estarán a la venta desde el uno de diciembre.#¿Desde cuándo se pueden comprar las entradas para el concierto?#desde el uno de diciembre;desde el uno de noviembre;desde Navidad;desde hoy
La cafetería del centro abre todos los días, también los domingos.#La cafetería abre:#todos los días;solo por la mañana;de lunes a viernes;solo los domingos
"""),
    facts="""
Me levanto {h=a las siete|a las seis y media|a las siete menos cuarto|a las siete y cuarto} porque las clases empiezan temprano.#¿A qué hora te levantas los días de clase?#¿A qué hora se levanta {N} los días de clase?#{h}#Refuse me levanto#*h#Se levanta pronto los días de colegio.#Los días de colegio se levanta a mediodía.#1
Los lunes tengo clase de piano después del instituto, así que llego a casa muy tarde.#¿Qué haces los lunes por la tarde?#¿Qué hace {N} los lunes después del instituto?#(Tiene/Va a) clase de piano#Refuse tengo clase de piano#Tiene clase de piano.;Hace los deberes en la biblioteca.;Entrena al fútbol.;Trabaja en una tienda.#Los lunes estudia música.#Los lunes vuelve pronto a casa.#1
Mi día favorito es el viernes porque por la tarde no tenemos clases.#¿Cuál es tu día favorito?#¿Por qué le gusta a {N} el viernes?#(Porque) no tiene(n) clases por la tarde#Refuse no tenemos clases#No tiene clases por la tarde.;Sale con sus amigos.;Hay partido de fútbol.;Come en un restaurante.#Prefiere el viernes porque la tarde es libre.#Odia los viernes.#1
En invierno los días son muy cortos y a las cinco y media ya es de noche.#¿Qué piensas del invierno?#¿Qué pasa a las cinco y media en invierno?#(Ya) es de noche / está oscuro#Refuse es invierno tc#Ya es de noche.;Empieza a nevar.;Cierran las tiendas.;Termina el colegio.#En invierno oscurece pronto.#En invierno hay luz hasta muy tarde.#2#temperate
Mi cumpleaños es {fe=el tres de mayo|el veinte de febrero|el doce de octubre|el uno de noviembre}, y este año cae en sábado.#¿Cuándo es tu cumpleaños?#¿Cuándo es el cumpleaños de {N}?#{fe}#Accept the date in figures#*fe#Este año su cumpleaños es en fin de semana.#Este año su cumpleaños es un lunes.#1
Hace dos años que aprendo a tocar la guitarra y practico media hora cada día.#¿Cuánto tiempo practicas la guitarra?#¿Cuánto tiempo practica {N} la guitarra cada día?#Media hora / treinta minutos#Refuse dos años#media hora;una hora;dos horas;quince minutos#Toca la guitarra todos los días.#Ya no toca la guitarra.#2
Los fines de semana me acuesto más tarde, a eso de la medianoche, porque veo películas con mi hermano.#¿A qué hora te acuestas los fines de semana?#¿Por qué se acuesta tarde {N} los fines de semana?#(Porque) ve películas (con su hermano)#Refuse veo películas#Ve películas con su hermano.;Hace los deberes.;Juega en línea con amigos.;Trabaja en un restaurante.#El sábado y el domingo se va a la cama tarde.#Los fines de semana se acuesta muy pronto.#1
El verano pasado no tenía horario y me levantaba cuando quería, pero al final me aburría un poco.#¿Cómo eran tus días el verano pasado?#¿Cómo se sentía {N} al final del verano pasado?#(Un poco) aburrid<o|a> / se aburría#Refuse me aburría#Se aburría un poco.;Estaba muy cansad<o|a>.;Estaba enferm<o|a>.;Tenía demasiado trabajo.#Durante el verano no seguía un horario fijo.#El verano pasado tenía un horario muy estricto.#2
Mi madre dice que siempre llego tarde, pero yo creo que solo llego cinco minutos tarde de vez en cuando.#¿Eres puntual?#¿Qué opina {N} de su puntualidad?#(Solo) llega tarde de vez en cuando / (solo) cinco minutos tarde#Refuse siempre llega tarde#Solo llega tarde a veces.;Siempre llega tarde.;Nunca llega tarde.;Llega una hora tarde.#No está de acuerdo con su madre.#Piensa lo mismo que su madre.#3
El próximo mes empiezan los exámenes, así que voy a estudiar dos horas cada tarde.#¿Qué planes tienes para el próximo mes?#¿Qué va a hacer {N} cada tarde el próximo mes?#Estudiar (dos horas)#Refuse voy a estudiar#Va a estudiar.;Va a trabajar.;Va a nadar.;Va a descansar.#Pronto tendrá exámenes.#Ya ha terminado los exámenes.#2
Mi estación preferida es la primavera porque hace buen tiempo y los días son más largos.#¿Cuál es tu estación preferida?#¿Por qué prefiere {N} la primavera?#(Porque) hace buen tiempo / los días son más largos#Refuse es la primavera tc#Hace buen tiempo.;Hay vacaciones largas.;Puede esquiar.;Es su cumpleaños.#Le gustan los días largos de la primavera.#No le gusta nada la primavera.#1
Antes iba al instituto en autobús y tardaba cuarenta minutos, pero ahora voy en bicicleta y solo tardo quince.#¿Cuánto tiempo tardas en llegar al instituto?#¿Cuánto tarda {N} ahora en llegar al instituto?#Quince minutos#Refuse cuarenta minutos#quince minutos;cuarenta minutos;media hora;una hora#Ahora llega al instituto más rápido que antes.#Ahora tarda más que antes en llegar al instituto.#2
Los domingos comemos todos juntos en casa de mis abuelos a las dos y media.#¿Qué haces los domingos?#¿Dónde come {N} los domingos?#En casa de sus abuelos#Refuse en casa de mis abuelos#en casa de sus abuelos;en un restaurante;en casa de un amigo;en el instituto#Los domingos come con la familia.#Los domingos come sol<o|a>.#1
Nunca tengo tiempo para leer durante la semana, por eso leo los sábados por la mañana en la cama.#¿Cuándo lees?#¿Cuándo lee {N}?#(Los) sábados por la mañana#Refuse durante la semana#los sábados por la mañana;cada noche;en el autobús;los domingos por la tarde#Lee el fin de semana.#Lee todos los días de la semana.#2
En el futuro me gustaría tener un trabajo con un horario flexible para poder organizar mi tiempo.#¿Qué tipo de horario te gustaría tener en el futuro?#¿Qué tipo de horario quiere tener {N} en el futuro?#(Un horario) flexible#Refuse para organizar su tiempo tc#un horario flexible;un horario de noche;un horario muy largo;un horario de mañana#Quiere decidir cuándo trabaja.#Prefiere un horario fijo.#3
Ayer perdí el tren de las ocho y llegué tarde a la clase de inglés. ¡Qué vergüenza!#¿Te pasó algo ayer?#¿Por qué llegó tarde {N} ayer?#(Porque) perdió el tren (de las ocho)#Refuse perdí el tren#Perdió el tren.;Se levantó tarde.;Había mucho tráfico.;Estaba enferm<o|a>.#Ayer tuvo un problema con el transporte.#Ayer llegó pronto a clase.#2
Cuando termine el curso, en junio, pienso dormir hasta las diez todos los días.#¿Qué vas a hacer cuando termine el curso?#¿Qué piensa hacer {N} cuando termine el curso?#Dormir hasta las diez / levantarse tarde#Refuse dormir tc#Dormir hasta tarde.;Trabajar por las mañanas.;Viajar al extranjero.;Estudiar más horas.#Quiere levantarse tarde en las vacaciones.#Piensa levantarse temprano en junio.#3#north
""",
)

C["A2"] = dict(
    theme="la comida y la alimentación diaria", tema="La comida y la bebida",
    scene=["Estás en el mercado de {city} con {fr}. Vais a comprar comida para una cena.",
           "Estás en casa de {fr} en {city}. Vais a preparar la comida juntos."],
    ex="""
{fr} dice:#Tengo que comprar {v} para el postre.#¿Qué tiene que comprar {fr}?#fruta
{fr} dice:#Para la ensalada necesito {v}.#¿Qué necesita {fr}?#verdura
{fr} pregunta:#¿Quieres {v}?#¿Qué te ofrece {fr}?#bebida
{fr} dice:#Esta noche cenamos {v}.#¿Qué van a cenar?#plato
{fr} dice:#De postre hay {v}.#¿Qué hay de postre?#postre
{fr} dice:#Mi comida favorita del día es {v}.#¿Qué comida prefiere {fr}?#comida_hora
{fr} dice:#Las {v} están muy baratas hoy.#¿Qué fruta está barata?#fruta
{fr} dice:#No me gustan nada {v}.#¿Qué no le gusta a {fr}?#verdura
{fr} dice:#Para merendar, prefiero {v}.#¿Qué prefiere tomar {fr}?#bebida
"""
.replace("Las {v} están muy baratas hoy.#¿Qué fruta está barata?", "Hoy compramos {v}, que están baratas.#¿Qué compran hoy?")
.replace("que están baratas", "que hoy están de oferta").replace("¿Qué compran hoy?", "¿Qué fruta compran hoy?"),
    signs=("En un supermercado", """
Caja rápida: máximo 10 productos#Solo llevo tres cosas, así que pago aquí.
Productos sin gluten#Mi hermano no puede comer pan normal: miremos en esta sección.#pan
Fruta y verdura: pésela usted mismo#Antes de pagar las manzanas, tengo que ponerlas en la báscula.
Panadería: pan recién hecho#Necesitamos una barra para los bocadillos.#pan
Congelados#Busco helado y pescado que estén muy fríos.
Oferta: dos por el precio de uno#Si compras un paquete, te dan otro gratis.
Prohibido entrar con perros#El perro tiene que esperar fuera.
Bebidas frías#Hace calor y quiero un refresco que esté fresco.
Productos ecológicos#Quiero comprar verdura cultivada sin productos químicos.
Carnicería: coja su número#Para comprar el pollo, primero tienes que esperar tu turno.
"""),
    ann=dict(title="Un mercado de comida tradicional", desc="un anuncio en un mercado de comida", sp="Guía",
             open="¡Bienvenidos al Mercado Central de {city}! Les explico cómo funciona el mercado.",
             close="Esperamos que disfruten de su visita. ¡Buen provecho!",
             facts="""
El mercado tiene más de {n=cien|doscientos|cincuenta|trescientos} puestos de comida.#¿Cuántos puestos tiene el mercado?#más de {n};
El mercado se construyó hace más de un siglo, en mil novecientos diez.#El mercado se construyó en:#1910;1810;1990;2010
En la planta baja se vende fruta, verdura y pescado fresco.#En la planta baja se vende:#fruta, verdura y pescado;ropa y zapatos;carne y queso;flores y plantas
Lo que más les gusta a los turistas son los zumos naturales.#A los turistas les encantan:#los zumos naturales;los pasteles;los helados;las patatas fritas
Arriba hay una zona de restaurantes donde se puede probar comida de toda la región.#En el piso de arriba hay:#restaurantes;un aparcamiento;una biblioteca;tiendas de ropa
Está prohibido tocar la fruta sin guantes.#En el mercado está prohibido:#tocar la fruta sin guantes;hacer fotos;comer en los pasillos;entrar con niños
Los sábados hay clases de cocina gratuitas a las doce.#Las clases de cocina son:#los sábados a las doce;los domingos a las doce;los sábados a las diez;todos los días
El mercado cierra a las tres de la tarde.#El mercado cierra:#a las tres de la tarde;a las nueve de la noche;a mediodía;a las cinco de la tarde
"""),
    facts="""
Normalmente desayuno muy poco: solo un café con leche y una tostada.#¿Qué desayunas normalmente?#¿Qué desayuna {N} normalmente?#(Un) café con leche y (una) tostada#Refuse desayuno café tc#un café con leche y una tostada;cereales con fruta;huevos y zumo;nada#Toma un desayuno ligero.#Desayuna muchísimo.#1
A mediodía como en el comedor del instituto, pero la comida no me gusta porque siempre está fría.#¿Dónde comes a mediodía?#¿Por qué no le gusta a {N} la comida del comedor?#(Porque) (siempre) está fría#Refuse no me gusta#Porque siempre está fría.;Porque es cara.;Porque no hay postre.;Porque hay poca comida.#Critica la temperatura de la comida del instituto.#Le encanta la comida del comedor.#1
Mi plato favorito es la paella de mi abuela, que la prepara los domingos.#¿Cuál es tu plato favorito?#¿Cuándo prepara la abuela de {N} la paella?#(Los) domingos#Refuse el domingo pasado#los domingos;los sábados;en Navidad;cada día#Su abuela cocina su plato preferido.#No le gusta la paella.#1#-veg -nofish
Desde hace un año soy vegetarian<o|a> porque quiero proteger a los animales.#¿Comes carne?#¿Por qué es vegetarian<o|a> {N}?#(Para) proteger a los animales#Refuse quiero proteger tc#Para proteger a los animales.;Por su salud.;Porque la carne es cara.;Porque su familia lo es.#No come carne por los animales.#Come carne todos los días.#2#+veg
Mi madre dice que bebo demasiados refrescos, así que ahora intento beber más agua.#¿Qué bebes normalmente?#¿Qué intenta hacer {N} ahora?#Beber más agua#Refuse beber refrescos#beber más agua;beber más refrescos;comer más fruta;cocinar más#Quiere reducir los refrescos.#Ahora bebe más refrescos que antes.#2
Lo que más odio es el pescado, ¡no lo como nunca!#¿Hay alguna comida que no te guste?#¿Qué comida odia {N}?#(El) pescado#Refuse pescado no tc#el pescado;la carne;la verdura;el queso#Detesta el pescado.#Come pescado a menudo.#1#+nofish
El fin de semana pasado hice una tarta de chocolate para mi hermana, pero se me quemó un poco.#¿Cocinaste algo el fin de semana pasado?#¿Qué problema tuvo {N} con la tarta?#Se (le) quemó (un poco)#Refuse se me quemó#Se quemó un poco.;No tenía chocolate.;A su hermana no le gustó.;Se cayó al suelo.#La tarta no le salió perfecta.#La tarta le salió perfecta.#2
En mi casa cenamos tarde, a las nueve y media, como muchas familias españolas.#¿A qué hora cenáis en tu casa?#¿A qué hora cena la familia de {N}?#A las nueve y media#Refuse a las nueve tc#a las nueve y media;a las siete;a las ocho y media;a las diez y media#Su familia cena bastante tarde.#Su familia cena muy pronto.#1#spain
Creo que es importante comer cinco piezas de fruta al día, pero yo solo como dos.#¿Comes mucha fruta?#¿Cuántas piezas de fruta come {N} al día?#Dos#Refuse cinco#dos;cinco;una;ninguna#Come menos fruta de la recomendada.#Come más fruta de la recomendada.#2
Cuando era pequeñ<o|a> no comía verduras, pero ahora me encantan las espinacas.#¿Siempre te han gustado las verduras?#¿Qué verdura le encanta a {N} ahora?#(Las) espinacas#Refuse no comía verduras#las espinacas;las zanahorias;los guisantes;las patatas#Sus gustos han cambiado con los años.#De niñ<o|a> le encantaban las verduras.#2
Los sábados voy al mercado con mi padre porque allí la fruta es más fresca que en el supermercado.#¿Dónde compráis la fruta?#¿Por qué va {N} al mercado con su padre?#(Porque) la fruta es más fresca#Refuse la fruta es más barata#Porque la fruta es más fresca.;Porque es más barato.;Porque está cerca.;Porque abre los domingos.#Prefiere la calidad de la fruta del mercado.#Compra la fruta en el supermercado.#2
La comida rápida es muy práctica, pero tiene demasiada grasa y sal.#¿Qué piensas de la comida rápida?#¿Qué es lo malo de la comida rápida, según {N}?#(Tiene demasiada) grasa y sal#Refuse es práctica#Tiene demasiada grasa y sal.;Es demasiado cara.;Hay que esperar mucho.;Es aburrida.#Ve un inconveniente para la salud en la comida rápida.#Cree que la comida rápida es muy sana.#3
Mi hermano mayor trabaja de cocinero en un hotel y me ha enseñado a hacer tortilla de patatas.#¿Quién te enseñó a cocinar?#¿Qué le ha enseñado a {N} su hermano?#(A hacer) (una) tortilla (de patatas)#Refuse me ha enseñado#a hacer tortilla de patatas;a hacer pan;a hacer pizza;a hacer paella#Ha aprendido a cocinar con un familiar.#Ha aprendido a cocinar en un curso.#2
El año que viene quiero aprender a cocinar platos de otros países, sobre todo comida japonesa.#¿Qué quieres aprender a cocinar?#¿Qué tipo de comida quiere aprender a cocinar {N}?#(Comida/Platos de otros países) japonesa/de Japón#Refuse de otros países tc#comida japonesa;comida italiana;comida mexicana;postres franceses#Le interesa la cocina internacional.#Solo quiere cocinar platos de su país.#2
Si pudiera, comería pizza todos los días, aunque sé que no es muy sano.#¿Cuál es tu comida preferida?#¿Qué sabe {N} sobre la pizza?#(Que) no es (muy) sana#Refuse comería pizza todos los días#Que no es muy sana.;Que es barata.;Que engorda poco.;Que es italiana.#Reconoce que la pizza no es buena para la salud.#Cree que la pizza es muy sana.#3
Ayer cenamos en casa de mis tíos y probé un plato peruano que se llama ceviche.#¿Qué cenaste ayer?#¿Dónde cenó {N} ayer?#(En) casa de sus tíos#Refuse en casa de mis tíos#en casa de sus tíos;en un restaurante peruano;en su casa;en casa de un amigo#Ayer probó un plato nuevo.#Ayer cenó en casa sol<o|a>.#2#-veg -nofish
Para estar san<o|a>, intento no comer entre horas y tomo fruta en lugar de galletas.#¿Qué haces para comer bien?#¿Qué come {N} en lugar de galletas?#Fruta#Refuse galletas#fruta;yogur;chocolate;pan#Cuida lo que come entre comidas.#Come galletas a todas horas.#2
""",
    tq="""
p#¿Qué comes normalmente para el desayuno?#¿Qué desayunas los días de clase?#Breakfast items, e.g. *Desayuno cereales y un zumo.*
p#¿Qué plato te gusta más?#¿Cuál es tu plato preferido?#Names a dish/food with brief detail, e.g. *Me encanta la pasta.*
p#¿Quién cocina en tu casa?#¿Quién prepara la comida en tu familia?#Names who cooks and when.
o#¿Qué opinas de la comida rápida? ¿Por qué?#¿Te gusta la comida rápida? ¿Por qué (no)?#Opinion + reason, e.g. *es práctica pero tiene mucha grasa.*
o#¿Crees que comes de forma sana? ¿Por qué (no)?#¿Tu dieta es sana? ¿Por qué (no)?#Opinion on own diet with justification (fruit, sugar, exercise).
pa#¿Qué comiste ayer?#¿Qué cenaste anoche?#Past tense: foods eaten, e.g. *Ayer comí pollo con arroz.*
pa#Háblame de la última vez que cocinaste algo.#¿Qué cocinaste la última vez? ¿Cómo fue?#Past narrative: what was cooked, for whom, outcome.
f#¿Qué vas a comer este fin de semana?#¿Qué piensas comer el sábado?#Future: planned meal, e.g. *Voy a comer en casa de mis abuelos.*
c#En el futuro, ¿te gustaría aprender a cocinar mejor? ¿Por qué (no)?#¿Te gustaría hacer un curso de cocina? ¿Por qué (no)?#Conditional + reason, e.g. *Me gustaría aprender porque…*
d#Describe una comida típica de tu país.#¿Cómo es una comida típica de tu país?#Description of a typical dish/meal and when it is eaten.
c#Si fueras a un país hispano, ¿qué plato probarías? ¿Por qué?#¿Qué comida de otro país te gustaría probar? ¿Por qué?#Conditional: dish to try + reason.
f#¿Cómo vas a mejorar tu dieta en el futuro?#¿Qué cambios harás en tu dieta?#Future: one or more changes, e.g. *Voy a comer más verdura.*
""",
    ads=("Cursos y tiendas de alimentación", """
Quiero aprender a hacer pan en casa, pero solo tengo tiempo los fines de semana.#Panadería ‘La Espiga’: talleres para hacer pan casero. Grupos pequeños los sábados y domingos por la mañana.#Panadería ‘El Horno’: pan recién hecho todos los días. Abierto de lunes a viernes de 7:00 a 14:00. No ofrecemos cursos.
Mi familia es vegetariana y buscamos un restaurante con muchas opciones sin carne para celebrar un cumpleaños.#Restaurante ‘Huerta Verde’: cocina cien por cien vegetal. Menús especiales para fiestas y grupos.#Asador ‘El Toro’: las mejores carnes a la brasa. Salones para celebraciones familiares.
Necesito comprar fruta y verdura de buena calidad, pero no puedo salir de casa porque trabajo todo el día.#‘Frutas a domicilio’: pide en nuestra web y te llevamos la fruta y verdura más fresca a tu puerta.#Frutería ‘Marisol’: fruta fresca de la región. Ven a visitarnos en la calle Mayor, de 9:00 a 20:00.
Soy deportista y quiero aprender a preparar comidas sanas con muchas proteínas.#Curso ‘Come para ganar’: nutrición y recetas para personas que hacen deporte. Con una nutricionista.#Curso ‘Dulces de la abuela’: aprende a preparar tartas y galletas tradicionales.
Mi hijo de ocho años quiere aprender a cocinar, pero tiene que ser una actividad para niños.#‘Pequeños chefs’: clases de cocina divertidas para niños de 6 a 12 años. Los padres pueden esperar en la cafetería.#Escuela de cocina ‘Gourmet’: cursos profesionales para adultos mayores de 18 años.
Voy a dar una fiesta en casa y necesito alguien que prepare la comida para cincuenta personas.#‘Catering Sabores’: preparamos la comida para tu fiesta en casa, desde 20 hasta 200 invitados.#‘Catering Íntimo’: cenas especiales en tu casa para grupos de 2 a 10 personas.
Me encanta la comida mexicana y quiero comprar ingredientes para cocinarla en casa.#‘Tienda Maya’: productos mexicanos de importación: chiles, tortillas de maíz, salsas y mucho más.#‘Taquería Maya’: auténticos tacos mexicanos. Mesas en la terraza. No vendemos productos para llevar.
"""),
)

C["A3"] = dict(
    theme="la salud y el cuidado del cuerpo", tema="La salud y el cuerpo",
    scene=["Estás de excursión en la montaña cerca de {city} con {fr}. {fr} no se encuentra bien.",
           "Estás en {city} con {fr}. Hoy {fr} tiene que ir al médico."],
    ex="""
{fr} dice:#Me duele mucho {v}.#¿Qué le duele a {fr}?#cuerpo
{fr} dice:#Me he hecho daño en {v}.#¿Dónde se ha hecho daño {fr}?#cuerpo
{fr} dice:#El médico me ha dado {v}.#¿Qué le ha dado el médico?#remedio
{fr} dice:#Tengo que ir {v}.#¿Adónde tiene que ir {fr}?#salud_lugar
{fr} pregunta:#¿Tienes {v}?#¿Qué necesita {fr}?#remedio
{fr} dice:#Desde ayer me duele {v}.#¿Qué le duele a {fr} desde ayer?#cuerpo
{fr} dice:#Para estar en forma, me gusta {v}.#¿Qué hace {fr} para estar en forma?#actividad
{fr} dice:#Hoy no puedo ir porque tengo cita {v}.#¿Adónde va {fr} hoy?#salud_lugar
{fr} dice:#Ahora estoy mejor. ¿Vamos a tomar {v}?#¿Qué quiere tomar {fr}?#bebida
""".replace("tengo cita {v}", "tengo que ir {v} a las cinco"),
    signs=("En el centro de salud", """
Urgencias#Mi amigo se ha roto el brazo: hay que llevarlo aquí ahora mismo.
Sala de espera#Tienes que sentarte aquí hasta que te llamen.
Farmacia de guardia#Son las dos de la mañana y necesito medicinas.
Pida cita en recepción#Para ver al médico, primero hablas con la persona del mostrador.
Prohibido usar el móvil#Apaga el teléfono, por favor.#quiet
Vacunación: martes y jueves#Si quieres ponerte la vacuna, ven a mitad de semana.
Dentista: primera planta#Me duele una muela: tengo que subir las escaleras.#stairs
Lávese las manos#Antes de entrar, usa el jabón.
Silencio, por favor#Aquí no se puede hablar en voz alta.#quiet
Ascensor solo para pacientes#Si estás bien, tienes que usar las escaleras.#stairs
"""),
    ann=dict(title="Una semana de la salud en el instituto", desc="un anuncio sobre una semana de la salud en un instituto", sp="Directora",
             open="Buenos días a todos. La semana que viene celebramos la Semana de la Salud en el instituto.",
             close="Os esperamos a todos. ¡Cuidaos mucho!",
             facts="""
El lunes una enfermera va a hablar sobre la importancia de dormir bien.#El lunes la enfermera va a hablar sobre:#el sueño;la comida;el deporte;los dientes
El martes habrá fruta gratis en el patio durante el recreo.#El martes en el recreo habrá:#fruta gratis;bocadillos;un partido;música
El miércoles vamos a correr {k=cinco|tres|diez|ocho} kilómetros por el parque.#El miércoles los alumnos van a correr:#{k} kilómetros;
El jueves podéis aprender primeros auxilios con la Cruz Roja.#El jueves los alumnos pueden aprender:#primeros auxilios;a cocinar;a nadar;yoga
Durante toda la semana, la cafetería no venderá refrescos con azúcar.#Durante la semana la cafetería no venderá:#refrescos con azúcar;agua;fruta;bocadillos
El viernes hay una clase de yoga en el gimnasio para relajarse antes de los exámenes.#La clase de yoga es para:#relajarse;ganar una medalla;perder peso;conocer gente
Para participar en la carrera hay que traer zapatillas de deporte y una botella de agua.#Para la carrera hay que traer:#zapatillas y agua;una bicicleta;un bocadillo;un certificado médico
"""),
    facts="""
Hago deporte tres veces a la semana: los martes juego al baloncesto y los fines de semana corro en el parque.#¿Haces mucho deporte?#¿Cuántas veces a la semana hace deporte {N}?#Tres (veces)#Refuse dos veces#tres veces;una vez;todos los días;nunca#Hace ejercicio con regularidad.#No practica ningún deporte.#1#-injured
Duermo solo seis horas porque me quedo despiert<o|a> mirando el móvil.#¿Cuántas horas duermes?#¿Por qué duerme poco {N}?#(Porque) mira el móvil (por la noche)#Refuse miro el móvil#Porque mira el móvil.;Porque estudia mucho.;Porque hay ruido en la calle.;Porque trabaja por la noche.#Usa el teléfono antes de dormir.#Duerme más de diez horas.#1
El mes pasado me rompí la pierna jugando al fútbol y tuve que estar seis semanas sin hacer deporte.#¿Has tenido algún accidente?#¿Qué le pasó a {N} el mes pasado?#Se rompió la pierna#Refuse me rompí la pierna; Refuse se rompe la pierna#Se rompió la pierna.;Se cortó la mano.;Tuvo gripe.;Se cayó de la bici.#Se hizo daño practicando deporte.#El mes pasado ganó un partido de tenis.#2#+injured
Cuando estoy estresad<o|a> por los exámenes, salgo a caminar con mi perro.#¿Qué haces cuando estás estresad<o|a>?#¿Qué hace {N} cuando está estresad<o|a>?#(Sale a) caminar/pasear con su perro#Refuse salgo a caminar#Sale a pasear con su perro.;Come chocolate.;Escucha música.;Duerme la siesta.#Pasea con su mascota para relajarse.#Cuando está nervios<o|a> se queda en casa.#2
Nunca fumaría porque mi abuelo estuvo muy enfermo por culpa del tabaco.#¿Qué piensas del tabaco?#¿Por qué no fumaría nunca {N}?#(Porque) su abuelo estuvo (muy) enfermo (por el tabaco)#Refuse mi abuelo#Porque su abuelo enfermó por el tabaco.;Porque es caro.;Porque huele mal.;Porque sus amigos no fuman.#Una experiencia familiar le ha convencido de no fumar.#Fuma de vez en cuando.#3
Bebo dos litros de agua al día, sobre todo cuando hace calor.#¿Bebes mucha agua?#¿Cuánta agua bebe {N} al día?#Dos litros#Refuse un litro#dos litros;un litro;medio litro;tres litros#Toma mucha agua cada día.#Casi nunca bebe agua.#1
Ayer fui al médico porque tenía fiebre y me dolía la garganta.#¿Por qué fuiste al médico ayer?#¿Qué síntomas tenía {N} ayer? (Menciona uno.)#Fiebre / le dolía la garganta#Refuse me dolía la garganta#Tenía fiebre.;Le dolía la espalda.;Tenía tos.;Le dolían los oídos.#Ayer estaba enferm<o|a>.#Ayer se encontraba perfectamente.#2
El médico me dijo que me quedara en casa dos días y que bebiera mucho líquido.#¿Qué te dijo el médico?#¿Cuánto tiempo tiene que quedarse en casa {N}?#Dos días#Refuse una semana#dos días;una semana;un día;tres días#Tiene que descansar en casa unos días.#Puede ir al instituto mañana.#3
Me encanta el yoga porque me ayuda a relajarme y a dormir mejor.#¿Qué te gusta hacer para relajarte?#¿Para qué le sirve el yoga a {N}? (Menciona una cosa.)#(A/Para) relajarse / dormir mejor#Refuse para relajarme#Para relajarse.;Para perder peso.;Para conocer gente.;Para ganar competiciones.#Practica yoga para descansar mejor.#Odia el yoga.#2
De pequeñ<o|a> tenía asma y no podía correr mucho, pero ahora estoy muy bien.#¿Tuviste problemas de salud de pequeñ<o|a>?#¿Qué problema tenía {N} de pequeñ<o|a>?#(Tenía) asma / no podía correr (mucho)#Refuse tengo asma#Tenía asma.;Llevaba gafas.;Se rompió un brazo.;Tenía alergia a la leche.#Ahora su salud es mejor que antes.#Ahora tiene más problemas de salud.#2
Mi instituto ha prohibido la comida basura en la cafetería y creo que es una buena idea.#¿Qué hace tu instituto por la salud de los alumnos?#¿Qué opina {N} de la decisión del instituto?#Es una buena idea / está de acuerdo#Refuse prohibido tc#Le parece una buena idea.;Le parece injusta.;No le importa.;Le parece cara.#Está de acuerdo con su instituto.#Está en contra de la decisión.#3
Para mí, la salud mental es tan importante como la salud física.#¿Qué es importante para estar san<o|a>?#¿Qué piensa {N} de la salud mental?#Es tan importante como la (salud) física#Refuse es importante tc#Es tan importante como la física.;Es menos importante.;Es más importante.;No es importante.#Da el mismo valor a la mente que al cuerpo.#Piensa que solo importa la salud física.#3
El verano que viene voy a hacer un curso de socorrista para trabajar en la piscina.#¿Qué vas a hacer el verano que viene?#¿Por qué va a hacer {N} un curso de socorrista?#Para trabajar en la piscina#Refuse voy a trabajar#Para trabajar en la piscina.;Para aprender a nadar.;Porque es obligatorio.;Para ayudar a su madre.#Quiere un trabajo de verano en la piscina.#Ya trabaja de socorrista.#2
En invierno siempre me resfrío, así que tomo mucha fruta con vitamina C.#¿Te pones enferm<o|a> a menudo?#¿Qué hace {N} para no resfriarse?#Toma (mucha) fruta (con vitamina C)#Refuse tomo fruta#Toma fruta con vitamina C.;Lleva bufanda.;No sale de casa.;Toma pastillas.#Intenta evitar los resfriados con fruta.#En invierno nunca se pone enferm<o|a>.#2
Mi hermana es enfermera en un hospital y trabaja de noche, así que duerme por la mañana.#¿Alguien de tu familia trabaja en salud?#¿Cuándo duerme la hermana de {N}?#Por la mañana#Refuse por la noche#por la mañana;por la noche;por la tarde;los fines de semana#Su hermana tiene un horario de noche.#Su hermana trabaja por la mañana.#1
Si tuviera más tiempo, iría al gimnasio todos los días.#¿Vas al gimnasio?#¿Qué haría {N} si tuviera más tiempo?#Iría al gimnasio (todos los días)##Iría al gimnasio.;Dormiría más.;Cocinaría más.;Viajaría.#Le falta tiempo para hacer ejercicio.#Va al gimnasio todos los días.#3#-injured
""",
    tq="""
p#¿Qué haces para estar en forma?#¿Haces deporte para estar san<o|a>?#Exercise/activities in the present, e.g. *Corro dos veces por semana.*
p#¿Cuántas horas duermes normalmente?#¿A qué hora te acuestas normalmente?#Sleep habits, e.g. *Duermo ocho horas.*
p#¿Qué haces cuando estás enferm<o|a>?#¿Qué haces si te duele la cabeza?#Present: remedies/actions, e.g. *Me quedo en la cama.*
o#¿Crees que llevas una vida sana? ¿Por qué (no)?#¿Tu estilo de vida es sano? ¿Por qué (no)?#Opinion + reason about own lifestyle.
o#¿Es importante dormir bien? ¿Por qué?#¿Por qué es bueno dormir bien?#Opinion + reason (concentration, energy, mood).
pa#¿Cuándo fue la última vez que estuviste enferm<o|a>? [PAUSA] ¿Qué te pasó?#La última vez que te sentiste mal, ¿qué hiciste?#Past: illness/symptoms and what happened.
pa#¿Qué hiciste la semana pasada para estar en forma?#¿Qué deporte hiciste la semana pasada?#Past tense activity, e.g. *Fui a nadar.*
f#¿Qué vas a hacer para estar más san<o|a> en el futuro?#¿Qué cambios vas a hacer en tu vida?#Future intentions, e.g. *Voy a dormir más.*
c#¿Te gustaría trabajar en un hospital? ¿Por qué (no)?#En el futuro, ¿trabajarías como médico o enfermero? ¿Por qué (no)?#Conditional + reason.
d#Describe un día sano ideal.#¿Cómo sería un día sano perfecto para ti?#Description of food, exercise, sleep in a healthy day.
d#Explica qué hacen los jóvenes de tu país para relajarse.#¿Cómo se relajan los jóvenes en tu país?#Description of ways young people relax; opinion.
""",
    ads=("Salud y bienestar", """
Me duele mucho la espalda por trabajar con el ordenador y necesito un tratamiento con un profesional.#Clínica ‘Espalda Sana’: fisioterapeutas especializados en dolores de espalda y cuello. Cita previa por teléfono.#Clínica ‘Sonrisa’: dentistas para toda la familia. Revisiones gratuitas en mayo.
Quiero dejar de fumar pero no sé cómo hacerlo solo.#Programa ‘Respira’: grupos de apoyo para dejar el tabaco, con médicos y psicólogos. Gratis.#Tienda ‘Aire Puro’: aparatos para limpiar el aire de tu casa.
Estoy muy estresada por el trabajo y busco una actividad tranquila por las tardes.#Centro ‘Calma’: clases de meditación y yoga suave de 19:00 a 21:00.#Gimnasio ‘Power’: entrenamientos de alta intensidad con música fuerte, de 7:00 a 9:00.
Tengo setenta años y quiero hacer ejercicio con personas de mi edad.#‘Activos siempre’: gimnasia suave y paseos en grupo para mayores de 65 años.#‘Jóvenes en forma’: deporte en grupo para chicos y chicas de 14 a 18 años.
Me he roto el brazo y necesito un médico, pero es domingo por la noche.#Hospital San Rafael: urgencias abiertas 24 horas, todos los días del año.#Centro de salud del barrio: de lunes a viernes de 8:00 a 15:00.
Quiero aprender a nadar porque nunca he aprendido y ya tengo treinta años.#Piscina municipal: cursos de natación para adultos principiantes. Grupos de máximo seis personas.#Club ‘Delfines’: entrenamiento para nadadores de competición. Nivel avanzado.
Mi hijo necesita gafas nuevas y queremos un sitio con buenos precios.#Óptica ‘Ver bien’: gafas para niños desde 30 euros. Revisión de la vista gratis.#Óptica ‘Lujo’: gafas de sol de marcas exclusivas.
"""),
)

C["A4"] = dict(
    theme="el transporte y los viajes", tema="Los viajes y el transporte",
    scene=["Estás en la estación de {city} con {fr}. Vais a hacer un viaje.",
           "Estás en {city} con {fr}. Queréis visitar la ciudad."],
    ex="""
{fr} dice:#Prefiero ir {v}.#¿Cómo prefiere ir {fr}?#transporte
{fr} dice:#Quiero un billete, pero solo {v}.#¿Qué billete quiere {fr}?#billete
{fr} dice:#Primero tenemos que ir a {v}.#¿Adónde tienen que ir primero?#lugar_ciudad
{fr} dice:#Para llegar al museo, sigue {v}.#¿Por dónde hay que ir?#direccion
{fr} dice:#El tren sale {v}.#¿A qué hora sale el tren?#hora
{fr} dice:#Hoy voy al instituto {v}.#¿Cómo va {fr} al instituto hoy?#transporte
{fr} pregunta:#¿Está lejos {v}?#¿Qué lugar busca {fr}?#lugar_ciudad
{fr} dice:#La parada está {v}.#¿Dónde está la parada?#direccion
{fr} dice:#He olvidado {v} en el tren.#¿Qué ha olvidado {fr}?#equipaje
""".replace("Quiero un billete, pero solo {v}.", "Quiero comprar {v}.").replace("Primero tenemos que ir a {v}.#¿Adónde tienen que ir primero?", "Mi lugar favorito de la ciudad es {v}.#¿Cuál es el lugar favorito de {fr}?").replace("sigue {v}.", "gira {v}.").replace("Para llegar al museo, gira todo recto", "x"),
    signs=("En la estación de tren", """
Salidas#Quiero saber a qué hora se va mi tren.
Llegadas#Mi abuela viene en tren: miremos a qué hora llega.
Taquilla#Aquí compramos los billetes.
Consigna#Podemos dejar las maletas aquí y visitar la ciudad.
Objetos perdidos#He perdido mi mochila en el tren.
Andén 3: no cruzar las vías#Es peligroso pasar por las vías.
Prohibido fumar#Aquí no se puede fumar.
Validar el billete antes de subir#Antes de entrar en el tren, hay que pasar el billete por la máquina.
Aseos#Necesito ir al servicio.
Parada de taxis#Llevamos mucho equipaje; vamos al hotel en coche.
Salida de emergencia#Si hay un incendio, salimos por esta puerta.
"""),
    ann=dict(title="Información para viajeros", desc="un anuncio en una estación de autobuses", sp="Locutor",
             open="Atención, señores pasajeros. Esta es la información del día en la estación de autobuses de {city}.",
             close="Gracias por viajar con nosotros. Les deseamos un buen viaje.",
             facts="""
El autobús a la playa sale hoy del andén {a=cuatro|dos|seis|ocho}.#El autobús a la playa sale del andén:#{a};
El autobús de las once llegará veinte minutos tarde por el tráfico.#El autobús de las once llegará tarde por:#el tráfico;la nieve;un accidente;una huelga
La cafetería de la estación está cerrada hoy por obras.#Hoy la cafetería está:#cerrada;abierta toda la noche;llena de gente;en el andén uno
Los pasajeros con bicicleta deben ponerla en la parte de atrás del autobús.#Las bicicletas van:#en la parte de atrás;dentro del autobús;en el techo;en la consigna
Recuerden que está prohibido comer dentro de los autobuses.#Dentro de los autobuses está prohibido:#comer;hablar por teléfono;dormir;llevar maletas
Los billetes se pueden comprar en las máquinas o en la aplicación del móvil.#Los billetes se pueden comprar:#en máquinas o en el móvil;solo en la taquilla;al conductor;en el hotel
Los estudiantes tienen un descuento del {p=veinte|diez|treinta|cincuenta} por ciento.#Los estudiantes tienen un descuento del:#{p} por ciento;
"""),
    facts="""
Voy al instituto en autobús porque vivo bastante lejos, a unos diez kilómetros.#¿Cómo vas al instituto?#¿Por qué va {N} al instituto en autobús?#(Porque) vive (bastante) lejos#Refuse vivo lejos#Porque vive lejos.;Porque es gratis.;Porque no tiene bici.;Porque llueve mucho.#Su casa está lejos del instituto.#Vive al lado del instituto.#1#+sbus -sbike -smetro
El metro de mi ciudad es rápido, pero en hora punta está lleno de gente.#¿Qué piensas del metro de tu ciudad?#¿Qué es lo malo del metro según {N}?#(En hora punta) está lleno (de gente)#Refuse es rápido#Hay demasiada gente en hora punta.;Es muy caro.;Es lento.;Está sucio.#Critica la cantidad de gente en el metro a ciertas horas.#Dice que el metro es lento.#2
El año pasado viajé en avión por primera vez y estaba muy nervios<o|a>.#¿Has viajado en avión?#¿Cómo se sentía {N} en su primer viaje en avión?#Nervios<o|a>#Refuse tranquil<o|a>#Nervios<o|a>.;Content<o|a>.;Cansad<o|a>.;Aburrid<o|a>.#Su primer vuelo le dio miedo.#Estaba muy tranquil<o|a> en su primer vuelo.#2
Me encanta viajar en tren porque puedo leer y mirar el paisaje.#¿Cuál es tu medio de transporte preferido?#¿Qué hace {N} cuando viaja en tren? (Menciona una cosa.)#Lee / mira el paisaje#Refuse puedo leer#Lee y mira el paisaje.;Duerme.;Trabaja con el ordenador.;Come.#Disfruta de los viajes en tren.#Odia viajar en tren.#1
En mi barrio hay un carril bici nuevo, así que ahora voy a todas partes en bicicleta.#¿Usas la bicicleta?#¿Qué ha cambiado en el barrio de {N}?#Hay un carril bici nuevo#Refuse voy en bicicleta tc#Hay un carril bici nuevo.;Hay una estación nueva.;Hay menos tráfico.;Han cerrado el metro.#Hay una nueva vía para bicicletas en su zona.#No puede ir en bici por su barrio.#2#+sbike -sbus -smetro
Mi padre va al trabajo en coche y siempre se queja de los atascos.#¿Cómo va tu familia al trabajo?#¿De qué se queja el padre de {N}?#(De los) atascos / del tráfico#Refuse del coche#De los atascos.;Del precio de la gasolina.;Del aparcamiento.;De los autobuses.#A su padre le molesta el tráfico.#Su padre va al trabajo a pie.#1
Creo que deberíamos usar menos el coche para proteger el medio ambiente.#¿Qué piensas del coche?#¿Por qué cree {N} que deberíamos usar menos el coche?#(Para) proteger el medio ambiente#Refuse deberíamos usar menos tc#Para proteger el medio ambiente.;Porque es caro.;Porque es peligroso.;Porque es lento.#Piensa en el planeta cuando habla del coche.#Cree que hay que usar más el coche.#3
La semana pasada perdí el autobús y tuve que ir andando al instituto.#¿Te pasó algo la semana pasada?#¿Cómo fue {N} al instituto la semana pasada?#Andando / a pie#Refuse en autobús#a pie;en autobús;en coche;en bicicleta#Ese día caminó hasta el instituto.#Ese día fue en coche con su padre.#2#+sbus -sbike -smetro
En mi ciudad el transporte público es barato para los jóvenes: pagamos solo diez euros al mes.#¿Es caro el transporte en tu ciudad?#¿Cuánto paga {N} al mes por el transporte?#Diez euros#Refuse veinte euros#diez euros;veinte euros;cinco euros;nada#El abono para jóvenes cuesta poco.#Los jóvenes pagan mucho por el transporte.#1#spain
Cuando tenga dieciocho años, voy a sacarme el carné de conducir.#¿Quieres aprender a conducir?#¿Qué va a hacer {N} a los dieciocho años?#Sacar(se) el carné (de conducir)#Refuse conducir tc#sacarse el carné de conducir;comprarse una moto;viajar en avión;vender su bicicleta#Quiere conducir cuando sea mayor de edad.#Nunca quiere conducir.#2
Para ir a casa de mis abuelos en el campo, tenemos que coger dos trenes y un autobús.#¿Es fácil ir a casa de tus abuelos?#¿Qué transporte usa {N} para ir a casa de sus abuelos?#Dos trenes y un autobús#Refuse dos trenes tc#dos trenes y un autobús;un avión;el coche de su padre;un barco#El viaje a casa de sus abuelos es complicado.#Sus abuelos viven en su misma calle.#2
Una vez me perdí en el centro de Madrid, pero un señor muy amable me ayudó a encontrar la estación.#¿Te has perdido alguna vez?#¿Quién ayudó a {N} cuando se perdió?#Un señor (muy amable)#Refuse un policía#un señor;un policía;una amiga;su madre#Un desconocido le ayudó.#Encontró la estación sol<o|a> sin ayuda.#2
Me gustaría ir en barco a las islas, aunque me mareo un poco.#¿Te gustaría hacer un viaje en barco?#¿Qué problema tiene {N} en los barcos?#Se marea (un poco)#Refuse me mareo#Se marea.;Tiene miedo al agua.;Es muy caro.;No sabe nadar.#Los barcos no le sientan bien.#Nunca se marea.#3
El taxi es cómodo, pero es demasiado caro para usarlo todos los días.#¿Coges taxis?#¿Por qué no usa {N} el taxi todos los días?#(Porque) es (demasiado) caro#Refuse es cómodo#Porque es demasiado caro.;Porque es incómodo.;Porque no hay taxis.;Porque tarda mucho.#El precio del taxi es el problema.#Usa el taxi a diario.#2
Si pudiera elegir, viviría en una ciudad con buen transporte público para no necesitar coche.#¿Dónde te gustaría vivir en el futuro?#¿Por qué quiere vivir {N} en una ciudad con buen transporte?#Para no necesitar (un) coche#Refuse viviría en una ciudad tc#Para no necesitar coche.;Para trabajar en el metro.;Porque le gusta conducir.;Porque es más barato.#Prefiere no depender del coche.#Quiere comprarse un coche grande.#3
Ayer hubo huelga de metro y llegué al instituto una hora tarde.#¿Llegaste tarde ayer?#¿Por qué llegó tarde {N} ayer?#(Porque) hubo huelga (de metro)#Refuse hay huelga#Hubo huelga de metro.;Se levantó tarde.;Perdió las llaves.;Llovió mucho.#Ayer el metro no funcionó con normalidad.#Ayer llegó pronto al instituto.#2#+smetro -sbus -sbike
""",
    tq="""
p#¿Cómo vas al instituto?#¿Cómo llegas al instituto por la mañana?#Means of transport + detail, e.g. *Voy a pie porque vivo cerca.*
p#¿Qué transporte público hay en tu ciudad?#¿Hay autobuses o metro en tu ciudad?#Lists public transport available.
p#¿Cuál es tu medio de transporte favorito?#¿Prefieres el tren o el autobús?#Names a preferred means of transport.
o#¿Qué opinas del transporte público en tu zona? ¿Por qué?#¿Te gusta el transporte de tu ciudad? ¿Por qué (no)?#Opinion + reason (price, punctuality, crowds).
o#¿Es mejor ir en bicicleta o en coche? ¿Por qué?#¿Prefieres la bici o el coche? ¿Por qué?#Comparison + reason (environment, speed, health).
pa#Háblame de un viaje largo que hiciste.#¿Adónde fuiste en tu último viaje largo? [PAUSA] ¿Cómo fuiste?#Past narrative: destination, transport, experience.
pa#¿Cómo fuiste de vacaciones el año pasado?#El año pasado, ¿viajaste en tren, en avión o en coche?#Past tense: transport used and opinion.
f#¿Vas a aprender a conducir? ¿Por qué (no)?#En el futuro, ¿vas a tener coche? ¿Por qué (no)?#Future + reason.
c#¿Cómo sería el transporte ideal para tu ciudad?#¿Qué cambiarías del transporte de tu ciudad?#Conditional description of improvements.
d#Explica las ventajas y desventajas de viajar en avión.#¿Qué es lo bueno y lo malo de viajar en avión?#Advantages and disadvantages with explanation.
f#¿Qué viaje vas a hacer el próximo verano?#¿Adónde vas a viajar en las próximas vacaciones?#Future: destination and transport.
""",
)

# tidy two templates edited by .replace above
C["A4"]["ex"] = C["A4"]["ex"].replace("{fr} dice:#Para llegar al museo, gira {v}.#¿Por dónde hay que ir?#direccion",
                                      "{fr} dice:#El museo está {v}.#¿Dónde está el museo?#direccion")
