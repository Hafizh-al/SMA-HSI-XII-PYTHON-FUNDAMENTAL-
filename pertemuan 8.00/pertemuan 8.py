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

