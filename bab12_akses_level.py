class Siswa:
    def __init__(self, nama, alamat, saldo):
        self.nama = nama
        self._alamat = alamat
        self.__saldo = saldo

    def lihat_saldo(self):
        return self.__saldo

rahma = Siswa("Rahma", "Subang", 50000)

print(rahma.nama)
print(rahma._alamat)
print(rahma.lihat_saldo())

try:
    print(rahma.__saldo)
except AttributeError:
    print("Atribut private tidak bisa diakses langsung")