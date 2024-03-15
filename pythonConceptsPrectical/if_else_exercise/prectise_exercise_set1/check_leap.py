#Check if a year is a leap year.

n = int(input("Enter any year : "))

if(n % 100 == 0) and (n % 400 == 0):
    print("This year is leap year : ",n)
elif(n % 4 == 0) and (n % 100 != 0):
    print("This year is leap year : ",n)
else:
    print("This year is not a leap year : ",n)
