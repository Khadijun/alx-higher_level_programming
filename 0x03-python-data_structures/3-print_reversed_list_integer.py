#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for x in my_list:
        my_list.sort(reverse=True)
        print("{:d}".format(x))
