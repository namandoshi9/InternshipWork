# 5. **Palindrome Checker:**
#    Implement a program to check if a given string is a palindrome.

n = input("Enter you want to check palindrome or not : ")

i = 0
for i in range(len(n)):
   if n[i] != n[-1-i]:
      print(n,'is not a Palindrome')
      break
else:
   print(n,'is a Palindrome')
    