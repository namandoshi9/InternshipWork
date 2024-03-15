#         *
#       * *
#     * * *   
#   * * * * 
# * * * * *


r = 6
for i in range(1,r):
    for j in range(r,0,-1):  
        if j > i:
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()
    
 
#logic    
#   1 2 3 4 5 
#   5 4 3 2 1 
#   - - - - - *
#   2 3 4 5
#   4 3 2 1
#   - - - - * *
#   3 4 5
#   3 2 1 
#   - - - * * * 
        