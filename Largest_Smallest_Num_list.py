'''
Write a Python function to get the largest number, smallest num and
sum of all from a list.
'''

def listCount(n):
    l = []
    for i in range (n):
        num = int(input("Enter Number : "))
        l.append(num)
    print("\nList are : ",l)
    print("Largest Number is : ", max(l))
    print("Smallest Number is : ", min(l))


    print("*"*50)
    l.sort()
    print("List Sorted as : ",l)
    print("Largest Number is : ", l[-1])
    print("Smallest Number is : ", l[0])
    print("*"*50)

    sum = 0
    for i in range(len(l)):
        sum = sum + l[i]
        i = sum
    print("Sum of List Value is : ",sum)

    

n1 = int(input("Enter Length of List : "))
listCount(n1)
