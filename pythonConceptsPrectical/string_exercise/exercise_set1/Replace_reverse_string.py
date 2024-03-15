
string="hello hoe are you"
a="hello"

def functon(a,x):
    if a in x:
        print("yes")
        print(string.replace("hello",a[::-1]))
    else:
        print("no")

functon(a,string)