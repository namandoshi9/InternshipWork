#Determine the season based on the month.

month = int(input("Enter Any Number Month : "))
lst = [1,2,11,12]

if month in range(3,7):
    print("Summer")
elif month in range(7,11):
    print("Monsoon")
elif month in lst:
    print("winter")
else:
    print("Invalid Input")






#method 2
# n = int(input("Enter Any Number Month : "))

# month_no = {12: "Winter", 3: "Spring", 6: "Summer", 9: "Autumn"}

# season_list = [12,3,6,9]

# if n in season_list:
#     print("The Season is ",month_no[n])
# else:
#     print("Invalid Input")






#using function simple method 3
# def determine_season(month):
#     if month in range(3, 6):
#         return "Spring"
#     elif month in range(6, 9):
#         return "Summer"
#     elif month in range(9, 12):
#         return "Autumn"
#     else:
#         return "Winter"

# month = int(input("Enter month: "))
# season = determine_season(month)
# print("The season is: ", season)