#read 5 inputs from a user . print the sum of only positive number

# sum_posi = 0
# for i in range(5):
#     num = int(input("Enter a number: "))
#     if num > 0:
#         sum_posi += num

# print("Sum of positive numbers:", sum_posi)





sum =0         
for i in range (6):
    value = int(input())
    if(value<0):
        continue 
    sum = sum + value
print("sum=",sum)



# # Using break
# sum_positive = 0
# for i in range(5):
#     num = int(input("Enter a number: "))
#     if num > 0:
#         sum_positive += num
#     else:
#         break  
# print("Sum of positive numbers:", sum_positive)

# other program
# sum =0         
# for i in range (100):
#     value = int(input())
#     if(value<0):
#         break 
#     sum = sum + value
# print("sum=",sum)


