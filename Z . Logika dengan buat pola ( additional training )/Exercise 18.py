# Latihan 18: Segitiga Siku-Siku Terbalik
# Buat program yang mencetak segitiga siku-siku terbalik setinggi N.
# Input: N = 5
# Output yang diharapkan:
# *****
# ****
# ***
# **
# *
# Petunjuk: Gunakan range() dengan langkah mundur (misalnya range(N, 0, -1)).

N = 5
for i in range(N, 0, -1):   # mulai di N, berhenti sebelum 0 (jadi terakhir 1), langkahnya -1 (mundur).
    print('*' * i)
