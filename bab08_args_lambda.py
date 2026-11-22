def jumlah(*angka):
    return sum(angka)

def tampil_profil(**data):
    for kunci, nilai in data.items():
        print(kunci, ":", nilai)

kuadrat = lambda x: x * x

print(jumlah(1, 2, 3, 4))
tampil_profil(nama="Rahma", hobi="memasak")
print(kuadrat(6))