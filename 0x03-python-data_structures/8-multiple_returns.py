#!/usr/bin/python3


def multiple_returns(sentence):
    length = len(sentence)
    if length != 0:
        ch = sentence[0]
        return length, ch
    return length, None
