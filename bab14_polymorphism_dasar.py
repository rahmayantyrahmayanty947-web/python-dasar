class Kucing:
    def suara(self):
        print("Meong")

class Anjing:
    def suara(self):
        print("Guk guk")

class Bebek:
    def suara(self):
        print("Kwek kwek")

for hewan in [Kucing(), Anjing(), Bebek()]:
    hewan.suara()