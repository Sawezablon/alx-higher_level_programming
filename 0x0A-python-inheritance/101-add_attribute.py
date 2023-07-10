#!/usr/bin/python3
"""Module add_atribute"""


def add_attribute(obj, name, first_name):
    """add attribute"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, first_name)
