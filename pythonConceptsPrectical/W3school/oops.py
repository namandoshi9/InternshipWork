# class MyClass:
#     x = 5

# p1 = MyClass()
# print(p1.x)



# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# p1 = Person("naman",22)

# # print(p1)
# print(p1.name)
# print(p1.age)


# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"{self.name}({self.age})"

# p1 = Person("naman",22)

# print(p1)
# print(p1.name)
# print(p1.age)


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def myFun(self):
        print("Hello my name is " + self.name)

p1 = Person("naman",36)
p1.myFun()



class Person1:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def myFun(abc):
        print("Hello My Name Is : " + abc.name)

p1 = Person1("naman",22)
p1.age = 21
p1.myFun()
print(p1.age)