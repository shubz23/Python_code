# x= range(3,21,2)
# for n in x:
#     print (n)

# print the sum of reciprocals of first 100 natural number

sum_reci = 0

for i in range(1, 101):
    sum_reci += 1 / i

print("Sum of reciprocals of the first 100 natural numbers:", sum_reci)
