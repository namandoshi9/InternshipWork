# * * * * *
# * * * *
# * * *
# * * 
# *

n = int(input("Enter Number : "))
for i in range(n):
    for j in range(i,n):
        print("*",end=' ')
        # print(n,end=' ') it's work
    print()


r = 5
n = r
for i in range(r,0,-1):
    for j in range(0,i):
        print(n,end=' ')
    print()

#logic
#  j j j j j
# i* * * * *
# i* * * *
# i* * * 
# i* * 
# i*