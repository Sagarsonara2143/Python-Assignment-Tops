'''
Write a Python program to generate and print a list of first and last 5 elements
where the values are square of numbers between 1 and 30.
'''

def sq_num():
    list = []
    for i in range (1,31):
        list.append(i*i)
    print("List : - ",list)
    print("First Five Numbers :- ",list[:5])
    print("Last Five Numbers :-",list[-5:])

sq_num()
    
