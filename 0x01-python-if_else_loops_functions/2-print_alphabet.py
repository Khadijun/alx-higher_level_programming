#!/usr/bin/python3

ch = 'a'
while ch <= 'z':
    print('{}'.format(ch), end='')
    ch = chr(ord(ch) + 1)
