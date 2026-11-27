# Fuentes de la web de AcademiAmable (academiamable.es)

La web es estática: cada página es un `index.html` en su carpeta. Se genera entera con:

    python3 _src/build.py

## Qué hay en `_src/`

- `build.py`: el generador. Contiene las plantillas de todas las páginas (portada, catálogo, ficha del curso, lección, mapa, mi aprendizaje, talleres, entidades, legal y 404) y escribe también `estilos.css`, `app.js`, `sw.js`, `sitemap.xml`, `robots.txt`, `llms.txt` y `manifest.webmanifest`.
- `estilos.css`: los estilos. Colores de marca: negro #141414, amarillo #FFD90F, verde Academia #0B7A7C (texto blanco encima 5,1:1), rojo #E30613 solo para el punto.
- `app.js`: panel «A tu manera» (lectura fácil, escuchar, letra grande, alto contraste, paso a paso), glosario al tocar, cuestionarios, progreso y código para cambiar de dispositivo. Todo se guarda en el navegador del alumno; no hay cuentas.
- `contenido/curso_ia.py`: estructura del curso «IA sin miedo», módulos, lecciones, conexiones del mapa y preguntas frecuentes.
- `contenido/leccion_1_1.py`: la lección 1.1, que sirve de modelo para escribir las demás.

## Cómo añadir una lección

1. Copia `contenido/leccion_1_1.py` con el nombre de la nueva lección y rellena sus 6 pasos (situación, descubre, prueba, conecta, comparte, piensa). Cada bloque lleva versión normal y versión Fácil. Las palabras del glosario se escriben `[[palabra|definición]]`.
2. Impórtala en `build.py` y añádela a `LECCIONES`.
3. En `contenido/curso_ia.py`, cambia su `False` por `True` para que aparezca enlazada.
4. Cuando la versión Fácil esté validada por personas, pon `'validada': True` (quita el aviso de «Lección en prueba»).
5. Ejecuta `python3 _src/build.py`.

## Pendiente

- WhatsApp de contacto: provisionalmente el de IA-Mable (+34 639 924 211). Se cambia en `WA` y `WA_TXT` de `build.py`.
- Pictogramas ARASAAC: el panel ya tiene la clase `is-pictos` y el estilo `.picto`; falta añadir los pictogramas a cada lección.
- Certificado en PDF (fase 5) y precios de píldoras y talleres.
