#q12 nested tuplw to dict
x = ((2,3),(4,5),(6,7))
k = {}

for i in x:
    print(i[0],i[1])
    k[i[0]] = i[1]

print(k)