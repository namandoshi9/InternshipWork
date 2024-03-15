class Car:
    def __init__(self,make,model,year=2000):
        self.make = make
        self.model = model
        self.year = year
  
c1 = Car("Toyota", "Camry")
c2 = Car("Honda", "Civic", 2021)
      
print(c1.make,c1.model,c1.year)
print(c2.make,c2.model,c2.year)