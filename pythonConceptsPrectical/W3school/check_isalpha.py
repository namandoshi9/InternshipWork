"""
python program to check input is Alpha,digit or Specail character
"""
n = input("Enter The Anyrhing : ")

if n.isalpha():
    print(f"Yes, {n} is Alpha")
elif n.isdigit():
    print(f"Yes, {n} is Digit")
else:
    print(f"No, {n} is not Alpha or Digit it's Specail Charcter")