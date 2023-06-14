#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    key = a_dictionary.keys()
    key = sorted(key)
    for i in key:
        print("{}: {}".format(i, a_dictionary[i]))
