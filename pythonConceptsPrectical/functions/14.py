def tri_recursion(k):
    if k > 0:
        r = k + tri_recursion(k-1)
        print(r)
    else:
        r = 0
    return r
        
    
print()    
tri_recursion(6)