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

class Mahasiswa(Manusia):
    """Class Mahasiswa yang dibangun dari class Manusia"""
    def __init__(self,nama,NIM,kota,us):
        """Metode inisialisasi ini menutupi metode inisiasi di class Manusia."""
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangsaku = us
    def __str__(self):
        s = self.nama+", NIM"+str(self.NIM)\
            +". Tinggal di" +self.kotaTinggal \
            +". Uang saku Rp."+str(self.uangsaku)\
            +" tiap bulan."
            
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.uangsaku
    def makan(self,s):
        """Metode ini menutupi makan -nya class Manusia. Mahasiswa kalau makan sambil belajar"""
        return("Saya baru saja makan",s,"sambil belajar.")
        self.keadaan="Kenyang"
    def ambilKotaTinggal(self):
        return self.kotaTinggal
    def perbaruiKotaTinggal(self,kotabaru):
        self.kotaTinggal = kotabaru
    def tambahUangSaku(self,uang):
        self.uangsaku = self.uangsaku+uang
    
    
    
