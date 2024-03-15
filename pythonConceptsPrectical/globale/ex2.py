gv = 100
def func():
    print("gv value " , gv)

def modify():
    global gv
    gv += 50

func()
modify()
print("Updated value " , gv)