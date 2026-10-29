from unittest.mock import MagicMock
from models.buku_model import BukuModel

def test_create_buku_berhasil():
    # Menginisialisasi Model
    model = BukuModel()

    # Memanipulasi (Mock) koneksi database agar tidak mengotori data asli
    model.conn = MagicMock()
    mock_cursor = MagicMock()
    model.conn.cursor.return_value = mock_cursor

    # Melakukan eksekusi fungsi
    hasil = model.create_buku("Buku Testing", "Penulis QA", 2026)

    # Memverifikasi apakah fungsi mengembalikan nilai True
    assert hasil is True
    # Memverifikasi apakah cursor.execute benar-benar dipanggil
    mock_cursor.execute.assert_called_once()
    # Memverifikasi apakah perintah commit (simpan) dipanggil
    model.conn.commit.assert_called_once()

from unittest.mock import MagicMock
from models.buku_model import BukuModel

def test_get_all_buku():
    # Membuat mock untuk kelas BukuModel
    mock_model = MagicMock(spec=BukuModel)
    
    # Menentukan data tiruan (dummy data) yang dikembalikan saat get_all_buku() dipanggil
    mock_model.get_all_buku.return_value = [
        {"id_buku": 1, "judul": "Pemrograman Python MVC", "penulis": "Guido van Rossum", "tahun_terbit": 2023},
        {"id_buku": 2, "judul": "Algoritma dan Pemrograman", "penulis": "John Doe", "tahun_terbit": 2021}
    ]
    
    # Memanggil fungsi get_all_buku() dari mock model
    result = mock_model.get_all_buku()
    
    # Memastikan fungsi get_all_buku terpanggil dan mengembalikan data yang benar
    mock_model.get_all_buku.assert_called_once()
    assert len(result) == 2
    assert result[0]["judul"] == "Pemrograman Python MVC"
    assert result[1]["penulis"] == "John Doe"