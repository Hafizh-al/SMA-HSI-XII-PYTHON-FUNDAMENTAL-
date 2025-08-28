# Latihan 16: Persegi Bintang Solid
# Buat program yang mencetak persegi solid yang terdiri dari bintang (*) berukuran N x N.
# Input: N = 5
# Output yang diharapkan:
# *****
# *****
# *****
# *****
# Petunjuk: Kamu akan butuh dua for loop yang bersarang (nested). Loop luar untuk baris, loop
# dalam untuk kolom.

N = 3
for i in range(N):
    for j in range(N):
        print('*', end='') # end='' mencegah newline tiap print
    print()                # setelah selesai kolom , pindah baris    
