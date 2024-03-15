#           1 
#         1 2 
#       1 2 3 
#     1 2 3 4 
#   1 2 3 4 5

r = 6
for i in range(1,r):
    n = 1
    for j in range(r,0,-1):
        if j > i:
            print(" ",end=" ")
        else:
            print(n,end=" ")
            n += 1
    print()
    
    

