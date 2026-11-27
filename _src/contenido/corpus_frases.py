# Corpus del laboratorio «La siguiente palabra» (lección 1.2).
# Frases cotidianas de pueblo, de bar, de tienda y de asociación. El laboratorio cuenta qué palabra
# viene detrás de cada una o dos palabras, como hace (a lo grande) un modelo de lenguaje.
# Una frase por línea. Repetir estructuras es a propósito: así salen probabilidades claras.

FRASES = [f.strip() for f in '''
Mañana voy a ir al médico.
Mañana voy a ir al médico por la mañana.
Mañana voy a ir al mercado.
Mañana voy a ir al mercado de Zafra.
Mañana voy a ir al banco.
Mañana voy a ir al pueblo.
Mañana voy a ir a Badajoz.
Mañana voy a ir a Zafra.
Mañana voy a ir a ver a mi madre.
Mañana voy a llamar a mi hija.
Mañana voy a llamar a mi hijo.
Mañana voy a llamar al médico.
Mañana voy a llamar a la gestoría.
Mañana voy a hacer la compra.
Mañana voy a hacer pan.
Mañana voy a hacer migas.
Mañana voy a coger aceitunas.
Mañana voy a coger aceitunas con mi nieto.
Mañana voy a regar el huerto.
Mañana voy a abrir la tienda temprano.
Mañana voy a recoger a los niños.
Mañana voy a comprar pan.
Mañana vamos a ir a la feria.
Mañana vamos a comer en casa de mi madre.
Mañana es la reunión de la asociación.
Mañana es el mercadillo.
Mañana hace calor.
Mañana va a llover.
Mañana va a hacer frío.
Mañana va a hacer calor.
Hoy hay cocido en el bar.
Hoy hay migas en el bar.
Hoy hay mercadillo en la plaza.
Hoy hay reunión en la asociación.
Hoy hay partido en la tele.
Hoy hay pan recién hecho.
Hoy hay fiesta en el pueblo.
Hoy hay tapas de presa ibérica.
Hoy hace mucho calor.
Hoy hace un día muy bueno.
Hoy no abrimos por la tarde.
Hoy no hay pan.
Hoy cerramos a las dos.
Buenos días, ¿qué le pongo?
Buenos días, ¿qué tal está?
Buenos días, ¿qué tal la familia?
Buenos días a todos.
Buenos días, vecina.
Buenos días, vecino.
Buenas tardes, ¿qué le pongo?
Buenas tardes a todos.
Buenas noches y hasta mañana.
El pan está recién hecho.
El pan de hoy está muy bueno.
El pan de pueblo es el mejor.
El bar abre a las ocho.
El bar abre a las siete.
El bar cierra el lunes.
El bar cierra a las doce.
El bar está lleno de gente.
El médico pasa consulta por la mañana.
El médico viene los martes.
El mercadillo es los jueves.
El mercadillo es en la plaza.
El autobús a Zafra sale a las nueve.
El autobús a Badajoz sale a las ocho.
El tiempo va a cambiar.
El aceite de este año está muy bueno.
El aceite de oliva es lo mejor.
El huerto está precioso.
El lunes cerramos por descanso.
El lunes cerramos por la feria.
El lunes es fiesta en el pueblo.
El sábado es la comida de la asociación.
El sábado hay verbena en la plaza.
El sábado vamos a la feria.
El domingo comemos en casa de mi madre.
El domingo hay misa a las doce.
El domingo vamos al campo.
La tienda abre a las diez.
La tienda abre a las nueve.
La tienda cierra a las dos.
La tienda cierra el sábado por la tarde.
La tienda está en la plaza.
La reunión es el jueves a las seis.
La reunión es en el hogar del pensionista.
La reunión de la asociación es el jueves.
La comida de la asociación es el sábado.
La feria empieza el viernes.
La fiesta del pueblo es en agosto.
La fiesta del pueblo es en septiembre.
La plaza está llena de gente.
La farmacia abre a las nueve.
La farmacia de guardia está en la plaza.
Las aceitunas de este año están muy buenas.
Las rebajas empiezan el lunes.
Las rebajas empiezan el día siete.
Las migas de mi abuela son las mejores.
Las croquetas de mi madre son las mejores.
Los churros del domingo están muy buenos.
Los niños salen del colegio a las dos.
Los socios pueden venir con su familia.
Los martes viene el médico.
Mi abuela hace las mejores migas.
Mi abuela hace las mejores perrunillas.
Mi madre hace las mejores croquetas.
Mi madre vive en el pueblo.
Mi hija vive en Madrid.
Mi hija vive en Badajoz.
Mi hijo trabaja en Badajoz.
Mi hijo trabaja en el campo.
Mi nieto me ayuda con el móvil.
Mi nieto me ayuda con las aceitunas.
Mi vecina me trae el pan.
Te espero en la plaza.
Te espero en la plaza a las siete.
Te espero en el bar.
Te espero en la puerta de la iglesia.
Te espero en casa.
Te llamo mañana por la mañana.
Te llamo luego.
Te llamo cuando llegue.
Te mando la foto por WhatsApp.
Te mando un audio.
Te mando la ubicación.
Muchas gracias por todo.
Muchas gracias por venir.
Muchas gracias por la comida.
Muchas gracias por su visita.
Muchas gracias, vecina.
Gracias por venir a la reunión.
Gracias por comprar en el pueblo.
¿Qué tiempo va a hacer mañana?
¿Qué le pongo?
¿Qué tal está tu madre?
¿Qué tal la familia?
¿A qué hora abre la tienda?
¿A qué hora abre el bar?
¿A qué hora sale el autobús?
¿Me guardas dos barras de pan?
¿Me guardas el periódico?
¿Me traes el pan mañana?
¿Vienes a la reunión del jueves?
¿Vienes a la feria el sábado?
¿Vienes a comer el domingo?
Va a llover mañana.
Va a hacer calor esta semana.
Va a hacer frío por la noche.
Va a venir toda la familia.
Vamos a la feria el sábado.
Vamos a la plaza a tomar algo.
Vamos a comer a casa de mi madre.
Vamos a hacer una comida en la asociación.
Esta semana cerramos por vacaciones.
Esta semana hay ofertas en la tienda.
Esta semana hace mucho calor.
Este año la cosecha viene buena.
Este año la feria es más larga.
Este sábado hay verbena.
Abrimos todos los días de nueve a dos.
Abrimos el domingo por la mañana.
Cerramos el lunes por la feria.
Cerramos por vacaciones en agosto.
Tenemos tomates del huerto.
Tenemos pan de pueblo todos los días.
Tenemos ofertas en aceite de oliva.
Se vende aceite de oliva del pueblo.
Se vende leña de encina.
Se avisa a los vecinos de que mañana no hay agua.
Se avisa a los socios de que la reunión es el jueves.
Hay que llevar el DNI al banco.
Hay que pedir cita en el centro de salud.
Hay que regar el huerto por la tarde.
Hay tapas de migas en el bar.
No te olvides de la reunión.
No te olvides de comprar pan.
No te olvides de llamar a tu madre.
No hay pan hasta mañana.
Recuerda que la reunión es el jueves.
Recuerda que mañana cerramos.
Recuerda llevar el DNI.
Llámame cuando llegues.
Llámame mañana por la mañana.
Feliz cumpleaños, guapa.
Feliz cumpleaños, abuela.
Feliz Navidad a toda la familia.
Feliz fin de semana a todos.
Un abrazo muy fuerte.
Un abrazo a toda la familia.
Un beso muy grande.
Que tengas un buen día.
Que aproveche.
Que te mejores pronto.
Ya estoy en casa.
Ya estoy en el bar.
Ya he llegado al pueblo.
Estoy en el médico.
Estoy en la tienda.
Estoy haciendo la comida.
Nos vemos en la plaza.
Nos vemos mañana.
Nos vemos en la feria.
'''.strip().split('\n') if f.strip()]

# Comienzos que se ofrecen con un toque
SEMILLAS = ['Mañana voy a', 'Buenos días', 'Hoy hay', 'Te espero en', 'La tienda', 'Mi abuela']
SEMILLAS_F = ['Mañana voy a', 'Buenos días', 'Hoy hay']
