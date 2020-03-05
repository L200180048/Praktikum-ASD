def apakahPrima():
    lower = 2 
    upper = 1000
    print("Bilangan prima antara",lower,"and",upper,":")
    for x in range(lower,upper + 1): 
        if x > 1: 
            for i in range(2,x): 
                if (x % i) == 0: 
                    break 
            else: 
                print(x)
