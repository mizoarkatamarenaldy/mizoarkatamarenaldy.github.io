# Catatan Proyek: Web Portofolio

## Ringkasan
Situs portofolio pribadi di GitHub Pages, fork tema Jekyll Minimal Mistakes.
Static saja (tanpa backend). Tema tidak akan diupdate dari upstream, boleh edit file mana pun.

## Struktur
- index.html: halaman pilih bahasa (3 kartu) + redirect otomatis sesuai bahasa browser
- _pages/: halaman per bahasa (/id/main/, /en/main/, /ja/main/)
- Kode bahasa yang dipakai: id, en, ja (bukan jp)
- Site title: "Main Page"

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
- [ ] (fitur berikutnya)

## Aturan untuk agent
- Kerjakan satu tugas per sesi.
- Jangan ubah file di luar tugas.
- Di akhir, kabari file apa saja yang diubah.