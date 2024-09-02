n = int(input("Enter the number of terms to print:"))
a=0
b=1
c=0
if n==1:
    print(a)
elif n==2:
    print(a)
    print(b)
elif n==3:
    print(a)
    print(b)
    print(c)
else:
    print(a)
    print(b)
    print(c)
    while((n-3)>=1):
        a=b
        b=c
        c=a+b
        print(c)
        n=n-1
