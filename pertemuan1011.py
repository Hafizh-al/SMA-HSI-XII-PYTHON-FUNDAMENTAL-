# Pertemuan 10

# Latihan 1: Standardisasi Judul
# Buat program yang meminta pengguna memasukkan judul buku yang mungkin diketik dengan huruf
# besar/kecil yang acak (misal: "aLaDiN dan LaMPu aJAib"). Programmu harus membersihkan spasi ekstra di
# awal/akhir dan mengubahnya ke format Title Case yang benar.
judul = "aLaDiN dan LaMPu aJAib"
judul_baru = judul.strip().title()
print(judul_baru)

# Latihan 2: Validasi Email Sederhana
# Buat program yang meminta pengguna memasukkan alamat email. Program harus melakukan dua
# pengecekan sederhana:
# 1. Apakah email mengandung karakter @? (Gunakan find() atau operator in).
# 2. Apakah email diakhiri dengan .com atau .co.id? (Gunakan .endswith()).
# Cetak pesan "Email valid" atau "Email tidak valid" berdasarkan hasil pengecekan.
email = "h4f1zh2838@gmail.com"
if email.find("@") != -1 and (email.endswith(".com") or email.endswith(".co.id")):
    print("Email valid")
else:
    print("Email tak valid")    

# Latihan 3: Sensor Kata
# Buat program yang memiliki sebuah kalimat dan sebuah kata yang ingin disensor. Program harus mengganti
# semua kemunculan kata terlarang itu dengan tanda bintang ***.
# Contoh: kalimat = "Harga tiketnya sangat mahal.", kata_sensor = "mahal".
# Output yang diharapkan: "Harga tiketnya sangat ***."
kalimat = "Harga tiket sangat mahal"
kalimat_sensor = kalimat.replace("mahal", "***")
print(kalimat_sensor)

# Latihan 4: Akronim Generator
# Buat program yang meminta pengguna memasukkan sebuah nama organisasi yang panjang (misal: "Badan
# Usaha Milik Negara"). Program harus:
# 1. Memecah input menjadi list kata-kata.
# 2. Mengambil huruf pertama dari setiap kata.
# 3. Menggabungkan huruf-huruf pertama tersebut menjadi satu string akronim dalam huruf kapital.
# Output yang diharapkan: "BUMN"
kalimat = "Badan Usaha Milik Negara"
akronim = ''.join([kata[0] for kata in kalimat.split()]).upper()
print(akronim)

# Latihan 5: URL Slug Generator
# Di dunia web, "slug" adalah versi URL-friendly dari sebuah judul artikel. Buat program yang mengubah judul
# artikel menjadi slug. Aturannya:
# 1. Ubah semua huruf menjadi kecil.
# 2. Ganti semua spasi dengan tanda hubung (-).
# 3. (Bonus) Hapus semua karakter selain huruf, angka, dan tanda hubung.
# Contoh: judul = "10 Tips Jitu Belajar Python!"
# Output yang diharapkan: "10-tips-jitu-belajar-python"
judul = "10 Tips Jitu Belajar Python!"
URL_Slug_Generator = judul.lower().replace(" ", "-").replace("!", "")
print(URL_Slug_Generator)

import re
judul = "10 Tips Jitu Belajar Python!"
slug = re.sub(r'[^a-z0-9\s-]', '', judul.lower())  # hapus karakter selain huruf, angka, spasi
slug = slug.replace(" ", "-")
print(slug)
# Output: 10-tips-jitu-belajar-python

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
        