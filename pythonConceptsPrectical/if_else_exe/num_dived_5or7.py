#Check if a number is divisible by both 5 and 7.

n = int(input("Enter Any Number : "))

if (n % 5 == 0) and (n % 7 == 0):
    print(n," is divisible by both number 5 and 7")
else:
    print(n, "is not divisible by both the numbers 5 and 7")