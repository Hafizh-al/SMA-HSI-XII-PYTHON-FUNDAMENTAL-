# Latihan 9: Mencari Bilangan Prima Pertama
# Buat program untuk menemukan dan mencetak 5 bilangan prima pertama setelah angka 1. Bilangan prima
# adalah bilangan yang hanya bisa dibagi oleh 1 dan dirinya sendiri.
# Gunakan while loop luar untuk memastikan kamu sudah menemukan 5 bilangan prima.
# Gunakan for loop di dalamnya untuk mengecek apakah sebuah angka bisa dibagi oleh angka lain
# selain 1 dan dirinya sendiri.
# Kamu akan butuh sebuah "flag" (variabel boolean) untuk menandai apakah sebuah angka prima atau
# tidak.
# Output yang diharapkan:
# 2
# 3
# 5
# 7
# 11

import math

count = 0
n = 2
while count < 5:
    prima = True
    for d in range(2, int(math.sqrt(n)) + 1):
        if n % d == 0:
            prima = False
            break
    if prima:
        print(n)
        count += 1
    n += 1
