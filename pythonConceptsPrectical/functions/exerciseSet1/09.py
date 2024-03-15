# 9. **Sum of List Function:**
#    Write a function named `calculate_sum` that takes a list of numbers as input and returns their sum.

def calculate_sum(n):
    sumN = 0
    for i in range(n+1):
        sumN += i
    return sumN
    
num = int(input("Enter Number : "))
print(calculate_sum(num))

