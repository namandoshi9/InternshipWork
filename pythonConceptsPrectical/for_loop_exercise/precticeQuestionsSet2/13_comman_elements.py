# 13. **Common Elements:**
#     Given two lists, find and print the common elements between them.

n = int(input("how many number enter in list1 : "))
li1 = []
li2 = []
for i in range(n):
    num=int(input("Enter Number : "))
    li1.append(num)
print(li1)

n2 = int(input("how many number enter in list2 : "))
for i in range(n2):
    num=int(input("Enter Number : "))
    li2.append(num)

print("Your list1 is : ",li1)
print("Your list2 is : ",li2)

z = []
for i in li1:
    if i in li2:
        z.append(i)
print("Common element is ",z)
        
