# li = [1,2,4,6,-1,0,0,-5,2,-6,0]

# n = int(input("Which number you want to index : "))

# if n in li:
#     print(li.index(n))
# else:
#     print("-1")

    
# def check_index(li, n):
#     if n not in li:
#         return -1
#     else:
#         return li.index(n)

# li = [1,2,4,6,-1,0,0,-5,2,-6,0]
# n = int(input("Which number you want to index : "))
# print(check_index(li,n))



#using function
# def index_finder(n, li):
#     for index, value in enumerate(li):
#         if value == n:
#             return index
#     return -1

# li = [1,2,4,6,-1,0,0,-5,2,-6,0]

# n = int(input("Which number you want to index : "))

# print(index_finder(n, li))




#simple Method 2
li = [1,2,4,6,-1,0,0,-5,2,-6,0]
n = int(input("Which number you want to index : "))
for index, value in enumerate(li):
        if value == n:
            print(index)
            break
else:
    print("-1")