'''
Write a Python program to count the number of strings where the string length
is 2 or more and the first and last character are same from a given list of
strings.
'''

def matchStr(list):     # Create a function to check str are match to criteria 
    count = 0           # count the str to match criteria and store

    for i in list:      # check in list till end of the list
        if len(i)>=2 and i[0]==i[-1]:   # match with criteria
            count = count + 1           # if matched increment count variable 
            print("Length is more then 2 and first and Last Character are same : ",i)
    return count        # if not found str then return 

l1 = ["sagas", "Sanjay","Rajr","J","joj","SS"]  # List for check str

print(matchStr(l1))             # Call Function with list

