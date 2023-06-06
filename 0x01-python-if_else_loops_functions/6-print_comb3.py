#!/usr/bin/python3
j = 1
i = 0
while i < 9:
    while j < 10:
        if (i == 8) and (j == 9):
            print("{}{}".format(i, j))
        else:
            print("{}{}".format(i, j), end=", ")
        j += 1
    i += 1
    j = i + 1
