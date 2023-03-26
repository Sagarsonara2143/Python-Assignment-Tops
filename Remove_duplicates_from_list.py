#Write a Python program to remove duplicates from a list.


list = []

n = int(input("Enter List length : "))

for i in range(n):
    i = input("Enter Value : ")
    list.append(i)

print("Original List are : ",list)
unique_val = []


for i in list:
    if i in unique_val:
        continue
    else:
        unique_val.append(i)


print("List after removed duplicates values : ",unique_val)



