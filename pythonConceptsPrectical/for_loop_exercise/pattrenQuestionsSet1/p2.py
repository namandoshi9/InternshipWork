#         * 
#       * * 
#     * * * 
#   * * * * 
# * * * * * 

rows = 5
for i in range(rows):
    for j in range(rows, 0, -1):
        if j > i:
            print(" ", end=' ')
        else:
            print("*", end=' ')
    print("")


#logic
#   5 4 3 2 1 
#   j j j j j
#0 i            
#1 i        *  
#2 i      * *
#3 i    * * * 
#4 i  * * * *  