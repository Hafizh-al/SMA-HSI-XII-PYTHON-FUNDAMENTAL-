# Latihan 3: Sensor Kata
# Buat program yang memiliki sebuah kalimat dan sebuah kata yang ingin disensor. Program harus mengganti
# semua kemunculan kata terlarang itu dengan tanda bintang ***.
# Contoh: kalimat = "Harga tiketnya sangat mahal.", kata_sensor = "mahal".
# Output yang diharapkan: "Harga tiketnya sangat ***."
kalimat = "Harga tiket sangat mahal"
kalimat_sensor = kalimat.replace("mahal", "***")
print(kalimat_sensor)
