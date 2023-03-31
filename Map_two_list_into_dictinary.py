#Write a Python program to map two lists into a dictionary.

key = [1,2,3]
val = ["Sagar","Sanjay","Ansh"]

dic = {}

for i in key:           #loop for Key
    for j in val:           #loop for Values
        dic[i]=j                # Keys assign with value
        val.remove(j)        # Value Remove from list
        break                      #Value loop terminate after value getting for key
print(dic)
