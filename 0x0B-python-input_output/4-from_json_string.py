#!/usr/bin/python3
"""Module from_json_string"""
import json


def from_json_string(my_str):
    """function that returns an object"""
    return json.load(my_str)


