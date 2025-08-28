# Latihan 25: Piramida Angka Palindromik
# Buat program yang mencetak piramida angka yang simetris.
# Input: N = 5
# Output yang diharapkan:
# 1
# 121
# 12321
# 1234321
# 123454321
# Petunjuk: Ini adalah yang paling menantang. Setiap baris terdiri dari tiga bagian: spasi, urutan angka
# naik, dan urutan angka turun. Kamu mungkin perlu tiga loop terpisah di dalam loop baris utama: satu
# untuk spasi, satu untuk angka naik, dan satu untuk angka turun.

N = 5
for i in range(1, N+1):
    jarak = N - i
    kiri = ''.join(str(j) for j in range(1, i+1))
    kanan = ''.join(str(j) for j in range(i-1, 0, -1)) 
    print(' ' * jarak + kiri + kanan)
    