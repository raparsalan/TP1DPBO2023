class BukuTulis: 
    __merk = ""
    __jmlHalaman  = ""

    def __init__(self):
        self.merk = ""
        self.jmlHalaman = ""

    def setMerk(self, a):
        self.merk = a
    def setJmlHalaman(self, a):
        self.jmlHalaman = a
    
    def getMerk(self):
        return self.merk
    def getJmlHalaman(self):
        return self.jmlHalaman

