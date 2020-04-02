def mengurutkan(A,B):
    C = A+B
    n = len(C)
    for i in range(1,n):
        nilai=C[i]
        x=i
        while x > 0 and nilai < C[x-1]:
            C[x]=c[x-1]
            x=x-1
        C[x] = nilai
    return C
A = [15,16,17,18,20,24]
B = [28,29,30,32,33,36]
