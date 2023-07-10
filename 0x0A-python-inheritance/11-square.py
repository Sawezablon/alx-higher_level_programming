#!/usr/bin/python3
"""Module BaseGeometry"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """method for Square class"""
    def __init__(self, size):
        """initialization"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """print string"""
        return "[Square] {}/{}".format(self.__size, self.__size)
