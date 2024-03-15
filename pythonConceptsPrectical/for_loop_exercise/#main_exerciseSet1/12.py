li = [1,2,4,6,-1,0,0,-5,2,-6,0]
dic = {'pos': 0, 'neg': 0, 'zero': 0}
for i in li:
    if i > 0:
        dic['pos'] += 1
    elif i < 0:
        dic['neg'] += 1
    else:
        dic['zero'] += 1
print(dic)  