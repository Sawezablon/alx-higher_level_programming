#!/usr/bin/python3
"""Module save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file"""
    with open(filename, "w") as file:
        json.dump(my_obj, file)
