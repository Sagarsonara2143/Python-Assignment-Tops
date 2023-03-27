# Write a Python function that takes two lists and returns true if they have at least one common member.

def common_num(list1,list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False

l1 = [10,15,20,25,30,35,40,45,50]
l2 = [1,2,3,4,5,6,7,8,9,10]

print("*"*50)
print("List 1 : ",l1)
print("List 2 : ",l2)
print(common_num(l1,l2))
print("*"*50)
