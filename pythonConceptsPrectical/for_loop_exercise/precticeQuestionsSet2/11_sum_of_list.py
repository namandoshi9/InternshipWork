# 11. **List Sum:**
#     Given a list of numbers, calculate and print the sum of all elements.

n = int(input("how many number enter in list : "))
li = []
for i in range(n):
    num=int(input("Enter Number : "))
    li.append(num)
print(li)
# print("The sum of li is ",sum(li)) #method 1
    
if len(li) == 0:
    print("list is empty")
else:
    c = 0
    for i in li:
        c += i
    print("the sum of list is : ", c)