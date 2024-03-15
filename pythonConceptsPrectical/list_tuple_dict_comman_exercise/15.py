#q15 dict to nested list
y = {2:3,4:5,6:7} 
z = []
for i,j in y.items():
    print(i,j)  
    z.append([i,j])

print(z)