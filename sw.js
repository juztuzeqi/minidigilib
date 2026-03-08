const CACHE_NAME = 'minidigilib-v1';
const urlsToCache = [
  '/minidigilib/',
  '/minidigilib/index.html',
  '/minidigilib/audio/index-ad.html',
  '/minidigilib/logo.png',
  '/minidigilib/favicon.png',
  '/minidigilib/icon-192.png',
  '/minidigilib/icon-512.png',
  '/minidigilib/manifest.json'
];

// Install service worker
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        console.log('Cache opened');
        return cache.addAll(urlsToCache);
      })
  );
});

// Fetch: ambil dari cache dulu, baru network
self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => {
        // Dapat dari cache
        if (response) {
          return response;
        }
        
        // Clone request karena sekali pakai
        const fetchRequest = event.request.clone();
        
        return fetch(fetchRequest)
          .then(response => {
            // Cek response valid
            if (!response || response.status !== 200 || response.type !== 'basic') {
              return response;
            }
            
            // Clone response untuk cache
            const responseToCache = response.clone();
            
            caches.open(CACHE_NAME)
              .then(cache => {
                cache.put(event.request, responseToCache);
              });
            
            return response;
          });
      })
  );
});

// Hapus cache lama saat aktivasi
self.addEventListener('activate', event => {
  const cacheWhitelist = [CACHE_NAME];
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.map(cacheName => {
          if (cacheWhitelist.indexOf(cacheName) === -1) {
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
});
