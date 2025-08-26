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


