# txt = "Hello!9 You are python Programmer Welcome."
# txt1 = "My Name is {fname}, I'm {age}"
# txt2 = "My Name is {0}, I'm {1}"
# txt3 = "Hello! {name} You are python\t Programmer\t Welcome."
# txt4 = "hello9"
# x = txt.capitalize() #Convert the first character to upper case
# x = txt.casefold()  #Converts string into lower case
# x = txt.center(50) #Return a centerd string
# x = txt.center(50,"-")
# x = txt.count("e") #Returns the number of times a specified value occurs in a string
# x = txt.count("o",10,50)
# x = txt.encode() #Returns an encoded version of the string
# x = txt.encode(encoding="ascii",errors="backslashreplace")
# x = txt.endswith(".")#returns true if the string ends with the specified value
# x = txt.endswith("Welcome.")
# x = txt.endswith("Programmer",5,10)
# x = txt.expandtabs(2)#see the tab size of the string
# x = txt.find("Welcome")#searches the string for a specified value and returns the position of where it was found
# x = txt.find("e")
# x = txt.find("e",5,10)
# x = txt.format(name = "Naman")#formates specified values in a string
# x = txt1.format(fname = "Naman",age = 22)
# x = txt2.format("Naman",22)
# x = txt.index("e")
# x = txt.isalnum()
# x = txt4.isalnum()
# print(x)




# txt = ("A","a","b","B")
# x = "#".join(txt)
# x = "-".join(txt)
# x = " ".join(txt)
# print(x)


# myDict = {"name" : "naman", "Country" : "Bharat"}
# mySep = "YES"
# x = mySep.join(myDict)
# print(x)


# txt = "     Apple       "
# x = txt.lstrip()
# y = txt.strip()
# z = txt.rstrip()
# print(x)
# print(y)
# print(z)


# txt = "bi naman"
# x = "abc"
# y = "bca"

# z = str.maketrans(x,y)
# print(z)
# print(txt.translate(z))


# txt = "Hello world"
# x = "hello"[::-1]

# print(txt.maketrans(x))


# txt = "I could eat, bananas all day"
# x = txt.partition("bananas")
# x = txt.replace("bananas","apples")
# x = txt.split()
# x = txt.split(",")
# x = txt.swapcase()
# print(x)


mydict = {83:80}
txt = "Hello Naman!"
print(txt.translate(mydict))