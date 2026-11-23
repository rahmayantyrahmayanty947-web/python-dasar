file = open("data.txt", "r")
isi = file.read()
file.close()
print(isi)

file = open("data.txt", "r")
for baris in file:
    print("Baris:", baris.strip())
file.close()