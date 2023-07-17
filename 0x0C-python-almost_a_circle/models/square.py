#!/usr/bin/python3
"""Module square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Methods and attributes"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialization of init method"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """private instance attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """size value setter"""
        self.width = value
        self.width = value

    def __str__(self):
        """overloading __str__ method """
        return ("[Square] ({}) {}/".format(self.id, self.x)) + \
            ("{} - {}".format(self.y, self.width))

    def update(self, *args, **kwargs):
        """public method  that assigns attributes"""
        if len(args):
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if hasattr(self, key) is True:
                    setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
