## Rencana: Mode Terang (multi-sesi)

Tujuan: pengunjung bisa memilih tampilan terang atau gelap. Situs tetap statis.

Keputusan:
- Pakai tombol ganti tema (Opsi B), bukan hanya ikut pengaturan sistem.
- Default saat pertama kali dibuka: ikut pengaturan terang/gelap di perangkat pengunjung (`prefers-color-scheme`).
- Setelah pengunjung menekan tombol, pilihannya disimpan di `localStorage` dan dipakai di semua halaman dan semua bahasa.
- Tanpa JavaScript, situs tetap bekerja: tampilan ikut pengaturan sistem lewat CSS `@media (prefers-color-scheme)`.
- JavaScript hanya dipakai untuk fitur tema ini (tombol, penyimpanan pilihan, skrip anti-kedip). Fitur lain tetap tanpa JavaScript.
- Palet terang harus tetap bernuansa Kanade. Warna terang dipilih berdasarkan angka kontras dari Sesi 1, bukan ditebak.

Kendala teknis yang diketahui:
- Tema Minimal Mistakes memakai variabel SCSS, jadi warna sudah menjadi hex saat build dan tidak bisa berubah saat runtime. Perlu cara agar warna bisa berganti, misalnya kompilasi dua set warna di bawah selector `[data-theme="light"]` dan `[data-theme="dark"]`, atau mengubah tema supaya memakai CSS variable.
- Aturan palet sekarang bentrok dengan rencana ini ("palet Kanade wajib sama", "hex hanya di `_kanade.scss`"). Aturannya direvisi di Sesi 2.
- Halaman standalone ikut kena: `index.html`, `404.html`, dan easter egg Kanade. Easter egg paling rumit karena kanji 奏 di-blend ke background, jadi butuh versi terang yang tetap menyatu.
- Perlu skrip kecil di `<head>` yang menerapkan tema sebelum halaman tampil, supaya tidak berkedip.
- og-image dan favicon tidak berubah (satu versi).

Urutan sesi (satu sesi satu tugas):
- [x] Sesi 1: Audit kontras warna dan fokus keyboard di mode gelap yang sekarang. Catat rasio kontras pasangan warna utama (teks, aksen, link, tombol, hover, visited). Perbaiki hanya masalah fokus keyboard. Hasil angka ditulis di `CATATAN.md`.
- [x] Sesi 2: Fondasi palet terang. Tambah palet terang di `_kanade.scss`, variabel baru di `kanade-palette.scss`, mekanisme `[data-theme]` dan fallback `@media` di halaman Minimal Mistakes. Revisi aturan tema di `CATATAN.md`. Belum ada tombol.
- [x] Sesi 3: Tombol ganti tema, skrip anti-kedip di `<head>`, penyimpanan pilihan di `localStorage`, default ikut sistem. Tombol ikut dipasang secara terpusat dan teksnya tiga bahasa (id, en, ja).
- [x] Sesi 4: Halaman standalone `index.html` (pilih bahasa) dan `404.html` mendukung dua tema.
- [x] Sesi 5: Easter egg Kanade mendukung dua tema (kanji 奏 tetap menyatu dengan background di keduanya).
- [x] Sesi 6: Pengecekan akhir. Perbarui `scripts/check-languages.py` agar ikut memeriksa warna hardcode dan teks tombol tiga bahasa. Cek semua halaman x 3 bahasa x 2 tema. Pastikan kontras lolos.
