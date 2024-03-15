#w.a.p to get the element with the hieghest count in a list

li = [2,4,5,41,2,4,6,2,4,6,2,56,2,4,6,7,8,9,0]

h_count = 0
num = li[0]

for i in li:
    x = li.count(i)
    if x > h_count:
        h_count = x
        num = i
print("highest count element is : ",num)
        