#!/usr/bin/python3
"""Create a class Rectangle"""


class Rectangle:
    """instantiatition"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    """Private instance attribute width"""
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """Private instance attribute height"""
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    """Public instance method that returns the rectangle area"""
    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return ((self.__width * 2) + (self.__height * 2))

    """Public instance method that returns the rectangle perimeter"""
    def __str__(self):
        row = "#" * self.__width
        rectangle = (row + "\n") * (self.__height - 1)
        rectangle += row
        return rectangle
