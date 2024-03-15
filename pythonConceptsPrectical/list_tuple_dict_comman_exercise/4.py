#q4 balnk list to convert dict
l1 = [1,2,3,4,5,6]
d = {}
if len(l1) > 0:
    for i in range(0, len(l1), 2):
        d[l1[i]] = l1[i + 1]
        print(type(d))
        print("List convert to dict ",d)
else:
    x = dict(l1)
    print(type(x))
    print("List is blank so dictionry is also blank ",l1)

