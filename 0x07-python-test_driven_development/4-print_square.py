#!/usr/bin/python3
"""function that prints a square with the character #"""


def print_square(size):
    """
    the size is the lnght of the square
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    for i in range(0, size):
        print("#" * size)
