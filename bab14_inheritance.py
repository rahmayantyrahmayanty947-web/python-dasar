class Pembayaran:
    def bayar(self, jumlah):
        print("Membayar", jumlah)

class Tunai(Pembayaran):
    def bayar(self, jumlah):
        print("Bayar tunai sebesar", jumlah)

class Transfer(Pembayaran):
    def bayar(self, jumlah):
        print("Bayar transfer sebesar", jumlah)

for metode in [Tunai(), Transfer()]:
    metode.bayar(36000)