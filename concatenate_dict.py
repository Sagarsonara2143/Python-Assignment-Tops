#Write a Python script to concatenate following dictionaries to create a new one.

dic1={'a':10,'b':20}
dic2={'c':30,'d':40}
dic3={'e':50,'f':60}

dic4 = {}

all_dic=dic1, dic2, dic3        #stored all dictionary in one

for i in all_dic:                   # dictionary inserted on by one to dict4
    dic4.update(i)
print(dic4)
