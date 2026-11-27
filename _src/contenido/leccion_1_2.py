# Lección 1.2 · Cómo «aprende» una IA
# Versión Fácil: BORRADOR pendiente de validar con personas usuarias de Euexia.
# Formato de cada paso: lista de bloques (tipo, normal, facil). Las palabras del glosario se
# escriben como [[palabra|definición]].

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
        ]),
        ('Piensa', [
            ('quiz', [
                ('¿Cómo aprende una IA a hacer una tarea?',
                 [('Alguien le escribe todas las reglas una a una', False, False),
                  ('Viendo muchísimos ejemplos y ajustando sus cálculos', True, False),
                  ('Leyendo un libro de instrucciones', False, True),
                  ('Copiando lo que piensa la persona que la usa', False, True)],
                 'Una IA se entrena con muchísimos ejemplos. No le escriben las reglas: las encuentra ella sola, como Dani con las aceitunas.'),
                ('¿Qué pasa si una IA aprende con ejemplos malos o poco variados?',
                 [('Que aprende mal y se equivoca más', True, False),
                  ('Nada, la IA corrige sola los ejemplos malos', False, False),
                  ('Que deja de funcionar del todo', False, True),
                  ('Que avisa siempre de que no sabe', False, True)],
                 'La IA es tan buena como sus ejemplos. Si los ejemplos están torcidos, lo que aprende también. A eso se le llama sesgo.'),
                ('¿Por qué una IA puede fallar con cosas de tu pueblo?',
                 [('Porque no le caen bien los pueblos', False, False),
                  ('Porque ha visto muy pocos ejemplos sobre tu pueblo', True, False),
                  ('Porque solo funciona en las ciudades', False, True),
                  ('Porque necesita que vayas a enseñárselo en persona', False, True)],
                 'Sobre lo que casi no ha visto, la IA acierta menos. Las fechas de las fiestas, las calles o las costumbres, compruébalas tú.'),
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
