import tkinter.messagebox as messagebox
from models.anggota_model import AnggotaModel
from views.anggota_view import AnggotaView

class AnggotaController:
    def __init__(self):
        # Inisialisasi Model dan View untuk Anggota
        self.model = AnggotaModel()
        self.view = AnggotaView()

        # Binding (mengikat) tombol di View dengan fungsi di Controller
        self.view.btn_simpan.configure(command=self.simpan_data)
        self.view.btn_hapus.configure(command=self.hapus_data)
        self.view.btn_update.configure(command=self.perbarui_data)

        # Binding klik pada tabel agar data otomatis masuk ke form saat baris diklik
        self.view.tabel_anggota.bind("<<TreeviewSelect>>", self.select_data)

        # Memuat data ke tabel saat aplikasi pertama kali dibuka
        self.muat_data_tabel()

    def muat_data_tabel(self):
        # Mengosongkan isi tabel menggunakan tabel_anggota
        for item in self.view.tabel_anggota.get_children():
            self.view.tabel_anggota.delete(item)

        # Mengambil data dari Model (database)
        data_anggota = self.model.get_all_anggota()

        # Memasukkan data ke dalam tabel View
        for anggota in data_anggota:
            self.view.tabel_anggota.insert("", "end", values=(anggota['id_anggota'], anggota['nama'], anggota['alamat']))

    def select_data(self, event):
        # Fungsi untuk mengisi form otomatis saat baris pada tabel diklik
        selected_item = self.view.tabel_anggota.selection()
        if selected_item:
            item_data = self.view.tabel_anggota.item(selected_item)
            values = item_data['values']
            if values:
                self.view.entry_nama.delete(0, 'end')
                self.view.entry_nama.insert(0, values[1])
                
                self.view.text_alamat.delete("1.0", "end")
                self.view.text_alamat.insert("1.0", values[2])

    def simpan_data(self):
        nama = self.view.entry_nama.get()
        alamat = self.view.text_alamat.get("1.0", "end-1c").strip()

        if not nama or not alamat:
            messagebox.showwarning("Peringatan", "Semua kolom form anggota harus diisi!")
            return

        berhasil = self.model.create_anggota(nama, alamat)

        if berhasil:
            messagebox.showinfo("Sukses", "Data anggota berhasil disimpan!")
            self.view.entry_nama.delete(0, 'end')
            self.view.text_alamat.delete("1.0", "end")
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Terjadi kesalahan saat menyimpan data anggota.")

    def hapus_data(self):
        selected_item = self.view.tabel_anggota.selection()
        if not selected_item:
            messagebox.showwarning("Peringatan", "Pilih baris data anggota pada tabel yang ingin dihapus!")
            return

        item_data = self.view.tabel_anggota.item(selected_item)
        id_anggota = item_data['values'][0]

        if not messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus data anggota ini?"):
            return

        berhasil = self.model.delete_anggota(id_anggota)

        if berhasil:
            messagebox.showinfo("Sukses", "Data anggota berhasil dihapus!")
            self.view.entry_nama.delete(0, 'end')
            self.view.text_alamat.delete("1.0", "end")
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Terjadi kesalahan saat menghapus data anggota.")

    def perbarui_data(self):
        selected_item = self.view.tabel_anggota.selection()
        if not selected_item:
            messagebox.showwarning("Peringatan", "Pilih baris data anggota pada tabel yang ingin diperbarui!")
            return

        item_data = self.view.tabel_anggota.item(selected_item)
        id_anggota = item_data['values'][0]

        nama = self.view.entry_nama.get()
        alamat = self.view.text_alamat.get("1.0", "end-1c").strip()

        if not nama or not alamat:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi untuk memperbarui data!")
            return

        berhasil = self.model.update_anggota(id_anggota, nama, alamat)

        if berhasil:
            messagebox.showinfo("Sukses", "Data anggota berhasil diperbarui!")
            self.view.entry_nama.delete(0, 'end')
            self.view.text_alamat.delete("1.0", "end")
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Terjadi kesalahan saat memperbarui data anggota.")

    def run(self):
        self.view.mainloop()