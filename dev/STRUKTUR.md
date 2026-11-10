# Struktur

## Struktur teknis
- index.html: halaman pilih bahasa (3 kartu) + redirect otomatis sesuai bahasa browser
- 404.html: halaman 404 tiga bahasa (id, en, ja) tanpa JavaScript + tombol ke /?pilih
- _pages/: halaman per bahasa (/id/main/, /en/main/, /ja/main/)
- Kode bahasa yang dipakai: id, en, ja (bukan jp)
- Site title: "Main Page"
- Cara pakai include baru:
  `{% include youtube-embed.html id="..." title="..." %}`
  `{% include lazy-image.html src="..." alt="..." width="..." height="..." %}`
  `{% include portfolio-nav.html %}` (dipasang otomatis di _layouts/single.html)

## Aturan mapping
- Main Portfolio = 3 halaman terpisah (Psikologi, HR, Linguistik Terapan & Multilingual), karena kontennya banyak.
- Additional Portfolio = 8 halaman.
- Elemen buka-tutup dipakai di HOME saja. Pakai tag `<details>` (tanpa JavaScript).
  Kalau isinya Markdown, tambahkan `markdown="1"` di tag `<details>`.
- Konten paling mentok: embed video YouTube atau foto yang ditempel langsung.
- Slug URL tiap sub-halaman mengacu ke bagian "Slug URL" di bawah sebagai sumber yang berlaku.

## Slug URL
Sama di semua bahasa, huruf kecil, bahasa Inggris. `{lang}` = `id`, `en`, `ja`.
File di `_pages/` bernama `{lang}-{slug}.md`, `/` di slug diganti `-`
(contoh: `id-3e.md`, `id-portfolio-psychology.md`).

| Halaman | Slug |
|---|---|
| HOME | `/{lang}/main/` |
| 3E | `/{lang}/3e/` |
| About | `/{lang}/about/` |
| Contact | `/{lang}/contact/` |
| Main Portfolio: Psikologi | `/{lang}/portfolio/psychology/` |
| Main Portfolio: HR | `/{lang}/portfolio/hr/` |
| Main Portfolio: Linguistik Terapan & Multilingual | `/{lang}/portfolio/applied-linguistics-multilingual/` |
| Additional: Developer | `/{lang}/portfolio/developer/` |
| Additional: Data Science/Analyst | `/{lang}/portfolio/data-science-analyst/` |
| Additional: Desain & UI/UX | `/{lang}/portfolio/design-ui-ux/` |
| Additional: Ilustrasi & Seni Visual | `/{lang}/portfolio/illustration-visual-arts/` |
| Additional: Literasi & Creative Writing | `/{lang}/portfolio/literacy-creative-writing/` |
| Additional: Audio & Komposisi Musik | `/{lang}/portfolio/audio-music-composition/` |
| Additional: Operasional Domestik & Kuliner | `/{lang}/portfolio/domestic-operations-culinary/` |
| Additional: Entrepreneurship | `/{lang}/portfolio/entrepreneurship/` |
