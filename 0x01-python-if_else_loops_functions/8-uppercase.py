#!/usr/bin/python3


def uppercase(str):
    for i in range(len(str)):
        s = ord(str[i])
        if s > 96 and s < 123:
            print("{:c}".format(s - 32), end="" if i < len(str) - 1 else "\n")
        else:
            print("{:c}".format(s), end="" if i < len(str) - 1 else "\n")
