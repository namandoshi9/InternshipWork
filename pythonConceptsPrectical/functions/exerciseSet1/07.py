# 7. **Factorial Function:**
#    Write a function named `calculate_factorial` that computes the factorial of a given number.

def calculate_factorial(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f
    
num = int(input("Enter Number : "))
print("your factorial is : ",calculate_factorial(num))