# Lat 5 Faktorial
n = int(input("Masukkan angka: "))
faktorial = 1
for i in range(1, n+1):
    faktorial *= i
print(f"{n}! = {faktorial}")