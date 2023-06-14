#!/usr/bin/python3


def search_replace(my_list, search, replace):
    new = my_list.copy()
    for i in new:
        if i == search:
            j = new.index(i)
            new.remove(i)
            new.insert(j, replace)
    return new
