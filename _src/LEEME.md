# Fuentes de la web de AcademiAmable (academiamable.es)

La web es estática: cada página es un `index.html` en su carpeta. Se genera entera con:

    python3 _src/build.py

## Qué hay en `_src/`

- `build.py`: el generador. Contiene las plantillas de todas las páginas (portada, catálogo, ficha del curso, lección, mapa, mi aprendizaje, talleres, entidades, legal y 404) y escribe también `estilos.css`, `app.js`, `sw.js`, `sitemap.xml`, `robots.txt`, `llms.txt` y `manifest.webmanifest`.
- `estilos.css`: los estilos. Colores de marca: negro #141414, amarillo #FFD90F, verde Academia #0B7A7C (texto blanco encima 5,1:1), rojo #E30613 solo para el punto.
- `ilustraciones.py`: dibuja todas las ilustraciones propias en `img/ilus/` (lo llama `build.py`; también se puede ejecutar solo). No hay fotos de bancos de imágenes ni recursos descargados.
- `app.js`: panel «A tu manera» (lectura fácil, escuchar, letra grande, alto contraste, paso a paso), glosario al tocar, cuestionarios, progreso y código para cambiar de dispositivo. Todo se guarda en el navegador del alumno; no hay cuentas.
- `contenido/curso_ia.py`: estructura del curso «IA sin miedo», módulos, lecciones, conexiones del mapa y preguntas frecuentes.
- `contenido/leccion_1_1.py`: la lección 1.1, que sirve de modelo para escribir las demás.

## Sistema visual

- **Colores de apoyo** (comprobados con WCAG; el texto va siempre en negro #141414 encima):
  - Verde Academia pálido #DDF3F0 (franjas «A tu manera», ficha del curso). Negro 15,9:1; enlaces #08605F 6,4:1.
  - Amarillo pálido #FFF4B8 (franja «Para quién»). Negro 16,6:1; enlaces 6,6:1.
  - Color de cada módulo, fuerte (fondo de emblema) y pálido (cabecera de lección, tarjetas):
    1 amarillo #FFD90F / #FFF4B8 · 2 menta #6FCFC4 / #DDF3F0 · 3 coral #FF9573 / #FFE5DB ·
    4 lila #B9A6F2 / #EEE8FD · 5 cielo #84C8EE / #DFF1FB · 6 salvia #A6D38A / #E7F4DE.
    Negro sobre el fuerte: de 8,6:1 a 13,3:1; sobre el pálido, más de 15:1; gris #4A4A4A sobre el pálido, más de 7,3:1.
  - No uses el verde #0B7A7C como color de texto sobre los fondos pálidos (4,49:1): usa #08605F.
- **Ilustraciones** (`img/ilus/`, todas decorativas, con `alt=""`): `portada.svg` (Carmen con el móvil en un pueblo con encinas, torre y castillo), `modulo-1.svg` … `modulo-6.svg` (emblemas), `ico-facil|oir|grande|contraste|pasos|glosario|ritmo.svg` («A tu manera»), `ico-situacion|descubre|prueba|conecta|comparte|piensa.svg` (ciclo de la lección), `publico-negocio|mayores|comprension|entidades.svg` («Para quién»), `vacio.svg` (Mi aprendizaje sin progreso) y `404.svg`.
- **Movimiento**: solo la ilustración de portada asoma al cargar, y no se mueve si el sistema pide reducir el movimiento.

## Fotos (opcionales)

Si pones una foto en `img/fotos/` con uno de estos nombres (`.webp`, `.jpg` o `.png`), `build.py` la usa en lugar de la ilustración, con su ancho y alto reales, carga diferida (salvo la portada, que se carga primero) y recorte con `object-fit: cover`. Si no existe, sale la ilustración.

| Archivo | Dónde sale | Formato |
|---|---|---|
| `portada.webp` | Portada, a la derecha del título | horizontal, 16:10 (se recorta a 4:3 en ordenador) |
| `modulo-1.webp` … `modulo-6.webp` | Tarjetas de módulo de la portada y de la ficha, y cabecera de cada lección | 4:3 |
| `publico-pymes.webp`, `publico-mayores.webp`, `publico-comprension.webp`, `publico-entidades.webp` | Sección «Para quién» de la portada | 4:3 |

- El texto alternativo de cada foto está en el diccionario `FOTOS` de `build.py`: si cambias una foto, cambia también su descripción.
- Con alguna foto presente, la web añade «Imágenes creadas con IA.» en el pie de todas las páginas y bajo «Para quién».
- Que la persona quede en el centro de la foto (se recorta por los lados) y sin texto dentro de la imagen.
- Después de añadir o quitar fotos, ejecuta `python3 _src/build.py`.

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
