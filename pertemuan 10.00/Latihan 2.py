# Latihan 2: Validasi Email Sederhana
# Buat program yang meminta pengguna memasukkan alamat email. Program harus melakukan dua
# pengecekan sederhana:
# 1. Apakah email mengandung karakter @? (Gunakan find() atau operator in).
# 2. Apakah email diakhiri dengan .com atau .co.id? (Gunakan .endswith()).
# Cetak pesan "Email valid" atau "Email tidak valid" berdasarkan hasil pengecekan.
email = "h4f1zh2838@gmail.com"
if email.find("@") != -1 and (email.endswith(".com") or email.endswith(".co.id")):
    print("Email valid")
else:
    print("Email tak valid")    
