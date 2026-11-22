class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def makan(self):
        print(self.nama, "sedang makan")

class Burung(Hewan):
    def terbang(self):
        print(self.nama, "terbang tinggi")

burung = Burung("Kenari")
burung.makan()
burung.terbang()