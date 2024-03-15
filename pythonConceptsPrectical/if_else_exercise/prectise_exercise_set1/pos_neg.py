#Check if a number is positive, negative, or zero

n = int(input("Enter Number : "))

if n == 0:
    print("Your number is zero : ",n)
elif n < 0:
    print("Your number is negative : ",n)
else:
    print("Your number is positive : ",n)