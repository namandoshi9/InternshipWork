# x = abs(-7.25)
# x = abs(3+5j)
# print(x)

# x = list(('apple','banana'))
# print(X)

# x = hex(255) #num convert to hexadecimal value
# print(x)

# x = ('apple','banana','cherry')
# y = id(x)
# print(y)

# x = iter(["apple","banana","cherry"])
# print(next(x))
# print(next(x))

# class myAge:
#     age = 22

# class myObj(myAge):
#     name = "naman"
#     age = myAge

# x = issubclass(myObj,myAge)

# print(x)

# x = isinstance(5,int)
# print(x)

# x = isinstance("Hello",(float,int,str))
# print(x)

# class myObj:
#     name = "naman"

# y = myObj()

# x = isinstance(y, myObj)
# print(x)


# x = globals()
# print(x)
# print(x["__file__"])

# class Person:
#     name = "naman"
#     age = 22
#     country = "BHARAT"

# x = getattr(Person,'age')
# print(x)


# mylist = ["apple","banana","cherry"]
# x = frozenset(mylist)
# print(x)

# x = format(0.5,'%')
# print(x)

# age = [5,12,17,18,24,32]

# def myFunc(x):
#     if x < 18:
#         return False
#     else:
#         return True

# ad = filter(myFunc,age)

# for x in ad:
#     print(x)


# x = 'print(55)'
# eval(x)


# x = ('apple','banana','cherry','dog')
# y = enumerate(x) #by defualt start 0
# y = enumerate(x,2) ex of start index
# print(list(y))
# print(dict(y))
# print(dict(x)) its given error


# x = divmod(5,2)
# print(x)


class Person:
    name = "naman"
    age = 22
    country = "india"

print(dir(Person))