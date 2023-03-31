#Write a Python function to calculate the factorial of a number (a nonnegative integer).
#Factorial = 5*4*3*2*1


def calFact(n):
    res = 1
    for i in range(n):                  # Loop till number
        res = res*n                     # multiply with number and store in variable
        n=n-1                           #Decrement number - 6*5*4*3*2*1
    print(res)

n = int(input("Enter Number for Factorial  : "))
calFact(n)
