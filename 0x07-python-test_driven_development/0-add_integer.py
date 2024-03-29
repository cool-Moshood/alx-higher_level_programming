#!/usr/bin/python3
"""function that adds 2 integers"""


def add_integer(a, b=98):

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")

    return a + b


if __name__ == '__main__':
    doctest.testfile("./tests/0-add_integer.txt")
