class Laptop: 
    __merk = ""
    __processor  = ""
    __jumlahRAM= ""

    def __init__(self):
        self.merk = ""
        self.processor = ""
        self.jumlahRAM = ""

    def setMerk(self, a):
        self.merk = a
    def setProcessor(self, a):
        self.processor = a
    def setJumlahRAM(self, a):
        self.jumlahRAM = a
    
    def getMerk(self):
        return self.merk
    def getProcessor(self):
        return self.processor
    def getJumlahRAM(self):
        return self.jumlahRAM

