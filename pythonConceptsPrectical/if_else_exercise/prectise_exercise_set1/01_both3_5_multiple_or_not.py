# Write a program to check if a given number is a multiple of both 3 and 5.

n = int(input("enter any number : "))


if (n%3 == 0) and (n%5 == 0):
    print(f"{n} is multiple of both 3 and 5 ")
else:
    print(f"{n} is not the multiple of both 3 and 5")