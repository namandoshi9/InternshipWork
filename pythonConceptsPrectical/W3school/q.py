#nested list convert to dictionry

#q1 balnk list to convert tuple
#q2 list to convert tuple
#q3 nested list to nested tuple
#q4 balnk list to convert dict
#q5 list to convert dict hint:indexing odd/even
#q6 nested list to nested dict
#q7 balnk tuplw to convert list
#q8 tuplw to convert list
#q9 nested tuplw to nested list
#q10 balnk tuplw to convert dict
#q11 tuplw to convert dict
#q12 nested tuplw to nested dict
#q13 balnk dict to convert list
#q14 dict to convert list
#q15 nested dict to nested list
#q16 balnk dict to convert tuple
#q16 dict to convert tuple
#q17 nested dict to nested tuple


#q6 nested list to nested dict
# x = [[2,3],[4,5],[6,7]]

# k = {}
# k[z[0]] = z[1]
# print(k)

# for i in x:
#     print(i[0],i[1])
#     k[i[0]] = i[1]

# print(k)





#dict convert to nested list
    
y = {2:3,4:5,6:7} 
z = []
for i,j in y.items():
    print(i,j)  
    z.append([i,j]) 

# for i in y.keys():
#     print(i)

# for j in y.values():
#     print(j)


# z.extend()
# print(z)
# print(y.items())