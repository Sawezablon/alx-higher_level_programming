#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    length = len(sys.argv) - 1
    if length > 0:
        print("{} argument:".format(length))
    else:
        print("{} argument.".format(length))

    for i in range(length):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
