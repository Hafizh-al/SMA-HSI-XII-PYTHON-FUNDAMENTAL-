# PERTEMUAN 11

# Latihan 1: Tampilkan Semua Uppercase
# Buat file puisi.txt. Tulis program yang:
# 1. Meminta pengguna memasukkan nama file (puisi.txt).
# 2. Membaca file tersebut baris per baris.
# 3. Mencetak setiap baris ke layar dalam format HURUF KAPITAL SEMUA.
nama_file = input("Masukkan nama file: ")
try:
    with open(nama_file) as f:
        for baris in f:
            print(baris.strip().upper())
except FileNotFoundError:
    print("File tidak ditemukan.")

