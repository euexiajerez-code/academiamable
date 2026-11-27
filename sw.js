// AcademiAmable · funciona sin conexión con las páginas ya abiertas.
const V = 'aa-0bfc3214';
const BASE = ['/', '/estilos.css?v=4de048e1', '/app.js?v=7304d8be', '/labs.js?v=fea4825c', '/img/logo.svg', '/fonts/montserrat-latin.woff2', '/fonts/nunito-latin.woff2', '/mi-aprendizaje/'];
self.addEventListener('install', e => { e.waitUntil(caches.open(V).then(c => c.addAll(BASE)).then(() => self.skipWaiting())); });
self.addEventListener('activate', e => { e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== V).map(k => caches.delete(k)))).then(() => self.clients.claim())); });
self.addEventListener('fetch', e => {
  const r = e.request;
  if (r.method !== 'GET' || new URL(r.url).origin !== location.origin) return;
  if (r.mode === 'navigate') {
    e.respondWith(fetch(r).then(res => { const c = res.clone(); caches.open(V).then(k => k.put(r, c)); return res; })
      .catch(() => caches.match(r).then(m => m || caches.match('/'))));
  } else {
    e.respondWith(caches.match(r).then(m => m || fetch(r).then(res => { const c = res.clone(); caches.open(V).then(k => k.put(r, c)); return res; })));
  }
});
