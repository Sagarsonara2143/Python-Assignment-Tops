#Write a Python program to returns sum of all divisors of a number.

#Ex - 8  = 1,2,4
#Ex -25 = 1,5               Ex-30 = 1,2,3,5,6,10,15

n = int(input("Enter Number : "))

sum = 1

for i in range(2,n):            # loop from 2 to n value
    if n % i == 0:                  # check divisor and store in sum variable
        sum = sum+i

print(sum)
