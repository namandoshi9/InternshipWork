#Write a python program to print sum of first N natural numbers.

n = int(input("Enter Number : "))
sumN = 0

for i in range(1,n):
    sumN += i

print("Sum of", n,"natural numbers is: ",sumN)