#w.a.p to print all factore of a number

n = int(input("Enter Number You want to get factor : "))
for i in range(1,n+1):
    if i % 2 == 0:
        print(i, end=" ")