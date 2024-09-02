a = [1,1,1,3,4,5,5,5,5,7,7,7,9]
for i in range(len(a)-1,0,-1):
    if a[i] == a[i-1]:
        del a[i]
print(a)    