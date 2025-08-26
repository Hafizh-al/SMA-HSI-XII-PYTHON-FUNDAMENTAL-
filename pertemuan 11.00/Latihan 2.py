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