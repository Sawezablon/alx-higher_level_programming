#!/usr/bin/python3
"""Module pascal_triangle"""


def pascal_triangle(n):
    """function that returns a list of lists of integers"""
    if n <= 0:
        return []

    tri = [[1]]
    while len(tri) != n:
        new = tri[-1]
        temp = [1]
        for i in range(len(new) - 1):
            temp.append(new[i] + new[i + 1])
        temp.append(1)
        tri.append(temp)
    return tri
