"""
Python Program to Calculate Percentage and Grade of students 
on the basis of marks obtained in 5 subjects Maths,Physics,Chemistry,English and Hindi.
Marks of subject is taken as an input
Percentage >= 90% : Grade A, Percentage >= 80% : Grade B, Percentage >= 70% : Grade C,
Percentage >= 60% : Grade D, Percentage >= 40% : Grade F
"""

maths_marks = int(input("Enter Your Maths Marks : "))
physics_marks = int(input("Enter Your Physics Marks : "))
chemistry_marks = int(input("Enter Your Chemistry Marks : "))
english_marks = int(input("Enter Your English Marks : "))
hindi_marks = int(input("Enter Your Hindi Marks : "))

total_marks = (maths_marks + physics_marks + chemistry_marks + english_marks + hindi_marks) 
pr = total_marks / 500 * 100

print(f"Your Total Marks Is {total_marks} out of 500 and Youre Percentage is {pr}.")

if pr >= 90:
    print("Grade A")
elif pr >= 80:
    print("Grade B")
elif pr >= 70:
    print("Grade C")
elif pr >= 60:
    print("Grade D!")
else:
    print("Grade F.")