# Catatan Proyek: Web Portofolio

## Ringkasan
Situs portofolio pribadi di GitHub Pages, fork tema Jekyll Minimal Mistakes.
Static saja (tanpa backend). Tema tidak akan diupdate dari upstream, boleh edit file mana pun.

## Struktur teknis
- index.html: halaman pilih bahasa (3 kartu) + redirect otomatis sesuai bahasa browser
- _pages/: halaman per bahasa (/id/main/, /en/main/, /ja/main/)
- Kode bahasa yang dipakai: id, en, ja (bukan jp)
- Site title: "Main Page"

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
      │     │     └── Bahasa Jepang
      │     └── [buka-tutup] Additional Portfolio
      │           ├── Coding
      │           ├── Data Analysis
      │           ├── Design
      │           ├── Illustration
      │           ├── Writing
      │           ├── Music
      │           ├── Second Brain
      │           ├── Sport
      │           └── Cooking
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

Aturan mapping:
- Main Portfolio = 3 halaman terpisah (Psikologi, HR, Bahasa Jepang), karena kontennya banyak.
- Additional Portfolio = 9 halaman, namanya sederhana (bukan istilah taksonomi skill).
- Elemen buka-tutup dipakai di HOME saja. Pakai tag `<details>` (tanpa JavaScript).
  Kalau isinya Markdown, tambahkan `markdown="1"` di tag `<details>`.
- Konten paling mentok: embed video YouTube atau foto yang ditempel langsung.
- Slug URL tiap sub-halaman belum ditentukan, putuskan saat halamannya dikerjakan
  dan catat di bawah ini.

## Keputusan
- Bahasa: Indonesia, English, Jepang
- Halaman pilih bahasa tetap bisa dibuka manual lewat /?pilih
- Salam pembuka tiap halaman ditulis manual oleh pemilik, jangan diubah agent

## Gotcha (jangan diulang)
- Jangan pakai include_cached untuk masthead, karena teksnya beda per bahasa
  (dulu bikin tombol "ganti bahasa" selalu berbahasa Inggris).

## Status fitur
- [x] Halaman pilih bahasa
- [x] Halaman tujuan per bahasa
- [x] Tombol ganti bahasa per bahasa
- [x] Redirect otomatis sesuai bahasa browser
- [ ] Isi HOME (ringkasan diri, motto 3E sebagai link, dua bagian buka-tutup)
- [ ] Halaman 3E
- [ ] Halaman About (latar belakang, pengalaman hidup, CV)
- [ ] Halaman Contact
- [ ] Halaman Main Portfolio (Psikologi, HR, Bahasa Jepang)
- [ ] Halaman Additional Portfolio (9 halaman)
- [ ] Easter egg Kanade (3 bahasa)
- [x] Desain visual dan warna theme (unsur Kanade)

## Aturan untuk agent
- Kerjakan satu tugas per sesi.
- Jangan ubah file di luar tugas.
- Di akhir, kabari file apa saja yang diubah.
- Aturan tema:
  - Layout halaman bebas dan boleh berbeda-beda. Yang wajib sama di semua halaman hanya palet warnanya (palet Kanade).
  - Palet disimpan di satu tempat sebagai variabel CSS (`:root { --kanade-... }`) di `assets/css/kanade-palette.css`. File skin dan semua halaman mengambil warna dari sini, jadi ubah di satu tempat berlaku ke semua.
  - Setiap halaman atau layout baru, termasuk yang tanpa layout Minimal Mistakes, wajib memuat `kanade-palette.css`.
  - Dilarang warna hardcode (`#fff`, `white`, `black`, kode hex) di halaman, include, atau CSS baru. Pakai variabel palet. Butuh warna baru? Tambah dulu ke `kanade-palette.css`.

## Skin Kanade
- Nama skin: `kanade`
- File skin: `_sass/minimal-mistakes/skins/_kanade.scss`
- Sumber palet warna: `index.html` (halaman pilih bahasa)
  - Background: `#121016` (ungu-hitam gelap)
  - Teks: `#EDEAF0` (lavender terang)
  - Aksen/primary: `#BB6588` (pink Kanade)
- Diaktifkan via `_config.yml` → `minimal_mistakes_skin: "kanade"`

### Gotcha saat pembuatan skin
- Tidak ada warna hardcode di `_includes/`, `_layouts/`, atau `_pages/`.
  Semua modul SCSS Minimal Mistakes sudah pakai variabel, jadi cukup
  override variabel di file skin saja.
- File `_includes/head/custom.html` kosong (tidak ada CSS tambahan).
- Jika nanti menambah CSS custom (misal untuk elemen buka-tutup `<details>`
  atau easter egg), gunakan variabel `$background-color`, `$text-color`,
  dan `$primary-color` yang sudah didefinisikan skin, jangan hardcode.
