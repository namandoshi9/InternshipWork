#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * *

rows = int(input("enter number of rows : "))
k = rows - 1

for i in range(0,rows):
    for j in range(0,k):
        print(end=" ")
    k -= 1
    for j in range(0,i+1):
        print("* ", end="")
    print()


 