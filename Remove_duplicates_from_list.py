#Write a Python program to remove duplicates from a list.


list = [10,40,60,10,45,50,40,70,80,60,45]

print("Original List are : ",list)
unique_val = []


for i in list:
    if i in unique_val:
        continue
    else:
        unique_val.append(i)


print("List after removed duplicates values : ",unique_val)



