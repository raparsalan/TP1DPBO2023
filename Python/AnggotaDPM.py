from Mahasiswa import Mahasiswa
from PengurusBEM import PengurusBEM

class AnggotaDPM: 
    __anggota = Mahasiswa()
    __jabatan = ""

    def __init__(self):
        self.anggota = Mahasiswa()
        self.jabatan = ""

    def setAnggota(self, a):
        self.anggota = a
    def setJabatan(self, a):
        self.jabatan = a
    
    def getAnggota(self):
        return self.anggota
    def getJabatan(self):
        return self.jabatan
    def monitoringBEM(self, a:PengurusBEM):
        print(self.anggota.getNama() + " Sedang mengawasi kerja "+ a.getPengurus().getNama())
    def apresiasi(self, a:PengurusBEM):
        if(a.getStatusProker() == 1):
            print(self.getAnggota().getNama()+ " Berkata 'Mau apresiasi dulu buat " + a.getPengurus().getNama()+" udah beresin prokernya'")
        else:
            print("Ooopss "+a.getPengurus().getNama()+" belum menjalankan prokernya")

