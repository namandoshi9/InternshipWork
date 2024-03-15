"""
python program to convert temperature from fahrenheit to celsius
"""

f = int(input("Enter The Temperature in Fahrenheit : "))

if f >= 0:
    c = (f - 32) * 5/9
    print("Temperature in Celsius :", c)
else:
    print("Invalid Input")

