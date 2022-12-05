#!/usr/bin/bash
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    for item in reversed(my_list):
        print("{:d}".format(item))
