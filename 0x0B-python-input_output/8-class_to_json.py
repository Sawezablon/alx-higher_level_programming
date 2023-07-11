#!/usr/bin/python3
"""Module class_to_json"""
import json


def class_to_json(obj):
    """function that returns the dictionary description"""
    return obj.__dict__
