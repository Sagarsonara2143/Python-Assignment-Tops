#Write a Python program to count the frequency of words in a file.

f=open("python.txt","r")
wd = 0

for i in f.read().split():
    wd=wd+1
    print(i,end=" ")

print("\nTotal words :",wd)
f.close()
