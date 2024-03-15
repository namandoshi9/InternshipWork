class Shape:
    def __init__(self):
        pass
    
    def area(Self):
        pass
    
class Rectangle(Shape):
    def __init__(self,w,h):
        super().__init__()
        self.w = w
        self.h = h
        
    def area(self):
        return self.w * self.h
    
class Circle(Shape):
    def __init__(self,r):
        super().__init__()
        self.r = r
        
    def area(self):
        import math
        return math.pi * self.r ** 2
    
r = Rectangle(4,5)
c = Circle(10)

print(r.area())
print(c.area())
    