import math
def primefactors(n):
    while n % 2 == 0:
        print(2),
        n = n / 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while (n % i == 0):
            print(i)
            n = n / i
    if n > 2:
        print(n)
n = int(input("Enter the number for calculating the prime factors :"))
primefactors(n)