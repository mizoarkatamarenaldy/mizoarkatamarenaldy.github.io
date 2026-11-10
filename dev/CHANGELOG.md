# History Perubahan

Log perubahan web portofolio yang dikerjakan lewat Antigravity.

Aturan:
- Terbaru di atas. Satu entri = satu tugas/sesi.
- Format: nomor, judul singkat, tanggal, file, alasan.
- Jangan ubah entri lama. Kalau ada koreksi, tulis entri baru.
- Yang tidak diketahui ditulis "tidak tercatat", jangan menebak.

---

## #52 | samakan nama portofolio dengan Big Eleventh Skills
- Tanggal: 2026-11-10
- File: `_data/portfolio-nav.yml`, `_includes/head/jsonld-person.html`, `_pages/en-main.md`, `_pages/en-portfolio-applied-linguistics-multilingual.md`, `_pages/en-portfolio-audio-music-composition.md`, `_pages/en-portfolio-data-science-analyst.md`, `_pages/en-portfolio-design-ui-ux.md`, `_pages/en-portfolio-developer.md`, `_pages/en-portfolio-domestic-operations-culinary.md`, `_pages/en-portfolio-entrepreneurship.md`, `_pages/en-portfolio-illustration-visual-arts.md`, `_pages/en-portfolio-literacy-creative-writing.md`, `_pages/en-portfolio-second-brain.md`, `_pages/en-portfolio-sport.md`, `_pages/id-main.md`, `_pages/id-portfolio-applied-linguistics-multilingual.md`, `_pages/id-portfolio-audio-music-composition.md`, `_pages/id-portfolio-data-science-analyst.md`, `_pages/id-portfolio-design-ui-ux.md`, `_pages/id-portfolio-developer.md`, `_pages/id-portfolio-domestic-operations-culinary.md`, `_pages/id-portfolio-entrepreneurship.md`, `_pages/id-portfolio-illustration-visual-arts.md`, `_pages/id-portfolio-literacy-creative-writing.md`, `_pages/id-portfolio-second-brain.md`, `_pages/id-portfolio-sport.md`, `_pages/ja-main.md`, `_pages/ja-portfolio-applied-linguistics-multilingual.md`, `_pages/ja-portfolio-audio-music-composition.md`, `_pages/ja-portfolio-data-science-analyst.md`, `_pages/ja-portfolio-design-ui-ux.md`, `_pages/ja-portfolio-developer.md`, `_pages/ja-portfolio-domestic-operations-culinary.md`, `_pages/ja-portfolio-entrepreneurship.md`, `_pages/ja-portfolio-illustration-visual-arts.md`, `_pages/ja-portfolio-literacy-creative-writing.md`, `_pages/ja-portfolio-second-brain.md`, `_pages/ja-portfolio-sport.md`, `dev/CHANGELOG.md`, `dev/PLAN.md`, `dev/PLANSPEC.md`, `dev/STRUKTUR.md`, `scripts/check-languages.py`
- Alasan: Menyesuaikan daftar dan nama halaman portofolio dengan 11 skill pemilik (Big Eleventh Skills: 3 pilar dan 8 sayap). Mengubah Main Portfolio menjadi Psikologi, HR, dan Linguistik Terapan & Multilingual (menggantikan Bahasa Jepang). Mengubah susunan Additional Portfolio menjadi Developer, Data Science/Analyst, Desain & UI/UX, Ilustrasi & Seni Visual, Literasi & Creative Writing, Audio & Komposisi Musik, Operasional Domestik & Kuliner, dan Entrepreneurship. Menghapus halaman Second Brain dan Sport serta tautannya di tiga bahasa (id, en, ja). Membuat halaman kerangka Entrepreneurship dengan placeholder di tiga bahasa. Memperbarui tombol di HOME, JSON-LD Person, urutan navigasi Sebelumnya/Berikutnya di _data/portfolio-nav.yml, slug dan permalink di _pages/, skrip scripts/check-languages.py, serta dokumentasi di dev/PLAN.md, dev/PLANSPEC.md, dan dev/STRUKTUR.md.

## #51 | pecah CATATAN.md ke dev/
- Tanggal: 2026-11-06
- File: `_config.yml`, `CATATAN.md`, `dev/arsip/CHANGELOG_ARSIP1.md`, `dev/CHANGELOG.md`, `dev/DESIGN.md`, `dev/PLANSPEC.md`, `dev/RULES.md`, `dev/STRUKTUR.md`
- Alasan: Memecah berkas CATATAN.md ke dalam berkas-berkas modular di dev/ (dev/RULES.md, dev/DESIGN.md, dan dev/STRUKTUR.md). Memindahkan bagian Hasil Audit Sesi 1 dari dev/PLANSPEC.md ke dev/DESIGN.md. Memperbarui aturan membaca awal sesi dan aturan pengarsipan di dev/RULES.md. Menghapus berkas CATATAN.md dari repositori dan dari daftar exclude pada _config.yml. Mengarsipkan dev/CHANGELOG.md ke dev/arsip/CHANGELOG_ARSIP1.md karena telah mencapai 50 entri, lalu membuat dev/CHANGELOG.md baru.
