x = [2,'Python',45,78,6,9,2,13,2,]
x.append(56)
print("adding 56 to list x=",x)

y=x.copy()
print("print y =",y)

b = x.count(2)
print("no. of 2 =",b)

y.extend(x )
print("adding x to y",y)

h = x.index(45)
print("index of 45=",h)

k = x.insert(2,5)
print("inserting 5 at 2nd index =",k)

p =x.pop(4)
print("removing element with index 4=",p)

t =x.remove(2)
print("removing first 2",t)

x.reverse()
print("reversing list x=",x)

x.sort()

#z =x.clear()
#print("clear the element in list=",z)

