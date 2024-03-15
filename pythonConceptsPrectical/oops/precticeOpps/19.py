class Bikeshop:
    def __init__(self,stock):
        self.stock = stock
        
    def displayBike(self):
        print("Available bikes in the shop are : ",self.stock)
        
    def rentForBike(self,qty):
        if qty <= 0:
            print('Enter the positive value or above zero..')
        elif qty > self.stock:
            print("Enter the value (less than stock)")
        else:
            self.stock = self.stock - qty
            print("---TOtal price of rent",qty*100)
            print("Now total bike are available : ",self.stock)

while True:
    obj = Bikeshop(100)
    print("1.Display Bike Stock")
    print("2.Rent a bike")
    print("3.Exit") 
    uc = int(input("What do you want : "))
    
    if uc == 1:
        obj.displayBike()
    elif uc == 2:
        n = int(input("How many Bike you want")) 
        obj.rentForBike(n)
    elif uc == 3:
        print("Exit")
    else:
        print("invaieled choice")          