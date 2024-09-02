my_set = {1, 2,6,7,2,2,2,2,2}
sett = {2,80,97,56,34}
print(my_set|sett) # UNION OF MY_SET AND SETT

print(my_set & sett) #INTERSECTION OF TWO SETS

print(my_set - sett) # difference of two sets

print(my_set ^ sett) #symmetric difference of two sets

my_set.add(2)
print(my_set)

my_set.update([5,7,9])
print(my_set)

my_set.remove(6)
print(my_set)

my_set.discard(2)
print(my_set)

my_set.clear()
print(my_set)
