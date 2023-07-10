#!/usr/bin/python3
"""Class module MyInt"""


class MyInt(int):
    """fuction for class"""
    def __eq__(self, value):
        "change != to =="
        return self.real != value

    def __ne__(self, value):
        "change == to !="
        return self.real == value
