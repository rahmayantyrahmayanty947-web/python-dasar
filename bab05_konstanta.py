HARGA_SEBLAK = 12000
PAJAK_PERSEN = 10
NAMA_WARUNG = "Warung Rahma"

porsi = 3
subtotal = HARGA_SEBLAK * porsi
total = subtotal + subtotal * PAJAK_PERSEN // 100

print(NAMA_WARUNG)
print("Subtotal:", subtotal)
print("Total dengan pajak:", total)