#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        new_list = my_list[0]
    for i in my_list:
        if new_list < i:
            new_list = i
    return new_list
