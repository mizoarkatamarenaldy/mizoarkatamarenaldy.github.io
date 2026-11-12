# Plan Saat Ini

## Mapping web (target akhir)
Isi semua bahasa SAMA. Pilihan bahasa cuma mengganti bahasa tampilan.
Ini target akhir, tidak semua halaman sudah ada (lihat "Status fitur").

```
mizoarkatamarenaldy.github.io/
│
├── (root) Halaman pilih bahasa
│     3 kartu: bendera + nama bahasa
│     judul "choose your language" dalam 3 bahasa
│
└── /id/  /en/  /ja/   (isi sama, cuma beda bahasa)
      │
      ├── HOME (/main/)
      │     ├── Nama lengkap + ringkasan tentang diri
      │     ├── Motto 3E (Equilibrium Equivalence Equity)
      │     │     teksnya sendiri jadi link ke halaman 3E,
      │     │     ada tanda saat kursor diarahkan (hover)
      │     ├── [buka-tutup] Main Portfolio
      │     │     ├── Psikologi
      │     │     ├── HR
      │     │     └── Linguistik
      │     └── [buka-tutup] Additional Portfolio
      │           ├── Developer
      │           ├── Data
      │           ├── Desain
      │           ├── Ilustrasi
      │           ├── Menulis
      │           ├── Musik
      │           ├── Kuliner
      │           └── Wirausaha
      │
      ├── 3E (detail framework, halaman terpisah)
      │
      ├── About
      │     ├── Latar belakang dan pengalaman hidup
      │     └── CV
      │
      ├── Contact
      │     └── Semua sosmed (termasuk LinkedIn) + beberapa channel YouTube
      │
      └── Easter egg Kanade (tersembunyi)
            ├── URL berisi kanji 奏, kanji di-blend ke background
            ├── Penjelasan kenapa Kanade penting buat pemilik
            ├── Link keluar ke Fandom wiki (tanpa gambar/chibi)
            ├── Ada di tiga bahasa, isi sama
            └── (opsional, belum pasti) fanfic
```

## Status fitur
- [/] Halaman 3E — kerangka selesai, isi menunggu Mizo
- [/] Halaman About (latar belakang, pengalaman hidup, CV) — kerangka selesai, isi menunggu Mizo
- [/] Halaman Main Portfolio (Psikologi, HR, Linguistik) — kerangka selesai, isi menunggu Mizo
- [/] Halaman Additional Portfolio (8 halaman) — kerangka selesai, isi menunggu Mizo
- [/] Easter egg Kanade (3 bahasa) — kerangka selesai, teks masih [TEKS DARI MIZO]
- [x] Samakan nama portofolio dengan Big Eleventh Skills
- [x] Perpendek nama portofolio jadi 1 kata
- [x] Token dan font Sumi & Washi
- [x] Layout HOME Sumi & Washi
- [x] Header dan footer Sumi & Washi
- [x] Penyesuaian mobile Sumi & Washi
- [x] Isi halaman Developer: tiga repo

## Selesai
- [x] Halaman pilih bahasa
- [x] Halaman tujuan per bahasa
- [x] Tombol ganti bahasa (dinamis membawa ke halaman setara)
- [x] Redirect otomatis sesuai bahasa browser
- [x] Isi HOME (ringkasan diri, motto 3E sebagai link, dua bagian buka-tutup)
- [x] Link dari HOME ke semua sub-halaman (3E, 12 portofolio, About, Contact) lewat tombol
- [x] Halaman Contact — kerangka selesai, isi menunggu Mizo
- [x] Desain visual dan warna theme (unsur Kanade)
- [x] Halaman 404 (tiga bahasa: id, en, ja)
- [x] SEO dan meta tags multibahasa (judul tab, hreflang, lang attribute, deskripsi per bahasa)
- [x] Tombol "Kembali ke HOME" di semua sub-halaman (dipasang otomatis ke _layouts/single.html menggunakan _includes/back-to-home.html dan class home-btn)
- [x] Gambar preview (og:image) untuk share link (file di assets/images/og-image.png, tag dipasang terpusat di _includes/seo.html dan _config.yml)
- [x] Favicon tab browser aksen Kanade (file di assets/images/: favicon.svg, favicon.ico, favicon-32.png, apple-touch-icon.png dikecualikan dari larangan hex; tag dipasang terpusat di _includes/head/custom.html dan manual di index.html serta easter egg Kanade)
- [x] Sitemap dan robots.txt (jekyll-sitemap, easter egg Kanade dikecualikan via sitemap: false)
- [x] Structured data JSON-LD Person di HOME (3 bahasa, hanya nama panggung)
- [x] Pengecekan otomatis konsistensi 3 bahasa (skrip dan GitHub Action)
- [x] Peringatan teks Jepang tanpa lang="ja" di halaman id/en (tambahan di scripts/check-languages.py, hanya peringatan, tidak menggagalkan push)
- [x] Peringatan placeholder yang belum diisi (tambahan di scripts/check-languages.py, hanya peringatan, tidak menggagalkan push)
- [x] Standar embed YouTube dan lazy image tanpa JavaScript
- [x] Navigasi Sebelumnya/Berikutnya di portofolio (dipasang otomatis ke _layouts/single.html menggunakan _includes/portfolio-nav.html, urutan halaman di _data/portfolio-nav.yml)
- [x] Mode terang dan tombol ganti tema (rencana multi-sesi, lihat bagian "Rencana: Mode Terang")
