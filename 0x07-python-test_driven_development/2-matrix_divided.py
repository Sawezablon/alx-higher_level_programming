#!/usr/bin/python3
"""
Module matrix_divided
divides all elements

"""


def matrix_divided(matrix, div):
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for i in matrix:
        if len(matrix[0]) != len(i):
            raise TypeError("Each row of the matrix must have the same size")
        temp = []
        for j in i:
            if not isinstance(j, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
            temp.append(round(j / div, 2))
        new_matrix.append(temp)

    return new_matrix
