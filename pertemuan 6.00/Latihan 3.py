# Latihan 3
def analisis_daftar(daftar_angka):
    total = sum(daftar_angka)
    jumlah_elemen = len(daftar_angka)
    rata_rata = total / jumlah_elemen
    return total, jumlah_elemen, rata_rata

# Memanggil dan unpack hasil
hasil_total, jumlah, rata = analisis_daftar([10, 20, 30, 40, 50])
print(f"Total: {hasil_total}, Jumlah Elemen: {jumlah}, Rata-rata: {rata}")
