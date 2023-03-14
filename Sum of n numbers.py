# Write a python program to sum of the first n positive integers.


n = int(input("Enter Value of n : "))

sum = 0

while n>0:                          # Using While loop
    sum = sum + n
    n = n-1

print(sum)


n1 = int(input("Enter Value of N: "))

sum1 = n1 * (n1+1) / 2          # Using Arithmatic Operators
print(int(sum1))



n2 = int(input("Enter Value of N: "))
sum2 = 0
for i in range(1,n2+1):             # Using For loop
    sum2 = sum2 + i
print(sum2)







