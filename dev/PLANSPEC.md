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

## Samakan nama portofolio dengan Big Eleventh Skills

Tujuan: Daftar halaman portofolio di web harus sama dengan 11 skill pemilik (3 pilar dan 8 sayap). Ini hanya penyesuaian nama dan daftar halaman. Belum ada isi yang diisi.

Tempat dan tampilan:
- Tidak ada elemen tampilan baru. Yang berubah hanya teks nama halaman, tombol di HOME, dan navigasi Sebelumnya/Berikutnya.

Aturan:
- Main Portfolio menjadi tiga halaman: Psikologi, HR, Linguistik Terapan & Multilingual. Halaman "Bahasa Jepang" diganti namanya menjadi Linguistik Terapan & Multilingual.
- Additional Portfolio menjadi delapan halaman, dengan urutan ini:
  1. Developer (sebelumnya Coding)
  2. Data Science/Analyst (sebelumnya Data Analysis)
  3. Desain & UI/UX (sebelumnya Design)
  4. Ilustrasi & Seni Visual (sebelumnya Illustration)
  5. Literasi & Creative Writing (sebelumnya Writing)
  6. Audio & Komposisi Musik (sebelumnya Music)
  7. Operasional Domestik & Kuliner (sebelumnya Cooking)
  8. Entrepreneurship (halaman baru)
- Halaman Second Brain dan Sport dihapus di tiga bahasa (id, en, ja), termasuk semua link ke keduanya.
- Halaman Entrepreneurship dibuat sebagai kerangka kosong dengan pola yang sama seperti halaman Additional Portfolio lain, di tiga bahasa, dengan placeholder [TEKS DARI MIZO]. Jangan menulis isi sendiri.
- Nama tampil per bahasa:
  - Linguistik Terapan & Multilingual / Applied Linguistics & Multilingual / 応用言語学とマルチリンガル
  - Developer / Developer / デベロッパー
  - Data Science/Analyst / Data Science/Analyst / データサイエンス/アナリスト
  - Desain & UI/UX / Design & UI/UX / デザインとUI/UX
  - Ilustrasi & Seni Visual / Illustration & Visual Arts / イラストとビジュアルアート
  - Literasi & Creative Writing / Literacy & Creative Writing / リテラシーとクリエイティブライティング
  - Audio & Komposisi Musik / Audio & Music Composition / オーディオと作曲
  - Operasional Domestik & Kuliner / Domestic Operations & Culinary / 家事運営と料理
  - Entrepreneurship / Entrepreneurship / 起業
- Nama di judul halaman, tombol HOME, navigasi Sebelumnya/Berikutnya (dev/data/portfolio-nav.yml sesuai lokasi aslinya di _data/portfolio-nav.yml), dan JSON-LD kalau ada harus ikut berubah di tiga bahasa.
- Slug dan permalink halaman yang diganti nama mengikuti pola penamanya yang sudah ada di repo. Isi tiga bahasa tetap sama strukturnya.
- Perbarui pohon "Mapping web" dan teks status di dev/PLAN.md supaya cocok dengan daftar baru (jumlah halaman Additional jadi 8, total portofolio jadi 11). Jangan ubah item di bagian "Selesai".
- Jangan mengubah isi halaman yang sudah ada selain nama, jangan mengubah salam pembuka, dan jangan menyentuh halaman 3E, About, Contact, dan easter egg Kanade.

Data:
- Tidak ada perubahan struktur data, sinkron Drive, ekspor, atau impor.

Cek manual:
- Jalankan python scripts/check-languages.py. Hasilnya harus tanpa error, dan tidak ada link rusak ke halaman Second Brain atau Sport.
- Buka HOME di id, en, dan ja. Main Portfolio menampilkan 3 tombol dan Additional Portfolio menampilkan 8 tombol dengan nama baru.
- Dari halaman pertama sampai terakhir di portofolio, klik Sebelumnya/Berikutnya. Urutannya sesuai daftar di atas dan tidak ada halaman Second Brain atau Sport.
- Buka halaman Entrepreneurship di tiga bahasa. Kerangkanya sama seperti halaman lain dan muncul peringatan placeholder dari skrip, bukan error.

## Perpendek nama portofolio jadi 1 kata

Tujuan: Nama 11 halaman portofolio terlalu panjang untuk label tombol dan judul halaman. Semuanya dipendekkan jadi satu kata. Hanya nama yang berubah, isi halaman tidak.

Tempat dan tampilan:
- Tidak ada elemen tampilan baru. Yang berubah hanya teks nama di judul halaman, tombol di HOME, dan navigasi Sebelumnya/Berikutnya.

Aturan:
- Nama baru per bahasa (id / en / ja):
  - Psikologi / Psychology / 心理学
  - HR / HR / HR
  - Linguistik / Linguistics / 言語学
  - Developer / Developer / 開発
  - Data / Data / データ
  - Desain / Design / デザイン
  - Ilustrasi / Illustration / イラスト
  - Menulis / Writing / 執筆
  - Musik / Music / 音楽
  - Kuliner / Culinary / 料理
  - Wirausaha / Entrepreneurship / 起業
- Urutan dan pembagian tidak berubah. Main Portfolio: Psikologi, HR, Linguistik. Additional Portfolio: Developer, Data, Desain, Ilustrasi, Menulis, Musik, Kuliner, Wirausaha.
- Nama baru dipakai di semua tempat nama lama muncul, di tiga bahasa: judul halaman (H1), judul tab browser, tombol di HOME, navigasi Sebelumnya/Berikutnya, file _data/portfolio-nav.yml, teks meta description dan teks alt gambar preview yang menyebut nama portofolio, dan JSON-LD kalau ada.
- Slug dan permalink ikut dipendekkan menjadi: psychology, hr, linguistics, developer, data, design, illustration, writing, music, culinary, entrepreneurship. Slug sama di tiga bahasa, mengikuti pola URL yang sudah ada (/id/portfolio/[slug]/, /en/portfolio/[slug]/, /ja/portfolio/[slug]/).
- Semua link internal, hreflang, tombol ganti bahasa, dan sitemap harus mengikuti slug baru. Tidak ada link ke slug lama yang tersisa.
- Jangan mengubah isi halaman selain nama, jangan mengubah salam pembuka, dan jangan menyentuh halaman 3E, About, Contact, dan easter egg Kanade.
- Jangan membuat redirect dari slug lama.
- Perbarui pohon "Mapping web" di dev/PLAN.md supaya memakai nama baru. Jangan ubah item di bagian "Selesai".

Data:
- Tidak ada perubahan struktur data, sinkron Drive, ekspor, atau impor.

Cek manual:
- Jalankan python scripts/check-languages.py. Hasilnya tanpa error dan tanpa link rusak.
- Cari teks nama lama (contoh: "Linguistik Terapan", "Applied Linguistics", "応用言語学", "Operasional Domestik", "Data Science/Analyst", "Creative Writing") di seluruh repo di luar dev/arsip/ dan dev/CHANGELOG.md. Tidak boleh ada yang tersisa.
- Buka HOME di id, en, dan ja. Main Portfolio menampilkan 3 tombol dan Additional Portfolio menampilkan 8 tombol, semuanya satu kata.
- Dari halaman portofolio pertama sampai terakhir, klik Sebelumnya/Berikutnya. Urutannya sesuai daftar di atas.
- Di salah satu halaman portofolio, klik tombol ganti bahasa. Tujuannya halaman setara di bahasa lain dengan slug baru.
