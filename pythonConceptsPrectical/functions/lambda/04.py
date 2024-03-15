# 4. **Multiply with a Constant:**
#    Write a lambda function that takes a number and multiplies it by a constant (e.g., 5).

num = int(input("Enter number : "))

multiply_constant = lambda x : x * num
print(f"The result of the multiplication is {multiply_constant(5)}")