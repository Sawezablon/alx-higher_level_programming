#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    length = len(sys.argv) - 1
    if length == 0:
        print("{} argument.".format(length))
    elif length == 1:
        print("{} argument:".format(length))
    else:
        print("{} argument:".format(length))

    i = 0
    for arg in sys.argv:
        if i > 0:
            print("{}: {}".format(i, arg))
        i += 1
