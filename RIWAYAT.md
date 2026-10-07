# History Perubahan

Log perubahan web portofolio yang dikerjakan lewat Antigravity.

Aturan:
- Terbaru di atas. Satu entri = satu tugas/sesi.
- Format: nomor, judul singkat, tanggal, file, alasan.
- Jangan ubah entri lama. Kalau ada koreksi, tulis entri baru.
- Yang tidak diketahui ditulis "tidak tercatat", jangan menebak.

---

## #43 | halaman index.html dan 404.html mendukung dua tema (Sesi 4)
- Tanggal: 2026-10-07
- File: `CATATAN.md`, `RIWAYAT.md`, `_includes/masthead.html`, `index.html`
- Alasan: Mengerjakan Sesi 4. Menambahkan skrip anti-kedip dan mengadopsi variabel palet Kanade di halaman standalone `index.html` (termasuk mengganti nilai rgba dengan color-mix). Memperbarui `masthead.html` agar tombol ganti tema di `404.html` (yang mewarisi layout Minimal Mistakes) tampil dalam tiga bahasa sekaligus ("Ganti Tema / Change Theme / テーマ変更"). Halaman `404.html` secara otomatis telah mendukung dua tema berkat infrastruktur dari Sesi 2 dan 3 yang diaplikasikan pada layout Minimal Mistakes.

## #42 | tombol ganti tema dan skrip anti-kedip (Sesi 3)
- Tanggal: 2026-10-07
- File: `CATATAN.md`, `RIWAYAT.md`, `_includes/head/custom.html`, `_includes/masthead.html`
- Alasan: Mengerjakan Sesi 3. Menambahkan tombol "Ganti Tema" (dalam 3 bahasa sesuai bahasa halaman) pada bagian `masthead.html`. Elemen `<a role="button">` digunakan agar styling tombol menyatu dengan tautan navigasi dan secara otomatis menerima *focus ring* sesuai standar Sesi 1. Menyisipkan JavaScript di `_includes/head/custom.html` untuk menyimpan preferensi di `localStorage`, membaca `localStorage` (anti-kedip sebelum halaman di-render), dan mendeteksi OS default dengan `window.matchMedia` jika `localStorage` kosong. Karena Sesi 2 sudah membangun kerangka dengan `html:not([data-theme="dark"])`, penetapan atribut `data-theme` lewat JS di sesi ini sempurna meng-override fallback `@media` OS.

## #41 | perbaiki bug build GitHub Pages sass extend di Sesi 2
- Tanggal: 2026-10-07
- File: `assets/css/main-light.scss`, `assets/css/main-light-os.scss`, `_includes/head/custom.html`
- Alasan: GitHub Pages (Sass 3.7.4) gagal mem-build Sesi 2 karena error `"You may not @extend an outer selector from within @media"`. Untuk memperbaikinya tanpa menyentuh file inti Minimal Mistakes atau memakai JavaScript, struktur `main-light.scss` dipecah menjadi dua file agar SASS tidak lagi menggunakan `@media`. `main-light.scss` kini eksklusif menangani override lewat wrapper atribut `[data-theme="light"]`, sementara file baru `main-light-os.scss` menampung aturan dengan wrapper `html:not([data-theme="dark"])`. Fungsi `@media (prefers-color-scheme: light)` dipindahkan ke dalam tag `<link>` pemanggil di HTML. Dengan teknik ini, *fallback* pengaturan OS tetap bekerja 100% menggunakan CSS. Karena keterbatasan environment, hasil build akhir harus diverifikasi lewat GitHub Actions.


## #40 | fondasi palet mode terang (Sesi 2)
- Tanggal: 2026-10-07
- File: `CATATAN.md`, `RIWAYAT.md`, `_includes/head/custom.html`, `_sass/minimal-mistakes/skins/_kanade.scss`, `assets/css/kanade-palette.scss`, `assets/css/main-light.scss`
- Alasan: Mengerjakan Sesi 2 (Fondasi palet terang). Menambahkan warna terang (latar, teks, aksen, dan warn turunan SASS) ke `_kanade.scss` dengan nilai default. Membuat file `assets/css/main-light.scss` untuk mengompilasi CSS tema terang menggunakan teknik SASS wrapper (`[data-theme="light"]` dan `@media (prefers-color-scheme: light)`) agar bisa dieksekusi tanpa JavaScript. Memasukkan CSS mode terang ke dalam pemanggilan `custom.html`. Mengupdate variabel root di `kanade-palette.scss`. Mengubah aturan warna dan menambahkan tabel kontras mode terang ke `CATATAN.md`.


## #39 | audit kontras dan perbaiki fokus keyboard (Sesi 1)
- Tanggal: 2026-10-07
- File: CATATAN.md, RIWAYAT.md, _includes/head/custom.html, index.html
- Alasan: Menjalankan Sesi 1 dari rencana mode terang. Mengaudit kontras WCAG untuk warna saat ini (mode gelap) di mana seluruh elemen lulus standar kontras, dan mencatat hasilnya di CATATAN.md. Memperbaiki aksesibilitas fokus pada elemen interaktif (kartu bahasa, skip link, menu masthead, elemen summary) yang mengandalkan gaya bawaan browser dengan menambahkan ring fokus eksplisit via :focus-visible menggunakan ar(--kanade-text) agar kontras dan konsisten.

## #38 | rencana multi-sesi mode terang dan tombol ganti tema
- Tanggal: 2026-10-07
- File: `CATATAN.md`, `RIWAYAT.md`
- Alasan: Menambahkan rencana multi-sesi untuk mode terang dan tombol ganti tema ke `CATATAN.md` tepat setelah bagian "Status fitur", serta menambahkan satu baris item pada "Status fitur". Rencana ini mencakup tujuan situs statis dengan default `prefers-color-scheme` dan penyimpanan `localStorage`, kendala teknis SCSS/runtime, skrip anti-kedip, dan rincian 6 sesi pengerjaan bertahap mulai dari audit kontras, fondasi palet, tombol ganti tema, halaman standalone, easter egg Kanade, hingga pengecekan akhir. Tidak ada perubahan pada kode, CSS, atau halaman web.

## #37 | tambah navigasi Sebelumnya/Berikutnya di portofolio
- Tanggal: 2026-10-07
- File: `CATATAN.md`, `RIWAYAT.md`, `_data/portfolio-nav.yml`, `_includes/head/custom.html`, `_includes/portfolio-nav.html`, `_layouts/single.html`
- Alasan: Menambahkan tombol navigasi (Sebelumnya / Berikutnya) di semua halaman portofolio sesuai urutan dua rantai (Main dan Additional) dari daftar tunggal di `_data/portfolio-nav.yml`. Tombol ini membantu pengunjung pindah antar halaman tanpa harus kembali ke HOME. Navigasi ini diterapkan secara terpusat pada layout `single.html` menggunakan `_includes/portfolio-nav.html` khusus untuk halaman portofolio, serta gaya layout grid di `_includes/head/custom.html` yang akan menyesuaikan tampilan dengan menyusun kedua tombol berjajar atau vertikal sesuai lebar layar tanpa JavaScript dan tetap menggunakan palet warna tema Kanade.

## #36 | standar embed YouTube dan lazy image
- Tanggal: 2026-10-07
- File: `CATATAN.md`, `RIWAYAT.md`, `_includes/head/custom.html`, `_includes/lazy-image.html`, `_includes/youtube-embed.html`
- Alasan: Membuat cara standar untuk memasang video YouTube dan gambar dengan memisahkan komponen `youtube-embed.html` dan `lazy-image.html` menggunakan praktik lazy loading. Include ini mendukung atribut alt dan title untuk aksesibilitas, dengan pencegahan build `ERROR_ALT_WAJIB_DIISI.html` apabila parameter alt pada gambar kosong. Gaya CSS pembungkus ditambahkan ke `_includes/head/custom.html` dengan aspect-ratio dan border yang memanfaatkan variabel palet Kanade tanpa menambahkan warna hex hardcode. Dokumentasi cara pakai ditambahkan ke `CATATAN.md`.

## #35 | deteksi placeholder halaman kerangka
- Tanggal: 2026-10-07
- File: `CATATAN.md`, `RIWAYAT.md`, `scripts/check-languages.py`
- Alasan: menambah deteksi placeholder `[TEKS DARI MIZO]` pada halaman kerangka (`_pages/` dan `奏/`) di `scripts/check-languages.py`. Pola placeholder disimpan dalam list agar mudah ditambah nanti. Skrip akan mencetak peringatan berupa lokasi file, bahasa, pola, dan nomor baris, beserta ringkasan jumlah halaman per bahasa di akhir, tanpa mengubah exit code (tidak menggagalkan push). `CATATAN.md` diperbarui untuk mencatat status fitur dan panduan pengujian lokal.

## #34 | peringatan teks Jepang tanpa lang="ja"
- Tanggal: 2026-10-06
- File: `CATATAN.md`, `RIWAYAT.md`, `scripts/check-languages.py`
- Alasan: menambah fitur peringatan pada `scripts/check-languages.py` untuk mendeteksi teks Jepang (hiragana, katakana, kanji) yang tidak diapit elemen dengan atribut `lang="ja"` di halaman id dan en. Peringatan akan menampilkan nama file, nomor baris, dan potongan teks, namun tidak mengubah exit code atau menggagalkan push. Status fitur di `CATATAN.md` diperbarui.

## #33 | pengecekan otomatis konsistensi 3 bahasa
- Tanggal: 2026-10-06
- File: `.github/workflows/check-languages.yml`, `CATATAN.md`, `RIWAYAT.md`, `_config.yml`, `scripts/check-languages.py`
- Alasan: membuat skrip python murni `scripts/check-languages.py` untuk mengecek kelengkapan halaman (16 slug dari tabel untuk id, en, ja), kebenaran permalink di front matter, serta validitas link internal antar-halaman dan ke file aset. Skrip tersebut dijalankan otomatis menggunakan GitHub Action di `.github/workflows/check-languages.yml` setiap ada push atau pull request ke branch master. Direktori `scripts` ditambahkan ke `exclude` di `_config.yml` agar tidak ter-publish oleh Jekyll, tanpa mengubah daftar pengecualian lainnya. Status fitur dan panduan pengujian lokal juga diperbarui di `CATATAN.md`.

## #32 | ubah entri LINE di Contact jadi tautan (id, en, ja)
- Tanggal: 2026-10-04
- File: `RIWAYAT.md`, `_pages/en-contact.md`, `_pages/id-contact.md`, `_pages/ja-contact.md`
- Alasan: mengubah elemen entri LINE di halaman Contact (id, en, ja) dari elemen div menjadi tombol tautan (tag a dengan class contact-btn) yang mengarah ke https://line.me/ti/p/~mizoarkatamarenaldy. Teks yang ditampilkan tetap mizoarkatamarenaldy, serta tautan dibuka di tab baru menggunakan target="_blank" dan rel="noopener noreferrer".

## #31 | isi halaman Contact (id, en, ja)
- Tanggal: 2026-10-04
- File: `CATATAN.md`, `RIWAYAT.md`, `_pages/en-contact.md`, `_pages/id-contact.md`, `_pages/ja-contact.md`
- Alasan: mengisi halaman Contact dengan daftar akun profesional, pesan langsung, sosial, dan YouTube di tiga bahasa (id, en, ja). Layout dibuat responsif (CSS flex/grid inline pada markdown) dengan tombol yang menampilkan nama platform di kiri dan teks tampilan di kanan. Warna tombol dan efek hover memakai variabel palet tema Kanade tanpa ada hardcode hex. Link eksternal dibuka di tab baru dengan atribut `noopener noreferrer`. Mengubah status fitur Contact menjadi [x] di file CATATAN.md.

## #30 | tambah structured data JSON-LD Person di HOME
- Tanggal: 2026-10-04
- File: `CATATAN.md`, `RIWAYAT.md`, `_includes/head/custom.html`, `_includes/head/jsonld-person.html`
- Alasan: menambahkan structured data JSON-LD dengan tipe Person yang ditempatkan secara terpusat pada file `_includes/head/jsonld-person.html` dan dipanggil di `_includes/head/custom.html`. JSON-LD ini hanya dimunculkan di halaman HOME untuk tiga bahasa (id, en, ja). Informasi yang dimasukkan terbatas pada nama panggung ("Mizo Arkatama Renaldy" dan "Mizo AR"), link gambar og-image.png, deskripsi dari masing-masing bahasa, bidang pengetahuan (knowsAbout), serta profil media sosial (sameAs) yang sejauh ini tersedia (Medium dan Substack). Sesuai aturan privasi, data pribadi seperti nama asli atau kampus tidak disertakan, serta referensi mengenai easter egg Kanade sengaja dikecualikan dari deskripsi di JSON-LD.

## #29 | tambah sitemap dan robots.txt
- Tanggal: 2026-10-04
- File: `CATATAN.md`, `RIWAYAT.md`, `robots.txt`, `奏/en/index.html`, `奏/id/index.html`, `奏/ja/index.html`
- Alasan: menambahkan sitemap.xml (dibantu plugin jekyll-sitemap yang sudah aktif) dan robots.txt di root. URL easter egg Kanade pada versi id, en, ja ditambahkan front matter `sitemap: false` untuk disembunyikan dari sitemap. robots.txt sengaja tidak memuat aturan Disallow untuk mencegah pembocoran URL rahasia.

## #28 | pasang favicon aksen Kanade di semua halaman
- Tanggal: 2026-10-04
- File: `_includes/head/custom.html`, `assets/images/apple-touch-icon.png`, `assets/images/favicon-32.png`, `assets/images/favicon.ico`, `assets/images/favicon.svg`, `CATATAN.md`, `index.html`, `RIWAYAT.md`, `奏/en/index.html`, `奏/id/index.html`, `奏/index.html`, `奏/ja/index.html`
- Alasan: memasang favicon (ikon tab browser) beraksen Kanade di semua halaman situs. Empat file gambar favicon (favicon.svg, favicon-32.png, favicon.ico, apple-touch-icon.png) di folder assets/images/ dicatat sebagai pengecualian dari aturan larangan hex. Tag link dipasang secara terpusat di `_includes/head/custom.html` menggunakan relative_url (otomatis dimuat di /id/main/, /en/main/, /ja/main/, seluruh sub-halaman portofolio/3E/about/contact, dan 404.html via layout single). Untuk halaman-halaman HTML mandiri yang tidak memakai layout Minimal Mistakes (`index.html` pemilih bahasa dan seluruh halaman easter egg `奏/`), keempat tag link dipasang langsung pada elemen `<head>`. File /favicon.ico di root situs diperiksa dan tidak ditemukan, sehingga dilaporkan ke pemilik tanpa disalin sepihak sesuai instruksi.

## #27 | pasang gambar preview link og:image
- Tanggal: 2026-10-04
- File: `_config.yml`, `_includes/seo.html`, `assets/images/og-image.png`, `CATATAN.md`, `RIWAYAT.md`
- Alasan: memasang preview gambar (Open Graph dan Twitter Card) untuk memunculkan kartu saat link dibagikan di WhatsApp, Discord, LinkedIn, dll. Konfigurasi dilakukan terpusat di `_config.yml` (menetapkan `url` kanonikal dan default `og_image`) dan `_includes/seo.html` (memastikan `og:image` menggunakan URL absolut `https://mizoarkatamarenaldy.github.io/assets/images/og-image.png`, menambahkan atribut `og:image:width` 1200, `og:image:height` 630, `og:image:type` image/png, deskripsi `og:image:alt` yang mengikuti bahasa halaman: id, en, ja, serta `twitter:card` berupa summary_large_image dan `twitter:image`). Nilai `og:title` dan `og:description` tetap mengikuti bahasa halaman tanpa diubah. File gambar biner `assets/images/og-image.png` (1200x630 PNG) dicatat sebagai pengecualian dari aturan larangan hex di `CATATAN.md`. Halaman easter egg Kanade tidak diubah karena merupakan file HTML statis murni tanpa include layout Jekyll.

## #26 | perbaiki kanji easter egg tidak muncul saat hover
- Tanggal: 2026-10-04
- File: `_includes/head/custom.html`, `_pages/id-main.md`, `_pages/en-main.md`, `_pages/ja-main.md`, `CATATAN.md`, `RIWAYAT.md`
- Alasan: Kanji easter egg 奏 di HOME sebelumnya mungkin tidak muncul saat dihover karena masalah spesifisitas CSS (kalah dari aturan link bawaan tema Minimal Mistakes) atau karena `opacity: 0.5` yang membuatnya terlalu redup di atas background gelap. Solusinya, atribut CSS di `.kanade-trigger` (terutama `color` dan `z-index`) ditambahkan `!important` untuk memastikan tidak ada override, mengubah opacity saat hover menjadi `1` agar terlihat sangat jelas, dan menghapus `tabindex="-1"` pada elemen HTML di ketiga file HOME agar kanji bisa diakses (fokus) menggunakan keyboard (Tab).

## #25 | tombol Kembali ke HOME di semua sub-halaman
- Tanggal: 2026-10-04
- File: `_includes/back-to-home.html`, `_layouts/single.html`, `CATATAN.md`, `RIWAYAT.md`
- Alasan: Menambahkan tombol navigasi "Kembali ke HOME" di seluruh sub-halaman (portofolio, about, contact) untuk ketiga bahasa (id, en, ja). Tombol dipasang secara terpusat lewat satu file include baru `back-to-home.html` pada `single.html` tanpa perlu mengubah puluhan file konten secara manual. Desain menggunakan class `home-btn` dan `.home-links` bawaan sehingga otomatis responsif dan serasi dengan palet tema Kanade tanpa JavaScript.

## #24 | exclude catatan internal di _config.yml
- Tanggal: 2026-10-04
- File: `CATATAN.md`, `RIWAYAT.md`, `_config.yml`
- Alasan: menambahkan `RIWAYAT.md` dan `RIWAYAT_ARSIP*.md` ke daftar `exclude` di `_config.yml` (menggabungkannya dengan `CATATAN.md` yang sudah ada) agar file catatan internal tidak ter-publish sebagai halaman publik di situs; memastikan kunci `include` (.well-known) tidak bentrok; serta menambahkan poin di bagian "Gotcha (jangan diulang)" pada `CATATAN.md` agar `CATATAN.md`, `RIWAYAT.md`, dan `RIWAYAT_ARSIP*.md` tidak dihapus dari `exclude`.

## #23 | ganti nama HISTORY ke RIWAYAT + aturan arsip
- Tanggal: 2026-10-04
- File: `CATATAN.md`, `RIWAYAT.md`
- Alasan: mengubah nama HISTORY.md menjadi RIWAYAT.md dengan git mv; memperbarui semua penyebutan HISTORY.md di CATATAN.md menjadi RIWAYAT.md; menambahkan aturan baca RIWAYAT.md (hanya 5 entri teratas di awal sesi) dan aturan arsip RIWAYAT.md (arsip ke RIWAYAT_ARSIP{n}.md jika sudah mencapai 50 entri) di CATATAN.md. Tidak ditemukan penyebutan HISTORY di file lain di luar entri lama.

## #22 | tambah aturan branch master di CATATAN.md
- Tanggal: 2026-10-04
- File: `CATATAN.md`, `HISTORY.md`
- Alasan: menambahkan aturan eksplisit mengenai branch pada CATATAN.md agar agent selalu memeriksa git branch --show-current di awal sesi dan memastikan berada di branch master. Jika bukan master, atau jika selama sesi muncul branch atau worktree baru otomatis, agent wajib berhenti dan melapor ke pemilik serta tidak melakukan commit/push. Semua commit dan push dilakukan di master saja. Menambahkan poin gotcha bahwa branch utama repo ini adalah master (bukan main) dan branch tambahan sebelumnya (hide-kanade-seo) dibuat tidak sengaja serta sudah dihapus. Langkah 1 sampai 7 dan bagian lain di CATATAN.md tidak diubah.
- Catatan: dicek manual. Langkah 1 sampai 7 masih utuh dan nomornya tidak berubah. git status --short hanya menampilkan CATATAN.md dan HISTORY.md. git branch --show-current setelah push masih menampilkan master.

## #21 | sembunyikan easter egg Kanade dari mesin pencari
- Tanggal: 2026-10-04
- File: `HISTORY.md`, `_config.yml`
- Alasan: menyembunyikan halaman easter egg Kanade dari mesin pencari. Telah diverifikasi bahwa keempat halaman HTML murni (`奏/index.html`, `奏/id/index.html`, `奏/en/index.html`, `奏/ja/index.html`) sudah memiliki tag `<meta name="robots" content="noindex, nofollow">`. Karena plugin `jekyll-sitemap` aktif, ditambahkan entri `defaults` pada `_config.yml` dengan scope path `奏` dan `values: sitemap: false` untuk mengeluarkan halaman-halaman tersebut dari sitemap tanpa harus menambahkan front matter pada file HTML murni.


## #20 | judul tab, hreflang, dan deskripsi per bahasa
- Tanggal: 2026-10-03
- File: `CATATAN.md`, `HISTORY.md`, `_includes/seo.html`, `_layouts/default.html`, `_pages/en-main.md`, `_pages/id-main.md`, `_pages/ja-main.md`
- Alasan: menyesuaikan meta tag SEO agar mendukung situs multibahasa. Tag `<title>` di tab browser sekarang mengambil dari `page.title` halaman ditambah `site.name` jika ada, dan fallback ke logika lama untuk halaman tanpa prefix bahasa. Menambahkan atribut `lang` pada `<html>` yang menyesuaikan prefix bahasa halaman (`page.lang` dengan fallback URL) dan fallback ke nilai locale untuk halaman root. Menambahkan empat tag `<link rel="alternate" hreflang="...">` (id, en, ja, x-default) pada setiap halaman berprefix untuk memudahkan mesin pencari mengindeks versi setara, dengan mengecualikan halaman kanji 奏, root, dan 404. Terakhir, menambahkan front matter `description` di tiga halaman HOME (`-main.md`) yang berfungsi sebagai fallback `seo_description` untuk sub-halaman di masing-masing bahasa jika tidak memiliki deskripsi sendiri.

## #19 | aturan commit dan push mandiri untuk agent di CATATAN.md
- Tanggal: 2026-10-03
- File: `CATATAN.md`, `HISTORY.md`
- Alasan: memperbarui aturan di bagian "Aturan untuk agent" pada CATATAN.md agar agent melakukan commit dan push secara mandiri menggunakan alur 7 langkah (verifikasi git status, pembaruan HISTORY.md, staging per nama file tanpa git add -A atau ., commit lengkap dengan trailer Co-authored-by Claude dan Gemini, push ke branch aktif tanpa force push atau perubahan branch/config, penghentian dan pelaporan saat error, serta pelaporan file yang diubah dan hash commit di akhir tugas). Menghapus kalimat lama yang bertentangan terkait verifikasi lama, larangan commit dan push bagi agent, serta saran pesan commit untuk pemilik.

## #18 | hapus nama situs dari teks footer
- Tanggal: 2026-10-03
- File: `HISTORY.md`, `_includes/footer.html`
- Alasan: menghapus nama situs (dan tautan site.copyright/site.title) dari teks copyright di footer sehingga teks hanya menampilkan rentang tahun hak cipta diikuti dengan teks "Powered by Jekyll & Minimal Mistakes" ("© 2013 - 2026. Powered by Jekyll & Minimal Mistakes."). Rentang tahun dan cara perhitungannya tidak diubah, tautan Jekyll dan Minimal Mistakes dipertahankan, tanda baca titik diletakkan tepat setelah tahun tanpa spasi berlebih, teks footer tetap sama di semua bahasa, serta tidak ada penambahan CSS atau warna hardcode.

## #17 | judul situs masthead multibahasa (id, en, ja)
- Tanggal: 2026-10-03
- File: `HISTORY.md`, `_includes/masthead.html`
- Alasan: menyesuaikan teks judul situs yang tampil di masthead (`site-title` dan alt `site-logo`) agar dinamis mengikuti bahasa halaman (`page.lang` dengan fallback deteksi prefix URL: `Beranda` untuk `id`, `Home` untuk `en`, `ホーム` untuk `ja`). Halaman tanpa prefix bahasa (seperti `404.html` dan `index.html`) tetap memakai fallback `site.masthead_title | default: site.title` ("Main Page") sehingga tidak kosong. Nilai `title` di `_config.yml` tidak diubah, tidak ada penambahan CSS atau warna hardcode, masthead tetap dipanggil via `include` (bukan `include_cached`), dan navigasi ganti bahasa tidak terganggu.
- Catatan: render belum diverifikasi lokal (Jekyll tidak terpasang). Tag `<title>` di tab browser (`_includes/seo.html`) juga menggunakan `site.title` dan dilaporkan ke pemilik tanpa diubah.

## #16 | buat halaman 404 tiga bahasa (id, en, ja)
- Tanggal: 2026-10-03
- File: `404.html`, `CATATAN.md`, `HISTORY.md`
- Alasan: membuat halaman 404 di root (`404.html`) berisi pesan judul dan satu kalimat singkat "halaman tidak ditemukan" dalam tiga bahasa (Indonesia, English, 日本語) secara berurutan, tanpa JavaScript dan tanpa redirect otomatis. Dilengkapi tombol link ke `/?pilih` dengan label tiga bahasa menggunakan class yang sudah ada (`ul.home-links` > `a.home-btn`) dan palet Kanade via layout Minimal Mistakes (`layout: single`). Tombol ganti bahasa di masthead jatuh ke fallback `/?pilih` via `change_lang_text`. Struktur teknis dan status fitur di CATATAN.md diperbarui.
- Catatan: render belum diverifikasi lokal (Jekyll tidak terpasang).

## #15 | perbaiki tombol ganti bahasa (membawa ke halaman setara)
- Tanggal: 2026-10-03
- File: `CATATAN.md`, `HISTORY.md`, `_includes/masthead.html`
- Alasan: mengubah tombol ganti bahasa di masthead agar dinamis menampilkan link ke dua bahasa lainnya (bukan ke `/?pilih`) untuk halaman yang sedang aktif. Tujuan link dihitung dengan Liquid (`replace_first`) dengan mengganti prefix bahasa di `page.url` (misalnya `/id/portfolio/hr/` menjadi `/en/portfolio/hr/`). Jika halaman tidak memiliki prefix `/id/`, `/en/`, atau `/ja/`, tombol fallback ke `/?pilih`. Label memakai nama asli tiap bahasa. Paragraf usang di `CATATAN.md` dihapus dan status fitur diperbarui.
- Catatan: dicek manual permalink di `_pages/` sudah setara antarbahasa. Render belum diverifikasi lokal (Jekyll tidak terpasang).

## #14 | aturan co-author commit
- Tanggal: 2026-10-03
- File: `CATATAN.md`, `HISTORY.md`
- Alasan: menambahkan satu aturan baru di bagian "Aturan untuk agent" pada CATATAN.md agar agent menuliskan saran pesan commit lengkap beserta dua baris trailer Co-authored-by (Claude dan Gemini (Antigravity)) yang dipisah satu baris kosong di akhir tugas, serta menegaskan bahwa agent tidak menjalankan git commit.

## #13 | link Medium dan Substack di halaman Writing (id, en, ja)
- Tanggal: 2026-10-03
- File: `HISTORY.md`, `_pages/en-portfolio-writing.md`, `_pages/id-portfolio-writing.md`, `_pages/ja-portfolio-writing.md`
- Alasan: menambahkan dua tombol link ke halaman profil publik Medium dan Substack pada halaman portofolio Writing di tiga bahasa (id, en, ja) tepat di bawah teks placeholder [TEKS DARI MIZO]. Menggunakan struktur dan class yang sama dengan HOME (`ul.home-links` > `a.home-btn`), urutan Medium lalu Substack, dibuka di tab baru (`target="_blank" rel="noopener noreferrer"`), serta memanfaatkan styling yang sudah ada di `_includes/head/custom.html` tanpa penambahan CSS atau style inline.

## #12 | siapkan verifikasi domain Discord lewat HTTPS
- Tanggal: 2026-10-03
- File: `CATATAN.md`, `HISTORY.md`, `_config.yml`, `.well-known/discord`
- Alasan: menyiapkan verifikasi domain Discord lewat HTTPS dengan membuat file `.well-known/discord` berisi satu baris kode verifikasi `dh=11a13d75cc51e5695ff63a9f2cb6af048da6da90` tanpa baris kosong tambahan, menambahkan `.well-known` ke daftar `include:` di `_config.yml` agar tidak diabaikan Jekyll, dan menambahkan catatan di bagian Gotcha pada `CATATAN.md` mengenai verifikasi Discord dan larangan membuat file `.nojekyll`.

## #11 | perbarui acuan slug URL di CATATAN.md
- Tanggal: 2026-10-03
- File: `CATATAN.md`, `HISTORY.md`
- Alasan: memperbarui baris usang di bagian "Aturan mapping" pada CATATAN.md yang sebelumnya menyatakan bahwa slug URL tiap sub-halaman belum ditentukan, menjadi menunjuk ke bagian "Slug URL" sebagai sumber yang berlaku. Bagian lain tidak diubah.

## #10 | tombol link HOME ke semua sub-halaman (id, en, ja)
- Tanggal: 2026-10-03
- File: `CATATAN.md`, `HISTORY.md`, `_includes/head/custom.html`, `_pages/en-main.md`, `_pages/id-main.md`, `_pages/ja-main.md`
- Alasan: menghubungkan HOME ke halaman di mapping. Motto 3E sekarang ke `/{lang}/3e/` (tooltip dan efek hover tidak diubah). Isi dua `<details markdown="1">` diganti daftar HTML berisi tombol link (`ul.home-links` > `a.home-btn`, tanpa JavaScript): 3 Main Portfolio + 9 Additional Portfolio, ditambah tombol About dan Contact di bawahnya (tugas opsional). Teks tombol mengikuti bahasa halaman (en "Japanese Language" jadi "Japanese", ja "人事（HR）" jadi "HR", sesuai permintaan). Urutan dan jumlah tombol sama di tiga bahasa (15 href per halaman termasuk 3E). CSS tombol hanya memakai `--kanade-bg`, `--kanade-text`, `--kanade-accent`; hover dibatasi `@media (hover: hover)`, ada `:active` untuk layar sentuh, `:focus-visible` dengan outline, tinggi minimum 2.75rem. Dua komentar lama ("href sementara" dan "Link sub-halaman dikosongkan") dihapus karena sudah tidak berlaku. Status fitur ditambah satu baris. Salam pembuka dan [TEKS DARI MIZO] tidak diubah.
- Catatan: dicek manual. Semua 45 href cocok dengan permalink di `_pages/`, tidak ada link ke halaman yang belum ada. Render belum diverifikasi lokal (Jekyll tidak terpasang).

## #9 | kerangka 15 sub-halaman (id, en, ja)
- Tanggal: 2026-10-03
- File: `CATATAN.md`, `HISTORY.md`,
  `_pages/en-3e.md`, `_pages/en-about.md`, `_pages/en-contact.md`, `_pages/en-portfolio-coding.md`, `_pages/en-portfolio-cooking.md`, `_pages/en-portfolio-data-analysis.md`, `_pages/en-portfolio-design.md`, `_pages/en-portfolio-hr.md`, `_pages/en-portfolio-illustration.md`, `_pages/en-portfolio-japanese.md`, `_pages/en-portfolio-music.md`, `_pages/en-portfolio-psychology.md`, `_pages/en-portfolio-second-brain.md`, `_pages/en-portfolio-sport.md`, `_pages/en-portfolio-writing.md`,
  `_pages/id-3e.md`, `_pages/id-about.md`, `_pages/id-contact.md`, `_pages/id-portfolio-coding.md`, `_pages/id-portfolio-cooking.md`, `_pages/id-portfolio-data-analysis.md`, `_pages/id-portfolio-design.md`, `_pages/id-portfolio-hr.md`, `_pages/id-portfolio-illustration.md`, `_pages/id-portfolio-japanese.md`, `_pages/id-portfolio-music.md`, `_pages/id-portfolio-psychology.md`, `_pages/id-portfolio-second-brain.md`, `_pages/id-portfolio-sport.md`, `_pages/id-portfolio-writing.md`,
  `_pages/ja-3e.md`, `_pages/ja-about.md`, `_pages/ja-contact.md`, `_pages/ja-portfolio-coding.md`, `_pages/ja-portfolio-cooking.md`, `_pages/ja-portfolio-data-analysis.md`, `_pages/ja-portfolio-design.md`, `_pages/ja-portfolio-hr.md`, `_pages/ja-portfolio-illustration.md`, `_pages/ja-portfolio-japanese.md`, `_pages/ja-portfolio-music.md`, `_pages/ja-portfolio-psychology.md`, `_pages/ja-portfolio-second-brain.md`, `_pages/ja-portfolio-sport.md`, `_pages/ja-portfolio-writing.md`
- Alasan: merealisasikan kerangka "Mapping web": 15 halaman (3E, About, Contact, 3 Main Portfolio, 9 Additional Portfolio) x 3 bahasa = 45 file. Front matter meniru halaman main (`layout: single`, `lang`, `change_lang_text`), permalink sesuai slug baru, title dalam bahasa halaman; body hanya `[TEKS DARI MIZO]`. Slug dicatat di bagian baru "Slug URL" di CATATAN.md, Status fitur ditandai [/]. HOME, easter egg, dan halaman pilih bahasa tidak disentuh; belum ada link dari HOME.
- Catatan: Jekyll tidak terpasang, dicek manual (45 file baru, tidak ada permalink ganda, front matter valid, UTF-8 tanpa BOM). Tombol ganti bahasa belum membawa ke halaman setara (selalu ke `/?pilih` lalu ke `/{lang}/main/`); dilaporkan ke pemilik, tidak diperbaiki.

## #8 | isi HOME (id, en, ja)
- Tanggal: 2026-10-03
- File: `CATATAN.md`, `HISTORY.md`, `_includes/head/custom.html`, `_pages/en-main.md`, `_pages/id-main.md`, `_pages/ja-main.md`
- Alasan: mengisi HOME di tiga bahasa dengan isi yang sama: nama lengkap + ringkasan (placeholder [TEKS DARI MIZO]), motto 3E sebagai link (href sementara `#`, ada tooltip `title` dan perubahan warna/garis bawah + panah saat hover), serta dua bagian buka-tutup `<details markdown="1">` (Main Portfolio 3 item, Additional Portfolio 9 item, belum ada link karena slug belum ditentukan). CSS baru di `_includes/head/custom.html` hanya memakai `--kanade-text` dan `--kanade-accent`. Salam pembuka tidak diubah.
- Catatan: render belum diverifikasi lokal (Ruby/Jekyll tidak terpasang di mesin agent). Cek tampilan setelah push.

## #7 | perbaiki aturan verifikasi file
- Tanggal: 2026-10-03
- File: `CATATAN.md`, `HISTORY.md`
- Alasan: mengganti aturan verifikasi daftar file dari `git show` menjadi `git status --short` di CATATAN.md karena commit dan push dikerjakan oleh pemilik (belum ada commit saat agent selesai).

## #6 | kerangka easter egg Kanade
- Tanggal: 2026-09-21
- File: `奏/index.html`, `奏/id/index.html`, `奏/en/index.html`, `奏/ja/index.html`, `_pages/id-main.md`, `_pages/en-main.md`, `_pages/ja-main.md`, `CATATAN.md`
- Alasan: kerangka halaman rahasia easter egg Kanade — URL berkanji 奏, 3 bahasa (id/en/ja), redirect otomatis berdasarkan bahasa browser, noscript fallback. Kanji 奏 ditaruh di pojok kanan bawah halaman home (position: fixed), warna menyatu dengan background, muncul samar saat hover. Semua teks konten masih placeholder [TEKS DARI MIZO].
- Catatan: file list belum diverifikasi dengan `git show --name-only` (belum di-commit). Verifikasi setelah push.

## #5 | buat kanade-palette.scss + koreksi #4
- Tanggal: 2026-09-21
- File: `assets/css/kanade-palette.scss`, `_includes/head/custom.html`, `CATATAN.md`
- Alasan: `kanade-palette.css` di entri #4 ternyata tidak pernah dibuat (tidak ada di commit `a73609f6`). Dibuat sekarang sebagai SCSS dengan front matter Jekyll yang mengimport `_kanade.scss` dan mengekspornya sebagai CSS custom properties (`:root { --kanade-bg; --kanade-text; --kanade-accent }`), sehingga warna tidak ditulis dua kali.
- Catatan koreksi #4: entri #4 mencantumkan `assets/css/kanade-palette.css` sebagai file yang dibuat, padahal tidak ada di commit tersebut. Daftar file di #4 tidak akurat; entri #4 tidak diubah sesuai aturan.

## #4 | add kanade theme
- Tanggal: tidak tercatat
- File: `_sass/minimal-mistakes/skins/_kanade.scss`, `assets/css/kanade-palette.css`, `_config.yml`
- Alasan: warna theme memakai palet Kanade (background `#121016`, teks `#EDEAF0`, aksen `#BB6588`)
- Catatan: skin diaktifkan lewat `minimal_mistakes_skin: "kanade"`. Warna hardcode dilarang, pakai variabel palet.

## #3 | add name and desc
- Tanggal: tidak tercatat
- File: `_config.yml`
- Alasan: menambah nama (nama panggung) dan description situs
- Catatan: description ditulis dalam English, kalimat belum final.

## #2 | fix feed
- Tanggal: tidak tercatat
- File: tidak tercatat (footer)
- Alasan: blog tidak dipakai, link Feed di footer dihapus

## #1 | fix ganti bahasa
- Tanggal: tidak tercatat
- File: `_layouts/default.html`
- Alasan: tombol "ganti bahasa" selalu berbahasa Inggris
- Catatan: `include_cached` untuk masthead diganti `include`, karena teksnya beda per bahasa.
