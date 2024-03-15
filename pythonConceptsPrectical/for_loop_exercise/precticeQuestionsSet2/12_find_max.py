# 12. **Find Maximum:**
#     Write a Program to find the maximum value in a list of numbers.

n = int(input("how many number enter in list : "))
li = []
for i in range(n):
    num=int(input("Enter Number : "))
    li.append(num)
print(li)
print("The max number in list is : ",max(li))