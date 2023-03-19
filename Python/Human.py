class Human: 
    __nik = ""
    __nama  = ""
    __jk= ""
    __statusTidur = 0

    def __init__(self):
        self.nik = ""
        self.nama = ""
        self.jk = ""
        self.statusTidur = 0

    def setNik(self, a):
        self.nik = a
    def setNama(self, a):
        self.nama = a
    def setJk(self, a):
        self.jk = a
    
    def getNik(self):
        return self.nik
    def getNama(self):
        return self.nama
    def getJk(self):
        return self.jk
    
    def makan(self, a):
        if(self.statusTidur == 1):
            print("Oopss "+self.nama+" masih tidur dan tidak bisa makan")
        else:
            print(self.nama+ " sudah memakan "+ a)

    def minum(self, a):
        if(self.statusTidur == 1):
            print("Oopss "+self.nama +" masih tidur dan tidak bisa Minum")
        else:
            print(self.nama+ " sudah meminum "+ a)

    def tidur(self):
        print(self.nama+ " tertidur")
        self.statusTidur=1

    def bangun(self):
        print(self.nama+ " sudah bangun")
        self.statusTidur=0
    
    

