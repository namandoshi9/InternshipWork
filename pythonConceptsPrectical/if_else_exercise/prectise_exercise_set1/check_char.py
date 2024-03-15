#Determine if a given character is a vowel or a consonant.
 
txt = input("Enter any charcter : ")
x = ['a','e','i','o','u']


if txt.lower() in x:
    print("Your Character is vowel : ",txt)
else:
    print("Your Character is Consonant : ",txt)