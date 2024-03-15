#Create a program to calculate the sum of all prime numbers within a given range.

li = []
c = 0
n = int(input("How many elements You want to enter a list : "))
for i in range(0,n):
    e = int(input("Enter Any Number In list : "))
    li.append(e)
print(li)

for x in li:
    if x % 2 != 0:
        c = c + x
        
print("The sum of prime number is : ",c)
    

