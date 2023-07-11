#!/usr/bin/python3
"""Module class Student"""

class Student:
    """method for class"""
    def __init__(self, first_name, last_name, age):
    """Initialization"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """that retrieves a dictionary representation"""
        return self.__dict__
