#Calculate the grade based on a given percentage.

n = float(input("Enter your percentage : "))

if (n <= 99.99) and (n > 70):
    print ("Grade: Distinction")
elif(n <= 70) and (n > 60):
    print ("Grade: First Class")
elif(n <= 60) and (n > 50):
    print ("Grade: Second Class")
elif(n <= 50) and (n > 35):
    print ("Grade: Pass")
elif (n <= 35) and (n >= 0):
    print ("Grade: Fail")
else:
    print("Invalid Marks")