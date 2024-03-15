class Person:
    def __init__(Self,fname,lname):
        Self.firstName = fname
        Self.lastName = lname
    
    def printname(self):
        print(self.firstName,self.lastName)
        
class Student(Person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.g_year = year
        
    def welcome(self):
        print("Welcom",self.firstName,self.lastName,self.g_year)
        
        
x = Student("Naman","Doshi","2022")
x.welcome()        