class Room:
    l = 0.0
    b = 0.0
    
    def cal_area(self):
        print("area of room = ",self.l*self.b)
        
sr = Room()

sr.l = 42.5
sr.b = 30.8

sr.cal_area()