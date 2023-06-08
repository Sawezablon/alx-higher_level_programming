#!/usr/bin/python3


def uppercase():
    j = 65
    for i in range(26):
        print("{:c}".format(j), end='')
        j += 1
    print()
