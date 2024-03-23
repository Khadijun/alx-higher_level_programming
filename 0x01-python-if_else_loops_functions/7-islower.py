#!/usr/bin/python3
def islower(c):
    ch = 'a'
    while ch <= 'z' or ch <= 'Z':
        if ch == c:
            return True
        ch = chr(ord(ch) + 1)
    return False
