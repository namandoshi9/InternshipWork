# class Person:
#     def __init__(self,fname,lname):
#         self.firstname = fname
#         self.lastname = lname

#     def printname(self):
#         print(self.firstname,self.lastname)

# x = Person("naman","doshi")
# x.printname()


# class Student(Person):
#     def __init__(self,fname,lname,year):
#         # Person.__init__(self,fname,lname)
#         super().__init__(fname,lname)
#         self.graduationyear = year

#     def welcome(self):
#         print("Welcom",self.firstname,self.lastname,"to the class of ",self.graduationyear)

# x = Student("Mike","Olsen",2019)
# x.printname()
# print(x.graduationyear)
# x.welcome()


# mytuple = ("apple","banana","cherry")
# myit = iter(mytuple)

# print(next(myit))
# print(next(myit))
# print(next(myit))

# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self

#     def __next__(self):
#         x = self.a
#         self.a += 1
#         return x

# myclass = MyNumbers()
# myiter = iter(myclass)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))



class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for i in myiter:
    print(i)