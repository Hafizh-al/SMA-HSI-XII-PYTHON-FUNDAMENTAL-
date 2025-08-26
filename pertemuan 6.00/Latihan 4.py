# latihan 4
def analisis_daftar(daftar_angka):
    """
    Menganalisis daftar angka untuk mendapatkan total, jumlah elemen, dan rata-rata.

    Args:
        daftar_angka (list of int or float): Daftar angka yang ingin dianalisis.

    Returns:
        tuple: Berisi tiga nilai:
            - Total (int/float): Jumlah semua angka.
            - Jumlah Elemen (int): Banyaknya elemen dalam daftar.
            - Rata-rata (float): Nilai rata-rata dari semua angka.
    """
    total = sum(daftar_angka)
    jumlah_elemen = len(daftar_angka)
    rata_rata = total / jumlah_elemen
    return total, jumlah_elemen, rata_rata

# Mengecek dokumentasi
help(analisis_daftar)
