#Write a Python program to read a file line by line store it into a variable.

file=open("listfile.txt","r")

read = file.readlines()
print(read)

file.close()
