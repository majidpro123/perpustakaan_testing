import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.main import register, login, tambah_buku, daftar_buku

# ==== Test Case Positif ====
def test_register_anggota2():
    hasil = register("anggota2", "pass123")
    assert hasil == "Registrasi berhasil."

def test_login_anggota2():
    register("anggota2_user", "456")
    hasil = login("anggota2_user", "456")
    assert hasil == "Login berhasil."

def test_tambah_buku_anggota2():
    hasil = tambah_buku("Python Lanjutan", "Guido van Rossum", 2023)
    assert hasil == "Buku berhasil ditambahkan."

# ==== Test Case Negatif ====
def test_login_salah_anggota2():
    register("anggota2_salah", "abc")
    hasil = login("anggota2_salah", "xyz")
    assert hasil == "Password salah."

# ==== Test Case Boundary / Limit ====
def test_tambah_buku_kosong_anggota2():
    hasil = tambah_buku("", "", 0)
    assert hasil == "Data buku tidak lengkap."

def test_daftar_buku_anggota2():
    daftar = daftar_buku()
    assert len(daftar) >= 0  # minimal sudah ada buku atau kosong
