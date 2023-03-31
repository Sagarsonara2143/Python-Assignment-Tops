#Write a Python program to check whether an element exists within a tuple.

tuple = (10,20,30,40,50,60)

print(tuple)
print(10 in tuple)
print(15 in tuple)

n = int(input("Enter an Element to check : "))

for i in tuple:
    if i == n:
        print(n," is available in tuple")
        break
else:
    print(n," is not available in tuple")
