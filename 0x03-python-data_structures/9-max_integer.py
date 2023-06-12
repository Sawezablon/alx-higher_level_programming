#!/usr/bin/python3


def max_integer(my_list=[]):
    if len(my_list) != 0:
        for i in range(len(my_list)):
            k = 0
            for j in range(len(my_list)):
                if my_list[i] > my_list[j]:
                    k += 1
            if k == len(my_list) - 1:
                return my_list[1]
    else:
        return None
