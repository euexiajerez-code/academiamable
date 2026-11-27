# Lección 1.2 · Cómo «aprende» una IA
# Versión Fácil: BORRADOR pendiente de validar con personas usuarias de Euexia.
# Formato de cada paso: lista de bloques (tipo, normal, facil). Las palabras del glosario se
# escriben como [[palabra|definición]].

from corpus_frases import FRASES, SEMILLAS, SEMILLAS_F

LECCION = {
    'id': 'como-aprende',
    'modulo': 1,
    'num': '1.2',
    'titulo': 'Cómo «aprende» una IA',
    'minutos': 25,
    'descripcion': 'Cómo aprende una inteligencia artificial: con ejemplos, no con reglas, y por qué a veces aprende mal. Lección 1.2 del curso gratis IA sin miedo, desde cero.',
    'validada': True,
    'pasos': [
        ('Situación', [
            ('texto',
             '<p>Antonio tiene olivos en Valle de Matamoros. Este otoño su nieto Dani le ayuda a separar la aceituna picada de la sana. Antonio no le da ninguna regla: le enseña una, luego otra, luego cien. «Esta sí, esta no». A media mañana, Dani ya no falla ni una.</p>'
             '<p>Por la tarde, Dani le dice a su abuelo: «Pues así aprende la IA, abuelo. Igualito que yo con las aceitunas». Antonio se ríe: «Anda ya. Un ordenador no aprende, hace lo que le mandan».</p>'
             '<p>¿Quién tiene razón? En esta lección vas a ver qué quiere decir que una máquina «aprende».</p>',
             '<p>Antonio tiene olivos.</p>'
             '<p>Su nieto Dani le ayuda a separar las aceitunas buenas de las malas.</p>'
             '<p>Antonio le enseña muchas aceitunas. Al final, Dani no se equivoca.</p>'
             '<p>Dani dice: «La IA aprende igual que yo».</p>'
             '<p>En esta lección vas a ver si Dani tiene razón.</p>'),
        ]),
        ('Descubre', [
            ('lab', {
                'tipo': 'ensena-a-la-maquina', 'id': 'como-aprende-maquina', 'titulo': 'Enséñale a una máquina a detectar estafas',
                'intro': '<p>Como Antonio con las aceitunas: no le das reglas, le das ejemplos. Etiqueta los mensajes como «estafa» o «normal» y mira qué va aprendiendo la máquina. Después, ponla a prueba con mensajes que nunca ha visto. Y si quieres ver qué es el sesgo, enséñale mal a propósito.</p>',
                'intro_f': '<p>Vas a enseñar a una máquina. Di si cada mensaje es una estafa o es normal. Después, la máquina adivina mensajes nuevos.</p>',
                'clases': [{'id': 'estafa', 't': 'Estafa'}, {'id': 'normal', 't': 'Normal'}],
                'ejemplos': [
                    {'t': 'Su cuenta del banco está bloqueada. Pinche en este enlace y escriba su clave.', 'c': 'estafa', 'f': True,
                     'x': 'pide pinchar en un enlace y dar la clave del banco. Tu banco nunca te pide la clave por mensaje.', 'xf': 'pide tu clave del banco. Es una estafa.'},
                    {'t': 'Hola, soy Juani. ¿Me guardas dos barras de pan para mañana?', 'c': 'normal', 'f': True,
                     'x': 'es un encargo de una vecina, sin enlaces, sin prisas y sin dinero.', 'xf': 'es un encargo normal.'},
                    {'t': '¡Enhorabuena! Ha ganado un premio de 1.000 euros. Pinche aquí para cobrarlo.', 'c': 'estafa', 'f': True,
                     'x': 'nadie regala premios por sorpresa: es un cebo para que pinches.', 'xf': 'nadie regala premios. Es una estafa.'},
                    {'t': 'Recuerda que la reunión de la asociación es el jueves a las seis.', 'c': 'normal', 'f': True,
                     'x': 'es un aviso que no te pide nada.', 'xf': 'es un aviso normal.'},
                    {'t': 'Correos: su paquete está retenido. Pague 1,99 euros en este enlace.', 'c': 'estafa', 'f': True,
                     'x': 'es una estafa muy común: un enlace y un pago pequeño para quedarse con los datos de tu tarjeta.', 'xf': 'pide dinero con un enlace. Es una estafa.'},
                    {'t': 'Tu cita en el centro de salud es el martes a las diez. Si no puedes ir, llama al centro.', 'c': 'normal', 'f': True,
                     'x': 'te recuerda una cita y te dice que llames tú. No pide datos ni que pinches nada.', 'xf': 'es un aviso del centro de salud.'},
                    {'t': 'Hola mamá, se me ha roto el móvil. Este es mi número nuevo. ¿Me haces un bizum urgente?', 'c': 'estafa',
                     'x': 'es la estafa del «hijo en apuros»: número nuevo, prisas y dinero. Llama tú al número de siempre.'},
                    {'t': 'El pedido de aceite ya está listo. Pásate cuando quieras por la tienda.', 'c': 'normal',
                     'x': 'es el aviso de una tienda: no pide dinero ni datos.'},
                ],
                'pruebas': [
                    {'t': 'Urgente: su tarjeta del banco ha sido bloqueada. Pinche en el enlace.', 'c': 'estafa', 'f': True},
                    {'t': '¿Te guardo el pan de siempre para el sábado?', 'c': 'normal', 'f': True},
                    {'t': 'Ha ganado un móvil nuevo. Pague el envío aquí.', 'c': 'estafa', 'f': True},
                    {'t': 'Mañana es la reunión de la asociación en el hogar.', 'c': 'normal'},
                    {'t': 'Hola mamá, este es mi número nuevo. Escríbeme cuando puedas.', 'c': 'estafa'},
                ]}),
            ('info',
             '<h3>La idea clave</h3>'
             '<p>Un programa normal sigue reglas que alguien escribe una a una: «si pasa esto, haz aquello». Una IA no funciona así. A una IA se la [[entrena|Se le enseñan muchísimos ejemplos para que aprenda a hacer una tarea.]]: se le enseñan muchísimos ejemplos y ella sola va ajustando sus cálculos hasta acertar casi siempre. Como Dani con las aceitunas.</p>'
             '<p>Por eso una IA es tan buena como los ejemplos que ha visto. Si los ejemplos están mal, o son todos parecidos, aprende mal. Si casi nunca ha visto nada de tu pueblo, de tu oficio o de tu forma de hablar, se equivocará más con esas cosas. A eso se le llama [[sesgo|Cuando la IA aprende una idea torcida porque los ejemplos que vio no eran variados o estaban mal.]].</p>'
             '<p>Y un detalle importante: la IA no «entiende» por qué una aceituna está picada. Solo ha aprendido a reconocer cómo suele ser. Dani, en cambio, sabe que es por la mosca.</p>',
             '<h3>La idea clave</h3>'
             '<p>Un programa normal sigue unas reglas.</p>'
             '<p>La IA es diferente. La IA aprende con ejemplos.</p>'
             '<p>Ve muchísimos ejemplos. Así aprende a acertar.</p>'
             '<p>Si los ejemplos están mal, la IA aprende mal.</p>'
             '<p>Si la IA conoce pocas cosas de tu pueblo, se equivoca más.</p>'),
            ('dos',
             '<h3>Un programa normal</h3><ul><li>Alguien le escribe todas las reglas.</li><li>Hace siempre lo mismo.</li><li>Si algo no está en sus reglas, no sabe qué hacer.</li><li>Ejemplo: la calculadora.</li></ul>'
             '<h3>Una IA</h3><ul class="lista-ok"><li>Aprende viendo muchísimos ejemplos.</li><li>Encuentra parecidos que nadie le ha explicado.</li><li>Se atreve con casos nuevos, aunque a veces falla.</li><li>Ejemplo: el teclado del móvil que adivina tu siguiente palabra.</li></ul>',
             '<h3>Programa normal</h3><ul><li>Sigue reglas.</li><li>Hace siempre lo mismo.</li><li>Ejemplo: la calculadora.</li></ul>'
             '<h3>IA</h3><ul class="lista-ok"><li>Aprende con ejemplos.</li><li>A veces se equivoca.</li><li>Ejemplo: el teclado del móvil.</li></ul>'),
        ]),
        ('Prueba', [
            ('lab', {
                'tipo': 'siguiente-palabra', 'id': 'como-aprende-palabra', 'titulo': 'Escribe como una IA',
                'intro': '<p>Este laboratorio ha «leído» unas doscientas frases de pueblo, de bar y de tienda. Escribe el principio de una frase y mira qué palabras cree que vienen detrás, y con qué probabilidad. Pulsa una barra, o «Añadir la más probable» varias veces, y estarás escribiendo como un chat de IA. Después, haz lo mismo con el teclado de tu móvil.</p>',
                'intro_f': '<p>Escribe el principio de una frase. Mira qué palabras pueden ir detrás. Pulsa una para ponerla.</p>',
                'corpus': FRASES, 'semillas': SEMILLAS, 'semillas_f': SEMILLAS_F}),
            ('tarea',
             '<h3>Tarea guiada · 10 minutos</h3>'
             '<ol><li>Abre WhatsApp o las notas del móvil y escribe: <q>Mañana voy a</q>. No sigas escribiendo.</li>'
             '<li>Mira las palabras que te propone el teclado encima de las letras. Pulsa la del medio cinco veces seguidas. ¿Qué frase sale?</li>'
             '<li>Pídele a alguien de tu casa que haga lo mismo en su móvil. ¿Os sale la misma frase? Seguramente no: cada teclado ha aprendido de lo que escribe su dueño.</li>'
             '<li>Si quieres ir un paso más allá, abre un chat de IA gratis (ChatGPT, Gemini, Claude o Copilot) y escribe: <q>Explícame cómo aprendiste lo que sabes, con un ejemplo de aceitunas y en 4 frases.</q></li></ol>'
             '<p>Si no quieres usar ninguna IA todavía, juega a «aprender con ejemplos»: enséñale a alguien diez objetos de casa diciendo solo «este sí» o «este no», sin explicar la regla. ¿Cuántos ejemplos necesita para adivinarla?</p>',
             '<h3>Tarea · 10 minutos</h3>'
             '<ol><li>Abre WhatsApp en el móvil.</li>'
             '<li>Escribe: <q>Mañana voy a</q>.</li>'
             '<li>Mira las palabras que salen encima de las letras.</li>'
             '<li>Pulsa la palabra del medio 5 veces.</li>'
             '<li>Lee la frase. El teclado aprende de lo que tú escribes.</li></ol>'
             '<p>Puedes hacerlo con alguien de tu familia.</p>'),
        ]),
        ('Conecta', [
            ('texto',
             '<p>Saber que la IA aprende de ejemplos te ayuda a usarla mejor:</p>'
             '<ul><li><b>En el trabajo:</b> si le pides un texto sobre tu oficio, dale ejemplos tuyos (un aviso que ya usaste, cómo hablas con tus clientes). Cuantos mejores ejemplos le das, mejor te contesta.</li>'
             '<li><b>En casa:</b> el móvil aprende de lo que haces. Por eso conviene revisar de vez en cuando qué permisos tienen las aplicaciones, como el micrófono o la ubicación.</li>'
             '<li><b>En el pueblo o la asociación:</b> la IA sabe poco de las fiestas, los nombres de calles o las costumbres de un pueblo pequeño. Ahí el que sabe eres tú: revisa siempre esos datos.</li></ul>',
             '<ul><li><b>En el trabajo:</b> dale ejemplos a la IA. Así te ayuda mejor.</li>'
             '<li><b>En casa:</b> el móvil aprende de ti. Revisa qué permisos tiene.</li>'
             '<li><b>En el pueblo:</b> la IA sabe poco de tu pueblo. Tú revisas los datos.</li></ul>'),
        ]),
        ('Comparte', [
            ('texto',
             '<p>Busca a alguien de tu entorno y explícale, con un ejemplo de tu vida (como las aceitunas de Antonio), cómo aprende una IA. Puede ser cocinar, conducir o aprender un juego de cartas: todos aprendimos viendo muchas veces.</p>'
             '<p>Si quieres, mándanos tu ejemplo por WhatsApp y lo comentamos.</p>',
             '<p>Cuéntale a una persona cómo aprende la IA.</p><ul><li>Usa un ejemplo de tu vida.</li><li>Por ejemplo: cómo aprendiste a cocinar.</li></ul>'),
            ('lab', {
                'tipo': 'explicaselo', 'id': 'como-aprende-explica', 'titulo': 'Explícaselo a…', 'tema': 'cómo aprende una IA',
                'intro': '<p>Elige a quién se lo cuentas y rellena los huecos con tus palabras. Después, mándaselo por WhatsApp o cópialo.</p>',
                'intro_f': '<p>Elige a una persona. Escribe con tus palabras. Mándalo por WhatsApp.</p>',
                'huecos': [
                    {'l': 'Cómo aprende, en una frase', 'lf': 'La IA aprende…', 'ph': 'viendo muchísimos ejemplos, no con reglas'},
                    {'l': 'Un ejemplo de tu vida', 'lf': 'Un ejemplo', 'ph': 'como Dani, que aprendió a separar las aceitunas viendo muchas'},
                    {'l': 'Un cuidado', 'lf': 'Un cuidado', 'ph': 'si los ejemplos están mal, aprende mal'},
                ]}),
        ]),
        ('Piensa', [
            ('quiz', [
                ('¿Cómo aprende una IA a hacer una tarea?',
                 [('Alguien le escribe todas las reglas una a una', False, False),
                  ('Viendo muchísimos ejemplos y ajustando sus cálculos', True, False),
                  ('Leyendo un libro de instrucciones', False, True),
                  ('Copiando lo que piensa la persona que la usa', False, True)],
                 'Una IA se entrena con muchísimos ejemplos. No le escriben las reglas: las encuentra ella sola, como Dani con las aceitunas.',
                 'La IA aprende viendo muchos ejemplos.'),
                ('¿Qué pasa si una IA aprende con ejemplos malos o poco variados?',
                 [('Que aprende mal y se equivoca más', True, False),
                  ('Nada, la IA corrige sola los ejemplos malos', False, False),
                  ('Que deja de funcionar del todo', False, True),
                  ('Que avisa siempre de que no sabe', False, True)],
                 'La IA es tan buena como sus ejemplos. Si los ejemplos están torcidos, lo que aprende también. A eso se le llama sesgo.',
                 'Si los ejemplos están mal, la IA aprende mal.'),
                ('¿Por qué una IA puede fallar con cosas de tu pueblo?',
                 [('Porque no le caen bien los pueblos', False, False),
                  ('Porque ha visto muy pocos ejemplos sobre tu pueblo', True, False),
                  ('Porque solo funciona en las ciudades', False, True),
                  ('Porque necesita que vayas a enseñárselo en persona', False, True)],
                 'Sobre lo que casi no ha visto, la IA acierta menos. Las fechas de las fiestas, las calles o las costumbres, compruébalas tú.',
                 'La IA sabe poco de tu pueblo. Tú revisas los datos.'),
            ]),
            ('texto',
             '<p><label for="reflexion-1-2"><b>Tu reflexión en una línea:</b> ¿qué has aprendido tú «a base de ejemplos», como la IA?</label></p>'
             '<p><textarea id="reflexion-1-2" rows="2" style="width:100%;font:inherit;padding:12px;border-radius:12px;border:2px solid var(--l)"></textarea></p>'
             '<p style="font-size:.9rem;color:var(--m)">Lo que escribas aquí no se guarda ni se envía a ningún sitio.</p>',
             '<p><label for="reflexion-1-2-f"><b>Escribe una frase:</b> ¿qué has aprendido hoy?</label></p>'
             '<p><textarea id="reflexion-1-2-f" rows="2" style="width:100%;font:inherit;padding:12px;border-radius:12px;border:2px solid var(--l)"></textarea></p>'),
        ]),
    ],
    'conecta': [('ia-que-ya-usas', 'La IA que ya usas sin saberlo'), ('errores-e-invenciones', 'Errores e invenciones')],
}
