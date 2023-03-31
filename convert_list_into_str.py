# Write a Python program to convert a list of characters into a string.

l1 = []

n = int(input("Enter Length of List : "))
for i in range(n):
    data = input("Enter Character : ")
    l1.append((data))
    
#print(l1)

for i in l1:
    print(i,end= "")
