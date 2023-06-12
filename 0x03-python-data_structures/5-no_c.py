#!/usr/bin/python3


def no_c(my_string):
    test = ""
    for i in my_string:
        if i == "c" or i == "C":
            continue
        test += i
    return test
