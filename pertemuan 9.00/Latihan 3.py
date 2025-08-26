# Lat 3-Membalikkan Kata+Palindrom Check
kata = input("Masukkan kata: ")
terbalik = kata[::-1]
print(f"Dibalik: {terbalik}")
if kata == terbalik:
    print("Ini Palindrom!")
else:
    print("Bukan Palindrom.")
