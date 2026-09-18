#!/usr/bin/python3
"""Module that prints a list of integers in reverse order."""


def print_reversed_list_integer(my_list=[]):
    """Print all integers of a list, one per line, in reverse order."""
    for i in reversed(my_list):
        print("{:d}".format(i))
