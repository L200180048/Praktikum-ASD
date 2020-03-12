class Manusia(object):
    keadaan="lapar"
    def __init__(self,nama):
        self.nama=nama
    def ucapkanSalam(self):
        print("Salam, namaku", self.nama)
    def makan(self,s):
        print("Saya baru saja makan", s)
        self.keadaan="kenyang"
    def olahraga(self,k):
        print("Saya baru saja latihan", k)
        self.keadaan="lapar"
    def mengalikanDenganDua(self,n):
        return n*2
    
class SiswaSMA(Manusia):

    def __init__(self,nama,NISN,kelas,jurusan):
        
        self.nama = nama
        self.nisn = NISN
        self.kelas = kelas
        self.jurusan = jurusan
    def __str__(self):
        s = self.nama+" "+str(self.nisn)\
            +" " +self.kelas \
            +" "+self.jurusan   
        return s
    def ambilNama(self):
        return self.nama
    def ambilNISN(self):
        return self.nisn
    def ambilkelas(self):
        return self.kelas
    def ambiljurusan(self):
        return self.jurusan
