#Write a Python program to convert a tuple to a string.

tup = ('S','A','G','A','R')

print("Tuple is : ",tup)
str = ''.join(tup)
print("String is (using 'Join') : ",str)


str1 = ""
for i in tup:
    str1 = str1 + i

print("String is : ",str1)
