# app/main.py

# Simulasi sederhana sistem perpustakaan
# berisi login, register, dan tambah buku

users = {}   # Menyimpan data user
books = []   # Menyimpan daftar buku


def register(username, password):
    """Mendaftarkan user baru."""
    if username in users:
        return "Username sudah terdaftar."
    users[username] = password
    return "Registrasi berhasil."


def login(username, password):
    """Login ke sistem."""
    if username not in users:
        return "Username tidak ditemukan."
    if users[username] != password:
        return "Password salah."
    return "Login berhasil."


def tambah_buku(judul, pengarang, tahun):
    """Menambahkan buku baru ke daftar."""
    if not judul or not pengarang or not tahun:
        return "Data buku tidak lengkap."
    if any(buku['judul'] == judul for buku in books):
        return "Buku sudah ada."
    books.append({
        "judul": judul,
        "pengarang": pengarang,
        "tahun": tahun
    })
    return "Buku berhasil ditambahkan."


def daftar_buku():
    """Menampilkan semua buku yang tersimpan."""
    if not books:
        return "Belum ada buku."
    return books
