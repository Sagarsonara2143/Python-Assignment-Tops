#Write a Python program to append text to a file and display the text.

file = open("example.txt","a")

file.write("This is Appended Text\n")
file.write("Second line of appended text\n")
file.close()

file=open("example.txt","r")
print(file.read())
file.close()
