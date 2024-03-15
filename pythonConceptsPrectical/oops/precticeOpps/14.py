class Animal:
    def __init__(self):
        pass
    
class Dog(Animal):
    def make_sound(self):
        return "Woof"
    

class Cat(Animal):
    def make_sound(self):
        return "meow"
    
d = Dog()
c = Cat()

print(d.make_sound())
print(c.make_sound())