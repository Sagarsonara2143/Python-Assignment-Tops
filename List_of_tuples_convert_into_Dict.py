#Write a Python program to convert a list of tuples into a dictionary.

l = [("A",10),("B",20),("C",30),("A",40),("B",50),("C",60),("A",70),("B",80),("C",90)]

print("List : ",l)
dic = {}

for i,j in l:
    dic.setdefault(i,[]).append(j)      #assign first value as key and second is values for the same


print("Dictionary : ",dic)
