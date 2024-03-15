# 10. **Palindrome Check Function:**
#     Create a function named `is_palindrome` that takes a string as input and returns True if it's a palindrome, False otherwise.

def is_pelindrome(txt):
    if txt == txt[::-1]:
        return True
    else:
        return False
    
txt = input("Enter String : ")
print(is_pelindrome(txt))