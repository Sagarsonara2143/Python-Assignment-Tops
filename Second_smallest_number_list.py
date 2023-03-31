#Write a Python program to find the second smallest number in a list.

list1 = []
n=int(input("Enter Length of List : "))

for i in range(n):
    x = int(input("Enter Value :- "))
    list1.append(x)

list1.sort()

print("List : ",list1)
print("Second Smallest Number in List is : ",list1[1])
