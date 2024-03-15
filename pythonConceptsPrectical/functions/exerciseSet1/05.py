# 5. **Even or Odd Function:**
#    Implement a function named `even_or_odd` that takes an integer as input and prints whether it's even or odd.

def even_or_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
num = int(input("Enter Number : "))
result = even_or_odd(num)
print(result)