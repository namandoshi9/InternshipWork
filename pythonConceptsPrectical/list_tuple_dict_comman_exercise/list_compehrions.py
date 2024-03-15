li = ["apple","banana","cherry"]
# [print(x) for x in li]

# neli = [x for x in li if "a" in x]
# print(neli)

# neli = [x for x in li if x != "apple"]
# print(neli)

# neli = [x for x in li]
# print(neli)

# neli = [x for x in range(1,5)]
# print(neli)

# neli = [x for x in range(10) if x < 5]
# print(neli)

# li = [x.upper() for x in li]
# print(li)

# li = ['hello' for x in li]
# print(li)

li = [x if x != "banana" else "orange" for x in li]
print(li)