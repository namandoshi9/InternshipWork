#capitalize() Uppercase only First letter/charcter
txt = "hello python Devloper"
x = txt.capitalize()
print(x)



#casefold() string convert to lowercase
txt = "Hello python Devloper"
x = txt.casefold()
print(x)



#center() create space around words
txt = "banana"
x = txt.center(20)
print(x)

txt = "banana"
x = txt.center(20,"-")
print(x)



#count() count the total
txt = "apple apple orange banana"
x = txt.count("apple")
print(x) 

txt = "apple apple orange banana"
x = txt.count("a")
print(x)

txt = "apple apple orange banana"
x = txt.count("e",10,24)
print(x)



#encode() return encode value
txt = "Hello World! Ståle"
x = txt.encode()
print(x)

txt = "Hello World! Ståle"
print(txt.encode(encoding="ascii",errors="replace"))



#endswith() check string end
txt = "I love Python!"
x = txt.endswith("Python!")
print(x)

txt = "I love Python!"
x = txt.endswith("!")
print(x)

txt = "I love Python!"
x = txt.endswith("Python!",5,11)
print(x)

txt = "I love Python!"
x = txt.endswith(".")
print(x)



#expandtabs() set the tab size
txt = "H\te\tl\tl\to"
x = txt.expandtabs()
print(x)

txt = "H\te\tl\tl\to"
x = txt.expandtabs(2)
print(x)



#find() search specific value
txt = "Hello, welcome to my world."
x = txt.find("e")
print(x)

x = txt.find("welcome")
print(x)

x = txt.find("Python")
print(x)

x = txt.find("e",5,10)
print(x)



#format() formatting the specific value
txt = "For only {price:.2f} dollars!"
print(txt.format(price=49))

#placeholder
txt1 = "My name is {fname}, I am {age} year old !".format(fname="naman",age=22)
txt2 = "My name is {0}, I am {1} year old !".format("naman",22)
txt3 = "My name is {}, I am {} year old !".format("naman",22)
print(txt1)
print(txt2)
print(txt3)



#index() indexing the word/char
txt = "Hello, welcome to my world."
x = txt.index("welcom")
print(x)

x = txt.index("e")
print(x)

x = txt.index("e",5,15)
print(x)



#isalnum() check alpha and numeric both in string
txt = "Company12"
x = txt.isalnum()
print(x)

txt = "Company 12"
x = txt.isalnum()
print(x)



#isalpha() check only alpha in string
txt = "CompanyX"
x = txt.isalpha()
print(x)

txt = "Company X"
x = txt.isalpha()
print(x)



#isascii() 
txt = "Company12"
x = txt.isascii()
print(x)

txt = "Company 12"
x = txt.isascii()
print(x)



#isdecimal() 
txt = "1234"
x = txt.isdecimal()
print(x)

txt = "Company 12"
x = txt.isdecimal()
print(x)



#isdigit() 
txt = "12346"
x = txt.isdigit()
print(x)

txt = "Company 12"
x = txt.isdigit()
print(x)



#isidentifier() 
a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"

print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())



#islower()
a = "Hello world!"
b = "hello 123"
c = "mynameisPeter"

print(a.islower())
print(b.islower())
print(c.islower())



#isnumeric()
a = "12456"
b = "\u00B2" #unicode for ²
c = "10km2"
d = "-1"
e = "1.5"

print(a.isnumeric())
print(b.isnumeric())
print(c.isnumeric())
print(d.isnumeric())
print(e.isnumeric())



#isprintable()
txt = "Hello! Are you #1?"
x = txt.isprintable()
print(x)

txt = "Hello!\nAre you #1?"
x = txt.isprintable()
print(x)



#istitle()
a = "HELLO, AND WELCOME TO MY WORLD"
b = "Hello"
c = "22 Names"
d = "This Is %'!?"

print(a.istitle())
print(b.istitle())
print(c.istitle())
print(d.istitle())



#isupper()
a = "Hello World!"
b = "hello 123"
c = "MY NAME IS PETER"

print(a.isupper())
print(b.isupper())
print(c.isupper())



#join() join two(tuple,list,string,char(all item))
myTuple = ("naman","doshi","22")
x = "#".join(myTuple)
print(x)

myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"
x = mySeparator.join(myDict)
print(x)