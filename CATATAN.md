# Catatan Proyek: Web Portofolio

## Ringkasan
Situs portofolio pribadi di GitHub Pages, fork tema Jekyll Minimal Mistakes.
Static saja (tanpa backend). Tema tidak akan diupdate dari upstream, boleh edit file mana pun.

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
| Main Portfolio: Bahasa Jepang | `/{lang}/portfolio/japanese/` |
| Additional: Coding | `/{lang}/portfolio/coding/` |
| Additional: Data Analysis | `/{lang}/portfolio/data-analysis/` |
| Additional: Design | `/{lang}/portfolio/design/` |
| Additional: Illustration | `/{lang}/portfolio/illustration/` |
| Additional: Writing | `/{lang}/portfolio/writing/` |
| Additional: Music | `/{lang}/portfolio/music/` |
| Additional: Second Brain | `/{lang}/portfolio/second-brain/` |
| Additional: Sport | `/{lang}/portfolio/sport/` |
| Additional: Cooking | `/{lang}/portfolio/cooking/` |



## Keputusan
- Bahasa: Indonesia, English, Jepang
- Halaman pilih bahasa tetap bisa dibuka manual lewat /?pilih
- Salam pembuka tiap halaman ditulis manual oleh pemilik, jangan diubah agent

## Gotcha (jangan diulang)
- Jangan pakai include_cached untuk masthead, karena teksnya beda per bahasa
  (dulu bikin tombol "ganti bahasa" selalu berbahasa Inggris).
- Verifikasi Discord memakai `.well-known/discord` dengan `include: [".well-known"]` di _config.yml, dan jangan pernah menambah .nojekyll karena situs ini butuh Jekyll.
- Branch utama repo ini adalah master, bukan main, dan branch tambahan sebelumnya (hide-kanade-seo) dibuat tidak sengaja serta sudah dihapus.
- CATATAN.md, RIWAYAT.md, dan RIWAYAT_ARSIP*.md harus tetap ada di exclude di _config.yml supaya tidak ter-publish di situs. Jangan hapus dari exclude.
- Hati-hati dengan spesifisitas CSS pada tag `<a>` (link) seperti untuk efek hover atau visited. Tema Minimal Mistakes memiliki styling bawaan (`a:hover`, `a:visited`, dll.) yang bisa menimpa class custom. Gunakan `!important` atau selector yang sangat spesifik jika elemen custom (seperti pemicu easter egg) tidak bereaksi.
- `robots.txt` tidak boleh memuat `Disallow` untuk URL easter egg karena robots.txt bersifat publik dan justru akan membocorkan URL-nya.
- JSON-LD Person tidak boleh memuat nama asli, kampus, atau data pribadi lain.

## Status fitur
- [x] Halaman pilih bahasa
- [x] Halaman tujuan per bahasa
- [x] Tombol ganti bahasa (dinamis membawa ke halaman setara)
- [x] Redirect otomatis sesuai bahasa browser
- [x] Isi HOME (ringkasan diri, motto 3E sebagai link, dua bagian buka-tutup)
- [x] Link dari HOME ke semua sub-halaman (3E, 12 portofolio, About, Contact) lewat tombol
- [/] Halaman 3E — kerangka selesai, isi menunggu Mizo
- [/] Halaman About (latar belakang, pengalaman hidup, CV) — kerangka selesai, isi menunggu Mizo
- [x] Halaman Contact — kerangka selesai, isi menunggu Mizo
- [/] Halaman Main Portfolio (Psikologi, HR, Bahasa Jepang) — kerangka selesai, isi menunggu Mizo
- [/] Halaman Additional Portfolio (9 halaman) — kerangka selesai, isi menunggu Mizo
- [/] Easter egg Kanade (3 bahasa) — kerangka selesai, teks masih [TEKS DARI MIZO]
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
- [ ] Mode terang dan tombol ganti tema (rencana multi-sesi, lihat bagian "Rencana: Mode Terang")

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
- [ ] Sesi 5: Easter egg Kanade mendukung dua tema (kanji 奏 tetap menyatu dengan background di keduanya).
- [ ] Sesi 6: Pengecekan akhir. Perbarui `scripts/check-languages.py` agar ikut memeriksa warna hardcode dan teks tombol tiga bahasa. Cek semua halaman x 3 bahasa x 2 tema. Pastikan kontras lolos.



### Hasil Audit Sesi 1

**Tabel Kontras Pasangan Warna (Mode Gelap saat ini)**

| Pasangan | Warna Depan | Warna Latar | Rasio Kontras | Target WCAG | Status |
|---|---|---|---|---|---|
| Teks utama di background | #EDEAF0 (Teks) | #121016 (Bg) | 15.86:1 | 4.5:1 | Lulus |
| Teks redup/sekunder di background | #F1EEF3 (Muted) | #121016 (Bg) | 16.43:1 | 4.5:1 | Lulus |
| Aksen di background | #BB6588 (Primary) | #121016 (Bg) | 4.80:1 | 4.5:1 | Lulus |
| Link normal di background | #C984A0 (Link) | #121016 (Bg) | 6.56:1 | 4.5:1 | Lulus |
| Link hover di background | #D6A3B8 (Link H) | #121016 (Bg) | 8.81:1 | 4.5:1 | Lulus |
| Link visited di background | #AB7088 (Link V) | #121016 (Bg) | 4.86:1 | 4.5:1 | Lulus |
| Teks tombol normal (contact-btn dll) | #EDEAF0 (Teks) | #121016 (Bg) | 15.86:1 | 4.5:1 | Lulus |
| Teks tombol hover (contact-btn dll) | #121016 (Bg) | #BB6588 (Primary)| 4.80:1 | 4.5:1 | Lulus |
| Ring fokus di background | #EDEAF0 (Teks) | #121016 (Bg) | 15.86:1 | 3:1 | Lulus |
| Ring fokus di warna tombol (hover state) | #EDEAF0 (Teks) | #BB6588 (Primary)| 3.95:1 | 3:1 | Lulus |

*Catatan: Semua pasangan kontras di mode gelap lulus standar WCAG. Kegagalan kontras yang diteruskan ke Sesi 2: **NIHIL (tidak ada)**.*

**Tabel Kontras Pasangan Warna (Mode Terang)**

| Pasangan | Warna Depan | Warna Latar | Rasio Kontras | Target WCAG | Status |
|---|---|---|---|---|---|
| Teks utama di background | #121016 (Teks) | #FAFAFC (Bg) | 18.13:1 | 4.5:1 | Lulus |
| Teks redup/sekunder di background | #413F44 (Muted) | #FAFAFC (Bg) | 9.98:1 | 4.5:1 | Lulus |
| Aksen di background | #A85A7A (Primary) | #FAFAFC (Bg) | 4.57:1 | 4.5:1 | Lulus |
| Link normal di background | #864861 (Link) | #FAFAFC (Bg) | 6.47:1 | 4.5:1 | Lulus |
| Link hover di background | #643648 (Link H) | #FAFAFC (Bg) | 9.31:1 | 4.5:1 | Lulus |
| Link visited di background | #986378 (Link V) | #FAFAFC (Bg) | 4.59:1 | 4.5:1 | Lulus |
| Teks tombol normal | #121016 (Teks) | #FAFAFC (Bg) | 18.13:1 | 4.5:1 | Lulus |
| Teks tombol hover | #FAFAFC (Bg) | #A85A7A (Primary)| 4.57:1 | 4.5:1 | Lulus |
| Ring fokus di background | #121016 (Teks) | #FAFAFC (Bg) | 18.13:1 | 3:1 | Lulus |
| Ring fokus di warna tombol (hover state) | #121016 (Teks) | #A85A7A (Primary)| 3.97:1 | 3:1 | Lulus |

**Daftar Audit Elemen Fokus & Perbaikan:**
1. **index.html (kartu bahasa)**: Tidak ada ring fokus yang terlihat.
   *Perbaikan*: Ditambahkan pseudoclass :focus-visible di index.html dengan outline: 2px solid var(--kanade-text) beserta tautan kanade-palette.css.
2. **Skip link, menu masthead, tombol ganti bahasa, link motto 3E**: Menggunakan outline bawaan browser yang kontrasnya tidak konsisten atau kurang optimal di layar gelap.
   *Perbaikan*: Ditambahkan rule CSS global di _includes/head/custom.html untuk memaksakan outline: 2px solid var(--kanade-text) agar ring selalu terlihat jelas dan konsisten dengan kontras tinggi (15.86:1).
3. **<summary> di bagian buka-tutup**: Outline kurang terlihat.
   *Perbaikan*: Tercakup dalam perbaikan CSS global di atas.
4. **home-btn, tombol Sebelumnya/Berikutnya, contact-btn**: Sudah memiliki desain ring fokus eksplisit dengan ar(--kanade-text) (kontras sangat jelas).
   *Perbaikan*: Tidak ada, dibiarkan seperti adanya (dikecualikan dari aturan CSS global agar tidak tumpang tindih).
5. **Pemicu easter egg Kanade (.kanade-trigger)**: Sesuai instruksi, pemicu ini sengaja dibuat sembunyi dan dilarang diubah. Outline sudah diatur 
one, namun ketika menerima fokus (hover/focus-visible), warna teks berubah menjadi #BB6588.
   *Perbaikan*: Tidak diubah tampilannya, warna teks #BB6588 memiliki kontras 4.80:1 terhadap latar #121016 sehingga masih terbaca dan lulus WCAG (meskipun sengaja dibuat obscure).

Aturan untuk sesi-sesi ini: kerjakan satu sesi satu nomor, centang nomor yang selesai di `CATATAN.md` pada akhir sesinya, dan jangan mengerjakan sesi berikutnya.

## Pengujian Lokal
- Untuk mengecek konsistensi bahasa, permalink, dan link rusak secara lokal, jalankan `python scripts/check-languages.py` dari root repo. Skrip akan memberikan rincian file yang bermasalah dan mengembalikan exit code 1 jika ada error. Skrip juga akan mencetak peringatan jika menemukan teks Jepang tanpa atribut lang="ja" di halaman id dan en. Skrip juga mencetak peringatan untuk placeholder yang belum diisi.

## Aturan untuk agent
- Kerjakan satu tugas per sesi.
- Jangan ubah file di luar tugas.
- Di akhir tugas, tambahkan satu entri di `RIWAYAT.md` (paling atas): nomor, judul singkat, tanggal, file yang diubah, alasan. Jangan ubah entri lama. Kalau tidak yakin tanggalnya, tulis "tidak tercatat", jangan menebak.
- Aturan baca RIWAYAT.md: di awal sesi, baca hanya 5 entri paling atas. Jangan baca seluruh file. Jangan baca file RIWAYAT_ARSIP*.md kecuali pemilik memintanya.
- Aturan arsip RIWAYAT.md: sebelum menambah entri baru, hitung jumlah entri di RIWAYAT.md. Kalau sudah ada 50 entri, lakukan ini dulu:
  1. Lihat file RIWAYAT_ARSIP*.md yang sudah ada. Ambil nomor terbesar lalu tambah 1 (kalau belum ada, mulai dari 1).
  2. Ganti nama RIWAYAT.md jadi RIWAYAT_ARSIP{n}.md dengan git mv.
  3. Buat RIWAYAT.md baru yang isinya sama seperti template RIWAYAT.md sebelumnya (judul, aturan, dan format entri di bagian atas file), tapi tanpa entri.
  4. Nomor entri tidak diulang dari 1. Lanjutkan dari nomor terakhir di arsip.
  5. Entri baru ditulis di RIWAYAT.md yang baru.
  6. Stage RIWAYAT.md dan RIWAYAT_ARSIP{n}.md satu per satu, dan sebutkan keduanya di daftar file pada entri.
  Jangan ubah isi file arsip setelah dibuat.
- Sebelum mulai kerja, jalankan git branch --show-current. Hasilnya harus master. Kalau hasilnya bukan master, berhenti: jangan pindah branch, jangan membuat branch, jangan commit, jangan push. Laporkan nama branch yang aktif ke pemilik. Kalau selama sesi muncul branch atau worktree baru yang dibuat otomatis oleh tool, berhenti dan laporkan juga, jangan push. Semua commit dan push dilakukan di master saja.
1. Jalankan git status --short. Kalau ada file yang muncul tapi bukan bagian dari tugas, berhenti: jangan commit, jangan push, laporkan ke pemilik.
2. Tambahkan entri di paling atas RIWAYAT.md. Daftar file diambil dari git status --short, ditambah RIWAYAT.md sendiri dan CATATAN.md kalau ikut berubah.
3. Stage file dengan menyebut namanya satu per satu. Dilarang git add -A atau git add .
4. Commit dengan pesan lengkap: judul singkat, isi penjelasan, lalu dua baris trailer di bawah, dipisah satu baris kosong dari isi pesan.
   Co-authored-by: Claude <noreply@anthropic.com>
   Co-authored-by: Gemini (Antigravity) <200291788+gemini-code-assist@users.noreply.github.com>
5. Jalankan git push ke branch yang sedang aktif. Dilarang force push, dilarang membuat atau menghapus branch, dan dilarang mengubah git config.
6. Kalau commit atau push gagal, jangan coba cara lain. Berhenti dan laporkan error-nya ke pemilik.
7. Di akhir, kabari file apa saja yang diubah dan hash commit-nya.
- Aturan tema:
  - Layout halaman bebas dan boleh berbeda-beda. Yang wajib sama di semua halaman hanya palet warnanya (palet Kanade).
  - Palet tersedia sebagai CSS custom properties (`:root { --kanade-... }`) lewat `assets/css/kanade-palette.css` (hasil kompilasi Jekyll dari `assets/css/kanade-palette.scss`). File skin dan semua halaman mengambil warna dari sini.
  - Setiap halaman atau layout baru, termasuk yang tanpa layout Minimal Mistakes, wajib memuat `kanade-palette.css`.
  - Dilarang warna hardcode (`#fff`, `white`, `black`, kode hex) di halaman, include, atau CSS baru. Pakai variabel palet. Butuh warna baru? Tambah dulu ke `_kanade.scss` dan tambah variabel baru di `kanade-palette.scss`. Pengecualian: file gambar (seperti `assets/images/og-image.png` dan file gambar favicon di `assets/images/`) dikecualikan dari aturan larangan hex karena warnanya tersimpan di dalam file gambar.

## Skin Kanade
- Nama skin: `kanade`
- File skin: `_sass/minimal-mistakes/skins/_kanade.scss`
- Sumber palet warna (Gelap):
  - Background: `#121016` (ungu-hitam gelap)
  - Teks: `#EDEAF0` (lavender terang)
  - Aksen/primary: `#BB6588` (pink Kanade)
- Sumber palet warna (Terang):
  - Background: `#FAFAFC` (silver-putih pucat)
  - Teks: `#121016` (ungu-hitam gelap)
  - Aksen/primary: `#A85A7A` (pink Kanade pekat)
- Diaktifkan via `_config.yml` → `minimal_mistakes_skin: "kanade"`

### Arsitektur kanade-palette.css & main-light.css
**Status: sudah ada** (diperbarui Sesi 2)

- `_kanade.scss` (dan turunannya) = satu-satunya tempat nilai warna hex untuk tema gelap maupun terang ditulis (variabel SCSS).
- `assets/css/kanade-palette.scss` = file SCSS dengan front matter Jekyll. Mengimport `_kanade.scss`, lalu emit `:root` dan CSS fallback (media query & data-theme) untuk mengaktifkan palet terang.
- Tema Terang = dikompilasi ke `assets/css/main-light.css` menggunakan wrapper SASS `[data-theme="light"]` dan fallback `@media (prefers-color-scheme: light)`, mengimport ulang inti SASS Minimal Mistakes agar berjalan murni CSS tanpa JS.
- Halaman Minimal Mistakes memuat `kanade-palette.css` dan `main-light.css` via `<link>` di `_includes/head/custom.html`.
- Halaman standalone HTML memuat `kanade-palette.css` via `<link>` langsung.
- **Jangan tulis hex di `kanade-palette.scss` maupun `main-light.scss`** — nilai warna hanya boleh ada di `_kanade.scss`.

### Gotcha saat pembuatan skin
- Tidak ada warna hardcode di `_includes/`, `_layouts/`, atau `_pages/`.
  Semua modul SCSS Minimal Mistakes sudah pakai variabel, jadi cukup
  override variabel di file skin saja.
- File `_includes/head/custom.html` semula kosong; sekarang berisi `<link>` ke `kanade-palette.css`.
- Jika nanti menambah CSS custom (misal untuk elemen buka-tutup `<details>`
  atau easter egg), gunakan variabel `--kanade-bg`, `--kanade-text`, `--kanade-accent`,
  atau variabel SCSS `$background-color`, `$text-color`, `$primary-color` — jangan hardcode.
