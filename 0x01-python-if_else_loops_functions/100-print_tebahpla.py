#!/usr/bin/python3
z = 122
for i in range(26):
    print("{:c}".format(z) if i % 2 == 0 else "{:c}".format(z - 32), end="")
    z -= 1
