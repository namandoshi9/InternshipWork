# 16. **Power of a Number:**
#     Implement a program to calculate the power of a number using a loop.

n = int(input("Enter numnber : "))
p = int(input("Enter the power you want to : "))

       
r = 1
for i in range(1,p+1):
    r *= n

print("Result is ", r)
        
