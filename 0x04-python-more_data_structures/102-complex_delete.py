#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new = []
    for key in a_dictionary:
        if a_dictionary[key] == value:
            new.append(key)
    for i in new:
        del a_dictionary[i]
    return a_dictionary
