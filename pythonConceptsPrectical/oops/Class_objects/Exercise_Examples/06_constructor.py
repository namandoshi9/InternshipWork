# Modify the Car class from Exercise 1 to include a default constructor that sets the year to 2022 if not provided.

class Car:
    def __init__(self,make,model,year=2022):
        self.make = make
        self.model = model
        self.year = year

car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic", 2021)

print(f"Car 1: {car1.make} {car1.model} ({car1.year})")
print(f"Car 2: {car2.make} {car2.model} ({car2.year})")