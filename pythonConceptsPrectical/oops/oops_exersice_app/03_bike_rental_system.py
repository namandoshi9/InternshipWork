'''
w.a.p.p to bike rental system
1) Display available stoke/bike
2) Request a bike for rent (100rs -> 1qty)
3) exit
'''
class Bikeshop:
    def __init__(self,stock):
        self.stock = stock
    
    def displayBike(self):
        print("-----Available Bikes are : ",self.stock)
        
    def rentForBike(self,qty):
        if qty <= 0:
            print("Enter the positive value or above zero..")
        elif qty > self.stock:
            print("Enter the value (less than stock)")
        else:
            self.stock = self.stock - qty
            print("---Total price of rent : ",qty * 100)
            print("---Now Total bike are available : ",self.stock)
            

while True:
    obj = Bikeshop(100)
    print("1).Display Bike Stock")
    print("2).Rent a Bike")
    print("3).Exit")
    uc  = int(input("What do you want : "))
    
    if uc == 1:
        obj.displayBike()
    elif uc == 2:
        n = (int(input("How many bike you want ? -> ")))
        obj.rentForBike(n)
    elif uc == 3:
        print("--You are Exit Thank you for visit---")
    else:
        print("----Invailed Choice----")
        
        
    