str_value = "Hello world"
w = "hello"

if w.lower() in str_value.lower():
    reversed_w = w[::-1]
    result_str = str_value.replace(w, reversed_w)
    print(result_str)
    # print(str_value.replace(w,w[::-1]))
else:
    print("No match found.")



# string="hello hoe are you"
# a="hello"

# def functon(a,x):
#     if a in x:
#         print("yes")
#         print(string.replace("hello",a[::-1]))
#     else:
#         print("no")

# functon(a,string)