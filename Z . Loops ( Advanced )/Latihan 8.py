# Latihan 8: Iterasi String dengan continue
# Buat program yang meminta pengguna memasukkan sebuah kalimat. Program akan mencetak ulang kalimat
# tersebut huruf per huruf, tetapi semua huruf vokal (a, i, u, e, o, baik besar maupun kecil) akan
# dilewati (tidak dicetak).
# Gunakan for loop untuk mengiterasi setiap huruf dalam kalimat.
# Gunakan if dan continue untuk melewati huruf vokal.
# Contoh Input: "Saya Belajar Python"
# Contoh Output: Sy Bljr Pythn

kalimat = input("Masukkan kalimat: ")
vokal = "aiueoAIUEO"
hasil = ""
for k in kalimat:
    if k in vokal:
        continue
    hasil += k
print(hasil)
    