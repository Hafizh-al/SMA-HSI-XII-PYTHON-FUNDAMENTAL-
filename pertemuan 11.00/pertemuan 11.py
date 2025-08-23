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

# Latihan 2: Hitung Rata-rata Spam Confidence
# Gunakan file mbox-short.txt dari www.py4e.com/code3/mbox-short.txt.
# Tulis program yang:
# -. Membaca file baris per baris.
# /. Mencari baris yang diawali dengan X-DSPAM-Confidence:.
# 0. Untuk setiap baris yang cocok, ekstrak angka desimal di akhir baris tersebut.
# 1. Hitung rata-rata dari semua angka yang berhasil diekstrak dan cetak hasilnya.
# Petunjuk: Gunakan .startswith() dan slicing string. Konversi hasil slicing ke float.    
fname = input("Masukkan nama file: ")
total = 0
count = 0

try:
    with open(fname) as f:
        for line in f:
            if line.startswith("X-DSPAM-Confidence:"):
                num = float(line.strip().split(':')[-1])
                total += num
                count += 1
    print(f"Rata-rata spam confidence: {total / count:.4f}")
except FileNotFoundError:
    print("File tidak ditemukan.")

# Latihan 3: Easter Egg File
# Modifikasi program Latihan 1. Jika pengguna memasukkan nama file yang persis sama dengan "na na
# boo boo", program tidak boleh mencoba membuka file tersebut, melainkan harus mencetak pesan lucu:
# NA NA BOO BOO TO YOU - You have been punk'd! dan kemudian berhenti. Untuk semua input
# nama file lainnya, program harus berjalan normal (dan menangani FileNotFoundError jika file tidak ada).    
nama = input("Masukkan nama file: ")
if nama.lower() == 'na na boo boo':
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
else:
    try:
        with open(nama) as f:
            for baris in f:
                print(baris.strip().upper())
    except FileNotFoundError:
        print("File tidak ditemukan.")
        