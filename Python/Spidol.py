class Spidol: 
    __merk = ""
    __warna  = ""
    __jenis= ""

    def __init__(self):
        self.merk = ""
        self.warna = ""
        self.jenis = ""

    def setMerk(self, a):
        self.merk = a
    def setWarna(self, a):
        self.warna = a
    def setJenis(self, a):
        self.jenis = a
    
    def getMerk(self):
        return self.merk
    def getWarna(self):
        return self.warna
    def getJenis(self):
        return self.jenis

