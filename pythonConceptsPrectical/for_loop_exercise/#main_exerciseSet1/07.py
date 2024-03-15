#w.a.p to count number of vowels in a string

li = ["a","e","i","o","u"]
cv = 0
txt = "Hello Python Programmer"

for i in txt.lower():
    if i in li:
        cv += 1

print("Total vowels in txt is : ",cv)