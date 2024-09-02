# Read no.s from the user until user enterd -1 and find the maximum
# max_number = None

# while True:
#     num = int(input("Enter a number (-1 to stop): "))
#     if num == -1:
#         break
#     if max_number is None or num > max_number:
#         max_number = num

# if max_number is not None:
#     print("Maximum number entered:", max_number)
# else:
#     print("No numbers were entered.")

n = int(input("Enter a number (-1 to stop): "))
max_num = n

while n != -1:
    n = int(input("Enter a number (-1 to stop): "))
    if n != -1 and n > max_num:
        max_num = n 

print('Maximum =', max_num)


