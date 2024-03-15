# Extend the Rectangle class from Exercise 3 to include a method is_square that returns True if the rectangle is a square and False otherwise.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width
    
    def is_square(self):
        if self.length == self.width:
            return True
        else:
            return False
    
rectangle = Rectangle(5,10)
print("Area of rectangle is", rectangle.calculate_area())
print("Area of rectangle 1: ",rectangle.is_square())
rect1 = Rectangle(5,5)
print("Area of rectangle is", rect1.calculate_area())
print("Area of rectangle 1: ",rect1.is_square())
        