#Check if a given number is a perfect square.

n = int(input("Enter Number"))

x = int(n**0.5)
print(x)

if x*x == n:
    print(f"{n} is a Perfect Square")
else:
    print(f"{n} is not a Perfect Square")
