# 3. **Filter Even Numbers:**
#    Use a lambda function with the `filter` function to filter out even numbers from a list.

li = [1,2,3,4,5,6,7,8,9,10]

filter_even = lambda x : x % 2 != 0

filterd_number = list(filter(filter_even,li))

print(filterd_number)