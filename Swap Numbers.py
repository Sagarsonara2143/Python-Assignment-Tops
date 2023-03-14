'''  	Write python program that swap two number with temp variable
        and without temp variable.  '''

x = int(input("Enter Value of X : "))
y = int(input("Enter Value of Y : "))

'''
temp = x
x = y
y = temp

print("Value of X is :",x)
print("Value of Y is :",y)

'''


x,y = y,x

print("Value of X is :",x)
print("Value of Y is :",y)
