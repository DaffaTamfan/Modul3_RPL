import tkinter.messagebox as messagebox
from models.buku_model import BukuModel
from views.buku_view import BukuView

class BukuController:
    def __init__(self):
        self.model = BukuModel()
        self.view = BukuView()

        # Binding tombol
        self.view.btn_simpan.configure(command=self.simpan_data)
        self.view.btn_hapus.configure(command=self.hapus_data)
        self.view.btn_update.configure(command=self.perbarui_data)

        # Binding klik tabel untuk mengisi form saat baris dipilih
        self.view.tabel.bind("<<TreeviewSelect>>", self.select_data)

        self.muat_data_tabel()

    def muat_data_tabel(self):
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        data_buku = self.model.get_all_buku()
        for buku in data_buku:
            self.view.tabel.insert("", "end", values=(buku['id_buku'], buku['judul'], buku['penulis'], buku['tahun_terbit']))

    def select_data(self, event):
        selected_item = self.view.tabel.selection()
        if selected_item:
            item_data = self.view.tabel.item(selected_item)
            values = item_data['values']
            if values:
                self.view.entry_judul.delete(0, 'end')
                self.view.entry_judul.insert(0, values[1])

                self.view.entry_penulis.delete(0, 'end')
                self.view.entry_penulis.insert(0, values[2])

                self.view.entry_tahun.delete(0, 'end')
                self.view.entry_tahun.insert(0, values[3])

    def simpan_data(self):
        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()

        if not judul or not penulis or not tahun:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return

        berhasil = self.model.create_buku(judul, penulis, tahun)
        if berhasil:
            messagebox.showinfo("Sukses", "Data buku berhasil disimpan!")
            self.view.entry_judul.delete(0, 'end')
            self.view.entry_penulis.delete(0, 'end')
            self.view.entry_tahun.delete(0, 'end')
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Terjadi kesalahan saat menyimpan data.")

    def hapus_data(self):
        selected_item = self.view.tabel.selection()
        if not selected_item:
            messagebox.showwarning("Peringatan", "Pilih baris data pada tabel yang ingin dihapus!")
            return

        item_data = self.view.tabel.item(selected_item)
        id_buku = item_data['values'][0]

        if not messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus data ini?"):
            return

        berhasil = self.model.delete_buku(id_buku)
        if berhasil:
            messagebox.showinfo("Sukses", "Data buku berhasil dihapus!")
            self.view.entry_judul.delete(0, 'end')
            self.view.entry_penulis.delete(0, 'end')
            self.view.entry_tahun.delete(0, 'end')
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Terjadi kesalahan saat menghapus data.")

    def perbarui_data(self):
        selected_item = self.view.tabel.selection()
        if not selected_item:
            messagebox.showwarning("Peringatan", "Pilih baris data pada tabel yang ingin diperbarui!")
            return

        item_data = self.view.tabel.item(selected_item)
        id_buku = item_data['values'][0]

        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()

        if not judul or not penulis or not tahun:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi untuk memperbarui data!")
            return

        berhasil = self.model.update_buku(id_buku, judul, penulis, tahun)
        if berhasil:
            messagebox.showinfo("Sukses", "Data buku berhasil diperbarui!")
            self.view.entry_judul.delete(0, 'end')
            self.view.entry_penulis.delete(0, 'end')
            self.view.entry_tahun.delete(0, 'end')
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Terjadi kesalahan saat memperbarui data.")

    def run(self):
        self.view.mainloop()