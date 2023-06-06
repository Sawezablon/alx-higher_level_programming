#!/usr/bin/env python3
def remove_char_at(str, n):
    if n < 0:
        return str
    elif len(str) < n:
        return str
    else:
        str = str.replace(str[n], '')
        
    return str
