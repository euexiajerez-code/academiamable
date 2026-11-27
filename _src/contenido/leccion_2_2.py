# Lección 2.2 · IA que crea imágenes, vídeo y voz
# Versión Fácil: BORRADOR pendiente de validar con personas usuarias de Euexia.
# Formato de cada paso: lista de bloques (tipo, normal, facil). Las palabras del glosario se
# escriben como [[palabra|definición]].

LECCION = {
    'id': 'ia-que-crea',
    'modulo': 2,
    'num': '2.2',
    'titulo': 'IA que crea imágenes, vídeo y voz',
    'minutos': 25,
    'descripcion': 'IA que crea imágenes, vídeo y voz: qué puede hacer, cómo pedírselo y qué cuidar para no engañar ni engañarte. Lección 2.2 del curso gratis IA sin miedo.',
    'validada': True,
    'pasos': [
        ('Situación', [
            ('texto',
             '<p>Lucía tiene una peluquería en Burguillos del Cerro. Para el Día de la Madre quiere hacer una promoción y necesita un cartel bonito para el escaparate y para Instagram. Ha buscado fotos en internet, pero no sabe si se pueden usar y todas parecen de otra peluquería.</p>'
             '<p>Una clienta le cuenta que ella le pidió a una IA «una tarta de cumpleaños con forma de tractor» y le salió un dibujo precioso. Lucía lo prueba con su cartel. La primera imagen le encanta… hasta que se fija en que la peluquera del dibujo tiene seis dedos en una mano.</p>'
             '<p>En esta lección vas a ver qué puede crear la IA, además de texto, y qué conviene vigilar.</p>',
             '<p>Lucía tiene una peluquería.</p>'
             '<p>Quiere un cartel para el Día de la Madre.</p>'
             '<p>Le pide a la IA un dibujo para el cartel.</p>'
             '<p>El dibujo es bonito. Pero la peluquera del dibujo tiene 6 dedos.</p>'
             '<p>En esta lección vas a ver qué puede crear la IA.</p>'),
        ]),
        ('Descubre', [
            ('lab', {
                'tipo': 'clasifica', 'id': 'ia-que-crea-quecrea', 'titulo': '¿Qué IA crea qué?',
                'intro': '<p>No todo lo que crea la IA es texto. Pon cada encargo con el tipo de IA que lo haría: texto, imagen, voz o vídeo. El primero ya está hecho.</p>',
                'intro_f': '<p>¿Qué crea la IA en cada caso? ¿Texto, imagen, voz o vídeo?</p>',
                'categorias': [
                    {'id': 'texto', 't': 'Texto', 'd': 'Escribe', 'p': 'Pídeselo a un chat de IA: dile para quién es, cómo de largo y con qué tono.'},
                    {'id': 'imagen', 't': 'Imagen', 'd': 'Dibuja', 'p': 'Describe qué sale, los colores, el momento del día y el estilo. Y revisa manos y letras.'},
                    {'id': 'voz', 't': 'Voz', 'd': 'Habla o canta', 'p': 'Puede leer tus textos en voz alta. Nunca imites la voz de una persona real sin su permiso.'},
                    {'id': 'video', 't': 'Vídeo', 'd': 'Imágenes que se mueven', 'p': 'Es lo más nuevo y lo que más falla: empieza por algo cortito y sin personas reales.'}],
                'items': [
                    {'t': 'La carta de tapas traducida al portugués', 'c': 'texto', 'f': True, 'x': 'Escribir y traducir es cosa de la IA de texto, como en el bar de Paco.', 'xf': 'Es texto: escribe y traduce.'},
                    {'t': 'El dibujo de una tarta con forma de tractor', 'c': 'imagen', 'f': True, 'x': 'Una descripción que se convierte en dibujo: IA de imagen.', 'xf': 'Es una imagen: un dibujo.'},
                    {'t': 'El bando del ayuntamiento leído con una voz artificial', 'tf': 'Una voz que lee el bando', 'c': 'voz', 'f': True, 'x': 'Convierte un texto en voz hablada: IA de voz. Ayuda a quien no puede leer bien.', 'xf': 'Es voz: lee en voz alta.'},
                    {'t': 'Un anuncio de 10 segundos con el castillo en movimiento', 'tf': 'Un vídeo corto del castillo', 'c': 'video', 'f': True, 'x': 'Imágenes que se mueven, creadas de cero: IA de vídeo.', 'xf': 'Es vídeo: imágenes que se mueven.'},
                    {'t': 'El mensaje para invitar a la comida de la asociación', 'c': 'texto', 'x': 'Un mensaje escrito: IA de texto. Las fechas, compruébalas tú.'},
                    {'t': 'El cartel de la verbena con farolillos', 'c': 'imagen', 'x': 'Un dibujo para el cartel: IA de imagen. Si lleva letras, revisa que se lean.'},
                    {'t': 'Una cuña de radio para la feria con voz de locutor', 'c': 'voz', 'x': 'Una voz que lee o anuncia: IA de voz.'},
                    {'t': 'Convertir una foto de la plaza en un vídeo corto', 'c': 'video', 'x': 'Parte de una foto, pero el resultado se mueve: IA de vídeo.'}],
                'reto': {'t': 'Ahora tú: ¿qué te gustaría crear con IA para tu casa, tu trabajo o tu pueblo?', 'tf': '¿Qué quieres crear tú?', 'ph': 'por ejemplo, la felicitación de cumpleaños de mi nieta'}}),
            ('info',
             '<h3>La idea clave</h3>'
             '<p>Hay IA que no solo escribe: también crea imágenes, vídeos, música y voces. Se les llama IA [[generativa|IA que crea cosas nuevas: textos, dibujos, vídeos o voces.]] porque generan algo nuevo a partir de lo que tú le describes. Tú escribes «un cartel alegre con flores para una peluquería» y te dibuja uno que no existía.</p>'
             '<p>Igual que la IA que escribe, han aprendido de millones de imágenes, vídeos y grabaciones. Por eso a veces fallan en detalles: manos raras, letras que no se leen, sombras imposibles. Y por eso hay que mirarlo todo dos veces antes de usarlo.</p>'
             '<p>Lo delicado: también pueden imitar la cara o la voz de una persona real. Eso es un [[deepfake|Vídeo, foto o audio falso hecho con IA que imita a una persona real.]], y se usa para bulos y estafas, como la llamada de un falso nieto pidiendo dinero con una voz que parece la suya.</p>',
             '<h3>La idea clave</h3>'
             '<p>Hay IA que crea dibujos, vídeos y voces.</p>'
             '<p>Tú le dices lo que quieres. La IA lo crea.</p>'
             '<p>A veces se equivoca. Por ejemplo: dibuja manos raras.</p>'
             '<p>La IA puede copiar la cara o la voz de una persona.</p>'
             '<p>Algunas personas usan esto para engañar.</p>'),
            ('dos',
             '<h3>Lo que puede crear</h3><ul class="lista-ok"><li>Dibujos e imágenes para carteles, invitaciones o redes sociales.</li><li>Vídeos cortos a partir de una descripción o de una foto.</li><li>Voces que leen un texto en voz alta, también en otros idiomas.</li><li>Música sencilla para un vídeo.</li></ul>'
             '<h3>Lo que conviene cuidar</h3><ul><li>Revisa manos, caras y letras: es donde más falla.</li><li>No uses fotos de otras personas sin su permiso, y menos de niños.</li><li>No imites la cara ni la voz de nadie real.</li><li>Si una imagen o un audio te parece rarísimo, sospecha: puede ser falso.</li></ul>',
             '<h3>Puede crear</h3><ul class="lista-ok"><li>Dibujos para carteles.</li><li>Vídeos cortos.</li><li>Voces que leen textos.</li></ul>'
             '<h3>Ten cuidado</h3><ul><li>Revisa las manos y las letras.</li><li>No uses fotos de otras personas sin permiso.</li><li>Un audio o un vídeo puede ser falso.</li></ul>'),
            ('lab', {
                'tipo': 'verdad-o-mito', 'id': 'ia-que-crea-senales', 'titulo': '¿Pista de imagen falsa o no?',
                'intro': '<p>Las imágenes hechas con IA mejoran cada mes, así que no hay ninguna prueba infalible. Pero hay pistas que ayudan, y otras que no sirven para nada. ¿Cuál es cuál? Si dudas de una imagen, lo más seguro sigue siendo buscar de dónde viene.</p>',
                'intro_f': '<p>¿Cómo saber si una foto la hizo una IA? Hay pistas que sirven y otras que no.</p>',
                'pregunta': '¿Es una pista de que la imagen la ha hecho una IA?', 'preguntaf': '¿Es una pista?',
                'etiquetas': {'si': 'Es una pista', 'no': 'No es una pista', 'fsi': 'es una pista', 'fno': 'no es una pista'},
                'cartas': [
                    {'t': 'Una mano con seis dedos, o dedos que se funden entre sí.', 'tf': 'Una mano con seis dedos.', 'v': True, 'f': True,
                     'x': 'Las manos son de lo que más falla. Cuenta los dedos.', 'xf': 'Es una pista. Cuenta los dedos.'},
                    {'t': 'Letras de un cartel que no se pueden leer, como inventadas.', 'tf': 'Letras que no se entienden.', 'v': True, 'f': True,
                     'x': 'La IA dibuja la forma de las letras sin saber escribir. Si los carteles del fondo no dicen nada con sentido, sospecha.', 'xf': 'Es una pista. La IA dibuja mal las letras.'},
                    {'t': 'La foto está un poco borrosa.', 'v': False, 'f': True,
                     'x': 'Muchísimas fotos reales salen movidas o borrosas. Eso solo no dice nada.', 'xf': 'No es una pista. Muchas fotos reales salen borrosas.'},
                    {'t': 'Sombras que van hacia lados distintos con un solo sol.', 'tf': 'Sombras que van a lados distintos.', 'v': True, 'f': True,
                     'x': 'Con un solo sol, las sombras van hacia el mismo lado. Si no, algo raro pasa.', 'xf': 'Es una pista. Con un sol, las sombras van al mismo lado.'},
                    {'t': 'Sale una persona famosa.', 'v': False, 'f': True,
                     'x': 'Que salga alguien famoso no la hace falsa ni verdadera. Busca de dónde viene la foto.', 'xf': 'No es una pista. Mira de dónde viene la foto.'},
                    {'t': 'Orejas deformes o pendientes que se funden con la piel.', 'v': True,
                     'x': 'Orejas, dientes y pendientes son detalles donde la IA suele liarse.'},
                    {'t': 'Los colores son muy bonitos y vivos.', 'v': False,
                     'x': 'Muchas fotos reales tienen colores vivos, y muchas de IA no. Por sí solo, no sirve.'},
                    {'t': 'El fondo tiene cosas que se derriten o líneas que no encajan.', 'v': True,
                     'x': 'Barandillas que se cortan, ventanas torcidas, objetos derretidos: el fondo delata mucho.'},
                    {'t': 'La ha compartido muchísima gente por WhatsApp.', 'v': False,
                     'x': 'Que corra mucho no la hace verdadera. Los bulos son justo lo que más se comparte.'},
                    {'t': 'La piel parece de plástico, perfecta y sin poros.', 'v': True,
                     'x': 'Una piel demasiado lisa, como de muñeco, es una pista frecuente. Pero los filtros de las cámaras también lo hacen: mira más cosas.'},
                ]}),
        ]),
        ('Prueba', [
            ('tarea',
             '<h3>Tarea guiada · 10 minutos</h3>'
             '<ol><li>Abre un chat de IA que haga imágenes. Muchos lo hacen en su versión gratis, como ChatGPT, Gemini o Copilot. Si el tuyo no te deja, prueba con otro.</li>'
             '<li>Escribe: <q>Haz un dibujo alegre para un cartel de la fiesta de mi pueblo. Con farolillos, una plaza con naranjos y colores vivos. Sin personas y sin letras.</q></li>'
             '<li>Mira la imagen con lupa: ¿hay algo raro? Busca sombras, ventanas o farolillos imposibles.</li>'
             '<li>Pídele un cambio: <q>Hazlo de noche y con fuegos artificiales.</q></li>'
             '<li>Ahora pídele que añada el texto <q>Fiestas patronales</q>. ¿Lo escribe bien o se inventa letras?</li></ol>'
             '<p>Fíjate: hemos pedido «sin personas». Para practicar es mejor así, y nunca subas fotos de otras personas sin su permiso.</p>'
             '<p>Si no quieres usar ninguna IA todavía, haz el ejercicio en papel: escribe cómo describirías tu cartel ideal con 5 detalles (qué sale, colores, momento del día, estilo y texto). Saber describir es la mitad del trabajo.</p>',
             '<h3>Tarea · 10 minutos</h3>'
             '<ol><li>Abre un chat de IA que haga dibujos. Por ejemplo: ChatGPT o Gemini.</li>'
             '<li>Escribe: <q>Haz un dibujo alegre de la fiesta de un pueblo. Sin personas.</q></li>'
             '<li>Mira el dibujo. ¿Hay algo raro?</li>'
             '<li>Escribe: <q>Hazlo de noche.</q></li></ol>'
             '<p>No subas fotos de otras personas.</p>'
             '<p>Puedes hacerlo con alguien de tu familia.</p>'),
        ]),
        ('Conecta', [
            ('texto',
             '<p>La IA que crea te puede ahorrar mucho trabajo, si la usas con cabeza:</p>'
             '<ul><li><b>En el trabajo:</b> como Lucía, puedes hacer el cartel de una promoción o la imagen de una publicación. Revisa letras y detalles, y no la hagas pasar por una foto real de tu negocio.</li>'
             '<li><b>En casa:</b> si recibes un audio o una llamada de un familiar pidiéndote dinero con prisas, cuelga y llámale tú a su número de siempre. Las voces se pueden imitar.</li>'
             '<li><b>En el pueblo o la asociación:</b> puedes ilustrar el cartel de la verbena o de una actividad. Si quieres usar fotos de vecinos o de chavales, pide antes permiso por escrito.</li></ul>',
             '<ul><li><b>En el trabajo:</b> la IA te hace dibujos para carteles. Revisa las letras.</li>'
             '<li><b>En casa:</b> si un familiar te pide dinero por audio, llámale tú.</li>'
             '<li><b>En el pueblo:</b> pide permiso antes de usar fotos de otras personas.</li></ul>'),
        ]),
        ('Comparte', [
            ('texto',
             '<p>Enséñale a alguien de tu entorno el dibujo que has creado y pregúntale si sabría decir que lo ha hecho una IA. Después cuéntale el consejo más importante de esta lección: <b>ante un audio o un vídeo que pide dinero con prisas, llama tú a la persona</b>.</p>'
             '<p>Si quieres, mándanos tu dibujo por WhatsApp.</p>',
             '<p>Enseña tu dibujo a una persona.</p><ul><li>Pregúntale si sabe que lo hizo una IA.</li><li>Cuéntale que los audios pueden ser falsos.</li></ul>'),
            ('lab', {
                'tipo': 'explicaselo', 'id': 'ia-que-crea-explica', 'titulo': 'Explícaselo a…', 'tema': 'la IA que crea imágenes, vídeo y voz',
                'intro': '<p>Elige a quién se lo cuentas y rellena los huecos con tus palabras. Después, mándaselo por WhatsApp o cópialo.</p>',
                'intro_f': '<p>Elige a una persona. Escribe con tus palabras. Mándalo por WhatsApp.</p>',
                'huecos': [
                    {'l': 'Qué puede crear', 'lf': 'Qué crea', 'ph': 'dibujos, vídeos y voces a partir de lo que le describes'},
                    {'l': 'Dónde suele fallar', 'lf': 'Dónde falla', 'ph': 'en las manos, las caras y las letras'},
                    {'l': 'El consejo más importante', 'lf': 'Un consejo', 'ph': 'si un audio te pide dinero con prisas, cuelga y llama tú'},
                ]}),
        ]),
        ('Piensa', [
            ('quiz', [
                ('¿Qué hace una IA generativa de imágenes?',
                 [('Busca en internet una foto que ya existe', False, False),
                  ('Crea una imagen nueva a partir de lo que le describes', True, False),
                  ('Saca fotos con la cámara del móvil sin avisar', False, True),
                  ('Solo arregla fotos antiguas', False, True)],
                 'Crea una imagen que no existía, a partir de tu descripción y de todo lo que aprendió de millones de imágenes.',
                 'Crea un dibujo nuevo con lo que le dices.'),
                ('¿En qué detalles suelen fallar las imágenes hechas con IA?',
                 [('En las manos, las caras y las letras', True, False),
                  ('En nada, son siempre perfectas', False, False),
                  ('Solo en los colores del cielo', False, True),
                  ('Solo cuando son en blanco y negro', False, True)],
                 'Manos con dedos de más, letras inventadas o sombras imposibles. Míralo todo dos veces antes de usarlo.',
                 'Mira bien las manos y las letras.'),
                ('Te llega un audio con la voz de tu nieto pidiéndote dinero urgente. ¿Qué haces?',
                 [('Le mando el dinero enseguida, es su voz', False, False),
                  ('Cuelgo y le llamo yo a su número de siempre', True, False),
                  ('Le contesto con los datos de mi cuenta', False, True),
                  ('Le reenvío el audio a todos mis contactos', False, True)],
                 'La IA puede imitar voces. Ante cualquier petición de dinero con prisas, comprueba llamando tú a la persona.',
                 'La voz puede ser falsa. Llama tú a la persona.'),
            ]),
            ('texto',
             '<p><label for="reflexion-2-2"><b>Tu reflexión en una línea:</b> ¿para qué usarías tú una IA que crea imágenes, y para qué no?</label></p>'
             '<p><textarea id="reflexion-2-2" rows="2" style="width:100%;font:inherit;padding:12px;border-radius:12px;border:2px solid var(--l)"></textarea></p>'
             '<p style="font-size:.9rem;color:var(--m)">Lo que escribas aquí no se guarda ni se envía a ningún sitio.</p>',
             '<p><label for="reflexion-2-2-f"><b>Escribe una frase:</b> ¿qué dibujo le pedirías a la IA?</label></p>'
             '<p><textarea id="reflexion-2-2-f" rows="2" style="width:100%;font:inherit;padding:12px;border-radius:12px;border:2px solid var(--l)"></textarea></p>'),
        ]),
    ],
    'conecta': [('imagen-y-video', 'Imágenes y vídeo'), ('bulos-y-videos-falsos', 'Bulos y vídeos falsos')],
}
