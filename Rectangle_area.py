#Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle.

# area_of_rec = len X width


class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def rectangle_area(self):
        return self.length*self.width

area = Rectangle(12, 10)
print("Area of Rectangle is : ",area.rectangle_area())

