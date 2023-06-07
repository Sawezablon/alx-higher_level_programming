#!/usr/bin/python3


def upper(ch):
    new = ord(ch)
    if new > 96 and new < 123:
        return new - 32
    else:
        return new


def uppercase(str):
    empty = ""
    for i in range(len(str)):
        empty += "%c" % upper(str[i])
    print("{:s}".format(empty))
