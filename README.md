# TP1DPBO2023
# Janji
Saya Rafi Arsalan NIM 2108938 mengerjakan Tugas Praktikum 1 dalam mata kuliah Desain dan Pemrograman Berorientasi Objek untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.
# Desain Program
Program yang dibuat kali ini bertujuan untuk melakukan praktek terhadap Composite dalam OOP, desain yang dibuat menggunakan Inheritence, Composite dan Agregation.     

Pada program yang saya buat kali ini memiliki 9 Class yaitu Human, Mahasiswa, Dosen, PengurusBEM, AnggotaDPM, Asprak, Laptop, BukuTulis, Spidol

Jadi pada awalnya dibuat sebuah class Human dan class ini akan menjadi parent dari class Mahasiswa dan Dosen dan berarti memiliki seluruh atribut dari class Human tersebut

Lalu class Mahasiswa ini akan diagregasikan kedalam 3 class lainnya yaitu Asprak, PengurusBEM, dan Anggota DPM mengapa saya memilih agregasi daripada extends dikarenakan seorang mahasiswa tidak selalu menjadi pengurus bem, dpm atau asprak dan ada kemungkinan satu orang mahasiswa menjabat sebagai pengurus BEM dan Asprak secara bersamaan dan apabila dipisah sebagai class yang extends terhadap mahasiswa maka harus membuat class dengan data atribut yang sama seperti memiliki nim, nama, jenis kelamin dan data yang lainnya yang sama
jadi disini saya akan memasukkan objek mahasiswa tersebut kedalam class pengurus BEM, anggota DPM atau Aprak sesuai jabatannya masing masing, jadi ketika class BEM tersebut dihapus maka mahasiswa tersebut masih ada dan tidak ikut terhapus beda ketika diextends atau composite

3 class lainnya yaitu laptop, bukutulis dan juga Spidol akan diagregasikan kedalam class mahasiswa dan dosen, kenapa agregasi dan bukan composite karena ketika objek mahasiswa nya dihapus objek spidol, laptop atau buku tulisnya masih ada dan bisa digunakan oleh objek yang lainnya

### Class Diagram :

![classDiagram](https://user-images.githubusercontent.com/90766249/226183597-115a12a1-4d64-4515-ad4d-07ed6e110ca7.png)

# Alur Program dan dokumentasi
Alur dari program ini sendiri awalnya membuat sebuah class Human dengan atribut :
- NIM
- Nama
- JenisKelamin
- statusTidur

Dan class Human ini bisa melakukan :
- Makan
- Minum 
- Tidur
- Bangun

Class Human ini tidak bisa makan atau minum ketika mereka masih tertidur dan lalu mahasiswa akan disimpan kedalam listMhs

setelah itu membuat sebuah class Laptop dengan atribut :
- Merk
- Processor
- Jumlah RAM

BukuTulis dengan atribut :
- Merk
- JmlHalaman

Dan spidol dengan atribut :
- Merk
- Warna
- Jenis

Setelah membuat 3 objek tadi barulah membuat class mahasiswa yang akan diwariskan dari class human dan mengagregasikan Laptop dan BukuTulis  sehingga memiliki atribut :
- NIM
- Nilai
- Laptop
- BukuTulis

lalu membuat class Dosen yang akan diwariskan dari class human dan mengagregasikan Laptop dan Spidol  sehingga memiliki atribut :
- NIP
- PendTerakhir
- Laptop
- BukuTulis

Dosen memiliki aksi tambahan yaitu :
- MemberiNilai

Setelah adanya class Mahasiswa tadi barulah disini saya membuat class Asprak, PengurusBEM, dan AnggotaDPM karena didalam ketiga class ini akan diagregasikan objek Mahasiswa, pengurusBEM memiliki atribut :
- Jabatan
- RancanganProker
- StatusProker

dan pengurusBEM bisa melakukan aksi tambahan yaitu
- merancangProker
- melaksanakanProker

class anggotaDPM memiliki atribut :
- Jabatan

dan AnggotaDPM bisa melakukan aksi tambahan yaitu
- monitoringBEM
- mengapreisasi

class Asprak memiliki atribut :
- namaMatkul
- tugas
- statusTugas

dan Asprak bisa melakukan aksi tambahan yaitu
- MemberikanTugas
- menandaiDinilai

### Output yang dihasilkan : 
mennmpilkan List Mahasiswa :

![menampilkanDataMahasiswa](https://user-images.githubusercontent.com/90766249/226185234-c8a5f784-19e3-43c5-86a1-63f87984c154.png)

menampilkan PengurusBEM dan AnggotaDPM serta interaksi diantara mereka
![pengurusBEMdanDPM](https://user-images.githubusercontent.com/90766249/226184875-6aa49b0c-66a4-49d2-b6d8-f2d7caf307ad.png)

menampilkan data Asprak dan dosen serta interaksi diantara mereka
![asprakDanDosen](https://user-images.githubusercontent.com/90766249/226185183-e577ea8e-0427-445c-b9fc-4b3869dfe14e.png)

dan diakhir menampilkan aktivitas yang bisa dilakukan oleh semua Human
![aktivitasHuman](https://user-images.githubusercontent.com/90766249/226185167-1501f187-11b2-4270-b50a-04e93d0eee26.png)


