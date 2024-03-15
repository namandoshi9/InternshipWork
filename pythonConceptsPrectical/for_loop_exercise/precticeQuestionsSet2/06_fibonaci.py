# 6. **Fibonacci Sequence:**
#    Write a program to generate the Fibonacci sequence up to a certain number of terms.

n = int(input("Enter Number : "))

a = 0
b = 1

if n == 1 or n == 0:
    print(f"You enter {n} so fibonaci sequnce is {b}")
elif n < 0:
    print(f"You Enter {n} negetive number")
else:
    print("The first two numbers in the Fibonacci sequence are.")
    print(a)
    print(b)
    for i in range(2,n):
        c = a + b
        a = b
        b = c
        print(c)
        
        
        
#logic
# a = 0
# b = 1
# 1 = 0 + 1, c = a + b
# 1 = 1 , a = b
# 1 = 1 , b = c

# 1
# 1
# 2 = 1 + 1
# 2 = 2
# 2 = 2

# 1
# 2
# 3 = 2 + 1
# 3 = 3
# 3 = 3


# 2
# 3
# 5 = 3 + 2...