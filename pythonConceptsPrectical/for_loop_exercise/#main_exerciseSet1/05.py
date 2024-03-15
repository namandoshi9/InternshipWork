#w.a.p to remove duplicate elements in list

li = [1,2,4,5,0,5,64,2,6,3,2,4,6,2,45]

# new_list = list(set(li))
# print("\nList after removing duplicates using Set: ", new_list)


#using for loop

newli = []
for i in li:
    if i not in newli:
        newli.append(i)

print("List after removing duplicates using For Loop: ", newli)
        


            