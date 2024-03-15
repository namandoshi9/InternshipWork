#Write a Python program using a for loop to print the numbers from 1 to 50 odd & Even number.
li1 = []
li2 = []

for i in range(1,50,2):
    li1.append(i)
print("Odd Number is : ",li1)
    
for i in range(1,50):
    if i % 2 == 0:
        li2.append(i)
print("Even Number is : ",li2)