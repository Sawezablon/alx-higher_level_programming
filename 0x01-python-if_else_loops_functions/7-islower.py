#!/usr/bin/python3

letters = ['abcdefghijklmnopqrstuvwxyz']


def islower(c):
    for i in range(26):
        if (letters[0][i] == c):
            return True
        else:
            return False
