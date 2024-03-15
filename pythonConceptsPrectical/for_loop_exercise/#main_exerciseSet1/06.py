#w.a.p to get the key from a dict which will have the minimum value
dic = {0:1,1:25,2:20,3:5}

min_val = min(dic.values())
for i,j in dic.items():
    if j == min_val:
        print(j)
    
# print(min_val)
    
    