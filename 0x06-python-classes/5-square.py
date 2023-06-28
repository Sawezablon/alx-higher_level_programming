#!/usr/bin/python3
"""defines a square"""


class Square:
    """functions"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            i = 0
            for i in range(self.__size):
                j = 0
                for j in range(self.__size):
                    print("#", end='')
                print()
