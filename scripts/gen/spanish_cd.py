"""Original content for Area D: The world of work (D1-D2). Format: see spanish.py."""

C = {}

C["D1"] = dict(
    theme="sus estudios y su instituto", tema="El instituto y los estudios",
    scene=["Estás en el instituto de {fr} en {city}. Es tu primer día de intercambio.",
           "Estás en casa de {fr} en {city}. {fr} está preparando la mochila para el instituto."],
    ex="""
{fr} dice:#Mi asignatura favorita es {v}.#¿Cuál es la asignatura favorita de {fr}?#asignatura
{fr} dice:#La primera clase de hoy es {v}.#¿Qué clase tienen primero?#asignatura
{fr} dice:#No me gusta nada {v}.#¿Qué asignatura no le gusta a {fr}?#asignatura
{fr} pregunta:#¿Me dejas {v}?#¿Qué necesita {fr}?#material
{fr} dice:#Se me ha olvidado {v} en casa.#¿Qué ha olvidado {fr}?#material
{fr} dice:#Ahora vamos a {v}.#¿Adónde van ahora?#lugar_escuela
{fr} dice:#Nos vemos en {v} a la hora del recreo.#¿Dónde van a verse en el recreo?#lugar_escuela
{fr} dice:#Mañana tenemos examen de {v}.#¿De qué es el examen de mañana?#asignatura
{fr} dice:#Para la clase de hoy tengo que llevar {v}.#¿Qué tiene que llevar {fr}?#material
""".replace("examen de {v}.#¿De qué es el examen de mañana?#asignatura", "un examen y tengo que estudiar {v}.#¿Qué tiene que estudiar {fr}?#asignatura"),
    signs=("En un instituto", """
Secretaría#Tengo que entregar un papel para el viaje de estudios.
Sala de profesores: no entrar#Los alumnos no pueden pasar a esta sala.
Silencio: exámenes#En este pasillo no se puede hacer ruido hoy.
Laboratorio: prohibido comer y beber#No puedes tomarte el zumo en la clase de química.
Biblioteca: préstamo de libros#Aquí puedes llevarte un libro a casa.
Comedor: turno de las dos#Los alumnos de este grupo comen a las dos.
Taquillas de los alumnos#Aquí guardo mis libros entre clases.
Enfermería#Me duele la cabeza y necesito ayuda.
Gimnasio: zapatillas obligatorias#Para entrar en clase de educación física hay que llevar calzado deportivo.
Tablón de anuncios: actividades extraescolares#Quiero saber qué clubes hay después de clase.
"""),
    ann=dict(title="Información para el viaje de estudios", desc="un anuncio del director de un instituto", sp="Director",
             open="Buenos días, alumnos. Os doy información sobre el viaje de estudios del mes que viene.",
             close="Si tenéis preguntas, hablad con vuestro tutor o tutora. Gracias.",
             facts="""
El viaje es para los alumnos de cuarto curso y dura {d=cinco|tres|cuatro|seis} días.#El viaje dura:#{d} días
Vamos a visitar museos y una universidad en la capital.#Los alumnos van a visitar:#museos y una universidad;playas;fábricas;parques de atracciones
Salimos el lunes a las siete de la mañana desde la puerta del instituto.#Los alumnos salen desde:#la puerta del instituto;la estación;el aeropuerto;la plaza
Hay que llevar el carné de estudiante y una autorización firmada por los padres.#Hay que llevar:#una autorización de los padres;un diccionario;un ordenador;dinero en efectivo
Está prohibido llevar altavoces en el autobús.#En el autobús está prohibido llevar:#altavoces;comida;libros;mochilas grandes
Los alumnos van a dormir en un albergue juvenil en el centro.#Los alumnos van a dormir en:#un albergue juvenil;un hotel de lujo;un camping;casas de familias
El último día hay una visita a una empresa de tecnología.#El último día visitarán:#una empresa de tecnología;un estadio;un zoo;un castillo
"""),
    facts="""
Estudio en un instituto público bastante grande, con más de mil alumnos.#¿Cómo es tu instituto?#¿Cuántos alumnos hay en el instituto de {N}?#Más de mil#Refuse mil on its own tc#más de mil;unos cien;quinientos;más de cinco mil#Va a un instituto grande.#Su instituto es muy pequeño.#1
Las clases empiezan a las ocho y media y terminan a las tres.#¿A qué hora empiezan las clases?#¿A qué hora terminan las clases de {N}?#A las tres#Refuse a las ocho y media#a las tres;a las dos;a las cinco;a mediodía#Sale del instituto por la tarde.#Las clases terminan a las seis.#1
Mi asignatura favorita es la biología porque me interesan mucho los animales.#¿Cuál es tu asignatura favorita?#¿Por qué le gusta la biología a {N}?#(Porque) le interesan los animales#Refuse me interesan#Le interesan los animales.;El profesor es simpático.;Es fácil.;Sacan buenas notas.#Le atrae el mundo animal.#No le gusta la biología.#1
Las matemáticas me cuestan mucho, así que voy a clases particulares los miércoles.#¿Qué asignatura te resulta difícil?#¿Qué hace {N} los miércoles?#(Va a) clases particulares (de matemáticas)#Refuse me cuestan#Va a clases particulares.;Juega al fútbol.;Trabaja.;Va al cine.#Recibe ayuda extra con las matemáticas.#Las matemáticas le parecen facilísimas.#2
Nuestro profesor de historia es muy divertido y explica las cosas con películas.#¿Cómo son tus profesores?#¿Cómo explica las cosas el profesor de historia de {N}?#Con películas#Refuse es divertido#con películas;con canciones;con juegos;con libros#El profesor usa el cine en clase.#El profesor de historia es muy aburrido.#2
En mi instituto no se puede usar el móvil y hay que llevar uniforme.#¿Qué normas hay en tu instituto?#¿Qué hay que llevar en el instituto de {N}?#Uniforme#Refuse el móvil#uniforme;corbata;gorra;zapatillas#Su instituto tiene normas sobre la ropa.#Puede llevar la ropa que quiera.#1
Creo que algunas normas son injustas; por ejemplo, no podemos salir del instituto en el recreo.#¿Qué piensas de las normas?#¿Qué norma le parece injusta a {N}?#No pueden salir (del instituto) en el recreo#Refuse algunas normas#No poder salir en el recreo.;Llevar uniforme.;No usar el móvil.;Hacer deberes.#No está de acuerdo con una norma.#Piensa que todas las normas son justas.#3
El año pasado hice un intercambio con un instituto francés y mejoré mucho mi francés.#¿Has hecho algún intercambio?#¿Qué mejoró {N} con el intercambio?#(Su) francés#Refuse un instituto francés#su francés;sus notas;su inglés;su español#El intercambio le ayudó con un idioma.#Nunca ha hecho un intercambio.#2
Ayer suspendí el examen de química porque no estudié bastante.#¿Qué tal te fue en los exámenes?#¿Por qué suspendió {N} el examen de química?#(Porque) no estudió bastante#Refuse no estudié#Porque no estudió bastante.;Porque estaba enferm<o|a>.;Porque llegó tarde.;Porque era muy difícil.#Admite que no se preparó lo suficiente.#Sacó la mejor nota en química.#2
Para estudiar, hago resúmenes y me grabo leyendo en voz alta.#¿Cómo estudias para los exámenes?#¿Qué hace {N} para estudiar? (Menciona una cosa.)#Hace resúmenes / se graba (leyendo)#Refuse estudiar tc#Hace resúmenes.;Estudia con música.;Estudia en el autobús.;No estudia.#Tiene su propio método de estudio.#Nunca estudia.#2
Me gustaría que el instituto tuviera más actividades al aire libre.#¿Qué cambiarías de tu instituto?#¿Qué le gustaría a {N} que tuviera su instituto?#Más actividades al aire libre#Refuse me gustaría tc#Más actividades al aire libre.;Más exámenes.;Más horas de clase.;Menos vacaciones.#Pide más actividades fuera del aula.#Quiere más horas de clase en el aula.#3
Después del instituto quiero estudiar Medicina en la universidad.#¿Qué vas a hacer después del instituto?#¿Qué quiere estudiar {N} en la universidad?#Medicina#Refuse la universidad#Medicina;Derecho;Arquitectura;Periodismo#Quiere ser médic<o|a>.#No quiere ir a la universidad.#2
Mi hermano prefirió hacer formación profesional y ahora es electricista.#¿Qué estudió tu hermano?#¿Qué es ahora el hermano de {N}?#Electricista#Refuse formación profesional#electricista;mecánico;cocinero;profesor#Su hermano eligió un camino práctico.#Su hermano estudió en la universidad.#2
Pienso que los deberes son útiles, pero los profesores nos mandan demasiados.#¿Qué piensas de los deberes?#¿Cuál es el problema de los deberes para {N}?#Les mandan demasiados#Refuse son útiles#Tienen demasiados.;Son inútiles.;Son fáciles.;Son aburridos.#Tiene demasiadas tareas para casa.#Le gustaría tener más deberes.#3
En el comedor la comida no está mal, pero prefiero traer un bocadillo de casa.#¿Comes en el comedor?#¿Qué prefiere comer {N} en el instituto?#Un bocadillo (de casa)#Refuse el comedor#un bocadillo de casa;la comida del comedor;una pizza;fruta#Lleva su propia comida al instituto.#Siempre come en el comedor.#1
El año que viene voy a ser delegad<o|a> de mi clase.#¿Tienes alguna responsabilidad en el instituto?#¿Qué va a ser {N} el año que viene?#Delegad<o|a> (de clase)#Refuse el año que viene#delegad<o|a> de clase;profesor<|a>;bibliotecari<o|a>;entrenador<|a>#Va a representar a sus compañeros.#Nunca ha querido ser delegad<o|a>.#2
""",
    tq="""
p#¿Cómo es tu instituto?#Describe tu instituto.#Buildings, size, facilities.
p#¿Qué asignaturas estudias?#¿Cuál es tu asignatura favorita?#Subjects with opinion.
p#¿Cómo es un día normal en tu instituto?#¿A qué hora empiezan y terminan tus clases?#Routine with times.
o#¿Qué opinas de las normas de tu instituto? ¿Por qué?#¿Te gusta tu instituto? ¿Por qué (no)?#Opinion + reason.
o#¿Son útiles los deberes? ¿Por qué (no)?#¿Es importante llevar uniforme? ¿Por qué (no)?#Opinion + justification.
pa#¿Qué hiciste en el instituto ayer?#Háblame de una excursión que hiciste con el instituto.#Past.
pa#¿Cómo era tu escuela primaria?#¿Qué hacías en la escuela primaria?#Imperfect.
f#¿Qué vas a hacer después de tus exámenes?#¿Qué vas a estudiar el año que viene?#Future.
c#¿Cómo sería tu instituto ideal?#Si fueras director o directora, ¿qué cambiarías?#Conditional.
d#Explica las diferencias entre los institutos de tu país y los de otro país.#Describe a tu profesor o profesora favorito/favorita.#Description/comparison.
f#¿Vas a ir a la universidad? ¿Por qué (no)?#¿Qué vas a hacer cuando termines el instituto?#Future + reason.
""",
    rp=[dict(ctx=["Estás de intercambio en {city}. Es tu primer día en el instituto. Hablas con el profesor / la profesora de español.#El profesor / La profesora",
                  "Estás en {city}. Quieres hacer un curso de verano en una escuela de idiomas. Hablas con el secretario / la secretaria.#El secretario / La secretaria"],
             slots=["""
Hola, bienvenido/bienvenida. ¿Cuántos años tienes?#Age, e.g. *Tengo dieciséis años.*
Buenos días, ¿qué curso quieres hacer?#Course, e.g. *Un curso de español.*
""", """
¿Qué asignaturas estudias en tu país?#Subjects, e.g. *Historia y ciencias.*
¿Cuántas semanas quieres estudiar?#Duration, e.g. *Dos semanas.*
""", """
¿Cuál es tu asignatura favorita? [PAUSA] ¿Por qué?#Subject + reason, e.g. *El arte, es creativo.*
¿Prefieres clases por la mañana o por la tarde? [PAUSA] ¿Por qué?#Choice + reason.
""", """
¿Qué hiciste ayer en clase?#Past, e.g. *Hice un examen.*
¿Has estudiado español antes?#Perfect/past, e.g. *Sí, estudié dos años.*
""", """
¿Qué vas a estudiar en el futuro?#Future, e.g. *Voy a estudiar idiomas.*
¿Qué te gustaría hacer después de las clases?#Conditional, e.g. *Me gustaría visitar la ciudad.*
"""])],
    form=dict(titles=["Inscripción en el intercambio escolar", "Ficha del curso de verano"],
              ctx=["Vas a participar en un intercambio con un instituto español.", "Te apuntas a un curso de verano en una escuela."],
              gaps="""
Asignatura favorita:#Any school subject, e.g. historia.#Teachers' names.#1
Asignatura que no te gusta:#Any school subject, e.g. química.#Non-subjects.#1
Actividad extraescolar:#Any club or activity, e.g. el coro.#Subjects.#1
Material que necesitas en clase:#Any classroom item, e.g. calculadora.#Subjects.#1
Dos lugares de tu instituto:#Any two places in school, e.g. la biblioteca, el gimnasio.#The same place twice.#2
Lo que quieres estudiar en el futuro:#Any subject or course, e.g. medicina.#Jobs alone are acceptable if they communicate a course of study; refuse non-studies.#1
"""),
)

C["D2"] = dict(
    theme="el trabajo y sus planes para el futuro", tema="El trabajo y el futuro",
    scene=["Estás en {city} con {fr}. Habláis de los trabajos de vuestra familia.",
           "Estás en una feria de empleo para jóvenes en {city} con {fr}."],
    ex="""
{fr} dice:#Mi tío es {v}.#¿Qué trabajo hace el tío de {fr}?#profesion
{fr} dice:#Mi vecino trabaja {v}.#¿Dónde trabaja el vecino de {fr}?#lugar_trabajo
{fr} dice:#En el futuro quiero ser {v}.#¿Qué quiere ser {fr}?#profesion
{fr} dice:#Este verano voy a trabajar {v}.#¿Dónde va a trabajar {fr} este verano?#lugar_trabajo
{fr} dice:#Mi padre es {v} desde hace veinte años.#¿Qué trabajo hace el padre de {fr}?#profesion
{fr} dice:#Mi hermana hace sus prácticas {v}.#¿Dónde hace las prácticas la hermana de {fr}?#lugar_trabajo
{fr} dice:#Nunca me gustaría ser {v}.#¿Qué trabajo no le gustaría hacer a {fr}?#profesion
{fr} dice:#Mi primo busca trabajo {v}.#¿Dónde quiere trabajar el primo de {fr}?#lugar_trabajo
""",
    signs=("En una oficina de empleo", """
Ofertas de trabajo para jóvenes#Busco un empleo de verano para estudiantes.
Entrevistas: espere su turno#Antes de hablar con la empleada, tienes que esperar.
Cursos de formación gratuitos#Puedo aprender algo nuevo sin pagar.
Entregue aquí su currículum#Dejo mis datos y mi experiencia en esta mesa.
Se busca camarero con experiencia#Un bar necesita a alguien que ya haya servido mesas.
Trabajo a tiempo parcial: fines de semana#Solo quiero trabajar el sábado y el domingo.
Prácticas en empresas para estudiantes#Quiero conocer el mundo del trabajo mientras estudio.
Horario de atención: de 9:00 a 14:00#Por la tarde no hay nadie para ayudarme.
Se necesita carné de conducir#Para este trabajo hay que saber manejar un coche.
Oficina cerrada por la tarde#Si vengo a las cinco, no puedo entrar.
"""),
    ann=dict(title="Una feria de empleo", desc="un anuncio en una feria de empleo para jóvenes", sp="Locutora",
             open="Buenos días y bienvenidos a la Feria del Empleo Joven de {city}.",
             close="¡Mucha suerte en la búsqueda de trabajo!",
             facts="""
Este año participan más de {n=sesenta|cuarenta|ochenta|cien} empresas.#¿Cuántas empresas participan?#más de {n}
En la sala A hay ofertas de trabajo en hoteles y restaurantes.#En la sala A hay trabajos en:#hoteles y restaurantes;hospitales;oficinas;fábricas
Podéis hacer una foto profesional gratis para vuestro currículum.#Se puede hacer gratis:#una foto para el currículum;un curso de inglés;una entrevista;un examen
A las once hay un taller sobre cómo preparar una entrevista.#El taller de las once es sobre:#las entrevistas;los idiomas;los viajes;la informática
Las empresas de tecnología buscan jóvenes que hablen inglés.#Las empresas de tecnología buscan jóvenes que:#hablen inglés;tengan coche;sepan cocinar;vivan cerca
Hay información sobre trabajos de voluntariado en el extranjero.#Hay información sobre voluntariado:#en el extranjero;en el colegio;en casa;en el hospital local
La cafetería ofrece descuentos a los estudiantes.#La cafetería ofrece descuentos a:#los estudiantes;los profesores;las empresas;los niños
"""),
    facts="""
Mi madre es enfermera y trabaja en el hospital de la ciudad.#¿En qué trabajan tus padres?#¿Dónde trabaja la madre de {N}?#En el hospital (de la ciudad)#Refuse enfermera#en el hospital;en una farmacia;en un colegio;en una oficina#Su madre trabaja en el sector de la salud.#Su madre es profesora.#1
Mi padre trabaja desde casa con el ordenador, así que lo veo mucho.#¿Y tu padre?#¿Por qué ve mucho {N} a su padre?#(Porque) trabaja desde casa#Refuse con el ordenador#Porque trabaja desde casa.;Porque no trabaja.;Porque trabaja en su instituto.;Porque viven cerca.#Su padre no va a la oficina.#Su padre trabaja muy lejos de casa.#1
Los sábados trabajo en la panadería de mi barrio para ganar un poco de dinero.#¿Tienes un trabajo a tiempo parcial?#¿Dónde trabaja {N} los sábados?#En la panadería (de su barrio)#Refuse para ganar dinero#en la panadería;en un supermercado;en un restaurante;en una tienda de ropa#Tiene un trabajo de fin de semana.#No tiene trabajo.#1
Tengo que levantarme a las seis, pero me gusta porque mis compañeros son simpáticos.#¿Qué te gusta de tu trabajo?#¿Qué le gusta a {N} de su trabajo?#Sus compañeros (son simpáticos)#Refuse levantarse a las seis#Sus compañeros.;El horario.;El sueldo.;La comida.#Se lleva bien con la gente del trabajo.#Odia a sus compañeros.#2
Con el dinero que gano estoy ahorrando para comprarme una moto.#¿Qué haces con el dinero que ganas?#¿Para qué ahorra {N}?#(Para comprarse) una moto#Refuse el dinero que gano#para comprarse una moto;para un viaje;para la universidad;para un móvil#Está guardando dinero para un vehículo.#Gasta todo su dinero en ropa.#2
El año pasado hice prácticas en una oficina de abogados, pero fue aburrido porque solo hacía fotocopias.#¿Has hecho prácticas?#¿Por qué fueron aburridas las prácticas de {N}?#(Porque) solo hacía fotocopias#Refuse en una oficina#Porque solo hacía fotocopias.;Porque no tenía compañeros.;Porque era lejos.;Porque no le pagaban.#Sus prácticas fueron poco interesantes.#Le encantaron sus prácticas.#2
Aprendí que no quiero trabajar en una oficina; prefiero un trabajo más activo.#¿Qué aprendiste de las prácticas?#¿Qué tipo de trabajo prefiere {N}?#(Un trabajo) más activo / fuera de una oficina#Refuse una oficina#un trabajo más activo;un trabajo en una oficina;un trabajo de noche;un trabajo en casa#Busca un trabajo con movimiento.#Quiere trabajar en una oficina toda la vida.#2
Me gustaría ser veterinari<o|a> porque me encantan los animales y quiero ayudarlos.#¿Qué quieres ser en el futuro?#¿Por qué quiere ser veterinari<o|a> {N}? (Menciona una cosa.)#Le encantan los animales / quiere ayudarlos#Refuse me encantan#Porque le encantan los animales.;Porque se gana mucho.;Porque su madre lo es.;Porque es fácil.#Quiere cuidar animales en su trabajo.#No le gustan los animales.#1
Para ser veterinari<o|a> hay que estudiar cinco años en la universidad.#¿Qué hay que hacer para ser veterinari<o|a>?#¿Cuántos años hay que estudiar para ser veterinari<o|a>?#Cinco (años)#Refuse en la universidad#cinco años;tres años;dos años;diez años#La carrera es larga.#Se puede ser veterinario sin estudiar.#2
Para mí, lo más importante en un trabajo no es el dinero, sino hacer algo útil.#¿Qué es lo más importante en un trabajo?#¿Qué es lo más importante en un trabajo para {N}?#Hacer algo útil#Refuse el dinero#Hacer algo útil.;Ganar mucho dinero.;Tener vacaciones largas.;Trabajar poco.#Valora más la utilidad que el sueldo.#Para {N} lo más importante es el sueldo.#3
Mi hermana trabaja en Alemania como ingeniera porque en mi país no encontraba trabajo.#¿Alguien de tu familia trabaja en el extranjero?#¿Por qué se fue a Alemania la hermana de {N}?#(Porque) no encontraba trabajo (en su país)#Refuse como ingeniera#Porque no encontraba trabajo en su país.;Porque quería aprender alemán.;Porque su novio es alemán.;Porque hace buen tiempo.#Su hermana emigró por motivos laborales.#Su hermana trabaja en la misma ciudad que {N}.#3
Creo que en el futuro muchas personas trabajarán desde casa.#¿Cómo será el trabajo en el futuro?#¿Qué cree {N} sobre el trabajo en el futuro?#Muchas personas trabajarán desde casa#Refuse en el futuro#Muchos trabajarán desde casa.;Habrá menos ordenadores.;Todos trabajarán en fábricas.;Nadie trabajará.#Prevé más teletrabajo.#Cree que nadie trabajará desde casa.#3
Este verano voy a trabajar de monitor<|a> en un campamento para niños.#¿Qué vas a hacer este verano?#¿Qué trabajo va a hacer {N} este verano?#Monitor<|a> (en un campamento)#Refuse para niños#monitor<|a> en un campamento;camarer<o|a>;socorrista;dependient<e|a>#Va a trabajar con niños en verano.#Este verano no va a trabajar.#2
No me gustaría trabajar de noche, porque necesito dormir mucho.#¿Hay algún trabajo que no te gustaría hacer?#¿Por qué no le gustaría a {N} trabajar de noche?#(Porque) necesita dormir mucho#Refuse de noche#Porque necesita dormir mucho.;Porque tiene miedo.;Porque no hay autobuses.;Porque pagan poco.#Prefiere un horario de día.#Le encantaría trabajar de noche.#2
Cuando busqué trabajo, mi tía me ayudó a escribir el currículum.#¿Quién te ayudó a buscar trabajo?#¿Qué hizo la tía de {N}?#Le ayudó a escribir el currículum#Refuse me ayudó#Le ayudó con el currículum.;Le dio trabajo.;Le llevó a la entrevista.;Le prestó dinero.#Recibió ayuda familiar para buscar empleo.#Escribió el currículum sin ayuda.#2
Si tuviera mi propia empresa, mis empleados trabajarían cuatro días a la semana.#¿Te gustaría tener tu propia empresa?#¿Cuántos días trabajarían los empleados de {N}?#Cuatro (días a la semana)#Refuse su propia empresa#cuatro días;cinco días;tres días;seis días#Daría a sus empleados una semana corta.#Sus empleados trabajarían todos los días.#3
""",
    tq="""
p#¿En qué trabajan las personas de tu familia?#¿Qué trabajo hace alguien de tu familia?#Jobs and workplaces.
p#¿Tienes un trabajo a tiempo parcial?#¿Ayudas en casa para ganar dinero?#Part-time job or pocket money.
p#¿Qué trabajo te interesa?#¿Qué tipo de trabajo prefieres?#Job interests.
o#¿Es importante ganar mucho dinero? ¿Por qué (no)?#¿Qué es lo más importante en un trabajo? ¿Por qué?#Opinion + reason.
o#¿Es buena idea trabajar mientras estudias? ¿Por qué (no)?#¿Deben trabajar los estudiantes? ¿Por qué (no)?#Opinion + justification.
pa#¿Has hecho prácticas en una empresa? ¿Qué tal?#Háblame de un trabajo que hiciste.#Past narrative + opinion.
pa#¿Qué querías ser cuando eras pequeño/pequeña?#¿Qué trabajo te gustaba de niño/niña?#Imperfect.
f#¿Qué vas a hacer para conseguir tu trabajo ideal?#¿Qué vas a estudiar para tu futura profesión?#Future steps.
c#¿Cuál sería tu trabajo ideal? ¿Por qué?#¿Te gustaría trabajar en el extranjero? ¿Por qué (no)?#Conditional + reason.
d#Describe el trabajo de una persona que admiras.#Explica qué hace una persona en un trabajo que te interesa.#Description.
f#¿Dónde vas a trabajar dentro de diez años?#¿Cómo será tu vida laboral en el futuro?#Future.
""",
    rp=[dict(ctx=["Estás en {city} y quieres trabajar en un restaurante este verano. Tienes una entrevista con el gerente / la gerente.#El gerente / La gerente",
                  "Estás en {city}. Quieres un trabajo de verano en un hotel. Hablas con el director / la directora de personal.#El director / La directora"],
             slots=["""
Buenos días. ¿Por qué quieres este trabajo?#Reason, e.g. *Quiero ganar dinero y practicar español.*
Hola, ¿qué trabajo te interesa?#A job, e.g. *Recepcionista.*
""", """
¿Qué idiomas hablas?#Languages, e.g. *Inglés y español.*
¿Cuándo puedes empezar?#A date/day, e.g. *El uno de julio.*
""", """
¿Cómo eres de carácter?#Personality, e.g. *Soy trabajador y simpático.*
¿Prefieres trabajar por la mañana o por la tarde? [PAUSA] ¿Por qué?#Choice + reason.
""", """
¿Has trabajado antes?#Past/perfect, e.g. *Sí, trabajé en una tienda.*
¿Qué hiciste el verano pasado?#Past, e.g. *Trabajé en un café.*
""", """
¿Qué vas a hacer con el dinero?#Future, e.g. *Voy a viajar.*
¿Qué trabajo te gustaría hacer en el futuro?#Conditional, e.g. *Me gustaría ser profesor.*
"""])],
    form=dict(titles=["Solicitud de trabajo de verano", "Ficha de prácticas en empresas"],
              ctx=["Quieres trabajar este verano en un hotel de la costa.", "Vas a hacer prácticas en una empresa de tu ciudad."],
              gaps="""
Trabajo que te interesa:#Any job, e.g. camarero.#Places alone.#1
Idioma que hablas:#Any language, e.g. inglés.#Countries.#1
Experiencia de trabajo:#Any job or work experience, e.g. en una tienda; or ninguna.#Hobbies.#1
Días que puedes trabajar:#Any day(s), e.g. sábado.#Times alone.#1
Dos cualidades personales:#Any two qualities, e.g. trabajador, puntual.#The same quality twice.#2
Trabajo que quieres hacer en el futuro:#Any job, e.g. médico.#Subjects alone.#1
"""),
    ads=("Ofertas de empleo y formación", """
Soy estudiante y quiero trabajar solo los fines de semana para ganar algo de dinero.#‘Heladería Polar’: buscamos jóvenes para sábados y domingos. No hace falta experiencia.#‘Oficina Gestoría’: administrativo a jornada completa, de lunes a viernes.
Me encantan los niños y busco un trabajo para el verano.#‘Campamento Pinos’: se buscan monitores para julio y agosto, para niños de 6 a 12 años.#‘Residencia Sol’: se necesita personal para cuidar a personas mayores todo el año.
Hablo tres idiomas y quiero trabajar con turistas.#‘Hotel Mirador’: recepcionista con idiomas para la temporada de verano.#‘Taller Mecánico Ruiz’: se busca mecánico con experiencia.
Quiero aprender a ser cocinero, pero no tengo experiencia.#‘Escuela de Hostelería’: curso de cocina de seis meses con prácticas en restaurantes.#‘Restaurante Gourmet’: se busca chef con diez años de experiencia.
Tengo carné de conducir y me gustaría trabajar repartiendo paquetes.#‘RepartoYa’: repartidores con coche propio. Horario flexible.#‘Bicimensajeros’: reparto en bicicleta por el centro de la ciudad.
Estoy terminando la universidad y busco prácticas en una empresa de informática.#‘TecnoSoft’: prácticas pagadas para estudiantes de informática en el último año.#‘Tienda Ordenadores Max’: vendedor de ordenadores, a tiempo completo.
Quiero trabajar al aire libre y me interesan las plantas.#‘Parques y Jardines’: jardineros para el mantenimiento de los parques de la ciudad.#‘Floristería Clara’: dependienta para la tienda, de lunes a sábado.
"""),
)
