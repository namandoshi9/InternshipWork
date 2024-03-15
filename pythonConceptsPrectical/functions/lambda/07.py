# 7. **Sort List of Tuples:**
#    Sort a list of tuples based on the second element of each tuple using a lambda function and the `sorted` function.

# List of tuples
list_of_tuples = [(1, 5), (3, 2), (7, 8), (4, 1), (6, 9)]

sorted_tuples = sorted(list_of_tuples, key=lambda x: x[1])

print(sorted_tuples)

