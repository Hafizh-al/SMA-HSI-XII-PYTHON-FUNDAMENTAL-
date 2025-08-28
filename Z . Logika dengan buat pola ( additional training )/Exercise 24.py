# Latihan 24: Pola Papan Catur
# Buat program yang mencetak pola papan catur berukuran N x N menggunakan karakter # dan .
# Input: N = 8
# Output yang diharapkan:
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# Petunjuk: Di dalam nested loop, gunakan if-else. Kuncinya ada pada posisi baris (i) dan kolom
# (j). Perhatikan bahwa karakter berubah jika i + j adalah genap atau ganjil. Gunakan operator
# modulo (%).

N = 8
for i in range(N):
    line = ''
    for j in range(N):
        if (i + j) % 2 == 0:
            line += '# '
        else:
            line += '  '    # 2 spasi agar kolom tetep rata
    print(line.rstrip())
            