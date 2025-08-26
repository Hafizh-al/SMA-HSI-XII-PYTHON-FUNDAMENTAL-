# Latihan 4: Akronim Generator
# Buat program yang meminta pengguna memasukkan sebuah nama organisasi yang panjang (misal: "Badan
# Usaha Milik Negara"). Program harus:
# 1. Memecah input menjadi list kata-kata.
# 2. Mengambil huruf pertama dari setiap kata.
# 3. Menggabungkan huruf-huruf pertama tersebut menjadi satu string akronim dalam huruf kapital.
# Output yang diharapkan: "BUMN"
kalimat = "Badan Usaha Milik Negara"
akronim = ''.join([kata[0] for kata in kalimat.split()]).upper()
print(akronim)
