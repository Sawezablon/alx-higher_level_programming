#!/usr/bin/pyhton3
"""rectangle"""
from models.base import Base


class Rectangle(Base):
    """Methods and attribute"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """instantiatition of init method"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Private instance attribute x"""
        return self.__x

    @x.setter
    def x(self, value):
        """x value setter"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Private instance attribute y"""
        return self.__y

    @y.setter
    def y(self, value):
        """y value setter"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Area of rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """Function that prints in stdout the Rectangle"""
        row = (" " * self.__x) + "#" * self.__width
        column = ("\n" * self.__y) + (row + '\n') * (self.__height - 1)
        column += row
        print(column)

    def __str__(self):
        """overriding the __str__ method"""
        return ("[Rectangle] ({}) {}/".format(self.id, self.x)) + \
            ("{} - {}/{}".format(self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """that assigns an argument to each attribute:"""
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        """returns the dictionary representation"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
