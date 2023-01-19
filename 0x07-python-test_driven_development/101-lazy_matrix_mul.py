#!/usr/bin/python3
"""function that multiplies 2 matrices by using the module NumPy"""
import numpy as np
import doctest


def lazy_matrix_mul(m_a, m_b):
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
            raise TypeError("each row of m_a must be of the same size")
    for row in m_b:
        if len(row) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    return np.dot(m_a, m_b).tolist()


if __name__ == '__main__':
    doctest.testfile("./tests/101-lazy_matrix_mul.txt")
