from Mahasiswa import Mahasiswa

class Asprak: 
    __asisten = Mahasiswa()
    __namaMatkul = ""
    __tugas = ""
    __statusTugas = 0

    def __init__(self):
        self.asisten = Mahasiswa()
        self.namaMatkul = ""
        self.statusTugas = 0
        self.tugas = ""

    def setAsisten(self, a):
        self.asisten = a
    def setNamaMatkul(self, a):
        self.namaMatkul = a
    def memberiTugas(self, a):
        self.tugas = a
        print(self.getAsisten().getNama()+" Sudah memberikan tugas "+self.getTugas())
        self.statusTugas = 1
    def tugasDinilai(self):
        self.tugas = ""
        self.statusTugas = 0
    
    def getAsisten(self):
        return self.asisten
    def getMatkul(self):
        return self.namaMatkul
    def getStatusTugas(self):
        return self.statusTugas
    def getTugas(self):
        return self.tugas
    
    

