/* AcademiAmable · panel «A tu manera», escuchar, glosario, cuestionarios, paso a paso y progreso.
   Todo se guarda solo en este navegador (localStorage). Nada sale del dispositivo. */
(function () {
  var H = document.documentElement;
  var LS = {
    get: function (k, d) { try { var v = localStorage.getItem(k); return v ? JSON.parse(v) : d; } catch (e) { return d; } },
    set: function (k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) {} }
  };
  var OPC = { facil: 'is-facil', oir: 'is-oir', grande: 'is-grande', contraste: 'is-contraste', pasos: 'is-pasos', pictos: 'is-pictos' };
  var prefs = LS.get('aa-prefs', {});

  function aplicar() {
    Object.keys(OPC).forEach(function (k) { H.classList.toggle(OPC[k], !!prefs[k]); });
    document.querySelectorAll('[data-opc]').forEach(function (i) { i.checked = !!prefs[i.dataset.opc]; });
    if (prefs.pasos) irPaso(pasoActual);
  }

  /* Panel */
  var panel = document.getElementById('panel');
  var abridor = null;
  function abrir(e) {
    abridor = e && e.currentTarget;
    panel.classList.add('abierto');
    panel.querySelector('.cerrar').focus();
  }
  function cerrar() {
    panel.classList.remove('abierto');
    if (abridor) abridor.focus();
  }
  document.querySelectorAll('[data-abre-panel]').forEach(function (b) { b.addEventListener('click', abrir); });
  if (panel) {
    panel.querySelector('.cerrar').addEventListener('click', cerrar);
    panel.addEventListener('click', function (e) { if (e.target === panel) cerrar(); });
    panel.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') cerrar();
      if (e.key === 'Tab') {
        var f = panel.querySelectorAll('button, input');
        var a = f[0], z = f[f.length - 1];
        if (e.shiftKey && document.activeElement === a) { e.preventDefault(); z.focus(); }
        else if (!e.shiftKey && document.activeElement === z) { e.preventDefault(); a.focus(); }
      }
    });
    panel.querySelectorAll('[data-opc]').forEach(function (i) {
      i.addEventListener('change', function () { prefs[i.dataset.opc] = i.checked; LS.set('aa-prefs', prefs); aplicar(); });
    });
  }

  /* Escuchar: lee en voz alta el texto visible del bloque */
  var hablando = null;
  function textoVisible(el) {
    var c = el.cloneNode(true);
    c.querySelectorAll('.oir, .sr, [hidden]').forEach(function (n) { n.remove(); });
    if (H.classList.contains('is-facil')) c.querySelectorAll('.n').forEach(function (n) { n.remove(); });
    else c.querySelectorAll('.f').forEach(function (n) { n.remove(); });
    return c.textContent.replace(/\s+/g, ' ').trim();
  }
  document.querySelectorAll('.oir').forEach(function (b) {
    b.addEventListener('click', function () {
      if (!('speechSynthesis' in window)) { alertaSuave(b, 'Tu navegador no puede leer en voz alta.'); return; }
      var on = b.getAttribute('aria-pressed') === 'true';
      speechSynthesis.cancel();
      document.querySelectorAll('.oir').forEach(function (o) { o.setAttribute('aria-pressed', 'false'); });
      if (on) return;
      var u = new SpeechSynthesisUtterance(textoVisible(b.closest('[data-leer]')));
      u.lang = 'es-ES'; u.rate = H.classList.contains('is-facil') ? 0.9 : 1;
      var v = speechSynthesis.getVoices().filter(function (x) { return x.lang && x.lang.indexOf('es') === 0; });
      if (v.length) u.voice = v.filter(function (x) { return x.lang === 'es-ES'; })[0] || v[0];
      u.onend = function () { b.setAttribute('aria-pressed', 'false'); };
      b.setAttribute('aria-pressed', 'true');
      hablando = u; speechSynthesis.speak(u);
    });
  });
  function alertaSuave(cerca, txt) {
    var p = document.createElement('p'); p.setAttribute('role', 'status'); p.textContent = txt;
    cerca.after(p); setTimeout(function () { p.remove(); }, 4000);
  }

  /* Glosario al tocar */
  var defAbierta = null;
  function cerrarDef() { if (defAbierta) { defAbierta.btn.setAttribute('aria-expanded', 'false'); defAbierta.el.remove(); defAbierta = null; } }
  document.querySelectorAll('button.g').forEach(function (b) {
    b.setAttribute('aria-expanded', 'false');
    b.addEventListener('click', function (e) {
      e.stopPropagation();
      var misma = defAbierta && defAbierta.btn === b;
      cerrarDef();
      if (misma) return;
      var d = document.createElement('span');
      d.className = 'def'; d.setAttribute('role', 'note'); d.textContent = b.dataset.def;
      var r = b.getBoundingClientRect();
      d.style.left = Math.max(8, Math.min(window.scrollX + r.left, window.scrollX + innerWidth - 316)) + 'px';
      d.style.top = (window.scrollY + r.bottom + 8) + 'px';
      document.body.appendChild(d);
      b.setAttribute('aria-expanded', 'true');
      defAbierta = { btn: b, el: d };
    });
  });
  document.addEventListener('click', cerrarDef);
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') cerrarDef(); });

  /* Progreso */
  var prog = LS.get('aa-progreso', { lecciones: {}, cuestionarios: {} });
  ['lecciones', 'cuestionarios', 'labs', 'meta', 'leitner', 'estado'].forEach(function (k) { prog[k] = prog[k] || {}; });
  function guardarProg() { LS.set('aa-progreso', prog); pintarProgreso(); }
  /* labs.js usa este mismo objeto para guardar sus resultados */
  window.AA = { prog: prog, guardar: guardarProg };

  /* Cuestionarios corregidos al momento */
  document.querySelectorAll('form.quiz').forEach(function (f) {
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      var total = 0, bien = 0, lec = f.dataset.id, m = prog.meta[lec] = prog.meta[lec] || {};
      f.querySelectorAll('fieldset.q').forEach(function (fs) {
        total++;
        var q = fs.dataset.q, marcada = fs.querySelector('input[name="q' + q + '"]:checked'), conf = fs.querySelector('input[name="q' + q + 'c"]:checked');
        fs.querySelectorAll('label').forEach(function (l) { l.classList.remove('bien', 'mal'); var s = l.querySelector('.marca'); if (s) s.remove(); });
        var ok = fs.querySelector('input[data-ok]');
        if (marcada) {
          if (marcada === ok) { bien++; marca(marcada.parentNode, 'bien', 'Correcta'); }
          else { marca(marcada.parentNode, 'mal', 'Tu respuesta, no es la correcta'); marca(ok.parentNode, 'bien', 'La correcta'); }
          m['quiz-' + q] = { p: fs.querySelector('legend').textContent.replace(/^\d+\.\s*/, ''), ok: marcada === ok, c: conf ? conf.value : null };
        }
        var ex = fs.querySelector('.expl');
        if (ex) ex.hidden = !marcada;
      });
      var res = f.querySelector('.res');
      res.textContent = bien === total ? '¡Todo bien! ' + bien + ' de ' + total + '.' :
        'Tienes ' + bien + ' de ' + total + '. Mira la explicación de cada pregunta y vuelve a probar si quieres.';
      prog.cuestionarios[f.dataset.id] = Math.max(prog.cuestionarios[f.dataset.id] || 0, bien / total);
      guardarProg();
    });
  });

  function marca(label, clase, txt) {
    label.classList.add(clase);
    var s = document.createElement('span'); s.className = 'marca'; s.textContent = txt; label.appendChild(s);
  }

  /* Dominio de una lección (0-100): media de las preguntas de «Piensa» y de sus laboratorios */
  function dominio(lec, labs) {
    var v = [prog.cuestionarios[lec] || 0].concat(labs.map(function (l) { return prog.labs[l] || 0; }));
    return Math.round(100 * v.reduce(function (a, b) { return a + b; }, 0) / v.length);
  }
  function lista(el) { return (el.dataset.labs || '').split(',').filter(Boolean); }
  function pintarDominio() {
    document.querySelectorAll('[data-resumen]').forEach(function (r) {
      var lec = r.dataset.resumen, labs = lista(r), p = dominio(lec, labs);
      r.querySelector('[data-dom-pc]').textContent = p + ' %';
      r.querySelector('.barra i').style.width = p + '%';
      r.querySelectorAll('[data-res-lab]').forEach(function (li) {
        var id = li.dataset.resLab, v = id === 'quiz' ? prog.cuestionarios[lec] : prog.labs[id], hecho = v != null;
        li.querySelector('.est').classList.toggle('hecha', hecho);
        li.querySelector('.est').setAttribute('aria-label', hecho ? 'Hecho' : 'Sin hacer');
        li.querySelector('.res-nota').textContent = hecho ? Math.round(v * 100) + ' %' : '';
      });
      var mc = r.querySelector('[data-metacog]'), m = prog.meta[lec] || {}, hay = false;
      mc.querySelectorAll('ul').forEach(function (u) { u.innerHTML = ''; });
      Object.keys(m).forEach(function (k) {
        var x = m[k]; if (!x.c) return; hay = true;
        var g = x.ok && x.c === 'seguro' ? 'a' : x.ok ? 'b' : 'c';
        var li = document.createElement('li'); li.textContent = x.p + (!x.ok && x.c === 'seguro' ? ' (estabas seguro)' : '');
        mc.querySelector('.mc-' + g + ' ul').appendChild(li);
      });
      mc.querySelectorAll('.mc').forEach(function (d) { d.hidden = !d.querySelector('li'); });
      mc.hidden = !hay; r.querySelector('[data-mc-vacio]').hidden = hay;
    });
    document.querySelectorAll('[data-dominio]').forEach(function (li) {
      var lec = li.dataset.dominio, labs = lista(li), p = dominio(lec, labs);
      var hechos = labs.filter(function (l) { return prog.labs[l] != null; }).length;
      li.querySelector('.barra i').style.width = p + '%';
      li.querySelector('.dom-txt').textContent = 'Dominio ' + p + ' %. Laboratorios hechos: ' + hechos + ' de ' + labs.length + (prog.cuestionarios[lec] != null ? '. Preguntas: ' + Math.round(prog.cuestionarios[lec] * 100) + ' %.' : '.');
    });
    document.querySelectorAll('[data-insignia]').forEach(function (el) {
      var ids = el.dataset.insignia.split(','), labs = lista(el);
      var v = ids.map(function (i) { return prog.cuestionarios[i] || 0; }).concat(labs.map(function (l) { return prog.labs[l] || 0; }));
      var p = Math.round(100 * v.reduce(function (a, b) { return a + b; }, 0) / (v.length || 1));
      var t = el.querySelector('[data-ins-dom]'); if (t) t.textContent = 'Dominio del módulo: ' + p + ' %.';
      var mz = el.querySelector('[data-maestria]'); if (mz) mz.hidden = p < 80;
    });
    var mp = document.getElementById('mejor-prompt');
    if (mp && prog.labs['laboratorio-evaluador'] != null) { mp.hidden = false; mp.textContent = 'Tu mejor prompt en el Laboratorio de prompts: ' + Math.round(prog.labs['laboratorio-evaluador'] * 100) + ' de 100.'; }
  }

  /* Marcar lección terminada */
  document.querySelectorAll('[data-terminar]').forEach(function (b) {
    b.addEventListener('click', function () {
      prog.lecciones[b.dataset.terminar] = new Date().toISOString().slice(0, 10);
      guardarProg();
      var m = document.getElementById('msg-fin');
      if (m) m.textContent = '¡Lección terminada! La tienes guardada en «Mi aprendizaje».';
    });
  });

  function pintarProgreso() {
    document.querySelectorAll('[data-lec]').forEach(function (el) {
      var h = !!prog.lecciones[el.dataset.lec];
      el.classList.toggle('hecha', h);
      el.setAttribute('aria-label', h ? 'Terminada' : 'Sin terminar');
    });
    document.querySelectorAll('[data-barra]').forEach(function (b) {
      var ids = b.dataset.barra.split(','), n = ids.filter(function (i) { return prog.lecciones[i]; }).length;
      var p = ids.length ? Math.round(100 * n / ids.length) : 0;
      b.querySelector('i').style.width = p + '%';
      var t = document.getElementById(b.dataset.txt);
      if (t) t.textContent = n + ' de ' + ids.length + ' lecciones (' + p + ' %)';
    });
    document.querySelectorAll('[data-insignia]').forEach(function (el) {
      var ids = el.dataset.insignia.split(',');
      var ok = ids.every(function (i) { return prog.lecciones[i]; });
      el.hidden = !ok;
    });
    var vacio = document.getElementById('sin-progreso');
    if (vacio) vacio.hidden = Object.keys(prog.lecciones).length > 0;
    pintarDominio();
  }

  /* Código para seguir en otro dispositivo */
  var exp = document.getElementById('exportar');
  if (exp) exp.addEventListener('click', function () {
    var cod = btoa(unescape(encodeURIComponent(JSON.stringify(prog))));
    var t = document.getElementById('codigo'); t.value = cod; t.select();
    if (navigator.clipboard) navigator.clipboard.writeText(cod).then(function () {
      document.getElementById('msg-cod').textContent = 'Código copiado. Pégalo en el otro móvil u ordenador.';
    });
  });
  var imp = document.getElementById('importar');
  if (imp) imp.addEventListener('click', function () {
    var msg = document.getElementById('msg-cod');
    try {
      var d = JSON.parse(decodeURIComponent(escape(atob(document.getElementById('codigo').value.trim()))));
      if (!d.lecciones) throw 0;
      Object.keys(d.lecciones).forEach(function (k) { prog.lecciones[k] = d.lecciones[k]; });
      Object.keys(d.cuestionarios || {}).forEach(function (k) { prog.cuestionarios[k] = Math.max(prog.cuestionarios[k] || 0, d.cuestionarios[k]); });
      Object.keys(d.labs || {}).forEach(function (k) { prog.labs[k] = Math.max(prog.labs[k] || 0, d.labs[k]); });
      ['meta', 'leitner', 'estado'].forEach(function (g) { Object.keys(d[g] || {}).forEach(function (k) { prog[g][k] = d[g][k]; }); });
      if (d.leitnerSesion > (prog.leitnerSesion || 0)) prog.leitnerSesion = d.leitnerSesion;
      guardarProg(); msg.textContent = 'Listo: tu progreso se ha cargado.';
    } catch (e) { msg.textContent = 'Ese código no es válido. Cópialo entero y vuelve a probar.'; }
  });

  /* Paso a paso */
  var pasos = Array.prototype.slice.call(document.querySelectorAll('.paso'));
  var pasoActual = 0;
  function irPaso(n) {
    if (!pasos.length) return;
    pasoActual = Math.max(0, Math.min(pasos.length - 1, n));
    pasos.forEach(function (p, i) { p.classList.toggle('actual', i === pasoActual); });
    H.classList.toggle('pasos-fin', pasoActual === pasos.length - 1);
    document.querySelectorAll('[data-paso-txt]').forEach(function (t) { t.textContent = 'Paso ' + (pasoActual + 1) + ' de ' + pasos.length; });
    document.querySelectorAll('[data-paso="-1"]').forEach(function (b) { b.disabled = pasoActual === 0; });
    document.querySelectorAll('[data-paso="1"]').forEach(function (b) { b.disabled = pasoActual === pasos.length - 1; });
  }
  document.querySelectorAll('[data-paso]').forEach(function (b) {
    b.addEventListener('click', function () {
      irPaso(pasoActual + Number(b.dataset.paso));
      var h = pasos[pasoActual].querySelector('h2'); h.setAttribute('tabindex', '-1'); h.focus();
    });
  });

  aplicar();
  pintarProgreso();

  if ('serviceWorker' in navigator && location.protocol === 'https:') {
    window.addEventListener('load', function () { navigator.serviceWorker.register('/sw.js').catch(function () {}); });
  }
})();
