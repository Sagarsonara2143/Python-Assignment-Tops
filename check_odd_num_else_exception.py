#Write python program that user to enter only odd numbers, else will raise an exception.

num = int(input("Enter Odd number : "))

try:
    if num % 2 == 0:
        print(num,"is odd number")
    else:
        print("Error : Enter only Odd number")
except:
    pass
