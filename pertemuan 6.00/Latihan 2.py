# Latihan 2
def kirim_paket(barang, tujuan, berat_kg, asuransi=False, express=False):
    print(f"Mengirim {barang} ke {tujuan}, Berat: {berat_kg}kg, Asuransi: {asuransi}, Express: {express}")

# Memanggil fungsi menggunakan keyword arguments
kirim_paket(barang="Buku", tujuan="Bandung", berat_kg=2, express=True)
