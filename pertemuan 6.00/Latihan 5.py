# Latihan 5
# Versi biasa
def get_luas_lingkaran(radius):
    return 3.14159 * (radius ** 2)

# Versi lambda
luas_lingkaran_lambda = lambda radius: 3.14159 * (radius ** 2)

# Uji coba
print(luas_lingkaran_lambda(7))  # Output: 153.93791
