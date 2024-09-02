from collections import OrderedDict
a = [1, 3, 3, 5, 5, 5, 6, 9]
print("The original list is : ", a)
b = list(OrderedDict.fromkeys(a))
print("The list after removing duplicates : " ,b)
