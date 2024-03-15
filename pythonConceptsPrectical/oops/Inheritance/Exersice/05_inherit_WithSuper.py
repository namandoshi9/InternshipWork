# Create a base class Vehicle with attributes make and model. 
# Create a derived class Car that inherits from Vehicle and adds an additional attribute year. 
# Override the __init__ method in the Car class to include the year attribute. 
# Create an instance of Car and print its make, model, and year.

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model)
        self.year = year

car = Car("Toyota", "Camry", 2022)

print(f"Make: {car.make}, Model: {car.model}, Year: {car.year}")

        