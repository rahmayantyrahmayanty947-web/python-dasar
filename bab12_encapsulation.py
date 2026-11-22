class Tabungan:
    def __init__(self, saldo):
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo

    def setor(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah

    def tarik(self, jumlah):
        if 0 < jumlah <= self.__saldo:
            self.__saldo -= jumlah
        else:
            print("Saldo tidak cukup")

tabungan = Tabungan(10000)
tabungan.setor(5000)
print(tabungan.get_saldo())
tabungan.tarik(3000)
print(tabungan.get_saldo())
tabungan.tarik(50000)
print(tabungan.get_saldo())