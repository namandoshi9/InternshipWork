class Vehicle:
    def __init__(self,make,model):
        self.make = make
        self.model = model
        
class Car(Vehicle):
    def __init__(self,make,model,year=2221):
        super().__init__(make,model)
        self.year = year
        
car = Car("Totata","abc",2022)

print(car.make,car.model,car.year)