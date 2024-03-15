#find most repeated number and find index using function
list1 = []

max_count = 0

if len(list1) == 0:
    print("list is empty")
else:
    for i in list1:
        count_ele = list1.count(i)
        if(count_ele > max_count):
            tmp = i
    print(tmp)
        
   






