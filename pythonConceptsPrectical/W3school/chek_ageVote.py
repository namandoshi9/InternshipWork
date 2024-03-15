"""
python program to check whether a person is valid for vote or not using if-else
"""

y = int(input("Enter Your Age : "))

if n >= 18:
    print(f"{y} Congratulation! You are eligible..")
elif n < 18:
    print(f"{y} Sorry! You are not eligible..")
else:
    print("Invalid Input")
