#w.a.p. to multiply all elements of list

li = [1,2,0,3,4,5]
# li2 = [] 
# for i in li:
#     x = i * i
#     li2.append(x)
# print(li2)

r = 1
li2 = []
for i in li:
    if i != 0:
        r *= i
        li2.append(r)
print(li2)