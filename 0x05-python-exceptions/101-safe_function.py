#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        res = fct(*args)
        return res
    except Exception as E:
        print("Exception: {}".format(E), file=sys.stderr)
        return None
