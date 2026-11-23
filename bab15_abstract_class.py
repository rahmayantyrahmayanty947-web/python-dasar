from abc import ABC, abstractmethod

class Hewan(ABC):
    @abstractmethod
    def suara(self):
        pass

class Kucing(Hewan):
    def suara(self):
        print("Meong")

class Anjing(Hewan):
    def suara(self):
        print("Guk guk")

Kucing().suara()
Anjing().suara()

try:
    hewan = Hewan()
except TypeError:
    print("Kelas abstrak tidak bisa dibuat objeknya")