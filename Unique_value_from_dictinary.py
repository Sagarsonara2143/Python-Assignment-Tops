#Write a Python program to print all unique values in a dictionary.

dic = {"A" : 50, "B" : 60,"C" : 80,"D" : 70,"E" : 60,"F" : 80,"G" : 70,"H" : 60}

print("Values : - ", sorted(dic.values()))
print("Unique Values :",sorted(set(dic.values())))
