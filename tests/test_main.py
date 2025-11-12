import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.main import register, login, tambah_buku, daftar_buku

def test_register_berhasil():
    hasil = register("majid", "123")
    assert hasil == "Registrasi berhasil."

def test_login_berhasil():
    register("user1", "123")
    hasil = login("user1", "123")
    assert hasil == "Login berhasil."

def test_login_gagal():
    hasil = login("user1", "salah")
    assert hasil == "Password salah."

def test_tambah_buku_berhasil():
    hasil = tambah_buku("Laskar Pelangi", "Andrea Hirata", 2005)
    assert hasil == "Buku berhasil ditambahkan."

def test_daftar_buku_tidak_kosong():
    daftar = daftar_buku()
    assert len(daftar) > 0
