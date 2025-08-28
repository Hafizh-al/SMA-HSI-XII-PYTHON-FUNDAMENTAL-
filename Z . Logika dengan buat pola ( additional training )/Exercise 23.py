# Latihan 23: Segitiga Huruf Alfabet
# Buat program yang mencetak segitiga yang berisi urutan huruf alfabet.
# Input: N = 5
# Output yang diharapkan:
# A
# AB
# ABC
# ABCD
# ABCDE
# Petunjuk: Kamu perlu mengonversi angka ke karakter. Gunakan fungsi chr() dan ord(). ord('A')
# akan memberimu nilai ASCII untuk 'A'. Kamu bisa menambahkan nilai loop j ke ord('A') lalu
# mengubahnya kembali ke karakter dengan chr().

N = 5
for i in range(1, N+1):
    line = ''
    for j in range(i):
        line += chr(ord('A') + j)
    print(line)
        