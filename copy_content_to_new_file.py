#Write a Python program to copy the contents of a file to another file.

file = open("python.txt","r")

f = open("python2.txt","w")

for i in file.readlines():
    f.write(i)
f.close()
file.close()

file = open("python.txt","r")
print("Python file content :",file.read())
file.close()

file = open("python2.txt","r")
print("Python2 file content :",file.read())
file.close()
