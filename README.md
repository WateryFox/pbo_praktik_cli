# CLI Book Management System

Aplikasi Command-Line Interface (CLI) berbasis Python dan Pemrograman Berbasis Objek (PBO) yang digunakan untuk mengelola inventaris buku. Proyek ini mengimplementasikan pemisahan modul secara terstruktur dan menyimpan data secara persisten menggunakan format CSV.

---

## Fitur Utama

- **Tampilkan Daftar Buku:** Menampilkan seluruh data buku yang tersimpan dalam sistem.
- **Tambah Buku Baru:** Menginput data buku baru ke dalam database secara interaktif.
- **Persistensi Data:** Seluruh perubahan data tersimpan otomatis pada file `buku.csv`.
- **Arsitektur Modular (OOP):** Pengkodean mengacu pada prinsip Pemrograman Berbasis Objek (`models.py`) untuk mempermudah pemeliharaan kode.

---

## Struktur Proyek

```text
pbo_praktik_cli/
├── Main.py            # Entry point program dan navigasi menu utama
├── models.py          # Class dan data model (OOP)
├── tambah_buku.py     # Modul penambahan data buku
├── tampil_buku.py     # Modul menampilkan daftar buku
├── buku.csv           # File penyimpanan data (CSV)
├── .gitignore         # Daftar berkas yang diabaikan oleh Git
└── LICENSE            # Lisensi proyek (MIT License)
