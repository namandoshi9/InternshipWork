# Python Program to Check if a String is Palindrome or Not

#method 1
txt = "naman"
x = txt[::-1]

if x == txt:
    print("The string is palindrome")
else:
    print("The string is not palindrome")


#method 2
def isPalindrome(s):
    return s == s[::-1]

s = "naman"
x = isPalindrome(s)

if x:
    print("Yes")
else:
    print("No")



            