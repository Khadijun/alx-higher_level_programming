#!/usr/bin/python3
for n in range(0, 10):
    print('{:02d}'.format(n), end=', ')
for n in range(12, 90):
    if n > 11 and n < 20:
        print('{}'.format(n), end=', ')
    if n > 22 and n < 30:
        print('{}'.format(n), end=', ')
    if n > 33 and n < 40:
        print('{}'.format(n), end=', ')
    if n > 44 and n < 50:
        print('{}'.format(n), end=', ')
    if n > 55 and n < 60:
        print('{}'.format(n), end=', ')
    if n > 66 and n < 70:
        print('{}'.format(n), end=', ')
    if n > 77 and n < 80:
        print('{}'.format(n), end=', ')
    if n > 88 and n < 90:
        print('{}'.format(n), end='\n')
