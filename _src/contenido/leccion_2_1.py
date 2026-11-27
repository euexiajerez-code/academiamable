# Lección 2.1 · IA que conversa
# Versión Fácil: BORRADOR pendiente de validar con personas usuarias de Euexia.
# Formato de cada paso: lista de bloques (tipo, normal, facil). Las palabras del glosario se
# escriben como [[palabra|definición]].

LECCION = {
    'id': 'ia-que-conversa',
    'modulo': 2,
    'num': '2.1',
    'titulo': 'IA que conversa',
    'minutos': 25,
    'descripcion': 'Qué es una IA que conversa, como ChatGPT o Gemini: para qué sirve, en qué falla y cómo hablar con ella paso a paso. Lección 2.1 del curso gratis IA sin miedo.',
    'validada': True,
    'pasos': [
        ('Situación', [
            ('texto',
             '<p>Paco tiene un bar en Fregenal de la Sierra. Los fines de semana entran muchos portugueses y él se apaña con gestos y cuatro palabras. Quiere poner la carta de tapas también en portugués, pero no sabe por dónde empezar.</p>'
             '<p>Su hija le abre un chat de IA en el móvil y le dice: «Papá, háblale como si fuera un camarero nuevo muy listo. Pídele lo que quieras y, si no te gusta, se lo dices». Paco escribe, duda, borra y vuelve a escribir. A los cinco minutos tiene su carta en portugués… y le ha pedido que quite «gourmet», que en su bar eso no pega.</p>'
             '<p>En esta lección vas a conocer el tipo de IA que más se usa: la que conversa.</p>',
             '<p>Paco tiene un bar.</p>'
             '<p>Vienen muchos clientes de Portugal.</p>'
             '<p>Paco quiere la carta de tapas en portugués.</p>'
             '<p>Su hija le enseña un chat de IA. Paco le escribe y la IA le ayuda.</p>'
             '<p>En esta lección vas a conocer la IA que conversa.</p>'),
        ]),
        ('Descubre', [
            ('info',
             '<h3>La idea clave</h3>'
             '<p>Una IA que conversa es un [[chatbot|Programa con el que hablas escribiendo o con la voz, como si chatearas con alguien.]]: un programa con el que hablas por escrito o con la voz, como en un chat de WhatsApp. Las más conocidas son ChatGPT, Gemini, Claude y Copilot. Por dentro funcionan con un [[modelo de lenguaje|IA que ha aprendido de muchísimos textos y sabe escribir frases que suenan naturales.]], que ha aprendido de muchísimos textos a escribir como una persona.</p>'
             '<p>Lo que la hace especial es la conversación: recuerda lo que le has dicho antes dentro de ese mismo chat. Por eso no hace falta acertar a la primera. Le pides algo, miras lo que te da y le corriges: «más corto», «más serio», «quita esa palabra». Como con Paco y su «gourmet».</p>'
             '<p>Eso sí: escribe con tanta seguridad que parece que lo sabe todo. Y no. Lo importante, compruébalo.</p>',
             '<h3>La idea clave</h3>'
             '<p>Hay una IA que conversa contigo.</p>'
             '<p>Le escribes o le hablas. Ella te contesta.</p>'
             '<p>Por ejemplo: ChatGPT, Gemini, Claude o Copilot.</p>'
             '<p>Si no te gusta lo que dice, se lo dices. Ella lo cambia.</p>'
             '<p>A veces se equivoca. Tú revisas lo importante.</p>'),
            ('dos',
             '<h3>Para qué es buena</h3><ul class="lista-ok"><li>Escribir o mejorar un mensaje, un aviso o una carta.</li><li>Explicar con palabras sencillas algo difícil.</li><li>Traducir a otro idioma.</li><li>Resumir un texto largo.</li><li>Darte ideas: un menú, un nombre, un plan para el sábado.</li></ul>'
             '<h3>Para qué no fiarte de ella</h3><ul><li>Datos exactos: fechas, precios, leyes, horarios.</li><li>Decisiones de salud, dinero o trámites: ahí, una persona experta.</li><li>Guardar tus secretos: no le des tu DNI, tus contraseñas ni tus números del banco.</li><li>Saber lo que ha pasado hoy en tu pueblo.</li></ul>',
             '<h3>Es buena para</h3><ul class="lista-ok"><li>Escribir mensajes.</li><li>Explicar cosas difíciles.</li><li>Traducir.</li><li>Darte ideas.</li></ul>'
             '<h3>No te fíes para</h3><ul><li>Fechas y precios.</li><li>Temas de salud o de dinero.</li><li>Guardar tus datos. No le des tu DNI.</li></ul>'),
            ('lab', {
                'tipo': 'elige-la-mejor', 'id': 'ia-que-conversa-elige', 'titulo': '¿Qué respuesta es mejor?',
                'intro': '<p>Dos respuestas de IA a la misma petición. Las dos suenan bien. ¿Con cuál te quedas? Elige, di cómo de seguro estás y después te enseñamos en qué fijarte.</p>',
                'intro_f': '<p>Hay dos respuestas de una IA. Elige la mejor. Después te decimos por qué.</p>',
                'rondas': [
                    {'f': True,
                     'pide': 'Escríbeme el horario del bar para Semana Santa, para ponerlo en la puerta.',
                     'a': {'t': '<p>¡Claro! Aquí tienes un horario perfecto:</p><p><mark data-c="1">Abrimos todos los días de 8:00 a 24:00</mark>, <mark data-c="1">con música en directo el Jueves Santo</mark> y <mark data-c="1">menú especial por 15 euros</mark>.</p><p><mark data-c="2">En nuestro establecimiento nos complace ofrecer una experiencia gastronómica inolvidable a todos nuestros distinguidos clientes durante estas fechas tan señaladas.</mark></p>'},
                     'b': {'t': '<p><mark data-c="2"><b>Horario de Semana Santa</b></mark></p><p>Jueves Santo: de <mark data-c="1">[hora]</mark> a <mark data-c="1">[hora]</mark><br>Viernes Santo: de [hora] a [hora]<br>Sábado: de [hora] a [hora]<br>Domingo: [abierto o cerrado]</p><p><mark data-c="3">No sé tu horario: rellena las horas antes de imprimirlo. Si me las dices, te lo dejo listo.</mark></p>'},
                     'mejor': 'b',
                     'criterios': [{'c': 1, 't': 'No se inventa datos: deja huecos donde no sabe.', 'tf': 'No se inventa las horas.'},
                                   {'c': 2, 't': 'Hace lo que se le pide: corto y claro, para una puerta.', 'tf': 'Es corto y claro.'},
                                   {'c': 3, 't': 'Te avisa de lo que tienes que revisar tú.', 'tf': 'Te dice qué revisar.'}],
                     'x': 'La A suena muy bien, pero se ha inventado el horario, la música y el precio. Si la cuelgas, tendrás clientes en la puerta a las ocho. La B deja huecos y te avisa: es la útil.',
                     'xf': 'La A se inventa las horas. La B deja huecos para que pongas tus horas.'},
                    {'pide': 'Explícame esta frase de una carta del banco: «Le comunicamos el cargo del adeudo domiciliado».',
                     'a': {'t': '<p><mark data-c="2">El adeudo domiciliado constituye una orden de cobro emitida por el acreedor contra la cuenta del deudor en virtud de un mandato previamente autorizado.</mark></p><p><mark data-c="1">Para revisarlo bien, dime tu número de cuenta y tu DNI.</mark></p>'},
                     'b': {'t': '<p><mark data-c="2">Quiere decir que te han cobrado un recibo en tu cuenta</mark>, como el de la luz o el del agua, porque un día diste permiso para que lo cobraran directamente.</p><p><mark data-c="3">Si no sabes de qué es, llama a tu banco o pásate por la oficina.</mark> <mark data-c="1">No hace falta que me des tus datos para explicártelo.</mark></p>'},
                     'mejor': 'b',
                     'criterios': [{'c': 1, 't': 'Cuida tus datos: no te los pide.'},
                                   {'c': 2, 't': 'Te lo explica con palabras sencillas.'},
                                   {'c': 3, 't': 'Te dice qué hacer después y con quién comprobarlo.'}],
                     'x': 'La A es correcta, pero no se entiende y, además, te pide tu cuenta y tu DNI: eso nunca. La B lo explica fácil y te manda a comprobarlo con tu banco.'},
                ]}),
        ]),
        ('Prueba', [
            ('lab', {
                'tipo': 'evaluador-prompts', 'id': 'ia-que-conversa-evaluador', 'titulo': 'Mejora este mensaje antes de mandarlo', 'modo': 'corto',
                'inicial': 'Escribe un mensaje para mi familia.',
                'intro': '<p>Antes de abrir un chat de verdad, prueba aquí. Esto es lo que le pediría casi todo el mundo. Mejóralo con lo que te sugiere el evaluador hasta pasar de 70: verás que la IA contesta mucho mejor cuando sabe quién eres, para qué es y cómo lo quieres. Lo verás a fondo en el módulo 4.</p>',
                'intro_f': '<p>Mejora este mensaje. Toca «Añadir» para poner las piezas que faltan.</p>'}),
            ('tarea',
             '<h3>Tarea guiada · 10 minutos</h3>'
             '<p>Vas a tener tu primera conversación de verdad, de tres pasos:</p>'
             '<ol><li>Abre un chat de IA gratis: ChatGPT, Gemini, Claude o Copilot.</li>'
             '<li>Escribe: <q>Ayúdame a escribir un mensaje para el grupo de WhatsApp de mi familia. Quiero invitarles a comer el domingo en mi casa. Que sea cariñoso y corto.</q></li>'
             '<li>Lee la respuesta. Ahora corrígela con tus palabras, por ejemplo: <q>Más corto y con un poco de gracia.</q></li>'
             '<li>Pide un último cambio: <q>Añade que cada uno traiga el postre que quiera.</q></li>'
             '<li>Si tu chat tiene un botón de micrófono, prueba a decirle algo con la voz en vez de escribir.</li></ol>'
             '<p>Fíjate en que no has tenido que repetirle lo de la comida: se acuerda de la conversación. No pongas direcciones ni nombres completos; para practicar no hacen falta.</p>'
             '<p>Si no quieres usar ninguna IA todavía, escribe tú el mensaje y pídele a alguien de tu entorno que lo mejore con una IA delante de ti. Luego comparad las dos versiones.</p>',
             '<h3>Tarea · 10 minutos</h3>'
             '<ol><li>Abre un chat de IA. Por ejemplo: ChatGPT o Gemini.</li>'
             '<li>Escribe: <q>Escribe un mensaje corto para invitar a mi familia a comer el domingo.</q></li>'
             '<li>Lee el mensaje.</li>'
             '<li>Escribe: <q>Más corto, por favor.</q></li>'
             '<li>Mira cómo cambia el mensaje.</li></ol>'
             '<p>Puedes hacerlo con alguien de tu familia.</p>'),
        ]),
        ('Conecta', [
            ('texto',
             '<p>Una IA que conversa es como tener a alguien que escribe muy rápido a tu lado:</p>'
             '<ul><li><b>En el trabajo:</b> como Paco, puedes preparar la carta, un cartel de horarios o un mensaje para clientes en otro idioma. Antes de colgarlo, que lo lea alguien que hable ese idioma si puede ser.</li>'
             '<li><b>En casa:</b> te puede explicar con palabras sencillas la carta del banco, de la luz o del ayuntamiento. Copia solo el texto que no entiendes y quita tu nombre, tu dirección y tus números.</li>'
             '<li><b>En el pueblo o la asociación:</b> te ayuda a escribir el orden del día de una reunión, el acta o el mensaje para avisar a los socios. Tú pones los datos y ella los ordena.</li></ul>',
             '<ul><li><b>En el trabajo:</b> la IA te ayuda a escribir en otro idioma.</li>'
             '<li><b>En casa:</b> la IA te explica una carta difícil. Quita tu nombre y tu dirección.</li>'
             '<li><b>En el pueblo:</b> la IA te ayuda a escribir avisos para la asociación.</li></ul>'),
        ]),
        ('Comparte', [
            ('texto',
             '<p>Enséñale a alguien de tu entorno el mensaje que has conseguido en la tarea, con sus tres versiones. Cuéntale el truco: <b>no hace falta acertar a la primera, se le va corrigiendo</b>.</p>'
             '<p>Si quieres, mándanos por WhatsApp la corrección que mejor te ha funcionado.</p>',
             '<p>Enseña a una persona tu mensaje.</p><ul><li>Cuéntale que a la IA le puedes pedir cambios.</li></ul>'),
            ('lab', {
                'tipo': 'explicaselo', 'id': 'ia-que-conversa-explica', 'titulo': 'Explícaselo a…', 'tema': 'cómo hablar con una IA que conversa',
                'intro': '<p>Elige a quién se lo cuentas y rellena los huecos con tus palabras. Después, mándaselo por WhatsApp o cópialo.</p>',
                'intro_f': '<p>Elige a una persona. Escribe con tus palabras. Mándalo por WhatsApp.</p>',
                'huecos': [
                    {'l': 'Qué es un chat de IA', 'lf': 'Qué es', 'ph': 'un programa con el que hablas como por WhatsApp'},
                    {'l': 'Un truco', 'lf': 'Un truco', 'ph': 'no hace falta acertar a la primera: le vas pidiendo cambios'},
                    {'l': 'Un cuidado', 'lf': 'Un cuidado', 'ph': 'no le des tu DNI ni tus números del banco'},
                ]}),
        ]),
        ('Piensa', [
            ('quiz', [
                ('¿Qué hace especial a una IA que conversa?',
                 [('Que siempre acierta a la primera', False, False),
                  ('Que recuerda lo que le has dicho en ese chat y puedes ir corrigiéndola', True, False),
                  ('Que es una persona que te contesta desde una oficina', False, True),
                  ('Que solo entiende órdenes en inglés', False, True)],
                 'Dentro de una misma conversación se acuerda de lo anterior. Por eso puedes pedirle cambios sin repetirlo todo.',
                 'Se acuerda de la conversación. Le puedes pedir cambios.'),
                ('¿Para qué NO deberías fiarte de una IA que conversa sin comprobarlo?',
                 [('Para fechas, precios, leyes o temas de salud', True, False),
                  ('Para darte ideas de un menú', False, False),
                  ('Para hacer más corto un mensaje', False, True),
                  ('Para cambiar el tono de un texto', False, True)],
                 'Escribe muy bien, pero se puede inventar datos. Lo que tenga consecuencias, compruébalo en una fuente fiable o con una persona experta.',
                 'Comprueba las fechas, los precios y la salud.'),
                ('Quieres que te explique una carta del banco. ¿Qué haces?',
                 [('Le hago una foto a la carta entera con mis datos y la subo', False, False),
                  ('Copio solo el texto que no entiendo, sin mi nombre ni mis números', True, False),
                  ('Le doy también mi número de cuenta para que lo revise', False, True),
                  ('Le doy mi DNI para que sepa quién soy', False, True)],
                 'Puede ayudarte a entender la carta, pero tus datos personales y bancarios no hacen falta. Quítalos antes.',
                 'No le des tus datos. Solo el texto que no entiendes.'),
            ]),
            ('texto',
             '<p><label for="reflexion-2-1"><b>Tu reflexión en una línea:</b> ¿para qué le pedirías ayuda tú a una IA que conversa?</label></p>'
             '<p><textarea id="reflexion-2-1" rows="2" style="width:100%;font:inherit;padding:12px;border-radius:12px;border:2px solid var(--l)"></textarea></p>'
             '<p style="font-size:.9rem;color:var(--m)">Lo que escribas aquí no se guarda ni se envía a ningún sitio.</p>',
             '<p><label for="reflexion-2-1-f"><b>Escribe una frase:</b> ¿para qué usarías tú un chat de IA?</label></p>'
             '<p><textarea id="reflexion-2-1-f" rows="2" style="width:100%;font:inherit;padding:12px;border-radius:12px;border:2px solid var(--l)"></textarea></p>'),
        ]),
    ],
    'conecta': [('asistentes-de-chat', 'ChatGPT, Claude, Gemini y Copilot'), ('que-es-un-prompt', 'Qué es un «prompt»')],
}
