#Check if a number is a prime number.

n = int(input("Enter Any Number : "))

if n == 0:
    print("You Enter Zero")
elif n % 2 != 0:
    print(n," is prime number")
else:
    print(n, "is not a Prime number")