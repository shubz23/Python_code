def print_factors(x):
    print("The factors of",x,"are:")
    for i in range (1,x+1):
        if x % i ==0:
           print(i)

x = 320
print_factors(x)


