a = [1,1,1,3,4,5,5,5,5,7,7,7,9,9]
i =0
l = len(a)-1
while i < l :
    if a[i] == a[i+1]:
        del a[i+1]
        l -=1
    else :
        i +=1
print(a)