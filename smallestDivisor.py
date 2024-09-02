x =int(input("Enter an integer no.:"))
l=[]
for i in range(2,x+1):
    if(x%i==0):
        l.append(i)
l.sort()
print("Smallest divisor is:",l[0])
print(l)
