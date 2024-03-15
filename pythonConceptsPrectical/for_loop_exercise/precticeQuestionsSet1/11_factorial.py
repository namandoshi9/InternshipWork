# Write a program to calculate the factorial of a given number using a for loop.

num = int(input("Enter a number: "))

factorial = 1

if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)


#logic
# 1 2 3 4 5 
# 1 * 1 = 1
# 1 = 2 * 1 = 2
# 2 = 3 * 2 = 6
# 6 = 4 * 6 = 24
# 24 = 5 * 24 = 120
