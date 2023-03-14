''' Write a Python program to find whether a given number is even or odd,
    print out an appropriate message to the user.'''

n = int(input("Enter Value : "))
if n > 0:
    if n % 2 == 0:
        print(n, "is Even Number")
    else:
        print(n," is Odd Number")
else:
    print("Invalid Input")
