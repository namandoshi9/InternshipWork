#single list/blank list convert to tuple using function

def list_to_tuple(list1):
    if len(list1) == 0:
        return tuple()
    else:
        return tuple(list1)
    

empty_list = []
single_list = [1,2,3]

print("Empty List Converted To Tuple :",list_to_tuple(empty_list))

result_empty = list_to_tuple(empty_list)
result_single = list_to_tuple(single_list)   


print(result_empty)
print(result_single)