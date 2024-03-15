class Car:
    make_compnay = ""
    model = ""
    year = ""
    
c1 = Car()
c2 = Car()

c1.make_compnay ="toyato"
c1.model = "camry"
c1.year = 2000

c2.make_compnay ="Honda"
c2.model = "Civic"
c2.year = 2001


print(c1.make_compnay,c1.model,c1.year)
print(c2.make_compnay,c2.model,c2.year)



class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        
c1 = Car("Toyota", "Camry", 2022)
c2 = Car("Honda", "Civic", 2021)

print(c1.make,c1.model,c1.year)
print(c2.make,c2.model,c2.year)