#Write a Python function that checks whether a passed string is palindrome or not.

#Example : - MAM, MADAM,

def checkPalindrome(str):
    left_side = 0
    right_side = len(str) - 1

    while right_side >= left_side:                      # Loop untill both side is meet
        if not str[left_side] == str[right_side]:       # check if both side character is not matched
            print(str,"is not Palindrome word")     
            return ""
        left_side = left_side + 1                               #Increment Left
        right_side = right_side - 1                             #Decrement Right
    print(str,"is Palindrome word")
    return ""
            

str = input("Enter String : ")
print(checkPalindrome(str))

