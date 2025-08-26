# Latihan 1

def buat_email(nama_pengguna, domain="coding.com"):
    # Gabungkan nama pengguna dan domain, lalu ubah ke huruf kecil
    email = f"{nama_pengguna}@{domain}".lower()
    return email

# Contoh pemanggilan fungsi
print(buat_email("suli"))               # Output: suli@coding.com
print(buat_email("Anu", "belajar.id"))  # Output: anu@belajar.id


