hitung = 3
while hitung > 0:
    print("Hitung mundur:", hitung)
    hitung -= 1
print("Seblak matang!")

for angka in range(1, 10):
    if angka == 3:
        continue
    if angka == 6:
        break
    print("Angka:", angka)