#!/usr/bin/python3
"""Module BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """function of class Rectangle"""
    def __init__(self, width, height):
        """initialization"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        "return str to be printed"
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        "return area"
        return self.__width * self.__height
