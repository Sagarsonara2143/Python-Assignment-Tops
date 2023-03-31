#Write a Python function to check whether a number is in a given range.

def checkNum(n):
    if n>=1 and n<=20:
        print(n,"is in range of 1 - 20.")
    else:
        print(n,"is not in range")

n = int(input("Enter Number Between 1 to 20 : "))
checkNum(n)
