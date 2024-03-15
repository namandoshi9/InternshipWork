# 10. **Count Vowels:**
#     Write a program to count the number of vowels in a given string.

txt = input("Enter String : ")
li = ['a','e','i','o','u']
c = 0
for i in range(len(txt)):
    if txt[i].lower() in li:
        print(txt[i],end=" ")
        c += 1
print("The Total vowels are : ",c)
    