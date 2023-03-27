# Write a Python function that takes two lists and returns true if they have at least one common member.

def common_num(list1,list2):
    common_list = []
    for i in list1:
        for j in list2:
            if i == j:
                common_list.append(i)
    print("Common Number in both List : ",common_list)
    return ""


l1 = [1,3,5,7,9,11,13,15,17]
l2 = [1,2,3,4,5,6,7,8,9,10,11]
print("List 1 is : ",l1)
print("List 2 is : ",l2)
print(common_num(l1,l2))

