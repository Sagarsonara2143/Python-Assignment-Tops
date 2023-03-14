# Write a Python program to test whether a passed letter is a vowel or not.

letter = input("Input Letter : ")

if letter.lower() in ('a','e','i','o','u'):
    print(letter ,"is Vowel")
else:
    print(letter, "is Consonant")
