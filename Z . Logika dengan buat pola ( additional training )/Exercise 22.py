# Kategori Lanjutan: Pola Kompleks
# Latihan 22: Diamond Bintang
# Buat program yang mencetak bentuk berlian (diamond) setinggi N (N harus ganjil).
# Input: N = 5
# Output yang diharapkan:
# *
# ***
# *****
# ***
# *
# Petunjuk: Pecah masalah ini menjadi dua bagian. Buat satu for loop besar untuk mencetak piramida
# bagian atas, lalu buat for loop besar kedua untuk mencetak piramida terbalik di bagian bawah.

N = 5
tengah = N // 2                    # 5//2 = 2
# bagian atas termasuk tengah
for i in range(tengah + 1):        # i = 0..tengah
    jarak = tengah - i
    bintang = 2 * i + 1
    print(' ' * jarak + '*' * bintang)

# bagian bawah (tanpa baris tengah)
for i in range(tengah - 1, -1, -1):  # i = tengah-1 .. 0
    jarak = tengah - i
    bintang = 2 * i + 1
    print(' ' * jarak + '*' * bintang)
