''' Write a Python program to get a single string from two given strings,
    separated by a space and swap the first two characters of each string.'''

s1 = input("Enter First String : ")
s2 = input("Enter Second String : ")

print("\n\nString Merged - Seprated by space : ",s1,s2)

a = s1[0:2]
s1 = s1.replace(s1[0:2],s2[0:2])
s2 = s2.replace(s2[0:2],a)

print("After swaping first two character of each string : ",s1,s2)
