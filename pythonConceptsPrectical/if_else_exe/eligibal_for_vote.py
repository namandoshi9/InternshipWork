#Determine the eligibility for voting based on age.

age = int(input("Enter your age : "))

if age < 18:
    print("Sorry, you are not eligible to vote.")
elif age >= 18:
    print("Congratulations! You are now eligible to vote.")
else:
    print("Invaild input")