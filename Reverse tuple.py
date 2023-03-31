#Write a Python program to reverse a tuple.

tup = ("Sagar","Sid","Raj","Kunal")

print("Original Tuple is : ",tup)
a = reversed(tup)                                                               # used reversed function 
print("Reversed tuple using inbuild function : ",tuple(a))

print("Reversed Tuple using slicing : ",tup[::-1])            # Used slicing to get reverse tuple
