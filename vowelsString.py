c=0
vowels = ['a','e','i','o','u','A','E','I','O','U']
thestring = input("Enter the String to check vowels:")
for char in thestring:
    if char in vowels:
        c +=1
print ("Number of vowels in the string are:",c)
