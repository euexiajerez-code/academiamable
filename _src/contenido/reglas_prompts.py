# Reglas del evaluador de prompts (laboratorio «evaluador-prompts» y «constructor-prompts»).
# build.py las mete como JSON en las páginas que tienen esos laboratorios; labs.js las lee.
#
# Cada ingrediente: k (clave), n / nf (nombre normal / Fácil), w (puntos), d / df (para qué sirve),
# re (expresiones regulares de JavaScript, en minúsculas y SIN tildes ni ñ: el texto se compara
# así, quitando tildes; «ñ» pasa a «n»). Con que case una, el ingrediente se enciende.
# Puntuación: suma de los puntos de los ingredientes encendidos (total 100). Si no hay tarea, como
# mucho 40. Con menos de 6 palabras, como mucho 25.
# Si cambias una frase de EJEMPLOS, comprueba que enciende su propio ingrediente.

INGREDIENTES = [
    {'k': 'rol', 'n': 'Quién eres', 'nf': 'Quién eres', 'w': 15,
     'd': 'Tu papel. La IA contesta mejor si sabe desde dónde le hablas.',
     'df': 'Di quién eres.',
     're': [
         r'\b(soy|somos) (un|una|el|la|de|del|duen|maestr|secretari|president|tesorer|autonom|jubilad|camarer|agricultor|ganader|peluquer|tender|monitor|profesor|educador|estudiante|madre|padre|abuel|vecin|voluntari|cociner|panader|enfermer|tecnic|socio|socia|responsable|coordinador|alcalde|concejal)\w*',
         r'\btengo (un|una) (bar|tienda|peluqueria|negocio|restaurante|panaderia|carniceria|farmacia|taller|granja|casa rural|empresa|comercio|kiosco|quiosco|asociacion|cafeteria|fruteria|huerto|olivar|explotacion|academia|hotel|hostal)\b',
         r'\b(trabajo|trabajamos) (en|como|de)\b',
         r'\b(actua|actue|haz|hazlo) (como|de) ',
         r'\beres (un|una|mi)\b',
         r'\bponte en (el papel|la piel)\b',
         r'\b(llevo|regento|dirijo|gestiono|presido) (un|una|el|la)\b',
         r'\b(mi|nuestro|nuestra) (bar|tienda|peluqueria|negocio|restaurante|asociacion|panaderia|empresa|club|ampa|cooperativa|comercio|cafeteria|colegio|clase)\b',
     ]},
    {'k': 'tarea', 'n': 'Qué quieres', 'nf': 'Qué quieres', 'w': 25,
     'd': 'La tarea, con un verbo claro: escribe, resume, haz, explica…',
     'df': 'Di qué quieres que haga.',
     're': [
         r'\b(escribe|escribeme|escribenos|redacta|redactame|resume|resumeme|resumelo|haz|hazme|hazlo|crea|creame|explica|explicame|explicalo|traduce|traduceme|dame|danos|prepara|preparame|propon|proponme|sugiere|sugiereme|ayudame|corrige|corrigeme|revisa|revisame|mejora|mejorame|organiza|organizame|inventa|inventame|genera|dime|enumera|compara|calcula|disena|disename|cuentame|ordena|convierte|transforma|adapta|adaptame|reescribe|busca|buscame|elabora|planifica|recomiendame|recomienda|piensa|escoge|elige|pon|ponme|anade|quita|acorta|alarga|simplifica)\b',
         r'\b(quiero|queremos|necesito|necesitamos) (que|un|una|unos|unas|el|la|saber|hacer|escribir|preparar|ideas)\b',
         r'\bme (gustaria|puedes|podrias|haces|harias)\b',
         r'\b(puedes|podrias) (escribir|hacer|ayudar|explicar|resumir|preparar|crear|traducir|darme|decirme)\b',
     ]},
    {'k': 'contexto', 'n': 'Para qué', 'nf': 'Para qué', 'w': 20,
     'd': 'El contexto: para qué es, para quién, qué está pasando.',
     'df': 'Di para qué lo quieres.',
     're': [
         r'\bpara (que|avisar|anunciar|invitar|celebrar|explicar|pedir|vender|promocionar|informar|felicitar|recordar|agradecer|presentar|convocar|animar|mandar|enviar|colgar|poner|repartir|mis|mi|nuestros|nuestras|nuestro|nuestra|cuando|los socios|las socias|los vecinos|los clientes|las clientas|la reunion|la fiesta|la feria|el grupo)\b',
         r'\bpara \w+(ar|er|ir)\b',
         r'\b(porque|ya que|puesto que|debido a)\b',
         r'\b(mis|nuestros|nuestras|los|las) (clientes|clientas|socios|socias|vecinos|vecinas|alumnos|alumnas|usuarios|usuarias|hijos|nietos|familiares|companeros|seguidores|proveedores|voluntarios)\b',
         r'\bsobre (el|la|los|las|mi|mis|un|una|nuestro|nuestra|como|que)\b',
         r'\b(el|este|esta|la proxima|el proximo|cada) (lunes|martes|miercoles|jueves|viernes|sabado|domingo|semana|mes|verano|invierno|navidad|feria|fiesta|ano|temporada)\b',
         r'\b(cerramos|abrimos|celebramos|organizamos|vendemos|tenemos|hacemos|empiezan|empieza|vamos a|queremos|estamos)\b',
         r'\b(se trata de|el objetivo|la idea es|lo voy a|lo quiero para|es para|va a ser|lo necesito para)\b',
         r'\b\d{1,2} de (enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|octubre|noviembre|diciembre)\b',
     ]},
    {'k': 'formato', 'n': 'Formato', 'nf': 'Cómo lo quieres', 'w': 15,
     'd': 'La forma: lista, 3 puntos, tabla, para WhatsApp, menos de 50 palabras…',
     'df': 'Di si lo quieres corto, en lista o para WhatsApp.',
     're': [
         r'\ben (\d+|un|una|dos|tres|cuatro|cinco|seis|siete|ocho|diez) (puntos|frases|lineas|parrafos|pasos|ideas|opciones|apartados|columnas|palabras|propuestas)\b',
         r'\b(tabla|lista|esquema|vinetas|guiones|titular|titulo|asunto|eslogan|en un parrafo|paso a paso|por puntos|numerado|numerada)\b',
         r'\b(menos|maximo|como mucho|no mas|mas o menos|unas) (de )?\d+',
         r'\b\d+ (palabras|caracteres|lineas|frases|puntos|ideas|opciones)\b',
         r'\bpara (whatsapp|instagram|facebook|un cartel|el cartel|la puerta|imprimir|el escaparate|la radio|un correo|el correo|email|un folleto|la web|redes|un sms|la pizarra)\b',
         r'\b(corto|corta|cortito|cortita|breve|resumido|en pocas palabras|una sola frase|en una frase)\b',
         r'\b(en (espanol|portugues|ingles|frances) y en)\b',
     ]},
    {'k': 'tono', 'n': 'Tono', 'nf': 'Cómo suena', 'w': 12,
     'd': 'El tono y el público: cercano, formal, sencillo, para mayores, lectura fácil…',
     'df': 'Di si lo quieres serio, alegre o fácil.',
     're': [
         r'\b(tono|cercano|cercana|formal|informal|amable|sencillo|sencilla|sencillas|sencillos|serio|seria|divertido|divertida|alegre|carinoso|carinosa|profesional|respetuoso|respetuosa|educado|educada|natural|simpatico|simpatica|calido|calida|positivo|positiva|motivador|tranquilo|tranquila|con gracia|con humor|de tu|de usted|tuteando|claro y|clara y)\b',
         r'\blectura facil\b',
         r'\b(palabras|frases|lenguaje) (faciles|sencillas|sencillo|claras|claro|cortas)\b',
         r'\bpara (personas mayores|mayores|ninos|ninas|jovenes|adolescentes|personas con|gente del pueblo|todos los publicos|que lo entienda|que se entienda)\b',
         r'\bcomo si (yo )?(tuviera|fuera|se lo explicaras|hablaras)\b',
         r'\b(dirigido a|va dirigido|el publico)\b',
     ]},
    {'k': 'limites', 'n': 'Límites o ejemplo', 'nf': 'Qué no quieres', 'w': 13,
     'd': 'Lo que no quieres, o un ejemplo de lo que sí. Así no se inventa.',
     'df': 'Di qué no quieres.',
     're': [
         r'\bno (uses|utilices|pongas|incluyas|menciones|digas|metas|anadas|inventes|te inventes|escribas|hables|repitas|cambies|toques|des|seas|exageres|prometas)\b',
         r'\b(evita|evitando|evites)\b',
         r'\bsin (palabras|tecnicismos|emojis|emoticonos|inventar|personas|letras|precios|datos|faltas|anglicismos|exagerar|repetir|rodeos|adornos|mentir|nombres|numeros|prometer|\w+ar\b|\w+er\b|\w+ir\b)',
         r'\b(por ejemplo|ejemplo:|como este|como esta|como estos|como estas|asi:|te pongo un ejemplo|imita|siguiendo este|basate en|parecido a|al estilo de)\b',
         r'\b(solo|solamente|unicamente)\b',
         r'\bsi no (sabes|estas seguro|estas segura|lo sabes|tienes)\b',
         r'\b(preguntame|avisame|marcalo|dejalo en blanco)\b',
         r'\[[^\]]{2,20}\]',
     ]},
]

# Avisos de datos personales (DNI, NIE, IBAN, teléfono, clave). No restan puntos: avisan.
DATOS = [r'\b\d{8}\s?[a-z]\b', r'\b[xyz]\d{7}[a-z]\b', r'\bes\d{2}[\s\d]{18,}', r'\b[6789]\d{2}\s?\d{2,3}\s?\d{2,3}\s?\d{0,2}\b', r'\b(contrasena|clave|pin)\b\W{0,3}(es|:)?\s*\S*\d']

# Orden en que se sugiere el ingrediente que falta.
ORDEN = ['tarea', 'contexto', 'rol', 'formato', 'tono', 'limites']

# Frase que propone el botón «Añadir», según el tema que detecta (bar, tienda, asociación o general).
EJEMPLOS = {
    'rol': {
        'bar': 'Tengo un bar en un pueblo de Extremadura.',
        'tienda': 'Tengo una tienda pequeña en el pueblo.',
        'asoc': 'Soy la secretaria de una asociación de vecinos.',
        'gen': 'Soy una persona que está empezando con la IA.',
    },
    'tarea': {
        'bar': 'Escribe un aviso para mis clientes.',
        'tienda': 'Escribe un mensaje para mis clientas.',
        'asoc': 'Escribe un aviso para los socios.',
        'gen': 'Escribe un mensaje corto para mi familia.',
    },
    'contexto': {
        'bar': 'Es para avisar de que el lunes cerramos por la feria.',
        'tienda': 'Es para anunciar que las rebajas empiezan el lunes.',
        'asoc': 'Es para invitar a la comida del sábado.',
        'gen': 'Es para invitarles a comer el domingo.',
    },
    'formato': {
        'bar': 'En menos de 60 palabras, para WhatsApp.',
        'tienda': 'En 3 puntos cortos, para el escaparate.',
        'asoc': 'En menos de 80 palabras, para el grupo de WhatsApp.',
        'gen': 'En menos de 50 palabras, para WhatsApp.',
    },
    'tono': {
        'bar': 'Con un tono cercano y alegre, de tú.',
        'tienda': 'Con un tono amable y cercano.',
        'asoc': 'Con palabras sencillas, para personas mayores.',
        'gen': 'Con un tono cariñoso y sencillo.',
    },
    'limites': {
        'bar': 'No te inventes precios: pon [precio] y lo relleno yo.',
        'tienda': 'No uses palabras en inglés.',
        'asoc': 'Si te falta un dato, no te lo inventes: pregúntame.',
        'gen': 'No uses palabras difíciles.',
    },
}

# Temas, para elegir el ejemplo que se propone
ESCENARIOS = {
    'bar': r'\b(bar|tapas?|cafeteria|restaurante|camarer|cocido|menu del dia)\b',
    'tienda': r'\b(tienda|comercio|clientas?|ropa|panaderia|peluqueria|productos|rebajas|escaparate)\b',
    'asoc': r'\b(asociacion|socios?|socias?|vecinos|ayuntamiento|ampa|club|junta|acta|reunion)\b',
}

REGLAS = {'ing': INGREDIENTES, 'datos': DATOS, 'orden': ORDEN, 'ej': EJEMPLOS, 'esc': ESCENARIOS}

# Galería «Antes y después» del evaluador: tres casos de pueblo (bar, tienda, asociación).
GALERIA = [
    {'t': 'El bar de Paco', 'tf': 'Un bar',
     'antes': 'Haz un cartel de tapas.',
     'despues': 'Tengo un bar en Fregenal de la Sierra. Escribe el texto de un cartel para la puerta, para anunciar las tapas del fin de semana a los vecinos y a los clientes portugueses. En 4 líneas cortas, en español y en portugués. Con un tono cercano y alegre. No uses la palabra «gourmet» ni te inventes precios: pon [precio].'},
    {'t': 'La tienda de Carmen', 'tf': 'Una tienda',
     'antes': 'Escribe algo para las rebajas.',
     'despues': 'Tengo una tienda de ropa en el pueblo. Escribe un mensaje para mis clientas de WhatsApp para anunciar que las rebajas empiezan el lunes 7 de enero. En menos de 50 palabras. Con un tono cariñoso y de tú. No pongas porcentajes de descuento: los pongo yo.'},
    {'t': 'La asociación de vecinos', 'tf': 'Una asociación',
     'antes': 'Resume esto.',
     'despues': 'Soy la secretaria de una asociación de vecinos. Resume el acta que te pego abajo para mandarla a los socios, que muchos son mayores. En 5 puntos, con frases cortas y en lectura fácil. Si algo no queda claro en el acta, no te lo inventes: márcalo con [revisar].'},
]

# Constructor de prompts: opciones de cada paso (k = ingrediente). 'f': True = sale en Fácil.
CONSTRUCTOR = [
    {'k': 'rol', 't': '¿Quién eres?', 'tf': '¿Quién eres?', 'chips': [
        {'t': 'Tengo un bar en el pueblo', 'f': True},
        {'t': 'Tengo una tienda pequeña', 'f': True},
        {'t': 'Soy la secretaria de una asociación'},
        {'t': 'Soy una persona que busca trabajo'}]},
    {'k': 'tarea', 't': '¿Qué quieres que haga?', 'tf': '¿Qué quieres?', 'chips': [
        {'t': 'Escribe un mensaje para mis clientes', 'f': True},
        {'t': 'Haz el texto de un cartel', 'f': True},
        {'t': 'Resume este texto'},
        {'t': 'Prepárame una lista de preguntas'}]},
    {'k': 'contexto', 't': '¿Para qué es?', 'tf': '¿Para qué es?', 'chips': [
        {'t': 'para avisar de que el lunes cerramos por la feria', 'f': True},
        {'t': 'para invitar a la comida del sábado', 'f': True},
        {'t': 'para anunciar las rebajas de enero'},
        {'t': 'para preparar una entrevista de camarero'}]},
    {'k': 'formato', 't': '¿Cómo lo quieres?', 'tf': '¿Cómo de largo?', 'chips': [
        {'t': 'En menos de 50 palabras, para WhatsApp', 'f': True},
        {'t': 'En 3 puntos cortos', 'f': True},
        {'t': 'En una tabla con dos columnas'},
        {'t': 'En 4 líneas, para poner en la puerta'}]},
    {'k': 'tono', 't': '¿Con qué tono?', 'tf': '¿Cómo tiene que sonar?', 'chips': [
        {'t': 'Con un tono cercano y alegre', 'f': True},
        {'t': 'En lectura fácil, con frases cortas', 'f': True},
        {'t': 'Con un tono formal y educado'},
        {'t': 'Con palabras sencillas, para personas mayores'}]},
    {'k': 'limites', 't': '¿Qué no quieres?', 'tf': '¿Qué no quieres?', 'chips': [
        {'t': 'No te inventes precios ni fechas', 'f': True},
        {'t': 'No uses palabras en inglés', 'f': True},
        {'t': 'Si te falta un dato, pregúntame'},
        {'t': 'Sin emojis'}]},
]
