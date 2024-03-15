a = "Welcome to The, Python Taks.."
print(a)

# #this are comment section..

# x = 5
# y = "Hello Programmer"
# z = 20.5
# a = 1j
# b = ["Apple","banana"]
# c = ("apple", "tametos")
# d = range(5)
# e = {"apple": "Apple","banana":"BANANA"}
# f = {"apple","banana","rice"}
# g = frozenset({"apple","banana","cherry"})
# h = True
# i = b"hello" 
# j = bytearray(5)
# k = memoryview(bytes(5))
# l = None
# m = None 

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
# print(type(f))
# print(type(h))
# print(type(i))
# print(type(j))
# print(type(l))
# print(type(m))
# print(type(x))
# print(type(y))
# print(type(z))
# print(type(a))



# x = float(1)
# y = int(2.27)
# z = int("330")

# print("x :",x, " y:",y, " z:",z)


# a = "Hello Programmer"
# print("indexing : ",a[1])
# print("length of a : ",len(a))
# print("Chek Programmer : ","Programmer" in a)
# for x in "Hello":
#     print(x)
# if "devloper" not in a:
#     print("No, 'Devloper' is not present..")
# if "Programmer" in a:
#     print("Yes, 'Programmer' is present...")


# Slicing
# print(a[2:5]) 
# print(a[:5])
# print(a[1:])
# print(a[-11:-6])
# print(a.upper())
# print(a.lower())
# print(a.strip())
# print(a.replace("o", "H"))
# print(a.split(","))


# b = "Jay Aadinath {}"
# c = a + b 
# d = a + " " + b
# e = 9
# print(c)
# print(d)
# print(b.format(e))


# t1 = 3
# t2 = "apple"
# t3 = 100
# myOrder = "I want {} pieces of item {} for {} rupee."
# print(myOrder.format(t2,t1,t3))
# myOrder = "I want {1} pieces of item {0} for {2} rupee."
# print(myOrder.format(t1,t2,t3))

# txt = "We are the so-called \"vikings\" from the north"
# print(txt)
# x = txt.capitalize()
# print(x)
# x = txt.casefold()
# print(x)
# x = txt.center(20)
# print(x)
# x = txt.count("so-called")
# print(x)
# x = txt.encode()
# print(x)
# x = txt.find("are")
# print(x)
# x = txt.index("vikings")
# print(x)


# print(10 > 9)
# print(100==9)

# a = 200
# b = 20

# if b > a:
#     print("Nananananan")
# else:
#     print("hahahaha")

# print(bool("Hello"))
# print(bool(15))



# class myClass():
#     def __len__(self):
#         return 0

# myObj = myClass()
# print(bool(myObj))


# def myFunc():
#     return True
# if myFunc():
#     print("YES",myFunc())
# else:
#     print("No")


# x = 200
# print(isinstance(x, int))

# print(10+5,10-5,10**2)

# x = 5
# x += 3
# print(x)

# print((6+3)-(6+3))
# print(100+5*3)

# print(5+4-7+3)

# myl = ["Apple","Banana","Cherry","orange", "kiwi", "melon", "mango"]
# print(myl)
# print(len(myl))
# print(1,0,2)
# print(myl[1])
# print(myl[-1])
# print(myl[2:5])
# print(myl[:4])
# print(myl[2:])
# print(myl[-2:-5])

# if "apple" in myl:
#     print("Yes,Apple is here")

# myl[1] = "bananaaaa"
# print(myl)

# myl.insert(2,"Watermelon")
# print(myl)

# myl.append("orange")
# print(myl)

# myl1 = ["mango","kela","kachakela"]
# myl.extend(myl1)
# print(myl)

# myl.remove("mango")
# print(myl)

# myl.pop(1)
# print(myl)

# myl.pop()
# print(myl)


# del myl[0]
# print(myl)

# myl.clear()
# print(myl)

# for x in myl:
#     print(x)

# for i in range(len(myl)):
#     print(myl[i])

# i = 0
# while i < len(myl):
#     print(myl[i])
#     i = i + 1

# newl = []
# for x in myl:
#     if "a" in x:
#         newl.append(x)
# print(newl)


# myl.sort()
# myl.sort(reverse = True)
# print(myl)

# myl.sort(key = str.lower)
# print(myl)


# tp = ("apple","banana","cherry")
# print(tp)

# y = list(tp)
# print(y)

# y[1] = "KIWII"
# x = tuple(y)

# print(x)
# tp = (1,2,4,5,7,9,6,5,42,1)
# x = tp.index(42)
# print(x)

# ts = {"a","b","c"}
# ts1 = {"j","k","l"}
# ts.update(ts1)
# print(ts)

# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}

# set1.update(set2)
# print(set1)


# d = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(d)
# print(d["brand"])
# print(len(d))

# d1 = dict(name="naman",age="36")
# print(d1)

# x = d["model"]
# print(x)

# x = d.get("model")
# print(x)

# x = d.keys()
# print(x)

# x = d.keys()
# print(x)
# d["color"] = "blue"
# print(x)

# x = d.values()
# print(x)

# d["year"] = 9999
# print(x)

# print(d.items())

# myFam = {
#     "ch1" : {
#         "name" : "a",
#         "year" : 2004
#     },
#     "ch2" : {
#         "name" : "b",
#         "year" : 2005
#     },
#     "ch3" : {
#         "name" : "c",
#         "year" : 2006
#     }
# }

# print(myFam["ch2"]["name"])

# a = 13
# b = 3

# if a > b : print("a is greterthan b")
# if a > b:
#     print ("Yes")
# elif a == b:
#     print("Equals")
# else:
#     print ("NO")

# if a > 10:
#     print("above ten,")
#     if a > 20:
#         print("and also above 20!")
#     else:
#         print("but not above 20.")

# i = 1
# while i < 6:
#     print(i)
#     i += 1

# while i < 6:
#     print(i)
#     if i == 3:
#         break
#     i += 1

# i = 0
# while i < 6:
#     i += 1
#     if i == 3:
#         continue
#     print(i)

# for x in range(2,30,6):
#     print(x)

# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in adj:
#     for y in fruits:
#         print(x,y)


# def myFunc(*kids):
#   print("Hello form a function kids " + kids[0])

# myFunc("Naman "," Doshi", " janak")

# def myFam(food):
#   for x in food:
#     print(x)

# fruits = ["apple","banana","cherry"]

# myFam(fruits)


# def re(k):
#   if k > 0:
#     r = k + re(k - 1)
#     print(r)
#   else:
#     r = 0
#   return r

# print("\n\nRecursion Example Results")
# re(6)

# x = lambda a : a + 10
# print(x(5))
# x = lambda a,b : a * b
# print(x(5,6))

# def myFam(n):
#   return lambda a : a * n

# mydoub = myFam(2)

# print(mydoub(5))


# class person:
#   def __init__(self,name,age):
#     self.name = name
#     self.age = age

# p1 = person("naman",22)

# print(p1.name)
# print(p1.age)

# class perosn:
#   def __init__(self,name,age):
#     self.name = name
#     self.age = age

#   def __str__(self):
#     return f"{self.name}({self.age})"

# p1 = perosn("name",22)

# print(p1)


# class Vehicale:
#   def __init__(self,brand,model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("drive")

# class Car(Vehicale):
#   pass

# class Boat(Vehicale):
#   def move(self):
#     print("sail")


# car1 = Car("Ford","Mustang")
# boat1 = Boat("aba","baba")

# for i in (car1,boat1):
#   print(i.brand)
#   print(i.model)
#   i.move()


# import json
# x = '{"name":"naman","age":30,"city":"liliya"}'

# # y = json.loads(x)
# y = json.dumps(x)

# # print(y["age"])
# print(y)


# import re
# txt = "The rain in spain"
# x = re.split("\s",txt,1)
# print(x)

# try:
#   print(x)
# except NameError:
#   print("Variable x is not defined")
# except:
#   print("An exception ocurred")


# try:
#   print(x)
# except:
#   print("Somthing went wrong")
# finally:
#   print("The 'try except' is finished")

# try:
#   f = open("demo.txt")
#   try:
#     f.write("heloo moto")
#   except:
#     print("somthing went wrong")
#   finally:
#     f.close()
# except:
#   print("somthing went wrong...")

# f = open("demo.txt")
# f = open("demo.txt","rt")
# f = open("demo.txt","w")
# print(f.readline())
# for x in f:
#   print(x)
# f.close()
# f.write(" Now the file has more contet!")
# f.close()

# f = open("demo1.txt","x")

import os
os.remove("demo1.txt")