#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    diff = []
    common = set(set_1) & set(set_2)
    for i in set_1:
        if i not in common:
            diff.append(i)
    for i in set_2:
        if i not in common:
            diff.append(i)
    return diff
