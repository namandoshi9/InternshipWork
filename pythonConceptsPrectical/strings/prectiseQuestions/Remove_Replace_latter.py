# How to Remove or replace Letters/Words From a String in Python
'''
EX1. INPUT : "Hello Python Programmer!"
     OUTPUT: "Hello Java Programmer!"

EX2. INPUT : "Hello Java Programmer!"
     OUTPUT: "Hello avaJ Programmer!"
'''
# EX.1
txt = "Hello Python Programmer!"
word = "Java"

new_string = txt.replace("Python", "Java")

if word in new_string:
    x = word[::-1]
    y = new_string.replace(word,x)
    print(y)
else:
    print("not match")
