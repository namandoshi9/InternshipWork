#write a python program to get print a list of all odd numbers in a given range

n = int(input("Enter Number : "))

for i in range(1,n+1):
    if i % 2 != 0:
        print(i)