#single list/blank list convert to Dictionry using function

def list_to_dict(list1):
    if len(list1) == 0:
        return dict()
    else:
        d = {}
        for i in range(0,len(list1),2):
            # key = list1[i]
            # value = list1[i+1]
            # d[key] = value
            d[list1[i]] = list1[i + 1]
        return d


empty_list = []
single_list = [1,2,3,4,5,6]

result_empty = list_to_dict(empty_list)
result_single_list = list_to_dict(single_list)

print(result_empty)
print(result_single_list)
            