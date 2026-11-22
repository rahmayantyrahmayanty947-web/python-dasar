def perkenalan(nama, kelas="XI RPL B"):
    print("Nama:", nama)
    print("Kelas:", kelas)

def total_bayar(porsi, harga):
    return porsi * harga

perkenalan("Rahma")
perkenalan("Sinta", "XI RPL A")
print("Total:", total_bayar(3, 12000))
print("Total:", total_bayar(harga=15000, porsi=2))