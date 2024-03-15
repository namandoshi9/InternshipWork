#Global Variables
#1
# x = "Awesome"

# def myfun():
#     print("Python is " + x)

# myfun()




#2
# x = "Awesome"

# def myfun():
#     x = "Yes it is"
#     print("Python is " + x)

# myfun()

# print("python is " + x)





#3keyword global
# def myfun():
#     global x  #this keyword makes the x in this function refer to the x outside of this
#     x = "Fentastic"

# myfun()

# print("Python is " + x)





#4
x = "awesome"

def myfun():
    global x
    x = "fantastic"

myfun()

print("python is " + x)