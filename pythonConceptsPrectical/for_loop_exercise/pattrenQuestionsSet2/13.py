#           1 
#         2 2 
#       3 3 3
#     4 4 4 4
#   5 5 5 5 5

r = 6
for i in range(1,r):
    for j in range(r,0,-1):
        if j > i:
            print(" ",end=" ")
        else:
            print(i,end=" ")
    print()