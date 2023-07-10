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
