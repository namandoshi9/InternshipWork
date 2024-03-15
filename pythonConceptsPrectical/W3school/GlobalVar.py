#Method 1
x = "Awesome "

def myFan():
    print("python is " + x)

myFan()


#Method 2
x = "Awesome "

def myFan():
    x = "fantastic"
    print("python is " + x)

myFan()
print("Python is " + x)


#global keyword
#Method 1
def myFan():
    global x
    x = "fantastic"
myFan()
print("Python is " + x)

#method 2
x = "Awesome"
def myFan():
    global x
    x = "fantastic"
myFan()
print("Python is "+x)