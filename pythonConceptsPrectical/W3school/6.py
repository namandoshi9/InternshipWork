#q6 nested list to dict
x = [[2,3],[4,5],[6,7]]

k = {}
k[z[0]] = z[1]
print(k)

for i in x:
    print(i[0],i[1])
    k[i[0]] = i[1]

print(k)