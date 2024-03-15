def myfunc(n):
    return lambda a: a* n

mydb = myfunc(2)
mytri = myfunc(3)


print(mydb(11))
print(mytri(11))