"""
Python Program to Check Division on the basis of marks obtained by students.
Percentage >= 60% : Division 1, Percentage >= 45% : Division 2,
Percentage >= 30% : Division 3, Percentage < 30% : Fail
"""
pr = int(input("Enter Your Percentage : "))

if pr >= 60 and pr < 100:
    print("Division 1")
elif pr >= 45 and pr < 60:
    print("Division 2")
elif pr >= 31 and pr < 45:
    print("Division 3")
elif pr <= 30:
    print("Failed!")
else:
    print("Invalid Percentage Entered.")