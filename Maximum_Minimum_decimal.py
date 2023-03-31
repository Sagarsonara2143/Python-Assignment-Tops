#Write a Python program to find the maximum and minimum numbers from the specified decimal numbers.
#google


from decimal import *

d = list(map(Decimal,'2.5 0.5 00.9 1.5 10.5 12.7 11.9 0.05 20.5'.split()))

print("Max : ", max(d))
print("Min : ", min(d))
