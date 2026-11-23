with open("contoh.txt", "w") as f:
    f.write("Seblak pedas level 5\n")
    f.write("Harga 12000\n")

with open("contoh.txt", "r") as f:
    for baris in f:
        print(baris.strip())