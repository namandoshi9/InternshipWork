#Python – Replace multiple words with K

txt = "Hello Python Programmer! How's for you.."

x = txt.split()

print(x)

w_list = ["Python","How's"]

r_word = "java"

for w in w_list:
    y = x.replace(w_list,r_word)
    print(y)
        
        
   