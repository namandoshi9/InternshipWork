x = lambda a : a + 10
print(x(5))

x = lambda a,b : a + b
print(x(5,10))

def myfunc(n):
    return lambda a : a * n

nn = myfunc(5)
print(nn(2))



def myfunc(n):
    return lambda a : a * n

nn = myfunc(5)
nm = myfunc(6)

print(nn(11))
print(nm(12))