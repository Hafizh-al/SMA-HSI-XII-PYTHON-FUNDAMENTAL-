# Latihan 2 (Game tebak angka)
angka_rahasia = 7
while True:
    tebakan = int(input("Tebak angka: "))
    if tebakan == angka_rahasia:
        print("Selamat, tebakan Anda benar!")
        break
    else:
        print("Salah, coba lagi.")
print("Terimakasih sudah bermain!")  
