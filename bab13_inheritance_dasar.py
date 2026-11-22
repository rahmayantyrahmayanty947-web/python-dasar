class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def suara(self):
        print("Suara hewan")

class Kucing(Hewan):
    def suara(self):
        print(self.nama, "berkata: Meong")

class Anjing(Hewan):
    def suara(self):
        print(self.nama, "berkata: Guk guk")

kucing = Kucing("Mimi")
anjing = Anjing("Doggo")

kucing.suara()
anjing.suara()