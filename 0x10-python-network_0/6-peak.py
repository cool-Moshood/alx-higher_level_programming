#!/bin/python3
""" function that finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """ find_peak definition """

    size = len(list_of_integers)
    if (size == 0):
        return
    mid_index = size // 2
    if (mid_index == size - 1 or list_of_integers[mid_index] >= list_of_integers[mid_index + 1]) \
            and (list_of_integers[mid_index] >= list_of_integers[mid_index -1] or mid_index == 0):
        return list_of_integers[mid_index]
    if (mid_index != size -1) and list_of_integers[mid_index + 1] > list_of_integers[mid_index]:
        return find_peak(list_of_integers[mid_index + 1:])
    else:
        return find_peak(list_of_integers[:mid_index])
