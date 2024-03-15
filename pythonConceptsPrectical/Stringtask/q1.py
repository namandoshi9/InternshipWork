str_value = "Hello world"
w = "hello"

if w.lower() in str_value.lower():
    reversed_w = w[::-1]
    result_str = str_value.replace(w, reversed_w)
    print(result_str)
else:
    print("No match found.")
