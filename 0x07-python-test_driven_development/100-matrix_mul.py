#!/usr/bin/python3
"""function that multiplies 2 matrices"""


def matrix_mul(m_a, m_b):
    """multiplies two matrices
    Args:
        m_a (list): matrix a
        m_b (list): matric b
    Raises:
        TypeError: m_a must be a list
        TypeError: m_b must be a list
        TypeError: m_a must be a list of lists
        TypeError: m_b must be a list of lists
        ValueError: m_a can't be empty
        ValueError: m_b can't be empty
        TypeError: m_a should contain only integers or floats
        TypeError: m_b should contain only integers or floats
        TypeError: each row of m_a must be of the same size"
        TypeError: each row of m_b must be of the same size"
        ValueError: m_a and m_b can't be multiplied
    Returns:
        list: matrix_a * matrix_b
    """

    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for row in m_a:
        if row and type(row) is not list:
            raise TypeError("m_a must be a list of lists")
    for row in m_b:
        if row and type(row) is not list:
            raise TypeError("m_b must be a list of lists")
    for row in m_a:
        for ele in row:
            if type(ele) is not int and type(ele) is not float:
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for ele in row:
            if type(ele) is not int and type(ele) is not float:
                raise TypeError("m_b should contain only integers or floats")
    for row in m_a:
        if len(row) != len(m_a[0]):
            raise TypeError("each row of m_a must should be of the same size")
    for row in m_b:
        if len(row) != len(m_b[0]):
            raise TypeError("each row of m_b must should be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    """caculation of multiplies of 2 matrices"""
    mul_matrix = []

    for row_1 in m_a:
        li = 0
        l_row = []
        while li < len(m_b[0]):
            result = 0
            k = 0
            for column_1 in row_1:
                result += column_1 * m_b[k][li]
                k += 1
            l_row.append(result)
            li += 1
        mul_matrix.append(l_row)

    return mul_matrix
