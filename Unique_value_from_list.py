#Write a Python program to get unique values from a list.

l = []

n = int(input("Enter Length of List : "))

for i in range(n):
    x = int(input("Enter Value : "))
    l.append(x)

uni_list=[]

for i in l:
    if i in uni_list:
        continue
    else:
        uni_list.append(i)

print("List : ",l)
print("Output : ",uni_list)

l1 = set(l)
print("List of unique value using 'Set' :",list(l1))
