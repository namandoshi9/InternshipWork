#Find The Maximum Repeated Chacrcter in string
#Method 1
txt = "HelloPythonProgrammerHwoareYouWhatdidYoulearn"
txt.lower()

c = {}

for i in txt:
    if i in c:
        c[i] += 1
    else:
        c[i] = 1

max_char = max(c,key=c.get)

print("the max repeated char is : ",max_char)
    

# METHOD : 2

def most_repeated_char(text):
    char_count = {}
    
    # Count occurrences of each character
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Find the character with the maximum count
    max_char = max(char_count, key=char_count.get)
    
    return max_char

# Example usage
text = "helloooNNNN"
result = most_repeated_char(text)

print("Most repeated character:", result)
