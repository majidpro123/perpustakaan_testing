import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.main import register, login, tambah_buku, daftar_buku

# ==== Test Case Positif ====
def test_register_anggota3():
    hasil = register("anggota3", "pass789")
    assert hasil == "Registrasi berhasil."

def test_login_anggota3():
    register("anggota3_user", "789")
    hasil = login("anggota3_user", "789")
    assert hasil == "Login berhasil."

def test_tambah_buku_anggota3():
    hasil = tambah_buku("Belajar Java", "James Gosling", 2010)
    assert hasil == "Buku berhasil ditambahkan."

# ==== Test Case Negatif ====
def test_login_salah_anggota3():
    register("anggota3_salah", "111")
    hasil = login("anggota3_salah", "222")
    assert hasil == "Password salah."

# ==== Test Case Boundary / Limit ====
def test_tambah_buku_kosong_anggota3():
    hasil = tambah_buku("", "", None)
    assert hasil == "Data buku tidak lengkap."

def test_daftar_buku_anggota3():
    daftar = daftar_buku()
    assert len(daftar) >= 0
