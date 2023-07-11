#!/usr/bin/python3
""" that reads stdin line by line and computes metrics:"""


def _status(length, code):
    """print status"""
    print("File size: {}".format(length))
    for i in sorted(code):
        print("{}: {}".format(i, code[i]))


if __name__ == "__main__":
    import sys

    length = 0
    code = {}
    status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    num = 0

    try:
        for line in sys.stdin:
            if num == 10:
                _status(length, code)
                num = 1
            else:
                num += 1

            line = line.split()

            try:
                length += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in status_codes:
                    if code.get(line[-2], -1) == -1:
                        code[line[-2]] = 1
                    else:
                        code[line[-2]] += 1
            except IndexError:
                pass

        _status(length, code)

    except KeyboardInterrupt:
        _status(length, code)
        raise
