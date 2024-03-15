# Create a base class Animal with a method make_sound (not implemented). 
# Create two derived classes Dog and Cat that inherit from Animal and implement the make_sound method to return "Woof!" for Dog and "Meow!" for Cat.
# Create instances of both Dog and Cat and print the sounds they make.

class Animal:
    def __init__(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow Meow!"
        
d = Dog()
c = Cat()
print("Dog sound is",d.make_sound())
print("Cat sound is",c.make_sound())