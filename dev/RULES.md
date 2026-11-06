# Rules

## Ringkasan
Situs portofolio pribadi di GitHub Pages, fork tema Jekyll Minimal Mistakes.
Static saja (tanpa backend). Tema tidak akan diupdate dari upstream, boleh edit file mana pun.

## Keputusan
- Bahasa: Indonesia, English, Jepang
- Halaman pilih bahasa tetap bisa dibuka manual lewat /?pilih
- Salam pembuka tiap halaman ditulis manual oleh pemilik, jangan diubah agent

## Gotcha (jangan diulang)
- Jangan pakai include_cached untuk masthead, karena teksnya beda per bahasa
  (dulu bikin tombol "ganti bahasa" selalu berbahasa Inggris).
- Verifikasi Discord memakai `.well-known/discord` dengan `include: [".well-known"]` di _config.yml, dan jangan pernah menambah .nojekyll karena situs ini butuh Jekyll.
- Branch utama repo ini adalah master, bukan main, dan branch tambahan sebelumnya (hide-kanade-seo) dibuat tidak sengaja serta sudah dihapus.
- dev/ harus tetap ada di exclude di _config.yml supaya tidak ter-publish di situs. Jangan hapus dari exclude.
- Hati-hati dengan spesifisitas CSS pada tag `<a>` (link) seperti untuk efek hover atau visited. Tema Minimal Mistakes memiliki styling bawaan (`a:hover`, `a:visited`, dll.) yang bisa menimpa class custom. Gunakan `!important` atau selector yang sangat spesifik jika elemen custom (seperti pemicu easter egg) tidak bereaksi.
- `robots.txt` tidak boleh memuat `Disallow` untuk URL easter egg karena robots.txt bersifat publik dan justru akan membocorkan URL-nya.
- JSON-LD Person tidak boleh memuat nama asli, kampus, atau data pribadi lain.
- Pada SASS Minimal Mistakes, beberapa variabel turunan seperti `$masthead-link-color` dievaluasi pada saat `_kanade.scss` diimpor (mengambil nilai `$text-color` mode gelap). Saat membuat mode terang, meng-override `$text-color` saja tidak cukup karena variabel turunan tersebut sudah menjadi hex. Cara memperbaikinya: definisikan variabel eksplisit seperti `$masthead-link-color-light: $text-color-light !default;` di `_kanade.scss`, lalu override secara manual `$masthead-link-color: $masthead-link-color-light;` di dalam `main-light.scss` dan `main-light-os.scss`.

## Pengujian Lokal
- Untuk mengecek konsistensi bahasa, permalink, dan link rusak secara lokal, jalankan `python scripts/check-languages.py` dari root repo. Skrip akan memberikan rincian file yang bermasalah dan mengembalikan exit code 1 jika ada error. Skrip juga akan mencetak peringatan jika menemukan teks Jepang tanpa atribut lang="ja" di halaman id dan en. Skrip juga mencetak peringatan untuk placeholder yang belum diisi. Skrip juga akan mencetak peringatan jika menemukan warna hardcode (file bawaan tema _includes/page__hero.html dikecualikan karena tidak dipakai), dan akan menghasilkan error jika teks tombol ganti tema tiga bahasa tidak lengkap di masthead.

## Aturan untuk agent
- Kerjakan satu tugas per sesi.
- Jangan ubah file di luar tugas.
- Rencana ada di folder dev/. Centang tugas yang selesai di dev/PLAN.md. Kalau satu rencana sudah selesai semua, pindahkan ke bagian ## Selesai di dev/PLAN.md apa adanya.
- Di akhir tugas, tambahkan satu entri di `dev/CHANGELOG.md` (paling atas): nomor, judul singkat, tanggal, file yang diubah, alasan. Jangan ubah entri lama. Kalau tidak yakin tanggalnya, tulis "tidak tercatat", jangan menebak.
- Aturan baca di awal sesi: baca dev/RULES.md, dev/PLAN.md, dan 5 entri teratas dev/CHANGELOG.md; baca dev/DESIGN.md hanya jika tugas menyentuh tampilan, dev/STRUKTUR.md hanya jika tugas menyentuh halaman, slug, atau include, dan dev/PLANSPEC.md hanya bagian item yang sedang dikerjakan; jangan baca dev/arsip/ kecuali pemilik memintanya.
- Aturan arsip dev/CHANGELOG.md: sebelum menambah entri baru, hitung jumlah entri di dev/CHANGELOG.md. Kalau sudah ada 50 entri, lakukan ini dulu:
  1. Lihat file dev/arsip/CHANGELOG_ARSIP*.md yang sudah ada. Ambil nomor terbesar lalu tambah 1 (kalau belum ada, mulai dari 1).
  2. Ganti nama dev/CHANGELOG.md jadi dev/arsip/CHANGELOG_ARSIP{n}.md dengan git mv.
  3. Buat dev/CHANGELOG.md baru yang isinya sama seperti template dev/CHANGELOG.md sebelumnya (judul, aturan, dan format entri di bagian atas file), tapi tanpa entri.
  4. Nomor entri tidak diulang dari 1. Lanjutkan dari nomor terakhir di arsip.
  5. Entri baru ditulis di dev/CHANGELOG.md yang baru.
  6. Stage dev/CHANGELOG.md dan dev/arsip/CHANGELOG_ARSIP{n}.md satu per satu, dan sebutkan keduanya di daftar file pada entri.
  Jangan ubah isi file arsip setelah dibuat.
- Sebelum mulai kerja, jalankan git branch --show-current. Hasilnya harus master. Kalau hasilnya bukan master, berhenti: jangan pindah branch, jangan membuat branch, jangan commit, jangan push. Laporkan nama branch yang aktif ke pemilik. Kalau selama sesi muncul branch atau worktree baru yang dibuat otomatis oleh tool, berhenti dan laporkan juga, jangan push. Semua commit dan push dilakukan di master saja.
1. Jalankan git status --short. Kalau ada file yang muncul tapi bukan bagian dari tugas, berhenti: jangan commit, jangan push, laporkan ke pemilik.
2. Tambahkan entri di paling atas dev/CHANGELOG.md. Daftar file diambil dari git status --short, ditambah dev/CHANGELOG.md sendiri dan file lain kalau ikut berubah.
3. Stage file dengan menyebut namanya satu per satu. Dilarang git add -A atau git add .
4. Commit dengan pesan lengkap: judul singkat, isi penjelasan, lalu dua baris trailer di bawah, dipisah satu baris kosong dari isi pesan.
   Co-authored-by: Claude <noreply@anthropic.com>
   Co-authored-by: Gemini (Antigravity) <200291788+gemini-code-assist@users.noreply.github.com>
5. Jalankan git push ke branch yang sedang aktif. Dilarang force push, dilarang membuat atau menghapus branch, dan dilarang mengubah git config.
6. Kalau commit atau push gagal, jangan coba cara lain. Berhenti dan laporkan error-nya ke pemilik.
7. Di akhir, kabari file apa saja yang diubah dan hash commit-nya.
