#!/usr/bin/python3
"""Module BaseGeometry"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """method for Square class"""
    def __init__(self, size):
        """initialization"""
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
