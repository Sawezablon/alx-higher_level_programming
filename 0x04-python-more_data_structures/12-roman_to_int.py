#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    prev = 0

    for i in roman_string[::-1]:
        value = values[i]
        if value >= prev:
            num += value
        else:
            num -= value
        prev = value

    return num
