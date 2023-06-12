#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    zero = (0,)
    for i in range(2):
        if len(tuple_b) < 2:
            tuple_b += zero
        if len(tuple_a) < 2:
            tuple_a += zero
    next = ()
    for i in range(2):
        next += (tuple_a[i] + tuple_b[i],)
    return (next)
