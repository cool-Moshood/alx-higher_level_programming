#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    i = 0
    count = len(my_list)
    while count > i:
        print("{:d}".format(my_list[count - 1]))
        count -= 1
