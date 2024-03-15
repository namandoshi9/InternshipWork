# Create a base class Animal with attributes name and sound. 
# Create a derived class Dog that inherits from Animal and has an additional attribute breed. 
# Create an instance of the Dog class and print its details.


class Animal:
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound

class Dog(Animal):
    def __init__(self,name,sound,breed):
        super().__init__(name,sound)
        self.breed = breed

dog1 = Dog("Buddy","woff woof", "Golden Retrie")
print(f"Name:{dog1.name}, Sound:{dog1.sound}, Breed:{dog1.breed}")
