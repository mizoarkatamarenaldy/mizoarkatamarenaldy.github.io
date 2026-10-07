# Plan Selesai

## Status fitur
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
| Ring fokus di warna tombol (hover state) | #EDEAF0 (Teks) | #BB6588 (Primary)| 3.31:1 | 3:1 | Lulus |

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
4. **home-btn, tombol Sebelumnya/Berikutnya, contact-btn**: Sudah memiliki desain ring fokus eksplisit dengan  ar(--kanade-text) (kontras sangat jelas).
   *Perbaikan*: Tidak ada, dibiarkan seperti adanya (dikecualikan dari aturan CSS global agar tidak tumpang tindih).
5. **Pemicu easter egg Kanade (.kanade-trigger)**: Sesuai instruksi, pemicu ini sengaja dibuat sembunyi dan dilarang diubah. Outline sudah diatur 
one, namun ketika menerima fokus (hover/focus-visible), warna teks berubah menjadi #BB6588.
   *Perbaikan*: Tidak diubah tampilannya, warna teks #BB6588 memiliki kontras 4.80:1 terhadap latar #121016 sehingga masih terbaca dan lulus WCAG (meskipun sengaja dibuat obscure).

Aturan untuk sesi-sesi ini: kerjakan satu sesi satu nomor, centang nomor yang selesai di `CATATAN.md` pada akhir sesinya, dan jangan mengerjakan sesi berikutnya.
