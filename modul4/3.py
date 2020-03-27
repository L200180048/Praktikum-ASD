class MhsUMS(object):
    def __init__(self, nama, nim, kota, us):
        self.nama = nama
        self.nim = nim
        self.kotaTinggal = kota
        self.uangSaku = us
        

class buatArray(object):
    
    internalData = 11*[None]
    
    def __getitem__(self, item):
        return self.internalData[item]

    def __setitem__(self, key, value):
        self.internalData[key] = value

    def cariKota(self, data):
        d = []
        t = 0
        for i in self:
            if i.kotaTinggal == data:
                d.append(t)
            t += 1
        return d
    def cariuangsaku(self):
        terkecil = self[0].uangSaku
        for i in self:
            if i.uangSaku < terkecil:
                terkecil = i.uangSaku
        return terkecil
    def cariuangkecil(self):
        terkecil = self[0].uangSaku
        d = []
        for i in self:
            if i.uangSaku < terkecil:
                d.append((i.nama, i.nim, i.kotaTinggal, i.uangSaku))
        return d


c = buatArray()
c[0] = MhsUMS('Ara', 20, 'Salatiga', 2500000)
c[1] = MhsUMS('Jono', 7, 'Malang', 2000000)
c[2] = MhsUMS('Tara', 2, 'Surakarta', 3000000)
c[3] = MhsUMS('Eva', 12, 'Sragen', 240000)
c[4] = MhsUMS('Fadil', 8, 'Wonogiri', 2500000)
c[5] = MhsUMS('Arif', 31, 'Sukoharjo', 2800000)
c[6] = MhsUMS('Dina', 29, 'Klaten', 2550000)
c[7] = MhsUMS('Ajeng', 35, 'Banten', 200000)
c[8] = MhsUMS('Deni', 27, 'Klaten', 2450000)
c[9] = MhsUMS('Hari', 42, 'Boyolali', 3500000)
c[10] = MhsUMS('tata', 24, 'Semarang', 2700000)

