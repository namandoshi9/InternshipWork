# Generate and print the first 10 numbers in the Fibonacci series using a for loop.

n1,n2 = 0,1
c = 0
for i in range(0,11):
    if c < 10:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        c += 1

# 0,1,
# 0,
# 1
# 1 1
# 1 1
# 0 + 1
# = 1
# 1
# 0 + 1
# = 1
# 1
# 1 + 1
# = 2
# 2
# 2 + 1
# = 3
# 3
# 3 + 2
# = 5
# 5
# 5 + 3
# = 8
# 8
# 8 + 5
# = 13
   
