print("Enter 7 distinct elements in set a: ")
a= set(input() for i in range(7))

print("Enter 7 distinct elements in set b: ")
b= set(input() for i in range(7))

print("A union B is: ", a|b)
print("A intersection b is: ", a&b)
print("Set difference between a and b is: ", a-b)
print("Symmetric Difference between a and b is: ", a^b)