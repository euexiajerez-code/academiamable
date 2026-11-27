# Lección 1.3 · La IA que ya usas sin saberlo
# Versión Fácil: BORRADOR pendiente de validar con personas usuarias de Euexia.
# Formato de cada paso: lista de bloques (tipo, normal, facil). Las palabras del glosario se
# escriben como [[palabra|definición]].

LECCION = {
    'id': 'ia-que-ya-usas',
    'modulo': 1,
    'num': '1.3',
    'titulo': 'La IA que ya usas sin saberlo',
    'minutos': 20,
    'descripcion': 'La IA que ya usas sin saberlo: en el móvil, los mapas, el correo y la tele. Descubre dónde está y cuida tus datos. Lección 1.3 del curso gratis IA sin miedo.',
    'validada': False,
    'pasos': [
        ('Situación', [
            ('texto',
             '<p>Remedios está jubilada y vive en Oliva de la Frontera. En la merienda del hogar del pensionista sale el tema de la inteligencia artificial y ella lo tiene claro: «Yo de eso no uso nada, hija. Yo con mi WhatsApp tengo bastante».</p>'
             '<p>Esa misma mañana, Remedios le ha dicho al móvil «llamar a mi hija» y la ha llamado. Ha mandado un audio que el móvil ha pasado a texto. Y para ir al médico a Badajoz ha mirado en el mapa por dónde había menos tráfico.</p>'
             '<p>Sin saberlo, Remedios ha usado la IA tres veces antes de comer. Y tú, seguramente, también.</p>',
             '<p>Remedios está jubilada.</p>'
             '<p>Remedios dice: «Yo no uso la IA».</p>'
             '<p>Pero esta mañana habló al móvil para llamar a su hija.</p>'
             '<p>También usó el mapa del móvil para ir al médico.</p>'
             '<p>Remedios usa la IA y no lo sabe.</p>'),
        ]),
        ('Descubre', [
            ('info',
             '<h3>La idea clave</h3>'
             '<p>La IA no está solo en los chats de los que habla todo el mundo. Lleva años escondida dentro de cosas que usas a diario: el mapa que te avisa de un atasco, el correo que manda la publicidad pesada al [[filtro de spam|Carpeta del correo donde van solos los mensajes de publicidad o de estafa.]], el teclado que te corrige las palabras o la tele que te dice «esto te puede gustar».</p>'
             '<p>Todas hacen lo mismo que vimos en la lección anterior: han aprendido de muchísimos ejemplos. Y muchas siguen aprendiendo de ti, de lo que buscas, lo que ves y por dónde vas. Por eso te hacen [[recomendaciones|Sugerencias que te hace una aplicación según lo que has visto o comprado antes.]] que aciertan tanto… y por eso conviene saber qué datos tuyos están usando.</p>',
             '<h3>La idea clave</h3>'
             '<p>La IA está en muchas cosas que usas cada día.</p>'
             '<p>Por ejemplo: en el mapa del móvil, en el correo o en la tele.</p>'
             '<p>Estas cosas aprenden de lo que tú haces.</p>'
             '<p>Por eso es importante cuidar tus datos.</p>'),
            ('dos',
             '<h3>Dónde está</h3><ul class="lista-ok"><li>Google Maps y otros mapas: te dicen por dónde ir y cuánto vas a tardar.</li><li>El correo: separa el spam de los mensajes buenos.</li><li>El teclado del móvil: corrige y adivina palabras.</li><li>El dictado y los audios: pasan tu voz a texto.</li><li>Spotify, Netflix o YouTube: te recomiendan qué escuchar o ver.</li><li>La galería de fotos: encuentra tus fotos si buscas «perro» o «playa».</li></ul>'
             '<h3>Qué conviene vigilar</h3><ul><li>Qué aplicaciones pueden usar tu micrófono y tu ubicación.</li><li>Que las recomendaciones te enseñan más de lo mismo, no lo mejor.</li><li>Que el corrector también se equivoca: lee antes de enviar.</li><li>Que el mapa no conoce el camino de tierra que está cortado: tú sí.</li></ul>',
             '<h3>Dónde está la IA</h3><ul class="lista-ok"><li>En el mapa del móvil.</li><li>En el correo.</li><li>En el teclado del móvil.</li><li>En las series y la música que te recomiendan.</li></ul>'
             '<h3>Ten cuidado con</h3><ul><li>Los permisos del móvil.</li><li>Los errores del corrector.</li></ul>'),
        ]),
        ('Prueba', [
            ('tarea',
             '<h3>Tarea guiada · 10 minutos</h3>'
             '<p>Vas a ser detective de la IA en tu propio móvil. Apunta en un papel o en las notas del móvil cada sitio donde la encuentres:</p>'
             '<ol><li>Abre la galería de fotos y busca una palabra, por ejemplo <q>perro</q>, <q>coche</q> o <q>tarta</q>. ¿Te encuentra las fotos sin que les hayas puesto nombre?</li>'
             '<li>Abre WhatsApp, pulsa el micrófono del teclado (no el de los audios) y dicta una frase. ¿La ha escrito bien?</li>'
             '<li>Abre el mapa y busca cómo ir al pueblo de al lado. ¿Te dice cuánto vas a tardar?</li>'
             '<li>Mira la carpeta de spam de tu correo. ¿Qué tipo de mensajes ha apartado?</li>'
             '<li>Entra en los ajustes del móvil, busca «Permisos» y mira qué aplicaciones pueden usar tu micrófono. ¿Hay alguna que no te cuadre?</li></ol>'
             '<p>Esta tarea no necesita ningún chat de IA. Si algún paso no te sale, pídele a alguien de casa que lo haga contigo. Al final, intenta tener 5 sitios apuntados: es la tarea de este módulo.</p>',
             '<h3>Tarea · 10 minutos</h3>'
             '<p>Busca la IA en tu móvil. Apunta lo que encuentres.</p>'
             '<ol><li>Abre tus fotos. Busca la palabra <q>perro</q>.</li>'
             '<li>Abre WhatsApp. Pulsa el micrófono del teclado. Di una frase.</li>'
             '<li>Abre el mapa. Busca el pueblo de al lado.</li>'
             '<li>Apunta 5 sitios donde hay IA.</li></ol>'
             '<p>Puedes hacerlo con alguien de tu familia.</p>'),
        ]),
        ('Conecta', [
            ('texto',
             '<p>Ahora que sabes dónde está la IA, puedes sacarle partido con cabeza:</p>'
             '<ul><li><b>En el trabajo:</b> dictar en vez de escribir te ahorra tiempo con los mensajes a clientes o proveedores. Eso sí, léelo antes de enviarlo, que el dictado a veces entiende «vaca» por «baca».</li>'
             '<li><b>En casa:</b> revisa una vez al año qué aplicaciones usan tu micrófono, tu cámara y tu ubicación. Si una linterna quiere tus contactos, algo raro pasa.</li>'
             '<li><b>En el pueblo o la asociación:</b> el mapa es muy útil para organizar una excursión, pero los caminos rurales, las fiestas con calles cortadas o la obra de la plaza los conoce mejor la gente del pueblo.</li></ul>',
             '<ul><li><b>En el trabajo:</b> puedes dictar mensajes al móvil. Léelos antes de enviar.</li>'
             '<li><b>En casa:</b> mira los permisos de tus aplicaciones.</li>'
             '<li><b>En el pueblo:</b> el mapa ayuda. Pero la gente del pueblo conoce mejor los caminos.</li></ul>'),
        ]),
        ('Comparte', [
            ('texto',
             '<p>Haz como Remedios, pero al revés: pregúntale a alguien de tu entorno si usa la IA. Si te dice que no, enséñale uno de los sitios que has encontrado en tu móvil. Seguro que se sorprende.</p>'
             '<p>Si quieres, mándanos por WhatsApp tu lista de 5 sitios y te la comentamos.</p>',
             '<p>Pregunta a una persona: «¿Usas la IA?».</p><ul><li>Enséñale un sitio de tu móvil donde hay IA.</li></ul>'),
        ]),
        ('Piensa', [
            ('quiz', [
                ('¿Cuál de estas cosas usa IA?',
                 [('La linterna del móvil', False, False),
                  ('El mapa que te avisa de un atasco', True, False),
                  ('El botón de subir el volumen', False, True),
                  ('El reloj de la pantalla', False, True)],
                 'El mapa ha aprendido de muchísimos viajes para calcular por dónde ir y cuánto vas a tardar. Eso es IA.'),
                ('¿Por qué Netflix o Spotify te recomiendan cosas que te gustan?',
                 [('Porque han aprendido de lo que tú has visto o escuchado antes', True, False),
                  ('Porque alguien de la empresa te conoce', False, False),
                  ('Porque es pura casualidad', False, True),
                  ('Porque te escuchan por el micrófono todo el día', False, True)],
                 'Aprenden de lo que ves y escuchas, y de lo que ven personas con gustos parecidos. Por eso aciertan, y por eso te enseñan más de lo mismo.'),
                ('¿Qué es buena idea hacer con los permisos del móvil?',
                 [('Revisar de vez en cuando qué aplicaciones usan el micrófono o la ubicación', True, False),
                  ('Darle todos los permisos a todas las aplicaciones', False, False),
                  ('No mirarlos nunca, que eso es cosa de informáticos', False, True),
                  ('Apagar el móvil cada noche para borrarlos', False, True)],
                 'Tú decides qué puede usar cada aplicación. Si una no necesita el micrófono o tu ubicación para funcionar, quítaselo.'),
            ]),
            ('texto',
             '<p><label for="reflexion-1-3"><b>Tu reflexión en una línea:</b> ¿en qué sitio de tu día a día no sabías que había IA?</label></p>'
             '<p><textarea id="reflexion-1-3" rows="2" style="width:100%;font:inherit;padding:12px;border-radius:12px;border:2px solid var(--l)"></textarea></p>'
             '<p style="font-size:.9rem;color:var(--m)">Lo que escribas aquí no se guarda ni se envía a ningún sitio.</p>',
             '<p><label for="reflexion-1-3-f"><b>Escribe una frase:</b> ¿dónde usas tú la IA?</label></p>'
             '<p><textarea id="reflexion-1-3-f" rows="2" style="width:100%;font:inherit;padding:12px;border-radius:12px;border:2px solid var(--l)"></textarea></p>'),
        ]),
    ],
    'conecta': [('ia-que-reconoce', 'IA que reconoce y clasifica'), ('en-casa-y-tramites', 'En casa y en trámites')],
}
