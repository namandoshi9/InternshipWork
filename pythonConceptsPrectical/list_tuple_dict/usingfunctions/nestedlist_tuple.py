#w.a.p. nested list convert to the single tuple using function

def nestedlist_to_tuple(list1):
    result = []
    if len(list1) == 0:
        return tuple(list1)
    else:
        for item in list1:
            if isinstance(item, list):
                result.extend(nestedlist_to_tuple(item))
            else:
                result.append(item)
        return result

empty_list = [[],[]]
nested_list = [[1,2],[3],[4,5],[6,7]]

empty_result = nestedlist_to_tuple(empty_list)
result_nested_list = nestedlist_to_tuple(nested_list)

print(result_nested_list)
print(empty_result)