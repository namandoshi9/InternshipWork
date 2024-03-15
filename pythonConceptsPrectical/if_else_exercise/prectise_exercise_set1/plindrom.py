#Determine if a given string is a palindrome.

txt = input("Enter Any String : ")

if txt[::-1] == txt:
    print(f"{txt} Is A Palindrome")
else:
    print(f"{txt} Is Not A Palindrome")