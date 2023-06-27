#!/usr/bin/bash
def safe_print_list(my_list=[], x=0):
    i = 0
    for list in range(x):
        try:
            print("{}".format(my_list[i]), end='')
            i += 1
        except IndexError:
            break
    print()
    return i
