# Latihan 10: for-else untuk Pengecekan Password
# Simulasikan sebuah sistem yang mengecek apakah sebuah password mengandung karakter terlarang.
# -. Buat variabel password = "katasandi123" dan karakter_terlarang = "$%&".
# /. Gunakan for loop untuk memeriksa setiap karakter di password.
# 0. Di dalam loop, gunakan if untuk mengecek apakah karakter tersebut ada di
# karakter_terlarang. Jika ada, cetak "Password mengandung karakter terlarang!" dan gunakan
# break.
# 1. Gunakan blok else setelah for loop. Blok ini hanya akan berjalan jika break tidak pernah
# dieksekusi, yang artinya password aman. Cetak "Password aman." di dalam else.
# (Coba ubah password menjadi "kata$andi" dan lihat perbedaannya)

password = "kata$andi"  # coba ganti "kata$andi"
karakter_terlarang = "$%&"

for ch in password:
    if ch in karakter_terlarang:
        print("Password mengandung karakter terlarang!")
        break
else:
    print("Password aman.")
