r = 5
for i in range(1,r+1):
    for j in range(r-i):
        print(" ",end="") 
    for j in range(i):
        print("* ", end="")
    print()
    
#     * 
#    * * 
#   * * *
#  * * * *
# * * * * *