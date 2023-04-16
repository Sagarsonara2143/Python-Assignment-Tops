#Write a python program to find the longest words.

file = open("python.txt","w")
file.write("This is example of file management in python")
file.close()

file = open("python.txt","r")
#print(file.read())

longest_word = "a"

for i in file:
    for j in i.split():
        if len(j) > len(longest_word):
            longest_word = j
        else:
            continue
print("Longest Word :",longest_word)
         
file.close()
