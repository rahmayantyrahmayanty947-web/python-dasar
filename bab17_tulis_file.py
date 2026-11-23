file = open("data.txt", "w")
file.write("Nama: Rahma\n")
file.write("Kelas: XI RPL B\n")
file.close()

file = open("data.txt", "a")
file.write("Hobi: memasak\n")
file.close()

print("File data.txt berhasil dibuat")