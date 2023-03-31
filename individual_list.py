#Write a Python program to unzip a list of tuples into individual lists.

l = [(10,20),(30,40),(True,False),(0.1,0.2),("Python","Java")]

print("List : ",l)
for i in l:
    print([i])
