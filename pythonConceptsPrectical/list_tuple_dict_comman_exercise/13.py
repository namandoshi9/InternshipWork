#q13 balnk dict to convert list
d = {1:2,3:4}
li = []
if len(d) > 0:
    for i,j in d.items():
        tmp = [i,j]
        li.extend(tmp)
    print("Dictionry convert to List : ",li)
else:
    x = list(d)
    print(type(x))
    print("Dictionry is blank so list is also blank : ",x)