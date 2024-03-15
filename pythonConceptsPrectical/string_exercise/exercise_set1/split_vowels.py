#Split String on vowels

txt = "Hello Python Devloper!"
vwl = ['a', 'e', 'i', 'o', 'u']
res = []
temp = ""

for i in txt.lower():
    if i in vwl:
        if temp != "":
            res.append(temp)
            temp = ""
    else:
        temp += i

if temp != "":
    res.append(temp)

print(res)


