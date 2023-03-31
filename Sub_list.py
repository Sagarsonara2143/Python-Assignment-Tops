#Write a Python program to check whether a list contains a sub list.

list1 = [10,20,40,True,60,70,"sagar"]

sub = [60,70]

x = len(list1)
y = len(sub)

print("Original List is ",list1)
if x>y:
    for i in range(x - y + 1):
        if list1[i:i+y] == sub:
            print("Yes",sub,"is a sub list of original list")
            break
    else:
        print("No")
else:
    print("Sub List length is more then Original List")
