def apakahKabisat(x):
    if x%4==0:
        if x%100==0 and x%400==0:
            return True
        elif x%100==0 and x%400!=0:
            return False
        return True
    return False
