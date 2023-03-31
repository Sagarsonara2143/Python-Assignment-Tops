#Write a Python script to sort (ascending and descending) a dictionary by value. (Google)
import operator
dic = {
            "X" : 40,
            "Y" : 50,
            "Z" : 30
            }

print(dic)

dic_sort = dict(sorted(dic.items(),key=operator.itemgetter(1)))
print("Dictionary in ascending order :-",dic_sort)

dic_sort2 = dict(sorted(dic.items(),key=operator.itemgetter(1),reverse=True))
print("Dictionary in descending order :-",dic_sort2)






