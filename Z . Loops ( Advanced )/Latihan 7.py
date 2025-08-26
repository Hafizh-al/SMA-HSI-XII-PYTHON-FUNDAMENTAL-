# Latihan 7: Pola Akumulator dengan while
# Buat program untuk menghitung jumlah kuadrat dari N bilangan bulat pertama.
# -. Minta pengguna memasukkan sebuah angka N.
# /. Gunakan while loop untuk menghitung 1² + 2² + 3² + ... + N².
# 0. Cetak hasil akhirnya.
# Contoh Input: N = 3
# Output yang diharapkan: Jumlah kuadrat dari 3 bilangan pertama adalah: 14 (karena 11 +
# 22 + 3*3 = 1 + 4 + 9 = 14).

N = int(input("Masukkan N: "))
i = 1
total = 0
while i <= N:
    total += i * i
    i += 1
print(f"Jumlah kuadrat dari {N} bilangan pertama adalah: {total}")    