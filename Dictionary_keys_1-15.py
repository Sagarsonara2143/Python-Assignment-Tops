#Write a Python script to print a dictionary where the keys are numbers between 1 and 15.

dic={}

for i in range(1,16):
    dic[i] = i*2                #Keys are 1 to 15 and values assigned as double of keys

print(dic)
