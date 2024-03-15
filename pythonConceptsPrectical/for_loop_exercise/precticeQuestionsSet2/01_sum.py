# 1. **Sum of Numbers:**
#    Write a program that calculates and prints the sum of all numbers from 1 to 100.


# print("The sum is:",sum(range(1,101)))  #Method 1

sum = 0
for i in range(1,101):
    sum = sum + i
print("The sum of 1 to 101 is : ",sum)    