# Daffa_039
import customtkinter as ctk
from tkinter import ttk

class AnggotaView(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistem Manajemen Perpustakaan - Anggota")
        self.geometry("850x450")

        # Konfigurasi Grid Utama (1 Baris, 2 Kolom)
        self.grid_columnconfigure(0, weight=1) # Kolom Kiri (Form)
        self.grid_columnconfigure(1, weight=3) # Kolom Kanan (Tabel Anggota)
        self.grid_rowconfigure(0, weight=1)

        # ========================================
        # FRAME KIRI: FORMULIR INPUT ANGGOTA
        # ========================================
        self.frame_kiri = ctk.CTkFrame(self)
        self.frame_kiri.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        ctk.CTkLabel(self.frame_kiri, text="Form Data Anggota", font=("Arial", 16, "bold")).pack(pady=15)

        # Komponen Input Anggota (Menyesuaikan kolom: Nama & Alamat)
        self.entry_nama = ctk.CTkEntry(self.frame_kiri, placeholder_text="Masukkan Nama Anggota")
        self.entry_nama.pack(pady=10, padx=15, fill="x")

        # Menggunakan CTkTextbox untuk Alamat agar mendukung teks panjang/multi-line
        ctk.CTkLabel(self.frame_kiri, text="Alamat Anggota:", font=("Arial", 12)).pack(anchor="w", padx=15, pady=(5, 0))
        self.text_alamat = ctk.CTkTextbox(self.frame_kiri, height=85)
        self.text_alamat.pack(pady=5, padx=15, fill="x")

        # Tombol Aksi Anggota
        self.btn_simpan = ctk.CTkButton(self.frame_kiri, text="Simpan Anggota", fg_color="green", hover_color="darkgreen")
        self.btn_simpan.pack(pady=10, padx=15, fill="x")

        self.btn_update = ctk.CTkButton(self.frame_kiri, text="Perbarui Anggota", fg_color="blue", hover_color="darkblue")
        self.btn_update.pack(pady=10, padx=15, fill="x")

        self.btn_hapus = ctk.CTkButton(self.frame_kiri, text="Hapus Anggota", fg_color="red", hover_color="darkred")
        self.btn_hapus.pack(pady=10, padx=15, fill="x")

        # ========================================
        # FRAME KANAN: TABEL DAFTAR ANGGOTA
        # ========================================
        self.frame_kanan = ctk.CTkFrame(self)
        self.frame_kanan.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        ctk.CTkLabel(self.frame_kanan, text="Daftar Anggota Perpustakaan", font=("Arial", 16, "bold")).pack(pady=15)

        # Komponen Tabel (Treeview) khusus data spesifik anggota
        kolom_anggota = ("id_anggota", "nama_anggota", "alamat")
        self.tabel_anggota = ttk.Treeview(self.frame_kanan, columns=kolom_anggota, show="headings", height=12)

        # Konfigurasi Header Tabel Anggota
        self.tabel_anggota.heading("id_anggota", text="ID")
        self.tabel_anggota.heading("nama_anggota", text="Nama Anggota")
        self.tabel_anggota.heading("alamat", text="Alamat")

        # Konfigurasi Lebar Kolom Tabel Anggota
        self.tabel_anggota.column("id_anggota", width=40, anchor="center")
        self.tabel_anggota.column("nama_anggota", width=150)
        self.tabel_anggota.column("alamat", width=210)

        self.tabel_anggota.pack(fill="both", expand=True, padx=15, pady=10)

if __name__ == "__main__":
    app = AnggotaView()
    app.mainloop()