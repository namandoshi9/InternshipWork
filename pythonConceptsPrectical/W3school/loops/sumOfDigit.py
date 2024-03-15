#Calculate the sum of digits of a number entered by the user using a `while` loop.
#The program should prompt the user to enter a positive integer and then calculate its digit sum.
# def main():
#     num = int(input("Enter a positive integer: "))
#     if num < 0:
#         print("Please enter a positive integer.")
#         else:
#             digit_sum = 0
#             while num > 0:
#                 digit_sum += num % 10
#                 num //= 10
#                 print("The sum of the digits is", digit_sum)
#                 print("The total sum of the digits is", digit_sum)
#                 main()</s>


n = int(input("How many Numbers You want add : "))
i = 0
dsum = 0
while i < n:
    num = int(input("Enter Number : "))
    dsum += num
    i+=1

print("Sum of all numbers is ", dsum)
    
    



