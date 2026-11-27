# Fuentes de la web de AcademiAmable (academiamable.es)

La web es estática: cada página es un `index.html` en su carpeta. Se genera entera con:

    python3 _src/build.py

## Qué hay en `_src/`

- `build.py`: el generador. Contiene las plantillas de todas las páginas (portada, catálogo, ficha del curso, lección, mapa, mi aprendizaje, talleres, entidades, legal y 404) y escribe también `estilos.css`, `app.js`, `sw.js`, `sitemap.xml`, `robots.txt`, `llms.txt` y `manifest.webmanifest`.
- `estilos.css`: los estilos. Colores de marca: negro #141414, amarillo #FFD90F, verde Academia #0B7A7C (texto blanco encima 5,1:1), rojo #E30613 solo para el punto.
- `ilustraciones.py`: dibuja todas las ilustraciones propias en `img/ilus/` (lo llama `build.py`; también se puede ejecutar solo). No hay fotos de bancos de imágenes ni recursos descargados.
- `app.js`: panel «A tu manera» (lectura fácil, escuchar, letra grande, alto contraste, paso a paso), glosario al tocar, cuestionarios (con «¿Cómo de seguro estás?»), progreso, dominio por lección, resumen de la lección y código para cambiar de dispositivo. Todo se guarda en el navegador del alumno; no hay cuentas.
- `labs.js`: el motor de los laboratorios (ver más abajo). Solo se carga en las páginas que tienen alguno.
- `contenido/repaso.py`: preguntas del «Repaso relámpago» (4 por lección como mínimo).
- `contenido/reglas_prompts.py`: reglas del evaluador de prompts (ingredientes, puntos, expresiones), frases de «Añadir», galería «Antes y después» y opciones del constructor.
- `contenido/corpus_frases.py`: las frases del laboratorio «La siguiente palabra».
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

## Método AcademiAmable: aprender tocando

Siete principios, explicados al público en `/metodo/` (función `metodo()` y lista `PRINCIPIOS` de `build.py`):
tocar antes que leer (laboratorio en Descubre o Prueba), ejemplo resuelto → práctica guiada → reto libre,
repaso relámpago con caja de Leitner al empezar, respuesta que siempre explica por qué (normal y Fácil),
dominio por lección sin bloquear nada, «Explícaselo a…» en Comparte y accesibilidad por diseño.

Lo que se monta solo en cada lección (no hay que escribirlo):
- **Repaso relámpago** al principio del paso 1: 3 preguntas de las lecciones publicadas anteriores (de `repaso.py`). En la primera lección sale un calentamiento sin nota.
- **Seguridad en las preguntas** de «Piensa»: «Lo sé / Creo que sí / Ni idea».
- **Resumen de la lección** antes de «He terminado»: dominio (media de las preguntas y de los laboratorios, sin contar el repaso), laboratorios hechos y «Acertaste y estabas seguro / Acertaste dudando / Repasa esto».

Las preguntas de «Piensa» admiten un cuarto elemento con la explicación Fácil:
`('Pregunta', [opciones], 'Explicación normal', 'Explicación Fácil')`.

## Cómo poner un laboratorio en una lección

Un laboratorio es un bloque más de un paso: `('lab', {...})`. Campos comunes:
`tipo`, `id` (único en toda la web; usa `idleccion-algo`), `titulo`, `intro` e `intro_f` (HTML normal y Fácil,
con botón Escuchar). En los textos, la clave `t` es la versión normal y `tf` la Fácil (igual con `x`/`xf`, `d`/`df`…);
si falta la Fácil, se usa la normal. `'f': True` en un elemento = sale en Fácil (que muestra menos elementos).
El resultado (de 0 a 1) se guarda en `aa-progreso` → `labs[id]`, y cuenta para el dominio de la lección.
Se puede usar con teclado, dedo y lector de pantalla; nada tiene tiempo. Después, `python3 _src/build.py`.

**clasifica** — tarjetas a grupos. Se toca la tarjeta y luego el grupo (con ratón, también arrastrando). El primer elemento sale como ejemplo resuelto. `c` puede ser una lista si vale más de un grupo (el primero es el ideal). `p` del grupo es lo que se dice en el reto libre.
```python
('lab', {'tipo': 'clasifica', 'id': 'mi-leccion-tipos', 'titulo': '¿Qué tipo de IA es?',
         'intro': '<p>…</p>', 'intro_f': '<p>…</p>',
         'categorias': [{'id': 'crea', 't': 'Crea', 'd': 'Hace algo nuevo', 'p': 'Revisa lo que crea.'},
                        {'id': 'reconoce', 't': 'Reconoce', 'd': 'Mira y clasifica'}],
         'items': [{'t': 'Google Lens te dice qué flor es', 'tf': 'El móvil dice qué flor es', 'c': 'reconoce', 'f': True,
                    'x': 'Por qué va ahí.', 'xf': 'Por qué, en fácil.'}],
         'reto': {'t': 'Ahora tú: escribe una herramienta tuya.', 'ph': 'por ejemplo…'}})   # reto es opcional
```

**verdad-o-mito** — mazo de cartas, una cada vez, con «¿Cómo de seguro estás?» (quítalo con `'confianza': False`).
```python
('lab', {'tipo': 'verdad-o-mito', 'id': 'mi-leccion-mitos', 'titulo': 'Mitos de la IA',
         'etiquetas': {'si': 'Verdad', 'no': 'Mito', 'fsi': 'es verdad', 'fno': 'es un mito'},   # opcional
         'pregunta': '¿Verdad o mito?',                                                       # opcional
         'cartas': [{'t': 'La IA piensa como tú.', 'v': False, 'f': True, 'x': '…', 'xf': '…'}]})
```

**siguiente-palabra** — predice la palabra siguiente contando qué viene detrás de 1 o 2 palabras en un corpus.
```python
from corpus_frases import FRASES, SEMILLAS, SEMILLAS_F
('lab', {'tipo': 'siguiente-palabra', 'id': 'mi-leccion-palabra', 'titulo': 'Escribe como una IA',
         'corpus': FRASES, 'semillas': SEMILLAS, 'semillas_f': SEMILLAS_F})
```

**ensena-a-la-maquina** — clasificador bayesiano ingenuo que aprende de lo que etiqueta el alumno. El primer ejemplo sale ya etiquetado. Botón «Enséñale mal a propósito» para ver el sesgo. Dos clases.
```python
('lab', {'tipo': 'ensena-a-la-maquina', 'id': 'mi-leccion-maquina', 'titulo': 'Enséñale a detectar estafas',
         'clases': [{'id': 'estafa', 't': 'Estafa'}, {'id': 'normal', 't': 'Normal'}],
         'ejemplos': [{'t': 'Pinche en este enlace…', 'c': 'estafa', 'f': True, 'x': 'por qué (en minúscula, sigue a «diría X:»)'}],  # unos 8
         'pruebas': [{'t': 'Mensaje nuevo', 'c': 'estafa', 'f': True}]})                                                      # unos 5
```
Las pruebas tienen que compartir palabras con los ejemplos, o la máquina no tiene en qué fijarse.

**evaluador-prompts** — puntúa un prompt con las reglas de `reglas_prompts.py`. `modo: 'corto'` lo deja sin galería.
```python
from reglas_prompts import GALERIA
('lab', {'tipo': 'evaluador-prompts', 'id': 'mi-leccion-evaluador', 'titulo': 'Evaluador de prompts',
         'inicial': 'Escribe un mensaje para mi familia.', 'galeria': GALERIA})     # o 'modo': 'corto'
```
Reglas: Qué quieres 25, Para qué 20, Quién eres 15, Formato 15, Límites o ejemplo 13, Tono 12 (total 100). Sin tarea, máximo 40; con menos de 6 palabras, máximo 25. Avisa (sin restar) si ve DNI, NIE, IBAN, teléfono o clave. Si cambias una frase de `EJEMPLOS` o de `CONSTRUCTOR`, comprueba que enciende su ingrediente.

**constructor-prompts** — un paso por ingrediente, con chips y «Otro…». «Llevar al evaluador» usa el de la misma página o abre `/laboratorio/`.
```python
from reglas_prompts import CONSTRUCTOR
('lab', {'tipo': 'constructor-prompts', 'id': 'mi-leccion-constructor', 'titulo': 'Monta tu prompt', 'pasos': CONSTRUCTOR})
```

**elige-la-mejor** — dos respuestas (HTML) a la misma petición. Lo que se marca con `<mark data-c="1">` se resalta al tocar el criterio 1.
```python
('lab', {'tipo': 'elige-la-mejor', 'id': 'mi-leccion-elige', 'titulo': '¿Qué respuesta es mejor?',
         'rondas': [{'f': True, 'pide': 'Lo que se le pidió', 'mejor': 'b',
                     'a': {'t': '<p><mark data-c="1">Dato inventado</mark></p>'},
                     'b': {'t': '<p><mark data-c="1">[hora]</mark></p>'},
                     'criterios': [{'c': 1, 't': 'No se inventa datos.', 'tf': '…'}],
                     'x': 'Por qué.', 'xf': '…'}]})
```

**detective** — lista de sitios para marcar, con «¿Cómo comprobarlo?». Se guarda lo marcado. `meta` = cuántos hacen falta.
```python
('lab', {'tipo': 'detective', 'id': 'mi-leccion-detective', 'titulo': 'Detective de la IA', 'meta': 5,
         'sitios': [{'id': 'galeria', 't': 'La galería de fotos', 'd': '…', 'f': True,
                     'pasos': ['Paso 1', 'Paso 2'], 'pasosf': ['Paso fácil']}]})
```

**explicaselo** — plantilla para explicárselo a tu madre, a un cliente o a un niño de 10 años; copia o abre WhatsApp (`wa.me/?text=`, sin número). Ponlo en «Comparte». En Fácil se usan los 2 primeros huecos.
```python
('lab', {'tipo': 'explicaselo', 'id': 'mi-leccion-explica', 'titulo': 'Explícaselo a…', 'tema': 'qué es la IA',
         'huecos': [{'l': 'Qué es, en una frase', 'lf': 'La IA es…', 'ph': 'un programa que…'},
                    {'l': 'Un ejemplo', 'ph': '…'}, {'l': 'Un consejo', 'ph': '…'}]})
```

**repaso** — no se escribe en la lección: lo pone `build.py`. Para que una lección nueva alimente los repasos siguientes, añade sus preguntas en `contenido/repaso.py` con su id de lección.

Páginas nuevas: `/laboratorio/` (evaluador y constructor, gratis y público; `laboratorio()` en `build.py`) y `/metodo/` (el método explicado).

## Pendiente

- WhatsApp de contacto: provisionalmente el de IA-Mable (+34 639 924 211). Se cambia en `WA` y `WA_TXT` de `build.py`.
- Pictogramas ARASAAC: el panel ya tiene la clase `is-pictos` y el estilo `.picto`; falta añadir los pictogramas a cada lección.
- Certificado en PDF (fase 5) y precios de píldoras y talleres.
