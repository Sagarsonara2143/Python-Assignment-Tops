#Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle.

# area = pi*r*r
# perimeter =   2*pi*r

class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14
    
    def perimeter(self):
        return 2*self.radius*3.14

obj = Circle(8)
print("Area of Circle : ",obj.area())
print("Perimeter of Circle :",obj.perimeter())
