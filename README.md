# Sistem Manajemen Perpustakaan (MVC Python)

## Deskripsi Singkat Aplikasi
Sistem Manajemen Perpustakaan adalah aplikasi desktop berbasis Python yang dirancang menggunakan arsitektur **Model-View-Controller (MVC)**. Aplikasi ini dilengkapi dengan antarmuka grafis modern menggunakan pustaka **CustomTkinter**, serta terintegrasi dengan database **MySQL** untuk manajemen data buku, anggota, peminjaman, dan sistem autentikasi berbasis *role* (Admin & Anggota).

## Struktur Direktori MVC
Proyek ini diorganisasikan secara modular ke dalam beberapa direktori utama:
```text
PERPUSTAKAAN/
│
├── config/             # Konfigurasi koneksi database
├── controllers/        # Pengatur logika alur aplikasi & otorisasi role
├── models/             # Pengelolaan data & kueri SQL (Prepared Statements)
├── views/              # Antarmuka grafis (GUI) CustomTkinter
├── tests/              # Berkas pengujian unit (Pytest)
├── .github/workflows/  # Konfigurasi CI/CD Pipeline (GitHub Actions)
├── main.py             # Titik masuk utama aplikasi (Entry point)
└── requirements.txt    # Daftar dependensi pustaka proyek
## Panduan Instalasi & Konfigurasi Database MySQL
1. Pastikan aplikasi **Laragon** sudah terinstal dan layanan **MySQL** sedang berjalan.
2. Buat database baru bernama `perpustakaan` melalui terminal MySQL atau HeidiSQL.
3. Buat tabel-tabel yang diperlukan (`buku`, `anggota`, `peminjaman`, dan `users`) sesuai skema relasional sistem.
4. Kloning repositori ini, lalu buat dan aktifkan *Virtual Environment* di terminal:
   ```bash
   python -m venv env
   .\env\Scripts\activate
5. Instal seluruh dependensi proyek:
   ```bash
   pip install -r requirements.txt
## Cara Menjalankan Aplikasi
* **Melalui Kode Sumber (Development Mode)**:
  Pastikan virtual environment aktif, lalu jalankan perintah:
  ```bash
  python main.py
* **Melalui File Eksekusi Mandiri (Standalone .exe):**
Buka folder dist/ melalui Windows Explorer, lalu klik dua kali pada file AplikasiPerpustakaan.exe.
