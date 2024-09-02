# rows = 5
# for i in range(1, rows + 1):   # for i in range (1,6)

#     num = i
#     for j in range(1, i + 1): # for j in range(1, 2*i) 
#         print(num, end=" ")
#         num += 1
#     print()


# 1
# 2 3
# 3 4 5
# 4 5 6 7
# 5 6 7 8 9
    

# Write the program that reads number of rows and prints following pattern 

# Input: 3




# 1 
# 3 1 
# 6 3 1 
# rows = int(input("Enter the number of rows: "))

# for i in range(1, rows + 1):
#     start = i * (i + 1) // 2
    
#     for j in range(i, 0, -1):
#         print(start, end=" ")
#         start //= 2  
#     print()  


# 1
# 2 1
# 4 2 1
rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    start = 2 ** (i - 1)
    
    for j in range(i, 0, -1):
        print(start, end=" ")
        start //= 2  
    print()  
