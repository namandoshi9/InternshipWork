class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
class Employee(Person):
    def __init__(self, name, age, e_id):
        super().__init__(name, age)
        self.e_id = e_id
            
e1 = Employee("naman",22,1)
print(e1.name,e1.age,e1.e_id)