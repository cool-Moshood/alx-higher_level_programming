#!/usr/bin/python3
"""function that divides all elements of a matrix"""


def matrix_divided(matrix, div):

    r = []
    j = len(matrix[0])
    if type(matrix) is not list or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    for row in matrix:
        if len(row) != j:
            raise TypeError("Each row of the matrix must have the same size")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    r = [[round(x / div, 2) for x in row] for row in matrix]
    return r
