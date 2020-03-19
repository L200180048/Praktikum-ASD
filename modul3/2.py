def buatNol(n,m=None):
    if(m==None):
        m=n
    print("Membuat matriks 0 dengan ordo "+str(n)+"x"+str(m))
    print([[0 for x in range(m)] for y in range(n)])
buatNol(5,4)
buatNol(5)

def buatIdentitas(n):
    print("Membuat matriks Identitas dengan ordo "+str(n)+"x"+str(n))
    print([[1 if j==i else 0 for j in range(n)] for i in range(n)])


buatIdentitas(2)
buatIdentitas(5)
buatIdentitas(7)
buatIdentitas(8)
