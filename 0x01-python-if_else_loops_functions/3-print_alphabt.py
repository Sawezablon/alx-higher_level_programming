#!/usr/bin/python3

letters = ['abcdefghijklmnopqrstuvwxyz']
for i in range(26):
    if (letters[0][i] == "q") or (letters[0][i] == "e"):
        continue
    print("{}".format(letters[0][i]), end="")
