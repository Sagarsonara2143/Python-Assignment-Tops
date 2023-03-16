''' Write a Python program to count the occurrences of
    each word in a given sentence '''

s = input("Enter a string : ").upper()

dic = {}

word = s.split()    # str split if space occured end its count word

for i in word:      # loop till all word 
    if i in dic:    # check word is availabel in dictionary or not
        dic[i] = dic[i] + 1     # if availabel in dic then increment 1
    else:
        dic[i] = 1              # if not availabel in dic then assign value 1

for i in dic:
    print(i,"\t:",dic[i])

















