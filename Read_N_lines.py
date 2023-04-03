#Write a Python program to read first n lines of a file.
from itertools import islice
n = int(input("Enter line number : "))

f = open("random.txt","r")

for i in islice(f,n):
    print(i,end="")
