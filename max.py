# def max3(a,b,c):
#     return (max(a,max(b,c)))
# print(max3(10,45,2))

def printName(firstName, lastName, initials = True ):
    if initials: #''
        print (firstName[0]+ '.'+ lastName[0]+ '.')
    else:
        print(firstName , lastName)