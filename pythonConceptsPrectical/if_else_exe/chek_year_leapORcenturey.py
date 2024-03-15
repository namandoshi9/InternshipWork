# Check if a year is a leap year and a century year simultaneously.

n = int(input("Enter any year : "))

if(n % 100 == 0) and (n % 400 == 0):
    print(f"{n} This year is leap year and a century year simultaneously")
elif(n % 4 == 0) and (n % 100 != 0):
    print(f"{n} year is leap year but not a century year")
elif(n % 4 == 0) and (n % 100 == 0):
    print(f"{n} year is century year but not a leap year")
else:
    print(f"{n} is niether leap or century year")