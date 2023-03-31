#Write a Python script to check if a given key already exists in a dictionary.

d1 = {"A":11,"B":51,"C":101,"D":151,"E":201}

print("Dictionary : ",d1)
n = input("Enter Key to check : ").upper()

for i in d1:
    if i == n:
        print("Key Already Exists")
        break
else:
    print("Key not found")
