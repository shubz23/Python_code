for Num in range (1, 101):
    if Num > 1:
        for i in range(2,Num):
            if(Num % i) == 0:
                break
        else:
            print(Num)
            