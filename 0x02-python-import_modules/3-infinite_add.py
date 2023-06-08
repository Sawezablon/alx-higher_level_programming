#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    len = len(sys.argv) - 1

    i = 0
    sum = 0
    for arg in sys.argv:
        if i > 0:
            sum += int(sys.argv[i])
        i += 1
    print("{}".format(sum))
