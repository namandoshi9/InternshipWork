#q3 nested list to nested tuple
l1 = [[1,2],[3,4],[5,6]]
x = []

for i in l1:
    x.extend(i)

res = tuple(x)
print(res)
