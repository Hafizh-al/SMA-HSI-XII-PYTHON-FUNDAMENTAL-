# Latihan 3: Easter Egg File
# Modifikasi program Latihan 1. Jika pengguna memasukkan nama file yang persis sama dengan "na na
# boo boo", program tidak boleh mencoba membuka file tersebut, melainkan harus mencetak pesan lucu:
# NA NA BOO BOO TO YOU - You have been punk'd! dan kemudian berhenti. Untuk semua input
# nama file lainnya, program harus berjalan normal (dan menangani FileNotFoundError jika file tidak ada).    
nama = input("Masukkan nama file: ")
if nama.lower() == 'na na boo boo':
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
else:
    try:
        with open(nama) as f:
            for baris in f:
                print(baris.strip().upper())
    except FileNotFoundError:
        print("File tidak ditemukan.")
        