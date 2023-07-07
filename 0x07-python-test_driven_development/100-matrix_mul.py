#!/usr/bin/python3
"""
Module matrix_mul
function that multiplies 2 matrices

"""


def matrix_mul(m_a, m_b):
    """
    function that multiplies 2 matrices
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")

    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    for i in m_a:
        if type(i) is not list:
            raise TypeError("m_a must be a list of lists")

    for i in m_b:
        if type(i) is not list:
            raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")

    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        for x in row:
            if type(x) is not int and type(x) is not float:
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for x in row:
            if type(x) is not int and type(x) is not float:
                raise TypeError("m_b should contain only integers or floats")

    rows_A = len(m_a)
    cols_A = len(m_a[0])
    rows_B = len(m_b)
    cols_B = len(m_b[0])

    if any(len(row) != cols_A for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    # Check if each row of m_b has the same size
    if any(len(row) != cols_B for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if cols_A != rows_B:
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
