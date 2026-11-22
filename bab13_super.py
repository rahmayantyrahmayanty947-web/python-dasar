class Siswa:
    def __init__(self, nama, kelas):
        self.nama = nama
        self.kelas = kelas

    def info(self):
        print("Nama:", self.nama, "| Kelas:", self.kelas)

class SiswaBaru(Siswa):
    def __init__(self, nama, kelas, asal_sekolah):
        super().__init__(nama, kelas)
        self.asal_sekolah = asal_sekolah

    def info(self):
        super().info()
        print("Asal sekolah:", self.asal_sekolah)

rahma = SiswaBaru("Rahma", "XI RPL B", "SMPN 1 Subang")
rahma.info()