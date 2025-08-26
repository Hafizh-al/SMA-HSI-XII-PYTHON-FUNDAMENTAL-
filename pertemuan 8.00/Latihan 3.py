# Lat 3 Hitung Angka yang Habis Dibagi 3 & 5
jumlah = 0
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        jumlah += 1
print(f"Ada {jumlah} angka.")  