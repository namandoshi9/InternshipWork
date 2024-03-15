print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 100
b = 33

if b > a:
    print("b is greater than a ")
else:
    print("b is not greater than a ")

print(bool("hello"))
print(bool(15))


bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})


class myClass():
    def __len__(self):
        return 0

myobj = myClass()
print(bool(myobj))


def myFan():
    return True
print(myFan())
if myFan():
    print("YES!")
else:
    print("NO!")