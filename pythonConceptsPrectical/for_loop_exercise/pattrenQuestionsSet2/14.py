#           1 
#         2 1 
#       3 2 1
#     4 3 2 1
#   5 4 3 2 1

r = 6
for i in range(1,r):
    for j in range(r,0,-1):
        if j > i:
            print(" ",end=" ")
        else:
            print(j,end=" ")
    print()