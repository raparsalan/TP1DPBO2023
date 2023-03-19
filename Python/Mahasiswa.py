from Human import Human
from Laptop import Laptop
from BukuTulis import BukuTulis

class Mahasiswa(Human): 
    __nim = ""
    __nilai = ""
    __laptopMahasiswa = Laptop()
    __bukuMahasiswa = BukuTulis()

    def __init__(self):
        super(Mahasiswa, self).__init__()
        self.nim = ""
        self.nilai = ""
        self.laptopMahasiswa = Laptop()
        self.bukuMahasiswa = BukuTulis()

    def setNim(self, a):
        self.nim = a
    def setNilai(self, a):
        self.nilai = a
    def setLaptop(self, a):
        self.laptopMahasiswa = a
    def setBukuTulis(self, a):
        self.bukuMahasiswa = a
    
    def getNim(self):
        return self.nim
    def getNilai(self):
        return self.nilai
    def getLaptop(self):
        return self.laptopMahasiswa
    def getBukuTulis(self):
        return self.bukuMahasiswa
    
    

