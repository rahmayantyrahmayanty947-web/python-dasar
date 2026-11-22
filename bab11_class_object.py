class Siswa:
    def __init__(self, nama, kelas):
        self.nama = nama
        self.kelas = kelas

    def sapa(self):
        print("Halo, saya", self.nama, "dari kelas", self.kelas)

rahma = Siswa("Rahma", "XI RPL B")
sinta = Siswa("Sinta", "XI RPL A")

rahma.sapa()
sinta.sapa()