a = [[1, 2, 4, 13],
     [12, 75, 2, 7],
     [9, 6, 0, 4]]

b = [[55, 12, 75, 10],
     [7, 5, 23, 47],
     [98, 3, 35, 17]]

x = [[0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0]]

for i in range(len(a)):
   for j in range(len(b[0])):
       x[i][j] = a[i][j] + b[i][j]

print ("Matrix a:")
for n in a:
   print(n)

print ("Matrix b:")
for n in b:
   print(n)

print ("Sum of matrices a and b:")
for n in x:
   print(n)
