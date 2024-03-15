a = "hello"
print(a)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua"""
print(a)


#string array
a = "hello world"
print(a[1])


#loop
for x in "hello":
    print(x)

#length
print(len(a))

#check 
print("world" in a)

#use if
if "hello" in a:
    print("yes , 'hello' is present..")

#check if not
print("naman" not in a)
if "naman" not in a:
    print("No, 'naman' is not present..")