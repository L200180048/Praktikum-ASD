def binary (kumpulan,target):
    low = 0
    high = len(kumpulan) -1
    listku = []

    while low <= high:
        if kumpulan [low] == target:
            listku.append(low)
            low += 1
        else:
            low += 1
    return listku

s = [2,3,5,6,6,6,8,9,9,10,11,12,13,13,14]
dicari = 6
print("mencari angka ", dicari, " pada list ", s, "akan mengembalikan ",binary(s, dicari))
