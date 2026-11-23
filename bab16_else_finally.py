try:
    angka = int("22")
except ValueError:
    print("Bukan angka")
else:
    print("Berhasil diubah:", angka)
finally:
    print("Selesai memeriksa")

try:
    angka = int("seblak")
except ValueError:
    print("Bukan angka")
finally:
    print("Selesai memeriksa lagi")