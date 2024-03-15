# Write a program to check if a given number is a palindrome using a for loop.

num = input("Enter Any Number : ")
rev = "" 

for i in num: 
 rev = i + rev   
 
if(num == rev): 
 print("The num is a palindrome.") 
else: 
 print("The num is not a palindrome.")