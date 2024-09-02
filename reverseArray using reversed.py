import array

new_arr=array.array('i',[10,20,30,40])
print("Original Array is :",new_arr)

#reversing using reversed()
res_arr=array.array('i',reversed(new_arr))
print("Resultant Reversed Array:",res_arr)
