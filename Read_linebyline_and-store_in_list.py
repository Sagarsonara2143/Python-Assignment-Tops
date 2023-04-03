#Write a Python program to read a file line by line and store it into a list.

file = open("listfile.txt","w")
file.write("Sagar\n")
file.write("Sanjay\n")
file.write("Ansh\n")
file.write("Sandhya\n")
file.close()

file=open("listfile.txt","r")
a = file.readlines()
l=[]
for i in a:
    l.append(i)
    print(i,end="")

print(l)
file.close()
