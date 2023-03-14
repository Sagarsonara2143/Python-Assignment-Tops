''' Write a Python program that will return true
    if the two given integer values are equal or their sum or difference is 5.'''

a = int(input("Enter Value of A: "))
b = int(input("Enter Value of B: "))

if a == b or abs(a-b)==5 or a+b == 5:   
    print("True")
else:
    print("False")



'''
When abs () is used, it converts negative numbers to positive.
However, when -abs () is used, then a positive number can be changed to a negative number.
'''





















