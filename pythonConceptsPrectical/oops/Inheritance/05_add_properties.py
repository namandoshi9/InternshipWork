class Person:
    def __init__(self,fname,lname):
        self.first_name = fname
        self.last_name = lname
        
    def printname(self):
        print(self.first_name,self.last_name)
        
class Student(Person):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)
        self.g_year = 2022
        
x = Student("Naman","Doshi")
print(x.g_year)
