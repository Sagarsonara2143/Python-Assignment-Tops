#Write a Python program to calculate surface volume and area of a cylinder.

#Volume: π × r² × h         Surface area: 2πrh+2πr²

pi = 22/7

radius = float(input("Enter Radius : "))
height = float(input("Enter Height : "))

vol = pi * (radius * radius) * height
area = 2 *(pi * radius * height) + 2*(pi*radius**2)

print("Volume : ",vol)
print("Area :", area)
