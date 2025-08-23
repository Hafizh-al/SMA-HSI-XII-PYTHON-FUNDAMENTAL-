# Waktunya mempraktikkan kemampuan baru program kita untuk berpikir!
# Latihan 1: 

# Input dari pengguna
jam = float(input("Masukkan jumlah jam kerja: "))
tarif = float(input("Masukkan tarif per jam: "))

# Menghitung upah
if jam <= 40:
    upah = jam * tarif
else:
    jam_normal = 40
    jam_lembur = jam - 40
    upah = (jam_normal * tarif) + (jam_lembur * tarif * 1.5)

# Output hasil
print("Pay:", upah)

# Latihan 2

try:
    jam = float(input("Masukkan jumlah jam kerja: "))
    tarif = float(input("Masukkan tarif per jam: "))

    if jam <= 40:
        upah = jam * tarif
    else:
        jam_lembur = jam - 40
        upah = (40 * tarif) + (jam_lembur * tarif * 1.5)

    print("Pay:", upah)

except ValueError:
    print("Error, please enter numeric input")

# Latihan 3

try:
    skor = float(input("Masukkan skor (antara 0.0 sampai 1.0): "))

    if skor < 0.0 or skor > 1.0:
        print("Bad score")  # Jika nilai di luar rentang 0.0–1.0
    else:
        if skor >= 0.9:
            print("Grade: A")
        elif skor >= 0.8:
            print("Grade: B")
        elif skor >= 0.7:
            print("Grade: C")
        elif skor >= 0.6:
            print("Grade: D")
        else:
            print("Grade: F")

except ValueError:
    print("Error, please enter numeric input")

# Latihan 4

# latihan 4 di tb.py

