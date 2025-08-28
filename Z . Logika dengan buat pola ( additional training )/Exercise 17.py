# Latihan 17: Segitiga Siku-Siku
# Buat program yang mencetak segitiga siku-siku seperti di bawah ini setinggi N.
# Input: N = 5
# Output yang diharapkan:
# *
# **
# ***
# ****
# *****
# Petunjuk: Jumlah bintang yang dicetak di setiap baris bergantung pada nomor baris saat ini.
# Gunakan variabel dari loop luar untuk mengontrol batas dari loop dalam

N = 5
for i in range(1, N+1):
    for j in range(i):
        print('*', end='')
    print()    