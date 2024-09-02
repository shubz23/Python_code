# given positive integer n print all the integers less than or equal to n that are divisible by 3 or divisible by 5 

n= int (input())
for i in range(1, n + 1):
    if i % 3 == 0 or i % 5 == 0:
        print(i)
