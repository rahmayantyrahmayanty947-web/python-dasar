def cetak_suara(hewan):
    hewan.suara()

class Kucing:
    def suara(self):
        print("Meong")

cetak_suara(Kucing())

print(len("seblak"))
print(len(["kerupuk", "bakso", "sosis"]))
print(len({"nama": "Rahma", "kelas": "XI RPL B"}))