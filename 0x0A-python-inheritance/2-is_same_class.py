#!/usr/bin/python3
def is_same_class(obj, a_class):
    """ function that returns True if the object is exactly"""
    if not isinstance(obj, a_class):
        return True
