#!/usr/bin/python3
"""Module is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """function that returns True if the object is an instance"""
    if isinstance(obj, a_class):
        return True
