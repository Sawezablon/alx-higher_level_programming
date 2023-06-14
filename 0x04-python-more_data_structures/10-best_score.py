#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max = 0
    keys = a_dictionary.keys()
    for key in keys:
        if a_dictionary[key] > max:
            max = a_dictionary[key]
    for key in keys:
        if a_dictionary[key] == max:
            return key
