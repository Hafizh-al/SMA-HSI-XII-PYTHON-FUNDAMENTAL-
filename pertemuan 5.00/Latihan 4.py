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
