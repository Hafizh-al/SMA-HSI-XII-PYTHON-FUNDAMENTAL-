# MATERI PERTEMUAN 7
# Latihan 1 (Countdown sederhana)
count = 10
while count > 0:
    print(count)
    count -= 1
print("Blastoff")  

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

# Latihan 3 (input angka cerdas)
total = 0
count = 0

while True:
    data = input("Masukkan angka (atau 'done'): ")
    if data == "done":
        break
    try:
        angka = float(data)
        total += angka
        count += 1
    except:
        print("Input tidak valid")
        continue


if count > 0:
    print(f"Total: {total}, Jumlah: {count}, Rata rata: {total / count}")


