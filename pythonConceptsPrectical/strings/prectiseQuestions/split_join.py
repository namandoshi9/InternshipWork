#Python program to split and join a string

# Split the string into list of strings
# Input : Python for Python
# Output : ['Python', 'for', 'Python']

# Join the list of strings into a string based on delimiter ('-')
# Input :  ['Python', 'for', 'Python']
# Output : Python-for-Python


txt = "Hello Pyhton Programmer"
x = txt.split()
print(f'Split Text: {x}')

y = "-".join(x)
print(y)
