class Rectangle:
    def __init__(self,l,w):
        self.l = l
        self.w = w
        
    def cal_area(self):
        return self.l * self.w
    
    def is_square(self):
        if self.l == self.w:
            return True
        else:
            return False    
        
r = Rectangle(5,10)
print(r.cal_area())
print(r.is_square())