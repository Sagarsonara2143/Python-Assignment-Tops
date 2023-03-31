#Write a Python program to remove an empty tuple(s) from a list of tuples.

list1 = [(10,20,30),(30,40),(),(40,50),(),(10,20),()]

print("List 1 is : ",list1)

list2=[]
for i in list1:
    for j in i:
        if j == "":
            break
        else:
           list2.append(i)
           break

print("List 2 is : ",list2)
