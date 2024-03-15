# Create a base class Person with attributes name and age. 
# Create a derived class Employee that inherits from Person and adds an additional attribute employee_id. 
# Create an instance of Employee and print its name, age, and employee ID.

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self,name,age,employee_id):
        super().__init__(name,age)
        self.employee_id = employee_id

emp1 = Employee("naman",22,1)
print(f"Name: {emp1.name}, Age: {emp1.age}, Employee ID: {emp1.employee_id}")
    