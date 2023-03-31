#Write a Python program to check multiple keys exists in a dictionary.

dic = { "A": 50, "B": 150, "C": 250}

print(dic.keys())

count = 0
for i in dic:
    if i == "":
        break
    else:
        count = count + 1

print(count," keys are exists in a dictionary")
