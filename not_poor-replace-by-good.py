'''
    Write a Python program to find the first appearance of the substring
    'not' and 'poor' from a given string, if 'not' follows the 'poor',
    replace the whole 'not'...'poor' substring with 'good'.
    Return the resulting string.
'''

s = input("Enter String : ").lower()

print(s)

a = s.find("not")

b = s.find("poor")

#print(a)
#print(b)

if b > a:
    print(s.replace(s[a:(b+4)],"good"))


