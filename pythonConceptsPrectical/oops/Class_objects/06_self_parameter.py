class Person:
    def __init__(mysillyobject,name,age):
        mysillyobject.name = name
        mysillyobject.age = age
    
    def myfunc(abc):
        print("Hello my name is "+ abc.name)
        
p1 = Person("naman",22)
p1.myfunc()