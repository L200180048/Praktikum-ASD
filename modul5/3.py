from time import time as detak
from random import shuffle as kocok
def swap(A,p,q):
    tmp = A[p]
    A[p]= A[q]
    A[q]= tmp

def bubbleSort(A):
    n = len(A)
    for i in range(n-1):
        for j in range(n-i-1):
            if A[j] > A[j+1]:
                swap(A,j,j+1)

def selectionSort(A):
    n = len(A)
    for i in range(n-1):
        indexKecil = cariPosisiTerkecil(A, i, n)
        if indexKecil != i :
            swap(A, i, indexKecil)

def insertionSort(A):
    n = len(A)
    for i in range(1,n):
        nilai = A[i]
        x = i
        while x > 0 and nilai < A[x - 1]:
            A[x] = A[x -1]
            x = x -1
        A[x] = nilai
        
def cariPosisiTerkecil(A,darisini, sampaisini):
    posisiTerkecil = darisini
    for i in range (darisini+1, sampaisini):
        if A[i] < A[posisiTerkecil]:
            posisiTerkecil = i
    return posisiTerkecil

k = []
for i in range(1, 6001):
    k.append(i)
kocok(k)
u_bub = k[:]
u_sel = k[:]
u_ins = k[:]

aw = detak(); bubbleSort(u_bub);ak=detak();print('bubble: %g detik' %(ak-aw));
aw = detak(); selectionSort(u_sel);ak=detak();print('selection: %g detik' %(ak-aw));
aw = detak(); insertionSort(u_ins);ak=detak();print('insertion: %g detik' %(ak-aw));
