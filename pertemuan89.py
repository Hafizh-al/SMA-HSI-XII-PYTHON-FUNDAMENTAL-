# Pertemuan 8
# Lat 1 cetak kelipatan 7(0-70)
for a in range(0, 71, 7):
    print(a)

# Lat 2 Balik String
kata = "Python"
kata_terbalik = ""
for huruf in kata:
    kata_terbalik = huruf + kata_terbalik
print(kata_terbalik)  # nohtyP    

# Lat 3 Hitung Angka yang Habis Dibagi 3 & 5
jumlah = 0
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        jumlah += 1
print(f"Ada {jumlah} angka.")        

# Lat 4 Pola Segitiga Terbalik
for i in range(5, 0, -1):
    print("*" * i)

# Lat 5 Faktorial
n = int(input("Masukkan angka: "))
faktorial = 1
for i in range(1, n+1):
    faktorial *= i
print(f"{n}! = {faktorial}")

# Pertemuan 9

# Lat 1-Ahli Indexing
s = "Belajar Python itu Menyenangkan"
print(s[0])   # Karakter pertama: 'B'
print(s[-1])  # Karakter terakhir: 'n'
print(s[7])   # Spasi pertama

# Lat 2-Master Slicing
print(s[8:14])   # "Python"
print(s[-12:])   # "Menyenangkan"
print(s[:7])     # "Belajar"

# Lat 3-Membalikkan Kata+Palindrom Check
kata = input("Masukkan kata: ")
terbalik = kata[::-1]
print(f"Dibalik: {terbalik}")
if kata == terbalik:
    print("Ini Palindrom!")
else:
    print("Bukan Palindrom.")

# Lat 4-Kode Rahasia
kode = "BPrOaGikRtoAdMiItMuINtuGhpPyYcThHoOnN"
rahasia = kode[::3]
print("Kode rahasia:", rahasia)

# Lat 5-Memperbaiki Nama Tanpa Method
nama_salah = "dUDI sANTOSO"   
nama_benar = "B" + nama_salah[1:4].lower() + "  " + nama_salah[5].upper() + nama_salah[6:].lower()
print(nama_benar)   # Output: Budi Santoso
