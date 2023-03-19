from Mahasiswa import Mahasiswa

class PengurusBEM: 
    __pengurus = Mahasiswa()
    __jabatan = ""
    __rancanganProker = ""
    __statusProker = 0

    def __init__(self):
        self.pengurus = Mahasiswa()
        self.jabatan = ""
        self.rancanganProker =""
        self.statusProker = 0

    def setPengurus(self, a):
        self.pengurus = a
    def setJabatan(self, a):
        self.jabatan = a
    def merancangProker(self, a):
        self.rancanganProker = a
        self.statusProker = 0
        print(self.pengurus.getNama()+" Sedang Merancang proker "+a)
    def menjalankanProker(self):
        print(self.pengurus.getNama()+(" Sudah menjalankan proker "+self.getRancanganProker()))
        self.rancanganProker = ""
        self.statusProker = 1
    
    def getPengurus(self):
        return self.pengurus
    def getJabatan(self):
        return self.jabatan
    def getRancanganProker(self):
        return self.rancanganProker
    def getStatusProker(self):
        return self.statusProker
    
    

