# Latihan 6: Validasi Input dengan while
# Buat program yang meminta pengguna memasukkan umur mereka. Program harus terus meminta input
# selama pengguna memasukkan nilai yang tidak valid (bukan angka atau angka di luar rentang wajar, misal <
# 0 atau > 100). Gunakan while True loop, try-except untuk menangani ValueError, dan if untuk
# mengecek rentang. Jika input sudah valid, cetak umur tersebut dan hentikan loop dengan break.

while True:
    raw = input("Masukkan umur lu: ")
    try:
        umur = int(raw)
    except ValueError:
        print("Input tidak valid. Masukin angka!.")
        continue

    if umur < 0 or umur > 100:
        print("umur segitu ngga dianggep di sini , di sini buat umur 0-100")    
        continue
    print(f"Syukron. Jadi umur Anda {umur} tahun.")
    break