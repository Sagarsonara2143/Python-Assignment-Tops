#Write a Python program to read a file line by line and store it into a list.

file = open("listfile.txt","w")
file.write("Sagar\n")
file.write("Sanjay\n")
file.write("Ansh\n")
file.write("Sandhya\n")
file.close()

file=open("listfile.txt","r")
a = file.read()
list=[]
for i in a.split():
    print(i)
file.close()
