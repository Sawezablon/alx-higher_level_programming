#!/usr/bin/python3
"""Module write_file"""


def write_file(filename="", text=""):
    """function that writes a string to a text file"""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
