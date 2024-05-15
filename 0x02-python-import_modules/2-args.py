#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    if len(sys.argv) - 1 == 0:
        print('{:d} {}.'.format(0, 'arguments'))
    elif len(sys.argv) - 1 == 1:
        print('{:d} {}:'.format(len(sys.argv) - 1, 'argument'))
    else:
        print('{:d} {}:'.format(len(sys.argv) - 1, 'arguments'))
    for i in range(len(sys.argv) - 1):
        arg = sys.argv[i + 1]
        print('{:d}: {}'.format(i + 1, arg))
