"""
python program to check input is digit or not
"""
n = input("Enter The Number : ")

if n.isdigit():
    print(f"Yes, {n} is digit")
else:
    print(f"No, {n} is not a digit.")