ml = ["apple","banana",34,"cherry",56,"apple"]
# print(ml)
# print(len(ml))
# print(type(ml))
# print(ml[1])
# print(ml[-1])
# print(ml[2:5])
# print(ml[:4])
# print(ml[2:])
# print(ml[-4:-1])
# if "apple" in ml:
#     print("YES")

# ml[1] = "blackapple"
# print(ml)

# ml[1:3] = ["aaa","bbb"]
# print(ml)


# ml.insert(2,"Watermelon")
# print(ml)
# ml.append("Orange")
# print(ml)
# ml2 = ["Mango","papaya"]
# ml.extend(ml2)
# print(ml)
# ml.remove("banana")
# print(ml)

# ml.pop(0)
# print(ml)
# ml.pop()
# print(ml)


# del ml2

# ml.clear()
# print(ml)


# for x in ml:
#     print(x)
# for x in range(len(ml)):
#     print(ml[x])


# i = 0
# while i < len(ml):
#     print(ml[i])
#     i = i + 1


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#   if "a" in x:
#     newlist.append(x)

# print(newlist)

# newml = ["hello" for x in fruits]


# fruits.sort()
# fruits.sort(reverse = True)
# print(fruits)


# def myFan(n):
#     return abs(n - 50)

# f = [100,20,65,42,320,2,9]
# f.sort(key = myFan)
# print(f)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# nl = []
# for i in fruits:
#     if "apple" != i:
#       nl.append(i)

# print(nl)  


nl = [x for x in range(10) if x < 5]
print(nl)

nl = [x.upper() for x in fruits]
print(nl)


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for i in list2:
    list1.append(i)
print(list1)