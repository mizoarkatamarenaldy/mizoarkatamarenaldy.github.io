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

## Token dan font Sumi & Washi

Tujuan: Menyiapkan fondasi desain baru (token warna dan font) supaya sesi berikutnya (layout home, header, footer, mobile) bisa memakainya. Sesi ini tidak mengubah layout atau komponen apa pun.

Tempat dan tampilan:
- Warna: hanya variabel baru di _kanade.scss yang belum dipakai di elemen mana pun, jadi warna tampilan tidak berubah.
- Font: semua halaman yang memakai layout tema. Heading (h1 sampai h6) dan judul masthead memakai serif, teks lainnya memakai sans. Ukuran, berat, jarak, dan layout tidak berubah.

Aturan:
- Semua nilai hex hanya ditulis di _kanade.scss.
- Tambahkan token hanya kalau belum ada padanan perannya di _kanade.scss. Nilai variabel yang sudah ada tidak diubah. Ikuti pola penamaan yang sudah ada.
- Token mode gelap: rose #BB6588 (aksen utama), plum #93506B (hover dan garis aksen sekunder), hanko #C25450 (hanya untuk stempel hanko, bukan teks), bamboo ash #9A96A0 (teks sekunder), fusuma wire #26232D (garis pembagi). Latar #121016 dan teks #EDEAF0 sudah ada.
- Token mode terang: washi #F8F6F0 (latar), ink #1D1A20 (teks), dry reed #706B76 (teks sekunder), rice paper seam #E5E0D5 (garis pembagi). Definisikan sebagai variabel terpisah berakhiran -light sesuai gotcha SASS di RULES.md.
- Di dev/DESIGN.md, buat bagian baru "Sumi & Washi" tanpa mengubah bagian lama. Isinya semua token baru beserta nilainya, font yang dipakai, dan catatan ini: di mode terang, rose #BB6588 tidak dipakai untuk teks kecil (kontras 3,65:1 di atas #F8F6F0, batas 4,5:1), pakai plum #93506B (5,4:1).
- Font dimuat lewat satu link Google Fonts di _includes/head/custom.html dengan display=swap. Keluarga dan berat: Noto Serif 300 dan 400 (normal dan italic), Plus Jakarta Sans 400, 500, 600, Noto Serif JP 300 dan 400.
- Stack serif: "Noto Serif", "Noto Serif JP", Georgia, serif. Stack sans: "Plus Jakarta Sans", system-ui, sans-serif.
- Terapkan lewat variabel font bawaan tema di _kanade.scss (font global dan font header), bukan dengan aturan CSS baru, kecuali variabel tidak cukup. Berlaku di semua file entry SASS tema, termasuk main-light.scss dan main-light-os.scss.
- Tidak mengubah font monospace, ukuran, berat, jarak, layout, atau teks halaman.
- Tidak memakai Tailwind, Material Symbols, gambar, atau hanko.
- Tidak menyentuh halaman pilih bahasa (index.html) dan easter egg Kanade.

Data:
- Tidak ada perubahan struktur data di _data/, URL, atau permalink.

Cek manual:
- Jalankan python scripts/check-languages.py. Tidak ada error baru dan tidak ada peringatan warna hardcode baru.
- Buka /id/main/, /en/main/, dan /ja/main/ di mode gelap. Semua warna sama seperti sebelum sesi. Judul tampil serif, teks lain sans. Di /ja/ huruf Jepang pada judul memakai Noto Serif JP (cek di DevTools, bagian Rendered Fonts).
- Ganti ke mode terang lewat tombol tema di salah satu halaman. Warna sama seperti sebelum sesi, font sama seperti mode gelap, tombol tema masih berfungsi.
- Buka /?pilih dan halaman easter egg Kanade. Tampilannya persis sama seperti sebelum sesi.

## Layout HOME Sumi & Washi

Tujuan: Mengubah tata letak HOME (/id/main/, /en/main/, /ja/main/) menjadi dua kolom: hero di kiri dan sidebar portofolio di kanan, memakai token dan font dari bagian "Sumi & Washi" di dev/DESIGN.md. Hanya HOME yang berubah.

Tempat dan tampilan:
- Layout baru khusus HOME. Isi hero dari atas ke bawah: salam pembuka, nama lengkap (h1), motto 3E, ringkasan diri.
- Sidebar kanan berisi dua bagian buka-tutup: Main Portfolio (Psikologi, HR, Linguistik) dan Additional Portfolio (Developer, Data, Desain, Ilustrasi, Menulis, Musik, Kuliner, Wirausaha).
- Pakai teks, label, dan URL yang sudah ada di HOME sekarang untuk semua elemen di atas. Jangan ganti kata atau tautannya.
- Konten tengah dengan lebar maksimum 80rem dan padding samping 2rem. Jarak vertikal atas dan bawah 3rem, dan 6rem di layar lebar (1024px ke atas).
- Layar 1024px ke atas: grid dua kolom, hero 2/3 lebar dan sidebar 1/3 lebar. Sidebar punya padding kiri 3rem dan garis vertikal 1px di sisi kirinya.
- Layar di bawah 1024px: hero lalu sidebar bertumpuk ke bawah, garis vertikal dihilangkan. Desain mobile khusus dikerjakan di sesi lain.
- Salam pembuka: teks body 15px, baris 26px, warna teks sekunder, di atas nama.
- Nama (h1): serif 56px dengan baris 68px, berat 400, letter-spacing -0.02em. Di bawah 1024px: 38px dengan baris 48px, letter-spacing -0.01em.
- Motto: serif italic berat 300, 22px dengan baris 30px, tetap berupa teks link ke halaman 3E (bukan tombol), dengan garis bawah 1px. Saat kursor diarahkan, warna teks dan garis bawah berubah ke aksen.
- Ringkasan diri: serif berat 300, 19px dengan baris 32px, warna teks sekunder, lebar maksimum 36rem.
- Judul bagian sidebar (h2): serif 22px, berat 400.
- Baris Main Portfolio: nama sans 17px dengan baris 24px, berat 600, nomor 01 sampai 03 di kanan (sans 10px, berat 500, letter-spacing 0.18em, warna sekunder). Baris dipisah garis 1px.
- Baris Additional Portfolio: nama sans 15px dengan baris 26px, berat 400, dipisah garis 1px, tanpa nomor.
- Seluruh baris adalah link ke sub-halamannya. Saat kursor diarahkan, warna nama berubah ke aksen.
- Warna: latar, teks, dan teks sekunder memakai token yang ada. Garis pembagi memakai fusuma wire di mode gelap dan rice paper seam di mode terang. Aksen hover memakai rose di mode gelap dan plum di mode terang.
- Tanpa border radius, tanpa bayangan, tanpa animasi gerak.

Aturan:
- Main Portfolio terbuka saat halaman dimuat, Additional Portfolio tertutup.
- Pakai mekanisme buka-tutup yang sudah ada di HOME. Harus bisa dioperasikan dengan keyboard.
- Tidak ada hex baru. Hanya pakai token yang sudah ada di _kanade.scss.
- Teks salam pembuka dan ringkasan diri tidak diubah, hanya dipindahkan posisinya.
- JSON-LD Person, hreflang, dan meta tags di HOME tetap utuh.
- Pemicu easter egg Kanade (kanji 奏) di HOME tetap ada, tetap tersembunyi di latar, tetap bisa di-hover dan diklik, dan tidak ikut terblok saat Ctrl+A. Perilakunya tidak berubah, boleh dipindahkan posisinya saja.
- Tidak mengubah header, footer, tombol ganti bahasa, tombol ganti tema, dan halaman selain HOME.
- Tidak mengubah _layouts/single.html, karena dipakai semua sub-halaman.
- Tidak menambah teks vertikal Jepang, hanko, subjudul, deskripsi tiap portofolio, daftar karya, atau konten lain dari desain Stitch yang belum ada di HOME.
- Tidak memakai Tailwind, Material Symbols, atau font monospace.

Data:
- Tidak ada perubahan struktur data di _data/, URL, atau permalink.

Cek manual:
- Jalankan python scripts/check-languages.py. Tidak ada error baru, tidak ada peringatan warna hardcode baru.
- Buka /en/main/ di layar lebar mode gelap. Hero di kiri, sidebar di kanan dengan garis vertikal tipis. Main Portfolio terbuka dengan tiga baris, Additional Portfolio tertutup. Klik Additional Portfolio, delapan baris muncul. Klik satu baris, halaman tujuan benar. Arahkan kursor ke motto, warna berubah, lalu klik, halaman 3E terbuka.
- Ulangi di mode terang lewat tombol tema. Semua teks terbaca, aksen hover memakai plum, tombol tema masih berfungsi.
- Buka /id/main/ dan /ja/main/. Struktur sama dengan /en/main/, teks sesuai bahasa, huruf Jepang tidak terpotong. Teks salam pembuka dan ringkasan sama persis seperti sebelum sesi.
- Perkecil lebar jendela ke 360px. Hero lalu sidebar bertumpuk, tidak ada scroll horizontal.
- Di HOME, arahkan kursor ke posisi kanji 奏. Kanji muncul, klik membuka easter egg. Tekan Ctrl+A, kanji tidak ikut terblok.
- Lihat source HOME. JSON-LD Person dan tag hreflang masih ada.

## Header dan footer Sumi & Washi

Tujuan: Menyamakan tampilan header (masthead) dan footer di semua halaman bahasa dengan desain "Sumi & Washi" di dev/DESIGN.md. Hanya tampilan yang berubah, bukan isi, teks, atau fungsinya.

Tempat dan tampilan:
- Header dan footer di semua halaman yang memakai layout tema (HOME, sub-halaman, 404).
- Konten header dan footer memakai lebar maksimum 80rem, di tengah, padding samping 2rem. Di bawah 768px padding samping 1rem.
- Header: tinggi 5rem (4rem di bawah 768px), tidak menempel saat scroll, garis bawah 1px. Kiri: judul situs (teks yang sudah ada), link ke HOME bahasa yang sedang dibuka. Kanan: tombol ganti bahasa dan tombol ganti tema yang sudah ada, berjarak 1.5rem.
- Judul situs: serif 22px dengan baris 30px, berat 400, warna teks utama. Di bawah 768px: 17px dengan baris 24px, boleh turun ke dua baris.
- Tombol header: sans 10px dengan baris 14px, berat 500, huruf kapital, letter-spacing 0.18em, warna teks sekunder. Saat kursor diarahkan, warna berubah ke aksen. Area sentuh tiap tombol minimal 44px tingginya.
- Footer: garis atas 1px, jarak atas dari konten 6rem, padding atas dan bawah 3rem. Latar sama dengan latar halaman.
- Layar 768px ke atas: footer satu baris, rata dasar teks. Kiri: nama (teks yang sama dengan judul situs, serif 22px dengan baris 30px, berat 400, warna teks utama). Kanan: link About dan Contact, lalu kredit yang sudah ada. Di bawah 768px: ketiganya bertumpuk ke bawah, jarak 1.5rem.
- Link About dan Contact: sans 11px dengan baris 16px, berat 600, huruf kapital, letter-spacing 0.14em, warna teks sekunder, jarak antar link 1.5rem. Saat kursor diarahkan, warna berubah ke aksen. Teks label dan URL memakai yang sudah dipakai untuk link About dan Contact di HOME, sesuai bahasa halaman.
- Kredit footer: teks yang sudah ada, sans 10px dengan baris 14px, berat 500, huruf kapital, letter-spacing 0.18em, warna teks sekunder.
- Warna: garis pembagi memakai fusuma wire di mode gelap dan rice paper seam di mode terang. Aksen hover memakai rose di mode gelap dan plum di mode terang.
- Tanpa border radius, tanpa bayangan, tanpa animasi gerak.

Aturan:
- Tombol ganti bahasa dan tombol ganti tema tetap satu tombol masing-masing seperti sekarang. Teks (tiga bahasa), link, dan perilakunya tidak diubah, hanya gayanya.
- Elemen header dan footer lain yang sudah ada tetap ada, teks dan fungsinya tidak diubah.
- Jangan pakai include_cached untuk masthead, sesuai gotcha di RULES.md.
- Tidak ada hex baru. Hanya pakai token yang sudah ada di _kanade.scss.
- Fokus keyboard tetap terlihat, pakai gaya fokus yang sudah ada.
- Tidak mengubah _layouts/single.html, layout HOME, tombol Kembali ke HOME, navigasi Sebelumnya/Berikutnya, halaman pilih bahasa (index.html), dan easter egg Kanade.
- Tidak menambah menu atas, foto atau avatar, ikon, deskripsi, tahun hak cipta baru, hanko, atau konten lain dari desain Stitch yang belum ada di situs.
- Tidak memakai Tailwind, Material Symbols, atau font monospace.

Data:
- Tidak ada perubahan struktur data di _data/, URL, atau permalink.

Cek manual:
- Jalankan python scripts/check-languages.py. Tidak ada error baru, tidak ada peringatan warna hardcode baru, teks tombol ganti tema tiga bahasa tetap lengkap.
- Buka /en/main/ di layar lebar mode gelap. Header: judul di kiri, dua tombol di kanan, garis tipis di bawah. Footer: garis tipis di atas, nama di kiri, About, Contact, dan kredit di kanan. Klik judul, HOME bahasa yang sama terbuka. Klik About dan Contact, halaman bahasa yang sama terbuka.
- Pakai tombol ganti bahasa dan tombol ganti tema. Keduanya berfungsi seperti sebelum sesi, dan warna berubah ke aksen saat kursor diarahkan.
- Ulangi di mode terang. Semua teks terbaca, aksen hover memakai plum, garis memakai warna seam.
- Buka /id/main/ dan /ja/main/. Teks sesuai bahasa, huruf Jepang tidak terpotong. Buka satu sub-halaman portofolio dan satu URL yang tidak ada (halaman 404). Header dan footer sama, tombol Kembali ke HOME dan navigasi Sebelumnya/Berikutnya tidak berubah.
- Perkecil lebar jendela ke 360px. Tidak ada scroll horizontal, kedua tombol mudah ditekan, judul boleh dua baris, footer bertumpuk.
- Buka /?pilih dan halaman easter egg Kanade. Tampilannya persis sama seperti sebelum sesi.

## Penyesuaian mobile Sumi & Washi

Tujuan: Merapikan HOME, header, dan footer di layar sempit dan tablet setelah item layout HOME serta header dan footer Sumi & Washi. Layar desktop tidak berubah.

Tempat dan tampilan:
- Tiga rentang lebar: di bawah 768px (mobile), 768px sampai 1023px (tablet), 1024px ke atas (desktop, tidak berubah).
- Padding samping isi HOME, header, dan footer disamakan: 1rem di bawah 768px, 2rem di 768px ke atas. Tepi kiri teks header, nama, ringkasan, baris sidebar, dan footer harus sejajar pada satu garis.
- Jarak vertikal HOME di bawah 768px: atas 3rem, antara hero dan sidebar 3rem, bawah 3rem.
- Tablet: hero dan sidebar bertumpuk selebar penuh, ringkasan diri tetap maksimum 36rem.
- Judul pemicu buka-tutup dan semua baris di sidebar (Main Portfolio dan Additional Portfolio): tinggi minimal 44px, seluruh lebar baris bisa disentuh.
- Motto, nama, dan judul situs boleh turun baris antar kata. Tidak boleh ada scroll horizontal pada lebar 320px.
- Warna aksen hover (header, footer, sidebar HOME, motto) hanya berlaku di perangkat yang punya hover (@media (hover: hover)). Di layar sentuh, warna aksen muncul saat disentuh (:active) dan hilang saat jari diangkat.

Aturan:
- Tampilan di 1024px ke atas tidak berubah sama sekali.
- Teks, URL, dan fungsi semua elemen tidak diubah.
- Tidak ada hex baru, tanpa border radius, tanpa bayangan, tanpa animasi gerak.
- Pemicu easter egg Kanade di HOME tidak berubah perilakunya dan tidak menimpa atau tertimpa elemen lain pada lebar 360px.
- Tidak menambah menu hamburger, drawer, bottom nav, kartu berlatar, avatar, hanko, teks vertikal Jepang, atau konten lain dari desain mobile Stitch.
- Tidak mengubah _layouts/single.html, halaman pilih bahasa (index.html), dan easter egg Kanade.

Data:
- Tidak ada perubahan struktur data di _data/, URL, atau permalink.

Cek manual:
- Jalankan python scripts/check-languages.py. Tidak ada error baru, tidak ada peringatan warna hardcode baru.
- Buka /en/main/ di lebar 320px, 360px, dan 390px. Tidak ada scroll horizontal. Tepi kiri header, nama, ringkasan, baris sidebar, dan footer sejajar.
- Buka /en/main/ di lebar 768px dan 1023px. Hero dan sidebar bertumpuk, tepi sejajar dengan padding 2rem, ringkasan tidak lebih lebar dari 36rem.
- Buka /en/main/ di lebar 1280px. Tampilan sama persis seperti setelah item layout HOME dan item header footer.
- Aktifkan emulasi sentuh di DevTools. Tinggi baris sidebar dan tombol header minimal 44px. Sentuh satu baris sidebar, warna aksen muncul, lalu hilang setelah jari diangkat.
- Buka /id/main/ dan /ja/main/ di mode terang pada lebar 360px. Teks terbaca dan tidak terpotong, huruf Jepang tidak terpotong.
- Buka satu sub-halaman portofolio dan satu URL yang tidak ada (halaman 404) pada lebar 360px. Header dan footer sejajar sama seperti HOME, tidak ada scroll horizontal.
- Buka /?pilih dan halaman easter egg Kanade. Tampilannya persis sama seperti sebelum sesi.

## Isi halaman Developer: tiga repo

Tujuan: Menampilkan tiga repo GitHub milik pemilik di halaman Developer (bagian Additional Portfolio), supaya pengunjung bisa melihat dan membuka proyeknya.

Tempat dan tampilan:
- Halaman Developer di /id/, /en/, dan /ja/. Cari lokasi filenya lewat dev/STRUKTUR.md.
- Tiga kartu atau item daftar, urutan: mizan-okane, shugen-hub, Shinri-LLM.
- Tiap item berisi nama repo (teks tetap, tidak diterjemahkan), satu baris deskripsi, dan tautan ke repo.
- Tautan:
  - https://github.com/mizoarkatamarenaldy/mizan-okane
  - https://github.com/mizoarkatamarenaldy/shugen-hub
  - https://github.com/mizoarkatamarenaldy/Shinri-LLM
- Teks deskripsi di semua bahasa ditulis persis "[TEKS DARI MIZO]". Pemilik yang mengisinya nanti.
- Teks tautan: id "Buka di GitHub", en "Open on GitHub", ja "GitHubで開く".

Aturan:
- Isi tiga bahasa sama: jumlah item, urutan, dan tautan identik.
- Tautan keluar dibuka di tab baru dengan rel="noopener noreferrer".
- Deskripsi tidak boleh ditulis atau dikarang oleh agent.
- Teks Jepang di halaman id dan en wajib memakai atribut lang="ja".
- Salam pembuka halaman tidak diubah.
- Tidak ada nama asli, kampus, atau data pribadi lain di halaman.
- Tidak ada warna hardcode, tidak ada JavaScript baru, tidak ada gambar baru.
- Tidak mengubah halaman lain, _config.yml, atau _data/portfolio-nav.yml.

Data:
- Tidak ada perubahan struktur data, _config.yml, atau navigasi.

Cek manual:
- Buka halaman Developer di /id/, /en/, dan /ja/: tiga item tampil dengan urutan sama dan tautannya mengarah ke repo yang benar.
- Klik tautan tiap item: repo GitHub terbuka di tab baru.
- Jalankan python scripts/check-languages.py: tidak ada error. Peringatan placeholder untuk "[TEKS DARI MIZO]" boleh muncul.
- Ganti bahasa lewat tombol di masthead: pindah ke halaman Developer yang setara.
- Buka di mode gelap dan mode terang: teks dan tautan terbaca.

## Samakan gaya link dan tombol

Tujuan: Link dan tombol di seluruh situs tampil dengan gaya yang sama, karena sekarang ada empat gaya berbeda dan situs terasa tidak konsisten.

Tempat dan tampilan:
- Link teks yang dipakai sekarang: motto 3E di HOME (italic, underline putih), "Next/Previous" di navigasi portofolio (warna pink-ungu dengan underline, terlihat seperti warna link bawaan tema), dan "Open on GitHub" di halaman Developer (putih dengan underline abu).
- Tombol yang dipakai sekarang: "Back to HOME" (border pink).
- Semua link teks memakai satu gaya, dengan gaya link motto 3E sebagai acuan (warna teks utama, underline tipis).
- Semua tombol memakai satu gaya, dengan gaya "Back to HOME" sebagai acuan.
- Gaya hover, focus, dan visited juga disamakan di semua link dan tombol tersebut.

Aturan:
- Hanya CSS yang diubah. Teks, urutan, dan struktur HTML tidak berubah.
- Motto 3E tetap italic. Yang disamakan hanya warna, underline, hover, dan visited.
- Warna, ukuran, dan font diambil dari token di dev/DESIGN.md. Tidak ada warna hex baru dan tidak ada warna hardcode.
- Gaya bawaan Minimal Mistakes untuk `a:hover` dan `a:visited` tidak boleh menimpa gaya baru. Ikuti gotcha spesifisitas CSS di dev/RULES.md.
- Berlaku di mode gelap dan mode terang, di tiga bahasa (id, en, ja).
- Border kartu (kartu Developer dan Contact) tidak diubah di item ini.
- Link di masthead dan footer tidak diubah di item ini.

Data:
- Tidak ada perubahan struktur data, sinkron Drive, ekspor, atau impor.

Cek manual:
- Buka HOME, halaman Psychology, dan halaman Developer di mode gelap. Motto 3E, "Next HR", dan "Open on GitHub" tampil dengan gaya link yang sama, termasuk saat kursor diarahkan dan setelah link pernah dikunjungi.
- Buka halaman Psychology. "Back to HOME" tampil dengan gaya tombol yang sama di semua sub-halaman yang punya tombol itu.
- Ganti ke mode terang lalu ulangi dua cek di atas. Warna tetap terbaca dan tetap sama antar elemen.
- Jalankan `python scripts/check-languages.py`. Tidak ada error baru dan tidak ada peringatan warna hardcode baru.

## Samakan desain sub-halaman standar dengan HOME

Tujuan: HOME sudah mengikuti desain Sumi & Washi (dev/DESIGN.md), tetapi sub-halaman masih tampil seperti gaya bawaan tema Minimal Mistakes. Item ini menyamakan sub-halaman standar dengan HOME. Acuannya HOME dan dev/DESIGN.md, bukan gaya baru dan bukan penyamaan acak antar halaman.

Tempat dan tampilan:
- Cakupan: Psychology, HR, Linguistics, About, 3E, dan halaman portofolio lain yang memakai layout sub-halaman yang sama. Halaman Developer dan Contact tidak termasuk, dikerjakan di sesi lain.
- Judul halaman memakai gaya judul HOME: serif besar, bobot dan ukuran mengikuti HOME, tidak tebal bawaan tema.
- Jarak antara header dan judul selega jarak header ke konten di HOME. Sekarang judul hampir menempel ke header.
- Teks isi memakai font sans dan ukuran yang sama dengan teks isi HOME. Sekarang teks placeholder lebih besar dari HOME.
- Lebar konten dan margin samping mengikuti HOME.
- Link Next dan Previous memakai warna, underline, dan efek hover yang sama dengan link di HOME. Sekarang berwarna pink-ungu dengan underline seperti link bawaan tema.
- Tombol "Back to HOME" memakai gaya tombol HOME, bukan border pink bawaan.
- Cara mengerjakan: baca CSS dan layout HOME dulu, lalu pakai ulang nilai, variabel, dan class yang sudah dipakai HOME. Jangan menebak nilai dari tampilan.

Aturan:
- Hanya CSS yang diubah. Teks dan struktur HTML tidak diubah.
- Tidak ada warna hex baru dan tidak ada warna hardcode. Semua warna dari variabel palet sesuai dev/DESIGN.md.
- Perhatikan gotcha spesifisitas CSS pada tag `<a>` di dev/RULES.md. Styling bawaan tema untuk `a:hover` dan `a:visited` tidak boleh menimpa gaya link dan tombol yang baru.
- Mode gelap dan mode terang harus sama-sama benar.
- Tiga bahasa (id, en, ja) harus tampil sama. Pastikan font serif untuk judul bahasa Jepang tetap memakai font stack di dev/DESIGN.md.
- Tampilan mobile tidak boleh rusak.
- Tidak mengubah HOME, header, footer, background, halaman Developer, dan halaman Contact.

Data:
- Tidak ada perubahan struktur data, sinkron Drive, ekspor, atau impor.

Cek manual:
- Buka halaman Psychology di /id/, /en/, dan /ja/ dalam mode gelap. Bandingkan dengan HOME: judul, jarak ke header, ukuran teks isi, dan lebar konten harus terasa satu keluarga.
- Ulangi di mode terang. Teks, link, dan tombol tetap terbaca, dan tidak ada warna bawaan tema yang muncul.
- Arahkan kursor ke link Next/Previous dan tombol Back to HOME, lalu klik salah satu dan kembali. Gaya hover dan visited sama dengan link di HOME.
- Buka About dan 3E. Gayanya sama dengan Psychology.
- Buka salah satu halaman di lebar layar HP. Tidak ada teks terpotong dan tidak ada scroll samping.
- Jalankan `python scripts/check-languages.py`. Tidak ada error, dan tidak ada peringatan warna hardcode baru.

## Samakan desain halaman Contact dengan HOME

Tujuan: Halaman Contact masih tampil seperti gaya bawaan tema dan punya dua bug tampilan. HOME sudah mengikuti desain Sumi & Washi (dev/DESIGN.md). Item ini menyamakan kartu Contact dengan gaya HOME dan memperbaiki dua bug tersebut. Acuannya HOME dan dev/DESIGN.md, bukan gaya baru.

Tempat dan tampilan:
- Cakupan: hanya halaman Contact di /id/, /en/, dan /ja/.
- Kartu: border pink diganti dengan bahasa visual HOME (garis tipis dari token pembagi di dev/DESIGN.md, jarak lega). Jarak dalam dan jarak antar kartu mengikuti HOME.
- Teks label dan isi kartu memakai font, ukuran, dan warna yang sama dengan teks di HOME. Link di dalam kartu memakai gaya link HOME: warna, underline, dan efek hover yang sama.
- Bug 1, label ganda: beberapa kartu menampilkan nama platform dua kali ("LinkedIn LinkedIn", "Wantedly Wantedly"). Cari penyebabnya dulu. Kalau penyebabnya CSS, perbaiki di CSS. Kalau penyebabnya teks di HTML, hapus salah satunya sehingga nama platform tampil satu kali di setiap kartu yang bermasalah. Perbaikan ini harus berlaku sama di tiga bahasa.
- Bug 2, handle GitHub terpotong: handle GitHub terpotong di tengah kata dan membuat kartunya lebih tinggi dari kartu lain. Perbaiki di CSS supaya handle tampil utuh dan tinggi semua kartu sejajar. Teks handle tidak diubah.
- Sub-halaman standar dan halaman Developer sudah disamakan dengan HOME di sesi sebelumnya. Pakai ulang nilai, variabel, dan class dari sana dan dari HOME untuk judul halaman, jarak ke header, lebar konten, dan tombol Back to HOME. Jangan membuat nilai baru.
- Cara mengerjakan: baca CSS HOME dan halaman yang sudah disamakan dulu, lalu pakai ulang nilainya. Jangan menebak nilai dari tampilan.

Aturan:
- Izin dari pemilik: perubahan di luar CSS hanya boleh satu hal, yaitu menghapus teks nama platform yang ganda di file halaman Contact (id, en, ja) kalau penyebab bug 1 ada di teks. Tidak ada perubahan teks atau struktur HTML lain.
- Tidak ada warna hex baru dan tidak ada warna hardcode. Semua warna dari variabel palet sesuai dev/DESIGN.md.
- Perhatikan gotcha spesifisitas CSS pada tag `<a>` di dev/RULES.md. Styling bawaan tema untuk `a:hover` dan `a:visited` tidak boleh menimpa gaya link di kartu.
- Mode gelap dan mode terang harus sama-sama benar.
- Tiga bahasa (id, en, ja) harus tampil sama dan konsisten, sesuai pengecekan di scripts/check-languages.py.
- Tampilan mobile tidak boleh rusak. Tidak ada teks terpotong dan kartu tidak melebar keluar layar.
- Tidak mengubah HOME, sub-halaman standar, halaman Developer, header, footer, dan background.

Data:
- Tidak ada perubahan struktur data, sinkron Drive, ekspor, atau impor.

Cek manual:
- Buka halaman Contact di /id/, /en/, dan /ja/ dalam mode gelap. Bandingkan dengan HOME: garis, jarak, font, dan warna link terasa satu keluarga. Tidak ada border pink.
- Cek semua kartu: nama platform tampil satu kali, termasuk LinkedIn dan Wantedly.
- Cek kartu GitHub: handle tampil utuh dan tinggi kartu sama dengan kartu lain yang sejajar.
- Ulangi di mode terang. Teks dan link tetap terbaca dan tidak ada warna bawaan tema yang muncul.
- Arahkan kursor ke link di kartu, lalu klik dan kembali. Gaya hover dan visited sama dengan link di HOME.
- Buka halaman Contact di lebar layar HP. Tidak ada teks terpotong dan tidak ada scroll samping.
- Jalankan `python scripts/check-languages.py`. Tidak ada error, dan tidak ada peringatan warna hardcode baru.

## Samakan desain halaman Developer dengan HOME

Tujuan: Halaman Developer (tiga kartu repo) masih tampil seperti gaya bawaan tema, sementara HOME sudah mengikuti desain Sumi & Washi (dev/DESIGN.md). Item ini menyamakan kartu repo dengan gaya HOME. Acuannya HOME dan dev/DESIGN.md, bukan gaya baru.

Tempat dan tampilan:
- Cakupan: hanya halaman Developer di /id/, /en/, dan /ja/.
- Kartu repo: border, garis pemisah, jarak dalam, dan jarak antar kartu mengikuti bahasa visual HOME (garis tipis dari token pembagi di dev/DESIGN.md, jarak lega). Sekarang berupa kartu dengan border tipis gelap kebiruan.
- Judul repo memakai font serif seperti judul di HOME. Teks deskripsi memakai font sans dengan ukuran dan warna sekunder yang sama dengan teks isi HOME. Sekarang teks placeholder berwarna abu yang tidak sama dengan HOME.
- Link "Open on GitHub" memakai gaya link HOME: warna, underline, dan efek hover yang sama. Sekarang putih dengan underline abu.
- Sub-halaman standar sudah disamakan dengan HOME di sesi sebelumnya. Pakai ulang nilai, variabel, dan class dari sana dan dari HOME untuk judul halaman, jarak ke header, lebar konten, dan tombol Back to HOME. Jangan membuat nilai baru.
- Cara mengerjakan: baca CSS HOME dan sub-halaman standar dulu, lalu pakai ulang nilainya. Jangan menebak nilai dari tampilan.

Aturan:
- Hanya CSS yang diubah. Teks dan struktur HTML tidak diubah.
- Tidak ada warna hex baru dan tidak ada warna hardcode. Semua warna dari variabel palet sesuai dev/DESIGN.md.
- Perhatikan gotcha spesifisitas CSS pada tag `<a>` di dev/RULES.md. Styling bawaan tema untuk `a:hover` dan `a:visited` tidak boleh menimpa gaya link "Open on GitHub".
- Mode gelap dan mode terang harus sama-sama benar.
- Tiga bahasa (id, en, ja) harus tampil sama.
- Tampilan mobile tidak boleh rusak. Teks panjang tidak boleh terpotong di tengah kata dan kartu tidak boleh melebar keluar layar.
- Tidak mengubah HOME, sub-halaman standar, halaman Contact, header, footer, dan background.

Data:
- Tidak ada perubahan struktur data, sinkron Drive, ekspor, atau impor.

Cek manual:
- Buka halaman Developer di /id/, /en/, dan /ja/ dalam mode gelap. Bandingkan dengan HOME: garis, jarak, font judul, dan font deskripsi terasa satu keluarga.
- Ulangi di mode terang. Teks dan link tetap terbaca dan tidak ada warna bawaan tema yang muncul.
- Arahkan kursor ke link "Open on GitHub", lalu klik dan kembali. Gaya hover dan visited sama dengan link di HOME.
- Buka halaman Developer di lebar layar HP. Tidak ada teks terpotong dan tidak ada scroll samping.
- Jalankan `python scripts/check-languages.py`. Tidak ada error, dan tidak ada peringatan warna hardcode baru.

## Samakan desain halaman Contact dengan HOME

Tujuan: Halaman Contact masih tampil seperti gaya bawaan tema dan punya dua bug tampilan. HOME sudah mengikuti desain Sumi & Washi (dev/DESIGN.md). Item ini menyamakan kartu Contact dengan gaya HOME dan memperbaiki dua bug tersebut. Acuannya HOME dan dev/DESIGN.md, bukan gaya baru.

Tempat dan tampilan:
- Cakupan: hanya halaman Contact di /id/, /en/, dan /ja/.
- Kartu: border pink diganti dengan bahasa visual HOME (garis tipis dari token pembagi di dev/DESIGN.md, jarak lega). Jarak dalam dan jarak antar kartu mengikuti HOME.
- Teks label dan isi kartu memakai font, ukuran, dan warna yang sama dengan teks di HOME. Link di dalam kartu memakai gaya link HOME: warna, underline, dan efek hover yang sama.
- Bug 1, label ganda: beberapa kartu menampilkan nama platform dua kali ("LinkedIn LinkedIn", "Wantedly Wantedly"). Cari penyebabnya dulu. Kalau penyebabnya CSS, perbaiki di CSS. Kalau penyebabnya teks di HTML, hapus salah satunya sehingga nama platform tampil satu kali di setiap kartu yang bermasalah. Perbaikan ini harus berlaku sama di tiga bahasa.
- Bug 2, handle GitHub terpotong: handle GitHub terpotong di tengah kata dan membuat kartunya lebih tinggi dari kartu lain. Perbaiki di CSS supaya handle tampil utuh dan tinggi semua kartu sejajar. Teks handle tidak diubah.
- Sub-halaman standar dan halaman Developer sudah disamakan dengan HOME di sesi sebelumnya. Pakai ulang nilai, variabel, dan class dari sana dan dari HOME untuk judul halaman, jarak ke header, lebar konten, dan tombol Back to HOME. Jangan membuat nilai baru.
- Cara mengerjakan: baca CSS HOME dan halaman yang sudah disamakan dulu, lalu pakai ulang nilainya. Jangan menebak nilai dari tampilan.

Aturan:
- Izin dari pemilik: perubahan di luar CSS hanya boleh satu hal, yaitu menghapus teks nama platform yang ganda di file halaman Contact (id, en, ja) kalau penyebab bug 1 ada di teks. Tidak ada perubahan teks atau struktur HTML lain.
- Tidak ada warna hex baru dan tidak ada warna hardcode. Semua warna dari variabel palet sesuai dev/DESIGN.md.
- Perhatikan gotcha spesifisitas CSS pada tag `<a>` di dev/RULES.md. Styling bawaan tema untuk `a:hover` dan `a:visited` tidak boleh menimpa gaya link di kartu.
- Mode gelap dan mode terang harus sama-sama benar.
- Tiga bahasa (id, en, ja) harus tampil sama dan konsisten, sesuai pengecekan di scripts/check-languages.py.
- Tampilan mobile tidak boleh rusak. Tidak ada teks terpotong dan kartu tidak melebar keluar layar.
- Tidak mengubah HOME, sub-halaman standar, halaman Developer, header, footer, dan background.

Data:
- Tidak ada perubahan struktur data, sinkron Drive, ekspor, atau impor.

Cek manual:
- Buka halaman Contact di /id/, /en/, dan /ja/ dalam mode gelap. Bandingkan dengan HOME: garis, jarak, font, dan warna link terasa satu keluarga. Tidak ada border pink.
- Cek semua kartu: nama platform tampil satu kali, termasuk LinkedIn dan Wantedly.
- Cek kartu GitHub: handle tampil utuh dan tinggi kartu sama dengan kartu lain yang sejajar.
- Ulangi di mode terang. Teks dan link tetap terbaca dan tidak ada warna bawaan tema yang muncul.
- Arahkan kursor ke link di kartu, lalu klik dan kembali. Gaya hover dan visited sama dengan link di HOME.
- Buka halaman Contact di lebar layar HP. Tidak ada teks terpotong dan tidak ada scroll samping.
- Jalankan `python scripts/check-languages.py`. Tidak ada error, dan tidak ada peringatan warna hardcode baru.

## Samakan warna latar HOME dan sub-halaman

Tujuan: Latar situs harus satu warna rata yang sama di header, HOME, dan semua sub-halaman. Sekarang ada dua masalah: HOME punya patch kotak yang sedikit lebih ungu dengan tepi tajam, dan sub-halaman terlihat lebih ungu dari header. Item ini menghilangkan patch dan menyamakan warna latar. Acuannya warna latar header dan HOME di luar patch, sesuai dev/DESIGN.md.

Tempat dan tampilan:
- Patch di HOME: ada area berbentuk kotak yang sedikit lebih ungu dengan tepi tajam, di sisi kiri bawah halaman, sekitar x 470 pada layar selebar 1264. Area itu harus hilang sehingga latar HOME rata dari ujung ke ujung dan dari atas sampai bawah, termasuk saat di-scroll.
- Sub-halaman: warna latar harus sama persis dengan latar header dan HOME. Tidak ada beda warna antara header dan area konten.
- Cakupan: HOME dan semua sub-halaman (Psychology, HR, Linguistics, About, 3E, semua portofolio tambahan, Developer, dan Contact) di /id/, /en/, dan /ja/.
- Cara mengerjakan: cari penyebabnya dulu. Periksa semua elemen yang punya latar atau gradasi di HOME dan sub-halaman (html, body, pembungkus halaman, sidebar, konten, header) dan temukan elemen yang membuat patch dan beda warna itu. Perbaiki di sumbernya, jangan menutup dengan elemen atau warna tambahan.
- Warna latar yang dipakai adalah warna latar header dan HOME di luar patch. Pakai variabel palet yang sudah dipakai di sana.

Aturan:
- Hanya CSS yang diubah. Teks dan struktur HTML tidak diubah.
- Tidak ada warna hex baru dan tidak ada warna hardcode. Semua warna dari variabel palet sesuai dev/DESIGN.md. Nilai hex hanya boleh ada di `_kanade.scss`.
- Perhatikan cara kerja `kanade-palette.css` dan `main-light.css` di dev/DESIGN.md. Perbaikan harus berlaku di mode gelap dan mode terang. Cek latar mode terang juga, jangan hanya mode gelap.
- Tiga bahasa (id, en, ja) harus tampil sama.
- Tampilan mobile tidak boleh rusak, dan tidak ada patch atau beda warna di lebar layar HP.
- Tidak mengubah teks, gaya kartu, gaya link, tombol, header, dan footer. Footer dikerjakan di sesi lain.

Data:
- Tidak ada perubahan struktur data, sinkron Drive, ekspor, atau impor.

Cek manual:
- Buka HOME di /id/ pada lebar sekitar 1264 dalam mode gelap. Scroll dari atas sampai bawah. Tidak ada patch kotak, tidak ada tepi tajam, dan latar rata.
- Buka Psychology di mode gelap. Warna latar konten sama dengan warna latar header, tidak lebih ungu.
- Ulangi dua cek di atas di mode terang.
- Buka HOME dan satu sub-halaman di /en/ dan /ja/. Hasilnya sama dengan /id/.
- Buka HOME dan satu sub-halaman di lebar layar HP. Tidak ada patch dan tidak ada beda warna.
- Jalankan `python scripts/check-languages.py`. Tidak ada error, dan tidak ada peringatan warna hardcode baru.
