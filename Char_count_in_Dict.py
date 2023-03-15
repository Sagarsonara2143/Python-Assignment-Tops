''' Write a Python program to count the number of characters
    (character frequency) in a string.  '''

str = input("Enter String : ").upper()
dict = {}
char = 0

for i in str:           
    if i in dict:       #Check char is availabel in string
        dict[i] = dict[i] + 1 # if availabel it will add with 1
    else:
        dict[i] = 1         # if not availabel then assign value is 1

for i in dict:
    print(i,":",dict[i])
    
