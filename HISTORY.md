# History Perubahan

Log perubahan web portofolio yang dikerjakan lewat Antigravity.

Aturan:
- Terbaru di atas. Satu entri = satu tugas/sesi.
- Format: nomor, judul singkat, tanggal, file, alasan.
- Jangan ubah entri lama. Kalau ada koreksi, tulis entri baru.
- Yang tidak diketahui ditulis "tidak tercatat", jangan menebak.

---

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
