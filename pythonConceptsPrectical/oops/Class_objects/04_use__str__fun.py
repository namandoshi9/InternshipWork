# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
        
# p1 = Person("naman",22)
# print(p1)


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"{self.name}({self.age})"
        
p1 = Person("naman",22)

print(p1)