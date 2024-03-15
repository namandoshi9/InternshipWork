"""
python program to check year is Leapyear or non leapyear
"""

y = int(input("Enter The Year : "))

if y % 100 == 0 and y % 400 == 0:
    print(f"{y} is Leap Year")
elif y % 4 == 0 and y % 100 != 0:
    print(f"{y} is Leap Year")
else:
    print(f"{y} is Not Leap Year")