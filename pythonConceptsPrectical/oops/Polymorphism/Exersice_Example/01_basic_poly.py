# Create a base class Shape with a method area (not implemented). 
# Create two derived classes Rectangle and Circle that inherit from Shape and implement the area method to calculate the area of a rectangle and a circle, respectively. 
# Create instances of both classes and print their areas.

class Shape:
    def __init__(self):
        pass
    
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
        self.radius  = radius 
    
    def area(self):
        return 3.14 * self.radius * self.radius 
    
rectangle = Rectangle(5, 8)
circle = Circle(3)

print(f"Rectangle Area: {rectangle.area()}")
print(f"Circle Area: {circle.area()}")