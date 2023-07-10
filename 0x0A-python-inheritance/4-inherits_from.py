#!/usr/bin/python3
"""Module inherits_from"""


def inherits_from(obj, a_class):
    """function that returns True if the object is an instance"""
    if (type(obj) != a_class):
        return issubclass(type(obj), a_class)
    else:
        return False
