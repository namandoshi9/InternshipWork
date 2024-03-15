# 3. **Multiplication Table:**
#    Write a program that generates the multiplication table for a given number.

n = int(input("Which number Table you want to print : "))


print(f"Multiplication table of {n}")
for i in range(1,11):
    print(f"{n} * {i} = {n*i}")