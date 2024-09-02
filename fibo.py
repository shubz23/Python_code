n = int(input("Enter Nth term:"))
a = 0
b = 1
print(a,b,end = "\t")
for i in range (1,n-1):
    c = a+b;
    print(c,end = "\t")
    a=b
    b=c