def reverse_and_replace(original_str, word):
    if word.lower() in original_str.lower():
        reversed_word = word[::-1]
        result_str = original_str.replace(word, reversed_word)
        return result_str
    else:
        return "No match found."

str_value = "Hello world"
w = "hello"

output = reverse_and_replace(str_value, w)
print(output)
