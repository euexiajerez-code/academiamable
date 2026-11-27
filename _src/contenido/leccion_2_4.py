# Lección 2.4 · Asistentes y agentes
# Versión Fácil: BORRADOR pendiente de validar con personas usuarias de Euexia.
# Formato de cada paso: lista de bloques (tipo, normal, facil). Las palabras del glosario se
# escriben como [[palabra|definición]].

LECCION = {
    'id': 'asistentes-y-agentes',
    'modulo': 2,
    'num': '2.4',
    'titulo': 'Asistentes y agentes',
    'minutos': 25,
    'descripcion': 'Asistentes y agentes de IA: en qué se diferencian, qué pueden hacer por ti y qué no deberías dejarles nunca. Lección 2.4 del curso gratis IA sin miedo.',
    'validada': False,
    'pasos': [
        ('Situación', [
            ('texto',
             '<p>Rafa tiene 24 años, vive en Jerez de los Caballeros y está buscando trabajo. Cada mañana le pide al asistente del móvil: «Recuérdame a las once llamar a la gestoría» o «¿Qué tiempo va a hacer en Zafra?», que mañana tiene entrevista allí.</p>'
             '<p>Un amigo le cuenta que hay IA que va más allá: «Tú le dices que busque ofertas y ella sola entra en las webs, rellena los formularios y manda tu currículum». A Rafa le suena a gloria… y a peligro. ¿Y si manda el currículum a una oferta falsa? ¿Y si pone que sabe inglés?</p>'
             '<p>En esta lección vas a ver la diferencia entre una IA que te ayuda cuando se lo pides y una que hace tareas por ti.</p>',
             '<p>Rafa tiene 24 años. Busca trabajo.</p>'
             '<p>Rafa habla con el asistente del móvil. Le pide recordatorios.</p>'
             '<p>Un amigo le dice: «Hay IA que manda tu currículum sola».</p>'
             '<p>Rafa tiene dudas.</p>'
             '<p>En esta lección vas a ver qué IA te ayuda y qué IA hace tareas por ti.</p>'),
        ]),
        ('Descubre', [
            ('info',
             '<h3>La idea clave</h3>'
             '<p>Un [[asistente|IA que te ayuda cuando se lo pides: contesta, pone una alarma o te recuerda algo.]] responde cuando le hablas. Le pides una cosa, la hace y espera a que le pidas otra. Es el asistente de voz del móvil o del altavoz de casa, o un chat de IA cuando le preguntas algo.</p>'
             '<p>Un [[agente|IA que hace sola una tarea de varios pasos: busca, decide, rellena o envía cosas por ti.]] va un paso más allá: le das un objetivo («búscame ofertas de trabajo cerca y apúntame») y él solo decide los pasos, entra en páginas web, usa otras aplicaciones y hace cosas en tu nombre. Algunas IA ya empiezan a funcionar así.</p>'
             '<p>Cuanto más hace la IA por ti, más importante es vigilarla. Un asistente que se equivoca te da una respuesta mala; un agente que se equivoca puede mandar un correo, hacer una compra o rellenar un formulario mal. Y la responsabilidad sigue siendo tuya.</p>',
             '<h3>La idea clave</h3>'
             '<p>Un asistente te ayuda cuando se lo pides.</p>'
             '<p>Por ejemplo: pone una alarma o te dice el tiempo.</p>'
             '<p>Un agente hace una tarea completa él solo.</p>'
             '<p>Por ejemplo: busca ofertas de trabajo y manda tu currículum.</p>'
             '<p>Tú tienes que revisar lo que hace el agente.</p>'),
            ('dos',
             '<h3>Asistente</h3><ul class="lista-ok"><li>Espera a que le pidas algo.</li><li>Hace una cosa cada vez.</li><li>Te contesta o hace algo sencillo: una alarma, una llamada, un recordatorio.</li><li>Si se equivoca, lo ves enseguida.</li></ul>'
             '<h3>Agente</h3><ul><li>Recibe un objetivo y decide él los pasos.</li><li>Puede entrar en webs, rellenar formularios o enviar mensajes.</li><li>Ahorra mucho tiempo en tareas repetitivas.</li><li>Si se equivoca, puede hacerlo en tu nombre: revisa antes de que envíe, pague o firme.</li></ul>',
             '<h3>Asistente</h3><ul class="lista-ok"><li>Espera a que le pidas algo.</li><li>Hace una cosa cada vez.</li><li>Ejemplo: pone una alarma.</li></ul>'
             '<h3>Agente</h3><ul><li>Hace una tarea larga él solo.</li><li>Puede enviar cosas en tu nombre.</li><li>Tú revisas antes de enviar o pagar.</li></ul>'),
        ]),
        ('Prueba', [
            ('tarea',
             '<h3>Tarea guiada · 10 minutos</h3>'
             '<ol><li>Usa el asistente de voz de tu móvil (mantén pulsado el botón de inicio o di la palabra para despertarlo). Pídele: <q>Recuérdame mañana a las diez llamar al médico.</q> Comprueba en tu agenda o en tus recordatorios que lo ha apuntado bien.</li>'
             '<li>Ahora abre un chat de IA gratis (ChatGPT, Gemini, Claude o Copilot) y escribe: <q>Quiero preparar una entrevista de trabajo para camarero. Hazme una lista de los pasos, del primero al último.</q></li>'
             '<li>Lee la lista y marca cada paso con una de estas tres cosas: <b>«lo haría la IA»</b>, <b>«lo haría con ayuda de la IA»</b> o <b>«lo hago yo siempre»</b>.</li>'
             '<li>Mira tu lista: ¿qué pasos no dejarías nunca en manos de una máquina?</li></ol>'
             '<p>Para practicar, no le des tu nombre completo, tu DNI ni tus contraseñas. Un buen asistente no los necesita.</p>'
             '<p>Si no quieres usar ninguna IA todavía, haz los pasos 3 y 4 en papel: apunta los pasos de una tarea que hagas a menudo (la compra de la semana, pedir cita) y marca cuáles le dejarías a una IA.</p>',
             '<h3>Tarea · 10 minutos</h3>'
             '<ol><li>Habla con el asistente del móvil.</li>'
             '<li>Di: <q>Recuérdame mañana a las 10 llamar al médico.</q></li>'
             '<li>Mira si el recordatorio está bien.</li>'
             '<li>Piensa: ¿qué cosas no dejarías hacer a una IA?</li></ol>'
             '<p>No le des tu DNI ni tus contraseñas.</p>'
             '<p>Puedes hacerlo con alguien de tu familia.</p>'),
        ]),
        ('Conecta', [
            ('texto',
             '<p>Asistentes y agentes te pueden quitar trabajo, si tú pones las normas:</p>'
             '<ul><li><b>En el trabajo:</b> un asistente te recuerda citas y pedidos. Si algún día usas un agente que envía correos o presupuestos, que te los enseñe antes de mandarlos. Nunca le des permiso para pagar solo.</li>'
             '<li><b>En casa:</b> el asistente de voz es muy cómodo para poner alarmas, llamar o recordar medicinas. Revisa de vez en cuando qué ha guardado de tus conversaciones y bórralo si quieres.</li>'
             '<li><b>En el pueblo o la asociación:</b> un asistente puede ayudarte a preparar el calendario de actividades y los avisos. Las decisiones de la junta y lo que se firma, siempre lo deciden personas.</li></ul>',
             '<ul><li><b>En el trabajo:</b> el asistente te recuerda citas. No dejes que la IA pague sola.</li>'
             '<li><b>En casa:</b> el asistente pone alarmas y te recuerda las medicinas.</li>'
             '<li><b>En el pueblo:</b> la IA ayuda con los avisos. Las decisiones las toman las personas.</li></ul>'),
        ]),
        ('Comparte', [
            ('texto',
             '<p>Cuéntale a alguien de tu entorno la diferencia entre un asistente y un agente con un ejemplo de tu vida. Y pregúntale: <b>¿qué tarea le dejarías tú a una IA y cuál nunca?</b> Seguro que no coincidís del todo.</p>'
             '<p>Si quieres, mándanos por WhatsApp vuestras respuestas.</p>',
             '<p>Cuéntale a una persona:</p><ul><li>Qué hace un asistente.</li><li>Qué hace un agente.</li></ul><p>Pregúntale qué le dejaría hacer a una IA.</p>'),
        ]),
        ('Piensa', [
            ('quiz', [
                ('¿Cuál es la principal diferencia entre un asistente y un agente?',
                 [('El asistente responde cuando se lo pides; el agente hace solo una tarea de varios pasos', True, False),
                  ('No hay ninguna diferencia, son dos nombres de lo mismo', False, False),
                  ('El agente es una persona y el asistente una máquina', False, True),
                  ('El asistente solo funciona sin internet', False, True)],
                 'El asistente hace una cosa cada vez que se lo pides. El agente recibe un objetivo y decide él los pasos para conseguirlo.'),
                ('¿Cuál de estas cosas es un ejemplo de asistente?',
                 [('Una IA que busca ofertas, rellena formularios y manda tu currículum sola', False, False),
                  ('Decirle al móvil «pon una alarma a las siete»', True, False),
                  ('Un vecino que te ayuda con la compra', False, True),
                  ('El calendario de papel de la cocina', False, True)],
                 'Le pides una cosa concreta, la hace y espera. Eso es un asistente.'),
                ('Usas un agente que manda correos por ti. ¿Qué es lo más prudente?',
                 [('Que me enseñe cada correo antes de enviarlo', True, False),
                  ('Darle mi contraseña del banco por si tiene que pagar algo', False, False),
                  ('Dejarle hacer y no mirar nunca lo que envía', False, True),
                  ('Darle permiso para firmar documentos en mi nombre', False, True)],
                 'Lo que haga un agente en tu nombre es responsabilidad tuya. Revisa antes de que envíe, pague o firme.'),
            ]),
            ('texto',
             '<p><label for="reflexion-2-4"><b>Tu reflexión en una línea:</b> ¿qué tarea de tu día a día le dejarías a una IA, y cuál no le dejarías nunca?</label></p>'
             '<p><textarea id="reflexion-2-4" rows="2" style="width:100%;font:inherit;padding:12px;border-radius:12px;border:2px solid var(--l)"></textarea></p>'
             '<p style="font-size:.9rem;color:var(--m)">Lo que escribas aquí no se guarda ni se envía a ningún sitio.</p>',
             '<p><label for="reflexion-2-4-f"><b>Escribe una frase:</b> ¿qué le pedirías a un asistente?</label></p>'
             '<p><textarea id="reflexion-2-4-f" rows="2" style="width:100%;font:inherit;padding:12px;border-radius:12px;border:2px solid var(--l)"></textarea></p>'),
        ]),
    ],
    'conecta': [('en-el-trabajo', 'En el trabajo y el negocio'), ('datos-y-privacidad', 'Datos personales y privacidad')],
}
