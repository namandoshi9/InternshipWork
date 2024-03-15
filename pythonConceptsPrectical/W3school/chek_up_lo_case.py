"""
python program to check text is Upper or lower
"""
txt = input("Enter Any Text : ")

if txt.isupper():
    print(f"The text is in uppercase: {txt}")
elif txt.islower():
    print(f"The text is in lowercase: {txt}")
else:
    print(f"The text contains both upper and lower case letters: {txt}")