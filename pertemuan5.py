# Latihan 1:
 # Fungsi tanpa parameter
def salam_pembuka(): # Kata kunci untuk membuat fungsi baru
    print("==============================")
    print("Selamat Datang di Program Saya!")
    print("==============================")

 # Memanggil fungsi beberapa kali
salam_pembuka()
salam_pembuka()

# Latihan 2
def info_cuaca(kota, cuaca):
    print(f"Cuaca di kota {kota} hari ini {cuaca}.")  # f = Ini adalah f-string, format string agar bisa menyisipkan variabel ke dalam teks

info_cuaca("Jakarta", "berawan")

# Latihan 3
  # Fungsi dengan return
def kubik(angka):
    return angka ** 3  # Mengembalikan angka pangkat 3

  # Memanggil fungsi dan menyimpan hasilnya ke variabel
hasil_kubik = kubik(4)

  # Mencetak hasil
print(hasil_kubik)

# Latihan 4
  # 1. Fungsi hitung_diskon
def hitung_diskon(harga_awal, persen_diskon):
    jumlah_diskon = harga_awal * (persen_diskon / 100)
    harga_akhir = harga_awal - jumlah_diskon
    return harga_akhir
# Input dari pengguna
try:
    harga = float(input("Masukkan harga barang"))
    diskon = float(input("Masukkan persen diskon(misal: 20 untuk 20%): "))
    # Panggil fungsi dan cetak hasil
    total_bayar = hitung_diskon(harga, diskon)
    print(f"Harga setelah diskon: {total_bayar:.2f}")

except ValueError:
    print("Error: Masukkan angka yang benar untuk harga dan diskon")

# Latihan 5
# 1. Fungsi fruitful: Mengembalikan hasil perhitungan
def fahrenheit_ke_celsius(temp_f):
    temp_c = (temp_f - 32) * 5/9
    return temp_c

# 2. Panggil fungsi dengan nilai 98.6 dan simpan hasilnya
hasil = fahrenheit_ke_celsius(98.6)

# 3. Cetak hasil konversi
print(f"98.6 derajat Fahrenheit = {hasil:.2f} derajat Celsius")
