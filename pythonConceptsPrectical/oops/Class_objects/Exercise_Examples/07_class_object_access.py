# Create a Rectangle class with attributes length and width. Add a method calculate_area that calculates and returns the area of the rectangle. 
# Create an instance of the Rectangle class and print its area.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width
    
rectangle = Rectangle(5,10)
print("Area of rectangle is", rectangle.calculate_area())