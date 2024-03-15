"""
python program to convert temperature from celsius to fahrenheit
"""

c = int(input("Enter The Temperature in celsius : "))

if c >= 0:
    f = (1.8 * c) + 32
    print("Temperature in Fahrenheit :", f)
else:
    print("Invalid Input")

