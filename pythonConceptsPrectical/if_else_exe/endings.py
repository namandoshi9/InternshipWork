#Check if a year is a century year (ending in 00).

y = int(input("Enter Any year : "))

if y % 100 == 0:
    print('The year',y,'is a century year')
else:
    print('The year',y,'is not a century year')


