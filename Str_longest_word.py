'''
Write a Python function that takes a list of words and returns the length of the
longest one
'''
def fun(str):
    #str = input("Enter a String : ")  # Take Input from User

    l = 0                           # store length of word in l
    l1 = []

    for i in str.split():           # Loop till all words from string
        if len(i) > l:              # check if length of i is greter then l or not
            l = len(i)              # if length of word is greter then l assign len to i
            word = i                # assign i to variable for printing purpose
    
    print("Longest Word is : ",word)
    print("Length is : ",len(word))


l1=[]
s = input("Enter a String : ")
fun(s)

for i in s.split():           
    l1.append(i)
print(l1)
