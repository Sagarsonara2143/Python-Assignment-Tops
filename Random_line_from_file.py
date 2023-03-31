#Write a Python program to read a random line from a file.
import random

file = open("random.txt","w")
file.write("This is Example of File Management in Python.\n")
file.write("Second Line Added in File\n")
file.write("Third Line Added in File\n")
file.write("Fourth Line Added in File\n")
file.write("Fifth Line Added in File\n")
file.close()

def rand_line(line):
    lines = open(line).read().splitlines()
    return random.choice(lines)


print(rand_line('random.txt'))
