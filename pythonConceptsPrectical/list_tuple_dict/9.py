#q9 nested tuplw to list
tp = ((1,2),(1,6),(3,4))
k = []

for i in tp:
    print(i[0],i[1])
    k.append(list(i))

print(k)