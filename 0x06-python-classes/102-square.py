#!/usr/bin/python3
"""My square"""


class Square:
    """function"""

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        return self.__size * self.__size

    def __lessE__(self, other):
        return self.area() <= other.area()

    def __less__(self, other):
        return self.area() < other.area()

    def __greaterE__(self, other):
        return self.area() >= other.area()

    def __notE__(self, other):
        return self.area() != other.area()

    def __greater__(self, other):
        return self.area() > other.area()

    def __eq__(self, other):
        return self.area() == other.area()
