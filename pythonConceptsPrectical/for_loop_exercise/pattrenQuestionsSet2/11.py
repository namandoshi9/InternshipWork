# 5 4 3 2 1 
# 4 3 2 1
# 3 2 1
# 2 1 
# 1

r = 5
for i in range(0,r):
    for j in range(r-i,0,-1):
        print(j,end=" ")
    print()
    
    
#logic
# 0 to 6
# 5 to 0 -1 
# 5 4 3 2 1
# 1 to 6
# 4 to 0 -1
# 4 3 2 1