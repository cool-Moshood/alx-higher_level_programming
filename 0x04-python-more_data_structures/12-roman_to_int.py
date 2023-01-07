#!/usr/bin/python3
""" Roman to Integer test file
"""
roman = __import__('roman').roman


def roman_to_int(roman_string):
    x = 0
    y = 0
    if not roman_string or type(roman_string) != str:
        return 0
    while y < len(roman_string):
        s1 = roman(roman_string[y])
        if y + 1 < len(roman_string):
            s2 = roman(roman_string[y + 1])
            if s1 >= s2:
                x = x + s1
                y = y + 1
            else:
                x = x + s2 - s1
                y = y + 2
        else:
            x = x + s1
            y = y + 1
    return x
