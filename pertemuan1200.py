# LAT 1
# Nama file log
nama_file = "log_kegiatan.txt"

# Minta pengguna mengetik kegiatan
kegiatan = input("Apa kegiatan yang baru saja kamu lakukan? ")

# Simpan ke file (mode append)
with open(nama_file, 'a') as file:
    file.write(kegiatan + '\n')

print("Kegiatan berhasil disimpan ke log!")

# LAT 2
# Nama file sumber dan tujuan
sumber = "sumber.txt"
tujuan = "salinan.txt"

# Buka file sumber dan baca isinya
with open(sumber, 'r') as file_sumber:
    isi = file_sumber.read()

# Tulis isi ke file tujuan
with open(tujuan, 'w') as file_tujuan:
    file_tujuan.write(isi)

print(f"File '{sumber}' berhasil disalin ke '{tujuan}'!")

# LAT 3
import os

# Minta nama file dari pengguna
nama_file = input("Masukkan nama file yang ingin dihapus: ")

# Cek keberadaan file
if os.path.exists(nama_file):
    konfirmasi = input(f"Anda yakin ingin menghapus '{nama_file}'? (y/n): ")
    if konfirmasi.lower() == 'y':
        os.remove(nama_file)
        print("File berhasil dihapus.")
    else:
        print("Penghapusan dibatalkan.")
else:
    print(f"File '{nama_file}' tidak ditemukan.")
