from abc import ABC, abstractmethod

class Pembayaran(ABC):
    @abstractmethod
    def bayar(self, jumlah):
        pass

class Gopay(Pembayaran):
    def bayar(self, jumlah):
        print("Bayar", jumlah, "lewat Gopay")

class Dana(Pembayaran):
    def bayar(self, jumlah):
        print("Bayar", jumlah, "lewat Dana")

for metode in [Gopay(), Dana()]:
    metode.bayar(36000)