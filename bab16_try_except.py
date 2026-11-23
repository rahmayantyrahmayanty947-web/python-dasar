try:
    hasil = 10 / 0
    print(hasil)
except ZeroDivisionError:
    print("Tidak bisa membagi dengan nol")

print("Program tetap berjalan")