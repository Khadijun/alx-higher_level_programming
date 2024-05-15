#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    for i in range(len(sys.argv) - 1):
        arg = int(sys.argv[i + 1])
        arg1 = int(sys.argv[i + 2])
        result = arg + arg1
        arg ** n = int(sys.argv[i + n])
        if len(sys.argv) - 1 == 0:
            print('{}'.format(0))
        elif len(sys.argv) - 1 == 2:
            print('{} + {} = {}'.format(arg, arg1, result))
        else:
            print('{} + {} + {} = {}'.format(arg, arg1, arg ** n, result))
