#single list/blank list convert to Set using function

def list_to_set(list1):
    if len(list1) == 0:
        return set()
    else:
        return set(list1)


empty_list = []
single_list = [1,2,3,4,5,6,"karan"]

result_empty_list = list_to_set(empty_list)
result_single_list = list_to_set(single_list)

print(result_empty_list)
print(result_single_list)