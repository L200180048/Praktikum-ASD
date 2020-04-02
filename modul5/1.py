class Mahasiswa(object):
    def __init__(self,nama,nim,kota,us):
        self.nama = nama
        self.nim = nim
        self.kotaTinggal = kota
        self.uangSaku = us
        

class MhsTIF (Mahasiswa):
    def katakanPy(self):
        print('Python is cool.')
        
c = [MhsTIF('Ara', 20, 'Salatiga', 2500000),
MhsTIF('Jono', 7, 'Malang', 2000000),
MhsTIF('Tara', 2, 'Surakarta', 3000000),
MhsTIF('Eva', 12, 'Sragen', 240000),
MhsTIF('Fadil', 8, 'Wonogiri', 2500000),
MhsTIF('Arif', 31, 'Sukoharjo', 2800000),
MhsTIF('Dina', 29, 'Klaten', 2550000),
MhsTIF('Ajeng', 35, 'Banten', 200000),
MhsTIF('Deni', 27, 'Klaten', 2450000),
MhsTIF('Hari', 42, 'Boyolali', 3500000),
MhsTIF('tata', 24, 'Semarang', 2700000)]
def urutkannim(l):
    n = len(l)
    for i in range (n -1) :
        for k in range (n-i-1) :
            if l[k].nim > l[k+1].nim :
                swap(l,k,k+1)

def lihatnim (l):
    for i in l :
        print (i.nim)

def swap (a, p, q) :
    tmp = a[p]
    a[p] = a[q]
    a[q] = tmp
        



