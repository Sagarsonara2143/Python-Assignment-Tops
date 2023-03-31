#Write a Python program to select an item randomly from a list.
import random

list1 = [1,2,3,4,5,6,7,8,9,10]

for i in list1:
    a = random.choice(list1)

print("Random Number :",a)
