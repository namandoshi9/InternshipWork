#q10 balnk tuplw to convert dict
tp = (1,2,3,4)
d = {}

if len(tp) > 0:
    for i in range(0,len(tp),2):
        d[tp[i]] = tp[i + 1]
        print(type(d))
        print("Tuple convert to dict ",d)
else:
    x = dict(tp)
    print(type(x))
    print("Tuple is blank so dictionry also blank ",x)