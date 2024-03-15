a = "Hello"
b = "Python"
c = "Devloper"

d = a + b + c
print(d)

e = a + " " + b + " " + c
print(e)

#string fromating
age = 36
txt = "My name is Johnm, I am {}"
print(txt.format(age))


q = 3
iNo = 555
p = 50.00
myOrder = "I want {} pieces of item {} for {} dollars."
print(myOrder.format(q,iNo,p)) 


q = 3
iNo = 555
p = 50.00
myOrder = "I want to pay {2} dollars for {0} pieces of item no {1}."
print(myOrder.format(q,iNo,p)) 