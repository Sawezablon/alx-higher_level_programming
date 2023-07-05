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
    for element in ".:?":
        text = (element + "\n\n").join(
            [line.strip(" ") for line in text.split(element)])

    print("{}".format(text), end="")
