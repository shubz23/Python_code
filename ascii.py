char = input("Enter the character:")
if (len(char)==1):
    print ("The ASCII code of",char,"is", ord(char))
else:
    print("Enter a character only,not a string.")