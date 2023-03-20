'''
Write a Python function to reverses a string if its length is a multiple of 4.
'''

def rev_string(str1):

    if len(str1) % 4 == 0:
        return print(" ".join(reversed(str1)))
    else:
        print("Invalid length ..!")

s = input("Enter a String : ")
rev_string(s)
