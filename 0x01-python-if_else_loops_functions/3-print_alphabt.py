#!/usr/bin/python3
ch = 'a'
while ch <= 'z':
    if ch != 'e' and ch != 'q':
        print('{}'.format(ch), end='')
    ch = chr(ord(ch) + 1)
