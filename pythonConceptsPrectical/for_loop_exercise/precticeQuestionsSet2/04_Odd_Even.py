# 4. **Even or Odd:**
#    Create a program that takes a user input and prints whether the number is even or odd.

# n = int(input("Enter a number : "))

        
# Taking user input
n = int(input("Enter a number: "))

for i in range(2):
    if n % 2 == 0:
        print(f"{n} is an even number.")
    else:
        print(f"{n} is an odd number.")
    break

