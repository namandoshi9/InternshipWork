# Write a program to check if a given number is a palindrome using a for loop.


#method 1
# num = input("Enter Any Number : ")
# rev = "" 

# for i in num: 
#  rev = i + rev   
 
# if(num == rev): 
#  print(f"The {num} is a palindrome.") 
# else: 
#  print(f"The {num} is not a palindrome.")
 
 
 
#method 2
number = int(input("Enter a number: "))
num_str = str(number)

if num_str == num_str[::-1]:
    print(f"{number} is a palindrome")
else:
    print(f"{number} is not a palindrome")


 