'''
Write a Python program to get a string made of the first 2 and the last 2
chars from a given a string.
If the string length is less than 2, return instead of the empty string.
'''

str1 = input("Enter String : ") # Take user input

if len(str1) > 2:               # check if str length is greter than 2
    print(str1[0:2] + str1[-2:])# if str greter than 2 then first two and last char of str will be print
else:
    print(" ") 
