#!/usr/bin/env python3
"""Genera la web estática de AcademiAmable en la raíz del repositorio.

    python3 _src/build.py

Lee el contenido de _src/contenido/ y escribe cada página en su carpeta (index.html),
más estilos.css, app.js, sw.js, sitemap.xml, robots.txt y llms.txt.
"""
import hashlib, html, json, math, os, re, sys, datetime

SRC = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(SRC)
sys.path.insert(0, os.path.join(SRC, 'contenido'))
from curso_ia import CURSO          # noqa: E402
from leccion_1_1 import LECCION as L11  # noqa: E402

LECCIONES = {L11['id']: L11}
DOM = 'https://academiamable.es'
WA = '34639924211'                  # Provisional: el WhatsApp de IA-Mable (pendiente de decidir)
WA_TXT = '+34 639 924 211'
HOY = datetime.date.today().isoformat()
ENTIDAD = {
    'nombre': 'Asociación Euexia Rural', 'cif': 'G06725477',
    'dir': 'Calle Calzada, 24, 06380 Jerez de los Caballeros (Badajoz)',
    'registro': 'Registro de Asociaciones de la Junta de Extremadura, n.º 7076, Sección 1.ª',
    'correo': 'proyectos@euexiarural.com',
}
PAGINAS = []   # (ruta, prioridad) para el sitemap
LLMS = []      # (titulo, url, descripcion)

e = html.escape


def leer(n):
    with open(os.path.join(SRC, n), encoding='utf-8') as f:
        return f.read()


def escribir(ruta, txt):
    p = os.path.join(RAIZ, ruta)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w', encoding='utf-8') as f:
        f.write(txt)


def huella(txt):
    return hashlib.sha1(txt.encode()).hexdigest()[:8]


CSS = leer('estilos.css')
JS = leer('app.js')
V_CSS, V_JS = huella(CSS), huella(JS)

# ---------- piezas comunes ----------
LOGO = '<img src="/img/logo.svg" width="44" height="44" alt="">'
WM = '<span class="wm">Academ<span class="i" aria-hidden="true">ı</span><span class="sr">i</span><b>Amable</b></span>'
ICO_ATM = ('<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round">'
           '<path d="M4 7h10M18 7h2M4 17h4M12 17h8"/><circle cx="16" cy="7" r="2.2"/><circle cx="10" cy="17" r="2.2"/></svg>')
ICO_OIR = ('<svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round">'
           '<path d="M4 10v4h4l5 4V6L8 10z"/><path d="M16 9a4 4 0 0 1 0 6M18.5 6.5a8 8 0 0 1 0 11"/></svg>')

NAV = [('/cursos/', 'Cursos'), ('/talleres/', 'Talleres'), ('/entidades/', 'Para entidades'), ('/mi-aprendizaje/', 'Mi aprendizaje')]

PREFS_INLINE = ("<script>try{var p=JSON.parse(localStorage.getItem('aa-prefs')||'{}'),m={facil:'is-facil',oir:'is-oir',grande:'is-grande',"
                "contraste:'is-contraste',pasos:'is-pasos',pictos:'is-pictos'};for(var k in m)if(p[k])document.documentElement.classList.add(m[k])}catch(e){}</script>")

PANEL = '''<div class="panel" id="panel" role="dialog" aria-modal="true" aria-labelledby="panel-t">
<div class="caja">
<button class="cerrar" type="button" aria-label="Cerrar">×</button>
<h2 id="panel-t">A tu manera</h2>
<p>Elige cómo quieres aprender. Se guarda en este móvil u ordenador.</p>
<label class="opc"><input type="checkbox" data-opc="facil"><span><b>Lectura fácil</b><span>Frases cortas y palabras sencillas.</span></span></label>
<label class="opc"><input type="checkbox" data-opc="oir"><span><b>Escuchar</b><span>Un botón en cada parte la lee en voz alta.</span></span></label>
<label class="opc"><input type="checkbox" data-opc="grande"><span><b>Letra grande</b><span>Más tamaño y más espacio entre líneas.</span></span></label>
<label class="opc"><input type="checkbox" data-opc="contraste"><span><b>Alto contraste</b><span>Colores más fuertes para ver mejor.</span></span></label>
<label class="opc"><input type="checkbox" data-opc="pasos"><span><b>Paso a paso</b><span>En las lecciones, una parte cada vez, sin desplazarte.</span></span></label>
<p style="margin-top:18px;font-size:.92rem;color:var(--m)">Las palabras subrayadas con puntos se explican al tocarlas. Sin límites de tiempo: vas a tu ritmo.</p>
</div></div>'''


def cabecera(activo):
    cur = ' aria-current="page"'
    nav = ''.join(f'<a href="{u}"{cur if u == activo else ""}>{t}</a>' for u, t in NAV)
    return (f'<a class="salto" href="#contenido">Saltar al contenido</a>'
            f'<header class="cab"><div class="c"><a class="marca" href="/">{LOGO}{WM}</a>'
            f'<nav class="nav" aria-label="Principal">{nav}</nav>'
            f'<button class="btn peq atm" type="button" data-abre-panel aria-haspopup="dialog">{ICO_ATM}A tu manera</button>'
            f'</div></header>')


PIE = f'''<footer class="pie-web"><div class="c">
<div class="rej">
<div><a class="marca" href="/" style="color:#fff">{LOGO}{WM.replace('<b>', '<b style="color:#7FD3D4">')}</a><p style="margin-top:12px">Aprender, a tu manera. Una iniciativa de la entidad social Euexia Rural, con <a href="https://esamable.es">IA-Mable</a>.</p></div>
<div><h2>Aprende</h2><ul><li><a href="/cursos/iniciacion-ia/">Curso gratis de IA</a></li><li><a href="/cursos/">Todos los cursos</a></li><li><a href="/talleres/">Talleres</a></li><li><a href="/mi-aprendizaje/">Mi aprendizaje</a></li></ul></div>
<div><h2>Contacto</h2><ul><li><a href="https://wa.me/{WA}">WhatsApp {WA_TXT}</a></li><li><a href="/entidades/">Formación para entidades y empresas</a></li><li><a href="https://euexiarural.com">Euexia Rural</a></li></ul></div>
</div>
<p class="leg">© {datetime.date.today().year} {ENTIDAD['nombre']} · CIF {ENTIDAD['cif']} · <a href="/aviso-legal/">Aviso legal</a> · <a href="/privacidad/">Privacidad</a> · <a href="/cookies/">Cookies</a></p>
</div></footer>'''


def glos(t):
    return re.sub(r'\[\[([^|\]]+)\|([^\]]+)\]\]',
                  lambda m: f'<button type="button" class="g" data-def="{e(m.group(2))}">{m.group(1)}</button>', t)


def B(normal, facil, tag='div', clase=''):
    """Bloque con versión normal y Fácil, y botón de escuchar."""
    return (f'<{tag} class="b {clase}" data-leer><button type="button" class="oir" aria-pressed="false">{ICO_OIR}Escuchar</button>'
            f'<div class="n">{glos(normal)}</div><div class="f">{facil}</div></{tag}>')


def pagina(ruta, titulo, desc, cuerpo, activo='', schema=None, noindex=False, prioridad='0.6'):
    canon = DOM + '/' + (ruta + '/' if ruta else '')
    sch = ''
    for s in (schema or []):
        sch += '<script type="application/ld+json">' + json.dumps(s, ensure_ascii=False) + '</script>'
    robots = '<meta name="robots" content="noindex">' if noindex else ''
    doc = f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(titulo)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{canon}">
{robots}
<meta name="theme-color" content="#FFD90F">
<meta property="og:type" content="website"><meta property="og:locale" content="es_ES"><meta property="og:site_name" content="AcademiAmable">
<meta property="og:title" content="{e(titulo)}"><meta property="og:description" content="{e(desc)}"><meta property="og:url" content="{canon}">
<meta property="og:image" content="{DOM}/img/og.png"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="/img/apple-touch-icon.png">
<link rel="manifest" href="/manifest.webmanifest">
<link rel="preload" href="/fonts/montserrat-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/nunito-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/estilos.css?v={V_CSS}">
{PREFS_INLINE}
{sch}
</head>
<body>
{cabecera(activo)}
<main id="contenido">
{cuerpo}
</main>
{PIE}
{PANEL}
<script src="/app.js?v={V_JS}" defer></script>
</body>
</html>
'''
    doc = re.sub(r'\n\s*\n', '\n', doc)
    escribir(os.path.join(ruta, 'index.html') if ruta else 'index.html', doc)
    if not noindex:
        PAGINAS.append((ruta, prioridad))
        LLMS.append((titulo, canon, desc))


ORG = {'@context': 'https://schema.org', '@type': 'EducationalOrganization', 'name': 'AcademiAmable', 'url': DOM + '/',
       'logo': DOM + '/img/icono-512.png', 'slogan': 'Aprender, a tu manera.',
       'parentOrganization': {'@type': 'NGO', 'name': ENTIDAD['nombre'], 'taxID': ENTIDAD['cif'], 'url': 'https://euexiarural.com'},
       'address': {'@type': 'PostalAddress', 'streetAddress': 'Calle Calzada, 24', 'postalCode': '06380',
                   'addressLocality': 'Jerez de los Caballeros', 'addressRegion': 'Badajoz', 'addressCountry': 'ES'},
       'contactPoint': {'@type': 'ContactPoint', 'telephone': '+' + WA, 'contactType': 'customer support', 'availableLanguage': 'es'}}

C = CURSO
CURL = f'/cursos/{C["slug"]}/'
TODAS = [(l[0], l[1], l[2], m) for m in C['modulos'] for l in m['lecciones']]
N_LEC = len(TODAS)
IDS_PUB = [l[0] for l in TODAS if l[2]]


def url_lec(lid):
    return f'{CURL}{lid}/'


# ---------- Portada ----------
def portada():
    mods = ''.join(f'<li><b>Módulo {m["n"]}</b> · {e(m["titulo"])}</li>' for m in C['modulos'])
    cuerpo = f'''
<section class="hero"><div class="c">
<div>
<span class="etq">Academia online · Euexia Rural</span>
<h1>Aprende a usar la inteligencia artificial, a tu manera</h1>
{B('<p class="ent">Cursos cortos, píldoras y talleres para entender la tecnología y sacarle partido en tu trabajo, en casa y en tu pueblo. Todo se puede leer, ver u oír, y todo tiene versión Fácil.</p>',
   '<p class="ent">Aquí aprendes a usar la tecnología. Puedes leer, ver vídeos o escuchar. Todo está también en lectura fácil.</p>')}
<div class="acc"><a class="btn" href="{CURL}">Empezar el curso gratis</a><button class="btn lin" type="button" data-abre-panel aria-haspopup="dialog">{ICO_ATM}Aprender a tu manera</button></div>
</div>
<img class="hero-img" src="/img/logo.svg" width="380" height="380" alt="">
</div></section>

<section class="sec"><div class="c">
<div class="rej" style="grid-template-columns:repeat(auto-fit,minmax(300px,1fr));align-items:center">
<div>
<span class="etq">Curso gratis</span>
<h2 style="margin-top:.2em">{e(C['titulo'])}: {e(C['subtitulo'].lower())}</h2>
{B(f'<p>Unas {C["horas"]} horas en 6 módulos, desde cero. Vídeos de 2 a 4 minutos, infografías, tareas con casos de tu vida y certificado al terminar. Sin registro.</p>',
   '<p>Un curso gratis para empezar desde cero. Tiene 6 partes. Al final te dan un certificado.</p>')}
<a class="btn" href="{CURL}">Ver el curso</a>
</div>
<ul class="lista-ok">{mods}</ul>
</div></div></section>

<section class="sec gris"><div class="c">
<span class="etq">A tu manera</span>
<h2 style="margin-top:.2em">Tú decides cómo aprender</h2>
{B('<p>Con el botón «A tu manera», arriba a la derecha, adaptas cualquier página a ti. Se queda guardado en tu móvil.</p>',
   '<p>Pulsa el botón amarillo «A tu manera». Allí eliges cómo quieres aprender.</p>')}
<div class="rej tres">
<div class="tar"><h3>Lectura fácil</h3><p>Cada texto tiene su versión Fácil, escrita con frases cortas y validada por personas.</p></div>
<div class="tar"><h3>Escuchar</h3><p>Cada parte se lee en voz alta con un toque.</p></div>
<div class="tar"><h3>Letra grande y alto contraste</h3><p>Más tamaño, más espacio y colores más fuertes.</p></div>
<div class="tar"><h3>Paso a paso</h3><p>La lección, de pantalla en pantalla, sin perderte.</p></div>
<div class="tar"><h3>Glosario al tocar</h3><p>Las palabras difíciles se explican al tocarlas.</p></div>
<div class="tar"><h3>A tu ritmo</h3><p>Sin fechas ni límites de tiempo. Tu progreso se guarda solo.</p></div>
</div>
</div></section>

<section class="sec"><div class="c">
<span class="etq">Cómo se aprende</span>
<h2 style="margin-top:.2em">Primero lo pruebas, luego lo entiendes</h2>
{B('<p>Cada lección dura de 20 a 30 minutos y parte de una situación real. Lo que aprendes lo conectas con tu trabajo, tu casa y tu comunidad.</p>',
   '<p>Cada lección dura media hora o menos. Empieza con un caso de la vida real.</p>')}
<ol class="ciclo">
<li><b>Situación</b>Un caso real en un vídeo de 1 minuto.</li>
<li><b>Descubre</b>La idea clave en una infografía.</li>
<li><b>Prueba</b>Una tarea guiada con una IA de verdad.</li>
<li><b>Conecta</b>Cómo se usa en el trabajo, en casa y en el pueblo.</li>
<li><b>Comparte</b>Enséñaselo a alguien de tu entorno.</li>
<li><b>Piensa</b>Tres preguntas y una reflexión.</li>
</ol>
</div></section>

<section class="sec gris"><div class="c">
<span class="etq">Para quién</span>
<h2 style="margin-top:.2em">Para cualquiera que quiera entender la tecnología</h2>
<div class="rej">
<div class="tar"><h3>Pymes y autónomos</h3><p>Para ahorrar tiempo con la IA en el día a día del negocio.</p></div>
<div class="tar"><h3>Personas mayores y vecinos</h3><p>Para usar el móvil y la IA sin miedo, también en trámites.</p></div>
<div class="tar"><h3>Personas con dificultades de comprensión</h3><p>Todo en lectura fácil, con audio y paso a paso.</p></div>
<div class="tar"><h3>Entidades sociales y docentes</h3><p>Formación para equipos y materiales accesibles. <a href="/entidades/">Ver formación a medida</a>.</p></div>
</div>
</div></section>

<section class="sec"><div class="c">
<span class="etq">Formatos</span>
<h2 style="margin-top:.2em">Cursos, píldoras y talleres</h2>
<div class="rej">
<div class="tar"><span><span class="pill gratis">Gratis</span></span><h3>Cursos</h3><p>Varias semanas, con certificado. El primero, «IA sin miedo», es gratis.</p><div class="pie"><a href="/cursos/">Ver cursos</a></div></div>
<div class="tar"><span><span class="pill pronto">Próximamente</span></span><h3>Píldoras</h3><p>De 10 a 20 minutos, un solo objetivo: aprender una cosa concreta y aplicarla ya.</p></div>
<div class="tar"><span><span class="pill pronto">Próximamente</span></span><h3>Talleres</h3><p>En directo, en persona u online, con fecha. <a href="/talleres/">Avísame</a>.</p></div>
</div>
<p class="aviso" style="margin-top:28px">AcademiAmable es la hermana de <a href="https://esamable.es">IA-Mable</a>, las apps sencillas y accesibles para negocios de la Asociación Euexia Rural. IA-Mable hace las apps; AcademiAmable te enseña a usarlas.</p>
</div></section>
'''
    pagina('', 'AcademiAmable · Aprende a usar la IA, a tu manera. Curso gratis',
           'Academia online de Euexia Rural: curso gratis de inteligencia artificial desde cero, píldoras y talleres. Todo en versión Fácil, con audio y a tu ritmo.',
           cuerpo, schema=[ORG, {'@context': 'https://schema.org', '@type': 'WebSite', 'name': 'AcademiAmable', 'url': DOM + '/', 'inLanguage': 'es'}],
           prioridad='1.0')


# ---------- Catálogo ----------
def catalogo():
    cuerpo = f'''
<div class="c"><p class="migas"><a href="/">Inicio</a> › Cursos</p>
<h1>Cursos, píldoras y talleres</h1>
{B('<p>Empieza por el curso gratis de IA. Iremos sumando píldoras cortas y talleres con fecha.</p>', '<p>Empieza por el curso gratis. Pronto habrá más cursos.</p>')}
<h2>Cursos</h2>
<div class="rej">
<article class="tar"><span><span class="pill gratis">Gratis</span> <span class="pill">{C['horas']} horas</span> <span class="pill">{C['nivel']}</span> <span class="pill">Con certificado</span></span>
<h3><a href="{CURL}">{e(C['titulo'])}</a></h3><p>{e(C['subtitulo'])}.</p>
<div class="pie"><a class="btn peq" href="{CURL}">Ver el curso</a></div></article>
</div>
<h2>Píldoras</h2>
<p>Muy pronto: vídeos y tareas de 10 a 20 minutos para aprender una cosa concreta, como hacer un cartel con IA o resumir un documento largo.</p>
<h2>Talleres</h2>
<p>Sesiones en directo, en persona u online. <a href="/talleres/">Mira cómo apuntarte</a>.</p>
</div>'''
    pagina('cursos', 'Cursos de IA y tecnología en versión Fácil | AcademiAmable',
           'Catálogo de AcademiAmable: curso gratis de inteligencia artificial desde cero, píldoras de 10 a 20 minutos y talleres. Todo con versión Fácil.',
           cuerpo, activo='/cursos/', prioridad='0.8')


# ---------- Ficha del curso ----------
def ficha():
    mods = ''
    for m in C['modulos']:
        lis = ''
        for lid, tit, pub, _ in [(l[0], l[1], l[2], m) for l in m['lecciones']]:
            lnk = f'<a href="{url_lec(lid)}">{e(tit)}</a>' if pub else f'<span class="pronto">{e(tit)} · próximamente</span>'
            lis += f'<li><span class="est" data-lec="{lid}" role="img" aria-label="Sin terminar"></span>{lnk}</li>'
        mods += (f'<li><h3>Módulo {m["n"]} · {e(m["titulo"])}</h3><p class="preg">{e(m["pregunta"])}</p>'
                 f'<ul class="lecs">{lis}</ul><p style="margin:10px 0 0"><b>Tarea práctica:</b> {e(m["tarea"])}.</p></li>')
    objs = ''.join(f'<li>{e(o)}</li>' for o in C['objetivos'])
    faq = ''.join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in C['faq'])
    primera = next(l for l in TODAS if l[2])
    ids = ','.join(l[0] for l in TODAS)
    cuerpo = f'''
<div class="c"><p class="migas"><a href="/">Inicio</a> › <a href="/cursos/">Cursos</a> › {e(C['titulo'])}</p>
<span class="pill gratis">Gratis</span> <span class="pill">{C['horas']} horas</span> <span class="pill">6 módulos</span> <span class="pill">Con certificado</span>
<h1>{e(C['titulo'])}: curso gratis de inteligencia artificial desde cero</h1>
{B('<p style="font-size:1.15rem">' + e(C['descripcion']) + '</p>', '<p>' + e(C['facil']) + '</p>')}
<div class="acc"><a class="btn" href="{url_lec(primera[0])}">Empezar por la lección 1.1</a><a class="btn lin" href="{CURL}mapa/">Ver el mapa del curso</a></div>
<div style="max-width:420px;margin-top:22px"><p id="txt-prog" style="margin:0 0 6px">Tu progreso</p><div class="barra" data-barra="{ids}" data-txt="txt-prog" role="presentation"><i></i></div></div>
<h2>Qué vas a aprender</h2><ul class="lista-ok">{objs}</ul>
<h2>Módulos y lecciones</h2>
<p>Cada lección sigue el mismo ciclo: situación, descubre, prueba, conecta, comparte y piensa. Las lecciones se van abriendo una a una.</p>
<ol class="mods">{mods}</ol>
<h2>Preguntas frecuentes</h2><div class="faq">{faq}</div>
</div>'''
    curso_sch = {'@context': 'https://schema.org', '@type': 'Course', 'name': f'{C["titulo"]}: {C["subtitulo"]}',
                 'description': C['descripcion'], 'inLanguage': 'es', 'url': DOM + CURL, 'isAccessibleForFree': True,
                 'educationalLevel': 'Beginner', 'teaches': C['objetivos'],
                 'provider': {'@type': 'EducationalOrganization', 'name': 'AcademiAmable', 'url': DOM + '/'},
                 'offers': {'@type': 'Offer', 'price': 0, 'priceCurrency': 'EUR', 'category': 'Free'},
                 'hasCourseInstance': {'@type': 'CourseInstance', 'courseMode': 'online', 'courseWorkload': f'PT{C["horas"]}H'},
                 'accessibilityFeature': ['simplifiedLanguage', 'readingOrder', 'highContrastDisplay', 'largePrint', 'ttsMarkup']}
    faq_sch = {'@context': 'https://schema.org', '@type': 'FAQPage',
               'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in C['faq']]}
    pagina(CURL.strip('/'), 'Curso de IA gratis desde cero, en versión Fácil | AcademiAmable',
           'Curso gratis de inteligencia artificial para empezar desde cero: qué es, tipos, ChatGPT y otras, cómo pedirle bien y usarla con cabeza. Versión Fácil y certificado.',
           cuerpo, activo='/cursos/', schema=[curso_sch, faq_sch], prioridad='0.9')


# ---------- Lección ----------
def leccion(Lc):
    m = next(x for x in C['modulos'] if x['n'] == Lc['modulo'])
    pasos_html = ''
    for i, (nombre, bloques) in enumerate(Lc['pasos'], 1):
        contenido = ''
        for bl in bloques:
            tipo = bl[0]
            if tipo == 'quiz':
                fs = ''
                for qi, (preg, opciones, expl) in enumerate(bl[1]):
                    ops = ''
                    for oi, (txt, ok, extra) in enumerate(opciones):
                        ops += (f'<label{" data-x" if extra else ""}><input type="radio" name="q{qi}" value="{oi}"{" data-ok" if ok else ""}>'
                                f'<span>{e(txt)}</span></label>')
                    fs += f'<fieldset><legend>{qi + 1}. {e(preg)}</legend>{ops}<p class="expl" hidden>{e(expl)}</p></fieldset>'
                contenido += (f'<form class="quiz" data-id="{Lc["id"]}"><p class="f-only" style="color:var(--m)">En lectura fácil verás solo 2 respuestas en cada pregunta.</p>{fs}'
                              f'<button class="btn" type="submit">Comprobar respuestas</button><p class="res" role="status" aria-live="polite"></p></form>')
            else:
                cls = {'info': 'info', 'tarea': 'tarea', 'dos': 'info', 'texto': ''}[tipo]
                contenido += B(bl[1], bl[2], clase=cls)
        pasos_html += (f'<li class="paso" id="paso-{i}"><h2><span class="num" aria-hidden="true">{i}</span>{e(nombre)}</h2>{contenido}</li>')
    conecta = ' y '.join(
        (f'<a href="{url_lec(lid)}">{e(t)}</a>' if lid in IDS_PUB else f'«{e(t)}» (próximamente)') for lid, t in Lc['conecta'])
    idx = [l[0] for l in TODAS].index(Lc['id'])
    sig = TODAS[idx + 1] if idx + 1 < len(TODAS) else None
    sig_html = (f'<a class="btn" href="{url_lec(sig[0])}">Siguiente lección</a>' if sig and sig[2]
                else (f'<p>La siguiente lección, «{e(sig[1])}», se publica muy pronto.</p>' if sig else ''))
    navp = ('<div class="nav-pasos"><button class="btn lin peq" type="button" data-paso="-1">Anterior</button>'
            '<span data-paso-txt aria-live="polite" style="align-self:center"></span>'
            '<button class="btn peq" type="button" data-paso="1">Siguiente</button></div>')
    borrador = '' if Lc['validada'] else '<p class="aviso" style="margin-top:14px"><b>Lección en prueba.</b> La versión Fácil está pendiente de validar con personas.</p>'
    cuerpo = f'''
<div class="lec-cab"><div class="c estrecho">
<p class="migas" style="margin-top:0"><a href="{CURL}">{e(C['titulo'])}</a> › Módulo {m['n']} · {e(m['titulo'])}</p>
<h1>{Lc['num']} · {e(Lc['titulo'])}</h1>
<p style="margin:0">{Lc['minutos']} minutos · 6 pasos · <button class="g" type="button" data-def="Pulsa el botón amarillo «A tu manera» para leer en fácil, escuchar o ver la lección paso a paso.">¿Cómo la quieres?</button></p>
{borrador}
</div></div>
<div class="c estrecho">
{navp}
<ol class="pasos">{pasos_html}</ol>
{navp}
<div class="fin-lec">
<p class="conecta"><b>Esto conecta con…</b> {conecta}.</p>
<button class="btn" type="button" data-terminar="{Lc['id']}">He terminado esta lección</button>
<p id="msg-fin" role="status" aria-live="polite" style="margin:10px 0 0;font-weight:700"></p>
</div>
<div class="tras-fin">{sig_html}</div>
</div>'''
    sch = {'@context': 'https://schema.org', '@type': 'LearningResource', 'name': f'{Lc["num"]} · {Lc["titulo"]}',
           'description': Lc['descripcion'], 'inLanguage': 'es', 'isAccessibleForFree': True, 'learningResourceType': 'Lesson',
           'timeRequired': f'PT{Lc["minutos"]}M', 'isPartOf': {'@type': 'Course', 'name': C['titulo'], 'url': DOM + CURL}}
    pagina(url_lec(Lc['id']).strip('/'), f'{Lc["titulo"]}: explicado fácil | Curso de IA gratis', Lc['descripcion'],
           cuerpo, activo='/cursos/', schema=[sch], prioridad='0.7')


# ---------- Mapa del curso ----------
def mapa():
    mods = C['modulos']
    COLW, X0, Y0, DY = 165, 85, 120, 92
    W = X0 * 2 + COLW * (len(mods) - 1)
    Hh = Y0 + DY * 3 + 70
    pos = {}
    for mi, m in enumerate(mods):
        k = len(m['lecciones'])
        for li, l in enumerate(m['lecciones']):
            pos[l[0]] = (X0 + mi * COLW, Y0 + li * DY + (4 - k) * DY / 2)
    lineas = ''
    for a, b in C['conexiones']:
        (x1, y1), (x2, y2) = pos[a], pos[b]
        if x1 == x2:
            d = f'M{x1:.0f} {y1:.0f} C{x1 - 40:.0f} {y1:.0f} {x2 - 40:.0f} {y2:.0f} {x2:.0f} {y2:.0f}'
        else:
            if x1 > x2:
                (x1, y1), (x2, y2) = (x2, y2), (x1, y1)
            mx = (x1 + x2) / 2
            d = f'M{x1:.0f} {y1:.0f} C{mx:.0f} {y1:.0f} {mx:.0f} {y2:.0f} {x2:.0f} {y2:.0f}'
        lineas += f'<path d="{d}" fill="none" stroke="#C9C9C2" stroke-width="2"/>'
    nodos = ''
    for mi, m in enumerate(mods):
        x = X0 + mi * COLW
        nodos += (f'<text x="{x}" y="38" text-anchor="middle" font-family="Montserrat,sans-serif" font-weight="800" font-size="15" fill="#0B7A7C">Módulo {m["n"]}</text>'
                  f'<text x="{x}" y="62" text-anchor="middle" font-family="Montserrat,sans-serif" font-weight="800" font-size="15" fill="#141414">{e(m["titulo"])}</text>')
        for l in m['lecciones']:
            px, py = pos[l[0]]
            c = f'<circle cx="{px:.0f}" cy="{py:.0f}" r="16" fill="{"#0B7A7C" if l[2] else "#FFFFFF"}" stroke="#0B7A7C" stroke-width="3"/>'
            corto = l[1] if len(l[1]) <= 24 else l[1][:22].rsplit(' ', 1)[0] + '…'
            t = f'<text x="{px:.0f}" y="{py + 36:.0f}" text-anchor="middle" font-family="Nunito,sans-serif" font-size="13" fill="#141414">{e(corto)}</text>'
            if l[2]:
                nodos += f'<a href="{url_lec(l[0])}">{c}{t}<title>{e(l[1])}</title></a>'
            else:
                nodos += f'<g>{c}{t}<title>{e(l[1])} (próximamente)</title></g>'
    svg = (f'<svg viewBox="0 0 {W} {Hh}" role="img" aria-labelledby="mapa-t"><title id="mapa-t">Mapa del curso: las lecciones de los 6 módulos y cómo se conectan</title>'
           f'{lineas}{nodos}</svg>')
    lista = ''.join(f'<li><b>Módulo {m["n"]} · {e(m["titulo"])}</b>: ' + '; '.join(
        (f'<a href="{url_lec(l[0])}">{e(l[1])}</a>' if l[2] else e(l[1])) for l in m['lecciones']) + '</li>' for m in C['modulos'])
    cuerpo = f'''
<div class="c"><p class="migas"><a href="/">Inicio</a> › <a href="{CURL}">{e(C['titulo'])}</a> › Mapa</p>
<h1>Mapa del curso</h1>
{B('<p>Nada se aprende suelto. Cada punto es una lección y cada línea une las que se relacionan. Los puntos verdes ya están abiertos: tócalos para entrar.</p>',
   '<p>Cada punto es una lección. Las líneas unen lecciones que se parecen. Los puntos verdes ya se pueden hacer.</p>')}
<div class="mapa">{svg}</div>
<h2>Las lecciones en lista</h2><ul>{lista}</ul>
</div>'''
    pagina(CURL.strip('/') + '/mapa', 'Mapa del curso de IA gratis | AcademiAmable',
           'Las lecciones del curso gratis IA sin miedo y cómo se conectan entre sí, de un vistazo.', cuerpo, activo='/cursos/', prioridad='0.5')


# ---------- Mi aprendizaje ----------
def mi_aprendizaje():
    insignias = ''.join(
        f'<div class="tar" data-insignia="{",".join(l[0] for l in m["lecciones"])}" hidden><span><span class="pill gratis">Insignia</span></span><h3>Módulo {m["n"]}: {e(m["titulo"])}</h3><p>Has terminado todas sus lecciones.</p></div>'
        for m in C['modulos'])
    ids = ','.join(l[0] for l in TODAS)
    cuerpo = f'''
<div class="c estrecho"><h1>Mi aprendizaje</h1>
{B('<p>Aquí ves lo que llevas hecho. Tu progreso se guarda solo en este móvil u ordenador: no hace falta registrarse y nadie más lo ve.</p>',
   '<p>Aquí ves lo que has hecho. Se guarda en tu móvil. No necesitas usuario ni contraseña.</p>')}
<h2>{e(C['titulo'])}</h2>
<p id="txt-mi" style="margin:0 0 6px"></p><div class="barra" data-barra="{ids}" data-txt="txt-mi"><i></i></div>
<p style="margin-top:14px"><a class="btn peq" href="{CURL}">Seguir con el curso</a></p>
<p id="sin-progreso" class="aviso">Todavía no has terminado ninguna lección. <a href="{url_lec(IDS_PUB[0])}">Empieza por la primera</a>.</p>
<h2>Insignias</h2><div class="rej">{insignias}</div>
<h2>Certificado</h2><p>Cuando termines los 6 módulos, aquí podrás descargar tu certificado en PDF con tu nombre y un código para comprobarlo.</p>
<h2>Seguir en otro dispositivo</h2>
<p>Copia tu código y pégalo en el otro móvil u ordenador, en esta misma página.</p>
<p><label for="codigo"><b>Tu código</b></label><br><textarea id="codigo" rows="3" style="width:100%;font:inherit;padding:12px;border-radius:12px;border:2px solid var(--l)"></textarea></p>
<div class="acc"><button class="btn" type="button" id="exportar">Copiar mi código</button><button class="btn lin" type="button" id="importar">Cargar un código</button></div>
<p id="msg-cod" role="status" aria-live="polite" style="font-weight:700;margin-top:10px"></p>
</div>'''
    pagina('mi-aprendizaje', 'Mi aprendizaje | AcademiAmable', 'Tu progreso, insignias y certificado en AcademiAmable, guardados en tu propio dispositivo.',
           cuerpo, activo='/mi-aprendizaje/', noindex=True)


# ---------- Talleres ----------
def talleres():
    msg = 'Hola, quiero que me aviséis de los próximos talleres de AcademiAmable.'
    cuerpo = f'''
<div class="c estrecho"><p class="migas"><a href="/">Inicio</a> › Talleres</p><h1>Talleres en directo</h1>
{B('<p>Sesiones de 1 a 2 horas, en persona en Jerez de los Caballeros y su comarca, u online. Grupos pequeños, mucha práctica y versión Fácil de todos los materiales.</p>',
   '<p>Los talleres son clases en directo. Pueden ser en persona o por internet. Son grupos pequeños.</p>')}
<h2>Próximos talleres</h2>
<p class="aviso">Estamos preparando el calendario. Escríbenos y te avisamos el primero.</p>
<a class="btn" href="https://wa.me/{WA}?text={msg.replace(' ', '%20')}">Avisadme por WhatsApp</a>
<h2>¿Quieres un taller para tu grupo?</h2><p>Lo organizamos para tu asociación, tu empresa o tu ayuntamiento. <a href="/entidades/">Mira la formación a medida</a>.</p>
</div>'''
    pagina('talleres', 'Talleres de inteligencia artificial en Extremadura | AcademiAmable',
           'Talleres prácticos de IA en Jerez de los Caballeros, su comarca y online. Grupos pequeños y materiales en lectura fácil.',
           cuerpo, activo='/talleres/', prioridad='0.6')


# ---------- Entidades ----------
def entidades():
    msg = 'Hola, queremos información sobre formación a medida de AcademiAmable para nuestro equipo.'
    cuerpo = f'''
<div class="c estrecho"><p class="migas"><a href="/">Inicio</a> › Para entidades y empresas</p>
<h1>Formación a medida para tu equipo</h1>
{B('<p>Llevamos AcademiAmable a tu asociación, empresa, centro educativo o ayuntamiento: formación en IA y tecnología adaptada a vuestro trabajo, con casos reales y materiales en lectura fácil.</p>',
   '<p>Damos clases a equipos de trabajo. Las clases se adaptan a cada equipo. Los materiales están en lectura fácil.</p>')}
<h2>Qué incluye</h2>
<ul class="lista-ok"><li>Diagnóstico corto de qué necesita tu equipo.</li><li>Sesiones en persona u online con tareas sobre vuestro propio trabajo.</li><li>Materiales accesibles: versión Fácil, audio e infografías.</li><li>Acceso a los cursos de la Academia para seguir practicando.</li></ul>
<h2>Para quién</h2><p>Entidades sociales, pymes, comercios, docentes, centros de mayores y ayuntamientos. Precio especial para entidades sociales y para clientes de <a href="https://esamable.es">IA-Mable</a>.</p>
<a class="btn" href="https://wa.me/{WA}?text={msg.replace(' ', '%20')}">Pedir información por WhatsApp</a>
</div>'''
    pagina('entidades', 'Formación en IA para entidades y empresas | AcademiAmable',
           'Formación a medida en inteligencia artificial para asociaciones, empresas, docentes y ayuntamientos, con materiales en lectura fácil.',
           cuerpo, activo='/entidades/', prioridad='0.6')


# ---------- Legal ----------
def legal():
    aviso = f'''<div class="c estrecho"><h1>Aviso legal</h1>
<p>Este sitio web, academiamable.es, es de la <b>{ENTIDAD['nombre']}</b>, con CIF {ENTIDAD['cif']}, domicilio en {ENTIDAD['dir']}, inscrita en el {ENTIDAD['registro']}. Contacto: {ENTIDAD['correo']} y WhatsApp {WA_TXT}.</p>
<h2>Uso del sitio</h2><p>Puedes usar los contenidos de AcademiAmable para aprender y para fines personales o educativos sin ánimo de lucro, citando la fuente. Para otros usos, pídenos permiso.</p>
<h2>Pictogramas</h2><p>Los pictogramas que puedan aparecer son de Sergio Palao, origen ARASAAC (arasaac.org), con licencia CC BY-NC-SA, propiedad del Gobierno de Aragón.</p>
<h2>Responsabilidad</h2><p>Los contenidos tienen fin formativo. Las herramientas de inteligencia artificial que se citan son de sus respectivas empresas y cambian a menudo; comprueba sus condiciones antes de usarlas.</p></div>'''
    pagina('aviso-legal', 'Aviso legal | AcademiAmable', 'Datos de la entidad titular de AcademiAmable y condiciones de uso.', aviso, prioridad='0.2')
    priv = f'''<div class="c estrecho"><h1>Política de privacidad</h1>
<p><b>Responsable:</b> {ENTIDAD['nombre']} (CIF {ENTIDAD['cif']}), {ENTIDAD['dir']}. Contacto: {ENTIDAD['correo']}.</p>
<h2>Qué datos tratamos</h2><p>Para hacer los cursos <b>no necesitas registrarte</b>. Tu progreso, tus respuestas y tus preferencias de «A tu manera» se guardan solo en tu navegador (almacenamiento local) y no nos llegan.</p>
<p>Si nos escribes por WhatsApp o por correo, tratamos tu nombre, tu teléfono o correo y lo que nos cuentes, solo para contestarte o avisarte de talleres. La base legal es tu consentimiento al escribirnos. Lo guardamos mientras haga falta para atenderte o hasta que nos pidas borrarlo.</p>
<h2>Tus derechos</h2><p>Puedes pedir acceso, rectificación, supresión, oposición, limitación y portabilidad escribiendo a {ENTIDAD['correo']}. Si no te atendemos bien, puedes reclamar ante la Agencia Española de Protección de Datos (aepd.es).</p>
<h2>Servicios de terceros</h2><p>La web se aloja en OVHcloud, en la Unión Europea. No usamos herramientas de publicidad ni de seguimiento.</p></div>'''
    pagina('privacidad', 'Política de privacidad | AcademiAmable', 'Cómo trata AcademiAmable tus datos: sin registro y con tu progreso guardado solo en tu dispositivo.', priv, prioridad='0.2')
    cook = '''<div class="c estrecho"><h1>Política de cookies</h1>
<p>AcademiAmable <b>no usa cookies</b> de análisis, publicidad ni seguimiento.</p>
<p>Usa el almacenamiento local de tu navegador solo para cosas que tú eliges: tus preferencias de «A tu manera» (aa-prefs) y tu progreso en los cursos (aa-progreso). También guarda en caché las páginas que visitas para que funcionen sin conexión. Son técnicas, necesarias para el servicio que pides, y no necesitan consentimiento.</p>
<p>Puedes borrarlas cuando quieras desde la configuración de tu navegador. Si lo haces, perderás tu progreso salvo que hayas copiado tu código en «Mi aprendizaje».</p></div>'''
    pagina('cookies', 'Política de cookies | AcademiAmable', 'AcademiAmable no usa cookies de seguimiento: solo almacenamiento local técnico para tu progreso.', cook, prioridad='0.2')


def error404():
    pagina('404', 'Página no encontrada | AcademiAmable', 'Esta página no existe.',
           '<div class="c estrecho"><h1>Esta página no existe</h1><p>Puede que la dirección esté mal escrita o que la lección todavía no esté publicada.</p><a class="btn" href="/">Ir al inicio</a></div>',
           noindex=True)
    os.replace(os.path.join(RAIZ, '404', 'index.html'), os.path.join(RAIZ, '404.html'))
    os.rmdir(os.path.join(RAIZ, '404'))


# ---------- Archivos técnicos ----------
def tecnicos():
    escribir('estilos.css', re.sub(r'\n\s*', '\n', CSS))
    escribir('app.js', JS)
    urls = ''.join(f'<url><loc>{DOM}/{r + "/" if r else ""}</loc><lastmod>{HOY}</lastmod><priority>{p}</priority></url>' for r, p in PAGINAS)
    escribir('sitemap.xml', f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
    escribir('robots.txt', f'User-agent: *\nAllow: /\nDisallow: /mi-aprendizaje/\n\n'
             '# Bienvenidos los buscadores con IA\nUser-agent: GPTBot\nAllow: /\nUser-agent: OAI-SearchBot\nAllow: /\nUser-agent: ChatGPT-User\nAllow: /\n'
             'User-agent: ClaudeBot\nAllow: /\nUser-agent: Claude-SearchBot\nAllow: /\nUser-agent: PerplexityBot\nAllow: /\nUser-agent: Google-Extended\nAllow: /\n\n'
             f'Sitemap: {DOM}/sitemap.xml\n')
    ll = '\n'.join(f'- [{t}]({u}): {d}' for t, u, d in LLMS)
    escribir('llms.txt', '# AcademiAmable\n\n> AcademiAmable (academiamable.es) es la academia online de la Asociación Euexia Rural, entidad social de '
             'Jerez de los Caballeros (Badajoz, Extremadura). Ofrece cursos, píldoras y talleres para aprender a usar la inteligencia artificial y la '
             'tecnología. Todo tiene versión en lectura fácil validada por personas, audio y opciones de accesibilidad. El primer curso, «IA sin miedo», '
             'es gratis, sin registro y con certificado. Es la hermana formativa de IA-Mable (esamable.es).\n\n'
             f'Contacto: WhatsApp {WA_TXT} · {DOM}\n\n## Páginas\n{ll}\n')
    escribir('manifest.webmanifest', json.dumps({
        'name': 'AcademiAmable', 'short_name': 'AcademiAmable', 'description': 'Aprender, a tu manera.', 'lang': 'es',
        'start_url': '/', 'scope': '/', 'display': 'standalone', 'background_color': '#FFFFFF', 'theme_color': '#FFD90F',
        'icons': [{'src': '/img/icono-192.png', 'sizes': '192x192', 'type': 'image/png'},
                  {'src': '/img/icono-512.png', 'sizes': '512x512', 'type': 'image/png', 'purpose': 'any maskable'},
                  {'src': '/favicon.svg', 'sizes': 'any', 'type': 'image/svg+xml'}]}, ensure_ascii=False, indent=1))
    escribir('sw.js', f'''// AcademiAmable · funciona sin conexión con las páginas ya abiertas.
const V = 'aa-{huella(CSS + JS + HOY)}';
const BASE = ['/', '/estilos.css?v={V_CSS}', '/app.js?v={V_JS}', '/img/logo.svg', '/fonts/montserrat-latin.woff2', '/fonts/nunito-latin.woff2', '/mi-aprendizaje/'];
self.addEventListener('install', e => {{ e.waitUntil(caches.open(V).then(c => c.addAll(BASE)).then(() => self.skipWaiting())); }});
self.addEventListener('activate', e => {{ e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== V).map(k => caches.delete(k)))).then(() => self.clients.claim())); }});
self.addEventListener('fetch', e => {{
  const r = e.request;
  if (r.method !== 'GET' || new URL(r.url).origin !== location.origin) return;
  if (r.mode === 'navigate') {{
    e.respondWith(fetch(r).then(res => {{ const c = res.clone(); caches.open(V).then(k => k.put(r, c)); return res; }})
      .catch(() => caches.match(r).then(m => m || caches.match('/'))));
  }} else {{
    e.respondWith(caches.match(r).then(m => m || fetch(r).then(res => {{ const c = res.clone(); caches.open(V).then(k => k.put(r, c)); return res; }})));
  }}
}});
''')


if __name__ == '__main__':
    portada(); catalogo(); ficha()
    for Lc in LECCIONES.values():
        leccion(Lc)
    mapa(); mi_aprendizaje(); talleres(); entidades(); legal(); error404(); tecnicos()
    print(f'{len(PAGINAS)} páginas indexables generadas.')
