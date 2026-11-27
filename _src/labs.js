/* AcademiAmable · Laboratorios del «Método AcademiAmable: aprender tocando».
   Sin librerías ni conexión. Cada laboratorio se declara en la lección como ('lab', {...});
   build.py deja su configuración en <script type="application/json" id="app-ID-cfg"> junto a
   <div class="lab-app" id="app-ID">. Los resultados se guardan en 'aa-progreso' a través de
   window.AA (app.js): prog.labs[id] = nota de 0 a 1, prog.meta[lección] = seguridad de cada
   respuesta, prog.leitner = cajas del repaso, prog.estado[id] = estado guardado de un laboratorio. */
(function () {
  'use strict';
  var H = document.documentElement;
  var AA = window.AA || { prog: {}, guardar: function () {} };
  var P = AA.prog;
  ['labs', 'meta', 'leitner', 'estado'].forEach(function (k) { P[k] = P[k] || {}; });
  var RM = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  var uid = 0;
  function F() { return H.classList.contains('is-facil'); }
  function tx(o, k) { k = k || 't'; return (F() && o[k + 'f']) ? o[k + 'f'] : o[k]; }
  function enFacil(lista, n) {
    if (!F()) return lista.slice();
    var f = lista.filter(function (x) { return x.f; });
    return f.length ? f : lista.slice(0, n || 5);
  }
  function barajar(a) { a = a.slice(); for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)), t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
  function sinTildes(s) {
    var o = '';
    for (var i = 0; i < s.length; i++) { var c = s[i].toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, ''); o += c.length === 1 ? c : s[i]; }
    return o;
  }

  /* Elementos */
  function h(tag, a, hijos) {
    var e = document.createElement(tag);
    for (var k in a || {}) {
      var v = a[k];
      if (v == null || v === false) continue;
      if (k === 'class') e.className = v;
      else if (k === 'text') e.textContent = v;
      else if (k === 'html') e.innerHTML = v;
      else if (k.slice(0, 2) === 'on') e.addEventListener(k.slice(2), v);
      else e.setAttribute(k, v === true ? '' : v);
    }
    (hijos || []).forEach(function (c) { if (c != null) e.appendChild(typeof c === 'string' ? document.createTextNode(c) : c); });
    return e;
  }
  var SVG = {
    ok: '<path d="M5 12.5l4.5 4.5L19 7.5"/>',
    no: '<path d="M7 7l10 10M17 7L7 17"/>',
    flecha: '<path d="M5 12h13M13 6l6 6-6 6"/>',
    copiar: '<rect x="9" y="9" width="11" height="11" rx="2"/><path d="M15 9V5.5A1.5 1.5 0 0 0 13.5 4h-8A1.5 1.5 0 0 0 4 5.5v8A1.5 1.5 0 0 0 5.5 15H9"/>',
    otra: '<path d="M4.5 12a7.5 7.5 0 1 0 2.6-5.7M4 4.5V9h4.5"/>',
    rayo: '<path d="M13 3L5 14h6l-1 7 8-11h-6z"/>',
    mas: '<path d="M12 5v14M5 12h14"/>',
    abre: '<path d="M14 4h6v6M20 4l-9 9M18 14v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1h5"/>',
    lupa: '<circle cx="10.5" cy="10.5" r="6"/><path d="M15 15l5 5"/>',
    aviso: '<path d="M12 4l9 16H3z"/><path d="M12 10v4M12 17.5v.5"/>',
    estrella: '<path d="M12 3.5l2.6 5.6 6 .7-4.5 4.1 1.2 6-5.3-3-5.3 3 1.2-6L3.4 9.8l6-.7z"/>',
    rol: '<circle cx="12" cy="8" r="3.8"/><path d="M4.5 20.5c.6-4.2 3.6-6.5 7.5-6.5s6.9 2.3 7.5 6.5"/>',
    tarea: '<path d="M4 20l1-4.5L15.5 5a2.1 2.1 0 0 1 3 3L8 18.5z"/><path d="M13.5 7l3 3"/>',
    contexto: '<circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="4.5"/><circle cx="12" cy="12" r="1" fill="currentColor"/>',
    formato: '<path d="M9.5 6.5h10M9.5 12h10M9.5 17.5h10"/><path d="M4.5 6.5h.5M4.5 12h.5M4.5 17.5h.5" stroke-width="3"/>',
    tono: '<path d="M4 5.5h16v11H10l-5 4v-4H4z"/><path d="M9 10.5c1.6 1.8 4.4 1.8 6 0"/>',
    limites: '<circle cx="12" cy="12" r="8.5"/><path d="M6 6l12 12"/>',
    wa: '<path d="M4.5 19.5l1.2-3.7A8 8 0 1 1 8.6 18.6z"/><path d="M9.2 8.6c.2 2.9 3.3 6 6.2 6.2l.8-1.6-1.8-.9-.9.9c-1-.4-2.3-1.7-2.7-2.7l.9-.9-.9-1.8z"/>'
  };
  function ico(n, c) {
    var s = h('span', { class: 'lab-ico' + (c ? ' ' + c : ''), 'aria-hidden': 'true' });
    s.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">' + SVG[n] + '</svg>';
    return s;
  }
  function boton(txt, a, icono) {
    a = a || {}; a.type = 'button'; a.class = 'btn' + (a.class ? ' ' + a.class : '');
    var b = h('button', a, [icono ? ico(icono) : null, txt]);
    return b;
  }
  function viva(app) { var v = h('p', { class: 'sr', 'aria-live': 'polite' }); app.appendChild(v); return function (t) { v.textContent = ''; setTimeout(function () { v.textContent = t; }, 60); }; }
  function foco(el) { if (!el) return; if (!el.hasAttribute('tabindex') && !/^(BUTTON|INPUT|TEXTAREA|A|SELECT)$/.test(el.tagName)) el.setAttribute('tabindex', '-1'); el.focus({ preventScroll: false }); }

  /* Escuchar dentro de los laboratorios (el panel «A tu manera» lo muestra con is-oir) */
  function oirBtn(objetivo) {
    var b = h('button', { type: 'button', class: 'oir', 'aria-pressed': 'false', html: '<svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><path d="M4 10v4h4l5 4V6L8 10z"/><path d="M16 9a4 4 0 0 1 0 6M18.5 6.5a8 8 0 0 1 0 11"/></svg>Escuchar' });
    b.addEventListener('click', function () {
      if (!('speechSynthesis' in window)) return;
      var on = b.getAttribute('aria-pressed') === 'true';
      speechSynthesis.cancel();
      document.querySelectorAll('.oir').forEach(function (o) { o.setAttribute('aria-pressed', 'false'); });
      if (on) return;
      var c = (objetivo || b.parentNode).cloneNode(true);
      c.querySelectorAll('.oir, .sr, [hidden], button').forEach(function (n) { n.remove(); });
      var u = new SpeechSynthesisUtterance(c.textContent.replace(/\s+/g, ' ').trim());
      u.lang = 'es-ES'; u.rate = F() ? 0.9 : 1;
      u.onend = function () { b.setAttribute('aria-pressed', 'false'); };
      b.setAttribute('aria-pressed', 'true'); speechSynthesis.speak(u);
    });
    return b;
  }

  /* Guardar */
  function nota(id, v) { if (!id) return; v = Math.round(Math.max(0, Math.min(1, v)) * 100) / 100; P.labs[id] = Math.max(P.labs[id] || 0, v); AA.guardar(); }
  function meta(c, k, preg, ok, conf) {
    if (!c.lec || !conf) return;
    (P.meta[c.lec] = P.meta[c.lec] || {})[c.id + '-' + k] = { p: preg, ok: ok, c: conf }; AA.guardar();
  }
  function copiar(txt, aviso) {
    function hecho() { aviso('Copiado. Ya lo puedes pegar donde quieras.'); }
    if (navigator.clipboard && window.isSecureContext) navigator.clipboard.writeText(txt).then(hecho, otro); else otro();
    function otro() {
      var t = h('textarea', { class: 'sr', 'aria-hidden': 'true' }); t.value = txt; document.body.appendChild(t); t.select();
      try { document.execCommand('copy'); hecho(); } catch (e) { aviso('No se ha podido copiar. Selecciona el texto y cópialo a mano.'); }
      t.remove();
    }
  }

  /* Seguridad en la respuesta (metacognición) */
  var CONF = [['seguro', 'Lo sé'], ['creo', 'Creo que sí'], ['ni', 'Ni idea']];
  function confianza() {
    var n = 'conf' + (++uid);
    var fs = h('fieldset', { class: 'conf' }, [h('legend', { text: '¿Cómo de seguro estás? (si quieres)' })]);
    CONF.forEach(function (c) { fs.appendChild(h('label', { class: 'conf-op' }, [h('input', { type: 'radio', name: n, value: c[0] }), h('span', { text: c[1] })])); });
    fs.valor = function () { var i = fs.querySelector('input:checked'); return i ? i.value : null; };
    return fs;
  }
  function resumenConf(lista) {
    // lista de {ok, c}: devuelve el bloque «Acertaste y estabas seguro / dudando / Repasa esto»
    var g = { a: 0, b: 0, c: 0 };
    lista.forEach(function (r) { if (!r.c) return; if (r.ok && r.c === 'seguro') g.a++; else if (r.ok) g.b++; else g.c++; });
    if (!g.a && !g.b && !g.c) return null;
    return h('ul', { class: 'mc-mini' }, [
      h('li', { class: 'mc-a' }, [ico('ok'), h('b', { text: g.a }), ' acertaste y estabas seguro']),
      h('li', { class: 'mc-b' }, [ico('estrella'), h('b', { text: g.b }), ' acertaste dudando']),
      h('li', { class: 'mc-c' }, [ico('otra'), h('b', { text: g.c }), ' para repasar'])]);
  }

  /* Bloque de respuesta: siempre dice por qué, sin castigar */
  function veredicto(ok, titulo, expl, matiz) {
    var d = h('div', { class: 'fb ' + (ok === null ? 'fb-info' : ok ? 'fb-ok' : 'fb-no') }, [
      ico(ok === null ? 'lupa' : ok ? 'ok' : 'flecha', 'fb-ico'),
      h('div', { class: 'fb-txt' }, [h('p', { class: 'fb-t' }, [h('b', { text: titulo })]), expl ? h('p', { text: expl }) : null, matiz ? h('p', { class: 'fb-matiz', text: matiz }) : null])]);
    d.querySelector('.fb-txt').insertBefore(oirBtn(d.querySelector('.fb-txt')), d.querySelector('.fb-txt').firstChild);
    return d;
  }
  function frase(n, t) { var r = n / t; return r === 1 ? '¡Perfecto!' : r >= .75 ? '¡Muy bien!' : r >= .5 ? 'Vas por buen camino.' : 'Cada fallo te ha enseñado algo.'; }
  function final(app, c, bien, total, extra, reiniciar) {
    var caja = h('div', { class: 'lab-fin', tabindex: '-1' }, [
      h('p', { class: 'lab-fin-n' }, [h('b', { text: bien }), ' de ' + total]),
      h('p', { class: 'lab-fin-t', text: frase(bien, total) + ' ' + (bien === total ? 'Lo tienes dominado.' : 'Puedes volver a intentarlo cuando quieras: lo que falla hoy, mañana se recuerda mejor.') }),
      extra || null,
      boton('Vuelve a intentarlo', { class: 'lin peq', onclick: reiniciar }, 'otra')]);
    app.appendChild(caja); foco(caja);
    return caja;
  }

  var TIPOS = {};

  /* ---------- a) clasifica ---------- */
  TIPOS.clasifica = function (app, c) {
    var dec = viva(app);
    var items = enFacil(c.items, 6);
    var cats = c.categorias;
    function cat(id) { return cats.filter(function (x) { return x.id === id; })[0]; }
    var ej = c.ejemplo === false ? null : items[0];
    var resto = barajar(ej ? items.slice(1) : items);
    var sel = null, bien = 0, hechos = 0, trasArrastre = false;

    if (ej) {
      var okc = cat([].concat(ej.c)[0]);
      app.appendChild(h('div', { class: 'lab-ejemplo' }, [
        h('p', { class: 'lab-mini', text: 'Ejemplo resuelto' }),
        h('p', { class: 'ej-fila' }, [h('span', { class: 'ficha fija', text: tx(ej) }), ico('flecha', 'ej-flecha'), h('span', { class: 'ej-cat', text: tx(okc) })]),
        h('p', { class: 'ej-x', text: tx(ej, 'x') })]));
    }
    var bandeja = h('ul', { class: 'cl-bandeja', 'aria-label': 'Tarjetas por colocar' });
    var cuenta = h('p', { class: 'cl-cuenta' });
    app.appendChild(h('div', { class: 'cl-arriba' }, [
      h('p', { class: 'lab-paso' }, [h('b', { text: F() ? 'Ahora tú.' : 'Ahora tú.' }), ' ' + (F() ? 'Toca una tarjeta. Después toca su grupo.' : 'Toca una tarjeta y después el grupo donde va. Con ratón, también puedes arrastrarla.')]),
      cuenta, bandeja]));
    var zonas = h('div', { class: 'cl-zonas' });
    var listas = {};
    cats.forEach(function (k) {
      var b = h('button', { type: 'button', class: 'cl-zona', 'data-cat': k.id }, [
        h('span', { class: 'cl-zona-t', text: tx(k) }), k.d ? h('span', { class: 'cl-zona-d', text: tx(k, 'd') }) : null,
        h('span', { class: 'cl-poner', 'aria-hidden': 'true' }, [ico('mas'), 'Poner aquí'])]);
      b.addEventListener('click', function () {
        if (!sel) { dec('Primero toca una tarjeta de arriba.'); var p = bandeja.querySelector('button'); if (p) p.focus(); return; }
        colocar(sel, k);
      });
      listas[k.id] = h('ul', { class: 'cl-lista', 'aria-label': 'En ' + tx(k) });
      zonas.appendChild(h('div', { class: 'cl-cat', 'data-cat': k.id }, [b, listas[k.id]]));
    });
    app.appendChild(zonas);
    var fb = h('div', { class: 'lab-fb', 'aria-live': 'polite' });
    app.appendChild(fb);

    function pintarCuenta() { var q = resto.length - hechos; cuenta.textContent = q ? (q === 1 ? 'Te queda 1 tarjeta.' : 'Te quedan ' + q + ' tarjetas.') : ''; }
    function elegir(b, it) {
      bandeja.querySelectorAll('button').forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
      sel = { b: b, it: it };
      app.classList.add('cl-eligiendo');
      dec('Has elegido «' + tx(it) + '». Ahora elige su grupo.');
    }
    function colocar(s, k) {
      var it = s.it, oks = [].concat(it.c), ok = oks.indexOf(k.id) >= 0, ideal = cat(oks[0]);
      if (ok) bien++;
      hechos++;
      s.b.parentNode.remove(); sel = null; app.classList.remove('cl-eligiendo');
      var dest = ok ? k : ideal;
      listas[dest.id].appendChild(h('li', { class: 'ficha puesta ' + (ok ? 'bien' : 'corregida') }, [ico(ok ? 'ok' : 'flecha'), h('span', { text: tx(it) }),
        ok ? h('span', { class: 'sr', text: ' (acertada)' }) : h('span', { class: 'ficha-nota', text: 'Tú dijiste: ' + tx(k) })]));
      var titulo = ok ? (k.id !== ideal.id ? 'Vale, también encaja en «' + tx(k) + '»' : 'Bien visto: va en «' + tx(k) + '»') : 'Va mejor en «' + tx(ideal) + '»';
      fb.innerHTML = ''; fb.appendChild(veredicto(ok, titulo, tx(it, 'x')));
      pintarCuenta();
      var sig = bandeja.querySelector('button');
      if (sig) { sig.focus(); } else terminar();
    }
    function terminar() {
      nota(c.id, resto.length ? bien / resto.length : 1);
      var extra = null;
      if (c.reto) extra = reto();
      final(app, c, bien, resto.length, extra, function () { montarUno(app, c); });
    }
    function reto() {
      var n = 'reto' + (++uid), caja = h('div', { class: 'lab-reto' });
      var inp = h('input', { type: 'text', id: n, autocomplete: 'off', placeholder: tx(c.reto, 'ph') || '' });
      var g = h('fieldset', { class: 'chips' }, [h('legend', { text: '¿En qué grupo lo pondrías?' })]);
      cats.forEach(function (k) { g.appendChild(h('label', { class: 'chip' }, [h('input', { type: 'radio', name: n + 'c', value: k.id }), h('span', { text: tx(k) })])); });
      var r = h('div', { 'aria-live': 'polite' });
      caja.appendChild(h('p', { class: 'lab-mini', text: 'Reto libre' }));
      caja.appendChild(h('label', { for: n, class: 'lab-etq-campo', text: tx(c.reto) }));
      caja.append(inp, g, boton('Ver qué significa', { class: 'peq', onclick: function () {
        var v = g.querySelector('input:checked');
        r.innerHTML = '';
        if (!inp.value.trim() || !v) { r.appendChild(veredicto(null, 'Escribe tu caso y elige un grupo.', '')); return; }
        var k = cat(v.value);
        r.appendChild(veredicto(null, '«' + inp.value.trim() + '» en «' + tx(k) + '»', tx(k, 'p') || '', 'Aquí no hay nota: lo importante es que sepas explicar por qué.'));
      } }), r);
      return caja;
    }
    function arrastre(b, it) {
      var x0 = null, y0, fant = null, sobre = null;
      b.addEventListener('pointerdown', function (e) { if (e.pointerType === 'touch' || e.button) return; x0 = e.clientX; y0 = e.clientY; });
      b.addEventListener('pointermove', function (e) {
        if (x0 === null) return;
        if (!fant && Math.abs(e.clientX - x0) + Math.abs(e.clientY - y0) > 10) {
          fant = b.cloneNode(true); fant.className = 'ficha fantasma'; fant.setAttribute('aria-hidden', 'true'); document.body.appendChild(fant);
          try { b.setPointerCapture(e.pointerId); } catch (er) {}
          elegir(b, it);
        }
        if (!fant) return;
        fant.style.left = e.clientX + 'px'; fant.style.top = e.clientY + 'px';
        var z = document.elementFromPoint(e.clientX, e.clientY); z = z && z.closest('.cl-cat');
        if (z !== sobre) { if (sobre) sobre.classList.remove('sobre'); sobre = z; if (z) z.classList.add('sobre'); }
      });
      function fin() {
        if (fant) { fant.remove(); fant = null; trasArrastre = true; if (sobre) { sobre.classList.remove('sobre'); colocar({ b: b, it: it }, cat(sobre.dataset.cat)); } sobre = null; }
        x0 = null;
      }
      b.addEventListener('pointerup', fin); b.addEventListener('pointercancel', fin);
    }
    resto.forEach(function (it) {
      var b = h('button', { type: 'button', class: 'ficha', 'aria-pressed': 'false', text: tx(it) });
      b.addEventListener('click', function () { if (trasArrastre) { trasArrastre = false; return; } elegir(b, it); });
      arrastre(b, it);
      bandeja.appendChild(h('li', {}, [b]));
    });
    pintarCuenta();
  };

  /* ---------- b) verdad-o-mito ---------- */
  TIPOS['verdad-o-mito'] = function (app, c) {
    var dec = viva(app);
    var cartas = barajar(enFacil(c.cartas, 5)), i = 0, bien = 0, resp = [], confs = [];
    var et = c.etiquetas || { si: 'Verdad', no: 'Mito' };
    var cont = h('p', { class: 'vm-cont' });
    var puntos = h('ol', { class: 'vm-puntos', 'aria-hidden': 'true' });
    cartas.forEach(function () { puntos.appendChild(h('li')); });
    var carta = h('div', { class: 'vm-carta' });
    var zona = h('div', { class: 'vm-zona' }, [h('div', { class: 'vm-cab' }, [cont, puntos]), carta]);
    app.appendChild(zona);
    function marcarPuntos() { puntos.querySelectorAll('li').forEach(function (l, k) { l.className = resp[k] != null ? (resp[k] ? 'si' : 'no') : k === i ? 'ahora' : ''; }); }
    function girar(cambio) {
      if (RM) { cambio(); return; }
      carta.classList.add('gira');
      setTimeout(function () { cambio(); carta.classList.remove('gira'); }, 190);
    }
    function frente() {
      var k = cartas[i];
      cont.textContent = 'Carta ' + (i + 1) + ' de ' + cartas.length; marcarPuntos();
      carta.innerHTML = ''; carta.className = 'vm-carta';
      var cw = c.confianza === false ? null : confianza();
      var bs = h('div', { class: 'vm-botones' }, [
        boton(et.si, { class: 'vm-b vm-si', onclick: function () { responder(true, cw); } }, 'ok'),
        boton(et.no, { class: 'vm-b vm-no', onclick: function () { responder(false, cw); } }, 'no')]);
      var txt = h('p', { class: 'vm-frase', tabindex: '-1', text: tx(k) });
      carta.append(h('p', { class: 'lab-mini', text: c.pregunta ? tx(c, 'pregunta') : '¿Verdad o mito?' }), txt, cw, bs);
      return txt;
    }
    function responder(v, cw) {
      var k = cartas[i], ok = v === k.v, conf = cw && cw.valor();
      if (ok) bien++;
      resp[i] = ok; confs.push({ ok: ok, c: conf }); meta(c, i, (k.v ? et.si : et.no) + ': ' + tx(k), ok, conf);
      girar(function () {
        carta.innerHTML = ''; carta.className = 'vm-carta vuelta ' + (ok ? 'es-ok' : 'es-no');
        var titulo = (ok ? 'Bien visto: ' : 'Pues no: ') + (k.v ? et.fsi || 'es verdad' : et.fno || 'es un mito') + '.';
        carta.append(h('p', { class: 'vm-frase peq', text: tx(k) }), veredicto(ok, titulo, tx(k, 'x'),
          conf === 'seguro' && !ok ? 'Estabas seguro y no era así: estas son las que más enseñan.' : conf === 'ni' && ok ? 'Has acertado sin estar seguro: apúntatela para repasar.' : null));
        var sig = boton(i + 1 < cartas.length ? 'Siguiente carta' : 'Ver mi resultado', { class: 'peq', onclick: function () { i++; if (i < cartas.length) girar(function () { foco(frente()); }); else terminar(); } }, 'flecha');
        carta.appendChild(sig);
        dec(titulo + ' ' + tx(k, 'x'));
        marcarPuntos();
        sig.focus();
      });
    }
    function terminar() {
      zona.remove();
      nota(c.id, bien / cartas.length);
      final(app, c, bien, cartas.length, resumenConf(confs), function () { montarUno(app, c); });
    }
    frente();
  };

  /* ---------- c) siguiente-palabra ---------- */
  function trocear(s) { return sinTildes(s).split(/[^a-z0-9ñ]+/).filter(Boolean); }
  function modelo(frases) {
    var M = {}, D = {};
    function suma(k, w) { var m = M[k] = M[k] || {}; m[w] = (m[w] || 0) + 1; }
    frases.forEach(function (f) {
      f.toLowerCase().split(/[^a-záéíóúüñ0-9]+/).filter(Boolean).forEach(function (w) { D[sinTildes(w)] = D[sinTildes(w)] || w; });
      var w = trocear(f).concat(['$']), a = '^', b = '^';
      w.forEach(function (x) { suma(b, x); suma(a + ' ' + b, x); a = b; b = x; });
    });
    return { M: M, D: D };
  }
  TIPOS['siguiente-palabra'] = function (app, c) {
    var dec = viva(app), md = modelo(c.corpus), creativa = false, puestas = 0, felicitado = false;
    var n = 'sp' + (++uid);
    var inp = h('input', { type: 'text', id: n, class: 'sp-inp', autocomplete: 'off', autocapitalize: 'sentences', spellcheck: 'false', value: '' });
    var semillas = h('div', { class: 'sp-semillas' }, [h('span', { class: 'lab-mini', text: 'O empieza con:' })]);
    (F() ? c.semillas_f || c.semillas : c.semillas).forEach(function (s) {
      semillas.appendChild(h('button', { type: 'button', class: 'chip-b', text: s, onclick: function () { inp.value = s; pintar(); inp.focus(); } }));
    });
    var mirando = h('p', { class: 'sp-mirando' });
    var barras = h('ol', { class: 'sp-barras', 'aria-label': 'Palabras más probables' });
    var bMas = boton('Añadir la más probable', { onclick: function () { poner(elegir()); } }, 'mas');
    var bBorra = boton('Borrar la última', { class: 'lin peq', onclick: function () { inp.value = inp.value.replace(/\s*\S+\s*$/, ''); pintar(); inp.focus(); } });
    var sw = h('input', { type: 'checkbox', id: n + 'c', class: 'sw' });
    sw.addEventListener('change', function () { creativa = sw.checked; bMas.lastChild.textContent = creativa ? 'Añadir una palabra (creativa)' : 'Añadir la más probable'; pintar(); dec(creativa ? 'Modo creativo: a veces elige palabras menos probables.' : 'Modo normal: elige la palabra más probable.'); });
    var msg = h('div', { 'aria-live': 'polite', class: 'sp-msg' });
    app.append(
      h('label', { for: n, class: 'lab-etq-campo', text: F() ? 'Escribe el principio de una frase:' : 'Escribe el principio de una frase (o elige uno):' }), inp, semillas,
      h('div', { class: 'sp-panel' }, [mirando, barras]),
      h('div', { class: 'lab-acc' }, [bMas, bBorra, h('label', { class: 'sw-l', for: n + 'c' }, [sw, h('span', { text: 'Más creativa' })])]),
      msg,
      h('p', { class: 'lab-nota', text: F() ? 'Un chat de IA hace esto: elige la palabra que más veces vio detrás. Una y otra vez.' : 'Así escribe un chat de IA: mira tus últimas palabras y elige una de las que más veces vio detrás en los textos con los que aprendió. Una y otra vez. Este solo conoce ' + c.corpus.length + ' frases; uno de verdad, muchísimas más.' }));
    inp.addEventListener('input', pintar);
    function frase() { var t = inp.value, k = Math.max(t.lastIndexOf('.'), t.lastIndexOf('?'), t.lastIndexOf('!')); return trocear(t.slice(k + 1)); }
    function dist() {
      var w = frase(), b = w.length ? w[w.length - 1] : '^', a = w.length > 1 ? w[w.length - 2] : '^';
      var m = md.M[a + ' ' + b], ctx = a === '^' ? b : a + ' ' + b;
      if (!m) { m = md.M[b]; ctx = b; }
      if (!m) return null;
      var tot = 0, l = Object.keys(m).map(function (k) { tot += m[k]; return { w: k, n: m[k] }; });
      l.forEach(function (x) { x.p = x.n / tot; });
      if (creativa) { var s = 0; l.forEach(function (x) { x.p = Math.pow(x.p, 1 / 2.5); s += x.p; }); l.forEach(function (x) { x.p /= s; }); }
      l.sort(function (x, y) { return y.p - x.p; });
      return { l: l, ctx: ctx === '^' ? '' : ctx };
    }
    function bonita(w) { return w === '$' ? '(fin de la frase)' : md.D[w] || w; }
    var actual = null;
    function pintar() {
      actual = dist(); barras.innerHTML = '';
      if (!actual) {
        mirando.textContent = '';
        msg.innerHTML = ''; msg.appendChild(veredicto(null, 'Esto no lo he visto nunca.', F() ? 'Borra la última palabra o prueba otra.' : 'En mis frases no aparece «' + frase().slice(-1)[0] + '». Una IA de verdad ha leído muchísimo más. Borra la última palabra o prueba con otra.'));
        bMas.disabled = true; return;
      }
      bMas.disabled = false; msg.innerHTML = '';
      mirando.textContent = actual.ctx ? 'Mirando: «' + actual.ctx.split(' ').map(bonita).join(' ') + '»' : 'Mirando: el principio de la frase';
      actual.l.slice(0, F() ? 3 : 5).forEach(function (x, k) {
        var pc = Math.round(x.p * 100);
        var i = h('i'); var b = h('button', { type: 'button', class: 'sp-barra' + (k ? '' : ' top') }, [
          h('span', { class: 'sp-w' }, [h('span', { class: 'sr', text: 'Añadir ' }), bonita(x.w)]), h('span', { class: 'sp-pista' }, [i]), h('span', { class: 'sp-pc', text: (pc < 1 ? '<1' : pc) + ' %' })]);
        b.addEventListener('click', function () { poner(x.w); });
        barras.appendChild(h('li', {}, [b]));
        if (RM) i.style.width = pc + '%'; else requestAnimationFrame(function () { requestAnimationFrame(function () { i.style.width = Math.max(pc, 1) + '%'; }); });
      });
    }
    function elegir() {
      if (!actual) return null;
      if (!creativa) return actual.l[0].w;
      var r = Math.random(), s = 0;
      for (var k = 0; k < actual.l.length; k++) { s += actual.l[k].p; if (r <= s) return actual.l[k].w; }
      return actual.l[0].w;
    }
    function poner(w) {
      if (!w) return;
      var t = inp.value.replace(/\s+$/, '');
      if (w === '$') t += '.';
      else { var nueva = !t || /[.?!]$/.test(t); var p = bonita(w); t += (t ? ' ' : '') + (nueva ? p.charAt(0).toUpperCase() + p.slice(1) : p); }
      inp.value = t; puestas++; pintar();
      var top = actual ? actual.l.slice(0, 3).map(function (x) { return bonita(x.w) + ' ' + Math.round(x.p * 100) + ' por ciento'; }).join(', ') : '';
      dec('Añadida: ' + bonita(w) + '. ' + (top ? 'Ahora lo más probable: ' + top + '.' : ''));
      if (puestas >= 5 && !felicitado) {
        felicitado = true; nota(c.id, 1);
        msg.innerHTML = ''; msg.appendChild(veredicto(true, '¡Ya escribes como una IA!', F() ? 'Has elegido palabras una a una. Así escribe un chat de IA.' : 'Has escrito palabra a palabra, eligiendo lo más probable. Fíjate: suena bien, pero nadie ha comprobado si es verdad. Por eso una IA puede inventarse cosas con mucha seguridad.'));
      }
    }
    pintar();
  };

  /* ---------- d) ensena-a-la-maquina ---------- */
  var VACIAS = 'a al de del el la las los lo un una unos unas y o u en es por con para que se su sus te tu mi me le les ha he ya este esta esto ese eso muy mas soy 000'.split(' ');
  var BONITA = {};
  function palabras(t) {
    t.toLowerCase().split(/[^a-záéíóúüñ0-9]+/).forEach(function (w) { if (w) BONITA[sinTildes(w)] = w; });
    return trocear(t).filter(function (w) { return w.length > 1 && VACIAS.indexOf(w) < 0; });
  }
  function bon(w) { return BONITA[w] || w; }
  function entrenar(ej) {
    var m = { n: {}, w: {}, tot: {}, voc: {}, N: 0 };
    ej.forEach(function (e) {
      if (!e.l) return; m.n[e.l] = (m.n[e.l] || 0) + 1; m.N++;
      palabras(e.t).forEach(function (w) { var d = m.w[e.l] = m.w[e.l] || {}; d[w] = (d[w] || 0) + 1; m.tot[e.l] = (m.tot[e.l] || 0) + 1; m.voc[w] = 1; });
    });
    return m;
  }
  function predecir(m, t, clases) {
    var V = Object.keys(m.voc).length || 1, ws = palabras(t), lp = {};
    clases.forEach(function (k) {
      var s = Math.log(((m.n[k] || 0) + 1) / (m.N + clases.length));
      ws.forEach(function (w) { if (!m.voc[w]) return; s += Math.log((((m.w[k] || {})[w] || 0) + 1) / ((m.tot[k] || 0) + V)); });
      lp[k] = s;
    });
    var mx = Math.max.apply(null, clases.map(function (k) { return lp[k]; })), z = 0, pr = {};
    clases.forEach(function (k) { pr[k] = Math.exp(lp[k] - mx); z += pr[k]; });
    clases.forEach(function (k) { pr[k] /= z; });
    var gana = clases.slice().sort(function (a, b) { return pr[b] - pr[a]; })[0];
    var pistas = ws.filter(function (w, i) { return m.voc[w] && ws.indexOf(w) === i && ((m.w[gana] || {})[w] || 0) > 0; }).sort(function (a, b) { return (m.w[gana][b] || 0) - (m.w[gana][a] || 0); }).slice(0, 3);
    return { k: gana, p: pr[gana], pistas: pistas };
  }
  TIPOS['ensena-a-la-maquina'] = function (app, c) {
    var dec = viva(app), clases = c.clases.map(function (k) { return k.id; });
    function nom(id) { return tx(c.clases.filter(function (k) { return k.id === id; })[0]); }
    var ej = enFacil(c.ejemplos, 6).map(function (e, i) { return { t: tx(e), x: tx(e, 'x'), v: e.c, l: i === 0 ? e.c : null }; });
    var pruebas = enFacil(c.pruebas, 3);
    var alReves = false;
    var cerebro = h('div', { class: 'em-cerebro', 'aria-live': 'off' });
    var lista = h('ol', { class: 'em-lista' });
    app.append(h('div', { class: 'em-rej' }, [
      h('div', {}, [h('p', { class: 'lab-paso' }, [h('b', { text: '1. Enséñale.' }), ' ' + (F() ? 'Di qué es cada mensaje.' : 'Etiqueta cada mensaje. El primero ya está hecho, como ejemplo.')]), lista]),
      h('div', { class: 'em-lado' }, [h('p', { class: 'lab-mini', text: 'Lo que está aprendiendo' }), cerebro])]));
    var bProbar = boton('2. Ponla a prueba', { onclick: probar }, 'flecha');
    var res = h('div', { class: 'em-res', tabindex: '-1' });
    app.append(h('div', { class: 'lab-acc' }, [bProbar]), res);
    ej.forEach(function (e, i) {
      var li = h('li', { class: 'em-msg' + (i === 0 ? ' ejemplo' : '') });
      var nota0 = h('p', { class: 'em-nota', 'aria-live': 'polite' });
      var grupo = h('div', { class: 'em-bs', role: 'group', 'aria-label': 'Etiqueta del mensaje ' + (i + 1) });
      clases.forEach(function (k) {
        var b = h('button', { type: 'button', class: 'em-b em-' + k, 'aria-pressed': e.l === k ? 'true' : 'false', text: nom(k) });
        b.addEventListener('click', function () {
          e.l = k; grupo.querySelectorAll('button').forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
          nota0.textContent = k === e.v ? '' : (F() ? 'Ojo: ' + e.x : 'Ojo, una persona experta diría «' + nom(e.v) + '»: ' + e.x + ' Lo dejamos como tú digas, a ver qué aprende.');
          pintarCerebro(); dec('Etiquetado como ' + nom(k) + '.');
        });
        grupo.appendChild(b);
      });
      if (i === 0) nota0.textContent = 'Ejemplo resuelto: ' + e.x;
      li.append(h('p', { class: 'em-t', text: '«' + e.t + '»' }), grupo, nota0);
      lista.appendChild(li);
    });
    function datos() { return ej.map(function (e) { return { t: e.t, l: e.l && alReves ? clases[1 - clases.indexOf(e.l)] : e.l }; }); }
    function pintarCerebro() {
      var m = entrenar(datos()); cerebro.innerHTML = '';
      clases.forEach(function (k) {
        var d = m.w[k] || {}, top = Object.keys(d).sort(function (a, b) { return d[b] - d[a]; }).slice(0, F() ? 3 : 5);
        cerebro.appendChild(h('div', { class: 'em-col em-' + k }, [h('p', { class: 'em-col-t', text: nom(k) + ' (' + (m.n[k] || 0) + ')' }),
          top.length ? h('ul', {}, top.map(function (w) { return h('li', { text: bon(w) }); })) : h('p', { class: 'em-vacio', text: 'Aún nada' })]));
      });
    }
    function probar() {
      var falta = ej.filter(function (e) { return !e.l; }).length;
      if (falta) {
        dec(falta === 1 ? 'Te falta 1 mensaje por etiquetar.' : 'Te faltan ' + falta + ' mensajes por etiquetar.');
        var li = [].filter.call(lista.querySelectorAll('.em-msg'), function (x, i) { return !ej[i].l; })[0];
        if (li) li.querySelector('button').focus();
        return;
      }
      var m = entrenar(datos()), acierta = 0; res.innerHTML = '';
      if (alReves) res.appendChild(h('p', { class: 'em-aviso' }, [ico('aviso'), F() ? 'La has enseñado al revés.' : 'Le has enseñado al revés: lo que es estafa, como normal, y al contrario.']));
      res.appendChild(h('p', { class: 'lab-paso' }, [h('b', { text: '3. Mensajes nuevos que nunca ha visto' })]));
      var ul = h('ul', { class: 'em-preds' });
      pruebas.forEach(function (pq) {
        var r = predecir(m, tx(pq), clases), ok = r.k === pq.c; if (ok) acierta++;
        var pc = Math.round(r.p * 100), barra = h('i', { style: 'width:' + pc + '%' });
        ul.appendChild(h('li', { class: 'em-pred ' + (ok ? 'bien' : 'mal') }, [
          h('p', { class: 'em-t', text: '«' + tx(pq) + '»' }),
          h('p', { class: 'em-dice' }, ['La máquina dice: ', h('b', { class: 'em-etq em-' + r.k, text: nom(r.k) }), ' ', ico(ok ? 'ok' : 'no'), h('span', { text: ok ? ' Acierta' : ' Se equivoca' })]),
          h('div', { class: 'em-seg' }, [h('span', { text: 'Seguridad ' + pc + ' %' }), h('span', { class: 'barra peq', 'aria-hidden': 'true' }, [barra])]),
          r.pistas.length ? h('p', { class: 'em-pistas', text: 'Se ha fijado en: ' + r.pistas.map(bon).join(', ') }) : null]));
      });
      res.appendChild(ul);
      var bienEt = ej.filter(function (e) { return e.l === e.v; }).length;
      res.appendChild(veredicto(acierta >= pruebas.length - 1 && !alReves, 'Ha acertado ' + acierta + ' de ' + pruebas.length,
        alReves ? (F() ? 'Con ejemplos malos, la máquina aprende mal. Eso es el sesgo.' : 'Con ejemplos torcidos, aprende torcido. Y lo dice con la misma seguridad. Eso es el sesgo: la IA es tan buena como sus ejemplos.')
          : (F() ? 'La máquina aprende de lo que tú le enseñas.' : 'Solo con ' + ej.length + ' ejemplos ya se fija en palabras como las de los mensajes que le enseñaste. Con millones de ejemplos, así funciona el filtro de spam de tu correo.')));
      var bMal = boton(alReves ? 'Vuelve a enseñarle bien' : 'Enséñale mal a propósito', { class: 'lin', onclick: function () { alReves = !alReves; pintarCerebro(); probar(); } }, 'otra');
      res.appendChild(h('div', { class: 'lab-acc' }, [bMal]));
      if (!alReves) nota(c.id, bienEt / ej.length);
      foco(res);
    }
    pintarCerebro();
  };

  /* ---------- e) evaluador-prompts ---------- */
  /* Reglas: vienen de _src/contenido/reglas_prompts.py, en <script id="aa-reglas"> */
  var ING = [], DATOS = [], EJ = {}, ORDEN = [], ESC = {};
  (function () {
    var s = document.getElementById('aa-reglas'); if (!s) return;
    var R = JSON.parse(s.textContent);
    ING = R.ing.map(function (g) { g.re = g.re.map(function (x) { return new RegExp(x); }); return g; });
    DATOS = R.datos.map(function (x) { return new RegExp(x); });
    EJ = R.ej; ORDEN = R.orden;
    for (var k in R.esc) ESC[k] = new RegExp(R.esc[k]);
  })();
  function analizar(t) {
    var n = sinTildes(t), r = { ing: {}, score: 0, pal: (t.match(/\S+/g) || []).length, datos: false };
    ING.forEach(function (g) {
      for (var i = 0; i < g.re.length; i++) { var m = g.re[i].exec(n); if (m) { r.ing[g.k] = t.substr(m.index, m[0].length); r.score += g.w; break; } }
    });
    if (!r.ing.tarea) r.score = Math.min(r.score, 40);
    if (r.pal < 6) r.score = Math.min(r.score, 25);
    if (!t.trim()) r.score = 0;
    r.datos = DATOS.some(function (re) { return re.test(n); });
    r.esc = 'gen'; for (var e in ESC) if (ESC[e].test(n)) { r.esc = e; break; }
    r.falta = ORDEN.filter(function (k) { return !r.ing[k]; });
    return r;
  }
  function nivel(s) { return s >= 90 ? (F() ? '¡De diez!' : '¡Prompt de diez!') : s >= 70 ? (F() ? 'Muy bien' : 'Buen prompt') : s >= 40 ? (F() ? 'Va bien' : 'Va tomando forma') : (F() ? 'Le faltan cosas' : 'Le falta casi todo'); }
  window.AALab = { analizar: analizar };
  var EVALS = [];
  function anillo(clase) {
    var d = h('div', { class: 'ev-anillo ' + (clase || '') });
    d.innerHTML = '<svg viewBox="0 0 120 120" aria-hidden="true"><circle class="pista" cx="60" cy="60" r="52"/><circle class="valor" cx="60" cy="60" r="52" stroke-dasharray="326.7" stroke-dashoffset="326.7" transform="rotate(-90 60 60)"/></svg>';
    var num = h('p', { class: 'ev-num' }, [h('b', { text: '0' }), h('span', { text: 'de 100' })]);
    d.appendChild(num);
    d.poner = function (s) { d.querySelector('.valor').setAttribute('stroke-dashoffset', (326.7 * (1 - s / 100)).toFixed(1)); num.firstChild.textContent = s; d.classList.toggle('diez', s >= 90); };
    return d;
  }
  var GUARDA = {};
  TIPOS['evaluador-prompts'] = function (app, c) {
    var dec = viva(app), n = 'ev' + (++uid), corto = c.modo === 'corto';
    var ini = GUARDA[c.id] != null ? GUARDA[c.id] : (c.inicial || '');
    try { var lleva = localStorage.getItem('aa-prompt'); if (lleva && !corto) { ini = lleva; localStorage.removeItem('aa-prompt'); } } catch (e) {}
    var ta = h('textarea', { id: n, rows: F() ? 4 : 5, class: 'ev-ta', spellcheck: 'true', 'aria-describedby': n + 'a' });
    ta.value = ini;
    var an = anillo(), niv = h('p', { class: 'ev-nivel' }), estado = h('p', { class: 'sr', id: n + 'e', 'aria-live': 'polite' });
    var ings = h('ul', { class: 'ev-ings', 'aria-label': 'Ingredientes del prompt' });
    var chips = {};
    ING.forEach(function (g) {
      var est = h('span', { class: 'ev-est' });
      var li = h('li', { class: 'ev-ing', 'data-k': g.k }, [ico(g.k, 'ev-ing-ico'), h('span', { class: 'ev-ing-txt' }, [h('b', { text: F() ? g.nf : g.n }), est]), ico('ok', 'ev-check')]);
      chips[g.k] = { li: li, est: est }; ings.appendChild(li);
    });
    var sug = h('div', { class: 'ev-sug' }), aviso = h('p', { class: 'ev-datos', hidden: true }, [ico('aviso'), F() ? 'Quita tus datos personales. La IA no los necesita.' : 'Parece que hay datos personales (DNI, teléfono, cuenta o clave). Quítalos: la IA no los necesita para ayudarte.']);
    var msg = h('p', { class: 'lab-msg', 'aria-live': 'polite' });
    var avisar = function (t) { msg.textContent = t; };
    var links = h('p', { class: 'ev-ir' }, [h('span', { text: F() ? 'Pruébalo en:' : 'Cópialo y pruébalo en:' })]);
    [['ChatGPT', 'https://chatgpt.com/'], ['Gemini', 'https://gemini.google.com/'], ['Claude', 'https://claude.ai/']].forEach(function (x) {
      links.appendChild(h('a', { class: 'btn lin peq', href: x[1], target: '_blank', rel: 'noopener' }, [x[0], ico('abre'), h('span', { class: 'sr', text: ' (se abre en otra pestaña)' })]));
    });
    app.append(
      h('div', { class: 'ev-rej' }, [
        h('div', { class: 'ev-izq' }, [
          h('label', { for: n, class: 'lab-etq-campo', text: F() ? 'Escribe lo que le pedirías a la IA:' : 'Escribe tu prompt: lo que le pedirías a la IA.' }),
          h('p', { class: 'lab-ayuda', id: n + 'a', text: F() ? 'Mira las 6 piezas. Se encienden solas.' : 'Mientras escribes, se encienden los 6 ingredientes de un buen prompt. Nada sale de tu móvil.' }),
          ta, aviso,
          h('div', { class: 'lab-acc' }, [boton('Copiar prompt', { onclick: function () { copiar(ta.value, avisar); } }, 'copiar'), boton('Borrar', { class: 'lin peq', onclick: function () { ta.value = ''; actualizar(true); ta.focus(); } })]),
          msg, links]),
        h('div', { class: 'ev-der' }, [h('div', { class: 'ev-marcador' }, [an, niv]), ings])]),
      sug, estado);
    var tAnuncio = null, antes = {}, tocado = false;
    function actualizar(yaAnuncia) {
      GUARDA[c.id] = ta.value;
      var r = analizar(ta.value);
      an.poner(r.score); niv.textContent = nivel(r.score);
      ING.forEach(function (g) {
        var on = !!r.ing[g.k], ch = chips[g.k];
        ch.li.classList.toggle('on', on);
        if (on && !antes[g.k] && !RM) { ch.li.classList.remove('pop'); void ch.li.offsetWidth; ch.li.classList.add('pop'); }
        ch.est.textContent = on ? (F() ? 'Lo tienes' : 'Lo tienes: «' + recorta(r.ing[g.k]) + '»') : 'Falta';
        antes[g.k] = on;
      });
      aviso.hidden = !r.datos;
      pintarSug(r);
      if (tocado && ta.value.trim()) nota(c.id, r.score / 100);
      clearTimeout(tAnuncio);
      var t = 'Puntuación: ' + r.score + ' de 100. ' + nivel(r.score) + '.' + (r.falta.length ? ' Falta: ' + r.falta.map(nombre).join(', ') + '.' : ' Tiene los 6 ingredientes.');
      if (yaAnuncia === true) estado.textContent = t; else tAnuncio = setTimeout(function () { estado.textContent = t; }, 1400);
    }
    function recorta(s) { return s.length > 28 ? s.slice(0, 26) + '…' : s; }
    function nombre(k) { var g = ING.filter(function (x) { return x.k === k; })[0]; return F() ? g.nf : g.n; }
    var pistaN = 0;
    function pintarSug(r) {
      sug.innerHTML = '';
      if (!r.falta.length) { sug.appendChild(veredicto(true, F() ? '¡Tiene las 6 piezas!' : '¡Tiene los 6 ingredientes!', F() ? 'Cópialo y pruébalo en un chat de IA.' : 'Cópialo y pruébalo en un chat de IA. Si la respuesta no te convence, corrígela en el mismo chat.')); return; }
      var k = r.falta[pistaN % r.falta.length], g = ING.filter(function (x) { return x.k === k; })[0], fr = EJ[k][r.esc];
      var bA = boton('Añadir', { class: 'peq', onclick: function () { añadir(fr); } }, 'mas');
      bA.setAttribute('aria-label', 'Añadir: ' + fr);
      sug.append(h('div', { class: 'ev-sug-caja' }, [ico(k, 'ev-sug-ico'), h('div', {}, [
        h('p', { class: 'ev-sug-t' }, [h('b', { text: (F() ? 'Te falta: ' : 'Para mejorarlo, añade ') + (F() ? g.nf : g.n.toLowerCase()) + '.' }), ' ' + (F() ? g.df : g.d)]),
        h('p', { class: 'ev-sug-ej' }, ['Por ejemplo: ', h('q', { text: fr })]),
        h('div', { class: 'lab-acc' }, [bA, r.falta.length > 1 ? boton('Otra pista', { class: 'lin peq', onclick: function () { pistaN++; pintarSug(analizar(ta.value)); sug.querySelector('.btn').focus(); } }) : null])])]));
    }
    function añadir(fr) {
      var v = ta.value.replace(/\s+$/, '');
      if (v && !/[.!?:]$/.test(v)) v += '.';
      ta.value = (v ? v + ' ' : '') + fr; pistaN = 0; tocado = true;
      actualizar(true); ta.focus(); ta.setSelectionRange(ta.value.length, ta.value.length);
      dec('Añadido: ' + fr);
    }
    ta.addEventListener('input', function () { tocado = true; actualizar(); });
    if (!corto && c.galeria) {
      var gal = h('div', { class: 'ev-gal' }, [h('h' + (c.nivel ? c.nivel + 1 : 4), { class: 'ev-gal-h', text: F() ? 'Antes y después' : 'Antes y después: tres casos de pueblo' })]);
      var ul = h('ul', { class: 'ev-pares' });
      c.galeria.forEach(function (p) {
        var a = analizar(p.antes).score, d = analizar(p.despues).score;
        ul.appendChild(h('li', { class: 'ev-par' }, [h('p', { class: 'ev-par-t', text: tx(p) }),
          h('div', { class: 'ev-antes' }, [h('p', { class: 'lab-mini' }, ['Antes ', h('span', { class: 'ev-pill', text: a + ' de 100' })]), h('p', { class: 'ev-txt', text: p.antes })]),
          h('div', { class: 'ev-despues' }, [h('p', { class: 'lab-mini' }, ['Después ', h('span', { class: 'ev-pill alto', text: d + ' de 100' })]), h('p', { class: 'ev-txt', text: p.despues })]),
          boton('Probar este en el evaluador', { class: 'lin peq', onclick: function () { ta.value = p.despues; actualizar(true); ta.focus(); ta.scrollIntoView({ block: 'center', behavior: RM ? 'auto' : 'smooth' }); } })]));
      });
      gal.appendChild(ul); app.appendChild(gal);
    }
    EVALS.push({ poner: function (t) { ta.value = t; tocado = true; actualizar(true); ta.focus(); ta.scrollIntoView({ block: 'center', behavior: RM ? 'auto' : 'smooth' }); } });
    actualizar(true);
  };

  /* ---------- f) constructor-prompts ---------- */
  TIPOS['constructor-prompts'] = function (app, c) {
    var dec = viva(app), n = 'cp' + (++uid), val = {};
    var pasos = c.pasos;
    var vista = h('p', { class: 'cp-vista', id: n + 'v' }), mini = h('p', { class: 'cp-nota' });
    var form = h('div', { class: 'cp-pasos' });
    pasos.forEach(function (p, i) {
      var g = ING.filter(function (x) { return x.k === p.k; })[0];
      var fs = h('fieldset', { class: 'cp-paso' }, [h('legend', {}, [ico(p.k, 'cp-ico'), h('span', { text: (i + 1) + '. ' + tx(p) })])]);
      var chs = h('div', { class: 'chips' });
      var otro = h('input', { type: 'text', class: 'cp-otro', 'aria-label': 'Escribe tu ' + (g ? g.n.toLowerCase() : 'opción'), placeholder: 'Escríbelo con tus palabras', hidden: true });
      enFacil(p.chips, 2).forEach(function (o) {
        chs.appendChild(h('label', { class: 'chip' }, [h('input', { type: 'radio', name: n + i, value: tx(o) }), h('span', { text: tx(o) })]));
      });
      chs.appendChild(h('label', { class: 'chip' }, [h('input', { type: 'radio', name: n + i, value: '__otro' }), h('span', { text: 'Otro…' })]));
      chs.addEventListener('change', function (e) {
        var v = e.target.value; otro.hidden = v !== '__otro';
        val[p.k] = v === '__otro' ? otro.value : v;
        if (v === '__otro') otro.focus();
        montarTexto();
      });
      otro.addEventListener('input', function () { val[p.k] = otro.value; montarTexto(); });
      fs.append(chs, otro); form.appendChild(fs);
    });
    function limpio(s) { s = (s || '').trim().replace(/[.\s]+$/, ''); return s ? s.charAt(0).toUpperCase() + s.slice(1) : ''; }
    function texto() {
      var t = [], tarea = limpio(val.tarea), ctx = (val.contexto || '').trim().replace(/[.\s]+$/, '');
      if (val.rol) t.push(limpio(val.rol));
      if (tarea || ctx) t.push(tarea ? tarea + (ctx ? ' ' + ctx.charAt(0).toLowerCase() + ctx.slice(1) : '') : limpio(ctx));
      ['formato', 'tono', 'limites'].forEach(function (k) { if (val[k]) t.push(limpio(val[k])); });
      return t.length ? t.join('. ') + '.' : '';
    }
    function montarTexto() {
      var t = texto();
      vista.textContent = t || (F() ? 'Elige una opción en cada paso.' : 'Elige una opción en cada paso y aquí se irá montando tu prompt.');
      vista.classList.toggle('vacia', !t);
      var r = analizar(t); mini.textContent = t ? 'En el evaluador sacaría ' + r.score + ' de 100.' : '';
    }
    var msg = h('p', { class: 'lab-msg', 'aria-live': 'polite' });
    var avisar = function (t) { msg.textContent = t; };
    app.append(h('div', { class: 'cp-rej' }, [form, h('div', { class: 'cp-lado' }, [h('div', { class: 'cp-hoja' }, [h('p', { class: 'lab-mini', text: 'Tu prompt' }), vista, mini]),
      h('div', { class: 'lab-acc' }, [
        boton('Copiar prompt', { onclick: function () { var t = texto(); if (!t) { avisar('Elige al menos una opción.'); return; } copiar(t, avisar); nota(c.id, 1); } }, 'copiar'),
        boton('Llevar al evaluador', { class: 'lin', onclick: function () {
          var t = texto(); if (!t) { avisar('Elige al menos una opción.'); return; }
          nota(c.id, 1);
          if (EVALS.length) { EVALS[0].poner(t); dec('Prompt llevado al evaluador.'); }
          else { try { localStorage.setItem('aa-prompt', t); } catch (e) {} location.href = '/laboratorio/#evaluador'; }
        } }, 'flecha')]), msg])]));
    montarTexto();
  };

  /* ---------- g) elige-la-mejor ---------- */
  TIPOS['elige-la-mejor'] = function (app, c) {
    var rondas = enFacil(c.rondas, 1), r = 0, bien = 0, confs = [];
    var caja = h('div', { class: 'el-caja' });
    app.appendChild(caja);
    function ronda() {
      var R = rondas[r]; caja.innerHTML = '';
      if (rondas.length > 1) caja.appendChild(h('p', { class: 'vm-cont', text: 'Caso ' + (r + 1) + ' de ' + rondas.length }));
      var pet = h('p', { class: 'el-pet', tabindex: '-1' }, [h('span', { class: 'lab-mini', text: 'Lo que se le pidió' }), h('q', { text: tx(R, 'pide') })]);
      caja.appendChild(pet);
      var cw = confianza(), resps = h('div', { class: 'el-resps' }), fb = h('div', { 'aria-live': 'polite' });
      ['a', 'b'].forEach(function (k) {
        var d = h('div', { class: 'el-resp', 'data-k': k }, [h('p', { class: 'el-resp-t', text: 'Respuesta ' + k.toUpperCase() }), h('div', { class: 'el-txt', html: tx(R[k]) })]);
        d.appendChild(boton('Me quedo con la ' + k.toUpperCase(), { class: 'peq el-elige', onclick: function () { elegir(k); } }));
        resps.appendChild(d);
      });
      caja.append(resps, cw, fb);
      function elegir(k) {
        var ok = k === R.mejor, conf = cw.valor(); if (ok) bien++;
        confs.push({ ok: ok, c: conf }); meta(c, r, tx(R, 'pide'), ok, conf);
        resps.querySelectorAll('.el-elige').forEach(function (b) { b.remove(); }); cw.remove();
        resps.querySelector('[data-k="' + k + '"]').classList.add('elegida');
        resps.querySelector('[data-k="' + R.mejor + '"]').classList.add('mejor');
        resps.querySelector('[data-k="' + R.mejor + '"] .el-resp-t').appendChild(h('span', { class: 'el-sello' }, [ico('estrella'), ' La más útil']));
        fb.appendChild(veredicto(ok, ok ? 'Bien elegido: la ' + R.mejor.toUpperCase() + ' es la más útil.' : 'La más útil es la ' + R.mejor.toUpperCase() + '.', tx(R, 'x')));
        var crit = h('ul', { class: 'el-crit' });
        R.criterios.forEach(function (cr) {
          var b = h('button', { type: 'button', class: 'el-crit-b', 'aria-pressed': 'false' }, [ico('lupa'), h('span', { text: tx(cr) })]);
          b.addEventListener('click', function () {
            var on = b.getAttribute('aria-pressed') !== 'true';
            crit.querySelectorAll('button').forEach(function (x) { x.setAttribute('aria-pressed', 'false'); });
            resps.querySelectorAll('mark').forEach(function (m) { m.classList.remove('on'); });
            if (on) { b.setAttribute('aria-pressed', 'true'); resps.querySelectorAll('mark[data-c="' + cr.c + '"]').forEach(function (m) { m.classList.add('on'); }); }
          });
          crit.appendChild(h('li', {}, [b]));
        });
        fb.append(h('p', { class: 'lab-paso' }, [h('b', { text: F() ? 'Mira por qué:' : 'Los criterios. Toca uno y lo marcamos en las respuestas:' })]), crit);
        var sig = boton(r + 1 < rondas.length ? 'Siguiente caso' : 'Ver mi resultado', { class: 'peq', onclick: function () { r++; if (r < rondas.length) { ronda(); } else terminar(); } }, 'flecha');
        fb.appendChild(sig); crit.querySelector('button').focus();
      }
      return pet;
    }
    function terminar() { caja.remove(); nota(c.id, bien / rondas.length); final(app, c, bien, rondas.length, resumenConf(confs), function () { montarUno(app, c); }); }
    ronda();
  };

  /* ---------- h) detective ---------- */
  TIPOS.detective = function (app, c) {
    var dec = viva(app), hechos = P.estado[c.id] = P.estado[c.id] || [], meta5 = c.meta || 5;
    var sitios = enFacil(c.sitios, 6);
    var an = anillo('peq'), txt = h('p', { class: 'dt-txt', 'aria-live': 'polite' });
    an.querySelector('.ev-num span').textContent = 'de ' + meta5;
    app.appendChild(h('div', { class: 'dt-marcador' }, [an, txt]));
    var ul = h('ul', { class: 'dt-lista' });
    sitios.forEach(function (s) {
      var id = c.id + '-' + s.id;
      var cb = h('input', { type: 'checkbox', id: id });
      cb.checked = hechos.indexOf(s.id) >= 0;
      cb.addEventListener('change', function () {
        var i = hechos.indexOf(s.id);
        if (cb.checked && i < 0) hechos.push(s.id); if (!cb.checked && i >= 0) hechos.splice(i, 1);
        pintar(true);
      });
      var pasos = h('ol', {}, (tx(s, 'pasos') || s.pasos).map(function (p) { return h('li', { text: p }); }));
      ul.appendChild(h('li', { class: 'dt-sitio' }, [
        h('div', { class: 'dt-fila' }, [cb, h('label', { for: id }, [h('b', { text: tx(s) }), s.d ? h('span', { text: tx(s, 'd') }) : null])]),
        h('details', {}, [h('summary', { text: '¿Cómo comprobarlo?' }), pasos])]));
    });
    app.appendChild(ul);
    function pintar(cambio) {
      var k = sitios.filter(function (s) { return hechos.indexOf(s.id) >= 0; }).length;
      an.poner(Math.min(100, Math.round(100 * k / meta5))); an.querySelector('.ev-num b').textContent = k;
      ul.querySelectorAll('.dt-sitio').forEach(function (li, i) { li.classList.toggle('on', hechos.indexOf(sitios[i].id) >= 0); });
      txt.textContent = k >= meta5 ? (F() ? '¡Ya tienes ' + k + ' sitios! Tarea hecha.' : '¡' + k + ' sitios! Tarea del módulo 1 hecha: ya sabes dónde te acompaña la IA.') : (F() ? 'Llevas ' + k + '. Busca ' + meta5 + '.' : 'Llevas ' + k + ' de ' + meta5 + '. Marca los que encuentres en tu móvil.');
      if (cambio) { P.labs[c.id] = Math.min(1, k / meta5); AA.guardar(); }
    }
    pintar(false);
  };

  /* ---------- i) repaso (caja de Leitner) ---------- */
  var INTERVALO = { 1: 1, 2: 2, 3: 4 };
  TIPOS.repaso = function (app, c) {
    if (!c.pool || !c.pool.length) return calentar(app, c);
    var paso = app.closest('.paso'), seguir = function () { var t = paso && paso.querySelector('.lab ~ .b'); foco(t || app); };
    var L = P.leitner, ses = (P.leitnerSesion || 0) + 1;
    var elegidas = barajar(c.pool).map(function (q) {
      var e = L[q.id], pri;
      if (!e) pri = 2 + (q.lec === c.pool[c.pool.length - 1].lec ? 0.5 : 0);
      else pri = (ses - e.s >= INTERVALO[e.c] ? 4 - e.c : -e.c);
      return { q: q, pri: pri };
    }).sort(function (a, b) { return b.pri - a.pri; }).slice(0, 3).map(function (x) { return x.q; });
    var i = 0, bien = 0;
    var cab = h('div', { class: 'rp-cab' }, [h('ol', { class: 'rp-puntos', 'aria-hidden': 'true' }, elegidas.map(function () { return h('li'); })),
      boton('Ahora no', { class: 'lin peq rp-saltar', onclick: function () { caja.remove(); cab.remove(); app.appendChild(h('p', { class: 'rp-vacio', text: 'Vale. Lo tienes aquí cuando quieras.' })); seguir(); } })]);
    var caja = h('div', { class: 'rp-caja' });
    app.append(cab, caja);
    function puntos() { cab.querySelectorAll('li').forEach(function (l, k) { l.className = k < i ? 'hecho' : k === i ? 'ahora' : ''; }); }
    function pregunta() {
      var q = elegidas[i]; caja.innerHTML = ''; puntos();
      var ops = q.ops.map(function (o, k) { return { t: o[0], tf: o[1], ok: o[2], k: k }; });
      if (F()) ops = [ops.filter(function (o) { return o.ok; })[0], ops.filter(function (o) { return !o.ok; })[0]];
      ops = barajar(ops);
      var leg = h('p', { class: 'rp-p', tabindex: '-1', id: 'rp' + (++uid) }, [h('span', { class: 'lab-mini', text: 'Pregunta ' + (i + 1) + ' de ' + elegidas.length + (q.lect ? ', de «' + q.lect + '»' : '') }), h('b', { text: tx(q, 'p') })]);
      var g = h('div', { class: 'rp-ops', role: 'group', 'aria-labelledby': leg.id });
      var fb = h('div', { 'aria-live': 'polite' });
      ops.forEach(function (o) {
        var b = h('button', { type: 'button', class: 'rp-op', text: tx(o) });
        b.addEventListener('click', function () {
          g.querySelectorAll('button').forEach(function (x) { x.disabled = true; });
          b.classList.add(o.ok ? 'bien' : 'mal'); b.insertBefore(ico(o.ok ? 'ok' : 'no'), b.firstChild);
          if (!o.ok) { var buena = [].filter.call(g.children, function (x, k) { return ops[k].ok; })[0]; buena.classList.add('bien'); buena.insertBefore(ico('ok'), buena.firstChild); }
          if (o.ok) bien++;
          var e = L[q.id] || { c: 1, s: 0 }; e.c = o.ok ? Math.min(3, e.c + 1) : 1; e.s = ses; L[q.id] = e;
          AA.guardar();
          fb.appendChild(veredicto(o.ok, o.ok ? 'Lo recuerdas.' : 'Así es:', tx(q, 'x'), o.ok ? null : 'Esta volverá en el próximo repaso.'));
          var sig = boton(i + 1 < elegidas.length ? 'Siguiente pregunta' : 'Terminar el repaso', { class: 'peq', onclick: function () { i++; if (i < elegidas.length) foco(pregunta()); else fin(); } }, 'flecha');
          fb.appendChild(sig); sig.focus();
        });
        g.appendChild(b);
      });
      caja.append(leg, g, fb);
      return leg;
    }
    function fin() {
      P.leitnerSesion = ses; AA.guardar();
      caja.innerHTML = ''; i = elegidas.length; puntos(); cab.querySelector('.rp-saltar').remove();
      var f = h('div', { class: 'rp-fin', tabindex: '-1' }, [ico('rayo'), h('p', {}, [h('b', { text: 'Has recordado ' + bien + ' de ' + elegidas.length + '. ' }),
        bien === elegidas.length ? (F() ? 'Muy bien. Ahora, la lección.' : 'Lo tienes fresco. Vamos con la lección.') : (F() ? 'Las que fallaste volverán pronto.' : 'Las que se te resistieron volverán antes. Recordar cuesta un poco: por eso funciona.')]),
        boton('Seguir con la lección', { class: 'peq', onclick: seguir }, 'flecha')]);
      caja.appendChild(f); foco(f);
    }
    pregunta();
  };
  // Primera lección: nada que repasar. Calentamiento sin respuesta correcta (activa lo que ya piensas).
  function calentar(app, c) {
    app.appendChild(h('p', { class: 'rp-vacio' }, [ico('rayo'), h('span', { text: F() ? 'Aún no hay nada que repasar. ¡Empiezas hoy!' : 'Repaso relámpago: aún no hay nada que repasar, ¡empiezas hoy!' })]));
    var q = c.calentamiento; if (!q) return;
    var leg = h('p', { class: 'rp-p', id: 'rp' + (++uid) }, [h('b', { text: tx(q, 'p') })]);
    var g = h('div', { class: 'rp-ops', role: 'group', 'aria-labelledby': leg.id }), fb = h('div', { 'aria-live': 'polite' });
    q.ops.forEach(function (o) {
      var b = h('button', { type: 'button', class: 'rp-op', 'aria-pressed': 'false', text: o });
      b.addEventListener('click', function () {
        g.querySelectorAll('button').forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
        try { P.estado[c.id] = o; AA.guardar(); } catch (e) {}
        fb.innerHTML = ''; fb.appendChild(veredicto(null, 'Has dicho: «' + o + '».', tx(q, 'x')));
      });
      g.appendChild(b);
    });
    app.appendChild(h('div', { class: 'rp-caja' }, [leg, g, fb]));
  }

  /* ---------- Explícaselo a… (técnica Feynman) ---------- */
  var PLANT = {
    madre: { t: 'Tu madre', p: 'Mamá, hoy he aprendido {tema}. Te lo cuento fácil: {0}. Por ejemplo: {1}. Y un consejo: {2}.', pf: 'Mamá, hoy he aprendido {tema}. {0}. Por ejemplo: {1}.' },
    cliente: { t: 'Un cliente', p: 'Le cuento algo útil que he aprendido sobre {tema}: {0}. Un ejemplo: {1}. Eso sí, {2}.', pf: 'Le cuento algo sobre {tema}. {0}. Por ejemplo: {1}.' },
    nino: { t: 'Un niño de 10 años', p: '¿Sabes qué he aprendido hoy? {Tema}. Mira: {0}. Por ejemplo: {1}. Y recuerda: {2}.', pf: '¿Sabes qué? {Tema}. {0}. Por ejemplo: {1}.' }
  };
  TIPOS.explicaselo = function (app, c) {
    var n = 'ex' + (++uid), a = 'madre', huecos = F() ? c.huecos.slice(0, 2) : c.huecos, inps = [];
    var quien = h('fieldset', { class: 'chips ex-quien' }, [h('legend', { text: '1. ¿A quién se lo explicas?' })]);
    Object.keys(PLANT).forEach(function (k) {
      var i = h('input', { type: 'radio', name: n, value: k }); if (k === a) i.checked = true;
      quien.appendChild(h('label', { class: 'chip' }, [i, h('span', { text: PLANT[k].t })]));
    });
    quien.addEventListener('change', function (e) { a = e.target.value; pintar(); });
    var campos = h('div', { class: 'ex-campos' }, [h('p', { class: 'lab-paso' }, [h('b', { text: '2. Rellena los huecos con tus palabras.' })])]);
    huecos.forEach(function (hu, i) {
      var id = n + 'h' + i, inp = h('input', { type: 'text', id: id, autocomplete: 'off', placeholder: tx(hu, 'ph') });
      inp.addEventListener('input', pintar); inps.push(inp);
      campos.append(h('label', { for: id, class: 'lab-etq-campo', text: tx(hu, 'l') }), inp);
    });
    var vista = h('p', { class: 'ex-vista' }), msg = h('p', { class: 'lab-msg', 'aria-live': 'polite' });
    var wa = h('a', { class: 'btn am', target: '_blank', rel: 'noopener', href: '#' }, [ico('wa'), 'Enviar por WhatsApp', h('span', { class: 'sr', text: ' (se abre WhatsApp y eliges a quién)' })]);
    wa.addEventListener('click', function () { nota(c.id, 1); });
    app.append(quien, campos, h('div', { class: 'ex-hoja' }, [h('p', { class: 'lab-mini', text: '3. Tu mensaje' }), vista]),
      h('div', { class: 'lab-acc' }, [wa, boton('Copiar texto', { class: 'lin', onclick: function () { copiar(texto(), function (t) { msg.textContent = t; }); nota(c.id, 1); } }, 'copiar')]), msg,
      h('p', { class: 'lab-nota', text: F() ? 'Si sabes explicarlo, lo has aprendido.' : 'Explicarlo con tus palabras es la mejor prueba de que lo has entendido. Si te atascas en un hueco, ahí está lo que conviene repasar.' }));
    function texto() {
      var pl = F() ? PLANT[a].pf : PLANT[a].p, tema = tx(c, 'tema');
      return pl.replace('{tema}', tema).replace('{Tema}', tema.charAt(0).toUpperCase() + tema.slice(1)).replace(/\{(\d)\}/g, function (m, k) {
        var v = inps[k] ? inps[k].value.trim().replace(/[.\s]+$/, '') : '';
        return v || '…';
      }).replace(/([.?!]\s+)([a-záéíóúñ])/g, function (m, a, b) { return a + b.toUpperCase(); });
    }
    function pintar() { var t = texto(); vista.textContent = t; wa.href = 'https://wa.me/?text=' + encodeURIComponent(t); }
    pintar();
  };

  /* Montaje: cada .lab-app con su configuración. Si cambia «Lectura fácil», se vuelven a montar. */
  var LISTA = [];
  function montarUno(app, c) {
    app.innerHTML = ''; app.className = 'lab-app vivo lab-' + c.tipo;
    var f = TIPOS[c.tipo];
    if (f) f(app, c); else app.textContent = 'Este laboratorio todavía no está disponible.';
  }
  document.querySelectorAll('.lab-app').forEach(function (app) {
    var s = document.getElementById(app.id + '-cfg');
    if (!s) return;
    try { var c = JSON.parse(s.textContent); c.lec = app.dataset.lec || null; LISTA.push([app, c]); } catch (e) {}
    var sin = app.querySelector('.lab-sin'); if (sin) sin.textContent = 'Preparando el laboratorio…';
  });
  // Se monta cada laboratorio cuando se acerca a la pantalla: la página carga antes.
  function montar(x) { x.hecho = true; montarUno(x[0], x[1]); }
  var io = 'IntersectionObserver' in window ? new IntersectionObserver(function (es) {
    es.forEach(function (en) { if (!en.isIntersecting) return; io.unobserve(en.target); LISTA.forEach(function (x) { if (x[0] === en.target && !x.hecho) montar(x); }); });
  }, { rootMargin: '800px 0px' }) : null;
  LISTA.forEach(function (x) { if (io) io.observe(x[0]); else montar(x); });
  // Y el resto, uno a uno cuando el navegador está libre (así el teclado nunca se salta uno sin montar).
  var ocioso = window.requestIdleCallback || function (f) { return setTimeout(f, 200); };
  function siguiente() { var x = LISTA.filter(function (y) { return !y.hecho; })[0]; if (!x) return; if (io) io.unobserve(x[0]); montar(x); ocioso(siguiente); }
  window.addEventListener('load', function () { ocioso(siguiente); });
  var eraF = F();
  new MutationObserver(function () { if (F() !== eraF) { eraF = F(); LISTA.forEach(function (x) { if (x.hecho) montar(x); }); } }).observe(H, { attributes: true, attributeFilter: ['class'] });
})();
