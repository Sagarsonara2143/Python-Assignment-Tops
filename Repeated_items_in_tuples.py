#Write a Python program to find the repeated items of a tuple.

tup = (10,20,30,40,10,20,60,10,70,20,10,50)

print("Tuple is ",tup)

count = tup.count(int(input("Enter Value to count repeates : ")))
print(count)

