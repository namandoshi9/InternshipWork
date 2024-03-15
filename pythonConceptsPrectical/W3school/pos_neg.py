"""
python program to check number is poisitive or negetive
"""
n = int(input("Enter The Number : "))

if n > 0:
    print(f"{n} is Positive Number")
elif n == 0:
    print(f"{n} is Zero")
else:
    print(f"{n} is Negative Number")