#Write a Python function to insert a string in the middle of a string.

def insert_str_mid(str1,str2):      # Make function and take two str as arguments

    return str1[:int(len(str1)/2)] + str2 + str1[int(len(str1)/2):] # print half of first str then second string and second half of first str

s1 = input("Enter String : ")   # Take input from User
s2 = input("Enter String : ")

print(insert_str_mid(s1,s2))    # call function
