# Desain

## Aturan tema
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

## Hasil Audit Sesi 1

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
