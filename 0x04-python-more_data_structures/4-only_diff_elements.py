#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    diff = []
    common = []
    for i in set_1:
        for j in set_2:
            if i == j:
                common.append(i)
    for i in set_1:
        for j in common:
            if i != j:
                diff.append(i)
    for i in set_2:
        for j in common:
            if i != j:
                diff.append(i)
    return diff
