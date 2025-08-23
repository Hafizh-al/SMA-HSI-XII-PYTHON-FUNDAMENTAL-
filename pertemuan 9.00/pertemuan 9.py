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
