#Write a Python script to merge two Python dictionaries.

student = {1:"Sagar",2:"Raj",3:"Pratik"}
faculty = {4: "Sachin",5:"Surya"}

dic = student.copy()        #student dictionary copied to dic
dic.update(faculty)         #faculty dict added in last of dictionary
print(dic)
