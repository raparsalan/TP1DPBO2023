from Mahasiswa import Mahasiswa
from Dosen import Dosen
from PengurusBEM import PengurusBEM
from AnggotaDPM import AnggotaDPM
from Asprak import Asprak
from Laptop import Laptop
from BukuTulis import BukuTulis
from Spidol import Spidol

asusROG = Laptop()
asusROG.setMerk("ASUS")
asusROG.setProcessor("i11 Gen 13")
asusROG.setJumlahRAM("32 GB")

pavilion = Laptop()
pavilion.setMerk("HP Pavilion")
pavilion.setProcessor("Ryzen 9")
pavilion.setJumlahRAM("20 GB")

tufGaming = Laptop()
tufGaming.setMerk("Asus TUF")
tufGaming.setProcessor("Ryzen 7 SS")
tufGaming.setJumlahRAM("16 GB")


sidu = BukuTulis()
sidu.setMerk("Sinar Dunia")
sidu.setJmlHalaman("59 Lembar")

turu = BukuTulis()
turu.setMerk("Tutur Wulan")
turu.setJmlHalaman("69 Lembar")

snowan = Spidol()
snowan.setMerk("Snowman")
snowan.setWarna("Hitam")
snowan.setJenis("Temporary")

listMhs = []
rafi = Mahasiswa()
rafi.setNik("3202050324656")
rafi.setJk("L")
rafi.setNama("Rafi Arsalan")
rafi.setNim("2108938")
rafi.setLaptop(asusROG)
rafi.setBukuTulis(sidu)
listMhs.append(rafi)

algha = Mahasiswa()
algha.setNik("320256487429")
algha.setJk("L")
algha.setNama("Alghaniyu Naufal")
algha.setNim("2104412")
algha.setLaptop(pavilion)
algha.setBukuTulis(turu)
listMhs.append(algha)

najmi = Mahasiswa()
najmi.setNik("32200145858")
najmi.setJk("P")
najmi.setNama("Najma Qalbi")
najmi.setNim("2105521")
najmi.setLaptop(pavilion)
najmi.setBukuTulis(sidu)
listMhs.append(najmi)

bulan = Mahasiswa()
bulan.setNik("3202445218963")
bulan.setJk("L")
bulan.setNama("Cahyana Bulan Fajar")
bulan.setNim("2104412")
bulan.setLaptop(tufGaming)
bulan.setBukuTulis(sidu)
listMhs.append(bulan)

afri = Mahasiswa()
afri.setNik("33002145877956")
afri.setJk("L")
afri.setNama("Afri Setiyadi")
afri.setNim("2104299")
afri.setLaptop(tufGaming)
afri.setBukuTulis(turu)
listMhs.append(afri)

anin = Mahasiswa()
anin.setNik("32077852216")
anin.setJk("P")
anin.setNama("Anindita Kutidaksuka")
anin.setNim("2109167")
anin.setLaptop(asusROG)
anin.setBukuTulis(turu)
listMhs.append(anin)

print("=========== Data Mahasiswa ==========")
jml = 1
for mhs in listMhs:
   print(str(jml)+". NIK                : ", mhs.getNik())
   print("   NIM                : " , mhs.getNim())
   print("   Nama               : " , mhs.getNama())
   print("   Jenis Kelamin      : " , mhs.getJk())
   print("   Merk Laptop        : ", mhs.getLaptop().getMerk())
   print("   Processor Laptop   : ", mhs.getLaptop().getProcessor())
   print("   Kapasitas RAM      : ", mhs.getLaptop().getJumlahRAM())
   print("   Merk Buku          : ", mhs.getBukuTulis().getMerk())
   print("   Kapasitas RAM      : ", mhs.getBukuTulis().getJmlHalaman())
   jml+=1

rosa = Dosen()
rosa.setNik("3202444158963")
rosa.setJk("P")
rosa.setNama("Rosa Ariani")
rosa.setPendTerakhir("S2 Teknik Informatika")
rosa.setLaptop(tufGaming)
rosa.setSpidol(snowan)

kabem = PengurusBEM()
kabem.setJabatan("Ketua")
kabem.setPengurus(rafi)

pengawasan = AnggotaDPM()
pengawasan.setJabatan("Staff Pengawas")
pengawasan.setAnggota(algha)

print("\n=========== Pengurus BEM ==========")
print("-  NIM                : " , kabem.getPengurus().getNim())
print("-  Nama               : " , kabem.getPengurus().getNama())
print("-  Jenis Kelamin      : " , kabem.getPengurus().getJk())
print("-  Jabatan            : ", kabem.getJabatan())

print("\n=========== Anggota DPM ==========")
print("-  NIM                : " , pengawasan.getAnggota().getNim())
print("-  Nama               : " , pengawasan.getAnggota().getNama())
print("-  Jenis Kelamin      : " , pengawasan.getAnggota().getJk())
print("-  Jabatan            : ", pengawasan.getJabatan()+"\n")

print("\n=========== Aktivitas DPM dan BEM ==========")
kabem.merancangProker("Rapat Kerja 1")
pengawasan.monitoringBEM(kabem)
pengawasan.apresiasi(kabem) #dpm mencoba apresiasi ketika bem belum menjalankan proker
kabem.menjalankanProker()
pengawasan.apresiasi(kabem)
kabem.merancangProker("DINAMIK")

listAsprak = []
asprakNajmi= Asprak()
asprakNajmi.setNamaMatkul("Alpro 2")
asprakNajmi.setAsisten(najmi)
listAsprak.append(asprakNajmi)

asprakBulan= Asprak()
asprakBulan.setNamaMatkul("Alpro 2")
asprakBulan.setAsisten(bulan)
listAsprak.append(asprakBulan)

print("\n=========== Data Asprak ===========")
jml=1
for asprak in listAsprak:
   print(str(jml)+". NIM                : " , asprak.getAsisten().getNim())
   print("   Nama               : " , asprak.getAsisten().getNama())
   print("   Jenis Kelamin      : " , asprak.getAsisten().getJk())
   print("   Asprak Matkul      : ", asprak.getMatkul())
   jml+=1

print("\n=========== Data Dosen ===========")
print("1. NIK                : ", rosa.getNik())
print("   Nama               : " , rosa.getNama())
print("   Jenis Kelamin      : " , rosa.getJk())
print("   Pend. Terakhir     : " , rosa.getPendTerakhir())
print("   Merk Laptop        : ", rosa.getLaptop().getMerk())
print("   Processor Laptop   : ", rosa.getLaptop().getProcessor())
print("   Kapasitas RAM      : ", rosa.getLaptop().getJumlahRAM())
print("   Merk Spidol        : ", rosa.getSpidol().getMerk())
print("   Warna Spidol       : ", rosa.getSpidol().getWarna())
print("   Jenis Spidol       : ", rosa.getSpidol().getJenis()+"\n")


print("\n=========== Aktivitas asprak dan dosen ===========")
asprakBulan.memberiTugas("TP 11")
rosa.memberiNilai(rafi,asprakBulan,"90")
rosa.memberiNilai(rafi,asprakNajmi,"80") #dosen mencoba memberi nilai ketika asprak belum memberikan tugas apapun
asprakNajmi.memberiTugas("TP 23")
rosa.memberiNilai(algha,asprakNajmi,"113")


print("\n=========== Aktivitas semua manusia ===========")
rosa.makan("Ramen")
afri.minum("Starbak")
algha.makan("Indomie Soto")
algha.minum("Kasih Sayang")
najmi.tidur()
najmi.makan("Nasi padang") #najmi mencoba makan ketika mmasih tertidur
najmi.bangun()
najmi.makan("Nasi padang")
