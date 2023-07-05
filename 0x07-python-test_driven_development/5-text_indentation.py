#!/usr/bin/python3
"""
Module text_indentation
function that prints a text with 2 new lines

"""


def text_indentation(text):
    """
    function that prints a text with 2 new lines
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        if text[i] == "." or text[i] == "?":
            print(text[i])
            print()
            i += 1
        elif i == len(text) - 1:
            print(text[i])
            print()
        else:
            print(text[i], end="")
        i += 1
