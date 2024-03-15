class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def myFunc(self):
        print("Hello my name is : " + self.name)
        
p1 = Person("naman",36)

p1.age = 22

print(p1.age)