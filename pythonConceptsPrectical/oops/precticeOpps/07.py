class Rectangle:
    def __init__(self,l,w):
        self.l = l
        self.w = w
        
    def cal_area(self):
        return self.l * self.w
    
r = Rectangle(5,10)
print(r.cal_area())