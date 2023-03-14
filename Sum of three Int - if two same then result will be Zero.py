''' Write a Python program to sum of three given integers.
    However, if two values are equal sum will be zero.'''



a = int(input("Enter 1st Value : "))
b = int(input("Enter 2nd Value : "))
c = int(input("Enter 3rd Value : "))

if a == b or b == c or c == a:
    print("Zero")
else:
    sum = a + b + c
    print("Sum of ",a,",",b,"and",c,"is",sum)
    
    
















