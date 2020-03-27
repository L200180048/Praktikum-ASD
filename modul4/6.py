def binary (kumpulan,target):
    low = 0
    high = len(kumpulan) -1

    while low <= high:
        mid = (high + low) // 2
        if kumpulan [mid] == target:
            return "target berada di index " + str(mid)
            break
        
        elif target < kumpulan [mid]:
            high = mid - 1

        else:
            low = mid + 1

    return False

listnya = [15, 32, 11, 22, 43, 80, 86]
target1 = 43
target2 = 40

