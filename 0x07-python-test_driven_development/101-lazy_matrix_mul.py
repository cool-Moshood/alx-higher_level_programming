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

    return np.dot(m_a, m_b).tolist()


if __name__ == '__main__':
    doctest.testfile("./tests/101-lazy_matrix_mul.txt")
