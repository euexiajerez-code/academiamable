#!/usr/bin/env python3
"""Ilustraciones propias de AcademiAmable (SVG planos, sin fotos ni recursos externos).

    python3 _src/ilustraciones.py      (build.py también las genera)

Escribe img/ilus/*.svg. Todo se dibuja aquí con la paleta de la marca, así que se pueden
retocar colores o formas y volver a generar. Son decorativas: en la web van con alt="".
"""
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEST = os.path.join(RAIZ, 'img', 'ilus')

# Paleta (marca + tonos de apoyo; ver contrastes en LEEME.md)
K, Y, T, T2, R, W, G = '#141414', '#FFD90F', '#0B7A7C', '#08605F', '#E30613', '#FFFFFF', '#F5F5F2'
MENTA, CORAL, LILA, CIELO, SALVIA = '#6FCFC4', '#FF9573', '#B9A6F2', '#84C8EE', '#A6D38A'
PALIDO = {'menta': '#DDF3F0', 'amarillo': '#FFF4B8', 'coral': '#FFE5DB', 'lila': '#EEE8FD', 'cielo': '#DFF1FB', 'salvia': '#E7F4DE'}
ENCINA, ENCINA2, TEJA, TEJA2, PASTO = '#3F6B33', '#2F5426', '#E2704C', '#C95A38', '#F2D27A'
PIEL = ['#F5C9A8', '#E0AA82', '#B57650', '#7A4A2C']
PELO = {'castano': '#4A2E1C', 'negro': K, 'gris': '#D4D4D0', 'rubio': '#E8B84A', 'canoso': '#9C9C98'}

# Colores de los módulos (texto negro encima: ver contrastes en LEEME.md)
MODULOS = [(Y, PALIDO['amarillo']), (MENTA, PALIDO['menta']), (CORAL, PALIDO['coral']),
           (LILA, PALIDO['lila']), (CIELO, PALIDO['cielo']), (SALVIA, PALIDO['salvia'])]


def svg(w, h, cuerpo, defs=''):
    d = f'<defs>{defs}</defs>' if defs else ''
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">{d}{cuerpo}</svg>'


def chispa(x, y, s, c=K):
    """Destello de cuatro puntas."""
    return (f'<path d="M{x} {y - s}Q{x} {y} {x + s} {y}Q{x} {y} {x} {y + s}Q{x} {y} {x - s} {y}Q{x} {y} {x} {y - s}Z" fill="{c}"/>')


def bocadillo(x, y, w, h, c, cola='bi', rad=18):
    """Bocadillo de chat con cola abajo a la izquierda (bi) o a la derecha (bd)."""
    if cola == 'bi':
        t = f'M{x + 22} {y + h - 2}l-10 22l30-22z'
    else:
        t = f'M{x + w - 22} {y + h - 2}l10 22l-30-22z'
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rad}" fill="{c}"/><path d="{t}" fill="{c}"/>'


def busto(piel, pelo='corto', color_pelo=K, ropa=T, extra='', gafas=False, pendientes=None, cuello=None, boca='sonrisa'):
    """Persona de medio cuerpo en coordenadas locales: (0,0) es el centro de la base."""
    p = ''
    # Pelo por detrás
    if pelo == 'media':
        p += f'<path d="M-46 -150C-50 -205 50 -205 46 -150L48 -98C30 -92 -30 -92 -48 -98Z" fill="{color_pelo}"/>'
    elif pelo == 'larga':
        p += f'<path d="M-46 -150C-50 -205 50 -205 46 -150L52 -60C30 -50 -30 -50 -52 -60Z" fill="{color_pelo}"/>'
    elif pelo == 'mono':
        p += f'<circle cx="0" cy="-198" r="19" fill="{color_pelo}"/>'
    elif pelo == 'rizos':
        for cx, cy, r in [(-34, -172, 18), (-20, -190, 19), (2, -196, 20), (24, -190, 19), (36, -172, 17), (-40, -150, 14), (42, -150, 13)]:
            p += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{color_pelo}"/>'
    # Cuello y cuerpo
    p += f'<rect x="-13" y="-122" width="26" height="30" rx="6" fill="{piel}"/>'
    p += f'<path d="M-84 0C-84 -66 -58 -100 0 -102C58 -100 84 -66 84 0Z" fill="{ropa}"/>'
    p += f'<path d="M-15 -101L0 -80L15 -101Z" fill="{piel}"/>'
    if cuello:
        p += f'<path d="M-24 -100L0 -76L-6 -100ZM24 -100L0 -76L6 -100Z" fill="{cuello}"/>'
    # Cabeza
    p += f'<circle cx="-38" cy="-148" r="9" fill="{piel}"/><circle cx="38" cy="-148" r="9" fill="{piel}"/>'
    p += f'<circle cx="0" cy="-150" r="39" fill="{piel}"/>'
    if pendientes:
        p += f'<circle cx="-39" cy="-134" r="5" fill="{pendientes}"/><circle cx="39" cy="-134" r="5" fill="{pendientes}"/>'
    # Pelo por delante
    if pelo in ('corto', 'media', 'larga', 'mono'):
        p += f'<path d="M-41 -150C-44 -198 44 -198 41 -150C38 -166 26 -178 4 -176C-14 -175 -30 -166 -41 -150Z" fill="{color_pelo}"/>'
    elif pelo == 'rizos':
        p += f'<path d="M-40 -150C-42 -192 42 -192 40 -150C30 -170 -30 -170 -40 -150Z" fill="{color_pelo}"/>'
    elif pelo == 'gorra':
        p += f'<path d="M-42 -156C-42 -200 42 -200 42 -156Z" fill="{color_pelo}"/><path d="M-42 -158H62a8 8 0 0 1 0 12H-42Z" fill="{color_pelo}"/>'
    elif pelo == 'calvo':
        p += f'<path d="M-40 -140C-42 -160 -38 -170 -30 -176L-28 -150ZM40 -140C42 -160 38 -170 30 -176L28 -150Z" fill="{color_pelo}"/>'
    # Cara
    p += f'<circle cx="-14" cy="-150" r="4" fill="{K}"/><circle cx="14" cy="-150" r="4" fill="{K}"/>'
    p += f'<circle cx="-24" cy="-134" r="7" fill="{CORAL}" opacity=".45"/><circle cx="24" cy="-134" r="7" fill="{CORAL}" opacity=".45"/>'
    if boca == 'sonrisa':
        p += f'<path d="M-12 -130Q0 -119 12 -130" stroke="{K}" stroke-width="4" fill="none" stroke-linecap="round"/>'
    else:
        p += f'<path d="M-12 -131Q0 -116 12 -131Z" fill="{K}"/>'
    if gafas:
        p += (f'<g fill="none" stroke="{K}" stroke-width="3.5"><circle cx="-15" cy="-150" r="11"/><circle cx="15" cy="-150" r="11"/>'
              f'<path d="M-4 -151h8M-26 -152l-11-3M26 -152l11-3"/></g>')
    return p + extra


def movil(x, y, ang=-8, w=46, h=78):
    return (f'<g transform="rotate({ang} {x + w / 2} {y + h / 2})"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="9" fill="{K}"/>'
            f'<rect x="{x + 5}" y="{y + 8}" width="{w - 10}" height="{h - 16}" rx="4" fill="{MENTA}"/>'
            f'<rect x="{x + 10}" y="{y + 16}" width="{w - 24}" height="10" rx="5" fill="{W}"/>'
            f'<rect x="{x + 14}" y="{y + 32}" width="{w - 24}" height="10" rx="5" fill="{Y}"/></g>')


def encina(x, y, s=1.0):
    return (f'<g transform="translate({x} {y}) scale({s})"><rect x="-5" y="-30" width="10" height="34" rx="3" fill="#6B4A2E"/>'
            f'<ellipse cx="0" cy="-44" rx="38" ry="24" fill="{ENCINA}"/><ellipse cx="-14" cy="-52" rx="20" ry="14" fill="#4E7F40"/></g>')


def casa(x, y, w, h, tejado=TEJA, ventana=True):
    s = (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{W}"/>'
         f'<path d="M{x - 4} {y}L{x + w / 2} {y - h * .45}L{x + w + 4} {y}Z" fill="{tejado}"/>'
         f'<rect x="{x}" y="{y + h - 6}" width="{w}" height="6" fill="{Y}"/>')
    if ventana:
        s += f'<rect x="{x + w * .3}" y="{y + h * .3}" width="{w * .4}" height="{h * .32}" rx="3" fill="{T2}"/>'
    return s


# ---------- Portada ----------
def portada():
    defs = '<clipPath id="v"><circle cx="300" cy="270" r="248"/></clipPath>'
    esc = f'<circle cx="300" cy="270" r="248" fill="{PALIDO["menta"]}"/>'
    g = '<g clip-path="url(#v)">'
    g += f'<circle cx="430" cy="130" r="34" fill="{W}"/>'
    # Sierra y lomas
    g += f'<path d="M40 330C120 250 190 262 260 300C330 250 420 230 560 300V560H40Z" fill="{SALVIA}"/>'
    # Pueblo en el cerro: castillo, torre y casas encaladas
    g += f'<path d="M300 268h120v-36h10v-10h10v10h10v-10h10v10h10v-10h10v46h8v40H300Z" fill="#EDE6D6"/>'
    g += f'<rect x="352" y="170" width="34" height="108" fill="{W}"/><path d="M346 172L369 120L392 172Z" fill="{TEJA}"/>'
    g += f'<rect x="362" y="188" width="14" height="22" rx="7" fill="{T2}"/><rect x="362" y="226" width="14" height="22" rx="7" fill="{T2}"/>'
    g += f'<rect x="349" y="210" width="40" height="6" fill="{Y}"/><circle cx="369" cy="114" r="5" fill="{K}"/>'
    for x, y, w, h in [(170, 276, 48, 40), (222, 286, 40, 34), (264, 280, 52, 44), (420, 292, 44, 38), (466, 284, 52, 44), (120, 296, 44, 36)]:
        g += casa(x, y, w, h)
    g += f'<path d="M40 360C150 320 250 330 330 356C410 330 480 330 560 350V560H40Z" fill="#8CC46E"/>'
    g += f'<path d="M40 400C160 370 300 372 560 398V560H40Z" fill="{PASTO}"/>'
    g += encina(110, 392, 1.0) + encina(470, 388, 1.15) + encina(536, 420, .8) + encina(70, 430, .75)
    g += '</g>'
    # Carmen con el móvil
    carmen = busto(PIEL[1], 'rizos', PELO['castano'], T, pendientes=Y, cuello=W)
    brazo = (f'<path d="M58 -78C88 -40 70 -10 30 -40" stroke="{T2}" stroke-width="34" fill="none" stroke-linecap="round"/>'
             + movil(-6, -108, -10) + f'<circle cx="24" cy="-42" r="16" fill="{PIEL[1]}"/>')
    persona = f'<g transform="translate(250 562) scale(1.32)">{carmen}{brazo}</g>'
    # Bocadillos de la IA
    burbujas = (bocadillo(372, 330, 176, 76, W, 'bi', 22)
                + f'<rect x="394" y="352" width="110" height="10" rx="5" fill="{K}"/><rect x="394" y="374" width="76" height="10" rx="5" fill="{K}" opacity=".35"/>'
                + bocadillo(56, 86, 132, 64, T, 'bd', 22)
                + f'<circle cx="94" cy="118" r="8" fill="{W}"/><circle cx="122" cy="118" r="8" fill="{W}"/><circle cx="150" cy="118" r="8" fill="{W}"/>'
                + f'<circle cx="538" cy="332" r="9" fill="{R}"/>')
    chispas = chispa(214, 70, 22) + chispa(250, 112, 11) + chispa(540, 250, 16, W) + chispa(58, 300, 14, W) + chispa(520, 446, 12)
    sombra = ''
    return svg(600, 560, esc + g + sombra + persona + burbujas + chispas, defs)


# ---------- Emblemas de módulo ----------
def emblema(n):
    fuerte, palido = MODULOS[n - 1]
    fondo = f'<rect width="160" height="160" rx="40" fill="{fuerte}"/>'
    luz = f'<path d="M40 0H120A40 40 0 0 1 160 40V60C110 30 60 30 0 70V40A40 40 0 0 1 40 0Z" fill="{W}" opacity=".22"/>'
    if n == 1:   # ¿Qué es la IA? bocadillo con interrogación
        d = (bocadillo(30, 34, 100, 78, W, 'bi', 24)
             + f'<path d="M66 62a14 14 0 1 1 20 12c-5 3-6 6-6 10" stroke="{K}" stroke-width="9" fill="none" stroke-linecap="round"/>'
             + f'<circle cx="80" cy="99" r="5.5" fill="{K}"/>' + chispa(126, 34, 14, K))
    elif n == 2:  # Tipos de IA: clasificar formas
        d = (f'<circle cx="54" cy="56" r="22" fill="{W}"/><rect x="88" y="34" width="44" height="44" rx="8" fill="{K}"/>'
             f'<path d="M54 92L78 132H30Z" fill="{T2}"/><rect x="88" y="92" width="44" height="40" rx="20" fill="{W}" stroke="{K}" stroke-width="6"/>')
    elif n == 3:  # Las más usadas: móvil con apps
        d = (f'<rect x="46" y="22" width="68" height="116" rx="14" fill="{K}"/><rect x="53" y="34" width="54" height="92" rx="6" fill="{W}"/>'
             + ''.join(f'<rect x="{60 + c * 22}" y="{42 + r * 22}" width="16" height="16" rx="5" fill="{col}"/>'
                       for r, fila in enumerate([(T, Y), (CORAL, LILA), (CIELO, T)]) for c, col in enumerate(fila))
             + f'<rect x="60" y="108" width="40" height="8" rx="4" fill="{K}" opacity=".3"/>' + chispa(128, 40, 13, K))
    elif n == 4:  # Pedir bien: mensaje y lápiz
        d = (bocadillo(24, 30, 98, 70, W, 'bi', 20)
             + f'<rect x="40" y="50" width="62" height="9" rx="4.5" fill="{K}"/><rect x="40" y="70" width="40" height="9" rx="4.5" fill="{K}" opacity=".35"/>'
             + f'<g transform="rotate(40 112 104)"><rect x="100" y="56" width="24" height="70" rx="4" fill="{Y}"/><rect x="100" y="56" width="24" height="14" rx="4" fill="{K}"/>'
             f'<path d="M100 126L112 148L124 126Z" fill="{W}"/><path d="M108 140L112 148L116 140Z" fill="{K}"/></g>')
    elif n == 5:  # Con cabeza: escudo con visto bueno
        d = (f'<path d="M80 24L128 42V80C128 110 106 130 80 140C54 130 32 110 32 80V42Z" fill="{W}"/>'
             f'<path d="M80 24L128 42V80C128 110 106 130 80 140Z" fill="{K}" opacity=".08"/>'
             f'<path d="M58 82L74 98L104 66" stroke="{T2}" stroke-width="12" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
    else:        # En tu vida: casa del pueblo con destello
        d = (f'<rect x="38" y="76" width="84" height="58" fill="{W}"/><path d="M28 80L80 36L132 80Z" fill="{TEJA}"/>'
             f'<rect x="38" y="126" width="84" height="8" fill="{Y}"/><rect x="70" y="98" width="22" height="36" rx="11" fill="{T2}"/>'
             f'<rect x="48" y="90" width="14" height="16" rx="3" fill="{K}"/><rect x="100" y="90" width="14" height="16" rx="3" fill="{K}"/>' + chispa(128, 30, 15, K))
    return svg(160, 160, fondo + luz + d)


# ---------- Iconos: A tu manera y ciclo de la lección ----------
def icono(fondo, d):
    return svg(96, 96, f'<circle cx="48" cy="48" r="48" fill="{fondo}"/>' + d)


ICONOS = {
    # A tu manera
    'facil': lambda: icono(Y, f'<path d="M18 30C30 24 40 26 48 32V74C40 68 30 66 18 72Z" fill="{W}"/><path d="M78 30C66 24 56 26 48 32V74C56 68 66 66 78 72Z" fill="{W}"/>'
                              f'<path d="M48 32V74" stroke="{K}" stroke-width="4"/><path d="M26 42h14M26 52h12M56 42h14M56 52h10" stroke="{K}" stroke-width="4" stroke-linecap="round"/>'),
    'oir': lambda: icono(MENTA, f'<path d="M20 40h12l16-14v44L32 56H20Z" fill="{K}"/><path d="M58 38a14 14 0 0 1 0 20M66 30a26 26 0 0 1 0 36" stroke="{K}" stroke-width="6" fill="none" stroke-linecap="round"/>'),
    'grande': lambda: icono(CORAL, f'<path d="M20 70L36 26L52 70M26 56h20" stroke="{K}" stroke-width="8" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
                                   f'<path d="M58 70L66 48L74 70M61 62h10" stroke="{K}" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'),
    'contraste': lambda: icono(LILA, f'<circle cx="48" cy="48" r="26" fill="{W}" stroke="{K}" stroke-width="5"/><path d="M48 22A26 26 0 0 1 48 74Z" fill="{K}"/>'),
    'pasos': lambda: icono(CIELO, f'<path d="M18 74V62H36V48H54V34H72V22" stroke="{K}" stroke-width="7" fill="none" stroke-linecap="round" stroke-linejoin="round"/><circle cx="72" cy="22" r="7" fill="{R}"/>'),
    'glosario': lambda: icono(SALVIA, bocadillo(18, 22, 60, 44, W, 'bi', 14) + f'<rect x="28" y="38" width="40" height="8" rx="4" fill="{K}"/>'
                                     + f'<path d="M28 76h40" stroke="{K}" stroke-width="5" stroke-dasharray="2 7" stroke-linecap="round"/>'),
    'ritmo': lambda: icono(Y, f'<circle cx="52" cy="46" r="22" fill="{T}"/><path d="M52 46m-10 0a10 10 0 1 1 10 10" stroke="{W}" stroke-width="5" fill="none" stroke-linecap="round"/>'
                              f'<path d="M16 74C16 58 22 52 30 52C38 52 40 60 40 66H80a8 8 0 0 1 0 8Z" fill="{K}"/><path d="M24 54l-6-14M32 53l2-15" stroke="{K}" stroke-width="4" stroke-linecap="round"/><circle cx="18" cy="39" r="4" fill="{K}"/><circle cx="34" cy="37" r="4" fill="{K}"/>'),
    # Ciclo de la lección
    'situacion': lambda: icono(Y, f'<rect x="16" y="24" width="64" height="44" rx="10" fill="{K}"/><path d="M42 36L58 46L42 56Z" fill="{Y}"/><path d="M36 76h24" stroke="{K}" stroke-width="6" stroke-linecap="round"/>'),
    'descubre': lambda: icono(MENTA, f'<path d="M48 18a22 22 0 0 0-13 40v8h26v-8a22 22 0 0 0-13-40Z" fill="{W}"/><rect x="36" y="70" width="24" height="9" rx="4.5" fill="{K}"/>'
                                     f'<path d="M38 48l5-7l5 7l5-7l5 7" stroke="{K}" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
                                     + chispa(76, 22, 9, K)),
    'prueba': lambda: icono(CORAL, f'<rect x="30" y="14" width="40" height="66" rx="9" fill="{K}"/><rect x="35" y="22" width="30" height="50" rx="4" fill="{W}"/>'
                                   f'<circle cx="50" cy="46" r="9" fill="{T}"/><path d="M50 46l22 22" stroke="{K}" stroke-width="8" stroke-linecap="round"/><path d="M50 46l22 22" stroke="{Y}" stroke-width="3" stroke-linecap="round"/>'),
    'conecta': lambda: icono(LILA, f'<path d="M26 64L48 30L72 62Z" stroke="{K}" stroke-width="5" fill="none" stroke-linejoin="round"/>'
                                   f'<circle cx="48" cy="30" r="11" fill="{W}" stroke="{K}" stroke-width="5"/><circle cx="26" cy="64" r="11" fill="{T}"/><circle cx="72" cy="62" r="11" fill="{Y}" stroke="{K}" stroke-width="5"/>'),
    'comparte': lambda: icono(CIELO, bocadillo(12, 18, 46, 34, W, 'bi', 12) + bocadillo(38, 44, 46, 34, K, 'bd', 12)
                                     + f'<circle cx="52" cy="61" r="4" fill="{W}"/><circle cx="64" cy="61" r="4" fill="{W}"/><circle cx="76" cy="61" r="4" fill="{W}"/>'),
    'piensa': lambda: icono(SALVIA, f'<path d="M30 58a14 14 0 0 1 2-28a18 18 0 0 1 32 0a14 14 0 0 1 2 28Z" fill="{W}"/><circle cx="34" cy="70" r="6" fill="{W}"/><circle cx="24" cy="80" r="4" fill="{W}"/>'
                                    f'<path d="M44 38a6 6 0 1 1 8 6c-3 2-4 3-4 6" stroke="{K}" stroke-width="4.5" fill="none" stroke-linecap="round"/><circle cx="48" cy="55" r="3" fill="{K}"/>'),
}


# ---------- Para quién: figuras ----------
def figura(fondo, persona, extra=''):
    return svg(240, 200, f'<rect width="240" height="200" fill="{fondo}"/><circle cx="120" cy="214" r="150" fill="{W}" opacity=".55"/>'
               + extra + f'<g transform="translate(120 200) scale(.82)">{persona}</g>')


def publico():
    out = {}
    # Pymes y autónomos: tendero con delantal y toldo
    toldo = ''.join(f'<path d="M{x} 18h30v26a15 15 0 0 1-30 0Z" fill="{c}"/>' for x, c in zip(range(0, 240, 30), [T, W] * 4))
    tendero = busto(PIEL[2], 'calvo', K, CIELO, extra=f'<path d="M-44 0V-70C-30 -62 30 -62 44 -70V0Z" fill="{Y}"/><rect x="-14" y="-40" width="28" height="18" rx="4" fill="{K}" opacity=".2"/>'
                    f'<path d="M-16 -137Q-8 -143 0 -138Q8 -143 16 -137" stroke="{K}" stroke-width="6" fill="none" stroke-linecap="round"/>')
    out['publico-negocio'] = figura(PALIDO['coral'], tendero, toldo)
    # Mayores y vecinos: mujer mayor con moño, gafas y móvil
    mayor = busto(PIEL[0], 'mono', PELO['gris'], LILA, gafas=True, pendientes=T,
                  extra=f'<path d="M-54 -64C-80 -20 -40 -10 -10 -40" stroke="#9A86DE" stroke-width="30" fill="none" stroke-linecap="round"/>'
                  + movil(-30, -94, 10, 40, 66) + f'<circle cx="-14" cy="-44" r="14" fill="{PIEL[0]}"/>')
    out['publico-mayores'] = figura(PALIDO['lila'], mayor, encina(36, 150, .7) + encina(206, 140, .55))
    # Comprensión: joven en silla de ruedas con cascos
    silla = (f'<rect x="150" y="70" width="14" height="104" rx="6" fill="{K}"/><rect x="62" y="150" width="104" height="14" rx="7" fill="{K}"/>')
    rueda = (f'<circle cx="104" cy="164" r="46" fill="none" stroke="{K}" stroke-width="9"/><circle cx="104" cy="164" r="36" fill="none" stroke="{K}" stroke-width="3" opacity=".5"/>'
             f'<circle cx="104" cy="164" r="7" fill="{K}"/><circle cx="190" cy="190" r="9" fill="{K}"/><path d="M164 166L190 182" stroke="{K}" stroke-width="6"/>')
    joven = busto(PIEL[3], 'corto', K, Y, extra=(
        f'<path d="M-44 -150C-44 -210 44 -210 44 -150" stroke="{T2}" stroke-width="8" fill="none"/>'
        f'<rect x="-52" y="-166" width="18" height="34" rx="8" fill="{T2}"/><rect x="34" y="-166" width="18" height="34" rx="8" fill="{T2}"/>'))
    out['publico-comprension'] = svg(240, 200, f'<rect width="240" height="200" fill="{PALIDO["cielo"]}"/><circle cx="120" cy="214" r="150" fill="{W}" opacity=".55"/>'
                                     + chispa(206, 46, 12) + silla + f'<g transform="translate(110 168) scale(.72)">{joven}</g>' + rueda)
    # Entidades y docentes: docente ante una pizarra
    pizarra = (f'<rect x="132" y="26" width="92" height="66" rx="8" fill="{T2}"/><rect x="146" y="42" width="50" height="7" rx="3.5" fill="{W}"/>'
               f'<rect x="146" y="58" width="32" height="7" rx="3.5" fill="{Y}"/>' + chispa(206, 70, 8, W))
    docente = busto(PIEL[2], 'larga', PELO['negro'], T, pendientes=Y,
                    extra=f'<path d="M60 -80C86 -110 100 -140 110 -150" stroke="{T2}" stroke-width="28" fill="none" stroke-linecap="round"/><circle cx="112" cy="-156" r="14" fill="{PIEL[2]}"/>')
    out['publico-entidades'] = svg(240, 200, f'<rect width="240" height="200" fill="{PALIDO["salvia"]}"/><circle cx="120" cy="214" r="150" fill="{W}" opacity=".55"/>'
                                   + pizarra + f'<g transform="translate(92 200) scale(.8)">{docente}</g>')
    return {k: v.replace('viewBox="0 0 240 200" width="240" height="200"', 'viewBox="0 10 240 180" width="240" height="180"') for k, v in out.items()}


# ---------- Estados vacíos y 404 ----------
def vacio():
    return svg(240, 200, f'<circle cx="120" cy="104" r="88" fill="{PALIDO["menta"]}"/>'
               f'<path d="M120 128C120 96 112 80 92 70C110 64 124 76 120 100C126 74 146 66 160 74C140 80 124 96 124 128Z" fill="{ENCINA}"/>'
               f'<path d="M84 128H156L148 182H92Z" fill="{TEJA}"/><rect x="78" y="122" width="84" height="16" rx="6" fill="{TEJA2}"/>'
               + chispa(170, 48, 14) + chispa(66, 70, 9, T) + f'<circle cx="186" cy="92" r="6" fill="{R}"/>')


def e404():
    return svg(320, 240, f'<circle cx="160" cy="124" r="110" fill="{PALIDO["amarillo"]}"/>'
               f'<path d="M30 200C90 170 150 176 290 196V240H30Z" fill="{SALVIA}"/>'
               f'<rect x="152" y="60" width="14" height="150" rx="5" fill="#6B4A2E"/>'
               f'<path d="M166 66H246L264 86L246 106H166Z" fill="{T}"/><path d="M152 112H74L56 132L74 152H152Z" fill="{W}"/>'
               f'<rect x="180" y="80" width="56" height="10" rx="5" fill="{W}"/><rect x="84" y="126" width="54" height="10" rx="5" fill="{K}"/>'
               + encina(258, 206, .8) + encina(50, 206, .6)
               + f'<path d="M150 30a12 12 0 1 1 16 11c-4 2-5 4-5 8" stroke="{K}" stroke-width="6" fill="none" stroke-linecap="round"/><circle cx="161" cy="58" r="0" fill="{K}"/>'
               + chispa(222, 34, 10) + chispa(100, 50, 7, T))


def generar():
    os.makedirs(DEST, exist_ok=True)
    piezas = {'portada': portada(), 'vacio': vacio(), '404': e404()}
    for n in range(1, 7):
        piezas[f'modulo-{n}'] = emblema(n)
    for k, f in ICONOS.items():
        piezas[f'ico-{k}'] = f()
    piezas.update(publico())
    for k, s in piezas.items():
        with open(os.path.join(DEST, k + '.svg'), 'w', encoding='utf-8') as fh:
            fh.write(s)
    return piezas


if __name__ == '__main__':
    p = generar()
    for k, s in sorted(p.items()):
        print(f'{k:22} {len(s.encode()) / 1024:5.1f} KB')
