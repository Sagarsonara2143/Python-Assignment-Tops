'''
Write a Python program to create a dictionary from a string.
Note: Track the count of the letters from the string.
Sample string: 'w3resource'
Expected output:
{'3': 1,’s’: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}
'''

s = input("Enter String : ")
dic = {}

for i in s:                         #for loop till str end
    if i in dic:                    #check if char availabel in dictionary or not
        dic[i] = dic[i]+1       # if available increment value
    else:   
        dic[i]=1                    # if not then assign value = 1
    
print(dic)
