# 2. **Factorial Calculator:**
#    Implement a program to calculate the factorial of a given number using a loop.

n = int(input("Enter number you want to get factorial : "))

f = 1

if n < 0:
    print(f"Sorry, Factorial does not exist you enter {n} negative numbers")
elif n == 0 or n == 1:
    print(f"You Enter {n} so your number factorial is 1")
else:
    for i in range(1,n + 1):
        f = f * i
    print(f"The Factorial of {n} is : {f}")
    

#logic        
# n = 5        
# in loop 1, 5 + 1 = 6
# f = 1 = 1 * 6
# 6 = 1 * 5 * 4 * 3 * 2