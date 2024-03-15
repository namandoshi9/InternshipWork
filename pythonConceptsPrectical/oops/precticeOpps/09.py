class Animal:
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound
    
class Dog(Animal):
    def __init__(self,name,sound,breed):
        super().__init__(name,sound)
        self.breed = breed
        
d1 = Dog("Buddy","woof","golden")
print(d1.name,d1.sound,d1.breed)
