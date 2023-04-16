#Write a Python program to write a list to a file.

file = open("list.txt","w")

list1=["sagar","rameshbhai","sonara"]

for i in list1:
    file.write(i + " ")

file.close()

f = open("list.txt","r")
print(f.read())
f.close()
