#Write a Python program to count the number of lines in a text file.

f = open("listfile.txt","r")

line=0
for i in f.readlines():
    line=line+1

print(line)
f.close()
