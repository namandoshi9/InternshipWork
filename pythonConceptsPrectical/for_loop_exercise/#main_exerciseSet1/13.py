# li = [1,2,4,5,6,7,2]

# n = int(input("Which number you want to get index : "))

# if n in li:
#     print(f"{n} is at the index of {li.index(n)}")
# else:
#     print("-1")
        
        
def check_index(n):
    if n in li:
       return li.index(n)
    else:
        return -1
    
li = [1,2,4,5,6,7,2]    
n = int(input("Which number you want to get index : "))
check_index()