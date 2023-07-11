#!/usr/bin/python3
"""Module append_after"""


def append_after(filename="", search_string="", new_string=""):
    """function that inserts a line of text to a file"""
    new_txt = ""
    with open(filename) as file:
        for line in file:
            new_txt += line
            if search_string in line:
                new_txt += new_string
    with open(filename, "w") as new_file:
        new_file.write(new_txt)
