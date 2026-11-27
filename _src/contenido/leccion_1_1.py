# Lección 1.1 · Qué es y qué no es la IA
# Versión Fácil: BORRADOR pendiente de validar con personas usuarias de Euexia.
# Formato de cada paso: lista de bloques (tipo, normal, facil). Las palabras del glosario se
# escriben como [[palabra|definición]].

LECCION = {
    'id': 'que-es-y-que-no-es',
    'modulo': 1,
    'num': '1.1',
    'titulo': 'Qué es y qué no es la IA',
    'minutos': 25,
    'descripcion': 'Qué es la inteligencia artificial, explicado sin tecnicismos: qué hace, qué no hace y por qué no es un robot que piensa. Lección 1.1 del curso gratis IA sin miedo.',
    'validada': True,
    'pasos': [
        ('Situación', [
            ('texto',
             '<p>Carmen tiene una tienda de ropa en el pueblo. Su sobrino le dice: «Tita, pregúntaselo a la IA, que te hace el cartel de las rebajas en un minuto».</p>'
             '<p>Carmen no se fía. Se imagina un robot que lo sabe todo, que la escucha por el móvil y que el día menos pensado le quita el trabajo. Así que dice que no.</p>'
             '<p>¿Tiene razón Carmen? En esta lección vas a ver qué hay de verdad y qué hay de película en lo que pensamos sobre la IA.</p>',
             '<p>Carmen tiene una tienda de ropa.</p>'
             '<p>Su sobrino le dice: «Usa la IA para hacer un cartel».</p>'
             '<p>Carmen tiene miedo. Piensa que la IA es un robot que lo sabe todo.</p>'
             '<p>En esta lección vas a ver si Carmen tiene razón.</p>'),
        ]),
        ('Descubre', [
            ('lab', {
                'tipo': 'verdad-o-mito', 'id': 'que-es-y-que-no-es-mitos', 'titulo': 'Mitos de la IA',
                'intro': '<p>Antes de leer la explicación, pon a prueba lo que ya piensas. Ocho frases que se oyen mucho sobre la IA: ¿verdad o mito? Después de cada una te contamos por qué.</p>',
                'intro_f': '<p>Lee cada frase. ¿Es verdad o es mentira? Después te explicamos por qué.</p>',
                'etiquetas': {'si': 'Verdad', 'no': 'Mito'},
                'cartas': [
                    {'t': 'La IA piensa y siente como una persona.', 'v': False, 'f': True,
                     'x': 'Escribe con mucha educación, pero no piensa ni siente: calcula qué palabras encajan mejor según los ejemplos que vio.',
                     'xf': 'Es un mito. La IA no siente. Solo calcula palabras.'},
                    {'t': 'Una IA puede equivocarse aunque conteste muy segura.', 'tf': 'La IA se puede equivocar.', 'v': True, 'f': True,
                     'x': 'Suena igual de segura cuando acierta que cuando se inventa algo. Fechas, precios y leyes, compruébalos siempre.',
                     'xf': 'Es verdad. A veces se inventa cosas. Compruébalas.'},
                    {'t': 'Ya usas IA en tu móvil, aunque no la veas.', 'tf': 'Ya usas IA en tu móvil.', 'v': True, 'f': True,
                     'x': 'El teclado que adivina palabras, el mapa que avisa de atascos o la carpeta de spam funcionan con IA.',
                     'xf': 'Es verdad. El teclado y el mapa del móvil usan IA.'},
                    {'t': 'Si una IA lo dice, es que es verdad.', 'v': False, 'f': True,
                     'x': 'No busca la verdad: escribe lo más probable. Lo importante se comprueba en una fuente fiable.',
                     'xf': 'Es un mito. La IA se puede equivocar.'},
                    {'t': 'La IA aprende viendo muchísimos ejemplos.', 'v': True,
                     'x': 'Encuentra patrones en millones de ejemplos. Lo verás en la próxima lección, con aceitunas.',
                     'xf': 'Es verdad. Aprende con ejemplos.'},
                    {'t': 'Para usar la IA hay que saber mucha informática.', 'v': False,
                     'x': 'Si sabes escribir un WhatsApp, sabes hablar con un chat de IA. Lo que hay que aprender es a pedir bien, y eso se aprende aquí.',
                     'xf': 'Es un mito. Si sabes usar WhatsApp, puedes usar la IA.'},
                    {'t': 'Si le pides mal las cosas, te contesta mal.', 'v': True,
                     'x': 'No es magia: cuanto más claro le digas quién eres, qué quieres y para qué, mejor te contesta.',
                     'xf': 'Es verdad. Pide las cosas con claridad.'},
                    {'t': 'La IA decide por ti y no puedes hacer nada.', 'tf': 'La IA decide por ti.', 'v': False, 'f': True,
                     'x': 'Te da propuestas. Lo que haces con ellas lo decides tú: revisarlas, cambiarlas o no usarlas.',
                     'xf': 'Es un mito. Tú decides.'},
                ]}),
            ('info',
             '<h3>La idea clave</h3>'
             '<p>Una inteligencia artificial es un programa de ordenador que ha visto millones de ejemplos y ha aprendido a encontrar [[patrones|Cosas que se repiten. Por ejemplo: después de «buenos» suele venir «días».]] en ellos. Con esos patrones hace cosas que parecen inteligentes: contestar preguntas, escribir un texto, reconocer una cara o recomendarte una canción.</p>'
             '<p>Cuando le escribes a un chat de IA, no busca la respuesta en un libro ni «piensa» como tú. Calcula qué palabras tienen más probabilidad de ir detrás de las tuyas, una a una. Por eso escribe muy bien… y por eso a veces se inventa cosas con total seguridad.</p>',
             '<h3>La idea clave</h3>'
             '<p>La inteligencia artificial es un programa de ordenador.</p>'
             '<p>Ha visto muchísimos ejemplos. Así aprende a hacer cosas.</p>'
             '<p>Por ejemplo: escribir un texto, contestar preguntas o reconocer una cara.</p>'
             '<p>La IA no piensa como una persona. A veces se equivoca.</p>'),
            ('dos',
             '<h3>Lo que SÍ es</h3><ul class="lista-ok"><li>Un programa que aprende de ejemplos.</li><li>Muy rápida escribiendo, resumiendo y ordenando información.</li><li>Una ayuda: tú decides qué haces con lo que te da.</li><li>Algo que ya está en tu móvil, tus mapas y tu correo.</li></ul>'
             '<h3>Lo que NO es</h3><ul><li>No es una persona ni tiene sentimientos, aunque hable con mucha educación.</li><li>No sabe si lo que dice es verdad: hay que comprobarlo.</li><li>No es un robot de película que decide solo.</li><li>No es magia: si le pides mal, te contesta mal.</li></ul>',
             '<h3>La IA SÍ es</h3><ul class="lista-ok"><li>Un programa que aprende.</li><li>Una ayuda rápida.</li><li>Algo que ya usas en el móvil.</li></ul>'
             '<h3>La IA NO es</h3><ul><li>No es una persona.</li><li>No siempre dice la verdad.</li><li>No es magia.</li></ul>'),
        ]),
        ('Prueba', [
            ('tarea',
             '<h3>Tarea guiada · 10 minutos</h3>'
             '<ol><li>Abre en tu móvil o en el ordenador un chat de IA gratis: ChatGPT, Gemini, Claude o Copilot. Cualquiera vale.</li>'
             '<li>Escribe: <q>Explícame qué eres en 3 frases, como si yo tuviera 10 años.</q></li>'
             '<li>Después escribe: <q>¿Te puedes equivocar? Dame un ejemplo.</q></li>'
             '<li>Lee las dos respuestas. ¿Te ha dicho que es una persona? ¿Ha reconocido que se equivoca?</li></ol>'
             '<p>Si no quieres usar ninguna todavía, no pasa nada: pídele a alguien de tu casa que lo haga contigo.</p>',
             '<h3>Tarea · 10 minutos</h3>'
             '<ol><li>Abre un chat de IA en el móvil. Por ejemplo: ChatGPT o Gemini.</li>'
             '<li>Escribe: <q>Explícame qué eres en 3 frases fáciles.</q></li>'
             '<li>Escribe: <q>¿Te puedes equivocar?</q></li>'
             '<li>Lee lo que contesta.</li></ol>'
             '<p>Puedes hacerlo con alguien de tu familia.</p>'),
        ]),
        ('Conecta', [
            ('texto',
             '<p>Saber qué es la IA cambia cómo la usas en tres sitios:</p>'
             '<ul><li><b>En el trabajo:</b> te puede ayudar a escribir un aviso para tus clientes, pero tú revisas que los precios y el horario estén bien.</li>'
             '<li><b>En casa:</b> te puede explicar con palabras sencillas una carta del banco o de la Seguridad Social. No le des tus números de cuenta ni tu DNI.</li>'
             '<li><b>En el pueblo:</b> puede hacer en un minuto el cartel de la fiesta o de la asociación. Las fechas, compruébalas tú.</li></ul>',
             '<ul><li><b>En el trabajo:</b> la IA te ayuda a escribir avisos. Tú revisas los precios.</li>'
             '<li><b>En casa:</b> la IA te explica una carta difícil. No le des tu DNI.</li>'
             '<li><b>En el pueblo:</b> la IA hace carteles. Tú revisas las fechas.</li></ul>'),
        ]),
        ('Comparte', [
            ('texto',
             '<p>Cuéntale a alguien de tu entorno, en una frase, <b>una cosa que la IA es</b> y <b>una cosa que no es</b>. Explicarlo es la mejor forma de comprobar que lo has entendido.</p>'
             '<p>Si quieres, mándanos tu frase por WhatsApp y la comentamos.</p>',
             '<p>Cuéntale a una persona:</p><ul><li>Una cosa que la IA sí es.</li><li>Una cosa que la IA no es.</li></ul>'),
            ('lab', {
                'tipo': 'explicaselo', 'id': 'que-es-y-que-no-es-explica', 'titulo': 'Explícaselo a…', 'tema': 'qué es la IA',
                'intro': '<p>Elige a quién se lo cuentas y rellena los huecos con tus palabras. Después, mándaselo por WhatsApp o cópialo.</p>',
                'intro_f': '<p>Elige a una persona. Escribe con tus palabras. Mándalo por WhatsApp.</p>',
                'huecos': [
                    {'l': 'Qué es la IA, en una frase', 'lf': 'La IA es…', 'ph': 'un programa que aprende de muchísimos ejemplos'},
                    {'l': 'Un sitio donde ya la usas', 'lf': 'Un ejemplo', 'ph': 'el teclado del móvil, que adivina palabras'},
                    {'l': 'Una cosa que no es, o un consejo', 'lf': 'Un consejo', 'ph': 'no es una persona y a veces se equivoca, así que lo importante se comprueba'},
                ]}),
        ]),
        ('Piensa', [
            ('quiz', [
                ('Cuando un chat de IA te contesta, ¿qué está haciendo?',
                 [('Calcula qué palabras encajan mejor detrás de las tuyas', True, False),
                  ('Busca la respuesta en una enciclopedia', False, False),
                  ('Piensa y siente como una persona', False, True),
                  ('Pregunta a una persona que hay detrás', False, True)],
                 'Calcula, palabra a palabra, lo más probable según los ejemplos que ha visto. Por eso escribe bien, pero no sabe si lo que dice es verdad.',
                 'La IA calcula palabras. No sabe si es verdad.'),
                ('¿Puede una IA equivocarse aunque conteste muy segura?',
                 [('No, si contesta segura es que es verdad', False, False),
                  ('Sí, y por eso hay que comprobar lo importante', True, False),
                  ('Solo si es de pago', False, True),
                  ('Solo en inglés', False, True)],
                 'Sí. La IA puede inventarse datos con mucha seguridad. Fechas, precios, leyes y nombres, compruébalos siempre.',
                 'Sí. A veces se inventa cosas. Compruébalas.'),
                ('¿Cuál de estas cosas NO es la IA?',
                 [('Un programa que aprende de ejemplos', False, False),
                  ('Algo que ya está en tu móvil', False, True),
                  ('Una persona con sentimientos', True, False),
                  ('Una ayuda para escribir textos', False, True)],
                 'La IA puede hablar con mucha educación, pero no es una persona ni tiene sentimientos.',
                 'La IA no es una persona. No tiene sentimientos.'),
            ]),
            ('texto',
             '<p><label for="reflexion"><b>Tu reflexión en una línea:</b> ¿qué te ha sorprendido de esta lección?</label></p>'
             '<p><textarea id="reflexion" rows="2" style="width:100%;font:inherit;padding:12px;border-radius:12px;border:2px solid var(--l)"></textarea></p>'
             '<p style="font-size:.9rem;color:var(--m)">Lo que escribas aquí no se guarda ni se envía a ningún sitio.</p>',
             '<p><label for="reflexion-f"><b>Escribe una frase:</b> ¿qué has aprendido hoy?</label></p>'
             '<p><textarea id="reflexion-f" rows="2" style="width:100%;font:inherit;padding:12px;border-radius:12px;border:2px solid var(--l)"></textarea></p>'),
        ]),
    ],
    'conecta': [('como-aprende', 'Cómo «aprende» una IA'), ('errores-e-invenciones', 'Errores e invenciones')],
}
