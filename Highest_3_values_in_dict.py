#Write a Python program to find the highest 3 values in a dictionary.

dic = {"A":110,"B":60,"C":30,"D":70,"E":20,"F":100,"G":25}

print("Dictionary : ",dic.values())

a = sorted(dic.values())

print("Highest Values in Dictionary : ",a[-3:])
