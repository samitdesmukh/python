def reverse_nested_list(lst):
    if isinstance(lst,list):
        return[reverse_nested_list(sublist) for sublist in reversed(lst)]
    else:
        return lst
nested_list=[[1,2],[3,[4,5]],6]
reversed_list= reverse_nested_list(nested_list)
print(reversed_list)