# #method1
# ml = ["Apple","Banana","Cherry"]
# ml2 = ml.copy()
# print(ml2)

# #method 2
# ml3 = list(ml2)
# print(ml3)



#join Two list
l1 = ["a","b","c"]
l2 = [1,2,3]

#method 1
# l3 = l1 + l2
# print(l3)

#method 2
# for x in l2:
#     l1.append(x)
# print(l1)

#method3
l1.extend(l2)
print(l1)