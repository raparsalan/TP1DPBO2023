from Human import Human
from Laptop import Laptop
from Spidol import Spidol
from Asprak import Asprak
from Mahasiswa import Mahasiswa
class Dosen(Human): 
    __nip = ""
    __pendTerakhir = ""
    __laptopDosen = Laptop()
    __spidolDosen = Spidol()

    def __init__(self):
        super(Dosen, self).__init__()
        self.nip = ""
        self.pendTerakhir =""
        self.laptopDosen = Laptop()
        self.spidolDosen = Spidol()

    def setNip(self, a):
        self.nip = a
    def setPendTerakhir(self, a):
        self.pendTerakhir = a
    def setLaptop(self, a):
        self.laptopDosen = a
    def setSpidol(self, a):
        self.spidolDosen = a

    def getLaptop(self):
        return self.laptopDosen
    def getSpidol(self):
        return self.spidolDosen
    def getNip(self):
        return self.nip
    def getPendTerakhir(self):
        return self.pendTerakhir
    def memberiNilai(self, a:Mahasiswa, b:Asprak, c):
        if(b.statusTugas == 1):
            if(self.getJk() == "P"):
                print("Ibu "+self.getNama()+" Telah memberikan nilai "+c+" untuk tugas "+b.getTugas()+" milik "+ a.getNama())
            elif(self.getJk() == 'L'):
                print("Bapak "+self.getNama()+" Telah memberikan nilai "+c+" untuk tugas "+b.getTugas()+" milik "+ a.getNama())
            b.tugasDinilai()
        else:
            print("Ooppss asprak " + b.getAsisten().getNama() + " Belum memberikan tugas apapun")        
    

