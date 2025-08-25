# Latihan 5
# 1. Fungsi fruitful: Mengembalikan hasil perhitungan
def fahrenheit_ke_celsius(temp_f):
    temp_c = (temp_f - 32) * 5/9
    return temp_c

# 2. Panggil fungsi dengan nilai 98.6 dan simpan hasilnya
hasil = fahrenheit_ke_celsius(98.6)

# 3. Cetak hasil konversi
print(f"98.6 derajat Fahrenheit = {hasil:.2f} derajat Celsius")
