/* Service Worker - 青梧笑 离线缓存 v33 */
const CACHE_NAME = "qingwuxiao-v33";
const ASSETS = [
  "./",
  "./index.html",
  "./manifest.json",
  "./icon-192.png",
  "./icon-512.png",
  "./words.json"
];

/* 安装：预缓存核心资源（容错，单个失败不影响整体） */
self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) =>
      Promise.allSettled(ASSETS.map((url) => cache.add(url)))
    ).then(() => self.skipWaiting())
  );
});

/* 激活：清理旧缓存，立即接管 */
self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(keys.filter((k) => k !== CACHE_NAME).map((k) => caches.delete(k)))
    ).then(() => self.clients.claim())
  );
});

/* 拦截请求：主页面网络优先，静态资源缓存优先 */
self.addEventListener("fetch", (event) => {
  if (event.request.method !== "GET") return;
  const url = new URL(event.request.url);
  if (url.origin !== self.location.origin) return;

  const isRoot = url.pathname === "/" ||
    url.pathname.endsWith("/index.html") ||
    url.pathname.endsWith("/青梧笑.html");

  /* words.json: 缓存优先，失败回退网络 */
  const isWordBank = url.pathname.endsWith("/words.json");

  if (isWordBank) {
    event.respondWith(
      caches.match(event.request).then((cached) => {
        if (cached) return cached;
        return fetch(event.request).then((response) => {
          if (response.ok) {
            const clone = response.clone();
            caches.open(CACHE_NAME).then((cache) => cache.put(event.request, clone));
          }
          return response;
        });
      })
    );
    return;
  }

  event.respondWith(
    isRoot
      ? fetch(event.request).then((response) => {
          if (response.ok) {
            const clone = response.clone();
            caches.open(CACHE_NAME).then((cache) => cache.put(event.request, clone));
          }
          return response;
        }).catch(() =>
          caches.match(event.request).then((c) =>
            c || caches.match("./index.html").then((c2) =>
              c2 || caches.match("./")
            )
          )
        )
      : caches.match(event.request).then((cached) => {
          if (cached) return cached;
          return fetch(event.request).then((response) => {
            if (response.ok) {
              const clone = response.clone();
              caches.open(CACHE_NAME).then((cache) => cache.put(event.request, clone));
            }
            return response;
          }).catch(() => caches.match("./index.html"));
        })
  );
});
