class Shape:
    def __init__(self):
        pass
    
class Rect(Shape):
    def __init__(self,w,h):
        super().__init__()
        self.w = w
        self.h = h
        
    def area(self):
        return self.w * self.h
    
class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius  = radius 
    
    def area(self):
        return 3.14 * self.radius * self.radius 
    
r1 = Rect(3,4)
c1 = Circle(3)

print(r1.area())
print(c1.area())

     