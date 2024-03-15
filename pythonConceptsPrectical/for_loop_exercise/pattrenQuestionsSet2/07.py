# 0 1 2 3 4 5 
# 0 1 2 3 4 
# 0 1 2 3 
# 0 1 2 
# 0 1
# 0

r = 6
for i in range(r,0,-1):
    for j in range(0,i):
        print(j,end=" ")
    print()