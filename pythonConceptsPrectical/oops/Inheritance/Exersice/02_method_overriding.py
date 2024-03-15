# Create a base class Shape with a method area (not implemented). 
# Create a derived class Rectangle that inherits from Shape and implements the area method to calculate the area of a rectangle. 
# Create another derived class Circle that inherits from Shape and implements the area method to calculate the area of a circle. 
# Create instances of both Rectangle and Circle and print their areas.

class Shape:
    def __init__(self):
        pass
    def area(self):
        raise NotImplementedError("Subclasses must implement the area() method")
    
class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    
    def area(self):
        import math
        return math.pi * self.radius ** 2

rectangle = Rectangle(4, 5)
circle = Circle(10)

print("area of rectangle is : ",rectangle.area())
print("area of circle is : ",circle.area())