# Define a Car class with the following attributes: make, model, and year. Create two instances of the Car class and print their details.

#Method 1
class Car:
    make_company = ""
    model = ""
    year = ""
    
car1 = Car()
car2 = Car()

car1.make_company = "Toyota"
car1.model = "Camry"
car1.year = 2022

car2.make_company = "Honda"
car2.model = "Civic"
car2.year = 2021

print(f"The Car Make Compny is {car1.make_company} and Model is {car1.model} made by {car1.year}")
print(f"The Car Make Compny is {car2.make_company} and Model is {car2.model} made by {car2.year}")


#Method2
class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Honda", "Civic", 2021)

print(f"Car 1: {car1.make} {car1.model} ({car1.year})")
print(f"Car 2: {car2.make} {car2.model} ({car2.year})")
