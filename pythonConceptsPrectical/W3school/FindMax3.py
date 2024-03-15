"""
python program to print maximum among three number
"""
n1 = int(input("Enter The Number 1 : "))
n2 = int(input("Enter The Number 2 : "))
n3 = int(input("Enter The Number 3 : "))

if n1 > n2 and n1 > n2: 
    print(f"{n1} is graterthan {n2} and {n3}")
elif n2 > n1 and n2 > n3:
    print(f"{n2} is graterthan {n1} and {n3}")
else:
    print(f"{n3} is graterthan both {n1} and {n2}")